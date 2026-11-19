# How caching works in cachekit: `@memoize` vs. `@cached`

*Written for backend engineers who already know `functools.lru_cache` and want to know which cachekit decorator to reach for. Covers cachekit 4.0.1, checked against Python 3.15.*

cachekit has two decorators, and they differ in more than expiry:

- **`@memoize`** is `functools.cache` and nothing else. If you know `lru_cache(maxsize=None)`, you already know `@memoize`.
- **`@cached(ttl)`** is a separate implementation, not built on `functools`. Results expire after `ttl` seconds, and **keyword arguments are left out of the cache key.**

That second point causes most of the bugs. The rest of this page explains the model behind each decorator so you can predict, for any call, whether it hits the cache.

## The bug that keeps happening

Here's an exchange-rate lookup cached for five minutes:

```python
from cachekit import cached

@cached(ttl=300)
def get_exchange_rate(base, quote="USD"):
    print(f"  fetching {base}->{quote}")
    return {"USD": 1.0, "EUR": 0.92}[quote]

print(get_exchange_rate("USD", quote="USD"))
print(get_exchange_rate("USD", quote="EUR"))
```

```text
  fetching USD->USD
1.0
1.0
```

The second call asked for EUR, got the USD rate back, and never ran the function. Swap in `@memoize` and the same two calls do what you'd expect:

```text
  fetching USD->USD
1.0
  fetching USD->EUR
0.92
```

Someone familiar with `lru_cache` reads `@cached(ttl=300)` as "`lru_cache` with expiry." That's the wrong model, and this example shows where it breaks.

## What each decorator stores

Each decorated function owns one dictionary. It lives in the memory of a single Python process. The decorators differ in what they use as the dictionary key and what they store as the value.

| | `@memoize` | `@cached(ttl)` |
| - | - | - |
| Implementation | `functools.cache(fn)` | Plain `dict` inside a closure |
| Key | All positional **and** keyword arguments | The positional arguments tuple **only** |
| Value | The result | `(timestamp, result)` |
| Expiry | Never | After `ttl` seconds, on the next call with the same key |
| Size limit | None | None |
| Shared across worker processes | No | No |
| Unhashable arguments | `TypeError` | `TypeError` |
| Exceptions cached | No | No |
| `cache_clear()` | Yes | Yes |
| `cache_info()` | Yes | No (`AttributeError`) |

### `@memoize`: `functools.cache`, unchanged

The whole implementation is `return functools.cache(fn)`. Everything you know about `functools.cache` applies, including two details that are easy to forget:

- The key reflects how you called the function, not what you passed. `get_rate("USD")` and `get_rate(base="USD")` are two separate entries, so each one runs the function once.
- No entry is ever removed, except by `cache_clear()`. Memory grows by one entry for every distinct set of arguments for as long as the process runs.

### `@cached(ttl)`: positional key, timestamped value

On each call, `@cached`:

1. Looks up `args` (the positional arguments as a tuple) in its dictionary. `kwargs` are not consulted.
2. If it finds an entry less than `ttl` seconds old, it returns the stored result without calling your function.
3. Otherwise it calls your function with all arguments, positional and keyword, and stores `(start_time, result)` under `args`, replacing any older entry.

Keyword arguments reach your function, so the first result is computed correctly. Because they aren't part of the key, every later call with the same positional arguments gets that first result back, whatever keyword arguments it passes. Positional arguments are keyed correctly: `get_exchange_rate("USD", "EUR")` and `get_exchange_rate("USD", "USD")` are separate entries.

The timestamp is taken *before* your function runs. A function that takes 4 seconds under `ttl=10` returns a result that stays cached for about 6 seconds after it comes back.

Time comes from `time.monotonic()`, so changes to the system clock don't expire or extend entries.

## Three misconceptions

### "Expired entries are cleaned up"

They aren't. `@cached` checks the age of an entry only when the same key is requested again, and then overwrites it. Nothing runs in the background. An entry for a key that's never requested again stays in memory until the process exits or you call `cache_clear()`.

A test that cached 1,000 distinct keys with `ttl=0.01` and then waited for every entry to expire still found 1,000 entries in the store. A TTL bounds staleness. It doesn't bound memory. With both decorators, memory grows with the number of distinct argument combinations the process has seen.

That matters most for functions keyed on something unbounded, like a user ID or a search string, in long-lived worker processes.

### "`cache_clear()` invalidates the cache"

It clears the cache in the process that calls it. Each gunicorn or uvicorn worker, each Celery worker, and each replica has its own independent cache. If an admin endpoint calls `get_exchange_rate.cache_clear()`, only the worker that handled that request forgets the rate. The others keep serving the old value until their own entries expire (`@cached`) or forever (`@memoize`).

The same applies to consistency: two requests for the same key can get different answers depending on which worker they land on. If a result must be the same everywhere, or must change everywhere at once, an in-process cache is the wrong tool. Use a shared store instead.

### "`@cached` takes a default TTL"

It doesn't, and leaving off the parentheses doesn't raise an error:

```python
from cachekit import cached

@cached
def double(x):
    return x * 2

print(double(3))
```

```text
<function cached.<locals>.decorator.<locals>.wrapper at 0x108ec66c0>
```

Without parentheses, your function is passed in as `ttl` and you get back the inner decorator. Calling `double(3)` returns a function object instead of `6`. Nothing fails until something downstream tries to use that value. Always write `@cached(ttl=SECONDS)`.

## Other behavior the decorators share

- **Failures aren't cached.** If the function raises, nothing is stored, and the next call runs it again. A failing upstream service is called on every request; neither decorator gives you negative caching.
- **No stampede protection.** `@cached` takes no lock, so threads that miss on the same key at the same time each run the function. `functools.cache` can also run the function more than once for concurrent misses. Expect duplicate calls when a hot key expires under load.
- **Unhashable arguments raise.** Passing a `list` or `dict` raises `TypeError`. From `@memoize`: `unhashable type: 'list'`. From `@cached`: `cannot use 'tuple' as a dict key (unhashable type: 'list')`. (The exact wording depends on your Python version.)
- **On methods, `self` is part of the key.** Each instance gets its own entries, and the cache holds a reference to every instance it has seen, so those instances are never garbage-collected.

## When to use which

Pick by whether the answer can change.

**Use `@memoize` when the result can never change while the process runs:** pure computations, parsing static config, building a lookup table from a file shipped with the code. If the result depends on a database, an API, or the clock, `@memoize` serves stale data forever, so don't use it there.

**Use `@cached(ttl)` when the result can change but being `ttl` seconds stale is acceptable:** feature-flag lookups, exchange rates, a slow aggregate query behind a dashboard. Choose `ttl` from how stale the data is allowed to be, not from how slow the function is.

**Use neither when:**

- The arguments are unbounded and the process is long-lived. Both caches grow without limit. `functools.lru_cache(maxsize=N)` keeps an upper bound, if you can live without expiry.
- Every worker must see the same value, or invalidation must take effect everywhere. Use a shared cache such as Redis.
- The function has side effects that must happen on every call.

### Make `@cached` safe against keyword arguments

If a parameter changes the result, the cache key has to include it. With `@cached`, that means it must be passed positionally. You can make Python enforce this by declaring the parameters positional-only with `/` and giving them no default:

```python
from cachekit import cached

@cached(ttl=300)
def get_price(product_id, currency, /):
    return f"{product_id} in {currency}"

print(get_price(42, "USD"))
print(get_price(42, "EUR"))
get_price(42, currency="EUR")
```

```text
42 in USD
42 in EUR
Traceback (most recent call last):
  ...
TypeError: get_price() got some positional-only arguments passed as keyword arguments: 'currency'
```

The `TypeError` only fires when `@cached` misses and calls your function. If `currency` had a default, a caller could first cache `get_price(42)`, and a later `get_price(42, currency="EUR")` would hit that entry and return the default-currency price without raising. That's why the parameters need no default.

## Related

- [`functools.cache`](https://docs.python.org/3/library/functools.html#functools.cache) and [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache) in the Python docs.
- cachekit API reference: TODO(verify): link to the internal reference page for `memoize` and `cached`.
- Shared caching across workers: TODO(verify): link to the team's Redis caching guide, if one exists.
