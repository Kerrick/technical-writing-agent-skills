# Command-line output

## Units

larder accepts `mg`, `g`, `kg`, `ml`, `l`, and a bare number for a count. It stores each quantity in its base unit (ADR 0006) and prints it in the largest unit that leaves no fraction beyond one decimal place: `1.5 kg`, not `1500 g`.

## Colour

`larder low` prints an item in red when stock is zero, and in yellow when it is under the threshold. Colour is off when the output is not a terminal, or when `NO_COLOR` is set.
