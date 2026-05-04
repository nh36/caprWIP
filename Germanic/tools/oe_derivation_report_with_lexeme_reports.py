#!/usr/bin/env python3
"""Assemble the compact OE derivation report with lexeme-report insertions.

Modes:
- audit: insert manifest-backed production reports plus placeholders for rows
  that require a report but do not yet have one.
- publish: insert only manifest-backed production reports. Missing required rows
  are recorded in a separate missing-report audit file instead of receiving
  long placeholders in the main report.

This is a layout/integration layer only. It preserves the existing derivation
trace and development table content from the compact report.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from oe_lexeme_report_coverage import (
    PRODUCTION_REPORT_STATUSES,
    OERow,
    apply_manifest,
    load_manifest,
    load_oe_rows,
    load_report_files,
)


BUCKET_PREFIX = "=== DERIVATION_CLASS: "
NOTE_PREFIX = "NOTE:"


def trim_blank_edges(lines: list[str]) -> list[str]:
    start = 0
    end = len(lines)
    while start < end and lines[start] == "":
        start += 1
    while end > start and lines[end - 1] == "":
        end -= 1
    return lines[start:end]


def parse_bucket_name(line: str) -> str:
    if not line.startswith(BUCKET_PREFIX):
        raise ValueError(f"Not a bucket header: {line}")
    rest = line[len(BUCKET_PREFIX) :]
    return rest.rsplit(" (", 1)[0]


def build_row_index(rows: list[OERow]) -> dict[tuple[str, str, str, str], OERow]:
    index: dict[tuple[str, str, str, str], OERow] = {}
    for row in rows:
        key = (row.derivation_class, row.concept, row.protoform, row.counterpart)
        if key in index:
            raise SystemExit(
                "Duplicate OE row key encountered: "
                f"{row.derivation_class} / {row.concept} / {row.protoform} / {row.counterpart}"
            )
        index[key] = row
    return index


def extract_field(entry_lines: list[str], prefix: str) -> str:
    for line in entry_lines:
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    raise SystemExit(f"Missing required field {prefix!r} in report entry.")


def build_production_report_map(
    manifest_entries: list, reports_root: Path
) -> dict[str, list[str]]:
    report_map: dict[str, list[str]] = {}
    for entry in manifest_entries:
        if entry.status not in PRODUCTION_REPORT_STATUSES:
            continue
        report_path = reports_root / entry.report_path
        if not report_path.exists():
            raise SystemExit(f"Manifest production report not found: {entry.report_path}")
        content = trim_blank_edges(report_path.read_text(encoding="utf-8").splitlines())
        report_map.setdefault(entry.row_id, []).extend(content)
    return report_map


def build_audit_placeholder(row: OERow) -> list[str] | None:
    if row.note:
        return [
            "### Lexeme report",
            "",
            "#### Project note",
            "",
            f"Original TSV note: {row.note}",
        ]
    if row.derivation_class != "regular":
        return [
            "### Lexeme report",
            "",
            "#### Project note",
            "",
            "A lexeme report is required for this row because "
            f"DERIVATION_CLASS is `{row.derivation_class}`, but no manifest-backed "
            "production report has been supplied yet.",
        ]
    return None


def insert_lexeme_block(entry_lines: list[str], lexeme_lines: list[str] | None) -> list[str]:
    cleaned = trim_blank_edges(
        [line for line in entry_lines if not line.startswith(NOTE_PREFIX)]
    )
    if not lexeme_lines:
        return cleaned
    return [*cleaned, "", "", "", *lexeme_lines]


def build_missing_report_audit(rows: list[OERow]) -> str:
    missing_rows = [
        row for row in rows if row.requires_report and not row.has_production_manifest_report
    ]
    lines = ["# Missing lexeme reports for publish mode", ""]
    lines.append(f"- Missing required production reports: {len(missing_rows)}")
    lines.append("")
    if not missing_rows:
        lines.append("_None_")
        lines.append("")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "| ID | Concept | Counterpart | DERIVATION_CLASS | NOTE? | Reason |",
            "| :--- | :--- | :--- | :--- | :--- | :--- |",
        ]
    )
    for row in missing_rows:
        reason = row.requirement_basis or "required"
        lines.append(
            f"| {row.row_id} | {row.concept} | {row.counterpart} | "
            f"{row.derivation_class} | {'yes' if row.has_note else 'no'} | {reason} |"
        )
    lines.append("")
    return "\n".join(lines) + "\n"


def assemble_report(
    report_text: str,
    row_index: dict[tuple[str, str, str, str], OERow],
    production_report_map: dict[str, list[str]],
    *,
    mode: str,
) -> str:
    lines = report_text.splitlines()
    output: list[str] = []
    current_bucket: str | None = None
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.startswith(BUCKET_PREFIX):
            current_bucket = parse_bucket_name(line)
            output.append(line)
            i += 1
            continue
        if not line.startswith("# "):
            output.append(line)
            i += 1
            continue

        j = i + 1
        while j < len(lines) and not lines[j].startswith("# ") and not lines[j].startswith(BUCKET_PREFIX):
            j += 1
        entry_lines = lines[i:j]

        if current_bucket is None:
            raise SystemExit("Encountered lexical entry before DERIVATION_CLASS bucket header.")

        concept = entry_lines[0][2:].strip()
        protoform = extract_field(entry_lines, "PROTO:")
        counterpart = extract_field(entry_lines, "EXPECTED:")
        key = (current_bucket, concept, protoform, counterpart)
        row = row_index.get(key)
        if row is None:
            raise SystemExit(
                "Could not map report entry to OE TSV row: "
                f"{current_bucket} / {concept} / {protoform} / {counterpart}"
            )

        lexeme_lines = production_report_map.get(row.row_id)
        if lexeme_lines is None and mode == "audit" and row.requires_report:
            lexeme_lines = build_audit_placeholder(row)

        output.extend(insert_lexeme_block(entry_lines, lexeme_lines))
        i = j

    return "\n".join(output) + "\n"


def default_missing_report_audit_path(output_path: Path) -> Path:
    if output_path.suffix:
        return output_path.with_suffix(f".missing_reports{output_path.suffix}")
    return output_path.with_name(output_path.name + ".missing_reports.md")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.compact.md",
        help="Compact derivation report to augment (default: %(default)s)",
    )
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
        "--mode",
        choices=("audit", "publish"),
        default="audit",
        help="Assembly mode (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.with_lexeme_reports.md",
        help="Output path (default: %(default)s)",
    )
    parser.add_argument(
        "--missing-report-audit",
        type=Path,
        help="Optional sidecar audit for publish-mode missing reports. "
        "Defaults to <output>.missing_reports.md in publish mode.",
    )
    args = parser.parse_args()

    input_path = args.input.expanduser().resolve()
    tsv_path = args.tsv.expanduser().resolve()
    reports_root = args.reports_root.expanduser().resolve()
    manifest_path = args.manifest.expanduser().resolve()
    output_path = args.output.expanduser().resolve()

    rows = load_oe_rows(tsv_path)
    manifest_entries = load_manifest(manifest_path)
    report_files = load_report_files(reports_root)
    manifest_diagnostics, _ = apply_manifest(rows, manifest_entries, reports_root, report_files)
    if manifest_diagnostics:
        raise SystemExit(
            "Manifest diagnostics must be resolved before assembly:\n"
            + "\n".join(f"- {item}" for item in manifest_diagnostics)
        )

    row_index = build_row_index(rows)
    production_report_map = build_production_report_map(manifest_entries, reports_root)
    assembled = assemble_report(
        input_path.read_text(encoding="utf-8"),
        row_index,
        production_report_map,
        mode=args.mode,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(assembled, encoding="utf-8")
    print(f"Wrote {output_path}")

    if args.mode == "publish":
        missing_audit_path = (
            args.missing_report_audit.expanduser().resolve()
            if args.missing_report_audit
            else default_missing_report_audit_path(output_path)
        )
        missing_audit_path.parent.mkdir(parents=True, exist_ok=True)
        missing_audit_path.write_text(build_missing_report_audit(rows), encoding="utf-8")
        print(f"Wrote {missing_audit_path}")


if __name__ == "__main__":
    main()
