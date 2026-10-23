# Daily equity research
2026-10-23T13:27:45.441376+05:30
Research and decision support; no order execution.

## AAPL — INSUFFICIENT DATA
Price: 348.22 USD | Score: N/A / 100
```json
{
  "ticker": "AAPL",
  "exchange": "NASDAQ",
  "name": "Apple Inc.",
  "price": 348.22,
  "score": null,
  "fair_value": 53.22803763470469,
  "currency": "USD",
  "price_timestamp": "2026-10-22T20:00:01+00:00",
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
        "score": 4.06,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.0250416398648082,
            "quality": 0.31302049831010254,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.019434727031796394,
            "quality": 0.24293408789745494,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -5.5420409144101255,
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
        "score": 21.14,
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
            "value": 0.012205814640661172,
            "quality": 0.5610290732033059,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.046544729540394236,
            "quality": 0.6551490984679808,
            "weight": 2
          },
          "macd_positive": {
            "value": 1.0,
            "quality": 1,
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
        "value": 0.0250416398648082,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-23T07:57:47.850162+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.019434727031796394,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-23T07:57:47.850190+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 5.803712793329723,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-23T07:57:47.850206+00:00",
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
    "margin_of_safety": -5.5420409144101255,
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
    "support": 338.70001220703125,
    "resistance": null,
    "entry_range": [
      338.70001220703125,
      341.92221414707086
    ],
    "invalidation": 332.25560832695203,
    "risk_reward": null,
    "support_zone": [
      337.0889112370115,
      340.311113177051
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
    "expected_session": "2026-10-22",
    "last_session": "2026-10-22",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 348.22,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 39.933487,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 36.383965,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 47.3125,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 30.388,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 1.5191298333175105,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 5081985449984.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 14773260000.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.1204,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 7.46,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 5103930572800.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 98657000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 338.5730010986328,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 328.6173999023438,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 318.9213510131836,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 293.6674782562256,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 339.1608758645471,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 330.972647877738,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 64.76079235106062,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 4.196411236424183,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 3.98176519189408,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 0.21464604453010283,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 328.66411819270974,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 348.48188400455587,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 6.444403880079199,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.2652000522127311,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 348.3599853515625,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.046544729540394236,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.012205814640661172,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850029+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850041+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850047+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850052+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850056+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850060+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850064+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850068+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850071+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850075+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850088+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850091+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850095+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850121+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850126+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850129+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850133+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850137+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850141+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.0250416398648082,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:47.850162+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.019434727031796394,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:47.850190+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 5.803712793329723,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-23T07:57:47.850206+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -5.5420409144101255,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:47.850338+00:00",
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
      "retrieved_at": "2026-10-23T07:57:47.850357+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:47.850365+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:47.850372+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:47.850377+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
      "retrieved_at": "2026-10-23T07:57:46.236807+00:00",
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
    "USD": 348.22,
    "INR": 33057.396106414795
  },
  "changes": {
    "price": {
      "previous": 343.99,
      "current": 348.22,
      "delta": 4.230000000000018
    },
    "new_news": []
  }
}
```

## MSFT — HOLD / REVIEW
Price: 521.08 USD | Score: 67.9 / 100
```json
{
  "ticker": "MSFT",
  "exchange": "NASDAQ",
  "name": "Microsoft Corporation",
  "price": 521.08,
  "score": 67.9,
  "fair_value": 99.97805431900618,
  "currency": "USD",
  "price_timestamp": "2026-10-22T20:00:01+00:00",
  "scores": {
    "total": 67.9,
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
        "score": 4.47,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.033680046963457486,
            "quality": 0.4210005870432186,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.0173124186780416,
            "quality": 0.21640523347552001,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -4.21194379655917,
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
            "value": 0.3228483534989739,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.3677257651666588,
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
        "value": 0.033680046963457486,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-23T07:57:49.076310+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.0173124186780416,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-23T07:57:49.076331+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 1.2990537376141527,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-23T07:57:49.076347+00:00",
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
    "margin_of_safety": -4.21194379655917,
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
    "support": 518.7899780273438,
    "resistance": 535.6900024414062,
    "entry_range": [
      518.7899780273438,
      524.4748573904985
    ],
    "invalidation": 507.42021930103414,
    "risk_reward": 1.0695608805813583,
    "support_zone": [
      515.9475383457664,
      521.6324177089211
    ],
    "resistance_zone": [
      532.8475627598289,
      538.5324421229836
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
    "expected_session": "2026-10-22",
    "last_session": "2026-10-22",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 521.08,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 29.69117,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 21.982824,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 8.748091,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 20.188,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.30233483352811,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 3869303373824.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 7428434704.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.1983,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 17.95,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 3921273159680.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-22T20:00:01+00:00",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 56826000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 526.2850036621094,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 507.7833612060547,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 458.65770416259767,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 435.1471238708496,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 524.8023416001116,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 504.0658946771417,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 50.521666852746286,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 8.1457189248556,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 10.065383205542354,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -1.919664280686753,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 505.5456830353434,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 547.0243242888753,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 11.36975872630964,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.9958997498512367,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.3677257651666588,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.3228483534989739,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076208+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076221+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076226+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076231+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076235+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076239+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076243+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076248+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076252+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076256+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076260+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076264+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076268+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076272+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076276+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076280+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076284+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076288+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076292+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.033680046963457486,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:49.076310+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.0173124186780416,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:49.076331+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 1.2990537376141527,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-23T07:57:49.076347+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -4.21194379655917,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.076467+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.076487+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:49.076494+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:49.076501+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-22",
      "retrieved_at": "2026-10-23T07:57:49.076508+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
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
      "retrieved_at": "2026-10-23T07:57:48.081942+00:00",
      "currency": "USD"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 521.08,
    "INR": 49467.42853118897
  },
  "changes": {
    "price": {
      "previous": 532.95,
      "current": 521.08,
      "delta": -11.870000000000005
    },
    "score": {
      "previous": 67.86,
      "current": 67.9,
      "delta": 0.04000000000000625
    },
    "new_news": []
  }
}
```

## TCS.NS — INSUFFICIENT DATA
Price: 2524.0 INR | Score: N/A / 100
```json
{
  "ticker": "TCS.NS",
  "exchange": "NSE",
  "name": "Tata Consultancy Services Limited",
  "price": 2524.0,
  "score": null,
  "fair_value": 1527.17671499812,
  "currency": "INR",
  "price_timestamp": "2026-10-23T07:57:47+00:00",
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
            "value": 0.05702060171446124,
            "quality": 0.7127575214307654,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.05250517294864818,
            "quality": 0.6563146618581022,
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
        "value": 0.05702060171446124,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-23T07:57:51.570455+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.05250517294864818,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-23T07:57:51.570484+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 3.079778154885352,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-23T07:57:51.570500+00:00",
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
      2394.322157499023
    ],
    "invalidation": 2279.28205299194,
    "risk_reward": null,
    "support_zone": [
      2336.8021052454815,
      2375.148806747842
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
    "last_session": "2026-10-23",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 2524.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 17.537521,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 15.664343,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 7.674905,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 11.928,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.45887728459530025,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 9132052578304.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 3618087518.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.4557,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 136.01,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 8689363714048.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:47+00:00",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 112830000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 2194.3295166015623,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 2236.5403271484374,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 2217.2096118164063,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 2411.9753552246093,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 2276.549634441664,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 2239.172450437057,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 75.8253774542778,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 79.38871817853715,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 25.375069729421206,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 54.01364844911594,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 1848.6140331535653,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 2540.0450000495593,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 76.69340300472187,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.9650033579279408,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.14903672919385524,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.23017980605377675,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570352+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570365+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570371+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570375+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570379+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570383+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570387+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570391+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570395+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570399+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570403+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570407+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570411+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570415+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570419+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570423+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570427+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570431+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.570435+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.05702060171446124,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.570455+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.05250517294864818,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.570484+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 3.079778154885352,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.570500+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.570616+00:00",
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
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.570636+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.570643+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.570650+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.570656+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
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
      "retrieved_at": "2026-10-23T07:57:49.307574+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 26.587311268277656,
    "INR": 2524.0
  },
  "changes": {
    "price": {
      "previous": 2494.0,
      "current": 2524.0,
      "delta": 30.0
    },
    "new_news": []
  }
}
```

## HDFCBANK.NS — INSUFFICIENT DATA
Price: 692.1 INR | Score: N/A / 100
```json
{
  "ticker": "HDFCBANK.NS",
  "exchange": "NSE",
  "name": "HDFC Bank Limited",
  "price": 692.1,
  "score": null,
  "fair_value": null,
  "currency": "INR",
  "price_timestamp": "2026-10-23T07:57:50+00:00",
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
        "value": 0.06610316363791886,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-23T07:57:52.812260+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.09987474275704072,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-23T07:57:52.812285+00:00",
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
        "retrieved_at": "2026-10-23T07:57:52.812301+00:00",
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
    "support": 690.5,
    "resistance": 716.5,
    "entry_range": [
      690.5,
      697.9946526785033
    ],
    "invalidation": 675.5106946429934,
    "risk_reward": 1.4933702507623257,
    "support_zone": [
      686.7526736607483,
      694.2473263392517
    ],
    "resistance_zone": [
      712.7526736607483,
      720.2473263392517
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
    "last_session": "2026-10-23",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 692.1,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 15.127869,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 11.050077,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 1.7528664,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.0862935303390961,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 10671129362432.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 15393260762.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.24040002,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 45.75,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 14236860284928.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-23T07:57:50+00:00",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 6643640400000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 712.2450012207031,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 716.1079992675782,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 743.0259735107422,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 789.0685986328125,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 710.8490865699428,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 720.8937068182538,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 40.56904519915363,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": -4.706594189880661,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": -3.1967833862281143,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -1.509810803652547,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 687.9070783201141,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 736.5829241212921,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 14.989305357006597,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.4126437880143097,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": -0.07400466750480927,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": -0.013844874517578987,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812161+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812174+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812180+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812184+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812188+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812192+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812196+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812200+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812203+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812207+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812211+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812215+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812219+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812222+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812226+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812230+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812234+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812238+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-23T07:57:52.812242+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.06610316363791886,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:52.812260+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.09987474275704072,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-23T07:57:52.812285+00:00",
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
      "retrieved_at": "2026-10-23T07:57:52.812301+00:00",
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
      "retrieved_at": "2026-10-23T07:57:52.812337+00:00",
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
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:52.812355+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:52.812361+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:52.812367+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-23",
      "retrieved_at": "2026-10-23T07:57:52.812373+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
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
      "retrieved_at": "2026-10-23T07:57:51.802548+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 7.290442998722253,
    "INR": 692.1
  },
  "changes": {
    "price": {
      "previous": 690.05,
      "current": 692.1,
      "delta": 2.050000000000068
    },
    "new_news": []
  }
}
```