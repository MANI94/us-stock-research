from __future__ import annotations


def decide(scores: dict, valuation: dict, risk: dict, news: dict, stale: bool, essentials: bool, horizon: str='long_term', risk_profile: str='moderate') -> dict:
    if risk['critical'] or news.get('critical'):
        return {'verdict':'AVOID','reasons':risk['critical'] or ['Critical confirmed news'], 'invalidation':'Resolve critical event through primary disclosures before reconsidering'}
    if stale or not essentials or scores['total'] is None:
        return {'verdict':'INSUFFICIENT DATA','reasons':['Stale, undated, or insufficient essential evidence/category coverage'],
            'invalidation':'Obtain current statements, valuation evidence and risk disclosures; rerun'}
    required_mos={'conservative':.3,'moderate':.2,'aggressive':.15}[risk_profile]
    total=scores['total']
    f=scores['categories']['fundamentals']['score']
    r=scores['categories']['risk']['score']
    if total<55:
        verdict='AVOID'
    elif total>=70 and f>=21 and r>=10.5 and valuation['verdict']=='Undervalued' and valuation.get('margin_of_safety',0)>=required_mos and not risk['concerns']:
        verdict='BUY CANDIDATE'
    elif total>=70 and valuation['verdict'] in {'Fairly Valued','Overvalued'}:
        verdict='WAIT FOR BETTER PRICE'
    else:
        verdict='HOLD / REVIEW'
    return {'verdict':verdict,'reasons':[scores['interpretation'], 'Valuation: '+valuation['verdict'], 'Review unresolved governance disclosures'],
        'invalidation':'Deteriorating cash generation, leverage, governance, or valuation assumptions invalidate the thesis.',
        'horizon':horizon,'note':'Technical entry/invalidation levels are swing scenarios; long-term thesis depends on company fundamentals.'}
