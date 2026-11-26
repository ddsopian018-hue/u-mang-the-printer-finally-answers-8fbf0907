#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes the printer's one-line comeback to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to ./output when the variable is unset).

Pure standard library, no network access. The line is validated before it
is written: non-empty, a single line, 1-240 characters, no surrounding
whitespace.
"""

import os
import sys

# The printer's comeback: one line, 209 characters.
# It leads with the error code and the jam count, then lands the ask.
LINE = (
    "Error E-47, jam #6 before 9 a.m. on a Monday, and you thumped me "
    "like a vending machine. I still printed your 214-page report in "
    "color, double-sided \u2014 so stop feeding me that damp paper from "
    "the supply closet."
)

MAX_CHARS = 240


def main() -> int:
    if not LINE:
        print("error: line is empty", file=sys.stderr)
        return 1
    if LINE != LINE.strip():
        print("error: line has surrounding whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(
            "error: line is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    print("wrote %d characters to %s" % (len(LINE), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
