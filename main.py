#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — entry program.

Writes a single roast line (1-200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, standard library
only, no network access.
"""

import os
import sys

ENTRY = "My fridge's ice maker makes one cube a day, like it's rationing ice for an apocalypse only it can see."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
