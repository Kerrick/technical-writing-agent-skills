
ledger.add("utilities", "-64.20", memo="Electric bill")
print()
print(ledger.summarize(accounts=["rent", "groceries", "utilities"]))
