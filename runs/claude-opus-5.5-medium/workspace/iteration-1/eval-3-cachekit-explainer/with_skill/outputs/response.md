I wrote the explainer and saved it as `outputs/caching-in-cachekit.md`. It's written against cachekit 4.0.1. I ran all 30 interactive-session steps on the page with doctest and the plain code blocks as scripts. Everything ran and printed exactly what the page shows. I also tested each claim in "Known limits" against `cachekit.py`.

**How the page is organized**
- **Starting from `lru_cache`:** it opens with what your team already knows. `@memoize` is exactly `functools.cache`, which is `lru_cache(maxsize=None)`. `@cached` is cachekit's own code, and a comparison table shows where it breaks `lru_cache` habits.
- **One running example:** every example uses the same `lookup_price(product_id, currency="USD")` function. It prints a line when it actually runs, so you can see which calls were served from the cache.
- **The keyword-argument trap:** this gets the most space. `@cached` leaves keyword arguments out of the cache key, so `ttl_price(101, currency="EUR")` silently returns a cached USD price. If every argument is passed by keyword, all calls share one cache entry, so every product and currency gets the same answer.
- **The fix:** make the cached function's parameters positional-only with no defaults, and put the keyword arguments and defaults on a thin uncached wrapper. A short aside explains why: if a cached parameter has a default, the trap still works, even with `/` in the signature.
- **Other traps:** `@cached` without parentheses fails silently: calls return a function instead of a value. `@memoize()` with parentheses fails at once with an error. Neither cache is shared between worker processes, and `cache_clear()` only clears one worker. Neither cache has a size limit, and `@cached` never removes expired entries in the background, so memory keeps growing.
- **Choosing between them:** three ordered questions, plus a list of known limits. These cover shared mutable results, exceptions not being cached, concurrent cache misses, decorating methods, the missing `cache_info()` on `@cached`, and `ttl=0`.

**Decisions I made**
- I gave the fix for the keyword trap as the standard pattern. If you'd rather change `cachekit` so `@cached` includes keyword arguments in the key, the page will need updating.
- For cases where neither decorator fits, I recommend `functools.lru_cache(maxsize=...)` when you need a size limit. When results must update across workers, the page only says "a cache that all workers share" and doesn't name a product, because I don't know what your team uses. Name it if you have a standard one.
- I used gunicorn and uWSGI only as examples of servers that run several worker processes, not as a claim about your setup.
- The examples are interactive-session transcripts with `>>>` prompts, and the page explains the prompt once. If your docs platform's copy button doesn't strip prompts, readers will have to delete them by hand.

The check scripts are in `scratch/`, outside `outputs/`. You can delete them.