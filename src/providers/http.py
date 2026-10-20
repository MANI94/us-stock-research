"""Bounded retry client. Never log URLs, params, response bodies or exceptions."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import random
import time
from typing import Any
import requests
from ..models import utcnow


class ProviderError(RuntimeError):
    pass


class Client:
    def __init__(self, cache: Path = Path('.cache'), ttl: int = 21600):
        self.cache, self.ttl = cache, ttl
        cache.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.last: dict[str, float] = {}

    def get(self, url: str, params: dict | None = None, headers: dict | None = None,
            interval: float = 0.3) -> tuple[Any, str]:
        key = hashlib.sha256(json.dumps([url, params, headers], sort_keys=True).encode()).hexdigest()
        file = self.cache / (key + '.json')
        if file.exists() and time.time() - file.stat().st_mtime < self.ttl:
            try:
                cached = json.loads(file.read_text())
                return cached['data'], cached['retrieved_at']
            except (ValueError, KeyError):
                pass
        host = url.split('/')[2]
        for attempt in range(4):
            time.sleep(max(0, interval - (time.monotonic() - self.last.get(host, 0))))
            self.last[host] = time.monotonic()
            try:
                response = self.session.get(url, params=params, headers=headers, timeout=(10, 45))
                if response.status_code == 429 or response.status_code >= 500:
                    delay = response.headers.get('Retry-After', '')
                    time.sleep(min(float(delay), 30) if delay.isdigit() else 2 ** attempt + random.random())
                    continue
                if response.status_code != 200:
                    raise ProviderError('HTTP status ' + str(response.status_code))
                data = response.json()
                if isinstance(data, dict) and any(k in data for k in ('Error Message', 'Information', 'Note', 'error')):
                    raise ProviderError('Provider returned unavailable data')
                stamp = utcnow()
                temporary = file.with_suffix('.tmp')
                temporary.write_text(json.dumps({'data': data, 'retrieved_at': stamp}))
                temporary.replace(file)
                return data, stamp
            except (requests.RequestException, ValueError):
                time.sleep(2 ** attempt)
        raise ProviderError('Request exhausted retries')
