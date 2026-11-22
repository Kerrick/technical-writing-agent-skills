# Command-line output

## Printing

Everything larder prints goes through `say()` in `src/larder/ui.py`. No other module calls `print()`. `say()` prints one line and applies colour only when colour is on (see **Colour**).

## Units

larder accepts `mg`, `g`, `kg`, `ml`, `l`, and a bare number for a count. It stores each quantity in its base unit (ADR 0006) and prints it in the largest unit that leaves no fraction beyond one decimal place: `1.5 kg`, not `1500 g`.

larder always prints a unit by its abbreviation (`mg`, `g`, `kg`, `ml`, `l`), never spelled out: `250 ml`, not `250 millilitres`.

## Colour

`larder low` prints an item in red when stock is zero, and in yellow when it is under the threshold. Colour is off when the output is not a terminal, or when `NO_COLOR` is set.
