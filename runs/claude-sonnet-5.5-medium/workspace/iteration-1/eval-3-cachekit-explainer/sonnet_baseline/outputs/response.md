I wrote the explainer page and saved it to `outputs/how-caching-works-in-cachekit.md`.

**Assumptions:**
- **Reader:** backend developers who know `lru_cache`, reading away from the keyboard.
- **Mode:** a conceptual explanation. It has a short comparison table, then one section per decorator, a decision flow, and a list of what cachekit doesn't do.

**What I ran.** I ran a script against `cachekit.py` with Python 3.15 and confirmed these behaviors:
- `@cached` ignores keyword arguments in its key. `price(1, currency="USD")` followed by `price(1, currency="EUR")` returns the USD value both times. The page's example output is the real output.
- `@memoize` treats `f(1)`, `f(a=1)`, `f(1, b=0)` and `f(1, 0)` as four separate entries.
- A bare `@cached` with no `(ttl=...)` fails silently. It replaces your function with a decorator, and calling it returns a function instead of raising an error.
- Only `cache_clear` exists on `@cached` functions. `cache_info` doesn't, so you can't see hit rates.
- Exceptions aren't cached, `None` results are cached, and unhashable arguments raise `TypeError` in both decorators.

**What I couldn't verify:**
- The concurrency section (no locking, so a cache stampede is possible) comes from reading the source. I didn't test it, and the page says so.
- The `fetch_rate_from_provider`, `load_tax_table` and `lookup_price` calls in the examples are placeholders, not real cachekit code.

**Things to review:**
- The page recommends keeping `functools.lru_cache(maxsize=...)` for bounded caches, because cachekit has no size limit. Check that this matches your team's policy.
- Neither decorator evicts entries, so `@cached` can leak memory on high-cardinality keys even with a TTL. The page calls this out because it's easy to miss. You may want to raise it with the cachekit owners.