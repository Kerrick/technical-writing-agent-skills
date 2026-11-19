import sys, time
sys.path.insert(0, sys.argv[1])
import cachekit
from cachekit import memoize, cached
print(cachekit.__version__)

calls = []
@cached(ttl=60)
def get_price(product_id, currency="USD"):
    calls.append((product_id, currency))
    return f"{product_id} in {currency}"
print(get_price(42, currency="USD"))
print(get_price(42, currency="EUR"))
print(get_price(42, "EUR"))
print("calls:", calls)

@memoize
def get_price_m(product_id, currency="USD"):
    return f"{product_id} in {currency}"
print(get_price_m(42, currency="USD"))
print(get_price_m(42, currency="EUR"))
print(get_price_m.cache_info())
print(get_price_m(42), get_price_m(product_id=42), get_price_m.cache_info())

print("has cache_info:", hasattr(get_price, "cache_info"), hasattr(get_price, "cache_clear"))

try:
    get_price_m([1])
except TypeError as e:
    print("memoize:", e)
try:
    get_price([1])
except TypeError as e:
    print("cached:", e)

@cached(ttl=0.1)
def now_ts(k):
    return time.monotonic()
a = now_ts(1); b = now_ts(1); time.sleep(0.15); c = now_ts(1)
print("hit within ttl:", a == b, "hit after ttl:", a == c)

@cached(ttl=0.01)
def sq(n):
    return n * n
for i in range(1000):
    sq(i)
time.sleep(0.05)
for cell in sq.__closure__:
    if isinstance(cell.cell_contents, dict):
        print("store size after expiry:", len(cell.cell_contents))

n = [0]
@cached(ttl=60)
def flaky(x):
    n[0] += 1
    raise ValueError("boom")
for _ in range(2):
    try:
        flaky(1)
    except ValueError:
        pass
print("flaky calls:", n[0])

@cached
def oops(x):
    return x * 2
print("oops(3) ->", oops(3))
print("memoize maxsize:", memoize(lambda: 1).cache_info().maxsize)
