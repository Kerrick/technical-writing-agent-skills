# How caching works in cachekit: `@memoize` vs `@cached`

cachekit gives you two decorators that both store a function's return value so the next call with the same arguments skips the work. They look similar and behave differently. This page explains the model behind each one and how to choose. It is written for backend developers who already know `functools.lru_cache`.

This page is true for cachekit 4.0.1. It covers the two decorators and their semantics. It is not a reference for every attribute, and it does not cover shared caches such as Redis, because cachekit has none (see [What cachekit does not do](#what-cachekit-does-not-do)).

## The short answer

| Question | `@memoize` | `@cached(ttl=...)` |
| - | - | - |
| Does an entry expire? | Never | After `ttl` seconds |
| What is the cache key? | All arguments, positional and keyword | **Positional arguments only** |
| Are entries ever evicted? | No | No. Expired entries are overwritten on the next call with the same key. |
| Is it shared across worker processes? | No | No |
| Can I inspect it? | `cache_info()`, `cache_clear()`, `cache_parameters()` | `cache_clear()` only |
| Do arguments need to be hashable? | Yes | Yes (positional ones) |

Use `@memoize` when the answer for a given input never changes while the process lives. Use `@cached(ttl=...)` when the answer can go stale and you can tolerate it being up to `ttl` seconds old.

## Mental model: one dictionary per decorated function, per process

Both decorators keep a plain in-memory dictionary, created when the decorator is applied, one per decorated function. Nothing is written to disk or sent over the network. Each worker process (for example, each Gunicorn or uWSGI worker) builds its own copy, and a restart empties it.

Consequences that apply to both decorators:

- **Each worker warms up separately.** With 8 workers, the first request for a given key can miss 8 times.
- **Workers can disagree.** Worker A may hold a value that worker B has already refreshed.
- **Memory grows with the number of distinct keys.** Neither decorator has a size limit (see [Memory growth](#memory-growth)).
- **Exceptions are not cached.** If the function raises, nothing is stored and the next call runs the function again.
- **`None` is a valid cached value.** A function that returns `None` is not re-run on the next hit.

## `@memoize`: cache forever

`memoize` is a thin wrapper over `functools.cache` (the same thing as `lru_cache(maxsize=None)`). If you know `lru_cache`, you know `memoize`, including its tools:

```python
from cachekit import memoize

@memoize
def tax_rate(country_code, product_category):
    return load_tax_table()[country_code][product_category]

tax_rate("DE", "books")
tax_rate("DE", "books")   # served from the cache
print(tax_rate.cache_info())
tax_rate.cache_clear()
```

Things to know:

- **The key is the full call signature.** Positional and keyword arguments are all part of the key. As with `lru_cache`, `f(1)` and `f(a=1)` are different keys. In a test run, `f(1)`, `f(a=1)`, `f(1, b=0)` and `f(1, 0)` against `def f(a, b=0)` produced four misses and four entries.
- **Arguments must be hashable.** A list argument raises `TypeError: unhashable type: 'list'`.
- **There is no eviction and no expiry.** Unlike `lru_cache`, there is no `maxsize` to set. `memoize` is `lru_cache(maxsize=None)` and nothing else.
- **The only way to refresh a value is `cache_clear()` or a restart.**

Good fits: pure functions of their inputs, such as parsing a config file, compiling a regular expression, or computing a value from constants, where the set of possible arguments is small and fixed.

## `@cached(ttl)`: cache for a time window

`cached` stores each result with the time it was computed (from `time.monotonic()`). On a later call with the same key, it returns the stored value if less than `ttl` seconds have passed. Otherwise it calls your function again and overwrites the entry.

```python
from cachekit import cached

@cached(ttl=60)
def exchange_rate(base, quote):
    return fetch_rate_from_provider(base, quote)

exchange_rate("USD", "EUR")   # calls the provider
exchange_rate("USD", "EUR")   # within 60 s: served from the cache
```

Things to know:

- **You must call it with a `ttl`.** `@cached(ttl=60)` is correct. A bare `@cached` is a mistake that fails quietly: `cached` receives your function as `ttl` and returns a decorator, so your function name now refers to that decorator. In a test run, `@cached` on `g(x)` left `g` as a plain function, and `g(3)` returned without raising and without running your code. Always write the parentheses and the `ttl`.
- **Expiry is lazy.** Nothing runs in the background. An expired entry stays in memory until the same key is requested again.
- **`ttl=0` never hits.** The check is `elapsed < ttl`, so no entry is ever fresh.
- **Only `cache_clear()` is available.** There is no `cache_info()`, so you cannot see hit rates from the decorator itself. Calling `price.cache_info()` raises `AttributeError`.
- **The original function is available** as `fn.__wrapped__` (cachekit uses `functools.wraps`), which is useful in tests that need to bypass the cache.

### The keyword-argument trap

This is the most common source of bugs. `cached` builds its key from positional arguments only. Keyword arguments are passed to your function on a miss, but they are ignored when looking up the entry.

```python
@cached(ttl=60)
def price(sku, currency="USD"):
    return lookup_price(sku, currency)

price(1, currency="USD")   # miss: computes the USD price and stores it under key (1,)
price(1, currency="EUR")   # hit: returns the USD price. The EUR request never reaches your function.
price(1, "EUR")            # miss: key is (1, "EUR"), a different entry
```

Verified output of those three calls: `1-USD 1-USD 1-EUR`. The second call returns the wrong currency, silently, until the first entry expires. Which value you get depends on which call ran first in that worker, so the bug can look intermittent.

The same applies to any argument that changes the answer: a tenant, a locale, a user ID, a feature flag. If it can change the result, either pass it positionally, or do not use `cached` for that function.

Rules that avoid the trap:

1. Pass every argument that affects the result **positionally** at every call site.
2. Or give the cached function only positional parameters, and keep a keyword-friendly wrapper around it.
3. Or use `@memoize` if you do not need expiry. It keys on keyword arguments too.

### Memory growth

`cached` removes nothing on its own. The dictionary keeps one entry per distinct positional-argument tuple for the life of the process. A TTL limits how long a value is served, not how long it is stored. A function keyed on user ID or search query can grow without bound in a long-lived worker. Keep `cached` for functions whose key space is small, or bounded by something outside the cache.

## Choosing between them

Ask these questions in order:

1. **Can the result change while the process runs?** If no, use `@memoize`. If yes, continue.
2. **Can you accept stale values for up to N seconds?** If yes, use `@cached(ttl=N)`. If no, do not cache with cachekit; the value must be read fresh or invalidated explicitly.
3. **Does any keyword argument change the result?** If yes with `@cached`, restructure the call so those arguments are positional (see [the trap](#the-keyword-argument-trap)).
4. **How many distinct keys can there be?** If the answer is unbounded, neither decorator is safe on its own, because neither evicts.

| Situation | Use |
| - | - |
| Parsing a static config or template once | `@memoize` |
| Compiling a regular expression from a constant | `@memoize` |
| Looking up an exchange rate that refreshes every minute | `@cached(ttl=60)` |
| Reading a feature flag that operators change at runtime | `@cached(ttl=...)`, with a `ttl` equal to how long a stale flag is acceptable |
| Per-user data with millions of users | Neither. Use a bounded cache such as `functools.lru_cache(maxsize=...)`, or a shared store |
| A value that must be correct immediately after a write | Neither. Read through, or invalidate explicitly |

If you are migrating from `lru_cache`:

| `functools` | cachekit equivalent |
| - | - |
| `@lru_cache(maxsize=None)` or `@cache` | `@memoize` (identical) |
| `@lru_cache(maxsize=N)` | No equivalent. Keep using `lru_cache`. |
| A hand-written TTL cache | `@cached(ttl=...)`, mind the keyword-argument key |

## Concurrency

Neither decorator takes a lock. If two threads, or two requests in an async handler running in separate threads, miss the same key at once, both call your function and both store a result (a "cache stampede"). For `@memoize` the call count can be more than one but the value stays consistent. For `@cached`, the later write wins. Do not rely on either decorator to ensure that an expensive or side-effecting function runs once. This page did not test concurrent behavior; the statement follows from reading the source, which contains no locking.

## What cachekit does not do

- No shared cache between processes or hosts.
- No size limit or least-recently-used eviction.
- No background expiry or refresh.
- No per-call invalidation of a single key. You can only clear the entire cache of one function with `cache_clear()`.
- No caching of exceptions.

If you need any of these, use a different tool rather than working around cachekit.

## Related

- Source: `cachekit.py`. The docstrings on `memoize` and `cached` are the authoritative reference for behavior.
- [`functools.cache` and `functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.cache) in the Python documentation, for the behavior `@memoize` inherits.
