from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", "3200.00", memo="November paycheck")
ledger.add("rent", "-1450.00", memo="November rent")

ledger.add("groceries", "-82.15", memo="Farmers market")
ledger.add("groceries", "-46.30", memo="Corner store")
ledger.add("salary", "3200.00", memo="December paycheck")
ledger.add("rent", "-1450.00", memo="December rent")

totals = ledger.summarize()
print(totals)

print()
for account, total in totals.items():
    print(f"{account:<10} {total:>9}")

rent_entries = ledger.entries("rent")
print()
print(len(rent_entries), "rent entries")
print(sum(entry.amount for entry in rent_entries))

spending = ledger.summarize(accounts=["rent", "groceries", "utilities"])
print()
print(spending)
print(spending.get("utilities", 0))

ledger.add("utilities", "-64.20", memo="Electric bill")
print()
print(ledger.summarize(accounts=["rent", "groceries", "utilities"]))
