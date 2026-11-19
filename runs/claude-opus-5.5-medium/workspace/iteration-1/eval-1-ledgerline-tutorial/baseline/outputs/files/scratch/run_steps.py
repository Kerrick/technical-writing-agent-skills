"""Run the tutorial's budget.py after each step, from a fresh process each time."""
import pathlib
import shutil
import subprocess
import sys

here = pathlib.Path(__file__).parent
shutil.copy(here.parent / "evals/developer-docs/files/ledgerline.py", here / "ledgerline.py")
code = ""
for n in range(6):
    code += (here / f"step{n}.py").read_text()
    (here / "budget.py").write_text(code)
    print(f"===== after step {n}")
    result = subprocess.run([sys.executable, "budget.py"], cwd=here, capture_output=True, text=True)
    print(result.stdout + result.stderr, end="")
print("===== python", sys.version)
