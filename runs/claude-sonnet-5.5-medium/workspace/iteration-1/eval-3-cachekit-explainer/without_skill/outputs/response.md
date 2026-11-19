I wrote the explainer to `outputs/cachekit-caching-explained.md`. I based it only on reading `cachekit.py` (4.0.1). I didn't run any of the code.

The page explains each decorator through its relationship to `lru_cache`, since that's what your team knows:

- **`@memoize`** is `functools.cache` under another name. Nothing is ever evicted, unlike `lru_cache`'s default `maxsize=128`. It keys on all arguments, including keyword arguments. It also gives you `cache_info()`.
- **`@cached(ttl)`** is a separate, simpler implementation. Expiry is lazy, so an expired entry is only replaced when that same key is called again. Entries that are never requested again stay in memory.

Three details in the code are likely to cause real bugs, and the page calls them out:

- **Keyword arguments are ignored in `@cached`'s key.** `f(1, currency="EUR")` returns the cached USD result. Calls made entirely by keyword all share one entry, because the key is `()`. The page suggests positional-only parameters (`/`) so the mistake raises an error.
- **Both caches are unbounded and per process.** TTL controls freshness, not memory. Each worker has its own cache, so workers can disagree.
- **Behaviors the code doesn't cover.** The page also covers shared mutable return values, no locking against stampedes, and `self` ending up in the key on methods.

It ends with a decision checklist, a scenario table, a three-way comparison with `lru_cache`, and testing tips.

The "no locking" and "return values are shared" points come from reading the code, not from tests. `@cached` is also missing `cache_info()`, and the page flags that.