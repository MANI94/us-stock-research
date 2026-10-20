from __future__ import annotations
import json
from pathlib import Path
from typing import Any


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False,ensure_ascii=False))
    temporary.replace(path)


def previous(history: Path, date: str) -> dict:
    files=sorted(p for p in history.glob('*.json') if p.stem<date)
    return json.loads(files[-1].read_text()) if files else {}


def changes(current: dict, old: dict) -> dict:
    if not old:
        return {'baseline':'First observation'}
    result={}
    for key in ('price','score','verdict','fair_value'):
        before,after=old.get(key),current.get(key)
        if before!=after:
            result[key]={'previous':before,'current':after,'delta':after-before if isinstance(after,(float,int)) and isinstance(before,(float,int)) else None}
    result['new_news']=[x for x in current.get('news_ids',[]) if x not in old.get('news_ids',[])]
    return result
