import sys
sys.path.insert(0, "../evals/developer-docs/files")
from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", "3000.00", "March pay")
ledger.add("rent", "-1200.00", "March rent")
ledger.add("salary", "3000.00", "April pay")
ledger.add("rent", "-1200.00", "April rent")

print(ledger.summarize())
print(ledger.summarize(["rent"]))
print(ledger.summarize(["groceries"]))
print(ledger.summarize("rent"))
print(Ledger().summarize())
try:
    ledger.add("groceries", 12.5)
except TypeError as e:
    print(e)
ledger.add("groceries", "-84.30", "Weekly shop")
print(ledger.summarize())
print(ledger.entries("rent"))
