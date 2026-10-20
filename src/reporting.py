from __future__ import annotations
import csv
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from .storage import write_json


def render(report: dict, root: Path) -> None:
    out=root/'reports'
    out.mkdir(exist_ok=True)
    write_json(out/'latest.json',report)
    env=Environment(loader=FileSystemLoader(str(Path(__file__).resolve().parent.parent/'templates')),autoescape=select_autoescape(['html']))
    env.filters['na']=lambda x:'N/A' if x is None else x
    (out/'latest.html').write_text(env.get_template('email.html').render(report=report))
    rows=[]
    for stock in report['stocks']:
        row={k:stock.get(k) for k in ('ticker','name','exchange','currency','price','price_timestamp','score','verdict','fair_value')}
        row['news_overlay']=stock.get('news',{}).get('overlay')
        for name,category in stock.get('scores',{}).get('categories',{}).items():
            row[name+'_score']=category['score']
            row[name+'_coverage']=category['coverage']
        rows.append(row)
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with (out/'latest.csv').open('w',newline='') as output:
        writer=csv.DictWriter(output,fieldnames=fields)
        writer.writeheader()
        # Neutralize spreadsheet formula injection from external company names.
        writer.writerows({k:("'"+v if isinstance(v,str) and v.startswith(('=','+','-','@')) else v) for k,v in row.items()} for row in rows)
    md=['# Daily equity research',report['generated_at'],'Research and decision support; no order execution.']
    for s in report['stocks']:
        md += [f"\n## {s['ticker']} — {s['verdict']}",f"Price: {s.get('price') or 'N/A'} {s.get('currency','')} | Score: {s.get('score') if s.get('score') is not None else 'N/A'} / 100",
            '```json',__import__('json').dumps(s,indent=2,ensure_ascii=False),'```']
    (out/'latest.md').write_text('\n'.join(md))
    write_json(root/'history'/f"{report['report_date']}.json",report)
