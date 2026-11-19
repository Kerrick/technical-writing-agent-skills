I've written the explainer and saved it to `outputs/cachekit-caching-explained.md`.

**What it says.** `@memoize` is just `functools.cache`, so everything your team knows about `lru_cache` carries over. `@cached(ttl)` is a separate implementation, and it builds its cache key from positional arguments only. It opens with an exchange-rate example: after a USD lookup, `quote="EUR"` returns the USD rate without calling the function. That is the likely source of the mix-ups.

The rest of the page covers:
- **What each decorator stores:** a side-by-side table, with `lru_cache` as the reference point.
- **Three wrong beliefs, each corrected:**
  - Expired entries are not cleaned up. Both caches only ever grow.
  - `cache_clear()` clears only the current worker process.
  - Writing `@cached` without parentheses doesn't raise an error. Your function gets a function object back instead of a value.
- **Shared behavior:** neither decorator caches exceptions or stops several threads from computing the same missing value at once. Neither accepts lists or dicts as arguments, and on methods, cached instances are never garbage-collected.
- **When to use which:** `@memoize` when the result can't change while the process runs, `@cached(ttl)` when results may be up to `ttl` seconds stale, and neither in some cases.
- **A safeguard:** declare cache-affecting parameters positional-only with `/` and no default. Callers who pass them by keyword then get a `TypeError` instead of the wrong cached result.

**How I checked it.** All behavior comes from `cachekit.py` (version 4.0.1). I ran every example and claim on Python 3.15 using scripts in `scratch/`. The output on the page is real. The wording of the error for lists and dicts depends on the Python version, and the page says so.

**For you to decide:**
- **The opinions are mine.** The page recommends positional-only parameters, `lru_cache(maxsize=N)` for unbounded inputs, and Redis when every worker must see the same value. Change these if your team has its own rules.
- **Two links are placeholders.** They're marked `TODO(verify)`: one for your internal cachekit reference page and one for a shared-cache (Redis) guide, if you have one.
- **Possible bugs in cachekit itself.** Silently ignoring keyword arguments and accepting `@cached` with no TTL are probably worth fixing in the package. Raising an error when keyword arguments are passed, or including them in the key, would remove the main hazard this page warns about.