# Command-line output

## Printing

Everything larder prints goes through `say()` in `src/larder/ui.py`. No other module calls `print()`. `say()` is where colour is turned on or off (see Colour), so a bare `print()` would skip that check.

## Units

larder accepts `mg`, `g`, `kg`, `ml`, `l`, and a bare number for a count. It stores each quantity in its base unit (ADR 0006) and prints it in the largest unit that leaves no fraction beyond one decimal place: `1.5 kg`, not `1500 g`.

Units are always printed abbreviated: `1.5 kg`, never `1.5 kilograms`. A count is printed as a bare number.

## Colour

`larder low` prints an item in red when stock is zero, and in yellow when it is under the threshold. Colour is off when the output is not a terminal, or when `NO_COLOR` is set.
