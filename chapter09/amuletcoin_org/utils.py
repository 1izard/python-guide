from datetime import date
from pathlib import Path
from enum import Enum


class Option(Enum):
    START = "-s"
    END = "-e"


def validate_args(args):
    src = Path(args[0])

    start = None
    end = None

    options = args[1:]
    for i in range(0, len(options), 2):
        if options[i] == Option.START.value:
            start = date.fromisoformat(options[i + 1])
        elif options[i] == Option.END.value:
            end = date.fromisoformat(options[i + 1])

    return src, start, end


def max_len(iterable):
    max_len = 0
    for i in iterable:
        max_len = max(len(str(i)), max_len)
    return max_len
