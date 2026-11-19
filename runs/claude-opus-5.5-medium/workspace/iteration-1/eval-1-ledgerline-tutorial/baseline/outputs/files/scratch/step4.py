
spending = ledger.summarize(accounts=["rent", "groceries", "utilities"])
print()
print(spending)
print(spending.get("utilities", 0))
