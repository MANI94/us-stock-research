# Daily equity research
2026-10-20T17:49:24.826610+05:30
Research and decision support; no order execution.

## AAPL — AVOID
Price: 159.03871248284568 USD | Score: 53.93 / 100
```json
{
  "ticker": "AAPL",
  "exchange": "NASDAQ",
  "name": "Synthetic Apple",
  "price": 159.03871248284568,
  "score": 53.93,
  "fair_value": 23.705257540436726,
  "currency": "USD",
  "price_timestamp": "2026-10-19T00:00:00+00:00",
  "scores": {
    "total": 53.93,
    "categories": {
      "fundamentals": {
        "score": 23.32,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 0.16666666666666666,
            "quality": 0.8333333333333333,
            "weight": 2
          },
          "roce": {
            "value": 0.1432844333215966,
            "quality": 0.716422166607983,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.0800000000000003,
            "quality": 0.6500000000000014,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.08000000000000007,
            "quality": 0.5333333333333339,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": 0.08000000000000007,
            "quality": 0.6666666666666673,
            "weight": 1
          },
          "eps_growth_3y": {
            "value": 0.08000000000000007,
            "quality": 0.5333333333333339,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "net_margin": {
            "value": 0.15,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 0.9333333333333333,
            "quality": 0.9333333333333333,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 10.285296537600004,
            "quality": 1,
            "weight": 1
          },
          "recurring_revenue_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "valuation": {
        "score": 1.82,
        "maximum": 30,
        "coverage": 0.6667,
        "details": {
          "earnings_yield": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "fcf_yield": {
            "value": 0.012934330738761986,
            "quality": 0.16167913423452482,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -5.70900589084744,
            "quality": 0,
            "weight": 5
          },
          "peer_pe_discount": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "technicals": {
        "score": 14.52,
        "maximum": 25,
        "coverage": 1.0,
        "details": {
          "above_sma200": {
            "value": 1.0,
            "quality": 1,
            "weight": 3
          },
          "above_sma50": {
            "value": 0.0,
            "quality": 0,
            "weight": 2
          },
          "relative_strength_63": {
            "value": 0.0,
            "quality": 0.5,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.0074673223989394355,
            "quality": 0.5248910746631315,
            "weight": 2
          },
          "macd_positive": {
            "value": 0.0,
            "quality": 0,
            "weight": 1
          },
          "weekly_up": {
            "value": 1.0,
            "quality": 1,
            "weight": 2
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "risk": {
        "score": 14.27,
        "maximum": 15,
        "coverage": 0.7143,
        "details": {
          "debt_equity": {
            "value": 0.1512407104519451,
            "quality": 0.9243796447740275,
            "weight": 3
          },
          "interest_coverage": {
            "value": 29.386561536000013,
            "quality": 1,
            "weight": 3
          },
          "current_ratio": {
            "value": 2.0,
            "quality": 1,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.13116459629492455,
            "quality": 0.8688354037050754,
            "weight": 2
          },
          "audit_clear": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "pledge_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      }
    },
    "profile": "technology",
    "interpretation": "Avoid candidate"
  },
  "verdict": "AVOID",
  "decision": {
    "verdict": "AVOID",
    "reasons": [
      "Avoid candidate",
      "Valuation: Overvalued",
      "Review unresolved governance disclosures"
    ],
    "invalidation": "Deteriorating cash generation, leverage, governance, or valuation assumptions invalidate the thesis.",
    "horizon": "long_term",
    "note": "Technical entry/invalidation levels are swing scenarios; long-term thesis depends on company fundamentals."
  },
  "valuation": {
    "metrics": {
      "earnings_yield": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.163959+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.012934330738761986,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.163978+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.163987+00:00",
        "freshness": "derived",
        "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
        "inputs": [
          "pe",
          "eps_growth_3y"
        ]
      }
    },
    "fair_values": {
      "conservative": {
        "value": 16.14321439343259,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 23.705257540436726,
        "growth": 0.05,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 33.66602443736114,
        "growth": 0.08,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": -5.70900589084744,
    "accumulation_range": [
      12.107410795074443,
      18.96420603234938
    ],
    "verdict": "Overvalued",
    "confidence": "low/model-sensitive",
    "historical_pe": {
      "historical_pe_median": null,
      "historical_pe_min": null,
      "historical_pe_max": null
    },
    "sector_relative_pe": null,
    "omission_reason": null,
    "assumptions": {
      "source": "Explicit research policy; rates are sensitivity assumptions, not forecasts. Historical annual FCF CAGR caps growth. No DCF for financial companies.",
      "terminal_growth": 0.02,
      "scenarios": {
        "conservative": {
          "growth_cap": 0,
          "discount_rate": 0.14
        },
        "base": {
          "growth_cap": 0.05,
          "discount_rate": 0.12
        },
        "optimistic": {
          "growth_cap": 0.08,
          "discount_rate": 0.1
        }
      }
    },
    "formulas": "FCF_t=FCF_0*(1+g)^t; PV=sum(FCF_t/(1+r)^t)+FCF_5*(1+terminal)/(r-terminal)/(1+r)^5; per-share equity=PV/shares. FCF is an equity cash-flow proxy; no second net-debt deduction.",
    "historical_fcf_growth": 0.08000000000000007
  },
  "technicals": {
    "trend": "mixed",
    "weekly_trend": "up",
    "support": 153.53725205244325,
    "resistance": 161.06660269934446,
    "entry_range": [
      153.53725205244325,
      155.53725205244325
    ],
    "invalidation": 149.53725205244325,
    "risk_reward": 0.21342931766678785,
    "support_zone": [
      152.53725205244325,
      154.53725205244325
    ],
    "resistance_zone": [
      160.06660269934446,
      162.06660269934446
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points."
  },
  "risk": {
    "critical": [],
    "concerns": [],
    "unverified": [
      "auditor qualifications",
      "pledged promoter shares",
      "business concentration",
      "refinancing maturity schedule",
      "litigation and regulatory exposure",
      "material corporate actions"
    ],
    "note": "Unknown governance information is not a clean audit or low-risk finding."
  },
  "market": {
    "expected_session": "2026-10-19",
    "last_session": "2026-10-19",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 159.03871248284568,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:24.830390+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "market_cap": {
      "value": 15903871.248284569,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:24.830406+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.16666666666666666,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.09375,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": null,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.15,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "debt_equity": {
      "value": 0.1512407104519451,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 2.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.9333333333333333,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": 29.386561536000013,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.1432844333215966,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "fcf": {
      "value": 205705.93075200007,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "eps": {
      "value": 2.203992115200001,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "equity": {
      "value": 1322395.2691200005,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "shares": {
      "value": 100000.0,
      "unit": "shares",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "debt": {
      "value": 200000.0,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 300000.0,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2024-12-31"
      ]
    },
    "eps_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2024-12-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2022-12-31"
      ]
    },
    "eps_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2022-12-31"
      ]
    },
    "revenue_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "2020-12-31"
      ]
    },
    "eps_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "2020-12-31"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 10.285296537600004,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.13116459629492455,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 162.09059367831705,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 159.3590016885118,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 156.35929919160003,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 150.35980734485275,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 161.32196505080327,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 159.553270923942,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 38.75682723385731,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 0.4128363861368314,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 1.095586381076533,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.6827499949397016,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 157.38941114207617,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 166.79177621455793,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 4.0,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.0009991911309892,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 167.07951966276556,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 126.40391407986147,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.0074673223989394355,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:24.830327+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163903+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163912+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163915+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163917+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163919+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163921+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163923+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163925+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163927+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163930+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163932+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163934+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163936+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163938+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163940+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163941+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163943+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163945+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.163947+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.163959+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.012934330738761986,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.163978+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.163987+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -5.70900589084744,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.164653+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.164664+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.164669+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.164672+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.164675+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:24.830338+00:00",
      "currency": "USD",
      "revenue": 1469328.0768000006,
      "net_income": 220399.21152000007,
      "eps": 2.203992115200001,
      "ebit": 293865.6153600001,
      "interest": 10000,
      "equity": 1322395.2691200005,
      "assets": 2350924.922880001,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 205705.93075200007,
      "ocf": 264479.0538240001,
      "capex": -58773.123072000024,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2024-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:24.830342+00:00",
      "currency": "USD",
      "revenue": 1360488.9600000002,
      "net_income": 204073.34400000004,
      "eps": 2.0407334400000003,
      "ebit": 272097.7920000001,
      "interest": 10000,
      "equity": 1224440.0640000002,
      "assets": 2176782.3360000006,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 190468.45440000005,
      "ocf": 244888.01280000005,
      "capex": -54419.55840000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2023-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:24.830344+00:00",
      "currency": "USD",
      "revenue": 1259712.0000000002,
      "net_income": 188956.80000000002,
      "eps": 1.8895680000000001,
      "ebit": 251942.40000000002,
      "interest": 10000,
      "equity": 1133740.8,
      "assets": 2015539.2000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 176359.68000000002,
      "ocf": 226748.16000000003,
      "capex": -50388.48,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2022-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:24.830346+00:00",
      "currency": "USD",
      "revenue": 1166400.0,
      "net_income": 174960.00000000003,
      "eps": 1.7496,
      "ebit": 233280.00000000003,
      "interest": 10000,
      "equity": 1049760.0,
      "assets": 1866240.0000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 163296.0,
      "ocf": 209952.00000000003,
      "capex": -46656.00000000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2021-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:24.830348+00:00",
      "currency": "USD",
      "revenue": 1080000.0,
      "net_income": 162000.0,
      "eps": 1.62,
      "ebit": 216000.0,
      "interest": 10000,
      "equity": 972000.0000000001,
      "assets": 1728000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 151200.0,
      "ocf": 194400.0,
      "capex": -43200.0,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2020-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:24.830350+00:00",
      "currency": "USD",
      "revenue": 1000000.0,
      "net_income": 150000.0,
      "eps": 1.5,
      "ebit": 200000.0,
      "interest": 10000,
      "equity": 900000.0,
      "assets": 1600000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 140000.0,
      "ocf": 180000.0,
      "capex": -40000.0,
      "shares": 100000,
      "dividends": -20000
    }
  ],
  "provider_conflicts": {},
  "warnings": [],
  "news_ids": [],
  "converted_prices": {
    "USD": 159.03871248284568,
    "INR": null
  },
  "changes": {
    "baseline": "First observation"
  }
}
```

## MSFT — AVOID
Price: 159.03871248284568 USD | Score: 53.93 / 100
```json
{
  "ticker": "MSFT",
  "exchange": "NASDAQ",
  "name": "Synthetic Technology Company",
  "price": 159.03871248284568,
  "score": 53.93,
  "fair_value": 23.705257540436726,
  "currency": "USD",
  "price_timestamp": "2026-10-19T00:00:00+00:00",
  "scores": {
    "total": 53.93,
    "categories": {
      "fundamentals": {
        "score": 23.32,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 0.16666666666666666,
            "quality": 0.8333333333333333,
            "weight": 2
          },
          "roce": {
            "value": 0.1432844333215966,
            "quality": 0.716422166607983,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.0800000000000003,
            "quality": 0.6500000000000014,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.08000000000000007,
            "quality": 0.5333333333333339,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": 0.08000000000000007,
            "quality": 0.6666666666666673,
            "weight": 1
          },
          "eps_growth_3y": {
            "value": 0.08000000000000007,
            "quality": 0.5333333333333339,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "net_margin": {
            "value": 0.15,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 0.9333333333333333,
            "quality": 0.9333333333333333,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 10.285296537600004,
            "quality": 1,
            "weight": 1
          },
          "recurring_revenue_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "valuation": {
        "score": 1.82,
        "maximum": 30,
        "coverage": 0.6667,
        "details": {
          "earnings_yield": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "fcf_yield": {
            "value": 0.012934330738761986,
            "quality": 0.16167913423452482,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -5.70900589084744,
            "quality": 0,
            "weight": 5
          },
          "peer_pe_discount": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "technicals": {
        "score": 14.52,
        "maximum": 25,
        "coverage": 1.0,
        "details": {
          "above_sma200": {
            "value": 1.0,
            "quality": 1,
            "weight": 3
          },
          "above_sma50": {
            "value": 0.0,
            "quality": 0,
            "weight": 2
          },
          "relative_strength_63": {
            "value": 0.0,
            "quality": 0.5,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.0074673223989394355,
            "quality": 0.5248910746631315,
            "weight": 2
          },
          "macd_positive": {
            "value": 0.0,
            "quality": 0,
            "weight": 1
          },
          "weekly_up": {
            "value": 1.0,
            "quality": 1,
            "weight": 2
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "risk": {
        "score": 14.27,
        "maximum": 15,
        "coverage": 0.7143,
        "details": {
          "debt_equity": {
            "value": 0.1512407104519451,
            "quality": 0.9243796447740275,
            "weight": 3
          },
          "interest_coverage": {
            "value": 29.386561536000013,
            "quality": 1,
            "weight": 3
          },
          "current_ratio": {
            "value": 2.0,
            "quality": 1,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.13116459629492455,
            "quality": 0.8688354037050754,
            "weight": 2
          },
          "audit_clear": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "pledge_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      }
    },
    "profile": "technology",
    "interpretation": "Avoid candidate"
  },
  "verdict": "AVOID",
  "decision": {
    "verdict": "AVOID",
    "reasons": [
      "Avoid candidate",
      "Valuation: Overvalued",
      "Review unresolved governance disclosures"
    ],
    "invalidation": "Deteriorating cash generation, leverage, governance, or valuation assumptions invalidate the thesis.",
    "horizon": "long_term",
    "note": "Technical entry/invalidation levels are swing scenarios; long-term thesis depends on company fundamentals."
  },
  "valuation": {
    "metrics": {
      "earnings_yield": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.227933+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.012934330738761986,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.227948+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.227955+00:00",
        "freshness": "derived",
        "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
        "inputs": [
          "pe",
          "eps_growth_3y"
        ]
      }
    },
    "fair_values": {
      "conservative": {
        "value": 16.14321439343259,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 23.705257540436726,
        "growth": 0.05,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 33.66602443736114,
        "growth": 0.08,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": -5.70900589084744,
    "accumulation_range": [
      12.107410795074443,
      18.96420603234938
    ],
    "verdict": "Overvalued",
    "confidence": "low/model-sensitive",
    "historical_pe": {
      "historical_pe_median": null,
      "historical_pe_min": null,
      "historical_pe_max": null
    },
    "sector_relative_pe": null,
    "omission_reason": null,
    "assumptions": {
      "source": "Explicit research policy; rates are sensitivity assumptions, not forecasts. Historical annual FCF CAGR caps growth. No DCF for financial companies.",
      "terminal_growth": 0.02,
      "scenarios": {
        "conservative": {
          "growth_cap": 0,
          "discount_rate": 0.14
        },
        "base": {
          "growth_cap": 0.05,
          "discount_rate": 0.12
        },
        "optimistic": {
          "growth_cap": 0.08,
          "discount_rate": 0.1
        }
      }
    },
    "formulas": "FCF_t=FCF_0*(1+g)^t; PV=sum(FCF_t/(1+r)^t)+FCF_5*(1+terminal)/(r-terminal)/(1+r)^5; per-share equity=PV/shares. FCF is an equity cash-flow proxy; no second net-debt deduction.",
    "historical_fcf_growth": 0.08000000000000007
  },
  "technicals": {
    "trend": "mixed",
    "weekly_trend": "up",
    "support": 153.53725205244325,
    "resistance": 161.06660269934446,
    "entry_range": [
      153.53725205244325,
      155.53725205244325
    ],
    "invalidation": 149.53725205244325,
    "risk_reward": 0.21342931766678785,
    "support_zone": [
      152.53725205244325,
      154.53725205244325
    ],
    "resistance_zone": [
      160.06660269934446,
      162.06660269934446
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points."
  },
  "risk": {
    "critical": [],
    "concerns": [],
    "unverified": [
      "auditor qualifications",
      "pledged promoter shares",
      "business concentration",
      "refinancing maturity schedule",
      "litigation and regulatory exposure",
      "material corporate actions"
    ],
    "note": "Unknown governance information is not a clean audit or low-risk finding."
  },
  "market": {
    "expected_session": "2026-10-19",
    "last_session": "2026-10-19",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 159.03871248284568,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:25.186631+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "market_cap": {
      "value": 15903871.248284569,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:25.186670+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.16666666666666666,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.09375,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": null,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.15,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "debt_equity": {
      "value": 0.1512407104519451,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 2.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.9333333333333333,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": 29.386561536000013,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.1432844333215966,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "fcf": {
      "value": 205705.93075200007,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "eps": {
      "value": 2.203992115200001,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "equity": {
      "value": 1322395.2691200005,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "shares": {
      "value": 100000.0,
      "unit": "shares",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "debt": {
      "value": 200000.0,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 300000.0,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2024-12-31"
      ]
    },
    "eps_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2024-12-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2022-12-31"
      ]
    },
    "eps_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2022-12-31"
      ]
    },
    "revenue_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "2020-12-31"
      ]
    },
    "eps_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "2020-12-31"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 10.285296537600004,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.13116459629492455,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 162.09059367831705,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 159.3590016885118,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 156.35929919160003,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 150.35980734485275,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 161.32196505080327,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 159.553270923942,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 38.75682723385731,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 0.4128363861368314,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 1.095586381076533,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.6827499949397016,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 157.38941114207617,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 166.79177621455793,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 4.0,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.0009991911309892,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 167.07951966276556,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 126.40391407986147,
      "unit": "USD",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.0074673223989394355,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.186446+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227890+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227896+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227898+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227900+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227902+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227903+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227905+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227907+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227909+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227910+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227912+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227913+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227915+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227917+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227918+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227920+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227922+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227923+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.227925+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.227933+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.012934330738761986,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.227948+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.227955+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -5.70900589084744,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.228024+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.228033+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.228036+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.228039+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.228042+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.186489+00:00",
      "currency": "USD",
      "revenue": 1469328.0768000006,
      "net_income": 220399.21152000007,
      "eps": 2.203992115200001,
      "ebit": 293865.6153600001,
      "interest": 10000,
      "equity": 1322395.2691200005,
      "assets": 2350924.922880001,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 205705.93075200007,
      "ocf": 264479.0538240001,
      "capex": -58773.123072000024,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2024-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.186502+00:00",
      "currency": "USD",
      "revenue": 1360488.9600000002,
      "net_income": 204073.34400000004,
      "eps": 2.0407334400000003,
      "ebit": 272097.7920000001,
      "interest": 10000,
      "equity": 1224440.0640000002,
      "assets": 2176782.3360000006,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 190468.45440000005,
      "ocf": 244888.01280000005,
      "capex": -54419.55840000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2023-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.186508+00:00",
      "currency": "USD",
      "revenue": 1259712.0000000002,
      "net_income": 188956.80000000002,
      "eps": 1.8895680000000001,
      "ebit": 251942.40000000002,
      "interest": 10000,
      "equity": 1133740.8,
      "assets": 2015539.2000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 176359.68000000002,
      "ocf": 226748.16000000003,
      "capex": -50388.48,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2022-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.186513+00:00",
      "currency": "USD",
      "revenue": 1166400.0,
      "net_income": 174960.00000000003,
      "eps": 1.7496,
      "ebit": 233280.00000000003,
      "interest": 10000,
      "equity": 1049760.0,
      "assets": 1866240.0000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 163296.0,
      "ocf": 209952.00000000003,
      "capex": -46656.00000000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2021-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.186518+00:00",
      "currency": "USD",
      "revenue": 1080000.0,
      "net_income": 162000.0,
      "eps": 1.62,
      "ebit": 216000.0,
      "interest": 10000,
      "equity": 972000.0000000001,
      "assets": 1728000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 151200.0,
      "ocf": 194400.0,
      "capex": -43200.0,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2020-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.186524+00:00",
      "currency": "USD",
      "revenue": 1000000.0,
      "net_income": 150000.0,
      "eps": 1.5,
      "ebit": 200000.0,
      "interest": 10000,
      "equity": 900000.0,
      "assets": 1600000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 140000.0,
      "ocf": 180000.0,
      "capex": -40000.0,
      "shares": 100000,
      "dividends": -20000
    }
  ],
  "provider_conflicts": {},
  "warnings": [],
  "news_ids": [],
  "converted_prices": {
    "USD": 159.03871248284568,
    "INR": null
  },
  "changes": {
    "baseline": "First observation"
  }
}
```

## TCS.NS — INSUFFICIENT DATA
Price: 159.03871248284568 INR | Score: N/A / 100
```json
{
  "ticker": "TCS.NS",
  "exchange": "NSE",
  "name": "Synthetic TCS",
  "price": 159.03871248284568,
  "score": null,
  "fair_value": 23.705257540436726,
  "currency": "INR",
  "price_timestamp": "2026-10-19T00:00:00+00:00",
  "scores": {
    "total": null,
    "categories": {
      "fundamentals": {
        "score": 23.32,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 0.16666666666666666,
            "quality": 0.8333333333333333,
            "weight": 2
          },
          "roce": {
            "value": 0.1432844333215966,
            "quality": 0.716422166607983,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.0800000000000003,
            "quality": 0.6500000000000014,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.08000000000000007,
            "quality": 0.5333333333333339,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": 0.08000000000000007,
            "quality": 0.6666666666666673,
            "weight": 1
          },
          "eps_growth_3y": {
            "value": 0.08000000000000007,
            "quality": 0.5333333333333339,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "net_margin": {
            "value": 0.15,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 0.9333333333333333,
            "quality": 0.9333333333333333,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 10.285296537600004,
            "quality": 1,
            "weight": 1
          },
          "recurring_revenue_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "valuation": {
        "score": null,
        "maximum": 30,
        "coverage": 0.25,
        "details": {
          "earnings_yield": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "fcf_yield": {
            "value": 0.012934330738761986,
            "quality": 0.16167913423452482,
            "weight": 3
          },
          "margin_of_safety": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "peer_pe_discount": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "technicals": {
        "score": null,
        "maximum": 25,
        "coverage": 0.0,
        "details": {
          "above_sma200": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "above_sma50": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "relative_strength_63": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "momentum_63": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "macd_positive": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "weekly_up": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "risk": {
        "score": 14.27,
        "maximum": 15,
        "coverage": 0.7143,
        "details": {
          "debt_equity": {
            "value": 0.1512407104519451,
            "quality": 0.9243796447740275,
            "weight": 3
          },
          "interest_coverage": {
            "value": 29.386561536000013,
            "quality": 1,
            "weight": 3
          },
          "current_ratio": {
            "value": 2.0,
            "quality": 1,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.13116459629492455,
            "quality": 0.8688354037050754,
            "weight": 2
          },
          "audit_clear": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "pledge_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      }
    },
    "profile": "technology",
    "interpretation": null
  },
  "verdict": "INSUFFICIENT DATA",
  "decision": {
    "verdict": "INSUFFICIENT DATA",
    "reasons": [
      "Stale, undated, or insufficient essential evidence/category coverage"
    ],
    "invalidation": "Obtain current statements, valuation evidence and risk disclosures; rerun"
  },
  "valuation": {
    "metrics": {
      "earnings_yield": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.554835+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.012934330738761986,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.554856+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.554864+00:00",
        "freshness": "derived",
        "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
        "inputs": [
          "pe",
          "eps_growth_3y"
        ]
      }
    },
    "fair_values": {
      "conservative": {
        "value": 16.14321439343259,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 23.705257540436726,
        "growth": 0.05,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 33.66602443736114,
        "growth": 0.08,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": null,
    "accumulation_range": [
      12.107410795074443,
      18.96420603234938
    ],
    "verdict": "Fairly Valued",
    "confidence": "low/model-sensitive",
    "historical_pe": {
      "historical_pe_median": null,
      "historical_pe_min": null,
      "historical_pe_max": null
    },
    "sector_relative_pe": null,
    "omission_reason": null,
    "assumptions": {
      "source": "Explicit research policy; rates are sensitivity assumptions, not forecasts. Historical annual FCF CAGR caps growth. No DCF for financial companies.",
      "terminal_growth": 0.02,
      "scenarios": {
        "conservative": {
          "growth_cap": 0,
          "discount_rate": 0.14
        },
        "base": {
          "growth_cap": 0.05,
          "discount_rate": 0.12
        },
        "optimistic": {
          "growth_cap": 0.08,
          "discount_rate": 0.1
        }
      }
    },
    "formulas": "FCF_t=FCF_0*(1+g)^t; PV=sum(FCF_t/(1+r)^t)+FCF_5*(1+terminal)/(r-terminal)/(1+r)^5; per-share equity=PV/shares. FCF is an equity cash-flow proxy; no second net-debt deduction.",
    "historical_fcf_growth": 0.08000000000000007
  },
  "technicals": {
    "trend": "mixed",
    "weekly_trend": "up",
    "support": 153.53725205244325,
    "resistance": 161.06660269934446,
    "entry_range": [
      153.53725205244325,
      155.53725205244325
    ],
    "invalidation": 149.53725205244325,
    "risk_reward": 0.21342931766678785,
    "support_zone": [
      152.53725205244325,
      154.53725205244325
    ],
    "resistance_zone": [
      160.06660269934446,
      162.06660269934446
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points."
  },
  "risk": {
    "critical": [],
    "concerns": [],
    "unverified": [
      "auditor qualifications",
      "pledged promoter shares",
      "business concentration",
      "refinancing maturity schedule",
      "litigation and regulatory exposure",
      "material corporate actions"
    ],
    "note": "Unknown governance information is not a clean audit or low-risk finding."
  },
  "market": {
    "expected_session": null,
    "last_session": "2026-10-19",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 159.03871248284568,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:25.230884+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "market_cap": {
      "value": 15903871.248284569,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:25.230894+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.16666666666666666,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.09375,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": null,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.15,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "debt_equity": {
      "value": 0.1512407104519451,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 2.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.9333333333333333,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": 29.386561536000013,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.1432844333215966,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "fcf": {
      "value": 205705.93075200007,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "eps": {
      "value": 2.203992115200001,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "equity": {
      "value": 1322395.2691200005,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "shares": {
      "value": 100000.0,
      "unit": "shares",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "debt": {
      "value": 200000.0,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 300000.0,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2024-12-31"
      ]
    },
    "eps_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2024-12-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2022-12-31"
      ]
    },
    "eps_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2022-12-31"
      ]
    },
    "revenue_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "2020-12-31"
      ]
    },
    "eps_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "2020-12-31"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 10.285296537600004,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.13116459629492455,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 162.09059367831705,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 159.3590016885118,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 156.35929919160003,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 150.35980734485275,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 161.32196505080327,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 159.553270923942,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 38.75682723385731,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 0.4128363861368314,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 1.095586381076533,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.6827499949397016,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 157.38941114207617,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 166.79177621455793,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 4.0,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.0009991911309892,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 167.07951966276556,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 126.40391407986147,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.0074673223989394355,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.230850+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554790+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554796+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554798+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554800+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554802+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554804+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554805+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554807+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554809+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554811+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554813+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554814+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554816+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554818+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554820+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554821+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554823+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554825+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554827+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.554835+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.012934330738761986,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.554856+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.554864+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": null,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.554927+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.554936+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.554939+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.554942+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.554945+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.230856+00:00",
      "currency": "INR",
      "revenue": 1469328.0768000006,
      "net_income": 220399.21152000007,
      "eps": 2.203992115200001,
      "ebit": 293865.6153600001,
      "interest": 10000,
      "equity": 1322395.2691200005,
      "assets": 2350924.922880001,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 205705.93075200007,
      "ocf": 264479.0538240001,
      "capex": -58773.123072000024,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2024-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.230860+00:00",
      "currency": "INR",
      "revenue": 1360488.9600000002,
      "net_income": 204073.34400000004,
      "eps": 2.0407334400000003,
      "ebit": 272097.7920000001,
      "interest": 10000,
      "equity": 1224440.0640000002,
      "assets": 2176782.3360000006,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 190468.45440000005,
      "ocf": 244888.01280000005,
      "capex": -54419.55840000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2023-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.230861+00:00",
      "currency": "INR",
      "revenue": 1259712.0000000002,
      "net_income": 188956.80000000002,
      "eps": 1.8895680000000001,
      "ebit": 251942.40000000002,
      "interest": 10000,
      "equity": 1133740.8,
      "assets": 2015539.2000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 176359.68000000002,
      "ocf": 226748.16000000003,
      "capex": -50388.48,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2022-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.230863+00:00",
      "currency": "INR",
      "revenue": 1166400.0,
      "net_income": 174960.00000000003,
      "eps": 1.7496,
      "ebit": 233280.00000000003,
      "interest": 10000,
      "equity": 1049760.0,
      "assets": 1866240.0000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 163296.0,
      "ocf": 209952.00000000003,
      "capex": -46656.00000000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2021-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.230864+00:00",
      "currency": "INR",
      "revenue": 1080000.0,
      "net_income": 162000.0,
      "eps": 1.62,
      "ebit": 216000.0,
      "interest": 10000,
      "equity": 972000.0000000001,
      "assets": 1728000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 151200.0,
      "ocf": 194400.0,
      "capex": -43200.0,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2020-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.230866+00:00",
      "currency": "INR",
      "revenue": 1000000.0,
      "net_income": 150000.0,
      "eps": 1.5,
      "ebit": 200000.0,
      "interest": 10000,
      "equity": 900000.0,
      "assets": 1600000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 140000.0,
      "ocf": 180000.0,
      "capex": -40000.0,
      "shares": 100000,
      "dividends": -20000
    }
  ],
  "provider_conflicts": {},
  "warnings": [],
  "news_ids": [],
  "converted_prices": {
    "USD": null,
    "INR": 159.03871248284568
  },
  "changes": {
    "baseline": "First observation"
  }
}
```

## HDFCBANK.NS — INSUFFICIENT DATA
Price: 159.03871248284568 INR | Score: N/A / 100
```json
{
  "ticker": "HDFCBANK.NS",
  "exchange": "NSE",
  "name": "Synthetic HDFC Bank",
  "price": 159.03871248284568,
  "score": null,
  "fair_value": null,
  "currency": "INR",
  "price_timestamp": "2026-10-19T00:00:00+00:00",
  "scores": {
    "total": null,
    "categories": {
      "fundamentals": {
        "score": null,
        "maximum": 30,
        "coverage": 0.2857,
        "details": {
          "roe": {
            "value": 0.16666666666666666,
            "quality": 0.9259259259259259,
            "weight": 2
          },
          "roa": {
            "value": 0.09375,
            "quality": 1,
            "weight": 2
          },
          "nim": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "gnpa": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "nnpa": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "capital_adequacy": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "credit_cost": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "funding_stability": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "valuation": {
        "score": null,
        "maximum": 30,
        "coverage": 0.0,
        "details": {
          "pb_discount_to_peers": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "normalized_roe": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "technicals": {
        "score": null,
        "maximum": 25,
        "coverage": 0.0,
        "details": {
          "above_sma200": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "above_sma50": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "relative_strength_63": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "momentum_63": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "macd_positive": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "weekly_up": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      },
      "risk": {
        "score": null,
        "maximum": 15,
        "coverage": 0.0,
        "details": {
          "capital_adequacy": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "nnpa": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "funding_stability": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "audit_clear": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "pledge_ratio": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          }
        },
        "method": "Linear clamp between bad/good thresholds; weights redistributed only within category"
      }
    },
    "profile": "financial",
    "interpretation": null
  },
  "verdict": "INSUFFICIENT DATA",
  "decision": {
    "verdict": "INSUFFICIENT DATA",
    "reasons": [
      "Stale, undated, or insufficient essential evidence/category coverage"
    ],
    "invalidation": "Obtain current statements, valuation evidence and risk disclosures; rerun"
  },
  "valuation": {
    "metrics": {
      "earnings_yield": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.585423+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.012934330738761986,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.585434+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-12-31",
        "retrieved_at": "2026-10-20T12:19:25.585444+00:00",
        "freshness": "derived",
        "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
        "inputs": [
          "pe",
          "eps_growth_3y"
        ]
      }
    },
    "fair_values": null,
    "margin_of_safety": null,
    "accumulation_range": null,
    "verdict": "N/A",
    "confidence": "low",
    "historical_pe": {
      "historical_pe_median": null,
      "historical_pe_min": null,
      "historical_pe_max": null
    },
    "sector_relative_pe": null,
    "omission_reason": "DCF requires >=4 consistent positive annual FCF periods, shares, same-currency statements and a non-financial sector",
    "assumptions": {
      "source": "Explicit research policy; rates are sensitivity assumptions, not forecasts. Historical annual FCF CAGR caps growth. No DCF for financial companies.",
      "terminal_growth": 0.02,
      "scenarios": {
        "conservative": {
          "growth_cap": 0,
          "discount_rate": 0.14
        },
        "base": {
          "growth_cap": 0.05,
          "discount_rate": 0.12
        },
        "optimistic": {
          "growth_cap": 0.08,
          "discount_rate": 0.1
        }
      }
    },
    "formulas": "FCF_t=FCF_0*(1+g)^t; PV=sum(FCF_t/(1+r)^t)+FCF_5*(1+terminal)/(r-terminal)/(1+r)^5; per-share equity=PV/shares. FCF is an equity cash-flow proxy; no second net-debt deduction."
  },
  "technicals": {
    "trend": "mixed",
    "weekly_trend": "up",
    "support": 153.53725205244325,
    "resistance": 161.06660269934446,
    "entry_range": [
      153.53725205244325,
      155.53725205244325
    ],
    "invalidation": 149.53725205244325,
    "risk_reward": 0.21342931766678785,
    "support_zone": [
      152.53725205244325,
      154.53725205244325
    ],
    "resistance_zone": [
      160.06660269934446,
      162.06660269934446
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points."
  },
  "risk": {
    "critical": [],
    "concerns": [],
    "unverified": [
      "auditor qualifications",
      "pledged promoter shares",
      "business concentration",
      "refinancing maturity schedule",
      "litigation and regulatory exposure",
      "material corporate actions"
    ],
    "note": "Unknown governance information is not a clean audit or low-risk finding."
  },
  "market": {
    "expected_session": null,
    "last_session": "2026-10-19",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 159.03871248284568,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:25.558467+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "market_cap": {
      "value": 15903871.248284569,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2026-10-19T00:00:00+00:00",
      "retrieved_at": "2026-10-20T12:19:25.558481+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.16666666666666666,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.09375,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": null,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.15,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "debt_equity": {
      "value": 0.1512407104519451,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 2.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.9333333333333333,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": 29.386561536000013,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.1432844333215966,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "fcf": {
      "value": 205705.93075200007,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "eps": {
      "value": 2.203992115200001,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "equity": {
      "value": 1322395.2691200005,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "shares": {
      "value": 100000.0,
      "unit": "shares",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "debt": {
      "value": 200000.0,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 300000.0,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2024-12-31"
      ]
    },
    "eps_growth_1y": {
      "value": 0.0800000000000003,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2024-12-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2022-12-31"
      ]
    },
    "eps_growth_3y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2022-12-31"
      ]
    },
    "revenue_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "2020-12-31"
      ]
    },
    "eps_growth_5y": {
      "value": 0.08000000000000007,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "2020-12-31"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 10.285296537600004,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.13116459629492455,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 162.09059367831705,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 159.3590016885118,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 156.35929919160003,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 150.35980734485275,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 161.32196505080327,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 159.553270923942,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 38.75682723385731,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 0.4128363861368314,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 1.095586381076533,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.6827499949397016,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 157.38941114207617,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 166.79177621455793,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 4.0,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.0009991911309892,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 167.07951966276556,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 126.40391407986147,
      "unit": "INR",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.0074673223989394355,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.0,
      "unit": "ratio",
      "source": "SYNTHETIC FIXTURE adjusted OHLCV",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.558405+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585379+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585384+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585387+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585389+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585391+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585393+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585394+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585396+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585398+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585400+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585401+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585403+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585405+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585407+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585409+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585410+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585412+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585413+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585415+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.585423+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.012934330738761986,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.585434+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-12-31",
      "retrieved_at": "2026-10-20T12:19:25.585444+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": null,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-20T12:19:25.585461+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.585469+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.585473+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.585476+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-19",
      "retrieved_at": "2026-10-20T12:19:25.585478+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.558423+00:00",
      "currency": "INR",
      "revenue": 1469328.0768000006,
      "net_income": 220399.21152000007,
      "eps": 2.203992115200001,
      "ebit": 293865.6153600001,
      "interest": 10000,
      "equity": 1322395.2691200005,
      "assets": 2350924.922880001,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 205705.93075200007,
      "ocf": 264479.0538240001,
      "capex": -58773.123072000024,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2024-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.558427+00:00",
      "currency": "INR",
      "revenue": 1360488.9600000002,
      "net_income": 204073.34400000004,
      "eps": 2.0407334400000003,
      "ebit": 272097.7920000001,
      "interest": 10000,
      "equity": 1224440.0640000002,
      "assets": 2176782.3360000006,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 190468.45440000005,
      "ocf": 244888.01280000005,
      "capex": -54419.55840000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2023-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.558429+00:00",
      "currency": "INR",
      "revenue": 1259712.0000000002,
      "net_income": 188956.80000000002,
      "eps": 1.8895680000000001,
      "ebit": 251942.40000000002,
      "interest": 10000,
      "equity": 1133740.8,
      "assets": 2015539.2000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 176359.68000000002,
      "ocf": 226748.16000000003,
      "capex": -50388.48,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2022-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.558431+00:00",
      "currency": "INR",
      "revenue": 1166400.0,
      "net_income": 174960.00000000003,
      "eps": 1.7496,
      "ebit": 233280.00000000003,
      "interest": 10000,
      "equity": 1049760.0,
      "assets": 1866240.0000000002,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 163296.0,
      "ocf": 209952.00000000003,
      "capex": -46656.00000000001,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2021-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.558433+00:00",
      "currency": "INR",
      "revenue": 1080000.0,
      "net_income": 162000.0,
      "eps": 1.62,
      "ebit": 216000.0,
      "interest": 10000,
      "equity": 972000.0000000001,
      "assets": 1728000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 151200.0,
      "ocf": 194400.0,
      "capex": -43200.0,
      "shares": 100000,
      "dividends": -20000
    },
    {
      "period": "2020-12-31",
      "source": "SYNTHETIC FIXTURE",
      "retrieved_at": "2026-10-20T12:19:25.558434+00:00",
      "currency": "INR",
      "revenue": 1000000.0,
      "net_income": 150000.0,
      "eps": 1.5,
      "ebit": 200000.0,
      "interest": 10000,
      "equity": 900000.0,
      "assets": 1600000.0,
      "current_liabilities": 300000,
      "current_assets": 600000,
      "debt": 200000,
      "cash": 300000,
      "fcf": 140000.0,
      "ocf": 180000.0,
      "capex": -40000.0,
      "shares": 100000,
      "dividends": -20000
    }
  ],
  "provider_conflicts": {},
  "warnings": [],
  "news_ids": [],
  "converted_prices": {
    "USD": null,
    "INR": 159.03871248284568
  },
  "changes": {
    "baseline": "First observation"
  }
}
```