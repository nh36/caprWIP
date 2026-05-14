#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

import build_full_lexical_volume as full


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
PILOT_MANIFEST_PATH = SCRIPT_DIR / "regular_compression_pilot_manifest.tsv"
TRACE_REPORT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"
BOOK_PROSE_DIR = SCRIPT_DIR / "book_prose" / "regular_pilot_03"
OUTPUT_PATH = SCRIPT_DIR / "regular_prose_pilot_03.md"


def prose_path_for(row: dict[str, str]) -> Path:
    entry_name = Path(row["model_entry_path"]).name
    return BOOK_PROSE_DIR / entry_name.replace(".model.md", ".book.md")


def build_entry(row: dict[str, str], trace_entries: list[dict[str, str]]) -> str:
    entry_path = REPO_ROOT / row["model_entry_path"]
    model = full.parse_model_entry(entry_path)
    trace_entry, basis, confident = full.match_trace_entry(model, trace_entries)
    if trace_entry is None or not confident:
        raise ValueError(f"trace match unresolved for {entry_path.name} ({basis})")

    prose_path = prose_path_for(row)
    if not prose_path.exists():
        raise FileNotFoundError(f"missing book prose file: {prose_path}")

    print(
        f"Matched {entry_path.name} -> {trace_entry['title']} / {trace_entry['proto']} / {trace_entry['outputs']} ({basis})",
        file=sys.stderr,
    )

    body = prose_path.read_text(encoding="utf-8").strip()
    lines = [
        f"## {model['title']}",
        "",
        full.derivation_summary(model, trace_entry),
        "",
        *full.render_trace_table(trace_entry),
    ]
    if body:
        lines.extend(["", body])
    return "\n".join(lines).strip()


def main() -> int:
    trace_entries = full.parse_trace_entries(TRACE_REPORT_PATH.read_text(encoding="utf-8"))
    with PILOT_MANIFEST_PATH.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    parts = [
        "# Regular-entry prose pilot 03",
        "",
        "_Assembly-only pilot for revised compact regular-entry commentary in a more direct factual style. Trace rendering is reused, and the commentary is supplied from a separate book-prose layer._",
        "",
    ]

    for row in rows:
        parts.extend(["", build_entry(row, trace_entries)])

    parts.extend(["", r"\clearpage", "", "## References", ""])
    OUTPUT_PATH.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
