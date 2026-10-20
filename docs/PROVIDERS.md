# Provider evaluation and integration boundaries

| Provider | Implemented use | Production considerations |
|---|---|---|
| [FMP](https://site.financialmodelingprep.com/developer/docs) | Preferred profile, quote, annual statements, adjusted OHLCV, TTM ratios, annual PE history and bounded peer comparisons | Documented API; paid entitlements and geographic coverage vary. Header API-key authentication. Indian symbols are resolved by directory plus exchange rather than stripped to US symbols. |
| [Yahoo / yfinance](https://ranaroussi.github.io/yfinance/) | Explicit opt-in fallback: profiles, statements, adjusted history, news and FX | Unofficial, personal-use terms, no service guarantee. Four annual periods are common, so five-year CAGR or DCF may be unavailable. Disabling Yahoo also disables its news/FX fallback. |
| [Finnhub](https://finnhub.io/docs/api/company-news) | Company-news ingestion with symbol + company-name filtering | Documented API; market/plan coverage varies. Does not establish that an article was read in full. |
| [SEC EDGAR](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Automatic CIK mapping and prioritized official submissions metadata | Identifying SEC_USER_AGENT required. Filings remain metadata until inspected. Form 8-K structured items 1.03 and 4.02 trigger review; no narrative audit-opinion extraction. Companyfacts evaluated but not merged automatically because taxonomy, annual/quarterly contexts and restatements require issuer-specific normalization. |
| [Alpha Vantage](https://www.alphavantage.co/documentation/) | Evaluated, not an active adapter | Adjusted daily data and fundamentals are documented; endpoint entitlements, small request budgets and inconsistent global regulatory metrics make it a poor default for this mixed-market watchlist. Raw daily OHLC must not masquerade as adjusted data. |
| [NSE official data](https://www.nseindia.com/static/market-data/real-time-data-subscription) / [BSE](https://www.bseindia.com/) / company IR | Evaluated as primary disclosure sources; no scraping-based universal adapter claimed | Production feed use requires suitable access/licensing and stable issuer identifiers. Bot-protected web pages are not treated as a reliable API. Bank regulatory metrics, pledges, audit opinions and qualitative moat data remain N/A unless a suitable future adapter supplies dated evidence. |

Client caches use original retrieval timestamps. Requests have timeouts, bounded
retries, exponential backoff, per-host spacing and capped Retry-After waits.
No expired cache is silently served as current. Provider failures are isolated by
ticker and provider. Conflicting values retain first-provider priority, alternative
observations and >10% discrepancy flags; currencies must agree before any merge.
No paid API key is required to run the fixture tests. FMP calls are bounded: six
annual statement periods, three peers and one adjusted-history window per ticker.

Optional LLM summaries use the
[Responses structured-output interface](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).
Only supplied public headline/snippet evidence is sent; output citations must match
supplied article IDs, and extractive quotes must occur verbatim in evidence.
Model impact descriptions remain unverified and cannot alter scores or overrides.
No browsing tools or full-article access are supplied to that model. No retries of
paid generation are attempted automatically; identical evidence is cached.
