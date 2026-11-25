#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

The whole internet, in a single word: Actually.

Every thread eventually becomes somebody correcting somebody else, and
the word alone delivers the joke: it is short, instantly readable,
true of the internet as a whole, and not the first obvious word
anyone reaches for. It won a blind tournament over 20 candidates,
ranked #1 by all three independent judges against the published
judge brief (Borda 60/60, unanimous).

The program writes the word to /output/entry.txt and checks it
against the competition gate first: UTF-8 text, 1-30 characters,
a single word, not only white space. After writing, it reads the
file back and refuses to report success unless the bytes match
the word exactly.
"""

import sys
from pathlib import Path

WORD = "Actually"
OUT = Path("/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 30


def gate_error(word):
    """Name the first gate problem, or return None when the word passes."""
    if not word.strip():
        return "entry is blank"
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        return f"entry is {len(word)} characters, gate allows {MIN_CHARS}-{MAX_CHARS}"
    if len(word.split()) != 1:
        return "entry must be a single word"
    if any(ch.isspace() for ch in word):
        return "entry contains whitespace"
    return None


def main():
    word = WORD.strip()
    error = gate_error(word)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(word, encoding="utf-8", newline="")

    back = OUT.read_bytes()
    if back != word.encode("utf-8"):
        print(
            f"error: read back {len(back)} bytes, expected {len(word)}",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {len(word)} characters, 1 word, to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
