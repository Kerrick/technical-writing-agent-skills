import sys

sys.path.insert(0, "evals/developer-docs/files")
from cachekit import cached, memoize

n = []


def boom(x):
    n.append(x)
    raise ValueError


for deco in (memoize, cached(60)):
    f = deco(boom)
    for _ in range(2):
        try:
            f(1)
        except ValueError:
            pass
print("exceptions run each time:", len(n) == 4)

z = []
g = cached(0)(lambda x: z.append(x))
g(1); g(1)
print("ttl=0 never hits:", len(z) == 2)

h = cached(60)(lambda x, opts=None: x)
print("unhashable kwarg ok:", h(1, opts=[1]) == 1)
for deco in (memoize, cached(60)):
    try:
        deco(lambda x: x)([1])
    except TypeError as e:
        print("unhashable positional:", e)

lst = cached(60)(lambda: [1])
a = lst(); a.append(2); print("shared object:", lst())
