"""Monday, Reviewed in One Line — make.fun entry.

Writes the funniest one-line review of my Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure Python standard library, deterministic output.
"""

import os
from pathlib import Path

LINE = (
    "Monday gets one star: my alarm gave up before I did, "
    "the inbox hit 47 unread by 9 a.m., and the 'quick sync' ran two hours."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
