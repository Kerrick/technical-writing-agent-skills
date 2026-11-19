#!/bin/sh
# Usage: run.sh N  -- concatenates step0..stepN into budget.py and runs it
cd "$(dirname "$0")" || exit 1
cp ../evals/developer-docs/files/ledgerline.py .
: > budget.py
i=0
while [ "$i" -le "$1" ]; do
  cat "step$i.py" >> budget.py
  i=$((i + 1))
done
python3 budget.py
