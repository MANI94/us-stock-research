"""Official filing metadata, not a claim to have read the filing."""
from __future__ import annotations
import os
from .http import Client


def filings(client: Client, ticker: str) -> list[dict]:
    agent=os.getenv('SEC_USER_AGENT','')
    if not agent:
        return []
    headers={'User-Agent':agent,'Accept-Encoding':'gzip, deflate'}
    mapping,_=client.get('https://www.sec.gov/files/company_tickers.json',headers=headers,interval=.2)
    company=next((row for row in mapping.values() if row['ticker'].upper()==ticker.upper()),None)
    if not company:
        return []
    cik=str(company['cik_str'])
    data,_=client.get(f'https://data.sec.gov/submissions/CIK{cik.zfill(10)}.json',headers=headers,interval=.2)
    recent=data.get('filings',{}).get('recent',{})
    result=[]
    for i,form in enumerate(recent.get('form',[])[:100]):
        if form not in {'8-K','10-K','10-Q','6-K','20-F','40-F'}:
            continue
        accession=recent['accessionNumber'][i].replace('-','')
        document=recent['primaryDocument'][i]
        item={'headline':f"{data.get('name',company['title'])} filed Form {form}",
            'summary':'Official filing metadata only; read the linked filing to assess materiality.',
            'published_at':recent.get('acceptanceDateTime',recent['filingDate'])[i],
            'url':f'https://www.sec.gov/Archives/edgar/data/{cik}/{accession}/{document}',
            'publisher':'SEC EDGAR','primary':True}
        section=recent.get('items',['']*len(recent.get('form',[])))[i]
        if form=='8-K' and '1.03' in [x.strip() for x in section.split(',')]:
            item.update(confirmed=True,event_code='bankruptcy_or_receivership',
                evidence_quote='SEC Form 8-K item 1.03: Bankruptcy or Receivership')
        if form=='8-K' and '4.02' in [x.strip() for x in section.split(',')]:
            item.update(confirmed=True,event_code='financial_statement_nonreliance',
                evidence_quote='SEC Form 8-K item 4.02: Non-Reliance on Previously Issued Financial Statements')
        result.append(item)
    return result
