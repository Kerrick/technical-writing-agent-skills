import shutil, subprocess, sys, tempfile, pathlib

SRC = pathlib.Path(sys.argv[1])
work = pathlib.Path(tempfile.mkdtemp())
shutil.copy(SRC, work / "ledgerline.py")

BASE = '''from decimal import Decimal

from ledgerline import Ledger

ledger = Ledger()
ledger.add("salary", Decimal("4200.00"), memo="October paycheck")
ledger.add("rent", Decimal("-1500.00"), memo="October rent")
'''
S1 = '''ledger.add("groceries", Decimal("-84.20"), memo="Market Street Grocer")
ledger.add("groceries", Decimal("-61.35"), memo="Corner market")
ledger.add("salary", Decimal("4200.00"), memo="November paycheck")
ledger.add("rent", Decimal("-1500.00"), memo="November rent")
'''
FLOAT = 'ledger.add("groceries", -84.20, memo="Market Street Grocer")\n'
S2 = '''rent_total = sum(entry.amount for entry in ledger.entries("rent"))
print(rent_total)
'''
S3 = '''totals = {}
for entry in ledger.entries():
    totals[entry.account] = totals.get(entry.account, Decimal("0")) + entry.amount

print(totals)
'''
S4 = '''summary = ledger.summarize()
print(summary)
print(summary == totals)
'''
S4X = 'print(list(summary.items()) == list(dict(sorted(totals.items())).items()))\n'
S4B = '''summary = ledger.summarize()
print(summary)
'''
S5 = '''spending = ledger.summarize(accounts=["groceries", "rent"])
print(spending)
'''
M1 = '''# Wrong: "utilities" has no entries, so it is missing from the result
# and the last line raises KeyError.
spending = ledger.summarize(accounts=["groceries", "rent", "utilities"])
print(spending)
print(spending["utilities"])
'''
M1FIX = '''spending = ledger.summarize(accounts=["groceries", "rent", "utilities"])
print(spending)
print(spending.get("utilities", Decimal("0")))
'''
EXTRA = '''print(ledger.summarize(accounts=["Rent"]))
print(ledger.summarize(accounts="rent"))
print(ledger.summarize(accounts=["rent"]))
L = Ledger(); L.add("car", 1); L.add("car-insurance", 2)
print(L.summarize(accounts="car-insurance"))
print(Ledger().summarize())
print(repr(sum(e.amount for e in ledger.entries("utilities"))))
'''
FINAL = BASE + S1.replace("", "") + '''
for account, total in ledger.summarize().items():
    print(f"{account:<12}{total:>10}")
'''
# final in the doc has no blank line between adds; rebuild exactly
FINAL = BASE + S1 + '''
for account, total in ledger.summarize().items():
    print(f"{account:<12}{total:>10}")
'''

def run(name, code):
    (work / "budget.py").write_text(code)
    r = subprocess.run([sys.executable, "budget.py"], cwd=work, capture_output=True, text=True)
    print(f"===== {name}")
    print(r.stdout + r.stderr, end="")

r = subprocess.run([sys.executable, "-c", "import ledgerline; print(ledgerline.__version__)"], cwd=work, capture_output=True, text=True)
print("===== version\n" + r.stdout + r.stderr, end="")
run("base", BASE)
run("float", BASE + FLOAT)
run("step2", BASE + S1 + S2)
run("step3", BASE + S1 + S3)
run("step4", BASE + S1 + S3 + S4 + S4X)
run("step4b", BASE + S1 + S4B)
run("step5", BASE + S1 + S4B + S5)
run("mistake1", BASE + S1 + S4B + M1)
print("line of spending[...] in mistake1 file:", (BASE + S1 + S4B + M1).splitlines().index('print(spending["utilities"])') + 1)
run("fix", BASE + S1 + S4B + M1FIX)
run("extra", BASE + S1 + EXTRA)
run("final", FINAL)
print(repr(subprocess.run([sys.executable, "budget.py"], cwd=work, capture_output=True, text=True).stdout))
run("final-1550", FINAL.replace('"-1500.00"), memo="November', '"-1550.00"), memo="November'))
