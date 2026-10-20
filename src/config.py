from pathlib import Path
import yaml
from .models import Config, Stock


def load_config(path: str, override: str = '') -> Config:
    config = Config.model_validate(yaml.safe_load(Path(path).read_text()))
    if override.strip():
        stocks = []
        for token in override.replace(',', ' ').split():
            parts = token.upper().split(':')
            ticker = parts[0]
            exchange = parts[1] if len(parts) == 2 else ('NSE' if ticker.endswith('.NS') else 'BSE' if ticker.endswith('.BO') else 'NASDAQ')
            if len(parts) > 2:
                raise ValueError('Use TICKER:EXCHANGE')
            stocks.append(Stock(ticker=ticker, exchange=exchange))
        config = Config(settings=config.settings, stocks=stocks)
    return config
