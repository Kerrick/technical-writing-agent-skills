
rent_entries = ledger.entries("rent")
print()
print(len(rent_entries), "rent entries")
print(sum(entry.amount for entry in rent_entries))
