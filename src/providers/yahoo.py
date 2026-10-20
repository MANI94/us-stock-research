from __future__ import annotations
from datetime import datetime, timezone
import time
import pandas as pd
import yfinance as yf
from . import Bundle
from ..models import Metric, Stock, utcnow

INFO = {'price': 'currentPrice', 'pe': 'trailingPE', 'forward_pe': 'forwardPE',
        'pb': 'priceToBook', 'ev_ebitda': 'enterpriseToEbitda', 'roe': 'returnOnEquity',
        'roa': 'returnOnAssets', 'operating_margin': 'operatingMargins', 'net_margin': 'profitMargins',
        'market_cap': 'marketCap', 'shares': 'sharesOutstanding', 'insider_ownership': 'heldPercentInsiders',
        'payout': 'payoutRatio', 'eps': 'trailingEps', 'fcf': 'freeCashflow',
        'enterprise_value': 'enterpriseValue', 'debt': 'totalDebt', 'cash': 'totalCash'}
ROWS = {'revenue': 'Total Revenue', 'net_income': 'Net Income', 'eps': 'Diluted EPS',
        'ebit': 'EBIT', 'interest': 'Interest Expense', 'equity': 'Stockholders Equity',
        'debt': 'Total Debt', 'cash': 'Cash And Cash Equivalents', 'assets': 'Total Assets',
        'current_liabilities': 'Current Liabilities', 'current_assets': 'Current Assets',
        'ocf': 'Operating Cash Flow', 'capex': 'Capital Expenditure', 'fcf': 'Free Cash Flow',
        'shares': 'Ordinary Shares Number', 'dividends': 'Cash Dividends Paid',
        'operating_income': 'Operating Income', 'inventory': 'Inventory', 'receivables': 'Receivables'}


class Yahoo:
    name = 'yahoo'

    def fetch(self, stock: Stock) -> Bundle:
        last = None
        for attempt in range(3):
            try:
                return self._fetch(stock)
            except Exception as error:
                last = error
                time.sleep(2 ** attempt)
        raise RuntimeError('Yahoo unavailable') from last

    def _fetch(self, stock: Stock) -> Bundle:
        ticker = yf.Ticker(stock.ticker)
        info = ticker.get_info()
        currency = info.get('currency')
        if currency not in {'USD', 'INR'}:
            raise ValueError('Unknown quote currency')
        stamp = utcnow()
        result = Bundle(info.get('longName', stock.ticker), currency, info.get('sector', 'Unknown'),
                        info.get('industry', 'Unknown'))
        price_time = info.get('regularMarketTime')
        for key, provider_key in INFO.items():
            period = datetime.fromtimestamp(price_time, timezone.utc).isoformat() if key in {'price','market_cap','pe','forward_pe','pb','ev_ebitda','enterprise_value'} and price_time else None
            result.metrics[key] = Metric(value=info.get(provider_key), source='Yahoo Finance', period=period,
                retrieved_at=stamp, unit=currency if key in {'price','market_cap','fcf','enterprise_value','debt','cash'} else 'shares' if key == 'shares' else 'ratio', freshness='snapshot' if period and key!='price' else 'unknown')
        tables = [ticker.income_stmt, ticker.balance_sheet, ticker.cashflow]
        periods = sorted(set().union(*(set(t.columns) for t in tables)), reverse=True)
        financial_currency = info.get('financialCurrency')
        if financial_currency and financial_currency != currency:
            result.warnings.append('Financial/quote currency mismatch; statements omitted')
        else:
            for period in periods:
                row = {'period': str(period.date()), 'source': 'Yahoo Finance', 'retrieved_at': stamp, 'currency': currency}
                for key, label in ROWS.items():
                    for table in tables:
                        if label in table.index and period in table.columns:
                            value = table.loc[label, period]
                            if pd.notna(value):
                                row[key] = float(value)
                result.statements.append(row)
        result.bars = ticker.history(period='2y', auto_adjust=True, actions=True)
        if not result.bars.empty:
            result.bars.attrs.update(source='Yahoo Finance auto_adjust=True', retrieved_at=stamp, currency=currency)
        result.warnings.append('Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete')
        return result
