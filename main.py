#!/usr/bin/env python3
"""One-Liner Groan-Off entry: write the single dad joke to /output/entry.txt.

The entry is one original one-line dad joke, at most 140 characters:
a pun a dad would deliver at the dinner table, with the punchline
landing in the last two words.
"""

import os

ENTRY = (
    "I hired a plumber to fix the sink, then supervised from the couch. "
    "That's what I call a drip campaign."
)


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry has a double space; tighten the wording")
    # The punchline is the last two words; refuse a version where it drifted.
    if not text.endswith("drip campaign."):
        raise ValueError("entry must end on its punchline, 'drip campaign.'")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
