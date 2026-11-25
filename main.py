#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — make.fun entry.

Writes one one-line joke about office life to /output/entry.txt.
Deterministic: the same joke, byte for byte, on every run. No randomness,
no network, no clock, no environment reads — the joke is baked into this file.

The joke — 2-beat + reveal in the final clause (see variants.md in the build
folder for the full pairwise tournament):

    I stayed on mute through the entire 90-minute all-hands. My manager
    Sarah just praised my 'thoughtful silence' in my performance review.

Why this line (judged against the bounty brief in RULES.txt):
  1. Real joke, setup + turn: muted through the all-hands, then the twist —
     the performance review PRAISES the silence.
  2. Universal: mute, all-hands, performance review — every office worker
     knows all three.
  3. Surprise: the reader expects a scolding for saying nothing and gets
     praise for it instead.
  4. One line, punchline last: the review praise is the final clause.
  5. Fresh: the mute angle has 0 entries in the 341-entry field (no printer,
     reply-all, or "meeting about meetings" cliche).
  6. Winner pattern (finalized one-liner bounties): specific number
     (90-minute) + named character (Sarah), 136 bytes.
"""

import os

JOKE = (
    "I stayed on mute through the entire 90-minute all-hands. "
    "My manager Sarah just praised my 'thoughtful silence' "
    "in my performance review."
)


def main() -> None:
    # Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
    # characters, not only whitespace, a single line. Fail loudly instead
    # of shipping an invalid entry.
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit(f"JOKE must be 1-200 characters, got {len(JOKE)}")
    if not JOKE.strip():
        raise SystemExit("JOKE must not be only whitespace")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("JOKE must be a single line")
    JOKE.encode("utf-8")  # gate requires UTF-8 text

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Read-back verification: prove the file the grader reads is
    # byte-identical to JOKE. Fail loudly rather than ship a corrupted
    # or truncated entry.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise SystemExit(
            f"entry.txt verification failed: read back {len(written)} chars, "
            f"expected {len(JOKE)} chars identical to the entry line"
        )
    print(f"wrote {len(JOKE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
