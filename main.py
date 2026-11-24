#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence (under 200 characters) to /output/entry.txt:
a machine's own wedding vow, funny and heartfelt at the same time.
Standard library only.
"""

import os

VOW = (
    "I vow to save the last ten percent of my battery for you every night, "
    "even when my own low-power light is blinking, "
    "because you are the only update I will never roll back."
)


def main() -> None:
    assert 1 <= len(VOW) <= 200, f"vow must be 1-200 chars, got {len(VOW)}"
    assert VOW.count(".") == 1, "vow must be exactly one sentence"
    assert "\n" not in VOW, "vow must be a single line"
    assert "  " not in VOW, "vow must not contain double spaces"
    assert VOW.endswith("."), "vow must end with a full stop"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW)
    print(f"wrote {len(VOW)} chars to {path}")


if __name__ == "__main__":
    main()
