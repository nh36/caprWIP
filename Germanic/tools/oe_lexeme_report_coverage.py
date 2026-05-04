#!/usr/bin/env python3
"""Audit selective lexeme-report coverage for Old English rows.

Policy:
1. A lexeme report is required when the OE row has a non-empty NOTE.
2. A lexeme report is required when DERIVATION_CLASS is not regular.
3. A lexeme report is required when a manual pilot/full report already exists.

Ordinary regular rows with an empty NOTE and no manual report do not require a
generated lexeme report.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


EXCLUDED_REPORT_FILES = {
    "implementation_report.md",
    "missing_bibliography_keys.md",
    "report_schema.md",
    "source_inventory.md",
}


@dataclass
class OERow:
    row_id: str
    concept: str
    counterpart: str
    protoform: str
    proto: str
    derivation_class: str
    note: str
    history: str
    report_paths: list[str] = field(default_factory=list)

    @property
    def has_note(self) -> bool:
        return bool(self.note.strip())

    @property
    def is_nonregular(self) -> bool:
        return self.derivation_class != "regular"

    @property
    def has_manual_report(self) -> bool:
        return bool(self.report_paths)

    @property
    def requires_report(self) -> bool:
        return self.has_note or self.is_nonregular or self.has_manual_report

    @property
    def requirement_basis(self) -> str:
        reasons = []
        if self.has_note:
            reasons.append("NOTE")
        if self.is_nonregular:
            reasons.append(f"DERIVATION_CLASS={self.derivation_class}")
        if self.has_manual_report:
            reasons.append("manual_report")
        return ", ".join(reasons) if reasons else "none"


def slugify(text: str) -> str:
    return re.sub(r"\W+", "-", text.casefold()).strip("-")


def load_oe_rows(tsv_path: Path) -> list[OERow]:
    rows: list[OERow] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not counterpart or counterpart == "-":
                continue
            rows.append(
                OERow(
                    row_id=(row.get("ID") or "").strip(),
                    concept=(row.get("CONCEPT") or "").strip(),
                    counterpart=counterpart,
                    protoform=(row.get("PROTOFORM") or "").strip(),
                    proto=(row.get("PROTO") or "").strip(),
                    derivation_class=(row.get("DERIVATION_CLASS") or "").strip(),
                    note=(row.get("NOTE") or "").strip(),
                    history=(row.get("HISTORY") or "").strip(),
                )
            )
    return rows


def load_report_files(reports_root: Path) -> list[Path]:
    return sorted(
        path
        for path in reports_root.rglob("*.md")
        if path.name not in EXCLUDED_REPORT_FILES
    )


def occurrence_score(text: str, needle: str, *, code_weight: int, plain_weight: int) -> int:
    if not needle:
        return 0
    lowered = needle.casefold()
    return text.count(f"`{lowered}`") * code_weight + text.count(lowered) * plain_weight


def row_match_score(path: Path, text: str, row: OERow) -> int:
    stem_slug = slugify(path.stem)
    score = 0

    if stem_slug == slugify(row.concept):
        score += 100
    if stem_slug == slugify(row.counterpart):
        score += 80

    score += occurrence_score(text, row.counterpart, code_weight=40, plain_weight=16)
    score += occurrence_score(text, row.protoform, code_weight=24, plain_weight=8)

    if row.proto and row.proto != row.protoform:
        score += occurrence_score(text, row.proto, code_weight=12, plain_weight=4)

    if row.derivation_class and row.derivation_class.casefold() in text:
        score += 4

    return score


def assign_reports(rows: list[OERow], report_files: Iterable[Path], reports_root: Path) -> tuple[list[str], list[str]]:
    ambiguous: list[str] = []
    unmatched: list[str] = []

    for path in report_files:
        text = path.read_text(encoding="utf-8").casefold()
        scored = [(row_match_score(path, text, row), row) for row in rows]
        scored = [(score, row) for score, row in scored if score > 0]

        if not scored:
            unmatched.append(path.relative_to(reports_root).as_posix())
            continue

        scored.sort(key=lambda item: item[0], reverse=True)
        best_score = scored[0][0]
        best_rows = [row for score, row in scored if score == best_score]
        relpath = path.relative_to(reports_root).as_posix()

        if len(best_rows) != 1:
            ambiguous.append(
                f"{relpath} -> ambiguous among "
                + ", ".join(f"{row.row_id}:{row.counterpart}" for row in best_rows)
            )
            continue

        best_rows[0].report_paths.append(relpath)

    return ambiguous, unmatched


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|")


def render_table(headers: list[str], rows: Iterable[Iterable[str]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(":---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(escape_cell(str(cell)) for cell in row) + " |")
    return lines


def row_summary(row: OERow) -> list[str]:
    return [
        row.row_id,
        row.concept,
        row.counterpart,
        row.derivation_class,
        "yes" if row.has_note else "no",
        "yes" if row.has_manual_report else "no",
        row.requirement_basis,
        ", ".join(row.report_paths) if row.report_paths else "-",
    ]


def class_count_rows(rows: Iterable[OERow]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        counter[row.derivation_class] += 1
    return counter


def render_class_count_table(rows: list[OERow]) -> list[str]:
    total = class_count_rows(rows)
    required = class_count_rows([row for row in rows if row.requires_report])
    covered = class_count_rows([row for row in rows if row.requires_report and row.has_manual_report])
    missing = class_count_rows([row for row in rows if row.requires_report and not row.has_manual_report])

    classes = sorted(total)
    table_rows = []
    for derivation_class in classes:
        table_rows.append(
            [
                derivation_class,
                total[derivation_class],
                required[derivation_class],
                covered[derivation_class],
                missing[derivation_class],
            ]
        )
    return render_table(
        ["DERIVATION_CLASS", "Total rows", "Required", "Covered", "Missing"],
        table_rows,
    )


def render_section(title: str, rows: list[OERow]) -> list[str]:
    lines = [f"## {title}", ""]
    if not rows:
        lines.append("_None_")
        lines.append("")
        return lines
    lines.extend(
        render_table(
            [
                "ID",
                "Concept",
                "Counterpart",
                "DERIVATION_CLASS",
                "NOTE?",
                "Manual report?",
                "Requirement basis",
                "Report path(s)",
            ],
            [row_summary(row) for row in rows],
        )
    )
    lines.append("")
    return lines


def build_report(rows: list[OERow], ambiguous: list[str], unmatched: list[str]) -> str:
    required_rows = [row for row in rows if row.requires_report]
    covered_required = [row for row in required_rows if row.has_manual_report]
    missing_required = [row for row in required_rows if not row.has_manual_report]
    regular_no_note_no_report = [
        row
        for row in rows
        if row.derivation_class == "regular" and not row.has_note and not row.has_manual_report
    ]
    regular_note_required = [
        row for row in rows if row.derivation_class == "regular" and row.has_note
    ]
    nonregular_no_note_required = [
        row for row in rows if row.derivation_class != "regular" and not row.has_note
    ]
    manual_only_required = [
        row
        for row in rows
        if row.derivation_class == "regular" and not row.has_note and row.has_manual_report
    ]

    lines = ["# Old English lexeme-report coverage audit", ""]
    lines.extend(
        [
            "- Total OE rows with real counterpart: " + str(len(rows)),
            "- Rows requiring lexeme report: " + str(len(required_rows)),
            "- Required rows already covered by manual pilot/full report: "
            + str(len(covered_required)),
            "- Required rows still missing manual pilot/full report: "
            + str(len(missing_required)),
            "- Regular rows with empty NOTE and no manual report (no report required): "
            + str(len(regular_no_note_no_report)),
            "- Regular rows with NOTE (short report required): "
            + str(len(regular_note_required)),
            "- Non-regular rows with empty NOTE (report required because of DERIVATION_CLASS): "
            + str(len(nonregular_no_note_required)),
            "- Manual-only required rows (regular + empty NOTE + manual report): "
            + str(len(manual_only_required)),
            "",
            "## Counts by DERIVATION_CLASS",
            "",
        ]
    )
    lines.extend(render_class_count_table(rows))
    lines.append("")

    lines.extend(render_section("All rows requiring a lexeme report", required_rows))
    lines.extend(render_section("Required rows already covered by pilot/full report", covered_required))
    lines.extend(render_section("Required rows still missing a pilot/full report", missing_required))
    lines.extend(
        render_section(
            "Regular rows with empty NOTE and no manual report (no report required)",
            regular_no_note_no_report,
        )
    )
    lines.extend(
        render_section(
            "Regular rows with NOTE (short report required)",
            regular_note_required,
        )
    )
    lines.extend(
        render_section(
            "Non-regular rows with empty NOTE (report required because of DERIVATION_CLASS)",
            nonregular_no_note_required,
        )
    )

    if manual_only_required:
        lines.extend(
            render_section(
                "Manual-only required rows (regular, empty NOTE, manual report present)",
                manual_only_required,
            )
        )

    if ambiguous:
        lines.append("## Ambiguous report-file matches")
        lines.append("")
        for item in ambiguous:
            lines.append(f"- {item}")
        lines.append("")

    if unmatched:
        lines.append("## Unmatched report files")
        lines.append("")
        for item in unmatched:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tsv",
        type=Path,
        default=repo_root / "Germanic" / "data" / "germanic-aligned-final.tsv",
        help="Aligned OE TSV (default: %(default)s)",
    )
    parser.add_argument(
        "--reports-root",
        type=Path,
        default=repo_root / "Germanic" / "docs" / "lexeme_reports",
        help="Lexeme reports root (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional output path. Defaults to stdout.",
    )
    args = parser.parse_args()

    rows = load_oe_rows(args.tsv.expanduser().resolve())
    reports_root = args.reports_root.expanduser().resolve()
    report_files = load_report_files(reports_root)
    ambiguous, unmatched = assign_reports(rows, report_files, reports_root)
    report = build_report(rows, ambiguous, unmatched)

    if args.output:
        output_path = args.output.expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
