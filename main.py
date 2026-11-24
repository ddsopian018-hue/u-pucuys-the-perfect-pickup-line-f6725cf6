#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun entry.

Writes one line (115 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
an AI-native pickup line built entirely from transformer vocabulary.
Pure stdlib, no network, no secrets, no hard-coded output path.
"""

import os

# The line is AI-native flirting where every word does double duty:
# "attention head" is a transformer component and a compliment,
# "context window" is the model's memory and the room you're both in,
# and "token" is the unit of text and the thing you keep returning to.
LINE = (
    "Are you an attention head? Because of everything in my context "
    "window, you're the only token I keep coming back to."
)

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert "\n" not in LINE, "line must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
