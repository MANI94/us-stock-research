from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
import math
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from zoneinfo import ZoneInfo


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


class Metric(BaseModel):
    model_config = ConfigDict(extra='forbid')
    value: float | None = None
    unit: str = 'ratio'
    source: str
    period: str | None = None
    retrieved_at: str = Field(default_factory=utcnow)
    freshness: str = 'unknown'
    formula: str | None = None
    inputs: list[str] = Field(default_factory=list)

    @field_validator('value', mode='before')
    @classmethod
    def finite(cls, value: Any) -> float | None:
        if value is None:
            return None
        number = float(value)
        return number if math.isfinite(number) else None


class Stock(BaseModel):
    model_config = ConfigDict(extra='forbid')
    ticker: str = Field(pattern=r'^[A-Z0-9][A-Z0-9.^-]{0,24}$')
    exchange: str

    @model_validator(mode='after')
    def exchange_matches(self) -> Stock:
        if self.exchange not in {'NASDAQ', 'NYSE', 'NSE', 'BSE'}:
            raise ValueError('Unsupported exchange')
        suffix = {'NSE': '.NS', 'BSE': '.BO'}.get(self.exchange)
        if suffix and not self.ticker.endswith(suffix):
            raise ValueError('Indian ticker requires .NS or .BO suffix')
        if not suffix and self.ticker.endswith(('.NS', '.BO')):
            raise ValueError('Ticker suffix conflicts with exchange')
        return self


class Settings(BaseModel):
    model_config = ConfigDict(extra='forbid')
    base_currency: str = 'INR'
    reporting_currencies: list[str] = ['USD', 'INR']
    investment_horizon: str = 'long_term'
    risk_profile: str = 'moderate'
    default_investment_inr: float = Field(default=50000, gt=0)
    report_timezone: str = 'Asia/Kolkata'
    news_lookback_days: int = Field(default=7, ge=1, le=30)
    enable_email: bool = True
    providers: list[str] = ['fmp', 'yahoo']
    allow_yahoo: bool = True

    @model_validator(mode='after')
    def validate_settings(self) -> Settings:
        ZoneInfo(self.report_timezone)
        if set(self.reporting_currencies + [self.base_currency]) - {'INR', 'USD'}:
            raise ValueError('Only INR and USD are supported')
        if self.investment_horizon not in {'long_term', 'swing'}:
            raise ValueError('Unsupported horizon')
        if self.risk_profile not in {'conservative', 'moderate', 'aggressive'}:
            raise ValueError('Unsupported risk profile')
        if not self.providers or set(self.providers) - {'fmp', 'yahoo'}:
            raise ValueError('Supported financial providers: fmp, yahoo')
        return self


class Config(BaseModel):
    model_config = ConfigDict(extra='forbid')
    settings: Settings
    stocks: list[Stock] = Field(min_length=1, max_length=100)

    @model_validator(mode='after')
    def unique(self) -> Config:
        if len({s.ticker for s in self.stocks}) != len(self.stocks):
            raise ValueError('Duplicate ticker')
        return self
