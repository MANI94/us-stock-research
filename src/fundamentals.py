from __future__ import annotations
from datetime import date
from .providers import Bundle
from .models import Metric


def analyze(data: Bundle) -> dict[str, Metric]:
    metrics = dict(data.metrics)
    rows = sorted(data.statements, key=lambda r:r['period'], reverse=True)
    if not rows:
        return metrics
    row = rows[0]
    age = (date.today() - date.fromisoformat(row['period'])).days
    def put(name, value, formula, inputs, unit='ratio'):
        metrics[name] = Metric(value=value, unit=unit, source=row['source'], period=row['period'],
            retrieved_at=row['retrieved_at'], freshness='fresh' if 0 <= age <= 550 else 'stale', formula=formula, inputs=inputs)
    def ratio(name, a, b, formula, positive=True):
        denominator = row.get(b)
        put(name, row[a]/denominator if row.get(a) is not None and denominator is not None and (denominator > 0 if positive else denominator != 0) else None, formula, [a,b])
    if 'fcf' not in row and row.get('ocf') is not None and row.get('capex') is not None:
        row['fcf'] = row['ocf'] - abs(row['capex'])
    for name, a, b in [('roe','net_income','equity'),('roa','net_income','assets'),('operating_margin','operating_income','revenue'),
        ('net_margin','net_income','revenue'),('debt_equity','debt','equity'),('current_ratio','current_assets','current_liabilities'),
        ('fcf_conversion','fcf','net_income'),('interest_coverage','ebit','interest')]:
        ratio(name,a,b,f'{a} / {b}')
    capital = row.get('assets',0) - row.get('current_liabilities',0)
    put('roce', row['ebit']/capital if row.get('ebit') is not None and 'assets' in row and 'current_liabilities' in row and capital > 0 else None,
        'EBIT / (assets - current liabilities)', ['ebit','assets','current_liabilities'])
    for key in ('fcf','eps','equity','shares','debt','cash'):
        put(key,row.get(key),'Latest annual statement value',[key],data.currency if key != 'shares' else 'shares')
    for years in (1,3,5):
        old = next((r for r in rows if abs((date.fromisoformat(row['period'])-date.fromisoformat(r['period'])).days/365.25-years)<0.25),None)
        for key in ('revenue','eps'):
            start, end = (old or {}).get(key), row.get(key)
            value = (end/start)**(1/years)-1 if start is not None and start>0 and end is not None and end>0 else None
            put(f'{key}_growth_{years}y',value,f'({key}_latest / {key}_{years}y_ago)^(1/{years}) - 1',[key, old['period'] if old else 'missing'])
    earnings = [r['net_income'] for r in rows if r.get('net_income') is not None]
    put('earnings_consistency',sum(x>0 for x in earnings)/len(earnings) if len(earnings)>=3 else None,'Profitable annual periods / observed annual periods',['net_income_history'])
    dividends = row.get('dividends')
    put('dividend_fcf_coverage',row['fcf']/abs(dividends) if dividends and row.get('fcf') is not None else None,'FCF / absolute cash dividends',['fcf','dividends'])
    if len(earnings)>=3:
        import statistics
        average = statistics.mean(earnings)
        put('earnings_volatility',statistics.pstdev(earnings)/abs(average) if average else None,'std annual net income / abs mean',['net_income_history'])
    return metrics
