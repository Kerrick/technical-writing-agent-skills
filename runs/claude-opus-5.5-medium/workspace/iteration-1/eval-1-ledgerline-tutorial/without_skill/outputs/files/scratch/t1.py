import sys; sys.path.insert(0, sys.argv[1])
from ledgerline import Ledger

ledger = Ledger()
ledger.add("rent", "-1500.00", memo="March rent")
ledger.add("salary", "4200.00", memo="March paycheck")
ledger.add("groceries", "-86.40", memo="Market run")
ledger.add("groceries", "-123.15", memo="Weekly shop")
ledger.add("salary", "4200.00", memo="April paycheck")
ledger.add("rent", "-1500.00", memo="April rent")

totals = ledger.summarize()
print(totals)
for account, total in totals.items():
    print(f"{account:<10} {total:>10}")
print(ledger.summarize(accounts=["rent", "salary"]))
print(ledger.summarize(accounts=["rent", "utilities"]))
print(ledger.summarize(accounts="rent"))
print(sum(totals.values()))
print(Ledger().summarize())
try:
    ledger.add("coffee", 4.50)
except TypeError as e:
    print("TypeError:", e)
