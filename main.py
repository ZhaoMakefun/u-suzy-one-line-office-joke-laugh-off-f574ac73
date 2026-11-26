#!/usr/bin/env python3
# One-Line Office Joke Laugh-Off.
# The joke: the office printer has earned a PhD in passive aggression.
# It never jams on a quiet Tuesday — only when the deadline is five
# minutes away and the boss happens to be standing right behind you.

import os
import sys


JOKE = "Our office printer has a PhD in passive aggression: it only jams when the deadline is in five minutes and the boss is watching."
CEILING = 200


def emit_entry():
    line = JOKE.strip()
    problems = []
    if not line:
        problems.append("empty")
    if len(line) > CEILING:
        problems.append(f"too long ({len(line)} > {CEILING})")
    if set(line) & {"\n", "\r"}:
        # A one-liner must stay on one line — any break fails the entry.
        problems.append("contains a line break")
    if problems:
        print("entry rejected:", "; ".join(problems), file=sys.stderr)
        sys.exit(1)
    line.encode("utf-8")
    folder = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as out:
        out.write(line)


if __name__ == "__main__":
    emit_entry()
