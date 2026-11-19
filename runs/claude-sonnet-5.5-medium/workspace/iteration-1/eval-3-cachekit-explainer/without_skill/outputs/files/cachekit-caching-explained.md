# How caching works in cachekit: `@memoize` vs `@cached`

cachekit gives you two decorators for caching function results inside a web handler process. They look similar and are easy to mix up, but they make different promises. This page explains the model behind each one and how to choose. It's written for people who already know `functools.lru_cache`.

*Applies to cachekit 4.0.1.*

## The short version

| | `@memoize` | `@cached(ttl)` |
|---|---|---|
| Question it answers | "This result never changes." | "This result is fine to reuse for N seconds." |
| Lifetime of an entry | Until the process exits (or `cache_clear()`) | `ttl` seconds, then recomputed on the next call |
| Cache key | All positional **and** keyword arguments | Positional arguments **only**. Keyword arguments are ignored |
| Size limit | None | None |
| Scope | Per process | Per process |
| Built on | `functools.cache` | A small dict-based wrapper in cachekit |

Rule of thumb: **use `@memoize` for pure functions of their inputs, and `@cached` for data that goes stale.** If you use `@cached`, pass arguments positionally (see [the keyword-argument trap](#the-keyword-argument-trap)).

## Mental model: how each relates to `lru_cache`

`@memoize` is `functools.cache` under a different name, and `functools.cache` is `lru_cache(maxsize=None)`. So if you know `lru_cache`, you already know `@memoize`, with one important difference:

- It is **unbounded**. Unlike `@lru_cache` (default `maxsize=128`), nothing is ever evicted. Every distinct argument combination stays in memory until the process dies.
- Arguments must be hashable, or you get a `TypeError`.
- Because the stdlib cache is underneath, you also get `cache_info()` and `cache_clear()`.

`@cached` is **not** an `lru_cache` variant. It adds time-based expiry, which the stdlib doesn't offer, but it is a simpler implementation with different key rules:

- It stores `(timestamp, value)` in a plain dict, keyed on the tuple of positional arguments.
- On each call it checks whether the entry is younger than `ttl`. It uses `time.monotonic()`, so system clock changes don't affect it. If the entry is fresh, it returns the stored value. If not, it calls the function and overwrites the entry.
- It exposes `cache_clear()` but **not** `cache_info()`.

## Behavior shared by both decorators

**Caches are per process.** Each worker (gunicorn/uvicorn worker, Celery worker, and so on) holds its own independent cache. With 8 workers, the same call can be computed 8 times, and workers can briefly disagree about a `@cached` value. Neither decorator coordinates across processes or hosts. If you need a shared cache or cross-worker invalidation, you need an external store such as Redis. cachekit doesn't provide one.

**Exceptions are not cached.** If the function raises, nothing is stored, and the next call tries again.

**Return values are shared, not copied.** A cache hit returns the *same object* every time. If a handler mutates a returned list or dict, every later caller sees the mutation. Return immutable values (tuples, frozensets, frozen dataclasses) or copy before mutating.

**No locking.** If two threads call a cold function at the same moment, both may run it. That is harmless for idempotent lookups, but it matters for expensive or side-effecting functions. Neither cache prevents a stampede on a cold or just-expired key.

**Methods include `self` in the key.** On an instance method, `self` is a positional argument, so it becomes part of the key. It must be hashable, and the cache holds a reference to the instance, which keeps it alive. Prefer decorating module-level functions.

## `@memoize` in detail

```python
from cachekit import memoize

@memoize
def parse_feature_flags(raw: str) -> dict:
    ...
```

Use it when:

- The function is **pure**: the same inputs always produce the same output.
- The set of possible inputs is **small or naturally bounded**: parsing config, compiling a regex per locale, looking up an enum-like mapping.
- The data is effectively **immutable for the life of the process**, such as a schema loaded at startup.

Don't use it when:

- Inputs are **high-cardinality or user-controlled** (user IDs, search strings, request payloads). The cache grows without limit, which is a memory leak. If you still want a cache here, use `functools.lru_cache(maxsize=...)` directly.
- The result depends on something that **changes** (database rows, remote APIs, the current time). It will be stale until restart.

Keys follow `functools.cache` rules: arguments are matched by how the call was written, so `f(1)` and `f(a=1)` are separate entries. This is the same behavior you're used to from `lru_cache`.

## `@cached(ttl)` in detail

```python
from cachekit import cached

@cached(ttl=60)
def get_exchange_rate(currency):
    ...
```

`cached` is a decorator *factory*. It always takes `ttl` (in seconds), so a bare `@cached` without arguments will not work.

Use it when:

- The data **changes slowly** and being up to `ttl` seconds out of date is acceptable (exchange rates, feature-flag snapshots, permission lookups, rarely edited reference data).
- You want to **bound staleness** instead of caching forever.

### How expiry actually works

Expiry is lazy. Nothing runs in the background:

- An entry past its TTL is only replaced when someone calls the function with that same key again.
- An entry that is never requested again **stays in memory indefinitely**. There is no eviction. TTL controls freshness, not memory use.

So `@cached` has the same unbounded-growth risk as `@memoize` if the key space is large. A `@cached(ttl=60)` function called with a million distinct user IDs will hold a million entries, including long-expired ones.

`cache_clear()` empties the whole cache for that function. It is useful in tests and for manual invalidation.

### The keyword-argument trap

The key is **positional arguments only**. Keyword arguments are passed to your function on a miss but are never part of the key. This is the example from the cachekit docstring:

```python
@cached(ttl=300)
def price(amount, currency="USD"):
    ...

price(1, currency="USD")   # computes, caches under key (1,)
price(1, currency="EUR")   # returns the cached USD result!
```

It gets worse when everything is passed by keyword: `price(amount=1)` and `price(amount=2)` both use the empty key `()`, so they share one cache entry.

This is the biggest difference from `lru_cache` and `@memoize`, and the most common source of "why am I getting someone else's data?" bugs. To avoid it:

1. **Call `@cached` functions with positional arguments only**, and make that a team convention.
2. Better, **make the result-affecting parameters positional-only** in the signature, so the mistake raises a `TypeError` instead of silently returning stale data:
   ```python
   @cached(ttl=300)
   def price(amount, currency, /):
       ...
   ```
3. If callers need keyword syntax, put a thin wrapper in front that passes everything positionally to the cached inner function.

## Choosing between them

Work through these questions in order:

1. **Can the result change while the process is running?** If not, `@memoize` fits. If so, `@cached(ttl)`.
2. **Is the number of distinct inputs bounded?** If not, neither decorator is safe as is. Use `functools.lru_cache(maxsize=N)` or an external cache.
3. **Does the function take keyword arguments that change the result?** If so, `@cached` needs the positional-only treatment above. `@memoize` is fine.
4. **Do all workers need to agree, or do you need to invalidate everywhere at once?** Neither works. Use a shared cache.

| Scenario | Use |
|---|---|
| Compile a regex or parse config for a small set of strings | `@memoize` |
| Load a static lookup table (country codes, schema) | `@memoize` |
| Fetch exchange rates, tolerate 5 minutes of staleness | `@cached(ttl=300)` |
| Per-user permission check on every request | `@cached(ttl=...)`, watching key-space size, or a bounded `lru_cache` |
| Expensive computation, many distinct inputs, no staleness concern | `functools.lru_cache(maxsize=N)` |
| Result must be consistent across all workers | External shared cache |

## Comparison with `lru_cache`

| | `lru_cache` | `@memoize` | `@cached` |
|---|---|---|---|
| Size bound | `maxsize` (default 128) | None | None |
| Eviction | LRU | Never | Never (an entry is only overwritten when the same key is called after its TTL) |
| Expiry | None | None | TTL, checked on read |
| Keyword args in key | Yes | Yes | **No** |
| `cache_info()` | Yes | Yes | No |
| `cache_clear()` | Yes | Yes | Yes |

## Testing and debugging

- Call `cache_clear()` between tests so cached state doesn't leak from one test into the next.
- On a `@memoize`d function, `cache_info()` shows hits, misses and current size, which is useful for spotting unbounded growth.
- A `@cached` function has no `cache_info()`. If you suspect staleness or key collisions, first check whether any callers pass keyword arguments.
