# Daily equity research
2026-10-22T13:29:21.649311+05:30
Research and decision support; no order execution.

## AAPL — INSUFFICIENT DATA
Price: 343.99 USD | Score: N/A / 100
```json
{
  "ticker": "AAPL",
  "exchange": "NASDAQ",
  "name": "Apple Inc.",
  "price": 343.99,
  "score": null,
  "fair_value": 53.22803763470469,
  "currency": "USD",
  "price_timestamp": "2026-10-21T20:00:01+00:00",
  "scores": {
    "total": null,
    "categories": {
      "fundamentals": {
        "score": 23.65,
        "maximum": 30,
        "coverage": 0.8235,
        "details": {
          "roe": {
            "value": 1.5191298333175105,
            "quality": 1,
            "weight": 2
          },
          "roce": {
            "value": 0.6872062393471412,
            "quality": 1,
            "weight": 2
          },
          "revenue_growth_1y": {
            "value": 0.06425511782832749,
            "quality": 0.5712755891416375,
            "weight": 1
          },
          "revenue_growth_3y": {
            "value": 0.01812535743479393,
            "quality": 0.12083571623195954,
            "weight": 2
          },
          "revenue_growth_5y": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "eps_growth_3y": {
            "value": 0.06880679389561806,
            "quality": 0.4587119593041204,
            "weight": 1
          },
          "earnings_consistency": {
            "value": 1.0,
            "quality": 1,
            "weight": 1
          },
          "operating_margin": {
            "value": 0.31970799762591884,
            "quality": 1,
            "weight": 1
          },
          "net_margin": {
            "value": 0.2691506412181824,
            "quality": 1,
            "weight": 1
          },
          "fcf_conversion": {
            "value": 0.8817694848674226,
            "quality": 0.8817694848674226,
            "weight": 2
          },
          "dividend_fcf_coverage": {
            "value": 6.404707865897153,
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
        "score": 4.11,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.025349577004283315,
            "quality": 0.3168697125535414,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.019673713156074284,
            "quality": 0.24592141445092855,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -5.4625715184307015,
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
        "score": 19.81,
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
            "value": 0.022205848657842253,
            "quality": 0.6110292432892113,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.07034335437614003,
            "quality": 0.7344778479204668,
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
            "value": 1.3380304612588665,
            "quality": 0.33098476937056676,
            "weight": 3
          },
          "interest_coverage": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
          },
          "current_ratio": {
            "value": 0.8932929222186667,
            "quality": 0.26219528147911114,
            "weight": 2
          },
          "earnings_volatility": {
            "value": 0.0686518404091043,
            "quality": 0.9313481595908957,
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
        "value": 0.025349577004283315,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-22T07:59:23.539050+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.019673713156074284,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-22T07:59:23.539082+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 5.733211470344684,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-22T07:59:23.539099+00:00",
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
        "value": 44.721791266313055,
        "growth": -0.039450634871626145,
        "discount_rate": 0.14
      },
      "base": {
        "value": 53.22803763470469,
        "growth": -0.039450634871626145,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 65.9485301866353,
        "growth": -0.039450634871626145,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": -5.4625715184307015,
    "accumulation_range": [
      33.54134344973479,
      42.582430107763756
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
    "historical_fcf_growth": -0.039450634871626145
  },
  "technicals": {
    "trend": "up",
    "weekly_trend": "up",
    "support": 334.29998779296875,
    "resistance": 344.2730974331505,
    "entry_range": [
      334.29998779296875,
      337.5362057832987
    ],
    "invalidation": 327.8275518123088,
    "risk_reward": 0.01751636673764381,
    "support_zone": [
      332.6818787978038,
      335.9180967881337
    ],
    "resistance_zone": [
      342.65498843798554,
      345.89120642831546
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [],
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
    "expected_session": "2026-10-21",
    "last_session": "2026-10-21",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 343.99,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 39.44839,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 35.94199,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 46.73777,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 30.02,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 1.5191298333175105,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "net_income / equity",
      "inputs": [
        "net_income",
        "equity"
      ]
    },
    "roa": {
      "value": 0.3117962593356549,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "net_income / assets",
      "inputs": [
        "net_income",
        "assets"
      ]
    },
    "operating_margin": {
      "value": 0.31970799762591884,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.2691506412181824,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 5020252110848.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 14773260000.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.01648,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.1204,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 7.46,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "eps"
      ]
    },
    "fcf": {
      "value": 98767000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 5042197233664.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 98657000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "debt"
      ]
    },
    "cash": {
      "value": 35934000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "cash"
      ]
    },
    "debt_equity": {
      "value": 1.3380304612588665,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "debt / equity",
      "inputs": [
        "debt",
        "equity"
      ]
    },
    "current_ratio": {
      "value": 0.8932929222186667,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "current_assets / current_liabilities",
      "inputs": [
        "current_assets",
        "current_liabilities"
      ]
    },
    "fcf_conversion": {
      "value": 0.8817694848674226,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "ebit / interest",
      "inputs": [
        "ebit",
        "interest"
      ]
    },
    "roce": {
      "value": 0.6872062393471412,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "EBIT / (assets - current liabilities)",
      "inputs": [
        "ebit",
        "assets",
        "current_liabilities"
      ]
    },
    "equity": {
      "value": 73733000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.06425511782832749,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_1y_ago)^(1/1) - 1",
      "inputs": [
        "revenue",
        "2024-09-30"
      ]
    },
    "eps_growth_1y": {
      "value": 0.22697368421052633,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2024-09-30"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.01812535743479393,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "(revenue_latest / revenue_3y_ago)^(1/3) - 1",
      "inputs": [
        "revenue",
        "2022-09-30"
      ]
    },
    "eps_growth_3y": {
      "value": 0.06880679389561806,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_3y_ago)^(1/3) - 1",
      "inputs": [
        "eps",
        "2022-09-30"
      ]
    },
    "revenue_growth_5y": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Profitable annual periods / observed annual periods",
      "inputs": [
        "net_income_history"
      ]
    },
    "dividend_fcf_coverage": {
      "value": 6.404707865897153,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "FCF / absolute cash dividends",
      "inputs": [
        "fcf",
        "dividends"
      ]
    },
    "earnings_volatility": {
      "value": 0.0686518404091043,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 337.9580017089844,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 327.6979998779297,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 318.49961151123046,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 293.2346164703369,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 338.2072837217937,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 330.26867427900453,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 60.65152752431379,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 3.858051982793768,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 3.9281036807716556,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.0700516979778878,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 329.04352977331,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 346.8724736446588,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 6.472435980659936,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.9686780651160917,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 348.1499938964844,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.07034335437614003,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.022205848657842253,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538940+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538955+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538961+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538965+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538970+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538974+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538978+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538982+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538986+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538993+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.538998+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539002+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539006+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539010+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539014+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539017+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539021+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539025+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539029+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.025349577004283315,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:23.539050+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.019673713156074284,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:23.539082+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 5.733211470344684,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-22T07:59:23.539099+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -5.4625715184307015,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.539235+00:00",
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
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.539254+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.539262+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.539269+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.539275+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
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
      "retrieved_at": "2026-10-22T07:59:22.329712+00:00",
      "currency": "USD",
      "revenue": 394328000000.0,
      "net_income": 99803000000.0,
      "eps": 6.11,
      "ebit": 119437000000.0,
      "interest": 2931000000.0,
      "equity": 50672000000.0,
      "debt": 132480000000.0,
      "cash": 23646000000.0,
      "assets": 352755000000.0,
      "current_liabilities": 153982000000.0,
      "current_assets": 135405000000.0,
      "ocf": 122151000000.0,
      "capex": -10708000000.0,
      "fcf": 111443000000.0,
      "shares": 15943425000.0,
      "dividends": -14841000000.0,
      "operating_income": 119437000000.0,
      "inventory": 4946000000.0,
      "receivables": 60932000000.0
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 343.99,
    "INR": 32612.832869796755
  },
  "changes": {
    "price": {
      "previous": 339.5,
      "current": 343.99,
      "delta": 4.490000000000009
    },
    "new_news": []
  }
}
```

## MSFT — HOLD / REVIEW
Price: 532.95 USD | Score: 67.86 / 100
```json
{
  "ticker": "MSFT",
  "exchange": "NASDAQ",
  "name": "Microsoft Corporation",
  "price": 532.95,
  "score": 67.86,
  "fair_value": 99.97805431900618,
  "currency": "USD",
  "price_timestamp": "2026-10-21T20:00:01+00:00",
  "scores": {
    "total": 67.86,
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
        "score": 4.43,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.03368045873593129,
            "quality": 0.4210057341991411,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.01692683213284749,
            "quality": 0.2115854016605936,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -4.3306698518005105,
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
        "score": 23.08,
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
            "value": 0.3363891148736744,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.39932207377189277,
            "quality": 1,
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
        "value": 0.03368045873593129,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-22T07:59:24.408191+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.01692683213284749,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-22T07:59:24.408212+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 1.299037855568859,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-22T07:59:24.408229+00:00",
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
    "margin_of_safety": -4.3306698518005105,
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
      530.0406324594491
    ],
    "invalidation": 513.2087131084456,
    "risk_reward": 0.13879482908859375,
    "support_zone": [
      521.6246727839473,
      527.2353125676152
    ],
    "resistance_zone": [
      532.8846825495723,
      538.4953223332402
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [],
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
    "expected_session": "2026-10-21",
    "last_session": "2026-10-21",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 532.95,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 29.690807,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 22.48847,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 8.947369,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 20.642,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.30233483352811,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 3957444575232.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 7428434704.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.1983,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 17.95,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 4009414361088.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-21T20:00:01+00:00",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 56826000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 525.1275024414062,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 507.19185546875,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 458.0434509277344,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 434.919190826416,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 525.1941652327714,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 503.37144070656416,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 58.95882909735171,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 9.613376846048823,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 10.545299275714218,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.931922429665395,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 501.04134176107107,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 549.2136631217414,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 11.221279567335646,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.6479767583832887,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 551.1500244140625,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.39932207377189277,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.3363891148736744,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408089+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408101+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408106+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408111+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408115+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408120+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408124+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408128+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408132+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408136+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408140+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408144+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408148+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408152+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408156+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408160+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408164+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408168+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408172+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.03368045873593129,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:24.408191+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.01692683213284749,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:24.408212+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 1.299037855568859,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-22T07:59:24.408229+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -4.3306698518005105,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.408351+00:00",
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
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:24.408370+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:24.408377+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:24.408385+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-21",
      "retrieved_at": "2026-10-22T07:59:24.408391+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
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
      "retrieved_at": "2026-10-22T07:59:23.643738+00:00",
      "currency": "USD"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 532.95,
    "INR": 50527.658588790895
  },
  "changes": {
    "price": {
      "previous": 531.87,
      "current": 532.95,
      "delta": 1.080000000000041
    },
    "score": {
      "previous": 67.87,
      "current": 67.86,
      "delta": -0.010000000000005116
    },
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
Price: 2494.0 INR | Score: N/A / 100
```json
{
  "ticker": "TCS.NS",
  "exchange": "NSE",
  "name": "Tata Consultancy Services Limited",
  "price": 2494.0,
  "score": null,
  "fair_value": 1527.17671499812,
  "currency": "INR",
  "price_timestamp": "2026-10-22T07:59:22+00:00",
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
            "value": 0.05720128744081669,
            "quality": 0.7150160930102086,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.0531367488929124,
            "quality": 0.664209361161405,
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
        "value": 0.05720128744081669,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-22T07:59:26.340249+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.0531367488929124,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-22T07:59:26.340278+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 3.0700498432017227,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-22T07:59:26.340295+00:00",
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
    "support": 2355.975455996662,
    "resistance": null,
    "entry_range": [
      2355.975455996662,
      2392.400727188883
    ],
    "invalidation": 2283.124913612219,
    "risk_reward": null,
    "support_zone": [
      2337.762820400551,
      2374.1880915927727
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
    "errors": [],
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
    "last_session": "2026-10-22",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 2494.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 17.482124,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 15.478158,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 7.5836816,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 12.037,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.45887728459530025,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 9023510282240.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 3618087518.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.4557,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 136.01,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 8769323401216.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:22+00:00",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 112830000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 2192.8295166015623,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 2235.9403271484375,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 2216.9096105957033,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 2411.825344848633,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 2273.6924915659533,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 2237.9959785757246,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 71.97397957249706,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 76.9955558778247,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 24.896437386415485,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 52.099118491409214,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 1852.6322948390211,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 2533.0267383641035,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 72.85054238444268,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.5391990332485102,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.13537939881516436,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.20442642411330647,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340143+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340156+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340162+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340167+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340171+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340175+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340179+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340183+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340188+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340192+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340196+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340201+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340204+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340209+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340213+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340216+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340221+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340225+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.340229+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.05720128744081669,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.340249+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.0531367488929124,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.340278+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 3.0700498432017227,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.340295+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.340410+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.340430+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.340438+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.340445+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.340451+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
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
      "retrieved_at": "2026-10-22T07:59:24.519306+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 26.30593494975178,
    "INR": 2494.0
  },
  "changes": {
    "price": {
      "previous": 2517.2,
      "current": 2494.0,
      "delta": -23.199999999999818
    },
    "new_news": []
  }
}
```

## HDFCBANK.NS — INSUFFICIENT DATA
Price: 690.05 INR | Score: N/A / 100
```json
{
  "ticker": "HDFCBANK.NS",
  "exchange": "NSE",
  "name": "HDFC Bank Limited",
  "price": 690.05,
  "score": null,
  "fair_value": null,
  "currency": "INR",
  "price_timestamp": "2026-10-22T07:59:25+00:00",
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
        "value": 0.06629954399173643,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-22T07:59:27.351553+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.10017144439104243,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-22T07:59:27.351573+00:00",
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
        "retrieved_at": "2026-10-22T07:59:27.351588+00:00",
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
    "trend": "down",
    "weekly_trend": "down",
    "support": 681.9000244140625,
    "resistance": 716.5,
    "entry_range": [
      681.9000244140625,
      689.6134946513689
    ],
    "invalidation": 666.4730839394497,
    "risk_reward": 1.1084446961009609,
    "support_zone": [
      678.0432892954093,
      685.7567595327157
    ],
    "resistance_zone": [
      712.6432648813468,
      720.3567351186532
    ],
    "method": "Confirmed 5-bar pivots in last 63 sessions; zones ±0.25 ATR; invalidation support - ATR. Swing scenarios, not price forecasts."
  },
  "news": {
    "items": [],
    "overlay": "No material catalyst",
    "critical": false,
    "coverage": "headline/snippet only; material catalysts not verified",
    "note": "No material catalyst means none confirmed in available feed, not absence of risk. News never adds score points.",
    "errors": [],
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
    "last_session": "2026-10-22",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 690.05,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 15.08306,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 11.017347,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 1.7476743,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.0862935303390961,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "operating_income / revenue",
      "inputs": [
        "operating_income",
        "revenue"
      ]
    },
    "net_margin": {
      "value": 0.36599947301398505,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 10639522136064.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 15393260762.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.0018000001,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.24040002,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 45.75,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 14435692314624.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-22T07:59:25+00:00",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 6643640400000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "equity"
      ]
    },
    "revenue_growth_1y": {
      "value": 0.04733207584666732,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "(eps_latest / eps_1y_ago)^(1/1) - 1",
      "inputs": [
        "eps",
        "2025-03-31"
      ]
    },
    "revenue_growth_3y": {
      "value": 0.16901404653643337,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 714.3175018310546,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 716.7719995117187,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 743.3741339111328,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 790.4649630737305,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 712.4717984771523,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 721.9241026478874,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 40.076273828829656,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": -3.7613627382276036,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": -2.880754797227379,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.8806079410002248,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 688.8457382806251,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 739.7892653814841,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 15.426940474612872,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.432510987380018,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 1003.8961237048558,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 681.9000244140625,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": -0.08358230122345844,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": -0.027851224812241893,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351433+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351444+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351449+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351453+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351457+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351462+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351466+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351469+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351473+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351477+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351481+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351507+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351512+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351516+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351520+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351524+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351528+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351532+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-22T07:59:27.351535+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.06629954399173643,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:27.351553+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.10017144439104243,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-22T07:59:27.351573+00:00",
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
      "retrieved_at": "2026-10-22T07:59:27.351588+00:00",
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
      "retrieved_at": "2026-10-22T07:59:27.351623+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:27.351639+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:27.351646+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:27.351652+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-22T07:59:27.351658+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "currency": "INR",
      "revenue": 1925667800000.0,
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "currency": "INR",
      "revenue": 1838641100000.0,
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "currency": "INR",
      "revenue": 1604968500000.0,
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
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
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
    },
    {
      "period": "2022-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-22T07:59:26.445937+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 7.278432402596717,
    "INR": 690.05
  },
  "changes": {
    "price": {
      "previous": 700.35,
      "current": 690.05,
      "delta": -10.300000000000068
    },
    "new_news": []
  }
}
```