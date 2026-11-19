
ledger.add("groceries", "-82.15", memo="Farmers market")
ledger.add("groceries", "-46.30", memo="Corner store")
ledger.add("salary", "3200.00", memo="December paycheck")
ledger.add("rent", "-1450.00", memo="December rent")

totals = ledger.summarize()
print(totals)
