I've written the explainer page and saved it as `outputs/cachekit-caching-explained.md`. Every claim in it comes from reading `cachekit.py` (v4.0.1). I tried to run a quick script to confirm the keying behavior, but it needed approval and didn't run, so none of the examples have been executed.

The page is built around a side-by-side table comparing `functools.lru_cache`, `@memoize` and `@cached`. It covers what goes into the key, when entries expire, when they're removed, size limits, and which helper methods each one has. Then it takes each decorator in turn, ends with a step-by-step guide for choosing one, and lists common mistakes.

What your team most needs to know, and what the page stresses:

- **`@cached` ignores keyword arguments when building the key.** So `price(42, currency="EUR")` can return the cached USD price. Worse, if callers pass every argument by keyword, the key is always empty and every call shares one entry, no matter the arguments. The page suggests declaring the parameters positional-only (with `/`) so this mistake raises an error instead of returning wrong data.
- **`@memoize` is just `functools.cache`.** It has no size limit, so using it on unbounded inputs like user IDs leaks memory.
- **A short TTL doesn't keep `@cached` small.** Expired entries are only replaced when the same key is called again, and there's no size limit.
- **Both caches live in one process.** Each worker has its own copy, and `cache_clear()` only clears the worker that calls it.
- **Smaller behaviors worth knowing:**
  - Exceptions aren't cached, but `None` is.
  - Callers share the same returned object, so changing a cached list or dict affects everyone.
  - Several threads missing the same key at once each run the function.
  - On methods, `self` is part of the key, which keeps every instance alive.
  - `@cached` has no `cache_info()`.

The first two points are probably worth raising with whoever maintains cachekit, not just documenting.