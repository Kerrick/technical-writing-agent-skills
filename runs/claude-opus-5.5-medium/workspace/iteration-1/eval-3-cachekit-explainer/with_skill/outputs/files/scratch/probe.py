import sys
sys.path.insert(0, "evals/developer-docs/files")
import cachekit

print(round(40 * 0.79, 2), round(25 * 0.92, 2), round(25 * 0.79, 2))
try:
    cachekit.memoize()
except TypeError as e:
    print(e)


@cachekit.cached
def rate(c):
    return 1


print(rate("EUR"))
f = cachekit.memoize(lambda x: x)
print([a for a in dir(f) if a.startswith("cache")], type(f))
