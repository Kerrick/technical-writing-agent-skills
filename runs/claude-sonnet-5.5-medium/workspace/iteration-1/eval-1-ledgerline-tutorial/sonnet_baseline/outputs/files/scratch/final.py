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
print(ledger.entries("groceries"))
ledger.add("groceries", "12.50", "Bakery")

ledger.add("salary","250.00","Bonus")
print(ledger.summarize(["salary"]))
l=Ledger();l.add("sal","1");l.add("x","1");print(l.summarize("salary"))
l.add("a","5");l.add("a","-5");print(l.summarize(["a"]))
