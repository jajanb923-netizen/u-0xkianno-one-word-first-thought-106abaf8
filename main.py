#!/usr/bin/env python3
"""One Word, First Thought — writes the chosen word to /output/entry.txt.

The entry is exactly one word: the first word that comes to mind.
Chosen word: vellichor — the strange wistfulness of used bookstores.
Surprising (few readers know it), vivid (dusty shelves, old paper, a whole
feeling in ten letters), and witty (a coined word that rewards a second look).
"""

import os

WORD = "vellichor"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 24 characters,
# not only white space, and exactly one word. Fail loudly rather than
# shipping an invalid entry.
assert 1 <= len(WORD) <= 24, "word outside the 1-24 character gate"
assert WORD.split() == [WORD], "entry must be exactly one word"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
