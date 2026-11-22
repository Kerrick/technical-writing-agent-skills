---
status: accepted
date: 2026-01-20
deciders: Mira Okafor (maintainer), Jun Akiyama
---

# Quantities are stored as integers in a base unit, and converted only for display

## Context and Problem Statement

Users type quantities as they read them on a package: `500g`, `1.5kg`, `2 l`, `3` (a count). `larder low` compares what is left with a threshold, and `larder use` subtracts. What does the database hold?

## Decision Drivers

* Subtracting many small uses must not drift.
* A threshold typed in one unit must compare with stock typed in another.

## Considered Options

1. An integer count of a base unit per kind of quantity (milligrams, millilitres, pieces)
2. The number and the unit as typed
3. A floating-point number of grams or litres

## Decision Outcome

Chosen: option 1, because integer arithmetic does not drift, and one base unit per kind makes every comparison a comparison of two integers. Option 2 lost because every comparison would convert first. Option 3 lost because 0.1 kg used ten times did not come to 1 kg in the spike. The units larder accepts and how it prints them are in [docs/design/cli-output.md](../design/cli-output.md).

Confidence: high; `tests/test_quantities.py` subtracts ten thousand random uses and compares the total exactly.

### Consequences

* Good, because totals are exact.
* Bad, because a quantity below one milligram or one millilitre cannot be stored.
* Bad, because changing a base unit would mean rewriting every stored quantity in every user's file.

### Confirmation

`tests/test_quantities.py` fails if any column that holds a quantity is not an integer.
