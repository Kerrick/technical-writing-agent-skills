# How caching works in cachekit: `@memoize` and `@cached`

cachekit gives you two decorators for caching function results: `@memoize` and `@cached(ttl)`. Both keep results in memory inside the current process. They differ in three ways that matter: how long a result is kept, which arguments decide whether a stored result is reused, and how you apply them. The last two are where most bugs come from.

This page describes cachekit 4.0.1. Both decorators are imported from the top-level package:

```python
from cachekit import cached, memoize
```

## Terms used on this page

- **Cache key**: the value a decorator builds from a call's arguments to look up a stored result. Two calls with the same cache key get the same result.
- **Cache entry**: one stored result, filed under one cache key.
- **Hit**: a call that finds an entry and returns it without running the function. **Miss**: a call that runs the function and stores the result.
- **TTL** (time to live): how many seconds `@cached` reuses an entry before the entry expires.

In conversation, "memoize" often means any kind of function-result caching. On this page, and in cachekit, `@memoize` means only the decorator that keeps results forever. `@cached` is the one with a TTL.

## Start from `functools.lru_cache`

If you know `functools.lru_cache`, you already know `@memoize`. It is a direct wrapper around `functools.cache`, which is `lru_cache(maxsize=None)`. These three definitions are exactly equivalent; real code would use only one:

```python
import functools

from cachekit import memoize


@memoize
def load_currency_format(currency):
    """Read and parse the formatting rules for `currency`."""


@functools.cache
def load_currency_format(currency):
    """Read and parse the formatting rules for `currency`."""


@functools.lru_cache(maxsize=None)
def load_currency_format(currency):
    """Read and parse the formatting rules for `currency`."""
```

`@memoize` returns the same `functools` wrapper object, so you get `cache_info()`, `cache_clear()`, and `cache_parameters()`, and all the `lru_cache` behavior you already know.

`@cached` is **not** built on `functools`. It is cachekit's own code, and it breaks several `lru_cache` habits:

| | `functools.lru_cache(maxsize=None)` | `@memoize` | `@cached(ttl=60)` |
|---|---|---|---|
| How you apply it | `@lru_cache(maxsize=None)` | `@memoize` (no parentheses) | `@cached(ttl=60)` (parentheses and a TTL are required) |
| Entries expire | Never | Never | After `ttl` seconds |
| Positional arguments in the cache key | Yes | Yes | Yes |
| **Keyword arguments in the cache key** | Yes | Yes | **No** |
| Bound on number of entries | None | None | None |
| Unhashable argument (list, dict) | `TypeError` | `TypeError` | `TypeError` (positional only; unhashable keyword arguments are never looked at) |
| `cache_clear()` | Yes | Yes | Yes |
| `cache_info()` | Yes | Yes | No |
| Shared between worker processes | No | No | No |

The row in bold is the one behind most `@cached` bugs. The section **The keyword-argument trap in `@cached`** shows what it does.

## Example setup

Every example on this page uses the same pricing function. The examples are written as Python interactive-session transcripts: lines starting with `>>>` or `...` are what you type, and the lines after them are what Python prints.

```python
>>> from cachekit import cached, memoize
>>> RATES = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79}
>>> BASE_PRICES_USD = {101: 25.00, 102: 40.00}
>>> def lookup_price(product_id, currency="USD"):
...     print(f"computing price for {product_id} in {currency}")
...     return round(BASE_PRICES_USD[product_id] * RATES[currency], 2)
```

The `print` call makes misses visible: when you see `computing price ...`, the function ran. When a call prints only a number, it was a hit. In real code this function would query a database or a rates service, which is the slow work that makes caching worth it.

To keep one shared setup, the examples apply the decorators by calling them, as in `memoize(lookup_price)`. That's the same thing `@memoize` does when you put it on a `def`.

## How `@memoize` works

`@memoize` stores every result forever, keyed on all positional and keyword arguments. Before you run the last call in this example, predict whether it will print `computing price ...`:

```python
>>> memo_price = memoize(lookup_price)
>>> memo_price(101, "EUR")
computing price for 101 in EUR
23.0
>>> memo_price(101, "EUR")
23.0
>>> memo_price(101, currency="EUR")
computing price for 101 in EUR
23.0
>>> memo_price.cache_info()
CacheInfo(hits=1, misses=2, maxsize=None, currsize=2)
```

The second call is a hit. The third call is a miss even though it means the same thing as the first, because the cache key records *how* each argument was passed. That's the same as `lru_cache`. The result is still correct. You just get a second entry, and the function runs one more time than it needs to.

The entry for `(101, "EUR")` stays until the process exits or something calls `memo_price.cache_clear()`. If the EUR rate changes while the process is running, `memo_price` keeps returning `23.0`.

## How `@cached` works

`@cached(ttl)` reuses an entry for `ttl` seconds, then runs the function again on the next call with that cache key. Here is the wrapper it builds. It is cachekit 4.0.1's code with two things left out: `functools.wraps`, which copies the function's name and docstring, and the `cache_clear` attribute. Otherwise it behaves the same.

```python
import time


def cached(ttl):
    def decorator(fn):
        store = {}  # cache key -> (time stored, result)

        def wrapper(*args, **kwargs):
            now = time.monotonic()
            hit = store.get(args)  # the key is args alone; kwargs are never looked at
            if hit and now - hit[0] < ttl:
                return hit[1]
            value = fn(*args, **kwargs)
            store[args] = (now, value)
            return value

        return wrapper

    return decorator
```

Three things in this code explain all of `@cached`'s behavior:

- The cache key is `args`, the tuple of positional arguments. `kwargs` are passed through to your function but never become part of the key.
- An expired entry stays in `store` until a call with the same cache key overwrites it. Nothing removes it in the background.
- `store` is a plain dictionary inside one process.

### A hit within the TTL

```python
>>> ttl_price = cached(ttl=60)(lookup_price)
>>> ttl_price(101, "EUR")
computing price for 101 in EUR
23.0
>>> ttl_price(101, "EUR")
23.0
```

The second call is within 60 seconds of the first, so it's a hit.

### A miss after the TTL

This example uses a one-second TTL so you can watch an entry expire:

```python
>>> import time
>>> short_price = cached(ttl=1)(lookup_price)
>>> short_price(102, "GBP")
computing price for 102 in GBP
31.6
>>> time.sleep(1.1)
>>> short_price(102, "GBP")
computing price for 102 in GBP
31.6
```

After the sleep, the entry has expired, so the second call runs the function again and stores the new result. The TTL counts from when the stored call *started*, not when it finished. A function that takes 5 seconds under `@cached(ttl=60)` gets about 55 seconds of reuse.

## The keyword-argument trap in `@cached`

> **Warning:** `@cached` leaves keyword arguments out of the cache key. A call that changes only a keyword argument gets the result stored for a different keyword value. There's no error, just the wrong result.

This continues with `ttl_price` from the section **A hit within the TTL**, which already has an entry for `(101, "EUR")`. Before reading on, predict what the second call here returns:

```python
>>> ttl_price(101)
computing price for 101 in USD
25.0
>>> ttl_price(101, currency="EUR")  # Wrong: returns the cached USD price
25.0
```

The first call stores the USD price under the cache key `(101,)`. The second call's positional arguments are also `(101,)`, so it's a hit, and it returns the USD price for a EUR request. If you're used to `lru_cache` or `@memoize`, you'd expect a miss here, followed by the correct price of `23.0`.

It gets worse when every argument is passed by keyword. Every such call has the same cache key, the empty tuple `()`, so one entry answers all of them:

```python
>>> kw_price = cached(ttl=60)(lookup_price)
>>> kw_price(product_id=101, currency="USD")
computing price for 101 in USD
25.0
>>> kw_price(product_id=102, currency="GBP")  # Wrong: every all-keyword call has the cache key ()
25.0
```

For the next 60 seconds, every all-keyword call to `kw_price` returns `25.0`, whatever product and currency it asks for.

### The fix: make cached arguments positional-only, with no defaults

Pass every argument that affects the result positionally. To make Python enforce that, declare those parameters positional-only (the `/` in the signature) and give them no default values. A caller who passes one by keyword then gets a `TypeError` instead of a wrong price. If you want callers to have keyword arguments and defaults, put them on a thin uncached wrapper that calls the cached function positionally:

```python
>>> @cached(ttl=60)
... def _cached_price(product_id, currency, /):
...     return lookup_price(product_id, currency)
>>> def price(product_id, currency="USD"):
...     return _cached_price(product_id, currency)
>>> price(101)
computing price for 101 in USD
25.0
>>> price(101, currency="EUR")
computing price for 101 in EUR
23.0
>>> price(product_id=102, currency="GBP")
computing price for 102 in GBP
31.6
```

Each call gets its own entry, because `price` always passes both arguments positionally to `_cached_price`.

The next sample is meant to fail. It shows what happens when someone calls the cached function directly with a keyword argument:

```python
>>> _cached_price(101, currency="EUR")  # Raises TypeError, as intended
Traceback (most recent call last):
  ...
TypeError: _cached_price() got some positional-only arguments passed as keyword arguments: 'currency'
```

> **Aside: Why the cached parameters must not have defaults**
>
> `@cached` looks up the cache before it calls your function. Say you write `def _cached_price(product_id, currency="USD", /)`. Then `_cached_price(101)` succeeds and stores an entry under `(101,)`. Later, `_cached_price(101, currency="EUR")` also has positional arguments `(101,)`. It's a hit, so the function never runs, Python never checks the keyword argument, and the call returns the USD price with no error. Without defaults, no call with fewer positional arguments can ever succeed, so no such entry can ever be stored.

## `@cached` needs parentheses; `@memoize` doesn't

`@memoize` takes the function directly. `@cached` takes a TTL and returns the decorator. If you swap the forms, you get two different failures.

`@memoize()` with parentheses fails right away when the module loads, with `TypeError: memoize() missing 1 required positional argument: 'fn'`.

`@cached` without parentheses fails silently:

```python
>>> @cached  # Wrong: missing (ttl=...)
... def exchange_rate(currency):
...     return RATES[currency]
>>> exchange_rate("EUR")
<function cached.<locals>.decorator.<locals>.wrapper at 0x...>
```

Your function was passed in as the TTL, so `exchange_rate` is now cachekit's internal decorator function. Calling it returns a new wrapper function, not a rate. Nothing fails until code downstream tries to use that function as a number. Write `@cached(ttl=60)`, or whatever TTL you need.

## Neither cache is shared between processes

Both caches live in the memory of one Python process. If your service runs several worker processes (for example, gunicorn or uWSGI workers), each worker has its own separate cache:

- Each worker misses once for every cache key before it has anything to reuse.
- `cache_clear()` clears only the cache in the process that calls it. Calling it from the request handler that saves a new price clears one worker. The other workers keep serving the old price, until the TTL runs out under `@cached`, or until they restart under `@memoize`.
- Two workers can return different results for the same call at the same moment.

cachekit has no way to invalidate entries across processes. If a result has to change everywhere as soon as the underlying data changes, cachekit is the wrong tool. Use a cache that all workers share, or don't cache that result.

## Neither cache limits its size

`@memoize` never removes an entry. `@cached` doesn't either: an expired entry is replaced only when a call with the same cache key comes in. An entry whose cache key is never used again stays in memory for the life of the process. With both decorators, memory use grows with the number of distinct cache keys the process has ever seen.

That's fine for arguments drawn from a small, fixed set, like currency codes or a few hundred product IDs. It is a slow memory leak for arguments that come from users and keep varying, like search strings, user IDs, or timestamps. If you need a cap on the number of entries, use `functools.lru_cache(maxsize=...)` directly. It has no TTL, and cachekit has no bounded version.

## Choosing between `@memoize` and `@cached`

Answer these in order:

1. **Must every worker see a change as soon as the data changes?** Use neither. See **Neither cache is shared between processes**.
2. **Can the set of distinct arguments grow without limit?** Use neither. Use `functools.lru_cache(maxsize=...)`, or don't cache. See **Neither cache limits its size**.
3. **Can the result for given arguments change while the process is running?** For example: prices, exchange rates, feature flags, or anything read from a database or another service.
   - **Yes:** use `@cached(ttl=...)`. Pick the longest TTL whose staleness you can accept. Make every argument that affects the result positional-only with no default, as shown in **The fix: make cached arguments positional-only, with no defaults**.
   - **No:** the result is fixed for the life of the process. For example: parsing a config file that ships with the deploy, or building a lookup table from constants. Use `@memoize`.

Comparing a function's call sites with these answers will also catch most existing misuse. Look for `@memoize` on anything that reads changing data, and for `@cached` functions called with keyword arguments.

## Known limits and interactions

These apply to both decorators unless noted.

- **Returned objects are shared.** A hit returns the same object that was stored, not a copy. If a caller changes a returned list or dict, every later hit sees the change. Return immutable values (tuples, frozen dataclasses) from cached functions, or copy before changing.
- **Exceptions are not cached.** If the function raises, nothing is stored, and the next call runs the function again. A failing dependency is called on every request.
- **Concurrent misses can run the function more than once.** When threads call with the same cache key before the first call has stored its result, each of them can run the function. Neither decorator holds a lock while your function runs.
- **On methods, `self` is part of the cache key.** Decorating a method stores the instance in the cache, which keeps the instance from being garbage-collected. For `@memoize` that means forever. For `@cached` it means until an entry with the same cache key replaces it. This is the same trap as `lru_cache` on methods.
- **`@cached` has no `cache_info()`.** You can't read its hit rate. Use `@memoize`'s `cache_info()`, or add your own logging, if you need to measure hits.
- **`@cached` with `ttl=0` or a negative TTL never hits.** It still stores an entry on every call.
