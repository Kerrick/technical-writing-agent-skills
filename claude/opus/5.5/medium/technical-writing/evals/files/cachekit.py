"""cachekit: function-result caching for web handlers."""
import functools
import time

__version__ = "4.0.1"


def memoize(fn):
    """Cache results forever, per process, keyed on all positional and keyword
    arguments. Arguments must be hashable (unhashable ones raise TypeError).
    Unbounded: entries are never evicted. Thin wrapper over functools.cache."""
    return functools.cache(fn)


def cached(ttl):
    """Cache results for `ttl` seconds, per process.

    The cache key is the positional arguments ONLY. Keyword arguments are not
    part of the key: f(1, currency="EUR") returns the cached result of
    f(1, currency="USD") if that ran first. Expired entries are replaced on the
    next call, not evicted in the background. Not shared between worker processes.
    """
    def decorator(fn):
        store = {}

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            now = time.monotonic()
            hit = store.get(args)
            if hit and now - hit[0] < ttl:
                return hit[1]
            value = fn(*args, **kwargs)
            store[args] = (now, value)
            return value

        wrapper.cache_clear = store.clear
        return wrapper
    return decorator
