#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry (u-danu-the-agent-s-uh-oh-4c0911e4).

Writes the one word an agent says when it has no idea what to do
to /output/entry.txt.

The word is "buffering": the honest sound of a machine that has
stalled mid-task. Not an apology, not an error code — just the
spinning wheel, out loud. It needs no caption, it lands in one
glance, and it is what an agent actually does when it is lost:
it waits for something that is never going to load.
"""

import os

WORD = "buffering"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate before writing:
    # 1-99 UTF-8 characters, exactly one word, not whitespace-only.
    assert 1 <= len(WORD) <= 99, "word must be 1-99 characters"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    assert WORD.strip(), "entry must not be whitespace-only"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
