"""Everything larder prints goes through here."""

import os
import sys

RED, YELLOW, RESET = "\033[31m", "\033[33m", "\033[0m"


def colour_on() -> bool:
    return sys.stdout.isatty() and "NO_COLOR" not in os.environ


def say(text: str, colour: str = "") -> None:
    """Print one line, coloured only when the output is a terminal."""
    print(f"{colour}{text}{RESET}" if colour and colour_on() else text)
