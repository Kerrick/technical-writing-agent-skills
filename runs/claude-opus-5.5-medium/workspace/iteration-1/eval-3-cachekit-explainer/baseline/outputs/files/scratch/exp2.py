import sys
sys.path.insert(0, sys.argv[1])
from cachekit import cached, memoize

@cached(ttl=300)
def get_price(product_id, currency, /):
    print(f"  computing {product_id} {currency}")
    return f"{product_id} in {currency}"

print(get_price(42, "USD"))
print(get_price(42, "EUR"))
print(get_price(42, "USD"))
try:
    get_price(42, currency="EUR")
except TypeError as e:
    print("TypeError:", e)

# The example from the page: kwargs ignored
@cached(ttl=300)
def get_exchange_rate(base, quote="USD"):
    print(f"  fetching {base}->{quote}")
    return {"USD": 1.0, "EUR": 0.92}[quote]

print(get_exchange_rate("USD", quote="USD"))
print(get_exchange_rate("USD", quote="EUR"))

@memoize
def get_exchange_rate_m(base, quote="USD"):
    print(f"  fetching {base}->{quote}")
    return {"USD": 1.0, "EUR": 0.92}[quote]

print(get_exchange_rate_m("USD", quote="USD"))
print(get_exchange_rate_m("USD", quote="EUR"))
print(get_exchange_rate_m("USD", quote="EUR"))
print(get_exchange_rate_m.cache_info())
get_exchange_rate.cache_clear()
print(get_exchange_rate("USD", quote="EUR"))
