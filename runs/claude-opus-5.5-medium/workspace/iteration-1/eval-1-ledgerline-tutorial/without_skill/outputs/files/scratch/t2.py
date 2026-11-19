import sys; sys.path.insert(0, sys.argv[1])
from ledgerline import Ledger

ledger = Ledger()

# March
ledger.add("rent", "-1500.00", memo="March rent")
ledger.add("salary", "4200.00", memo="March paycheck")
ledger.add("groceries", "-86.40", memo="Market run")

# April
ledger.add("groceries", "-123.15", memo="Weekly shop")
ledger.add("salary", "4200.00", memo="April paycheck")
ledger.add("rent", "-1500.00", memo="April rent")

totals = ledger.summarize()

for account, total in totals.items():
    print(f"{account:<10} {total:>10}")

print(f"{'net':<10} {sum(totals.values()):>10}")

from decimal import Decimal

totals = ledger.summarize(accounts=["rent", "utilities"])
print(totals.get("utilities", Decimal("0")))
ledger.add("ent", "1")
print(ledger.summarize(accounts="rent"))
