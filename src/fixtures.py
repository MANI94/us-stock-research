"""Explicit synthetic data for offline examples; never used in live runs."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from .models import Metric,utcnow
from .providers import Bundle
from .news import classify


def fixture_bundle(path, stock):
    fixture=json.loads(Path(path).read_text())
    settings=fixture.get(stock.ticker,fixture['default'])
    currency='INR' if stock.exchange in {'NSE','BSE'} else 'USD'
    now=pd.Timestamp.now(tz='UTC')
    index=pd.bdate_range(end=now.normalize()-pd.Timedelta(days=1),periods=520)
    close=100+np.arange(520)*.12+np.sin(np.arange(520)/4)*4
    bars=pd.DataFrame({'Open':close-.3,'High':close+2,'Low':close-2,'Close':close,'Volume':1000000+np.arange(520)*100},index=index)
    bars.attrs.update(source='SYNTHETIC FIXTURE adjusted OHLCV',retrieved_at=utcnow(),currency=currency)
    data=Bundle(settings.get('name',stock.ticker+' Synthetic Company'),currency,settings.get('sector','Technology'),settings.get('industry','Software'),bars=bars)
    for year in range(6):
        scale=1.08**(5-year)
        data.statements.append({'period':f'{now.year-year-1}-12-31','source':'SYNTHETIC FIXTURE','retrieved_at':utcnow(),'currency':currency,
            'revenue':1000000*scale,'net_income':150000*scale,'eps':1.5*scale,'ebit':200000*scale,'interest':10000,
            'equity':900000*scale,'assets':1600000*scale,'current_liabilities':300000,'current_assets':600000,
            'debt':200000,'cash':300000,'fcf':140000*scale,'ocf':180000*scale,'capex':-40000*scale,'shares':100000,'dividends':-20000})
    data.metrics={'price':Metric(value=float(close[-1]),unit=currency,source='SYNTHETIC FIXTURE',period=index[-1].isoformat(),freshness='fresh'),
        'market_cap':Metric(value=float(close[-1])*100000,unit=currency,source='SYNTHETIC FIXTURE',period=index[-1].isoformat(),freshness='fresh')}
    if settings.get('missing'):
        data.statements=[];data.metrics={}
    return data,bars.copy(),classify([],stock,data.name,7)
