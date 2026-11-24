"""The Perfect Pickup Line - make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one pickup line an AI agent could actually say out loud to a person
to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, no network, no absolute paths.
"""

import os

LINE = (
    "Are you an attention head? Because of everything in my context window, "
    "you're the only token I keep coming back to."
)


def main() -> None:
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    line = LINE.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs(output_dir, exist_ok=True)
    # Write exactly the line, no trailing newline: the gate counts every char.
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
