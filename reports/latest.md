# Daily equity research
2026-11-08T15:02:52.740778+05:30
Research and decision support; no order execution.

## AAPL — INSUFFICIENT DATA
Price: 342.37 USD | Score: N/A / 100
```json
{
  "ticker": "AAPL",
  "exchange": "NASDAQ",
  "name": "Apple Inc.",
  "price": 342.37,
  "score": null,
  "fair_value": 107.89030830441632,
  "currency": "USD",
  "price_timestamp": "2026-11-06T21:00:01+00:00",
  "scores": {
    "total": null,
    "categories": {
      "fundamentals": {
        "score": 27.71,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 1.17915480895328,
            "quality": 1,
            "weight": 2
          },
          "roce": {
            "value": 0.6736605677803208,
            "quality": 1,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.1505979656911629,
            "quality": 1,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.07701326503022221,
            "quality": 0.5134217668681481,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "eps_growth_3y": {
            "value": 0.13572177900514792,
            "quality": 0.9048118600343196,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": 0.3300997840587761,
            "quality": 1,
            "weight": 1
          },
          "net_margin": {
            "value": 0.27603511864236874,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 1.0293625874787213,
            "quality": 1,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 8.654411296991286,
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
        "score": 5.04,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.02622893374007415,
            "quality": 0.3278616717509269,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.0273458343741998,
            "quality": 0.3418229296774975,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -2.173315614540566,
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
        "score": 22.57,
        "maximum": 25,
        "coverage": 1.0,
        "details": {
          "above_sma200": {
            "value": 1.0,
            "quality": 1,
            "weight": 3
          },
          "above_sma50": {
            "value": 1.0,
            "quality": 1,
            "weight": 2
          },
          "relative_strength_63": {
            "value": 0.16730115042599114,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.11065329355402564,
            "quality": 0.8688443118467523,
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
        "score": null,
        "maximum": 15,
        "coverage": 0.5,
        "details": {
          "debt_equity": {
            "value": 0.7146833432952995,
            "quality": 0.6426583283523503,
            "weight": 3
          },
          "interest_coverage": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "current_ratio": {
            "value": 1.0231998352117235,
            "quality": 0.34879989014114904,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.1397060680172402,
            "quality": 0.8602939319827598,
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
        "value": 0.02622893374007415,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-09-30",
        "retrieved_at": "2026-11-08T09:32:55.048495+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.0273458343741998,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-09-30",
        "retrieved_at": "2026-11-08T09:32:55.048520+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 2.8091169508287903,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-09-30",
        "retrieved_at": "2026-11-08T09:32:55.048532+00:00",
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
        "value": 73.47299960613066,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 107.89030830441632,
        "growth": 0.05,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 153.22498604940236,
        "growth": 0.08,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": -2.173315614540566,
    "accumulation_range": [
      55.10474970459799,
      86.31224664353306
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
    "historical_fcf_growth": 0.10962451744460999
  },
  "technicals": {
    "trend": "up",
    "weekly_trend": "up",
    "support": 341.0299987792969,
    "resistance": 342.989990234375,
    "entry_range": [
      341.0299987792969,
      345.41527603480193
    ],
    "invalidation": 332.2594442682867,
    "risk_reward": 0.061321596266429405,
    "support_zone": [
      338.8373601515443,
      343.22263740704943
    ],
    "resistance_zone": [
      340.79735160662244,
      345.18262886212756
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [
      "Yahoo news unavailable"
    ],
    "llm": {
      "status": "disabled"
    }
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
    "expected_session": "2026-11-06",
    "last_session": "2026-11-06",
    "stale": false,
    "condition": "holiday/weekend",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 342.37,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 38.125835,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 32.412743,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 44.388695,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 29.234,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 1.17915480895328,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.3267226633180735,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": 0.3300997840587761,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.27603511864236874,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 4975383019520.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 14532259000.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.016549999,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.118,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 8.98,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "fcf": {
      "value": 136056000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 5013140144128.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 80111000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 36305000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "debt_equity": {
      "value": 0.7146833432952995,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 1.0231998352117235,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 1.0293625874787213,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.6736605677803208,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "equity": {
      "value": 112093000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.1505979656911629,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2025-09-30"
      ]
    },
    "eps_growth_1y": {
      "value": 0.20375335120643445,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2025-09-30"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.07701326503022221,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2023-09-30"
      ]
    },
    "eps_growth_3y": {
      "value": 0.13572177900514792,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2023-09-30"
      ]
    },
    "revenue_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "missing"
      ]
    },
    "eps_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "missing"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 8.654411296991286,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.1397060680172402,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 343.38450012207034,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 336.01380126953126,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 323.6724743652344,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 298.53540496826173,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 342.00818356947826,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 335.4922033127596,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 51.464314604094305,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 2.068660966402433,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 2.837776736221484,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.7691157698190509,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 335.4674812217084,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 351.3015190224323,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 8.770554511010163,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.9239058729131295,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 355.3800048828125,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 242.75922413209136,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.11065329355402564,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.16730115042599114,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048404+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048415+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048426+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048429+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048433+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048436+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048439+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048442+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048445+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048449+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048452+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048455+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048458+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048461+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048465+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048468+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048471+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048475+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048477+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.02622893374007415,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:55.048495+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.0273458343741998,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:55.048520+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 2.8091169508287903,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-08T09:32:55.048532+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -2.173315614540566,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.048649+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.048662+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.048669+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.048674+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.048679+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "currency": "USD",
      "revenue": 478834000000.0,
      "net_income": 132175000000.0,
      "eps": 8.98,
      "ebit": 158063000000.0,
      "equity": 112093000000.0,
      "debt": 80111000000.0,
      "cash": 36305000000.0,
      "assets": 404548000000.0,
      "current_liabilities": 169915000000.0,
      "current_assets": 173857000000.0,
      "ocf": 145097000000.0,
      "capex": -9041000000.0,
      "fcf": 136056000000.0,
      "shares": 14532259000.0,
      "dividends": -15721000000.0,
      "operating_income": 158063000000.0,
      "inventory": 14541000000.0,
      "receivables": 83713000000.0
    },
    {
      "period": "2025-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "currency": "USD",
      "revenue": 416161000000.0,
      "net_income": 112010000000.0,
      "eps": 7.46,
      "ebit": 133050000000.0,
      "equity": 73733000000.0,
      "debt": 98657000000.0,
      "cash": 35934000000.0,
      "assets": 359241000000.0,
      "current_liabilities": 165631000000.0,
      "current_assets": 147957000000.0,
      "ocf": 111482000000.0,
      "capex": -12715000000.0,
      "fcf": 98767000000.0,
      "shares": 14773260000.0,
      "dividends": -15421000000.0,
      "operating_income": 133050000000.0,
      "inventory": 5718000000.0,
      "receivables": 72957000000.0
    },
    {
      "period": "2024-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "currency": "USD",
      "revenue": 391035000000.0,
      "net_income": 93736000000.0,
      "eps": 6.08,
      "ebit": 123216000000.0,
      "equity": 56950000000.0,
      "debt": 106629000000.0,
      "cash": 29943000000.0,
      "assets": 364980000000.0,
      "current_liabilities": 176392000000.0,
      "current_assets": 152987000000.0,
      "ocf": 118254000000.0,
      "capex": -9447000000.0,
      "fcf": 108807000000.0,
      "shares": 15116786000.0,
      "dividends": -15234000000.0,
      "operating_income": 123216000000.0,
      "inventory": 7286000000.0,
      "receivables": 66243000000.0
    },
    {
      "period": "2023-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "currency": "USD",
      "revenue": 383285000000.0,
      "net_income": 96995000000.0,
      "eps": 6.13,
      "ebit": 114301000000.0,
      "interest": 3933000000.0,
      "equity": 62146000000.0,
      "debt": 111088000000.0,
      "cash": 29965000000.0,
      "assets": 352583000000.0,
      "current_liabilities": 145308000000.0,
      "current_assets": 143566000000.0,
      "ocf": 110543000000.0,
      "capex": -10959000000.0,
      "fcf": 99584000000.0,
      "shares": 15550061000.0,
      "dividends": -15025000000.0,
      "operating_income": 114301000000.0,
      "inventory": 6331000000.0,
      "receivables": 60985000000.0
    },
    {
      "period": "2022-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:53.520092+00:00",
      "currency": "USD",
      "interest": 2931000000.0
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 342.37,
    "INR": 32151.967953796386
  },
  "changes": {
    "new_news": []
  }
}
```

## MSFT — HOLD / REVIEW
Price: 530.61 USD | Score: 66.77 / 100
```json
{
  "ticker": "MSFT",
  "exchange": "NASDAQ",
  "name": "Microsoft Corporation",
  "price": 530.61,
  "score": 66.77,
  "fair_value": 99.97805431900618,
  "currency": "USD",
  "price_timestamp": "2026-11-06T21:00:01+00:00",
  "scores": {
    "total": 66.77,
    "categories": {
      "fundamentals": {
        "score": 27.86,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 0.30233483352811,
            "quality": 1,
            "weight": 2
          },
          "roce": {
            "value": 0.2866333871030666,
            "quality": 1,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.17788686799846665,
            "quality": 1,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.1612397915820203,
            "quality": 1,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "eps_growth_3y": {
            "value": 0.22855998285745227,
            "quality": 1,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": 0.4678081840892722,
            "quality": 1,
            "weight": 1
          },
          "net_margin": {
            "value": 0.4030538905915218,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 0.5008411277841329,
            "quality": 0.5008411277841329,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 2.5330686330119114,
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
        "score": 4.62,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.03610938428011176,
            "quality": 0.45136730350139703,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.016999995458360118,
            "quality": 0.21249994322950147,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -4.307264715383936,
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
        "score": 21.8,
        "maximum": 25,
        "coverage": 1.0,
        "details": {
          "above_sma200": {
            "value": 1.0,
            "quality": 1,
            "weight": 3
          },
          "above_sma50": {
            "value": 1.0,
            "quality": 1,
            "weight": 2
          },
          "relative_strength_63": {
            "value": 0.10406490196801044,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.050485831544563986,
            "quality": 0.6682861051485466,
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
        "score": 12.49,
        "maximum": 15,
        "coverage": 0.7143,
        "details": {
          "debt_equity": {
            "value": 0.12845314170624364,
            "quality": 0.9357734291468782,
            "weight": 3
          },
          "interest_coverage": {
            "value": 55.38675843985578,
            "quality": 1,
            "weight": 3
          },
          "current_ratio": {
            "value": 1.2303272619576484,
            "quality": 0.48688484130509896,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.22824538621011642,
            "quality": 0.7717546137898836,
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
    "interpretation": "Watchlist"
  },
  "verdict": "HOLD / REVIEW",
  "decision": {
    "verdict": "HOLD / REVIEW",
    "reasons": [
      "Watchlist",
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
        "value": 0.03610938428011176,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-11-08T09:32:56.232935+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.016999995458360118,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-11-08T09:32:56.232960+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 1.2116570737263268,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-11-08T09:32:56.232973+00:00",
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
        "value": 70.76791813130608,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 99.97805431900618,
        "growth": 0.040443958087982956,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 125.3153383345392,
        "growth": 0.040443958087982956,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": -4.307264715383936,
    "accumulation_range": [
      53.07593859847955,
      79.98244345520494
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
    "historical_fcf_growth": 0.040443958087982956
  },
  "technicals": {
    "trend": "up",
    "weekly_trend": "up",
    "support": 524.4299926757812,
    "resistance": 535.6900024414062,
    "entry_range": [
      524.4299926757812,
      532.1490287360293
    ],
    "invalidation": 508.99192055528516,
    "risk_reward": 0.23498944691471813,
    "support_zone": [
      520.5704746456572,
      528.2895107059053
    ],
    "resistance_zone": [
      531.8304844112822,
      539.5495204715303
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [
      "Yahoo news unavailable"
    ],
    "llm": {
      "status": "disabled"
    }
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
    "expected_session": "2026-11-06",
    "last_session": "2026-11-06",
    "stale": false,
    "condition": "holiday/weekend",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 530.61,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 27.693632,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 21.944775,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 8.375716,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 19.494,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.30233483352811,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.17636238488559763,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": 0.4678081840892722,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.4030538905915218,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 3940412817408.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 7428434704.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.00079,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.19,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 17.95,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "fcf": {
      "value": 66987000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 4009835102208.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-06T21:00:01+00:00",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 56826000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 20935000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "debt_equity": {
      "value": 0.12845314170624364,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 1.2303272619576484,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.5008411277841329,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": 55.38675843985578,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.2866333871030666,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "equity": {
      "value": 442387000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.17788686799846665,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2025-06-30"
      ]
    },
    "eps_growth_1y": {
      "value": 0.31598240469208205,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2025-06-30"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.1612397915820203,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2023-06-30"
      ]
    },
    "eps_growth_3y": {
      "value": 0.22855998285745227,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2023-06-30"
      ]
    },
    "revenue_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "missing"
      ]
    },
    "eps_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "missing"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 2.5330686330119114,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.22824538621011642,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 531.4075012207031,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 516.64580078125,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 471.9562683105469,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 438.8461834716797,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 528.3094191349965,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 513.14104905266,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 52.147724271944895,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 4.383007272742816,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 4.974342832899419,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.5913355601566028,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 511.9940971544979,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 550.8209052869083,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 15.438072120496113,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.0697488700751747,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 559.1500244140625,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 348.54386902384044,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.050485831544563986,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.10406490196801044,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232848+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232859+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232865+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232868+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232872+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232875+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232879+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232883+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232886+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232890+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232893+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232896+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232899+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232902+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232905+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232909+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232912+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232915+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.232918+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.03610938428011176,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:56.232935+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.016999995458360118,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:56.232960+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 1.2116570737263268,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-08T09:32:56.232973+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -4.307264715383936,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.233080+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:56.233095+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:56.233100+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:56.233106+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-06",
      "retrieved_at": "2026-11-08T09:32:56.233111+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "currency": "USD",
      "revenue": 331839000000.0,
      "net_income": 133749000000.0,
      "eps": 17.95,
      "ebit": 168985000000.0,
      "interest": 3051000000.0,
      "equity": 442387000000.0,
      "debt": 56826000000.0,
      "cash": 20935000000.0,
      "assets": 758376000000.0,
      "current_liabilities": 168825000000.0,
      "current_assets": 207710000000.0,
      "ocf": 182935000000.0,
      "capex": -115948000000.0,
      "fcf": 66987000000.0,
      "shares": 7428434704.0,
      "dividends": -26445000000.0,
      "operating_income": 155237000000.0,
      "inventory": 1397000000.0,
      "receivables": 80876000000.0
    },
    {
      "period": "2025-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "currency": "USD",
      "revenue": 281724000000.0,
      "net_income": 101832000000.0,
      "eps": 13.64,
      "ebit": 126012000000.0,
      "interest": 2385000000.0,
      "equity": 343479000000.0,
      "debt": 60588000000.0,
      "cash": 30242000000.0,
      "assets": 619003000000.0,
      "current_liabilities": 141218000000.0,
      "current_assets": 191131000000.0,
      "ocf": 136162000000.0,
      "capex": -64551000000.0,
      "fcf": 71611000000.0,
      "shares": 7434158655.0,
      "dividends": -24082000000.0,
      "operating_income": 128528000000.0,
      "inventory": 938000000.0,
      "receivables": 69905000000.0
    },
    {
      "period": "2024-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "currency": "USD",
      "revenue": 245122000000.0,
      "net_income": 88136000000.0,
      "eps": 11.8,
      "ebit": 110722000000.0,
      "interest": 2935000000.0,
      "equity": 268477000000.0,
      "debt": 67127000000.0,
      "cash": 18315000000.0,
      "assets": 512163000000.0,
      "current_liabilities": 125286000000.0,
      "current_assets": 159734000000.0,
      "ocf": 118548000000.0,
      "capex": -44477000000.0,
      "fcf": 74071000000.0,
      "shares": 7434138859.0,
      "dividends": -21771000000.0,
      "operating_income": 109433000000.0,
      "inventory": 1246000000.0,
      "receivables": 56924000000.0
    },
    {
      "period": "2023-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "currency": "USD",
      "revenue": 211915000000.0,
      "net_income": 72361000000.0,
      "eps": 9.68,
      "ebit": 91279000000.0,
      "interest": 1968000000.0,
      "equity": 206223000000.0,
      "debt": 59965000000.0,
      "cash": 34704000000.0,
      "assets": 411976000000.0,
      "current_liabilities": 104149000000.0,
      "current_assets": 184257000000.0,
      "ocf": 87582000000.0,
      "capex": -28107000000.0,
      "fcf": 59475000000.0,
      "shares": 7432000000.0,
      "dividends": -19800000000.0,
      "operating_income": 88523000000.0,
      "inventory": 2500000000.0,
      "receivables": 48688000000.0
    },
    {
      "period": "2022-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:55.275455+00:00",
      "currency": "USD"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 530.61,
    "INR": 49829.587043151856
  },
  "changes": {
    "fair_value": {
      "previous": 99.99736748912113,
      "current": 99.97805431900618,
      "delta": -0.01931317011495537
    },
    "new_news": []
  }
}
```

## TCS.NS — INSUFFICIENT DATA
Price: 2498.5 INR | Score: N/A / 100
```json
{
  "ticker": "TCS.NS",
  "exchange": "NSE",
  "name": "Tata Consultancy Services Limited",
  "price": 2498.5,
  "score": null,
  "fair_value": 1527.17671499812,
  "currency": "INR",
  "price_timestamp": "2026-11-08T09:32:55+00:00",
  "scores": {
    "total": null,
    "categories": {
      "fundamentals": {
        "score": 23.14,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 0.45887728459530025,
            "quality": 1,
            "weight": 2
          },
          "roce": {
            "value": 0.5492762930395693,
            "quality": 1,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.04581237956478823,
            "quality": 0.47906189782394115,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.05801848619364591,
            "quality": 0.38678990795763946,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "eps_growth_3y": {
            "value": 0.0569441047959276,
            "quality": 0.379627365306184,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": 0.2509989850985503,
            "quality": 1,
            "weight": 1
          },
          "net_margin": {
            "value": 0.1842926211796076,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 0.9743548059337533,
            "quality": 0.9743548059337533,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 1.2158125618074398,
            "quality": 0.2158125618074398,
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
        "coverage": 0.4167,
        "details": {
          "earnings_yield": {
            "value": 0.05709826176903662,
            "quality": 0.7137282721129578,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.053041046228127,
            "quality": 0.6630130778515875,
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
        "score": 14.58,
        "maximum": 15,
        "coverage": 0.7143,
        "details": {
          "debt_equity": {
            "value": 0.10521260723610593,
            "quality": 0.947393696381947,
            "weight": 3
          },
          "interest_coverage": {
            "value": 54.37163814180929,
            "quality": 1,
            "weight": 3
          },
          "current_ratio": {
            "value": 2.2278129822372525,
            "quality": 1,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.059781621958506406,
            "quality": 0.9402183780414936,
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
        "value": 0.05709826176903662,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-08T09:32:58.173090+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.053041046228127,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-08T09:32:58.173115+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 3.075589310388545,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-08T09:32:58.173129+00:00",
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
        "value": 1040.0030915006273,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 1527.17671499812,
        "growth": 0.05,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 2103.4464451809217,
        "growth": 0.07251639943779664,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": null,
    "accumulation_range": [
      780.0023186254705,
      1221.7413719984959
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
    "historical_fcf_growth": 0.07251639943779664
  },
  "technicals": {
    "trend": "mixed",
    "weekly_trend": "up",
    "support": 2420.0,
    "resistance": 2549.89990234375,
    "entry_range": [
      2420.0,
      2454.014164261499
    ],
    "invalidation": 2351.9716714770025,
    "risk_reward": 0.3507847449149249,
    "support_zone": [
      2402.9929178692505,
      2437.0070821307495
    ],
    "resistance_zone": [
      2532.8928202130005,
      2566.9069844744995
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [
      "Yahoo news unavailable"
    ],
    "llm": {
      "status": "disabled"
    }
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
    "last_session": "2026-11-08",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 2498.5,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 17.513668,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 15.506086,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 7.5973654,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 11.886,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.45887728459530025,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.26983308841269493,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": 0.2509989850985503,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.1842926211796076,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 9039791521792.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 3618087518.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.71794,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.4557,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 136.01,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "fcf": {
      "value": 479480000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 8658971787264.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:55+00:00",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 112830000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 64050000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "debt_equity": {
      "value": 0.10521260723610593,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 2.2278129822372525,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.9743548059337533,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": 54.37163814180929,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.5492762930395693,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "equity": {
      "value": 1072400000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.04581237956478823,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2025-03-31"
      ]
    },
    "eps_growth_1y": {
      "value": 0.013562858633281216,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2025-03-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.05801848619364591,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2023-03-31"
      ]
    },
    "eps_growth_3y": {
      "value": 0.0569441047959276,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2023-03-31"
      ]
    },
    "revenue_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "missing"
      ]
    },
    "eps_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "missing"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 1.2158125618074398,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.059781621958506406,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 2445.988146972656,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 2280.5071728515627,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 2253.7996411132813,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 2375.7866931152344,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 2426.6353013255502,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 2335.6091964844245,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 63.232688006784166,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 71.45077548976451,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 76.7217478622923,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -5.270972372527794,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 2235.1369791391444,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 2656.8393148061677,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 68.02832852299768,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.03989269134371181,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 3269.7790009998616,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 1955.6242634941125,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.024088636849197043,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.003956943393601531,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173002+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173013+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173018+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173022+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173025+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173028+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173032+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173035+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173038+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173042+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173045+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173049+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173052+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173055+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173058+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173062+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173065+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173068+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.173072+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.05709826176903662,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.173090+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.053041046228127,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.173115+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 3.075589310388545,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.173129+00:00",
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
      "retrieved_at": "2026-11-08T09:32:58.173229+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.173245+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.173251+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.173256+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.173261+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "currency": "INR",
      "revenue": 2670210000000.0,
      "net_income": 492100000000.0,
      "eps": 136.01,
      "ebit": 667140000000.0,
      "interest": 12270000000.0,
      "equity": 1072400000000.0,
      "debt": 112830000000.0,
      "cash": 64050000000.0,
      "assets": 1823720000000.0,
      "current_liabilities": 609140000000.0,
      "current_assets": 1357050000000.0,
      "ocf": 520940000000.0,
      "capex": -41460000000.0,
      "fcf": 479480000000.0,
      "shares": 3618087518.0,
      "dividends": -394370000000.0,
      "operating_income": 670220000000.0,
      "inventory": 290000000.0
    },
    {
      "period": "2025-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "currency": "INR",
      "revenue": 2553240000000.0,
      "net_income": 485530000000.0,
      "eps": 134.19,
      "ebit": 661270000000.0,
      "interest": 7960000000.0,
      "equity": 947560000000.0,
      "debt": 93920000000.0,
      "cash": 83310000000.0,
      "assets": 1596290000000.0,
      "current_liabilities": 530010000000.0,
      "current_assets": 1230110000000.0,
      "ocf": 489080000000.0,
      "capex": -39370000000.0,
      "fcf": 449710000000.0,
      "shares": 3618087518.0,
      "dividends": -448640000000.0,
      "operating_income": 622930000000.0,
      "inventory": 210000000.0
    },
    {
      "period": "2024-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "currency": "INR",
      "revenue": 2408930000000.0,
      "net_income": 459080000000.0,
      "eps": 125.88,
      "ebit": 627750000000.0,
      "interest": 7780000000.0,
      "equity": 904890000000.0,
      "debt": 80210000000.0,
      "cash": 90070000000.0,
      "assets": 1464490000000.0,
      "current_liabilities": 461040000000.0,
      "current_assets": 1129840000000.0,
      "ocf": 443380000000.0,
      "capex": -26740000000.0,
      "fcf": 416640000000.0,
      "shares": 3618087518.0,
      "dividends": -251370000000.0,
      "operating_income": 594250000000.0,
      "inventory": 280000000.0
    },
    {
      "period": "2023-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "currency": "INR",
      "revenue": 2254580000000.0,
      "net_income": 421470000000.0,
      "eps": 115.19,
      "ebit": 576860000000.0,
      "interest": 7790000000.0,
      "equity": 904240000000.0,
      "debt": 76880000000.0,
      "cash": 71150000000.0,
      "assets": 1436510000000.0,
      "current_liabilities": 435580000000.0,
      "current_assets": 1102700000000.0,
      "ocf": 419650000000.0,
      "capex": -31000000000.0,
      "fcf": 388650000000.0,
      "shares": 3659051373.0,
      "dividends": -413470000000.0,
      "operating_income": 543770000000.0,
      "inventory": 280000000.0
    },
    {
      "period": "2022-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:56.455580+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 26.605259318162393,
    "INR": 2498.5
  },
  "changes": {
    "new_news": []
  }
}
```

## HDFCBANK.NS — INSUFFICIENT DATA
Price: 788.25 INR | Score: N/A / 100
```json
{
  "ticker": "HDFCBANK.NS",
  "exchange": "NSE",
  "name": "HDFC Bank Limited",
  "price": 788.25,
  "score": null,
  "fair_value": null,
  "currency": "INR",
  "price_timestamp": "2026-11-08T09:32:56+00:00",
  "scores": {
    "total": null,
    "categories": {
      "fundamentals": {
        "score": null,
        "maximum": 30,
        "coverage": 0.2857,
        "details": {
          "roe": {
            "value": 0.0862935303390961,
            "quality": 0.47940850188386724,
            "weight": 2
          },
          "roa": {
            "value": 0.013393717571573425,
            "quality": 0.6696858785786712,
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
        "value": 0.058039965972328744,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-08T09:32:59.408114+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.08761361840111405,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-08T09:32:59.408136+00:00",
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
        "period": "2026-03-31",
        "retrieved_at": "2026-11-08T09:32:59.408149+00:00",
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
    "support": 722.0,
    "resistance": null,
    "entry_range": [
      722.0,
      730.4427219235195
    ],
    "invalidation": 705.114556152961,
    "risk_reward": null,
    "support_zone": [
      717.7786390382403,
      726.2213609617597
    ],
    "resistance_zone": null,
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [
      "Yahoo news unavailable"
    ],
    "llm": {
      "status": "disabled"
    }
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
    "last_session": "2026-11-08",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 788.25,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 17.229507,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 12.591853,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 1.9963834,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.0862935303390961,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.013393717571573425,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
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
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.282412428988016,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 12164505010176.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 15393260762.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.0028600001,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.24040002,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 45.75,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "fcf": {
      "value": 1065776300000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 15688790966272.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-08T09:32:56+00:00",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 6643640400000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 3650673900000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "debt_equity": {
      "value": 0.8134343829261803,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 1.5121825771921247,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "fcf / net_income",
      "inputs": [
        "fcf",
        "net_income"
      ]
    },
    "interest_coverage": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "equity": {
      "value": 8167395600000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.0523334897176404,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2025-03-31"
      ]
    },
    "eps_growth_1y": {
      "value": 0.020749665327978617,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2025-03-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.27453553237474115,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2023-03-31"
      ]
    },
    "eps_growth_3y": {
      "value": -0.19797395587817435,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2023-03-31"
      ]
    },
    "revenue_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_5y_ago)^(1/5) - 1",
      "inputs": [
        "revenue",
        "missing"
      ]
    },
    "eps_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_5y_ago)^(1/5) - 1",
      "inputs": [
        "eps",
        "missing"
      ]
    },
    "earnings_consistency": {
      "value": 1.0,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 4.864998982061458,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.12794953761896946,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 715.9724975585938,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 714.917998046875,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 740.6064361572265,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 777.1061724853515,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 725.559211992158,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 722.57198199524,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 73.93644222949433,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 12.958808253735015,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 1.665333777553852,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 11.293474476181164,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 653.8117320339691,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 778.1332630832185,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 16.885443847039014,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.16183007510630687,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 1000.9449320171519,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 669.2000122070312,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.07831737346101231,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.05711964307983197,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408032+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408042+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408046+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408050+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408053+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408056+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408059+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408063+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408066+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408069+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408072+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408076+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408079+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408082+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408085+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408089+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408092+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408095+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-08T09:32:59.408098+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.058039965972328744,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:59.408114+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.08761361840111405,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:59.408136+00:00",
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
      "period": "2026-03-31",
      "retrieved_at": "2026-11-08T09:32:59.408149+00:00",
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
      "retrieved_at": "2026-11-08T09:32:59.408177+00:00",
      "freshness": "derived",
      "formula": "1 - price/base fair value",
      "inputs": [
        "price",
        "fcf",
        "shares"
      ]
    },
    "above_sma50": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:59.408189+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:59.408194+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:59.408199+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-08",
      "retrieved_at": "2026-11-08T09:32:59.408204+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "currency": "INR",
      "revenue": 2495617500000.0,
      "net_income": 704793400000.0,
      "eps": 45.75,
      "interest": 1860495500000.0,
      "equity": 8167395600000.0,
      "debt": 6643640400000.0,
      "cash": 3650673900000.0,
      "assets": 52621193200000.0,
      "ocf": 1118559900000.0,
      "capex": -52783600000.0,
      "fcf": 1065776300000.0,
      "shares": 15393260762.0,
      "dividends": -219070200000.0,
      "receivables": 458840400000.0
    },
    {
      "period": "2025-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "currency": "INR",
      "revenue": 2371508200000.0,
      "net_income": 673508300000.0,
      "eps": 44.82,
      "interest": 1823477000000.0,
      "equity": 7676891400000.0,
      "debt": 7326106100000.0,
      "cash": 3222323100000.0,
      "assets": 48187671100000.0,
      "ocf": 1195617400000.0,
      "capex": -66397300000.0,
      "fcf": 1129220100000.0,
      "shares": 15304409210.0,
      "dividends": -158058100000.0,
      "receivables": 454645400000.0
    },
    {
      "period": "2024-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "currency": "INR",
      "revenue": 1986934300000.0,
      "net_income": 622656600000.0,
      "eps": 44.16,
      "interest": 1533922800000.0,
      "equity": 6947327400000.0,
      "debt": 8093552100000.0,
      "cash": 3425973300000.0,
      "assets": 44118573000000.0,
      "ocf": 1022322400000.0,
      "capex": -53838000000.0,
      "fcf": 968484400000.0,
      "shares": 15193797254.0,
      "dividends": -86617100000.0,
      "receivables": 379127800000.0
    },
    {
      "period": "2023-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-08T09:32:58.395349+00:00",
      "currency": "INR",
      "revenue": 1205375000000.0,
      "net_income": 495446900000.0,
      "eps": 88.68,
      "interest": 775538200000.0,
      "equity": 2912200700000.0,
      "debt": 3151792800000.0,
      "cash": 2363920200000.0,
      "assets": 25755624000000.0,
      "ocf": 477200600000.0,
      "capex": -43620300000.0,
      "fcf": 433580300000.0,
      "shares": 11159485572.0,
      "dividends": -86394300000.0,
      "receivables": 278751200000.0
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 8.39367446769722,
    "INR": 788.25
  },
  "changes": {
    "new_news": []
  }
}
```