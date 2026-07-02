#!/usr/bin/env python3
"""Legacy helper superseded by index_verborum_filter.lua in the combined book build."""
from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FORMS = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"


@dataclass
class IndexRow:
    language: str
    form: str
    display: str
    sort_key: str
    regex: re.Pattern[str]
    command: str


def latex_index_value(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


def load_rows(path: Path) -> list[IndexRow]:
    rows: list[IndexRow] = []
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            language = (row.get("language") or "").strip()
            status = (row.get("status") or "").strip()
            if not language or status in {"unassigned", "ambiguous", "ignore"}:
                continue
            display = (row.get("display") or row.get("form") or "").strip()
            sort_key = (row.get("sort_key") or display).strip()
            command = rf"\index[{language}]{{{latex_index_value(sort_key)}@{latex_index_value(display)}}}"
            rows.append(
                IndexRow(
                    language=language,
                    form=(row.get("form") or "").strip(),
                    display=display,
                    sort_key=sort_key,
                    regex=re.compile((row.get("regex") or re.escape(display)).strip()),
                    command=command,
                )
            )
    return sorted(rows, key=lambda row: len(row.form), reverse=True)


def index_text(text: str, rows: list[IndexRow]) -> str:
    output: list[str] = []
    in_fence = False
    in_raw_box = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            output.append(line)
            continue
        if stripped == r"\begingroup":
            in_raw_box = True
            output.append(line)
            continue
        if stripped == r"\endgroup":
            in_raw_box = False
            output.append(line)
            continue
        if in_fence or in_raw_box:
            output.append(line)
            continue
        indexed = line
        for row in rows:
            if row.command in indexed:
                continue
            indexed = row.regex.sub(lambda match: match.group(0) + row.command, indexed, count=1)
        output.append(indexed)
    return "\n".join(output) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--forms", type=Path, default=DEFAULT_FORMS)
    args = parser.parse_args()
    rows = load_rows(args.forms.expanduser().resolve())
    text = args.input.expanduser().resolve().read_text(encoding="utf-8")
    args.output.expanduser().resolve().write_text(index_text(text, rows), encoding="utf-8")


if __name__ == "__main__":
    main()
