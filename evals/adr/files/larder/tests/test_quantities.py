import random


def test_ten_thousand_uses_sum_exactly():
    uses = [random.randint(1, 5000) for _ in range(10_000)]
    stock = sum(uses)
    for use in uses:
        stock -= use
    assert stock == 0 and all(isinstance(use, int) for use in uses)
