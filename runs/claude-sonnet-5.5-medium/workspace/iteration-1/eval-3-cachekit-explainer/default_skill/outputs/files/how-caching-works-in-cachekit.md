# How caching works in cachekit

Applies to cachekit 4.0.1.

cachekit gives you two decorators that cache a function's return value: `@memoize` and `@cached(ttl=...)`. They look like cousins, but they follow different rules for what counts as "the same call" and for when an entry goes away. Choosing the wrong one, or using `@cached` as if it were `lru_cache`, returns wrong results without raising an error.

This page explains the model behind both decorators, then helps you choose. It doesn't cover shared or cross-process caching: both decorators keep their cache in the memory of one process. Redis and similar stores are outside cachekit.

Both decorators come from the `cachekit` package:

```python
from cachekit import memoize, cached
```

## Start from what you know: `functools.lru_cache`

If you know `functools.lru_cache`, you already know most of `@memoize`. It is a thin wrapper over `functools.cache`, which is `lru_cache(maxsize=None)`. Its whole body is:

```python
def memoize(fn):
    return functools.cache(fn)
```

That makes the equivalence exact: `@memoize` and `@functools.cache` behave identically, including the extra methods `cache_info()` and `cache_clear()`. Everything you know about `functools.cache` applies, including the hazards below.

`@cached(ttl=...)` is not a wrapper over `lru_cache`. It is a small, separate implementation with different rules. This table puts the two side by side, with `lru_cache` for reference.

| | `functools.lru_cache` | `@memoize` | `@cached(ttl)` |
|---|---|---|---|
| Decorator syntax | `@lru_cache` or `@lru_cache(maxsize=...)` | `@memoize` (no parentheses) | `@cached(ttl=60)` (parentheses and `ttl` required) |
| Cache key | All positional and keyword arguments | All positional and keyword arguments | **Positional arguments only** |
| Entries expire | Only by LRU eviction when `maxsize` is set | Never | After `ttl` seconds, measured with `time.monotonic()` |
| Size limit | `maxsize` (default 128) | None: unbounded | None: unbounded |
| Unhashable arguments | `TypeError` | `TypeError` | `TypeError` |
| `cache_clear()` | Yes | Yes | Yes |
| `cache_info()` | Yes | Yes | **No** |
| Shared between worker processes | No | No | No |

The bold cells are where habits from `lru_cache` mislead you. The next sections cover each one.

## `@memoize`: remember forever

`@memoize` stores every distinct call's result for the life of the process. Use it for values that don't change while the process runs and that come from a small set of inputs.

```python
from cachekit import memoize

@memoize
def load_country(code):
    # Stands in for a database query or file read.
    return {"code": code}

load_country("DE")
load_country("DE")
print(load_country.cache_info())
```

```text
CacheInfo(hits=1, misses=1, maxsize=None, currsize=1)
```

The second call is a hit. `maxsize=None` shows that nothing is ever evicted.

### Argument spelling creates separate entries

Like `functools.cache`, `@memoize` keys on how you called the function, not on what the arguments mean. `load_country("DE")` and `load_country(code="DE")` are two entries, and the function body runs for each:

```python
load_country("DE")
load_country(code="DE")
print(load_country.cache_info())
```

```text
CacheInfo(hits=1, misses=2, maxsize=None, currsize=2)
```

(Counts continue from the previous example.) This wastes memory but never returns a wrong value. Pick one calling style per function and use it everywhere.

### Arguments must be hashable

`load_country(["DE"])` raises `TypeError: unhashable type: 'list'`. Pass a tuple instead.

### Unbounded means unbounded

`@memoize` never evicts. If the arguments come from user input, such as user IDs, search strings, or request parameters, the cache grows with every new value until the process restarts. Use it only where the set of possible arguments is small and fixed. For anything else, use `@cached`, or `functools.lru_cache(maxsize=...)` if you need a size bound.

## `@cached(ttl)`: remember for a while

`@cached(ttl=60)` stores a result for 60 seconds. A call within 60 seconds of the one that stored it returns the stored value. A later call runs the function again and replaces the entry. Use it for data that changes slowly and where slightly stale values are acceptable: exchange rates, feature flags, configuration fetched from another service.

```python
from cachekit import cached

rates = {"USD": 1.0, "EUR": 0.9}

@cached(ttl=60)
def convert(amount, currency):
    return amount * rates[currency]

convert(10, "EUR")  # runs the function; result is stored for 60 seconds
convert(10, "EUR")  # returns the stored result
```

### What the implementation does

Most of the surprises come from the implementation, which is short. This is the body of `cached`, with comments added. It is explanatory, so don't copy it into your code: import `cached` instead.

```python
def cached(ttl):
    def decorator(fn):
        store = {}

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            now = time.monotonic()
            hit = store.get(args)               # key: positional args only
            if hit and now - hit[0] < ttl:      # still fresh?
                return hit[1]
            value = fn(*args, **kwargs)         # miss or expired: call the function
            store[args] = (now, value)          # replace any old entry
            return value

        wrapper.cache_clear = store.clear
        return wrapper
    return decorator
```

Three behaviors follow directly:

- **The key is `args`, the tuple of positional arguments.** `kwargs` are passed to the function but never looked at when finding or storing an entry.
- **Expired entries are replaced, not removed.** Nothing runs in the background. An entry for arguments that are never called again stays in memory for the life of the process, so the cache is unbounded in the number of distinct argument tuples.
- **There is no lock.** If two threads miss on the same key at once, both run the function and the last one to finish stores its result.

Other consequences:

- The function runs once per call that misses. An exception propagates and nothing is stored, so the next call runs the function again.
- A returned `None` is cached like any other value.
- `store` is private. The only handle you get is `cache_clear()`, which removes every entry, so you can't invalidate a single key.

### Keyword arguments are not part of the key

> **Warning: `@cached` ignores keyword arguments when matching calls.** Two calls that differ only in keyword arguments return the same cached result. No error is raised, and the result is the wrong one.

Here is the trap, using a function that takes a keyword:

```python
@cached(ttl=60)
def price(amount, currency="USD"):
    return amount * rates[currency]

price(10, currency="USD")   # runs the function, stores under key (10,)
price(10, currency="EUR")   # Wrong: returns the USD result; the function doesn't run
```

```text
10.0
10.0
```

The second call should return `9.0`. Its key is `(10,)`, the same as the first call, so the stored USD result comes back.

The same thing happens, more destructively, when you pass *every* argument by keyword. All such calls have the empty key `()`:

```python
@cached(ttl=60)
def get_user(user_id):
    return {"id": user_id}

get_user(user_id=1)   # {'id': 1}
get_user(user_id=2)   # Wrong: returns {'id': 1}
```

Here the second call returns user 1's data to a request for user 2, which makes this a data-exposure bug as well as a correctness bug.

The fix is to pass every argument that affects the result positionally. This version is correct:

```python
get_user(1)   # {'id': 1}
get_user(2)   # {'id': 2}
```

`lru_cache` and `@memoize` don't have this problem, so code that you move from one to the other can change behavior.

Enforce positional-only arguments at the definition so that callers can't make the mistake:

```python
@cached(ttl=60)
def get_user(user_id, /):
    return {"id": user_id}

get_user(user_id=2)  # TypeError: get_user() got some positional-only arguments passed as keyword arguments: 'user_id'
```

The `/` makes `user_id` positional-only (Python 3.8+), so a keyword call fails loudly instead of returning the wrong user.

### The decorator takes parentheses

`@memoize` is used bare. `@cached` is a decorator factory, so it always needs `(ttl=...)`. If you write `@cached` bare, Python passes your function as `ttl`, and the name is bound to the inner `decorator` function:

```python
@cached          # Wrong: missing (ttl=...)
def rate(currency):
    return rates[currency]

rate("EUR")      # no error: returns a function, not 0.9
```

```text
<function cached.<locals>.decorator.<locals>.wrapper at 0x...>
```

The call raises nothing. It returns a function object where you expected a number, and the failure appears later wherever you use the value. (A function with two or more parameters fails sooner, with a `TypeError` at the first call.)

### Time is measured per process

`ttl` is measured with `time.monotonic()`, so changes to the system clock don't affect expiry. The cache lives inside each worker process. With four workers, there are four independent caches, each with its own expiry timeline, and `cache_clear()` clears only the worker that runs it. A value that changes in the database can be visible in one worker and stale in another for up to `ttl` seconds.

## Choosing between them

| Situation | Use |
|---|---|
| Result never changes while the process runs, and the argument set is small and fixed (country codes, parsed config, compiled regexes) | `@memoize` |
| Result changes over time and some staleness is acceptable | `@cached(ttl=...)`, with every argument passed positionally |
| Argument values come from user input or are otherwise unbounded, and the result never goes stale | `functools.lru_cache(maxsize=...)` |
| Callers need to pass keyword arguments, and the result depends on them | `@memoize` if the result never goes stale; otherwise a different design, because `@cached` can't distinguish those calls |
| You need `cache_info()` for hit-rate metrics | `@memoize` |
| Results must be identical across workers, or must be invalidated for one key | Not cachekit: both decorators are per-process and `cache_clear()` is all-or-nothing |

Two questions settle most cases:

1. **Can the result change while the process runs?** If yes, you need a TTL, so use `@cached`. If no, use `@memoize`.
2. **Do the arguments come from a bounded set?** If no, `@memoize` is unsafe, because it never evicts.

## What cachekit leaves to you

- **Invalidating a single entry.** Only `cache_clear()` exists.
- **Bounding memory.** Neither decorator limits the number of entries.
- **Sharing results across processes.** Each worker has its own cache.
- **Preventing duplicate work on a simultaneous miss.** Neither decorator locks.
- **Mutable results.** Both return the stored object itself, not a copy. If a caller mutates the returned dict or list, every later caller sees the mutation. Return immutable values or copy before mutating.
