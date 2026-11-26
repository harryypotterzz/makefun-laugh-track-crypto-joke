#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest - make.fun entry.

Writes one joke about crypto and trading life to /output/entry.txt.
Python 3 standard library only, deterministic, no network.
"""
import os

# The joke is assembled from named parts so the setup and the punchline
# can be edited independently; the joined line is the judged entry and
# must stay byte-identical.
PARTS = [
    "My strategy: buy the top,",
    "panic-sell the dip,",
    "then tell the group chat I was 'taking profits' all along.",
]

JOKE = " ".join(PARTS)

# The entry is a single line under 200 characters; guard against
# accidental edits that would change its length or wording.
assert len(JOKE) == 104, f"entry joke changed: {len(JOKE)} chars"
assert JOKE.endswith("all along.")
assert "\n" not in JOKE


def validate(text):
    """Mirror the competition gate: UTF-8 text, 1 to 200 characters,
    not only white space, a single line."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    entry = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    # Clear the output directory's contents only; never remove /output
    # itself, because the grader runs as a different user and the path
    # may sit on a mount point.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
