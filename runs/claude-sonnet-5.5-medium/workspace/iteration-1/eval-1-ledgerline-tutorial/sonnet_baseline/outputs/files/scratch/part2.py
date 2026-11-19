from ledgerline import Ledger

ledger = Ledger()
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3500.00", "March paycheck")

ledger.add("groceries", "-84.50", "Market")
ledger.add("groceries", "-23.10", "Corner store")
ledger.add("rent", "-1200.00", "April rent")
ledger.add("salary", "3500.00", "April paycheck")

print(ledger.summarize())
for account, total in ledger.summarize().items():
    print(f"{account}: {total}")
print(ledger.summarize(["groceries", "rent"]))
print(ledger.summarize(["savings"]))
print(Ledger().summarize())
print(ledger.entries("groceries"))
ledger.add("groceries", 12.5, "Bakery")
