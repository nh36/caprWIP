#!/usr/bin/env python3
"""Audit selective lexeme-report coverage for Old English rows.

Production policy:
1. A production lexeme report is required when the OE row has a non-empty NOTE.
2. A production lexeme report is required when DERIVATION_CLASS is not regular.
3. A production lexeme report is required when a manifest-backed report has
   STATUS=pilot or STATUS=full.

STATUS=format_test is tracked separately and does not make an otherwise ordinary
regular empty-NOTE row count as requiring a production lexeme report.

Coverage mapping policy:
- The manifest in Germanic/docs/lexeme_reports/report_manifest.tsv is the
  primary source of truth for row-to-report linkage.
- Fuzzy matching is diagnostic only, and is run only for existing report files
  that are not listed in the manifest.
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
    "coverage_audit.md",
    "implementation_report.md",
    "missing_bibliography_keys.md",
    "report_schema.md",
    "source_inventory.md",
}
PRODUCTION_REPORT_STATUSES = {"pilot", "full"}
FORMAT_TEST_REPORT_STATUS = "format_test"


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
    manifest_report_paths: list[str] = field(default_factory=list)
    manifest_statuses: list[str] = field(default_factory=list)
    fuzzy_report_paths: list[str] = field(default_factory=list)

    @property
    def has_note(self) -> bool:
        return bool(self.note.strip())

    @property
    def is_nonregular(self) -> bool:
        return self.derivation_class != "regular"

    @property
    def has_manifest_report(self) -> bool:
        return bool(self.manifest_report_paths)

    @property
    def has_production_manifest_report(self) -> bool:
        return any(status in PRODUCTION_REPORT_STATUSES for status in self.manifest_statuses)

    @property
    def has_format_test_manifest_report(self) -> bool:
        return FORMAT_TEST_REPORT_STATUS in self.manifest_statuses

    @property
    def has_fuzzy_report(self) -> bool:
        return bool(self.fuzzy_report_paths)

    @property
    def has_any_manual_report(self) -> bool:
        return self.has_manifest_report or self.has_fuzzy_report

    @property
    def requires_report(self) -> bool:
        return self.has_note or self.is_nonregular or self.has_production_manifest_report

    @property
    def requirement_basis(self) -> str:
        reasons = []
        if self.has_note:
            reasons.append("NOTE")
        if self.is_nonregular:
            reasons.append(f"DERIVATION_CLASS={self.derivation_class}")
        if self.has_production_manifest_report:
            reasons.append("production_report")
        return ", ".join(reasons) if reasons else "none"

    @property
    def coverage_source(self) -> str:
        if self.has_production_manifest_report:
            return "manifest"
        if self.has_format_test_manifest_report:
            return "manifest_format_test"
        if self.has_fuzzy_report:
            return "fuzzy"
        return "-"

    @property
    def report_paths(self) -> list[str]:
        if self.has_manifest_report:
            return self.manifest_report_paths
        if self.has_fuzzy_report:
            return self.fuzzy_report_paths
        return []

    @property
    def report_status(self) -> str:
        if self.has_manifest_report:
            return ", ".join(self.manifest_statuses)
        return "-"


@dataclass(frozen=True)
class ManifestEntry:
    row_id: str
    concept: str
    counterpart: str
    protoform: str
    derivation_class: str
    report_path: str
    status: str


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


def load_manifest(manifest_path: Path) -> list[ManifestEntry]:
    with manifest_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        expected = [
            "ID",
            "CONCEPT",
            "COUNTERPART",
            "PROTOFORM",
            "DERIVATION_CLASS",
            "REPORT_PATH",
            "STATUS",
        ]
        if reader.fieldnames != expected:
            raise SystemExit(
                "Manifest header mismatch. Expected: " + "\t".join(expected)
            )
        entries: list[ManifestEntry] = []
        for row in reader:
            entries.append(
                ManifestEntry(
                    row_id=(row.get("ID") or "").strip(),
                    concept=(row.get("CONCEPT") or "").strip(),
                    counterpart=(row.get("COUNTERPART") or "").strip(),
                    protoform=(row.get("PROTOFORM") or "").strip(),
                    derivation_class=(row.get("DERIVATION_CLASS") or "").strip(),
                    report_path=(row.get("REPORT_PATH") or "").strip(),
                    status=(row.get("STATUS") or "").strip(),
                )
            )
        return entries


def apply_manifest(
    rows: list[OERow],
    manifest_entries: list[ManifestEntry],
    reports_root: Path,
    report_files: list[Path],
) -> tuple[list[str], set[str]]:
    rows_by_id = {row.row_id: row for row in rows}
    existing_relpaths = {
        path.relative_to(reports_root).as_posix(): path for path in report_files
    }
    seen_paths: set[str] = set()
    diagnostics: list[str] = []
    listed_paths: set[str] = set()

    for entry in manifest_entries:
        if not entry.row_id:
            diagnostics.append(
                f"Manifest entry with report path {entry.report_path or '[empty]'} has empty ID."
            )
            continue
        row = rows_by_id.get(entry.row_id)
        if row is None:
            diagnostics.append(
                f"Manifest row ID {entry.row_id} not found in OE TSV ({entry.report_path})."
            )
            continue

        mismatches = []
        if entry.concept != row.concept:
            mismatches.append(f"CONCEPT manifest={entry.concept} tsv={row.concept}")
        if entry.counterpart != row.counterpart:
            mismatches.append(
                f"COUNTERPART manifest={entry.counterpart} tsv={row.counterpart}"
            )
        if entry.protoform != row.protoform:
            mismatches.append(
                f"PROTOFORM manifest={entry.protoform} tsv={row.protoform}"
            )
        if entry.derivation_class != row.derivation_class:
            mismatches.append(
                "DERIVATION_CLASS "
                f"manifest={entry.derivation_class} tsv={row.derivation_class}"
            )
        if mismatches:
            diagnostics.append(
                f"{entry.report_path} -> row {entry.row_id} metadata mismatch: "
                + "; ".join(mismatches)
            )
            continue

        if not entry.report_path:
            diagnostics.append(f"Manifest row {entry.row_id} has empty REPORT_PATH.")
            continue
        if entry.report_path in seen_paths:
            diagnostics.append(f"Manifest REPORT_PATH duplicated: {entry.report_path}")
            continue
        seen_paths.add(entry.report_path)
        listed_paths.add(entry.report_path)

        if entry.report_path not in existing_relpaths:
            diagnostics.append(
                f"Manifest report path not found on disk: {entry.report_path} (row {entry.row_id})"
            )
            continue

        row.manifest_report_paths.append(entry.report_path)
        row.manifest_statuses.append(entry.status or "-")

    return diagnostics, listed_paths


def occurrence_score(
    text: str, needle: str, *, code_weight: int, plain_weight: int
) -> int:
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


def assign_fuzzy_diagnostics(
    rows: list[OERow], report_files: Iterable[Path], reports_root: Path
) -> tuple[list[str], list[str]]:
    ambiguous: list[str] = []
    unmatched: list[str] = []

    for path in report_files:
        text = path.read_text(encoding="utf-8").casefold()
        scored = [(row_match_score(path, text, row), row) for row in rows]
        scored = [(score, row) for score, row in scored if score > 0]
        relpath = path.relative_to(reports_root).as_posix()

        if not scored:
            unmatched.append(relpath)
            continue

        scored.sort(key=lambda item: item[0], reverse=True)
        best_score = scored[0][0]
        best_rows = [row for score, row in scored if score == best_score]

        if len(best_rows) != 1:
            ambiguous.append(
                f"{relpath} -> ambiguous among "
                + ", ".join(f"{row.row_id}:{row.counterpart}" for row in best_rows)
            )
            continue

        best_rows[0].fuzzy_report_paths.append(relpath)

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
        row.coverage_source,
        row.report_status,
        ", ".join(row.report_paths) if row.report_paths else "-",
        row.requirement_basis,
    ]


def class_count_rows(rows: Iterable[OERow]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        counter[row.derivation_class] += 1
    return counter


def render_class_count_table(rows: list[OERow]) -> list[str]:
    total = class_count_rows(rows)
    required = class_count_rows([row for row in rows if row.requires_report])
    manifest = class_count_rows(
        [row for row in rows if row.requires_report and row.has_production_manifest_report]
    )
    fuzzy_only = class_count_rows(
        [
            row
            for row in rows
            if row.requires_report and not row.has_production_manifest_report and row.has_fuzzy_report
        ]
    )
    no_report = class_count_rows(
        [
            row
            for row in rows
            if row.requires_report
            and not row.has_production_manifest_report
            and not row.has_fuzzy_report
        ]
    )

    classes = sorted(total)
    table_rows = []
    for derivation_class in classes:
        table_rows.append(
            [
                derivation_class,
                total[derivation_class],
                required[derivation_class],
                manifest[derivation_class],
                fuzzy_only[derivation_class],
                no_report[derivation_class],
            ]
        )
    return render_table(
        [
            "DERIVATION_CLASS",
            "Total rows",
            "Required",
            "Manifest-backed",
            "Fuzzy-only",
            "No report",
        ],
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
                "Coverage source",
                "Report status",
                "Report path(s)",
                "Requirement basis",
            ],
            [row_summary(row) for row in rows],
        )
    )
    lines.append("")
    return lines


def build_report(
    rows: list[OERow],
    manifest_entries: list[ManifestEntry],
    manifest_diagnostics: list[str],
    ambiguous: list[str],
    unmatched: list[str],
) -> str:
    required_rows = [row for row in rows if row.requires_report]
    manifest_backed_required = [
        row for row in required_rows if row.has_production_manifest_report
    ]
    fuzzy_only_required = [
        row
        for row in required_rows
        if not row.has_production_manifest_report and row.has_fuzzy_report
    ]
    no_report_required = [
        row
        for row in required_rows
        if not row.has_production_manifest_report and not row.has_fuzzy_report
    ]
    regular_empty_note_no_report_required = [
        row
        for row in rows
        if row.derivation_class == "regular"
        and not row.has_note
        and not row.has_any_manual_report
    ]
    regular_empty_note_manual_present = [
        row
        for row in rows
        if row.derivation_class == "regular"
        and not row.has_note
        and row.has_any_manual_report
    ]
    format_test_rows = [row for row in rows if row.has_format_test_manifest_report]
    regular_note_required = [
        row for row in rows if row.derivation_class == "regular" and row.has_note
    ]
    nonregular_empty_note_required = [
        row for row in rows if row.derivation_class != "regular" and not row.has_note
    ]

    lines = ["# Old English lexeme-report coverage audit", ""]
    lines.extend(
        [
            "- Total OE rows with real counterpart: " + str(len(rows)),
            "- Manifest entries loaded: " + str(len(manifest_entries)),
            "- Rows requiring lexeme report: " + str(len(required_rows)),
            "- Required rows with manifest-backed reports: "
            + str(len(manifest_backed_required)),
            "- Required rows with only fuzzy-matched reports: "
            + str(len(fuzzy_only_required)),
            "- Required rows with no report: " + str(len(no_report_required)),
            "- Regular rows with empty NOTE and no report required: "
            + str(len(regular_empty_note_no_report_required)),
            "- Regular rows with empty NOTE but manual report present: "
            + str(len(regular_empty_note_manual_present)),
            "- Rows with STATUS=format_test reports: " + str(len(format_test_rows)),
            "- Regular rows with NOTE (report required): "
            + str(len(regular_note_required)),
            "- Non-regular rows with empty NOTE (report required because of DERIVATION_CLASS): "
            + str(len(nonregular_empty_note_required)),
            "",
            "## Counts by DERIVATION_CLASS",
            "",
        ]
    )
    lines.extend(render_class_count_table(rows))
    lines.append("")

    lines.extend(
        render_section(
            "Required rows with manifest-backed reports", manifest_backed_required
        )
    )
    lines.extend(
        render_section(
            "Required rows with only fuzzy-matched reports", fuzzy_only_required
        )
    )
    lines.extend(render_section("Required rows with no report", no_report_required))
    lines.extend(
        render_section(
            "Regular rows with empty NOTE and no report required",
            regular_empty_note_no_report_required,
        )
    )
    lines.extend(
        render_section(
            "Regular rows with empty NOTE but manual report present",
            regular_empty_note_manual_present,
        )
    )
    lines.extend(render_section("Rows with STATUS=format_test reports", format_test_rows))

    if manifest_diagnostics:
        lines.append("## Manifest diagnostics")
        lines.append("")
        for item in manifest_diagnostics:
            lines.append(f"- {item}")
        lines.append("")

    lines.append("## Ambiguous report files")
    lines.append("")
    if ambiguous:
        for item in ambiguous:
            lines.append(f"- {item}")
    else:
        lines.append("_None_")
    lines.append("")

    lines.append("## Unmatched report files")
    lines.append("")
    if unmatched:
        for item in unmatched:
            lines.append(f"- {item}")
    else:
        lines.append("_None_")
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
        "--manifest",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "lexeme_reports"
        / "report_manifest.tsv",
        help="Manifest TSV mapping report files to OE rows (default: %(default)s)",
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
    manifest_entries = load_manifest(args.manifest.expanduser().resolve())
    manifest_diagnostics, listed_paths = apply_manifest(
        rows, manifest_entries, reports_root, report_files
    )

    fuzzy_candidate_files = [
        path
        for path in report_files
        if path.relative_to(reports_root).as_posix() not in listed_paths
    ]
    ambiguous, unmatched = assign_fuzzy_diagnostics(
        rows, fuzzy_candidate_files, reports_root
    )
    report = build_report(
        rows, manifest_entries, manifest_diagnostics, ambiguous, unmatched
    )

    if args.output:
        output_path = args.output.expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report + "\n", encoding="utf-8")
        print(f"Wrote {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    main()
