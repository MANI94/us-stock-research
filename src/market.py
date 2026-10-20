from __future__ import annotations
from datetime import datetime, timedelta, timezone
import pandas as pd
import exchange_calendars as xcals


def market_status(exchange: str, last_bar: str | None, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    calendar = xcals.get_calendar({'NASDAQ':'XNYS','NYSE':'XNYS','NSE':'XBOM','BSE':'XBOM'}[exchange])
    schedule = calendar.schedule.loc[(now - timedelta(days=20)).date().isoformat():now.date().isoformat()]
    complete = schedule[pd.to_datetime(schedule['close'], utc=True) + pd.Timedelta(minutes=30) <= pd.Timestamp(now)]
    expected = str(complete.index[-1].date()) if len(complete) else None
    day = now.astimezone(__import__('zoneinfo').ZoneInfo('Asia/Kolkata' if exchange in {'NSE','BSE'} else 'America/New_York')).date()
    sessions = {s.date() for s in schedule.index}
    open_now = any(pd.Timestamp(row['open']).tz_convert('UTC') <= pd.Timestamp(now) <= pd.Timestamp(row['close']).tz_convert('UTC') for _, row in schedule.iterrows())
    return {'expected_session':expected,'last_session':last_bar,'stale':not last_bar or not expected or last_bar < expected,
            'condition':'open' if open_now else 'closed' if day in sessions else 'holiday/weekend',
            'calendar':calendar.name, 'calendar_note':'XBOM proxy for NSE; verify exceptional NSE-only sessions' if exchange == 'NSE' else None}
