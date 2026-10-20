from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol, Any
import logging
import pandas as pd
from ..models import Metric, Stock


@dataclass
class Bundle:
    name: str
    currency: str
    sector: str
    industry: str
    metrics: dict[str, Metric] = field(default_factory=dict)
    statements: list[dict[str, Any]] = field(default_factory=list)
    bars: pd.DataFrame = field(default_factory=pd.DataFrame)
    warnings: list[str] = field(default_factory=list)
    candidates: dict[str, list[dict]] = field(default_factory=dict)


class Provider(Protocol):
    name: str
    def fetch(self, stock: Stock) -> Bundle: ...


def collect(stock: Stock, providers: list[Provider]) -> Bundle:
    result: Bundle | None = None
    for provider in providers:
        try:
            incoming = provider.fetch(stock)
            if result is None:
                result = incoming
                continue
            if result.currency != incoming.currency:
                result.warnings.append(f'{provider.name}: currency conflict; rejected')
                continue
            if result.bars.empty:
                result.bars = incoming.bars
            if not result.statements:
                result.statements = incoming.statements
            for key, metric in incoming.metrics.items():
                old = result.metrics.get(key)
                if old is None or old.value is None:
                    result.metrics[key] = metric
                elif metric.value is not None and old.value != metric.value:
                    result.candidates.setdefault(key, []).append(metric.model_dump())
                    if abs(old.value - metric.value) / max(abs(old.value), 1e-9) > 0.1:
                        result.warnings.append(f'{key}: provider conflict >10%; first provider retained')
            result.warnings.extend(incoming.warnings)
        except Exception as error:
            logging.warning('provider_failed', extra={'ticker': stock.ticker, 'provider': provider.name, 'error_type': type(error).__name__})
            if result:
                result.warnings.append(provider.name + ': unavailable')
    if result is None:
        raise RuntimeError('All financial providers unavailable')
    return result
