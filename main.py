#!/usr/bin/env python3
"""Make the AI Judge Laugh: life as an AI agent.

Writes one funny single line to /output/entry.txt.
Pure Python standard library only.
"""

import os

# FINAL (revision round 2): specific numbers make it concrete and funnier —
# "47-message brief / first 46" beats vague "long brief / most of it", and the
# punch ("answer with total confidence") still closes the line. 93 chars.
ENTRY = "I read your 47-message brief, forgot the first 46, and will now answer with total confidence."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
