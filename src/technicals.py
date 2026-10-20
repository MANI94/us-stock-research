from __future__ import annotations
import numpy as np
import pandas as pd
from .models import Metric


def analyze(bars: pd.DataFrame, benchmark: pd.DataFrame | None = None) -> dict:
    if bars.empty:
        return {'metrics':{},'trend':'N/A','error':'No adjusted OHLCV'}
    bars = bars.sort_index()
    if bars.index.has_duplicates or not {'Open','High','Low','Close','Volume'} <= set(bars):
        raise ValueError('Invalid OHLCV schema')
    if not np.isfinite(bars[['Open','High','Low','Close','Volume']].to_numpy()).all():
        raise ValueError('Non-finite bars')
    if (bars[['Open','High','Low','Close']]<=0).any().any() or (bars.Volume<0).any() or (bars.High<bars.Low).any():
        raise ValueError('Invalid OHLCV values')
    if bars.index[-1].date()>pd.Timestamp.now(tz='UTC').date():
        raise ValueError('Future market bar')
    c,h,l,v = bars.Close,bars.High,bars.Low,bars.Volume
    metrics = {}
    def put(name,value,formula):
        metrics[name] = Metric(value=value,unit='ratio' if name in {'rsi14','volume_ratio','momentum_63','relative_strength_63'} else bars.attrs.get('currency','quote currency'),
            source=bars.attrs.get('source','adjusted OHLCV'), period=str(bars.index[-1].date()),
            retrieved_at=bars.attrs.get('retrieved_at'), freshness='pending_calendar_check',formula=formula,inputs=['adjusted OHLCV']).model_dump()
    for window in (20,50,100,200):
        put(f'sma{window}',c.rolling(window).mean().iloc[-1],f'mean last {window} adjusted closes')
    for window in (20,50):
        put(f'ema{window}',c.ewm(span=window,adjust=False,min_periods=window).mean().iloc[-1],f'EMA span {window}')
    delta = c.diff()
    # Wilder smoothing seeded with the first arithmetic mean.
    def wilder(series, period):
        result = pd.Series(np.nan,index=series.index)
        if len(series)>=period:
            result.iloc[period-1]=series.iloc[:period].mean()
            for i in range(period,len(series)):
                result.iloc[i]=(result.iloc[i-1]*(period-1)+series.iloc[i])/period
        return result
    gains = wilder(delta.iloc[1:].clip(lower=0),14)
    losses = wilder((-delta.iloc[1:]).clip(lower=0),14)
    rsi = 100-100/(1+gains/losses.replace(0,np.nan))
    rsi = rsi.mask((losses==0)&(gains>0),100).mask((losses==0)&(gains==0),50)
    put('rsi14',rsi.iloc[-1] if len(rsi) else None,'Wilder RSI 14; flat market = 50')
    macd=c.ewm(span=12,adjust=False,min_periods=12).mean()-c.ewm(span=26,adjust=False,min_periods=26).mean()
    signal=macd.ewm(span=9,adjust=False,min_periods=9).mean()
    put('macd',macd.iloc[-1],'EMA12 - EMA26')
    put('macd_signal',signal.iloc[-1],'EMA9 of MACD')
    put('macd_histogram',(macd-signal).iloc[-1],'MACD - signal')
    mean,std=c.rolling(20).mean(),c.rolling(20).std(ddof=0)
    put('bollinger_lower',(mean-2*std).iloc[-1],'SMA20 - 2 population std20')
    put('bollinger_upper',(mean+2*std).iloc[-1],'SMA20 + 2 population std20')
    tr=pd.concat([h-l,(h-c.shift()).abs(),(l-c.shift()).abs()],axis=1).max(axis=1)
    atr=wilder(tr,14).iloc[-1]
    put('atr14',atr,'Wilder mean true range14')
    put('volume_ratio',v.iloc[-1]/v.iloc[-21:-1].mean() if len(v)>20 and v.iloc[-21:-1].mean()>0 else None,'Latest volume / previous 20 sessions mean')
    put('high_52w',h.iloc[-252:].max() if len(h)>=252 else None,'Maximum adjusted high last 252 sessions')
    put('low_52w',l.iloc[-252:].min() if len(l)>=252 else None,'Minimum adjusted low last 252 sessions')
    put('momentum_63',c.iloc[-1]/c.iloc[-64]-1 if len(c)>63 else None,'close / close63 sessions ago - 1')
    rs=None
    if benchmark is not None and not benchmark.empty:
        left=pd.Series(c.to_numpy(),index=pd.to_datetime(c.index.date))
        right=pd.Series(benchmark.Close.to_numpy(),index=pd.to_datetime(benchmark.index.date))
        joined=pd.concat([left,right],axis=1).dropna()
        if len(joined)>=64:
            rs=(joined.iloc[-1,0]/joined.iloc[-64,0])/(joined.iloc[-1,1]/joined.iloc[-64,1])-1
    put('relative_strength_63',rs,'stock 63-session return factor / benchmark factor - 1; aligned dates')
    price=float(c.iloc[-1])
    # Confirmed five-bar pivots, excludes last two unconfirmed bars.
    lows=[float(l.iloc[i]) for i in range(max(2,len(l)-63),len(l)-2) if l.iloc[i]==l.iloc[i-2:i+3].min() and l.iloc[i]<price]
    highs=[float(h.iloc[i]) for i in range(max(2,len(h)-63),len(h)-2) if h.iloc[i]==h.iloc[i-2:i+3].max() and h.iloc[i]>price]
    support=max(lows) if lows else None
    resistance=min(highs) if highs else None
    invalidation=support-float(atr) if support and np.isfinite(atr) else None
    rr=(resistance-price)/(price-invalidation) if resistance and invalidation and 0<invalidation<price else None
    weekly=c.resample('W-FRI').last()
    # Drop the in-progress weekly bar (Friday close is usable).
    if c.index[-1].weekday()!=4:
        weekly=weekly.iloc[:-1]
    weekly_trend='up' if len(weekly)>=20 and weekly.iloc[-1]>weekly.iloc[-20:].mean() else 'down' if len(weekly)>=20 else 'N/A'
    sma50,sma200=metrics['sma50']['value'],metrics['sma200']['value']
    trend='up' if sma50 and sma200 and price>sma50>sma200 else 'down' if sma50 and sma200 and price<sma50<sma200 else 'mixed' if sma200 else 'N/A'
    return {'metrics':metrics,'trend':trend,'weekly_trend':weekly_trend,'support':support,'resistance':resistance,
            'entry_range':[support,support+float(atr)*0.5] if support and np.isfinite(atr) else None,
            'invalidation':invalidation if invalidation and invalidation>0 else None,'risk_reward':rr,
            'support_zone':[support-float(atr)*0.25,support+float(atr)*0.25] if support and np.isfinite(atr) else None,
            'resistance_zone':[resistance-float(atr)*0.25,resistance+float(atr)*0.25] if resistance and np.isfinite(atr) else None,
            'method':'Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts.'}
