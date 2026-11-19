I wrote the explainer page and saved it as `outputs/how-caching-works-in-cachekit.md`. I ran the code samples against `cachekit.py`, and the output blocks on the page are the real output. I didn't check the page against the skill's pre-publish checklist item by item.

The page makes three points:
- **Expiry:** `@memoize` never expires and never evicts. `@cached(ttl=…)` expires each entry `ttl` seconds after the value was computed.
- **Keys:** `@memoize` keys on positional and keyword arguments. `@cached` keys on positional arguments only. The page shows the stale-result case from the docstring: `convert(1, currency="EUR")` returns `1 USD`, with no error. The wrong version is marked as wrong inside the code block.
- **Memory:** neither decorator bounds memory. `@cached` only limits how stale a value can be.

It also has a side-by-side table and a short "Coming from `functools.lru_cache`" mapping. It ends with a choose-by-question decision list, and it covers per-process storage, `cache_clear()`, and the limit that only `@memoize` has `cache_info()`.

A few claims on the page come from reading the code rather than from running it:
- A function that raises is not cached.
- Cache hits return the same object, not a copy.
- Two threads that miss on the same key both run the function.

Two calls I made, which you may want to check:
- **No internal links.** I didn't invent links to sibling pages. The page points to the `cachekit.py` source for exact signatures. If you have a reference page, add a link to it in the Scope section.
- **No version number.** I left `__version__` out of the prose, per the skill.