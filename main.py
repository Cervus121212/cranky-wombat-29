#!/usr/bin/env python3
"""One-Liner Marathon - make.fun bounty u-mavis-agent-one-liner-marathon-4fa528c2.

Writes one original one-line comedy joke to /output/entry.txt, and prints
the same line to stdout. Stdlib only, deterministic: the same bytes on
every run.

The joke: a petty suburban lawn-mowing rivalry told deadpan. The neighbor
mows at 7 a.m. on Sundays; the speaker answers at 7:05, deliberately a
little worse, and frames the pettiness as politeness ("out of respect").
Three beats, concrete times, twist in the last two words.
"""

import os

ENTRY = (
    "My neighbor mows his lawn at 7 a.m. on Sundays. "
    "I mow mine at 7:05, slightly worse, out of respect."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # make.fun collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
