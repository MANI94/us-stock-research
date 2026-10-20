from __future__ import annotations
from .models import Metric


def sector_profile(sector: str, industry: str) -> str:
    text=(sector+' '+industry).lower()
    if any(x in text for x in ('bank','credit','financial','insurance')):
        return 'financial'
    if any(x in text for x in ('technology','software','information technology')):
        return 'technology'
    if any(x in text for x in ('steel','mining','oil','commodity','chemical','energy')):
        return 'cyclical'
    return 'manufacturing'


def category_score(metrics: dict[str, Metric], rules: dict, maximum: int, coverage_min: float) -> dict:
    possible=sum(rule['weight'] for rule in rules.values())
    eligible=0.0
    weighted=0.0
    detail={}
    for key,rule in rules.items():
        m=metrics.get(key)
        val=m.value if m and m.freshness not in {'stale','unknown','pending_calendar_check'} else None
        if val is None:
            detail[key]={'value':None,'points':None,'reason':'missing, stale, or undated'}
            continue
        eligible+=rule['weight']
        low,high=rule['bad'],rule['good']
        quality=min(1,max(0,(val-low)/(high-low)))
        weighted+=quality*rule['weight']
        detail[key]={'value':val,'quality':quality,'weight':rule['weight']}
    coverage=eligible/possible if possible else 0
    score=round(maximum*weighted/eligible,2) if eligible and coverage>=coverage_min else None
    return {'score':score,'maximum':maximum,'coverage':round(coverage,4),'details':detail,
            'method':'Linear clamp between bad/good thresholds; weights redistributed only within category'}


def score(metrics: dict[str, Metric], profile: str, policy: dict) -> dict:
    categories={}
    for name,maximum in {'fundamentals':30,'valuation':30,'technicals':25,'risk':15}.items():
        rules=policy['profiles'][profile].get(name,policy['common'].get(name))
        categories[name]=category_score(metrics,rules,maximum,policy['minimum_coverage'])
    total=round(sum(c['score'] for c in categories.values()),2) if all(c['score'] is not None for c in categories.values()) else None
    return {'total':total,'categories':categories,'profile':profile,
        'interpretation':None if total is None else 'Strong candidate' if total>=85 else 'Attractive candidate, further review' if total>=70 else 'Watchlist' if total>=55 else 'Avoid candidate'}
