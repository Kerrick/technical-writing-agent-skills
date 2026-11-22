# Command-line output

Everything larder prints goes through `say()` in `src/larder/ui.py`. Code elsewhere never calls `print()` directly.

## Units

larder accepts `mg`, `g`, `kg`, `ml`, `l`, and a bare number for a count. It stores each quantity in its base unit (ADR 0006) and prints it in the largest unit that leaves no fraction beyond one decimal place: `1.5 kg`, not `1500 g`.

A unit is always printed abbreviated: `g`, `kg`, `ml`, `l`, and `mg`. It is never spelled out, so larder prints `2 l`, not `2 litres`.

## Colour

`larder low` prints an item in red when stock is zero, and in yellow when it is under the threshold. Colour is off when the output is not a terminal, or when `NO_COLOR` is set.
