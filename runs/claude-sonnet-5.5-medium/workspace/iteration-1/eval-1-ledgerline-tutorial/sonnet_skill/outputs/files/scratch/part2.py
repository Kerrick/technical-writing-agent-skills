from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", "3000.00", "March pay")
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3000.00", "April pay")
ledger.add("rent", "-1200.00", "April rent")
totals = ledger.summarize()
print(totals)
ledger.add("groceries", "-84.30", "Weekly shop")
print(ledger.summarize())
print(ledger.summarize(["rent", "groceries"]))
print(ledger.summarize(["groceries_typo"]))
