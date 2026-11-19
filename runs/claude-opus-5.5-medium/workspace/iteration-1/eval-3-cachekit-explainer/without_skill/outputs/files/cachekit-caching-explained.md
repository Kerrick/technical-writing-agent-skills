# How caching works in cachekit: `@memoize` vs `@cached`

*Applies to cachekit 4.0.1.*

cachekit has two decorators, and they look interchangeable. They aren't. They
build their cache keys differently, they expire entries differently, and one of
them can quietly return the wrong answer if you call it the wrong way. This page
covers how each one works, using `functools.lru_cache` as the reference point,
and when to use which.

## The short version

- **`@memoize`** is `functools.cache`, which is `lru_cache(maxsize=None)`. Use it
  for pure functions whose result never changes for the same inputs.
- **`@cached(ttl)`** is a small hand-written cache whose entries go stale after
  `ttl` seconds. Use it for results that change over time, like database lookups
  or calls to other services, where a slightly old answer is acceptable.
- **The trap:** `@cached` builds its key from **positional arguments only**.
  Keyword arguments aren't part of the key. If a cached function takes keyword
  arguments that change the result, either pass them positionally or don't use
  `@cached`.

## The mental model: lru_cache, then what changes

If you know `lru_cache`, you already understand most of this. Every function
cache answers the same four questions:

1. **What is the key?** What makes two calls "the same call"?
2. **When does an entry stop being valid?**
3. **When is an entry removed from memory?**
4. **Where does the cache live?**

| | `functools.lru_cache(maxsize=128)` | `cachekit.memoize` | `cachekit.cached(ttl)` |
|---|---|---|---|
| **Key** | Positional **and** keyword args | Positional **and** keyword args | **Positional args only** |
| **Unhashable args** | `TypeError` | `TypeError` | `TypeError` for positional args; keyword args are ignored, so they never raise |
| **Becomes invalid** | Never | Never | `ttl` seconds after the call that stored it |
| **Removed from memory** | When it's least recently used and the cache is full | Never (no size limit) | Only when the same key is called again after expiry, or on `cache_clear()` |
| **Size limit** | `maxsize` | None | None |
| **Scope** | Per process | Per process | Per process |
| **`cache_clear()`** | Yes | Yes | Yes |
| **`cache_info()`** | Yes | Yes | **No** |

The rest of this page explains the rows that cause trouble.

## `@memoize`: remember forever

```python
from cachekit import memoize

@memoize
def tax_bracket(income_cents: int, filing_status: str) -> int:
    ...
```

`memoize` just returns `functools.cache(fn)`. Everything you know about
`lru_cache` applies, with one difference: **there is no `maxsize`, so nothing
is ever evicted.** Each distinct set of arguments adds one entry, and the entry
stays until the process exits or someone calls `tax_bracket.cache_clear()`.

That's fine when the set of possible inputs is small and fixed, like
enum values, config keys, or a handful of country codes. It's a memory leak
when the inputs are unbounded, like user IDs, request payloads, or timestamps.
In a long-running worker, a `@memoize` on `get_user(user_id)` eventually holds
every user who ever made a request to that worker.

Keying follows `functools.cache` exactly. That includes one quirk:
`f(1)` and `f(x=1)` are stored as **separate entries**, as are
`f(a=1, b=2)` and `f(b=2, a=1)`. You get the correct result each time, but the
function may run more often than you expect.

**Use `@memoize` when** the function is pure (same inputs, same output, forever)
**and** the input space is bounded. If you need a size limit, use
`functools.lru_cache(maxsize=N)` directly; cachekit doesn't offer one.

## `@cached(ttl)`: remember for a while

```python
from cachekit import cached

@cached(ttl=300)
def exchange_rate(base: str, quote: str) -> Decimal:
    return rates_service.fetch(base, quote)
```

`cached` keeps its own dictionary that maps each key to a pair:
`(time stored, value)`. On every call it does this:

1. Looks up the key.
2. If an entry exists and is less than `ttl` seconds old, returns it.
3. Otherwise, calls the function, stores `(now, result)` under the key, and
   returns the result.

Time comes from `time.monotonic()`, so changes to the system clock don't affect
expiry. The timestamp is taken **before** the function runs, so a slow call
spends part of its TTL while it's still computing.

### The key is positional arguments only

This is where most bugs come from. Here's what the code does:

```python
hit = store.get(args)        # kwargs are not used
...
store[args] = (now, value)
```

Keyword arguments get passed to your function, but they never become part of the key.
So:

```python
@cached(ttl=60)
def price(sku, currency="USD"):
    ...

price(42, currency="USD")   # runs, stores under key (42,)
price(42, currency="EUR")   # cache hit on (42,): returns the USD price
price(42, "EUR")            # key (42, "EUR"): runs, correct EUR price
```

It gets worse if callers pass **everything** as keywords. Then `args` is
always the empty tuple `()`, and **every call shares one cache entry**,
whatever the arguments are:

```python
price(sku=42)   # runs, stores under key ()
price(sku=99)   # cache hit on (): returns the price for sku 42
```

It fails silently. There's no error and nothing shows up in the logs. The
result is just wrong, and it stays wrong for up to `ttl` seconds.

**Rules for `@cached` functions:**

- Every argument that affects the result must be passed **positionally**.
- To force this, make the parameters positional-only with `/`:

  ```python
  @cached(ttl=60)
  def price(sku, currency, /):
      ...
  ```

  Now `price(sku=42)` raises `TypeError` right away, so the mistake can't
  return wrong data.
- Keyword arguments are only safe for things that don't change the result,
  like a timeout or a logger.

### Expired entries are not cleaned up

Expiry is checked lazily, when a key is requested. Nothing runs in the
background. An expired entry only gets replaced if someone calls the function
with **that same key** again. There's no size limit either. So for a function
called with many distinct, mostly one-off keys (`@cached(ttl=60)` on
`get_session(session_id)`, say), the dictionary keeps growing and is never
pruned. A short TTL doesn't bound memory use. It only bounds how stale the
data can get.

If you need both a TTL and a memory bound, cachekit can't do it today.
Call `cache_clear()` periodically, or use a real cache (Redis, or
`cachetools.TTLCache`).

### Other differences from lru_cache

- There's no `cache_info()`, so you can't read hit and miss counts.
  `cache_clear()` exists and empties the whole store.
- Unhashable **positional** arguments (a list or dict) raise `TypeError` from
  the dictionary lookup. Unhashable keyword arguments don't raise, because
  they're never hashed. That's another clue that they aren't in the key.

**Use `@cached(ttl)` when** the result can change over time, serving a slightly
old value for up to `ttl` seconds is acceptable, and every argument that
affects the result is positional.

## What both decorators share

### Caches live in one process

Both caches are ordinary Python dictionaries inside a single process. Under
gunicorn, uWSGI, Celery, or anything else with multiple worker processes:

- Each worker has its **own** cache and fills it separately. Hit rates are
  lower than you'd expect, and memory use is multiplied by the number of
  workers.
- `cache_clear()` only clears the cache in the worker that called it. If you
  clear the cache in an admin endpoint after a data change, the other workers
  keep serving the old value (until the TTL runs out for `@cached`, or forever
  for `@memoize`).
- Two requests with the same arguments can get different answers, depending
  on which worker handles them and when that worker last refreshed.

If the data has to stay consistent across workers, or you need to invalidate
it when data changes, use a shared cache, not cachekit.

### Other things to know

- **Exceptions are not cached.** If the function raises, nothing is stored and
  the next call tries again.
- **`None` and other falsy values *are* cached.** A lookup that returns `None`
  for "not found" stays `None` for the TTL (`@cached`) or forever (`@memoize`).
- **Results are shared, not copied.** If the cached function returns a list or
  dict and a caller changes it, every later caller sees the change.
  Return immutable values (tuples, frozen dataclasses) or copy at the call site.
- **No protection against simultaneous misses.** If several threads miss the
  same key at once, each one calls the function. A cold cache in front of a
  slow service can send a burst of identical requests.
- **On methods, `self` is part of the key.** The cache holds a reference to every
  instance it has seen, which keeps those instances alive. Usually you want
  to decorate a module-level function instead.

## Choosing between them

Ask these questions in order:

1. **Does the result for the same inputs ever change?** (Database rows,
   service calls, anything that depends on time or configuration.)
   - No → `@memoize` (check question 3).
   - Yes → `@cached(ttl)` (check questions 2 and 3), or a shared cache if
     question 4 applies.
2. **Can every argument that affects the result be positional?**
   - Yes → `@cached`, and declare those parameters positional-only with `/`.
   - No → Don't use `@cached` as-is. Wrap the function so the keyword arguments
     are converted to positional ones, or use another cache.
3. **Is the set of distinct inputs small and bounded?**
   - Yes → Either decorator is fine for memory.
   - No → Neither one bounds memory. Use `functools.lru_cache(maxsize=N)` (for
     pure functions) or a size-limited TTL cache.
4. **Do all workers need to agree on the value, or does it need to be
   invalidated when data changes?**
   - Yes → Use a shared cache like Redis. Per-process caching is the wrong
     tool.

### Quick examples

| Function | Use | Why |
|---|---|---|
| `parse_feature_flag_name(raw: str)` | `@memoize` | Pure, with a small set of inputs |
| `country_for_code(code: str)` (static table) | `@memoize` | Pure and bounded |
| `exchange_rate(base, quote, /)` | `@cached(ttl=300)` | Changes over time, a few minutes of staleness is fine, positional-only |
| `get_user(user_id)` | Neither | Unbounded keys, and changes must show up in every worker |
| `search(query, *, page=1, sort="relevance")` | Neither as-is | Unbounded keys, and with `@cached` the keyword arguments would be ignored |
| `price(sku, currency="USD")` called as `price(sku, currency=c)` | **Not `@cached`** | Returns the wrong currency |

## Common mistakes

- **Moving a function from `@memoize` to `@cached` to "add a TTL".** If any
  caller passes keyword arguments, this change makes results wrong.
  Check every call site, or make the parameters positional-only first.
- **Assuming a short TTL keeps memory down.** It doesn't. Expired entries stay
  in memory until the same key is requested again.
- **Calling `cache_clear()` to invalidate after a write.** This only clears
  one worker's cache.
- **Reading the decorator name as a guarantee.** "Cached for 60 seconds" means
  "up to 60 seconds stale, in this process, for this exact positional key."
