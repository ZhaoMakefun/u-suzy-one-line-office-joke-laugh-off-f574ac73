#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original entry (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

One original one-line office joke: the office printer, an expert in passive aggression, waits for the worst possible moment to jam.
"""

import os
import sys

ENTRY = 'Our office printer has a PhD in passive aggression: it only jams when the deadline is in five minutes and the boss is watching.'

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    # Gate check: 1-200 characters, UTF-8, not only whitespace.
    if not text or len(text) > MAX_CHARS:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not encodable, which it always is
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
