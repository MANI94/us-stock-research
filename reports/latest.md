# Daily equity research
2026-11-17T16:43:38.593612+05:30
Research and decision support; no order execution.

## AAPL — INSUFFICIENT DATA
Price: 352.78 USD | Score: N/A / 100
```json
{
  "ticker": "AAPL",
  "exchange": "NASDAQ",
  "name": "Apple Inc.",
  "price": 352.78,
  "score": null,
  "fair_value": 107.89030830441632,
  "currency": "USD",
  "price_timestamp": "2026-11-16T21:00:01+00:00",
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
        "score": 4.89,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.025454956436387555,
            "quality": 0.31818695545484443,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.02653889973342468,
            "quality": 0.3317362466678085,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -2.2698025016725203,
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
        "score": 24.86,
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
            "value": 0.18100445846010138,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.13875445137838804,
            "quality": 0.9625148379279602,
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
        "value": 0.025454956436387555,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-09-30",
        "retrieved_at": "2026-11-17T11:13:40.952697+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.02653889973342468,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-09-30",
        "retrieved_at": "2026-11-17T11:13:40.952722+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 2.8945302874721324,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-09-30",
        "retrieved_at": "2026-11-17T11:13:40.952734+00:00",
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
    "margin_of_safety": -2.2698025016725203,
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
    "support": 340.7710769804186,
    "resistance": 355.1101713190276,
    "entry_range": [
      340.7710769804186,
      344.7914728178791
    ],
    "invalidation": 332.73028530549766,
    "risk_reward": 0.11621974263002607,
    "support_zone": [
      338.7608790616884,
      342.78127489914885
    ],
    "resistance_zone": [
      353.09997340029736,
      357.1203692377578
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
    "expected_session": "2026-11-16",
    "last_session": "2026-11-16",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 352.78,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 39.28508,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 33.370792,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 45.738365,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 30.116,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 1.17915480895328,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 5126663176192.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 14532259000.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.01687,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.118,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 8.98,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 5164420300800.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 80111000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 346.4197067260742,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 339.45084899902344,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 327.09973083496095,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 301.2455997467041,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 346.9498073492677,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 339.05107759379746,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 57.22840853007414,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 4.207217204561573,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 3.4734215046616956,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 0.7337956998998774,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 334.4481156721441,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 358.39129778000427,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 8.040791674920948,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.9732704645655664,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Latest volume / previous 20 sessions mean",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "high_52w": {
      "value": 360.8299865722656,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Maximum adjusted high last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "low_52w": {
      "value": 242.57490960968966,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.13875445137838804,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.18100445846010138,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952611+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952623+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952628+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952631+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952634+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952638+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952643+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952646+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952649+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952652+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952655+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952658+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952662+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952664+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952667+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952670+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952673+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952676+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952679+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.025454956436387555,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:40.952697+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.02653889973342468,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:40.952722+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 2.8945302874721324,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-09-30",
      "retrieved_at": "2026-11-17T11:13:40.952734+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -2.2698025016725203,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:40.952844+00:00",
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
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:40.952857+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:40.952864+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:40.952869+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:40.952874+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-09-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
      "retrieved_at": "2026-11-17T11:13:39.363643+00:00",
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
    "USD": 352.78,
    "INR": 32970.818477020264
  },
  "changes": {
    "price": {
      "previous": 356.27,
      "current": 352.78,
      "delta": -3.490000000000009
    },
    "new_news": []
  }
}
```

## MSFT — HOLD / REVIEW
Price: 517.99 USD | Score: 63.38 / 100
```json
{
  "ticker": "MSFT",
  "exchange": "NASDAQ",
  "name": "Microsoft Corporation",
  "price": 517.99,
  "score": 63.38,
  "fair_value": 99.97805431900618,
  "currency": "USD",
  "price_timestamp": "2026-11-16T21:00:01+00:00",
  "scores": {
    "total": 63.38,
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
        "score": 4.73,
        "maximum": 30,
        "coverage": 0.8333,
        "details": {
          "earnings_yield": {
            "value": 0.036989129264800365,
            "quality": 0.46236411581000453,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.017414172078964417,
            "quality": 0.2176771509870552,
            "weight": 3
          },
          "margin_of_safety": {
            "value": -4.181037013855232,
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
        "score": 18.3,
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
            "value": 0.11749625331504143,
            "quality": 1,
            "weight": 3
          },
          "momentum_63": {
            "value": 0.07751822928801055,
            "quality": 0.7583940976267018,
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
        "value": 0.036989129264800365,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-11-17T11:13:42.029788+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.017414172078964417,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-11-17T11:13:42.029805+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 1.182839168169745,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-06-30",
        "retrieved_at": "2026-11-17T11:13:42.029817+00:00",
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
    "margin_of_safety": -4.181037013855232,
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
    "trend": "mixed",
    "weekly_trend": "up",
    "support": 515.7000122070312,
    "resistance": 519.4000244140625,
    "entry_range": [
      515.7000122070312,
      523.1626308977837
    ],
    "invalidation": 500.77477482552626,
    "risk_reward": 0.0819062757101914,
    "support_zone": [
      511.968702861655,
      519.4313215524076
    ],
    "resistance_zone": [
      515.6687150686862,
      523.1313337594388
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
    "expected_session": "2026-11-16",
    "last_session": "2026-11-16",
    "stale": false,
    "condition": "closed",
    "calendar": "XNYS",
    "calendar_note": null
  },
  "metrics": {
    "price": {
      "value": 517.99,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 27.03497,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 21.407288,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 8.176508,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 19.039,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.30233483352811,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 3846694502400.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 7428434704.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.00116,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.19,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 17.95,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 3916116525056.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-11-16T21:00:01+00:00",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 56826000000.0,
      "unit": "USD",
      "source": "Yahoo Finance",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 528.6094970703125,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 519.3629992675782,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 481.46254180908204,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 440.94380111694335,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 527.3082788099657,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 516.0681974477501,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 46.37412270238981,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 1.009908136105878,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 3.286384494512858,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -2.2764763584069803,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 508.54015272901427,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 548.6788414116107,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 14.925237381504985,
      "unit": "USD",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 1.1508783322729206,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.07751822928801055,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.11749625331504143,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "freshness": "fresh",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029706+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029716+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029721+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029724+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029727+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029731+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029734+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029737+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029741+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029744+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029747+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029750+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029754+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029757+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029760+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029764+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029767+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029770+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029773+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.036989129264800365,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:42.029788+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.017414172078964417,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:42.029805+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 1.182839168169745,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-06-30",
      "retrieved_at": "2026-11-17T11:13:42.029817+00:00",
      "freshness": "derived",
      "formula": "PE / historical EPS CAGR in percentage points; historical proxy, not forecast",
      "inputs": [
        "pe",
        "eps_growth_3y"
      ]
    },
    "margin_of_safety": {
      "value": -4.181037013855232,
      "unit": "ratio",
      "source": "DCF scenarios",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.029915+00:00",
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
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:42.029929+00:00",
      "freshness": "derived",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:42.029935+00:00",
      "freshness": "derived",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:42.029940+00:00",
      "freshness": "derived",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-16",
      "retrieved_at": "2026-11-17T11:13:42.029945+00:00",
      "freshness": "derived",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-06-30",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
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
      "retrieved_at": "2026-11-17T11:13:41.177202+00:00",
      "currency": "USD"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 517.99,
    "INR": 48411.34492576599
  },
  "changes": {
    "price": {
      "previous": 523.88,
      "current": 517.99,
      "delta": -5.889999999999986
    },
    "score": {
      "previous": 67.37,
      "current": 63.38,
      "delta": -3.990000000000002
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
Price: 2406.6 INR | Score: N/A / 100
```json
{
  "ticker": "TCS.NS",
  "exchange": "NSE",
  "name": "Tata Consultancy Services Limited",
  "price": 2406.6,
  "score": null,
  "fair_value": 1527.17671499812,
  "currency": "INR",
  "price_timestamp": "2026-11-17T09:58:11+00:00",
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
            "value": 0.059278649964314256,
            "quality": 0.7409831245539282,
            "weight": 2
          },
          "fcf_yield": {
            "value": 0.055066503992117544,
            "quality": 0.6883312999014692,
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
        "value": 0.059278649964314256,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-17T11:13:43.883191+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.055066503992117544,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-17T11:13:43.883222+00:00",
        "freshness": "derived",
        "formula": "annual FCF / market cap",
        "inputs": [
          "fcf",
          "market_cap"
        ]
      },
      "peg": {
        "value": 2.962462938078611,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-17T11:13:43.883234+00:00",
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
    "support": 2246.35838320449,
    "resistance": 2549.89990234375,
    "entry_range": [
      2246.35838320449,
      2279.5429764928344
    ],
    "invalidation": 2179.989196627801,
    "risk_reward": 0.6323605971166849,
    "support_zone": [
      2229.766086560318,
      2262.9506798486623
    ],
    "resistance_zone": [
      2533.307605699578,
      2566.492198987922
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
    "last_session": "2026-11-17",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 2406.6,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 16.86948,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 14.972255,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 7.317919,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": 11.422,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.45887728459530025,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 8707289645056.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 3618087518.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.4557,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 136.01,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 8320680722432.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 112830000000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 2476.964990234375,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 2289.8212548828124,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 2268.6679870605467,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 2359.4964599609375,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 2424.0507732432225,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 2351.1437784608984,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 50.59713431241914,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 35.39298702437145,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 56.35830199412189,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": -20.965314969750438,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 2398.025600389042,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 2555.9043800797076,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 66.36918657668892,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.6682163577448417,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.024732632133959376,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": -0.01649499632122986,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883103+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883114+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883119+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883123+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883126+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883130+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883133+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883136+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883139+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883142+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883146+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883150+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883153+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883156+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883159+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883162+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883166+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883169+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:43.883172+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.059278649964314256,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:43.883191+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.055066503992117544,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:43.883222+00:00",
      "freshness": "derived",
      "formula": "annual FCF / market cap",
      "inputs": [
        "fcf",
        "market_cap"
      ]
    },
    "peg": {
      "value": 2.962462938078611,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:43.883234+00:00",
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
      "retrieved_at": "2026-11-17T11:13:43.883340+00:00",
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
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:43.883355+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:43.883361+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 0.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:43.883367+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:43.883372+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
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
      "retrieved_at": "2026-11-17T11:13:42.250116+00:00",
      "currency": "INR"
    }
  ],
  "provider_conflicts": {},
  "warnings": [
    "Yahoo is an unofficial personal-use fallback; governance disclosures are incomplete"
  ],
  "news_ids": [],
  "converted_prices": {
    "USD": 25.750053751068673,
    "INR": 2406.6
  },
  "changes": {
    "price": {
      "previous": 2405.0,
      "current": 2406.6,
      "delta": 1.599999999999909
    },
    "new_news": []
  }
}
```

## HDFCBANK.NS — INSUFFICIENT DATA
Price: 814.95 INR | Score: N/A / 100
```json
{
  "ticker": "HDFCBANK.NS",
  "exchange": "NSE",
  "name": "HDFC Bank Limited",
  "price": 814.95,
  "score": null,
  "fair_value": null,
  "currency": "INR",
  "price_timestamp": "2026-11-17T09:58:11+00:00",
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
        "value": 0.05613841577615234,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-17T11:13:45.190979+00:00",
        "freshness": "derived",
        "formula": "1 / trailing PE",
        "inputs": [
          "pe"
        ]
      },
      "fcf_yield": {
        "value": 0.08474314920975304,
        "unit": "ratio",
        "source": "calculated",
        "period": "2026-03-31",
        "retrieved_at": "2026-11-17T11:13:45.190996+00:00",
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
        "retrieved_at": "2026-11-17T11:13:45.191008+00:00",
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
    "support": 798.0,
    "resistance": 817.8499755859375,
    "entry_range": [
      798.0,
      806.3102321516371
    ],
    "invalidation": 781.3795356967257,
    "risk_reward": 0.08638433767885344,
    "support_zone": [
      793.8448839241814,
      802.1551160758186
    ],
    "resistance_zone": [
      813.6948595101189,
      822.0050916617561
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
    "last_session": "2026-11-17",
    "stale": true,
    "condition": "holiday/weekend",
    "calendar": "XBOM",
    "calendar_note": "XBOM proxy for NSE; verify exceptional NSE-only sessions"
  },
  "metrics": {
    "price": {
      "value": 814.95,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": null,
      "inputs": []
    },
    "pe": {
      "value": 17.813114,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "forward_pe": {
      "value": 13.018372,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "pb": {
      "value": 2.0640059,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "ev_ebitda": {
      "value": null,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "roe": {
      "value": 0.0862935303390961,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "fresh",
      "formula": "net_income / revenue",
      "inputs": [
        "net_income",
        "revenue"
      ]
    },
    "market_cap": {
      "value": 12576548192256.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "shares": {
      "value": 15393260762.0,
      "unit": "shares",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "shares"
      ]
    },
    "insider_ownership": {
      "value": 0.0030899998,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "payout": {
      "value": 0.24040002,
      "unit": "ratio",
      "source": "Yahoo Finance",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "eps": {
      "value": 45.75,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "fresh",
      "formula": "Latest annual statement value",
      "inputs": [
        "fcf"
      ]
    },
    "enterprise_value": {
      "value": 16124216344576.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-11-17T09:58:11+00:00",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "snapshot",
      "formula": null,
      "inputs": []
    },
    "debt": {
      "value": 6643640400000.0,
      "unit": "INR",
      "source": "Yahoo Finance",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "fresh",
      "formula": "std annual net income / abs mean",
      "inputs": [
        "net_income_history"
      ]
    },
    "sma20": {
      "value": 739.9199981689453,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "mean last 20 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma50": {
      "value": 725.142998046875,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "mean last 50 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma100": {
      "value": 742.2375,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "mean last 100 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "sma200": {
      "value": 774.6577697753906,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "mean last 200 adjusted closes",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema20": {
      "value": 759.8860755423541,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "EMA span 20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "ema50": {
      "value": 738.9279545185968,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "EMA span 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "rsi14": {
      "value": 74.78839586640287,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "Wilder RSI 14; flat market = 50",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd": {
      "value": 27.863831607826228,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "EMA12 - EMA26",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_signal": {
      "value": 17.248665482105842,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "EMA9 of MACD",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "macd_histogram": {
      "value": 10.615166125720386,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "MACD - signal",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_lower": {
      "value": 635.9158523733399,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "SMA20 - 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "bollinger_upper": {
      "value": 843.9241439645507,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "SMA20 + 2 population std20",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "atr14": {
      "value": 16.620464303274304,
      "unit": "INR",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "Wilder mean true range14",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "volume_ratio": {
      "value": 0.897880423262696,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "Minimum adjusted low last 252 sessions",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "momentum_63": {
      "value": 0.1209766330220512,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "close / close63 sessions ago - 1",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "relative_strength_63": {
      "value": 0.07587686096059065,
      "unit": "ratio",
      "source": "Yahoo Finance auto_adjust=True",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
      "freshness": "stale",
      "formula": "stock 63-session return factor / benchmark factor - 1; aligned dates",
      "inputs": [
        "adjusted OHLCV"
      ]
    },
    "competitive_advantage": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190901+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "audit_clear": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190910+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "credit_cost": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190914+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "concentration_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190918+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "regulatory_exposure": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190921+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_median": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190925+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "promoter_ownership": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190928+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190931+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capital_adequacy": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190934+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "funding_stability": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190937+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "dilution_risk": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190940+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "recurring_revenue_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190944+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_min": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190947+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "historical_pe_max": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190950+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "normalized_roe": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190953+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "pledge_ratio": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190956+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "gnpa": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190959+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "nim": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190963+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "capacity_utilization": {
      "value": null,
      "unit": "ratio",
      "source": "Not available from configured providers",
      "period": null,
      "retrieved_at": "2026-11-17T11:13:45.190966+00:00",
      "freshness": "unknown",
      "formula": null,
      "inputs": []
    },
    "earnings_yield": {
      "value": 0.05613841577615234,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:45.190979+00:00",
      "freshness": "derived",
      "formula": "1 / trailing PE",
      "inputs": [
        "pe"
      ]
    },
    "fcf_yield": {
      "value": 0.08474314920975304,
      "unit": "ratio",
      "source": "calculated",
      "period": "2026-03-31",
      "retrieved_at": "2026-11-17T11:13:45.190996+00:00",
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
      "retrieved_at": "2026-11-17T11:13:45.191008+00:00",
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
      "retrieved_at": "2026-11-17T11:13:45.191052+00:00",
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
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:45.191065+00:00",
      "freshness": "stale",
      "formula": "price > SMA50",
      "inputs": []
    },
    "above_sma200": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:45.191071+00:00",
      "freshness": "stale",
      "formula": "price > SMA200",
      "inputs": []
    },
    "macd_positive": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:45.191076+00:00",
      "freshness": "stale",
      "formula": "MACD histogram > 0",
      "inputs": []
    },
    "weekly_up": {
      "value": 1.0,
      "unit": "ratio",
      "source": "adjusted OHLCV derived",
      "period": "2026-11-17",
      "retrieved_at": "2026-11-17T11:13:45.191081+00:00",
      "freshness": "stale",
      "formula": "last completed weekly close > weekly SMA20",
      "inputs": []
    }
  },
  "statements": [
    {
      "period": "2026-03-31",
      "source": "Yahoo Finance",
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
      "retrieved_at": "2026-11-17T11:13:44.107373+00:00",
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
    "USD": 8.719773250408634,
    "INR": 814.95
  },
  "changes": {
    "price": {
      "previous": 816.5,
      "current": 814.95,
      "delta": -1.5499999999999545
    },
    "new_news": []
  }
}
```