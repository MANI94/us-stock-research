from __future__ import annotations
from .models import Metric


def analyze(metrics: dict[str, Metric], news: dict, financial: bool) -> dict:
    critical=[]
    concerns=[]
    def val(key):
        metric=metrics.get(key)
        return metric.value if metric and metric.freshness!='stale' else None
    if news.get('critical'):
        critical.append('Confirmed material news requires review')
    if val('equity') is not None and val('equity')<=0:
        critical.append('Non-positive book equity')
    if not financial:
        if val('interest_coverage') is not None and val('interest_coverage')<1:
            critical.append('EBIT does not cover interest expense')
        if val('current_ratio') is not None and val('current_ratio')<0.5:
            critical.append('Severe current liquidity shortfall')
        if val('debt_equity') is not None and val('debt_equity')>2:
            concerns.append('High debt/equity')
    return {'critical':critical,'concerns':concerns,'unverified':['auditor qualifications','pledged promoter shares',
        'business concentration','refinancing maturity schedule','litigation and regulatory exposure','material corporate actions'],
        'note':'Unknown governance information is not a clean audit or low-risk finding.'}
