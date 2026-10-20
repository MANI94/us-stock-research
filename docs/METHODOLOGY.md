# Deterministic methodology

All source metrics retain value, unit/currency, source, observation period, original
retrieval timestamp and freshness. Unknown observation dates are displayed and
excluded from direct score inputs. Statement metrics become stale after 550 days;
this annual-data policy is intentionally distinct from price/session freshness.
Forward PE is a provider aggregate snapshot, not a fabricated forecast or growth rate.

Fundamentals use annual statement periods: ROE = net income / closing equity,
ROA = net income / closing assets, ROCE = EBIT / (assets - current liabilities),
margins = corresponding profit / revenue, FCF conversion = FCF / net income,
interest coverage = EBIT / positive interest expense, and debt/equity uses total debt.
Closing balance-sheet denominators are explicit approximations, not average balances.
Growth uses actual annual periods within 0.25 year of 1/3/5-year targets and requires
positive endpoints for CAGR. Negative/zero-base growth is N/A. Profitable-year share
requires at least three annual observations. Annual earnings volatility is population
standard deviation / absolute mean, requiring at least three observations.

Rules live in `config/scoring.yml`: a versioned, reviewable research policy, not an
empirically validated predictor. Each metric's quality is a clamped linear function
between its `bad` and `good` thresholds. A category's eligible weights are normalized
only within that category, and a 65% minimum weighted coverage applies. Categories
always keep their maxima (30,30,25,15). One missing category makes the total N/A.
Missing eligible bank-specific metrics cannot be substituted with industrial-company
leverage metrics. A total above 85 is a screening interpretation, not a BUY instruction.

BUY additionally requires >=70 total, >=21 fundamental points, >=10.5 risk points,
adequate essentials, fresh prices, no critical override or current risk concerns,
and an undervalued supported model with margin of safety >=30/20/15% for
conservative/moderate/aggressive profiles. Numerical thresholds cannot establish
auditor clearance, competitive advantage or promoter integrity.

DCF requires four consecutive positive annual FCF observations and dated current
FCF/shares; financial companies are excluded. Each scenario projects five years,
with growth capped by the observed three-year FCF CAGR and explicit policy caps.
Terminal growth is 2%; scenario discount rates are 14%, 12%, 10%. These are disclosed
sensitivity assumptions, not sourced market forecasts, issuer WACC estimates or
promises. The equity FCF proxy may be unsuitable around large changes in borrowing,
share count or capital intensity. N/A is preferable to an unsupported price target.
Margin of safety = 1 - price/base value. Accumulation range is conservative value ×
0.75 through base value ×0.80, a policy range rather than an executable order.

Technicals use adjusted closes and adjusted highs/lows. RSI and ATR use Wilder
seeds; MACD is EMA12-EMA26 with EMA9 signal; Bollinger bands use population std20.
Volume comparison excludes the current day from its previous-20-session denominator.
Relative strength compares matched 63-session stock/benchmark return factors.
Five-bar pivots require two confirming bars on each side within a 63-session window;
last two unconfirmed bars are excluded. Zones are ±0.25 ATR, entry is support through
support+0.5 ATR, invalidation support-ATR. Risk/reward uses current price and the next
observed resistance. Missing valid support/resistance means N/A, not invented targets.
Weekly trend uses completed Friday-labelled weeks; a holiday-shortened current week
may be withheld conservatively until the following week. Swing levels are separate
from the long-term business thesis and do not guarantee future prices.

News never adds fundamental points. Primary filings rank first, then timestamp.
Headline/snippet-only sentiment remains uncertain; event classification is descriptive.
Only structured, confirmed primary event evidence permits directional risk overlays.
Confirmed bankruptcy/receivership, non-reliance on statements, adverse audit opinion,
default or suspension overrides a favorable score. Available general feeds do not
constitute exhaustive litigation, governance or corporate-action monitoring.
