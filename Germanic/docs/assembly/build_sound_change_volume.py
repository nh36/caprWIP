#!/usr/bin/env python3
from __future__ import annotations

import csv
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
REPORTS_DIR = REPO_ROOT / "Germanic/docs/sound_changes/change_reports"
MANIFEST_PATH = REPORTS_DIR / "report_manifest.tsv"


def env_path(name: str) -> Path | None:
    raw = os.environ.get(name)
    if not raw:
        return None
    path = Path(raw)
    return path if path.is_absolute() else SCRIPT_DIR / path


OUTPUT_PATH = env_path("SOUND_CHANGE_VOLUME_OUTPUT_MD") or (SCRIPT_DIR / "sound_change_volume_alpha_01.md")
ALLOWED_STATUSES = {"pilot", "full"}


def load_manifest_rows() -> list[dict[str, str]]:
    with MANIFEST_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = [row for row in reader if (row.get("STATUS") or "").strip() in ALLOWED_STATUSES]
    if not rows:
        raise ValueError(f"No pilot/full rows found in {MANIFEST_PATH}")
    return rows


def normalize_entry_markdown(title: str, text: str) -> str:
    stripped = text.lstrip()
    lines = stripped.splitlines()
    if lines and lines[0].startswith("# "):
        body = "\n".join(lines[1:]).lstrip()
        return f"## {title}\n\n{body}".rstrip()
    return f"## {title}\n\n{stripped}".rstrip()


def build_volume_text(rows: list[dict[str, str]]) -> str:
    parts: list[str] = [
        "# Sound-change reports, alpha 01",
        "",
        "_Generated from `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`. "
        "This assembly includes only manifest-backed `pilot` and `full` production reports._",
        "",
    ]

    for row in rows:
        title = (row.get("TITLE") or "").strip()
        report_path = (row.get("REPORT_PATH") or "").strip()
        if not title:
            raise ValueError(f"Manifest row is missing TITLE: {row}")
        if not report_path:
            raise ValueError(f"Manifest row is missing REPORT_PATH: {row}")

        source_path = REPORTS_DIR / report_path
        if not source_path.exists():
            raise FileNotFoundError(f"Report file not found: {source_path}")

        entry_text = source_path.read_text(encoding="utf-8")
        parts.append(normalize_entry_markdown(title, entry_text))
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    rows = load_manifest_rows()
    output_text = build_volume_text(rows)
    OUTPUT_PATH.write_text(output_text, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH} with {len(rows)} assembled sound-change report(s).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise
