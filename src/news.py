from __future__ import annotations
from datetime import datetime, timedelta, timezone
import hashlib
import os
import re
from urllib.parse import urlsplit, urlunsplit
from .providers.http import Client
from .models import Stock, utcnow

CATEGORIES = {'Earnings':r'earnings|quarterly results|profit report', 'Guidance':r'guidance|outlook',
    'Acquisitions':r'acquisition|merger|acquire', 'Contracts':r'contract|order win',
    'Management changes':r'chief executive|resign|appoint|CEO', 'Regulations':r'regulator|regulatory|SEBI|SEC investigation',
    'Litigation':r'lawsuit|litigation|court', 'Debt and capital raising':r'debt|capital raising|offering|bankruptcy|insolvency',
    'Dividends and buybacks':r'dividend|buyback|repurchase', 'Product announcements':r'launch|product'}


def classify(items: list[dict], stock: Stock, name: str, days: int, now: datetime | None = None) -> dict:
    now=now or datetime.now(timezone.utc)
    accepted={}
    names=[t.lower() for t in re.findall(r'[A-Za-z]{3,}',name) if t.lower() not in {'limited','ltd','inc','corporation','company','the'}]
    for item in items:
        title=str(item.get('headline','')).strip()
        snippet=str(item.get('summary','')).strip()
        try:
            published=datetime.fromisoformat(item['published_at'].replace('Z','+00:00'))
            if published.tzinfo is None or not now-timedelta(days=days)<=published<=now:
                continue
            url=urlsplit(item['url'])
            if url.scheme not in {'https','http'} or not url.netloc:
                continue
        except (KeyError,ValueError,TypeError):
            continue
        # Provider's symbol-bound endpoint is necessary but company identity is also checked.
        text=(title+' '+snippet).lower()
        if not any(re.search(r'\b'+re.escape(token)+r'\b',text) for token in names):
            continue
        canonical=urlunsplit((url.scheme,url.netloc,url.path,url.query,''))
        dedupe=re.sub(r'[^a-z0-9]','',title.lower())
        if not dedupe:
            continue
        category=next((k for k,p in CATEGORIES.items() if re.search(p,title,re.I)),'Other material developments')
        # Headline/snippet access cannot establish materiality, direction, or confirmation.
        # Structured primary-source event facts may be supplied by a vetted filing adapter.
        verified=item.get('primary',False) and item.get('confirmed',False) and bool(item.get('evidence_quote'))
        critical=verified and item.get('event_code') in {'bankruptcy_filed','trading_suspended','auditor_adverse_opinion','payment_default','bankruptcy_or_receivership','financial_statement_nonreliance'}
        sentiment='negative' if critical else item.get('impact_direction','uncertain') if verified and item.get('impact_direction') in {'positive','negative','neutral'} else 'uncertain'
        record={'retrieved_at':utcnow(),'id':hashlib.sha256(dedupe.encode()).hexdigest()[:16], 'headline':title,'publisher':item.get('publisher','Unknown'),
            'published_at':published.isoformat(),'url':canonical,'category':category,'summary':snippet or title,
            'access':'snippet' if snippet else 'headline only','sentiment':sentiment,
            'impact':'Critical solvency/governance review' if critical else 'Potential '+category.lower()+' impact; review original source',
            'confirmation':'confirmed structured primary event' if verified else 'unverified; not independently confirmed',
            'critical':critical,'verified':verified,'primary':bool(item.get('primary'))}
        if dedupe not in accepted or record['primary']:
            accepted[dedupe]=record
    events=sorted(accepted.values(),key=lambda x:(not x['primary'],-datetime.fromisoformat(x['published_at']).timestamp()))
    critical=any(x['critical'] for x in events)
    return {'items':events,'overlay':'Critical event requiring review' if critical else 'Negative catalyst' if any(x['verified'] and x['sentiment']=='negative' for x in events) else 'Positive catalyst' if any(x['verified'] and x['sentiment']=='positive' for x in events) else 'No material catalyst',
            'critical':critical,'coverage':'headline/snippet only; material catalysts not verified',
            'note':'No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.'}


def fetch(client: Client, stock: Stock, name: str, days: int) -> dict:
    raw=[]
    errors=[]
    now=datetime.now(timezone.utc)
    key=os.getenv('FINNHUB_API_KEY')
    if key:
        try:
            data,_=client.get('https://finnhub.io/api/v1/company-news',{'symbol':stock.ticker,'from':(now-timedelta(days=days)).date().isoformat(),'to':now.date().isoformat()}, {'X-Finnhub-Token':key},interval=1.1)
            for row in data:
                raw.append({'headline':row['headline'],'summary':row.get('summary',''),'publisher':row.get('source'),
                    'url':row['url'],'published_at':datetime.fromtimestamp(row['datetime'],timezone.utc).isoformat()})
        except Exception:
            errors.append('Finnhub unavailable')
    if stock.exchange in {'NASDAQ','NYSE'}:
        try:
            from .providers.sec import filings
            raw.extend(filings(client, stock.ticker))
        except Exception:
            errors.append('SEC filings unavailable')
    try:
        import yfinance as yf
        for entry in yf.Ticker(stock.ticker).get_news(count=30):
            row=entry.get('content',{})
            raw.append({'headline':row.get('title',''),'summary':row.get('summary',''),
                'publisher':row.get('provider',{}).get('displayName'), 'published_at':row.get('pubDate'),
                'url':(row.get('canonicalUrl') or {}).get('url','')})
    except Exception:
        errors.append('Yahoo news unavailable')
    result=classify(raw,stock,name,days,now)
    result['errors']=errors
    from .llm import summarize
    result['llm']=summarize(result['items'],client.cache/'llm')
    return result
