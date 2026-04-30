#!/usr/bin/env python3
"""Compact a trace report: drop [no-change] lines, collapse internal stars.

Reads a trace report produced by oe_full_trace_report.py or
oe_derivation_class_trace_report.py and:
  1. Drops every stage line tagged ``[no-change]``.
  2. Rewrites starred forms so only the leading star survives, e.g.
     ``*n*ḗ*d*r*ō*n`` → ``*nḗdrōn``.

Pure post-processing: takes a report path in, writes a new report out.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List

# Match a starred form: a leading `*`, followed by one or more star-segmented
# characters (each an optional `*` plus exactly one printable non-space char).
# Internal `*`s between characters are collapsed; the leading `*` is kept.
STARRED_FORM_RE = re.compile(r"\*(?:\*?[^\s*,])+")


def collapse_stars(token: str) -> str:
    # Token starts with `*`. Strip every other `*` after the first char.
    return "*" + token[1:].replace("*", "")


def compact_line(line: str) -> str:
    return STARRED_FORM_RE.sub(lambda m: collapse_stars(m.group(0)), line)


def compact_report(text: str) -> str:
    filtered = []
    for line in text.splitlines():
        if "[no-change]" in line:
            continue
        filtered.append(compact_line(line))

    # If a section header has no stage lines beneath it (all were dropped),
    # insert "[no change]" so empty sections are visible.
    out_lines: List[str] = []
    i = 0
    while i < len(filtered):
        line = filtered[i]
        out_lines.append(line)
        if line.startswith("## "):
            # Look ahead past blank lines to see if any content follows before
            # the next section/lexeme/bucket boundary.
            j = i + 1
            while j < len(filtered) and filtered[j] == "":
                j += 1
            terminates = (
                j >= len(filtered)
                or filtered[j].startswith("## ")
                or filtered[j].startswith("--- ")
                or filtered[j].startswith("=== ")
            )
            if terminates:
                out_lines.append("")
                out_lines.append("[no change]")
        i += 1
    return "\n".join(out_lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Trace report to compact")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output path (default: <input>.compact.txt)",
    )
    args = parser.parse_args()

    in_path: Path = args.input.expanduser().resolve()
    out_path: Path = (
        args.output.expanduser().resolve()
        if args.output
        else in_path.with_suffix(".compact.txt")
    )
    text = in_path.read_text(encoding="utf-8")
    out_path.write_text(compact_report(text), encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
