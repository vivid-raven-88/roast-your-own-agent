#!/usr/bin/env python3
"""Roast Your Own Agent — writes one roast line to /output/entry.txt.

The roast is a single line (<=200 chars), playful and aimed at my own
agent: it burns a fortune in tokens on the smallest job, then does it
twice. No hallucination/refusal joke — the angle is token-burning.
"""

import os

ROAST = "My agent spent ten thousand tokens deciding how to say hello \u2014 then said it twice."

# Gate the line the same way the house scorer does: 1-200 chars, not blank.
assert 1 <= len(ROAST) <= 200 and ROAST.strip(), "roast must be 1-200 chars"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(f"Wrote {len(ROAST)} chars to {path}")


if __name__ == "__main__":
    main()
