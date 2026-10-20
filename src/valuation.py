from __future__ import annotations
from decimal import Decimal
from .models import Metric
from .providers import Bundle


def analyze(data: Bundle, metrics: dict[str, Metric], policy: dict) -> dict:
    def value(key):
        m=metrics.get(key)
        return m.value if m and m.freshness not in {'stale','unknown'} else None
    price,cap,fcf,eps=value('price'),value('market_cap'),value('fcf'),value('eps')
    derived={}
    def put(key,number,formula,inputs):
        derived[key]=Metric(value=number,source='calculated',period=metrics.get('fcf',Metric(source='N/A')).period,
            formula=formula,inputs=inputs,freshness='derived').model_dump()
    pe=value('pe')
    put('earnings_yield',1/pe if pe and pe>0 else None,'1 / trailing PE',['pe'])
    put('fcf_yield',fcf/cap if fcf is not None and cap and cap>0 else None,'annual FCF / market cap',['fcf','market_cap'])
    growth=value('eps_growth_3y')
    put('peg',pe/(growth*100) if pe and pe>0 and growth and growth>0 else None,'PE / historical EPS CAGR in percentage points; historical proxy, not forecast',['pe','eps_growth_3y'])
    result={'metrics':derived,'fair_values':None,'margin_of_safety':None,'accumulation_range':None,
        'verdict':'N/A','confidence':'low','historical_pe':{k:value(k) for k in ('historical_pe_median','historical_pe_min','historical_pe_max')},'sector_relative_pe':value('peer_pe_discount'),
        'omission_reason':'DCF requires >=4 consistent positive annual FCF periods, shares, same-currency statements and a non-financial sector',
        'assumptions':policy['dcf'],'formulas':'FCF_t=FCF_0*(1+g)^t; PV=sum(FCF_t/(1+r)^t)+FCF_5*(1+terminal)/(r-terminal)/(1+r)^5; per-share equity=PV/shares. FCF is an equity cash-flow proxy; no second net-debt deduction.'}
    rows=sorted(data.statements,key=lambda x:x['period'],reverse=True)
    financial=any(word in (data.sector+' '+data.industry).lower() for word in ('bank','financial','insurance','credit'))
    values=[r.get('fcf') for r in rows[:4]]
    if financial or len(values)<4 or any(v is None or v<=0 for v in values) or not value('shares') or not fcf or fcf<=0:
        return result
    from datetime import date
    if any(abs((date.fromisoformat(rows[i]['period'])-date.fromisoformat(rows[i+1]['period'])).days-365)>45 for i in range(3)):
        return result
    historical=(values[0]/values[3])**(1/3)-1
    # Model policy is explicit, historical growth is only a cap; no analyst forecasts invented.
    scenarios={}
    for name,assumptions in policy['dcf']['scenarios'].items():
        g=Decimal(str(min(max(historical,-0.1),assumptions['growth_cap'])))
        r=Decimal(str(assumptions['discount_rate']))
        terminal=Decimal(str(policy['dcf']['terminal_growth']))
        if r<=terminal:
            raise ValueError('Discount rate must exceed terminal growth')
        flow=Decimal(str(fcf))
        pv=Decimal(0)
        for year in range(1,6):
            flow*=1+g
            pv+=flow/(1+r)**year
        pv+=flow*(1+terminal)/(r-terminal)/(1+r)**5
        scenarios[name]={'value':float(pv/Decimal(str(value('shares')))),'growth':float(g),'discount_rate':float(r)}
    base=scenarios['base']['value']
    mos=1-price/base if price and base>0 else None
    result.update(fair_values=scenarios,margin_of_safety=mos,accumulation_range=[scenarios['conservative']['value']*0.75,base*0.8],
        verdict='Undervalued' if mos is not None and mos>=0.2 else 'Overvalued' if mos is not None and mos< -0.1 else 'Fairly Valued',
        confidence='low/model-sensitive',omission_reason=None,historical_fcf_growth=historical)
    return result
