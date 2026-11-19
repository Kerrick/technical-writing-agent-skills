# How caching works in cachekit

cachekit stores the result of a function call so that the next call with the same inputs returns the stored result instead of running the function again. It offers two decorators: `@memoize` and `@cached(ttl=...)`. They look similar and are easy to swap by mistake, but they differ in three ways that matter: **when an entry expires**, **what counts as "the same inputs"**, and **how much memory they can use**.

This page explains those differences and how to choose. It is not a function-by-function reference, and it does not cover shared caches such as Redis (see [Scope](#scope)). If you are looking for `functools.lru_cache`, that is a different tool. `@memoize` is the closest cachekit equivalent, as described in [Coming from `functools.lru_cache`](#coming-from-lru-cache).

## The short version {#short-version}

| | `@memoize` | `@cached(ttl=...)` |
|---|---|---|
| Entry lifetime | Until the process exits or you clear it | `ttl` seconds after the value was computed |
| Cache key | All positional **and** keyword arguments | Positional arguments **only** |
| Keyword arguments | Part of the key | **Ignored** |
| Bounded size | No | No |
| Eviction | Never | Only when the same key is called again after expiry |
| Inspect statistics (`cache_info()`) | Yes | No |
| Clear (`cache_clear()`) | Yes | Yes |
| Shared between worker processes | No | No |

Use `@memoize` for values that never change while the process runs. Use `@cached` for values that go stale, and call it with positional arguments only.

## Ideas both decorators share {#shared-ideas}

**Per-process storage.** Each decorator keeps its entries in a dictionary inside the Python process. Every worker process has its own copy. If you run four workers, a value can be computed four times, and clearing the cache in one worker does not clear it in the others.

**Hashable arguments.** Both build a dictionary key from the arguments, so every argument must be hashable. Passing a list or dict raises `TypeError`:

```text
memoize  -> unhashable type: 'list'
cached   -> cannot use 'tuple' as a dict key (unhashable type: 'list')
```

**Only successful returns are stored.** If the function raises, nothing is cached and the next call runs the function again.

**Shared result objects.** A cache hit returns the stored object itself, not a copy. If the function returns a list or dict and a caller mutates it, every later caller sees the mutation.

## `@memoize`: remember forever {#memoize}

`@memoize` is a thin wrapper over `functools.cache`. It never expires and never evicts.

```python
from cachekit import memoize

@memoize
def tax_rate(country):
    ...  # slow lookup

tax_rate("DE")  # runs the function
tax_rate("DE")  # served from the cache
```

```text
>>> tax_rate.cache_info()
CacheInfo(hits=1, misses=1, maxsize=None, currsize=1)
```

The key includes keyword arguments, and it records *how* you passed each argument. These three calls are three separate entries, even though they mean the same thing:

```python
@memoize
def price(amount, currency="USD"):
    return f"{amount} {currency}"

price(1)
price(1, "USD")
price(1, currency="USD")
```

```text
>>> price.cache_info()
CacheInfo(hits=0, misses=3, maxsize=None, currsize=3)
```

That is safe, because a call never returns another call's result. The cost is wasted entries and misses. Call a memoized function the same way everywhere.

Because `@memoize` never evicts, **memory grows with the number of distinct argument combinations**. Use it only where that number is small and fixed, such as country codes, feature-flag names or config sections. Do not use it on a function that takes user IDs, request IDs, free text or timestamps.

## `@cached(ttl=...)`: remember for a while {#cached}

`@cached(ttl=60)` stores each result with the time it was computed. A later call with the same key returns the stored value if fewer than `ttl` seconds have passed (measured with `time.monotonic()`). Otherwise it calls the function again and replaces the entry.

```python
from cachekit import cached

@cached(ttl=60)
def exchange_rate(pair):
    ...  # call a rate service
```

`ttl` is the age of the entry, counted from when the value was computed. Cache hits do not extend it.

Two behaviours follow from how it is built:

- **Expired entries are not removed in the background.** An entry is replaced only when its key is called again. A key that is never called again stays in memory. `@cached` limits how *stale* a value can be, not how *large* the cache can grow.
- **Concurrent calls are not coordinated.** If two threads miss on the same key at the same moment, both run the function.

### Keyword arguments are not part of the key {#cached-keyword-trap}

This is the most common source of confusion. `@cached` builds its key from positional arguments only. A call that passes a value by keyword gets the same key as a call that omits it.

```python
@cached(ttl=60)
def convert(amount, currency="USD"):
    return f"{amount} {currency}"

# WRONG: currency is passed by keyword, so it is not part of the cache key.
convert(1, currency="USD")  # '1 USD'
convert(1, currency="EUR")  # '1 USD'  <- stale, wrong currency
# RIGHT: pass it positionally, so it is part of the cache key.
convert(1, "EUR")           # '1 EUR'
```

Real output of these three calls:

```text
1 USD
1 USD
1 EUR
```

The second call returns the cached result of the first because both have the key `(1,)`. There is no error and no warning. The function gets the wrong answer quietly.

To stay safe, apply one of these:

- Declare the parameters that change the result as positional, and always pass them positionally.
- Use `@memoize` if the function does not need to expire.
- Do not put `@cached` on functions whose result depends on keyword-only parameters. Python rejects positional use of those, so they can never become part of the key.

## Coming from `functools.lru_cache` {#coming-from-lru-cache}

If you know `lru_cache`, these mappings help:

| In `functools` | In cachekit |
|---|---|
| `functools.cache` (same as `lru_cache(maxsize=None)`) | `@memoize`, which is a direct wrapper |
| `lru_cache(maxsize=128)` (bounded, evicts least recently used) | No equivalent. Use `functools.lru_cache` directly. |
| Time-based expiry | `@cached(ttl=...)`. `functools` has none. |
| Keyword arguments in the key | `@memoize`: yes. `@cached`: **no**. |

The point where habits from `lru_cache` mislead is `@cached`. It looks like a cache with an expiry added, but it keys differently from `lru_cache`, and it does not evict by size. If you need a bound on memory, `@cached` does not provide one.

## Choosing between them {#choosing}

Start from the first question and stop at the first match.

1. **Does the value ever change while the process is running?** If no, use `@memoize`, provided the set of distinct arguments is small and fixed.
2. **Is the set of arguments large or unbounded** (user IDs, request IDs, search text)? Neither decorator bounds memory. Use `functools.lru_cache(maxsize=...)` if staleness is acceptable, or a cache outside the process if it is not.
3. **Does the value go stale, and can you tolerate a value up to `ttl` seconds old?** Use `@cached`, and pass every argument that affects the result positionally.
4. **Does every worker need to see the same value, or does a change need to be visible immediately?** Neither decorator does this. Use a shared cache or skip caching.

Do not use either decorator for functions with side effects, since a cache hit skips the side effect, or for results that depend on the current user or request unless that information is a positional argument.

## Clearing the cache {#clearing}

Both decorators add `cache_clear()`. It empties the cache of the current process only. Use it in tests so one test's cached values do not leak into the next.

```python
exchange_rate.cache_clear()
```

Only `@memoize` functions have `cache_info()`. `@cached` functions do not, so you cannot read hit counts from them.

## Scope {#scope}

This page covers the two decorators in the `cachekit` module. It does not cover caching across processes or machines; cachekit has no such feature. For exact signatures and docstrings, read the module source in `cachekit.py`.
