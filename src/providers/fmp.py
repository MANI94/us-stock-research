from __future__ import annotations
import os
from datetime import datetime, timezone, timedelta
import statistics
import pandas as pd
from . import Bundle
from .http import Client
from ..models import Metric, Stock


class FMP:
    name = 'fmp'

    def __init__(self, client: Client):
        self.client = client

    def history(self, symbol: str) -> pd.DataFrame:
        data,stamp=self.client.get('https://financialmodelingprep.com/stable/historical-price-eod/dividend-adjusted',
            {'symbol':symbol,'from':(datetime.now(timezone.utc)-timedelta(days=760)).date().isoformat()},
            {'apikey':os.environ['FMP_API_KEY']})
        frame=pd.DataFrame(data).rename(columns={'adjOpen':'Open','adjHigh':'High','adjLow':'Low','adjClose':'Close','volume':'Volume'})
        frame.index=pd.to_datetime(frame.pop('date'),utc=True)
        frame=frame[['Open','High','Low','Close','Volume']].sort_index()
        frame.attrs.update(source='FMP dividend/split adjusted OHLCV',retrieved_at=stamp)
        return frame

    def fetch(self, stock: Stock) -> Bundle:
        key = os.environ.get('FMP_API_KEY')
        if not key:
            raise ValueError('FMP key not configured')
        symbol = stock.ticker
        if stock.exchange in {'NSE','BSE'}:
            root=stock.ticker.rsplit('.',1)[0]
            directory,_=self.client.get('https://financialmodelingprep.com/stable/search-symbol',{'query':root},{'apikey':key})
            matches=[r for r in directory if r.get('exchange')==stock.exchange and r.get('symbol','').split('.')[0]==root]
            if len(matches)!=1:
                raise ValueError('Cannot unambiguously resolve Indian FMP symbol')
            symbol=matches[0]['symbol']
        def get(endpoint: str, **extra):
            return self.client.get('https://financialmodelingprep.com/stable/' + endpoint,
                {'symbol': symbol, **extra}, {'apikey': key})
        profile, stamp = get('profile')
        if not isinstance(profile, list) or not profile:
            raise ValueError('Profile unavailable')
        p = profile[0]
        currency = p.get('currency')
        if currency not in {'USD','INR'}:
            raise ValueError('Unsupported currency')
        result = Bundle(p.get('companyName', symbol), currency, p.get('sector', 'Unknown'), p.get('industry', 'Unknown'))
        try:
            quote, fetched = get('quote')
            q=quote[0]
            observed=datetime.fromtimestamp(q['timestamp'],timezone.utc).isoformat()
            for metric,field in {'price':'price','market_cap':'marketCap'}.items():
                result.metrics[metric]=Metric(value=q.get(field),unit=currency,source='FMP quote',period=observed,retrieved_at=fetched,freshness='unknown')
        except Exception:
            result.warnings.append('FMP quote unavailable')
        try:
            result.bars=self.history(symbol)
            result.bars.attrs['currency']=currency
        except Exception:
            result.warnings.append('FMP adjusted OHLCV unavailable')
        mappings = {'income-statement': {'revenue':'revenue','net_income':'netIncome','eps':'epsDiluted',
            'ebit':'ebit','interest':'interestExpense','operating_income':'operatingIncome','shares':'weightedAverageShsOutDil'},
            'balance-sheet-statement': {'equity':'totalStockholdersEquity','debt':'totalDebt','cash':'cashAndCashEquivalents',
            'assets':'totalAssets','current_liabilities':'totalCurrentLiabilities','current_assets':'totalCurrentAssets',
            'inventory':'inventory','receivables':'netReceivables'},
            'cash-flow-statement': {'ocf':'operatingCashFlow','capex':'capitalExpenditure','fcf':'freeCashFlow','dividends':'commonDividendsPaid'}}
        rows = {}
        for endpoint, mapping in mappings.items():
            try:
                data, fetched = get(endpoint, limit=6, period='annual')
                for entry in data:
                    if entry.get('reportedCurrency') != currency:
                        result.warnings.append('Statement currency mismatch; row rejected')
                        continue
                    date = entry['date']
                    row = rows.setdefault(date, {'period':date,'currency':currency,'source':'FMP','retrieved_at':fetched})
                    row.update({k:entry[v] for k,v in mapping.items() if entry.get(v) is not None})
            except Exception:
                result.warnings.append(endpoint + ': unavailable')
        result.statements = [rows[k] for k in sorted(rows, reverse=True)]
        try:
            data, fetched = get('ratios-ttm')
            if data:
                for name, field in {'pe':'priceToEarningsRatioTTM','pb':'priceToBookRatioTTM',
                    'ev_ebitda':'enterpriseValueMultipleTTM','payout':'dividendPayoutRatioTTM'}.items():
                    result.metrics[name] = Metric(value=data[0].get(field), source='FMP', period='Snapshot '+fetched, retrieved_at=fetched, freshness='snapshot')
        except Exception:
            result.warnings.append('FMP ratios unavailable')
        try:
            historical,fetched=get('ratios',period='annual',limit=6)
            observations=[r for r in historical if r.get('priceToEarningsRatio') is not None and r['priceToEarningsRatio']>0 and r.get('date')]
            if len(observations)>=3:
                values=[r['priceToEarningsRatio'] for r in observations]
                for metric,number in {'historical_pe_median':statistics.median(values),'historical_pe_min':min(values),'historical_pe_max':max(values)}.items():
                    result.metrics[metric]=Metric(value=number,source='FMP annual ratios',period=', '.join(r['date'] for r in observations),retrieved_at=fetched,freshness='historical',formula='Historical fiscal-year-end annual PE summary',inputs=[str(r) for r in observations])
        except Exception:
            result.warnings.append('Historical PE unavailable')
        try:
            peer_data,_=get('stock-peers')
            candidates=peer_data[0].get('peersList',[]) if peer_data and 'peersList' in peer_data[0] else [r['symbol'] for r in peer_data if r.get('symbol')!=symbol]
            peers=[]
            for peer in candidates[:3]:
                peer_profile,_=self.client.get('https://financialmodelingprep.com/stable/profile',{'symbol':peer},{'apikey':key})
                if not peer_profile or peer_profile[0].get('industry')!=result.industry:
                    continue
                ratios,fetched=self.client.get('https://financialmodelingprep.com/stable/ratios-ttm',{'symbol':peer},{'apikey':key})
                pe=ratios[0].get('priceToEarningsRatioTTM') if ratios else None
                if pe and pe>0:
                    peers.append((peer,pe))
                    result.metrics['peer_'+peer+'_pe']=Metric(value=pe,source='FMP ratios-ttm',period='Snapshot '+fetched,retrieved_at=fetched,freshness='snapshot')
            own=result.metrics.get('pe')
            if len(peers)>=3 and own and own.value and own.value>0:
                median=statistics.median(v for _,v in peers)
                result.metrics['peer_pe_discount']=Metric(value=1-own.value/median,source='FMP provider-selected same-industry peers',period='Snapshot '+fetched,retrieved_at=fetched,freshness='snapshot',formula='1 - stock PE / median positive peer PE',inputs=[str(peers)])
        except Exception:
            result.warnings.append('Peer comparison unavailable; requires 3 same-industry peers')
        return result
