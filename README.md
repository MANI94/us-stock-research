# Automated US and Indian equity research

Python 3.12 application for a daily, evidence-linked investment research watchlist.
Edit **`config/stocks.yml`** to add/remove tickers. NASDAQ, NYSE, NSE (`.NS`), and
BSE (`.BO`) are accepted. There is no brokerage integration or order execution.

## Set up after reviewing and merging the pull request

1. Add repository **Actions Secrets**:
   - `GMAIL_ADDRESS`: Gmail sender address.
   - `GMAIL_APP_PASSWORD`: a Google App Password, never the account password.
   - `REPORT_TO_EMAIL`: comma-separated bare recipient addresses.
   - Optional `FMP_API_KEY`: preferred documented provider; a subscription with
     the required geography/endpoints may be necessary.
   - Optional `FINNHUB_API_KEY`: company-specific news.
   - Optional `SEC_USER_AGENT`: SEC identification, e.g. `EquityResearch contact@example.com`.
     This enables official US filing metadata. Its value is never written to reports.
   - Optional `LLM_API_KEY`: OpenAI API key for evidence-grounded news summaries.
     Also set Actions **variable** `LLM_MODEL` to a model available to your account
     that supports Responses structured outputs. No model or paid account is assumed.
2. Edit `config/stocks.yml`. Default examples: AAPL, MSFT, TCS.NS, HDFCBANK.NS.
3. Open **Actions → Daily stock research → Run workflow** on `main`. Leave tickers
   blank for the configured watchlist, or enter `IBM:NYSE,TCS.NS:NSE,500325.BO:BSE`.
   Bare US symbols default to NASDAQ; use `:NYSE` for NYSE symbols.
4. Inspect the research artifact and Gmail delivery audit. The default configuration
   enables email; the manual `send_email` checkbox permits a report-only run.
5. The workflow automatically maintains the `research-state` branch. Keep this
   branch: it stores prior reports, daily snapshots, and duplicate-delivery state.
   Repository rules must permit its writes by `GITHUB_TOKEN`. No main-branch writes occur.

Google requires eligible accounts and 2-Step Verification for App Passwords:
[Google setup instructions](https://support.google.com/accounts/answer/185833).
Never put credentials in YAML, commit them, or paste them into an issue.

## What you get

- `reports/latest.html`: standalone dashboard and matching formatted email.
- `reports/latest.md`, `.json`, `.csv`: full evidence and compact export.
- `history/YYYY-MM-DD.json`: daily snapshot (same-day reruns replace that day's
  durable snapshot; each Actions artifact remains a distinct immutable run output).
- 30/30/25/15 category scores and per-category weighted data coverage; at least
  65% coverage is required independently in **every** category. Missing/stale
  evidence never receives a zero score or an assumed favorable value.
- Sector policies for financials, technology, manufacturing, and cyclicals.
- DCF sensitivity scenarios with explicit formulas, growth caps and rates;
  no fabricated analyst estimates. An equity FCF proxy is used, so valuation is
  labelled low confidence and does not deduct debt a second time.
- Adjusted SMA/EMA, Wilder RSI/ATR, MACD, Bollinger Bands, aligned benchmark
  strength, weekly trend and confirmed five-bar support/resistance pivots.
- Company-disambiguated, deduplicated news with original links, access level,
  event category, cautious sentiment and a separate risk overlay.
- HTML email with scores, prices, fair values, news, changes, CSV attachment and
  a link to that run's full artifacts. No web hosting or public Pages deployment.

[Example dashboard](docs/example/reports/latest.html),
[example JSON](docs/example/reports/latest.json),
[methodology and limitations](docs/METHODOLOGY.md),
[provider evaluation](docs/PROVIDERS.md).
The example uses **synthetic fixtures**, prominently labelled. It is not an
investment recommendation or a claim about those companies' actual financials.

## Honest evidence limits

Yahoo is an unofficial personal-use fallback, enabled explicitly in the supplied
configuration. Set `allow_yahoo: false` to disable it; FMP adjusted history is
supported independently. FMP/SEC/Finnhub access depends on credentials, entitlements,
provider availability, exchange coverage and identification. See the provider matrix.

Specialist fields such as NIM, GNPA/NNPA, capital adequacy, promoter pledging,
auditor qualifications, recurring revenue and capacity utilization may be unavailable
from these general feeds. They appear as **N/A**; they are never inferred from news
keywords. Banks without essential regulatory metrics return **INSUFFICIENT DATA**.
Cyclicals without normalized earnings also need further review. There is no claim
that every requested disclosure can be obtained from a free or general-purpose API.
The architecture is ready for licensed disclosure adapters; they are not fabricated
or presented as integrated here. A missing audit result is not a clean audit.

Historical P/E comes from FMP annual ratios when at least three dated positive
observations exist. Same-industry peer valuation requires at least three of the
provider-selected peers and the relevant entitlements; otherwise it is N/A.
No same-day price is divided by a historical EPS to invent historical P/E.

## Local development

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --require-hashes -r requirements.lock
python -m pytest -q
# Offline, labelled synthetic example; never sends email:
python -m src.main --fixture tests/fixtures/equities.json --output example-output
# Live providers, never sends email by itself:
python -m src.main
python -m src.main --tickers AAPL:NASDAQ,TCS.NS:NSE
```

Run from the repository root. All money calculations in DCF use Decimal; prices,
ratios and indicators use finite floating-point numbers. Currency conversion uses
a dated USD/INR quote when available, and otherwise remains N/A. The configured
INR budget is a research setting, not an investment, portfolio allocation or order.

`requirements.txt` pins direct dependencies; `requirements.lock` pins and hashes
transitive dependencies for Python 3.12 on the Linux Actions runner. Recompile it
with `uv pip compile requirements.txt --python-version 3.12 --python-platform
x86_64-unknown-linux-gnu --generate-hashes -o requirements.lock` when updating.
Tests are fixture-based and use mocked SMTP/HTTP. No real email is sent by tests.

## Scheduling, holidays and durability

Cron is **02:47 UTC / 08:17 Asia/Kolkata daily**. This is after the preceding US
close, and before the Indian market opens. Markets are evaluated separately against
the latest completed session, with a 30-minute reporting buffer; closed markets and
stale bars are explicitly labelled. GitHub may delay or skip scheduled work, so
manual dispatch is supported. Report timestamps use `Asia/Kolkata` by default.
[GitHub scheduling behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

NYSE calendar is used for both US exchanges. XBOM is a disclosed proxy for NSE;
exceptional NSE-only sessions require calendar maintenance. This is not a promise
of complete exchange-specific exceptional-session coverage. Calendar dependency
updates should be reviewed as holidays are announced.

Analysis and PR tests have `contents: read`; only the delivery/state job receives
`contents: write`. Third-party Actions are pinned to verified commit SHAs. Provider
secrets exist only in analysis, Gmail secrets only in delivery. Untrusted dispatch
input is an environment variable parsed by Python, never shell-interpolated source.
No `pull_request_target`, recursive report pushes, force pushes or automatic merge.

The delivery job persists a `sending` reservation **before** SMTP. After acceptance
it persists `delivered`; pre-submission failures become `failed`; ambiguous/partial
sends become `uncertain`. `sending`, `delivered`, and `uncertain` block duplicate
submission for that reporting date. A reservation push failure prevents SMTP.
SMTP and Git are not one atomic transaction; exactly-once email cannot be guaranteed.

For `sending`/`uncertain`, check Gmail Sent and recipients before editing the ledger
on `research-state`. Mark delivered if accepted; mark failed only when non-delivery
is established. Never clear a reservation just to retry blindly. Manual overrides
use separate run keys and `manual/<run-id>/` snapshots, without replacing the normal
watchlist's comparison baseline. Regular daily runs send closed-market reports too.
Artifacts expire after 90 days; durable daily history remains on the state branch.

## Validation performed for this change

Python 3.12 deterministic tests cover US/Indian equities, banks, missing information,
holidays, split-adjusted history, retries, provider conflicts, news deduplication,
score thresholds, critical overrides, grounded-summary validation, historical changes,
HTML/JSON/CSV generation, TLS configuration and ambiguous SMTP delivery.
A live Yahoo smoke fetch for AAPL and TCS.NS retrieved price, statements and adjusted
history successfully. Paid FMP/Finnhub APIs, SEC with a real identifying user agent,
OpenAI summaries and Gmail delivery have **not** been exercised with live credentials.
The PR CI verifies the Linux workflow's offline tests; the daily schedule starts only
after the workflow reaches the default branch. Nothing is merged automatically.
