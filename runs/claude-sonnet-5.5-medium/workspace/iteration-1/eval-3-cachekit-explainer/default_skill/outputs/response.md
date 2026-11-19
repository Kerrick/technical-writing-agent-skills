I wrote the explainer page and saved it as `outputs/how-caching-works-in-cachekit.md`. I ran the code samples against `cachekit.py` (4.0.1) and the outputs match what the page shows. The one exception is the bare-`@cached` example, which I fixed after the run and didn't re-run.

**What the page covers**
- **Shape:** It opens from `lru_cache`, since the team knows it. `@memoize` is shown to be exactly `functools.cache`.
- **Comparison table:** It sets `lru_cache`, `@memoize` and `@cached(ttl)` side by side. It marks the three rows where `@cached` differs from `lru_cache`: key, `cache_info`, and decorator syntax.
- **`@cached` implementation:** It walks through the short implementation to show where the surprises come from.
- **Choosing:** It ends with a "choosing between them" table and a "what cachekit leaves to you" list.

**Traps in `@cached`**
- **Keyword arguments aren't in the cache key.**
  - `price(10, currency="EUR")` returns the cached USD result.
  - `get_user(user_id=2)` returns user 1's data. That is a data-exposure bug, not just a wrong value.
  - The page shows both wrong forms and a fix using positional-only parameters (`def f(x, /)`).
- **`@cached` needs parentheses.** Bare `@cached` raises no error. It returns a function where you expected a value.

**Other behaviors the page documents**
- `@memoize` and `@cached` both grow without limit, and expired `@cached` entries are never removed.
- Neither decorator uses a lock.
- Only `cache_clear()` exists, so you can't invalidate one entry.
- Both return the stored object itself, so a caller that mutates it changes what later callers get.
- `@memoize` treats `f("DE")` and `f(code="DE")` as separate entries.

The page also states that sharing across worker processes and per-key invalidation aren't part of cachekit. It says nothing about future plans.

**Calls for you to check:** I gave the page a version line ("Applies to cachekit 4.0.1") because the source file had no changelog or versioning policy. If these docs track the latest release, you may want to drop that line. The page also assumes Python 3.8 or later for the `/` syntax. I didn't check your minimum supported Python version.