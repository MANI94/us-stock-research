# Daily equity research
2026-10-29T14:27:00.723592+05:30
Research and decision support; no order execution.

## AAPL — INSUFFICIENT DATA
Price: 343.83 USD | Score: N/A / 100
```json
{
  "ticker": "AAPL",
  "exchange": "NASDAQ",
  "name": "Apple Inc.",
  "price": 343.83,
  "score": null,
  "fair_value": 53.22803763470469,
  "currency": "USD",
  "price_timestamp": "2026-10-28T20:00:01+00:00",
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
        "score": 4.12,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.025361372934880465,
            "quality": 0.3170171616860058,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.019682868675696612,
            "quality": 0.24603585844620765,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -5.459565583831006,
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
        "score": 18.43,
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
            "value": -0.00874856307427152,
            "quality": 0.4562571846286424,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.03208030032559206,
            "quality": 0.6069343344186402,
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
        "value": 0.025361372934880465,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-29T08:57:02.797869+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.019682868675696612,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-29T08:57:02.797899+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 5.73054487320199,
        "unit": "ratio",
        "source": "calculated",
        "period": "2025-09-30",
        "retrieved_at": "2026-10-29T08:57:02.797916+00:00",
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
    "margin_of_safety": -5.459565583831006,
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
    "support": 341.0299987792969,
    "resistance": 345.3399963378906,
    "entry_range": [
      341.0299987792969,
      344.11238192500497
    ],
    "invalidation": 334.8652324878807,
    "risk_reward": 0.16843850387989762,
    "support_zone": [
      339.4888072064428,
      342.57119035215095
    ],
    "resistance_zone": [
      343.79880476503655,
      346.8811879107447
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
    "expected_session": "2026-10-28",
    "last_session": "2026-10-28",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 343.83,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 39.430042,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 35.956264,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 46.71603,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 30.007,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 1.5191298333175105,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 5017916932096.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 14773260000.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.1204,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 7.46,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 5039862054912.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 98657000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 340.6070022583008,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 331.73260009765625,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 320.317470703125,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 295.39947814941405,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 341.26433524788484,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 333.135668169743,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 56.11523922980902,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 3.9198330549183424,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 4.067009213762157,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -0.14717615884381452,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 330.6107854838684,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 350.60321903273314,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 6.164766291416188,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.9107842979218048,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 351.7300109863281,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.03208030032559206,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": -0.00874856307427152,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797757+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797770+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797776+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797781+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797785+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797789+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797793+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797797+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797801+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797805+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797815+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797820+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797824+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797828+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797832+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797836+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797840+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797844+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.797848+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.025361372934880465,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:02.797869+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.019682868675696612,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:02.797899+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 5.73054487320199,
      "unit": "ratio",
      "source": "calculated",
      "period": "2025-09-30",
      "retrieved_at": "2026-10-29T08:57:02.797916+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -5.459565583831006,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:02.798049+00:00",
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
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:02.798069+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:02.798078+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:02.798085+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:02.798091+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2025-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
      "retrieved_at": "2026-10-29T08:57:01.334334+00:00",
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
    "USD": 343.83,
    "INR": 32751.5257056427
  },
  "changes": {
    "price": {
      "previous": 347.1,
      "current": 343.83,
      "delta": -3.2700000000000387
    },
    "new_news": []
  }
}
```

## MSFT — HOLD / REVIEW
Price: 531.01 USD | Score: 67.88 / 100
```json
{
  "ticker": "MSFT",
  "exchange": "NASDAQ",
  "name": "Microsoft Corporation",
  "price": 531.01,
  "score": 67.88,
  "fair_value": 99.99736748912113,
  "currency": "USD",
  "price_timestamp": "2026-10-28T20:00:01+00:00",
  "scores": {
    "total": 67.88,
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
        "score": 4.45,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.03380350630249473,
            "quality": 0.42254382878118407,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.016988671923927133,
            "quality": 0.21235839904908915,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -4.310239792640235,
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
            "value": 0.1327054813473132,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.17936072505988432,
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
        "value": 0.03380350630249473,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-29T08:57:03.850663+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.016988671923927133,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-29T08:57:03.850715+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 1.2943092500339435,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-10-29T08:57:03.850733+00:00",
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
        "value": 70.78158865981216,
        "growth": 0.0,
        "discount_rate": 0.14
      },
      "base": {
        "value": 99.99736748912113,
        "growth": 0.040443958087982956,
        "discount_rate": 0.12
      },
      "optimistic": {
        "value": 125.33954601155143,
        "growth": 0.040443958087982956,
        "discount_rate": 0.1
      }
    },
    "margin_of_safety": -4.310239792640235,
    "accumulation_range": [
      53.08619149485912,
      79.9978939912969
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
      529.8281208862938
    ],
    "invalidation": 513.6337362547561,
    "risk_reward": 0.2693323555740471,
    "support_zone": [
      521.730928570525,
      527.1290567810375
    ],
    "resistance_zone": [
      532.99093833615,
      538.3890665466625
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
    "expected_session": "2026-10-28",
    "last_session": "2026-10-28",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 531.01,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 29.58273,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 22.415209,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 8.9148,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 20.568,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.30233483352811,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 3943039238144.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 7427000000.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.1983,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 17.95,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 3995009024000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-10-28T20:00:01+00:00",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 56826000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 529.8950042724609,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 511.16060119628906,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 462.7506982421875,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 436.2146318054199,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 526.5433175000647,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 507.89377956918935,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 56.0817485247925,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 6.283674309323942,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 8.071447303976571,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -1.787772994652629,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 515.0093020151088,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 544.7807065298131,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 10.796256421025177,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.3788798898529961,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.17936072505988432,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.1327054813473132,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850559+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850572+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850578+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850582+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850586+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850591+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850595+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850599+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850603+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850607+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850611+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850615+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850620+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850624+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850628+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850632+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850636+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850640+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850644+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.03380350630249473,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.850663+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.016988671923927133,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.850715+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 1.2943092500339435,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-10-29T08:57:03.850733+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -4.310239792640235,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:03.850853+00:00",
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
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.850873+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.850880+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.850888+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-28",
      "retrieved_at": "2026-10-29T08:57:03.850895+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "shares": 7427000000.0,
      "dividends": -26445000000.0,
      "operating_income": 155237000000.0,
      "inventory": 1397000000.0,
      "receivables": 80876000000.0
    },
    {
      "period": "2025-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
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
      "retrieved_at": "2026-10-29T08:57:03.000466+00:00",
      "currency": "USD"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 531.01,
    "INR": 50581.35609153748
  },
  "changes": {
    "price": {
      "previous": 531.33,
      "current": 531.01,
      "delta": -0.32000000000005
    },
    "score": {
      "previous": 67.87,
      "current": 67.88,
      "delta": 0.009999999999990905
    },
    "new_news": []
  }
}
```

## TCS.NS — INSUFFICIENT DATA
Price: 2475.0 INR | Score: N/A / 100
```json
{
  "ticker": "TCS.NS",
  "exchange": "NSE",
  "name": "Tata Consultancy Services Limited",
  "price": 2475.0,
  "score": null,
  "fair_value": 1527.17671499812,
  "currency": "INR",
  "price_timestamp": "2026-10-29T08:57:02+00:00",
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
        "coverage": 0.1667,
        "details": {
          "earnings_yield": {
            "value": 0.057640402509847574,
            "quality": 0.7205050313730946,
            "weight": 2
          },
          "fcf_yield": {
            "value": null,
            "points": null,
            "reason": "missing, stale, or undated"
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
        "value": 0.057640402509847574,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-29T08:57:05.997419+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": null,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-29T08:57:05.997449+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 3.046661645164843,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-29T08:57:05.997465+00:00",
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
    "resistance": 2481.8066737190825,
    "entry_range": [
      2355.975455996662,
      2392.7719906476327
    ],
    "invalidation": 2282.38238669472,
    "risk_reward": 0.0353377533979438,
    "support_zone": [
      2337.5771886711764,
      2374.3737233221473
    ],
    "resistance_zone": [
      2463.408406393597,
      2500.204941044568
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
    "last_session": "2026-10-29",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 2475.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 17.348942,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 15.360242,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 7.525907,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 11.695,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.45887728459530025,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": null,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 3618087518.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.4557,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 136.01,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 8519675281408.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:02+00:00",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 112830000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 2302.9741088867186,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 2250.4969970703123,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 2228.9725732421875,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 2396.9355322265624,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 2361.8536585858196,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 2285.529234233229,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 65.64959555470247,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 91.41287036555059,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 70.75101158069899,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 20.661858784851603,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 1920.973918002811,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 2684.974299770626,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 73.5930693019419,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.46555416933974886,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.01698567516448679,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.07500672999968527,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997314+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997327+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997332+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997337+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997341+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997345+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997350+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997354+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997358+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997362+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997366+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997370+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997374+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997378+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997382+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997386+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997391+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997395+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:05.997399+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.057640402509847574,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:05.997419+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": null,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:05.997449+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 3.046661645164843,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:05.997465+00:00",
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
      "retrieved_at": "2026-10-29T08:57:05.997579+00:00",
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
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:05.997599+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:05.997607+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:05.997615+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:05.997621+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
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
      "retrieved_at": "2026-10-29T08:57:04.017867+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 25.98288878656381,
    "INR": 2475.0
  },
  "changes": {
    "price": {
      "previous": 2449.5,
      "current": 2475.0,
      "delta": 25.5
    },
    "new_news": []
  }
}
```

## HDFCBANK.NS — INSUFFICIENT DATA
Price: 686.5 INR | Score: N/A / 100
```json
{
  "ticker": "HDFCBANK.NS",
  "exchange": "NSE",
  "name": "HDFC Bank Limited",
  "price": 686.5,
  "score": null,
  "fair_value": null,
  "currency": "INR",
  "price_timestamp": "2026-10-29T08:57:05+00:00",
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
        "value": 0.06664238662380673,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-29T08:57:06.961350+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.10062980381854168,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-10-29T08:57:06.961371+00:00",
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
        "retrieved_at": "2026-10-29T08:57:06.961387+00:00",
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
      689.0310840978325
    ],
    "invalidation": 667.6379050465225,
    "risk_reward": 1.590491410100186,
    "support_zone": [
      678.3344945721775,
      685.4655542559475
    ],
    "resistance_zone": [
      712.934470158115,
      720.065529841885
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
    "last_session": "2026-10-29",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 686.5,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 15.005465,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 10.960669,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 1.7386835,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.0862935303390961,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 10591060099072.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 15393260762.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.24040002,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 45.75,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 14101994536960.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-10-29T08:57:05+00:00",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 6643640400000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 703.9774993896484,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 712.7259985351562,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 740.8920959472656,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 783.4307598876953,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 702.3852500561258,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 715.616796204666,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 40.08853319318001,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": -8.523360863603443,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": -5.867701732032121,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -2.655659131571322,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 677.2061647080435,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 730.7488340712533,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 14.262119367540013,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.6259009538247691,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": -0.082464596632429,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": -0.030117377539676804,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961251+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961263+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961268+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961272+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961277+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961281+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961285+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961289+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961292+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961296+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961300+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961304+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961308+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961312+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961316+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961320+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961324+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961328+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-10-29T08:57:06.961332+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.06664238662380673,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:06.961350+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.10062980381854168,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-10-29T08:57:06.961371+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.961387+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.961422+00:00",
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
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.961439+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.961446+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.961452+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-10-29",
      "retrieved_at": "2026-10-29T08:57:06.961459+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
      "retrieved_at": "2026-10-29T08:57:06.155473+00:00",
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
    "USD": 7.206970970495375,
    "INR": 686.5
  },
  "changes": {
    "price": {
      "previous": 684.75,
      "current": 686.5,
      "delta": 1.75
    },
    "new_news": []
  }
}
```