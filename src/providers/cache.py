from __future__ import annotations
from dataclasses import asdict
from io import StringIO
import json
from pathlib import Path
import time
import pandas as pd
from . import Bundle
from ..models import Metric


class CachedProvider:
    def __init__(self, provider, directory: Path, ttl: int=21600):
        self.provider=provider
        self.name=provider.name
        self.directory=directory
        self.ttl=ttl
        directory.mkdir(parents=True,exist_ok=True)

    def fetch(self,stock):
        path=self.directory/f'{self.name}-{stock.ticker}.json'
        if path.exists() and time.time()-path.stat().st_mtime<self.ttl:
            try:
                raw=json.loads(path.read_text())
                bars=pd.read_json(StringIO(raw.pop('bars')),orient='table')
                bars.attrs=raw.pop('bar_attrs')
                raw['metrics']={k:Metric.model_validate(v) for k,v in raw['metrics'].items()}
                return Bundle(**raw,bars=bars)
            except (ValueError,KeyError,TypeError):
                pass
        result=self.provider.fetch(stock)
        raw={k:v for k,v in result.__dict__.items() if k not in {'bars','metrics'}}
        raw['bars']=result.bars.to_json(orient='table')
        raw['bar_attrs']=result.bars.attrs
        raw['metrics']={k:v.model_dump() for k,v in result.metrics.items()}
        temporary=path.with_suffix('.tmp')
        temporary.write_text(json.dumps(raw,allow_nan=False))
        temporary.replace(path)
        return result
