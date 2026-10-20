from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import logging
import os
from pathlib import Path
from zoneinfo import ZoneInfo
import yaml
import pandas as pd
from .config import load_config
from .models import Metric, utcnow
from .providers import collect
from .providers.fmp import FMP
from .providers.yahoo import Yahoo
from .providers.http import Client
from .providers.cache import CachedProvider
from . import fundamentals, technicals, valuation, risk, news, scoring, decisions, reporting, storage
from .market import market_status


class StructuredFormatter(logging.Formatter):
    def format(self,record):
        return json.dumps({'level':record.levelname,'event':record.getMessage(),
            **{k:getattr(record,k) for k in ('ticker','provider','error_type') if hasattr(record,k)}})


def run(config_path: str, root: Path, override: str='', fixture: Path | None=None) -> dict:
    root.mkdir(parents=True,exist_ok=True)
    config=load_config(config_path,override)
    policy=yaml.safe_load((Path(config_path).parent/'scoring.yml').read_text())
    now=datetime.now(timezone.utc)
    local=now.astimezone(ZoneInfo(config.settings.report_timezone))
    old=storage.previous(root/'history',local.date().isoformat())
    old_stocks={s['ticker']:s for s in old.get('stocks',[])}
    client=Client(root/'.cache')
    provider_map={'fmp':FMP(client),'yahoo':Yahoo()}
    providers=[CachedProvider(provider_map[p], root/'.cache'/'financial') for p in config.settings.providers if p!='yahoo' or config.settings.allow_yahoo]
    fx=None
    if fixture is None and config.settings.allow_yahoo:
        try:
            import yfinance as yf
            fx_bars=yf.Ticker('INR=X').history(period='1mo',auto_adjust=True)
            if not fx_bars.empty:
                fx=Metric(value=fx_bars.Close.iloc[-1],unit='INR/USD',source='Yahoo Finance INR=X',period=str(fx_bars.index[-1].date()),
                    freshness='fresh' if (now.date()-fx_bars.index[-1].date()).days<=4 else 'stale')
        except Exception:
            logging.warning('fx_unavailable')
    results=[]
    for stock in config.stocks:
        base={'ticker':stock.ticker,'exchange':stock.exchange,'name':stock.ticker,'price':None,'score':None,'fair_value':None,'currency':None}
        try:
            if fixture:
                from .fixtures import fixture_bundle
                data,benchmark,news_data=fixture_bundle(fixture,stock)
            else:
                data=collect(stock,providers)
                benchmark=pd.DataFrame()
                if config.settings.allow_yahoo:
                    try:
                        import yfinance as yf
                        benchmark=yf.Ticker('^NSEI' if stock.exchange=='NSE' else '^BSESN' if stock.exchange=='BSE' else '^GSPC').history(period='2y',auto_adjust=True)
                    except Exception:
                        data.warnings.append('Benchmark unavailable')
                if benchmark.empty and os.getenv('FMP_API_KEY'):
                    try:
                        benchmark=provider_map['fmp'].history('^NSEI' if stock.exchange=='NSE' else '^BSESN' if stock.exchange=='BSE' else '^GSPC')
                    except Exception:
                        data.warnings.append('FMP benchmark unavailable')
                news_data=news.fetch(client,stock,data.name,config.settings.news_lookback_days)
            metrics=fundamentals.analyze(data)
            technical=technicals.analyze(data.bars,benchmark)
            last_session=str(data.bars.index[-1].date()) if not data.bars.empty else None
            market=market_status(stock.exchange,last_session,now)
            for key,value in technical['metrics'].items():
                m=Metric.model_validate(value)
                m.freshness='stale' if market['stale'] else 'fresh'
                metrics[key]=m
            if not data.bars.empty:
                # Yahoo auto-adjusted historical close is used for indicators only. Quote price retains raw nominal basis.
                price=metrics.get('price')
                if price and price.period:
                    try:
                        observed=datetime.fromisoformat(price.period).date().isoformat()
                        price.freshness='fresh' if market['expected_session'] and market['expected_session']<=observed<=now.date().isoformat() else 'stale'
                    except ValueError:
                        price.freshness='unknown'
            profile=scoring.sector_profile(data.sector,data.industry)
            expected={'nim','gnpa','nnpa','capital_adequacy','credit_cost','funding_stability','recurring_revenue_ratio',
                'capacity_utilization','normalized_roe','promoter_ownership','pledge_ratio','audit_clear','dilution_risk',
                'competitive_advantage','regulatory_exposure','concentration_risk','historical_pe_median','historical_pe_min','historical_pe_max'}
            for key in expected:
                metrics.setdefault(key,Metric(source='Not available from configured providers'))
            val=valuation.analyze(data,metrics,policy)
            for key,value in val['metrics'].items():
                metrics[key]=Metric.model_validate(value)
            metrics['margin_of_safety']=Metric(value=val['margin_of_safety'],source='DCF scenarios',freshness='derived',formula='1 - price/base fair value',inputs=['price','fcf','shares'])
            def flag(key,value,formula):
                metrics[key]=Metric(value=value,source='adjusted OHLCV derived',period=last_session,freshness='stale' if market['stale'] else 'derived',formula=formula)
            price=metrics.get('price',Metric(source='N/A')).value
            for n in (50,200):
                sma=metrics.get(f'sma{n}')
                flag(f'above_sma{n}',float(price>sma.value) if price and sma and sma.value else None,f'price > SMA{n}')
            hist=metrics.get('macd_histogram')
            flag('macd_positive',float(hist.value>0) if hist and hist.value is not None else None,'MACD histogram > 0')
            flag('weekly_up',float(technical.get('weekly_trend')=='up') if technical.get('weekly_trend') in {'up','down'} else None,'last completed weekly close > weekly SMA20')
            risks=risk.analyze(metrics,news_data,profile=='financial')
            scores=scoring.score(metrics,profile,policy)
            essential=all(metrics.get(k) and metrics[k].value is not None and metrics[k].freshness not in {'stale','unknown'} for k in ('price','roe','eps'))
            if profile=='financial':
                essential=essential and all(metrics.get(k) and metrics[k].value is not None for k in ('capital_adequacy','nnpa'))
            decision=decisions.decide(scores,val,risks,news_data,market['stale'],essential,config.settings.investment_horizon,config.settings.risk_profile)
            fair=val['fair_values']['base']['value'] if val['fair_values'] else None
            base.update(name=data.name,currency=data.currency,price=price,price_timestamp=metrics.get('price',Metric(source='N/A')).period,
                score=scores['total'],scores=scores,verdict=decision['verdict'],fair_value=fair,decision=decision,valuation=val,
                technicals={k:v for k,v in technical.items() if k!='metrics'},news=news_data,risk=risks,market=market,
                metrics={k:v.model_dump() for k,v in metrics.items()},statements=data.statements,
                provider_conflicts=data.candidates,warnings=data.warnings,news_ids=[n['id'] for n in news_data['items']])
            base['converted_prices']={currency:price if currency==data.currency else price*fx.value if fx and fx.freshness=='fresh' and price and data.currency=='USD' else price/fx.value if fx and fx.freshness=='fresh' and price and data.currency=='INR' else None for currency in config.settings.reporting_currencies}
            base['changes']=storage.changes(base,old_stocks.get(stock.ticker,{}))
        except Exception as error:
            logging.error('ticker_failed',extra={'ticker':stock.ticker,'error_type':type(error).__name__})
            base.update(verdict='INSUFFICIENT DATA',error='Ticker analysis unavailable: '+type(error).__name__)
        results.append(base)
    report={'generated_at':local.isoformat(),'report_date':local.date().isoformat(),'mode':'SYNTHETIC FIXTURE — NOT LIVE DATA' if fixture else 'Live provider research',
        'settings':config.settings.model_dump(),'fx':fx.model_dump() if fx else None,'artifact_url':os.getenv('REPORT_ARTIFACT_URL',''),'stocks':results}
    reporting.render(report,root)
    return report


def main():
    handler=logging.StreamHandler()
    handler.setFormatter(StructuredFormatter())
    logging.basicConfig(handlers=[handler],level=logging.INFO)
    # Third-party HTTP libraries must not emit credential-bearing request URLs.
    for name in ('yfinance','urllib3','requests','curl_cffi'):
        logging.getLogger(name).disabled=True
    parser=argparse.ArgumentParser()
    parser.add_argument('--config',default='config/stocks.yml')
    parser.add_argument('--output',default='.')
    parser.add_argument('--tickers',default=os.getenv('TICKER_OVERRIDE',''))
    parser.add_argument('--fixture',type=Path)
    args=parser.parse_args()
    report=run(args.config,Path(args.output),args.tickers,args.fixture)
    if all('error' in s for s in report['stocks']):
        raise SystemExit(2)


if __name__=='__main__':
    main()
