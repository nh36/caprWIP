#!/usr/bin/env python3
"""Validate assembled OE derivation reports with lexeme-report insertions."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from oe_derivation_report_with_lexeme_reports import (
    BUCKET_PREFIX,
    build_production_report_map,
    build_row_index,
    extract_field,
    parse_bucket_name,
    trim_blank_edges,
)
from oe_lexeme_report_coverage import (
    PRODUCTION_REPORT_STATUSES,
    OERow,
    apply_manifest,
    load_manifest,
    load_oe_rows,
    load_report_files,
)


def parse_count(text: str, label: str) -> int:
    match = re.search(rf"^- {re.escape(label)}: (\d+)$", text, re.MULTILINE)
    if not match:
        raise SystemExit(f"Could not find count line for {label!r} in coverage audit.")
    return int(match.group(1))


def parse_entries(
    report_text: str, row_index: dict[tuple[str, str, str, str], OERow]
) -> dict[str, list[str]]:
    lines = report_text.splitlines()
    entries: dict[str, list[str]] = {}
    current_bucket: str | None = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith(BUCKET_PREFIX):
            current_bucket = parse_bucket_name(line)
            i += 1
            continue
        if not line.startswith("# "):
            i += 1
            continue

        j = i + 1
        while j < len(lines) and not lines[j].startswith("# ") and not lines[j].startswith(BUCKET_PREFIX):
            j += 1
        entry_lines = lines[i:j]
        if current_bucket is None:
            raise SystemExit("Encountered entry before bucket header while validating.")
        concept = entry_lines[0][2:].strip()
        protoform = extract_field(entry_lines, "PROTO:")
        counterpart = extract_field(entry_lines, "EXPECTED:")
        key = (current_bucket, concept, protoform, counterpart)
        row = row_index.get(key)
        if row is None:
            raise SystemExit(
                "Could not map assembled entry to OE TSV row while validating: "
                f"{current_bucket} / {concept} / {protoform} / {counterpart}"
            )
        entries[row.row_id] = entry_lines
        i = j
    return entries


def contains_subsequence(lines: list[str], subseq: list[str]) -> bool:
    if not subseq:
        return True
    for start in range(0, len(lines) - len(subseq) + 1):
        if lines[start : start + len(subseq)] == subseq:
            return True
    return False


def is_placeholder(entry_lines: list[str]) -> bool:
    joined = "\n".join(entry_lines)
    return (
        "### Lexeme report" in joined
        and "#### Project note" in joined
        and (
            "Original TSV note:" in joined
            or "A lexeme report is required for this row because" in joined
        )
    )


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tsv",
        type=Path,
        default=repo_root / "Germanic" / "data" / "germanic-aligned-final.tsv",
    )
    parser.add_argument(
        "--reports-root",
        type=Path,
        default=repo_root / "Germanic" / "docs" / "lexeme_reports",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "lexeme_reports"
        / "report_manifest.tsv",
    )
    parser.add_argument(
        "--coverage-audit",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "lexeme_reports"
        / "coverage_audit.md",
    )
    parser.add_argument(
        "--audit-report",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.with_lexeme_reports.audit.md",
    )
    parser.add_argument(
        "--publish-report",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.with_lexeme_reports.publish.md",
    )
    parser.add_argument(
        "--publish-missing-audit",
        type=Path,
        default=repo_root
        / "Germanic"
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.with_lexeme_reports.publish.missing_reports.md",
    )
    args = parser.parse_args()

    rows = load_oe_rows(args.tsv.expanduser().resolve())
    manifest_entries = load_manifest(args.manifest.expanduser().resolve())
    report_files = load_report_files(args.reports_root.expanduser().resolve())
    manifest_diagnostics, _ = apply_manifest(
        rows, manifest_entries, args.reports_root.expanduser().resolve(), report_files
    )
    if manifest_diagnostics:
        raise SystemExit(
            "Manifest diagnostics must be resolved before validation:\n"
            + "\n".join(f"- {item}" for item in manifest_diagnostics)
        )

    row_index = build_row_index(rows)
    production_report_map = build_production_report_map(
        manifest_entries, args.reports_root.expanduser().resolve()
    )
    production_rows = [row for row in rows if row.has_production_manifest_report]
    missing_required_rows = [
        row for row in rows if row.requires_report and not row.has_production_manifest_report
    ]
    regular_empty_note_no_prod = [
        row
        for row in rows
        if row.derivation_class == "regular"
        and not row.has_note
        and not row.has_production_manifest_report
    ]

    coverage_text = args.coverage_audit.expanduser().resolve().read_text(encoding="utf-8")
    expected_prod = parse_count(coverage_text, "Required rows with manifest-backed reports")
    expected_missing = parse_count(coverage_text, "Required rows with no report")

    audit_entries = parse_entries(
        args.audit_report.expanduser().resolve().read_text(encoding="utf-8"),
        row_index,
    )
    publish_entries = parse_entries(
        args.publish_report.expanduser().resolve().read_text(encoding="utf-8"),
        row_index,
    )

    errors: list[str] = []

    if args.audit_report.expanduser().resolve().read_text(encoding="utf-8").count("NOTE:") != 0:
        errors.append("Audit assembled report still contains flat NOTE lines.")
    if args.publish_report.expanduser().resolve().read_text(encoding="utf-8").count("NOTE:") != 0:
        errors.append("Publish assembled report still contains flat NOTE lines.")

    inserted_production_count = 0
    for row in production_rows:
        audit_entry = audit_entries[row.row_id]
        publish_entry = publish_entries[row.row_id]
        report_lines = production_report_map[row.row_id]
        if not contains_subsequence(audit_entry, report_lines):
            errors.append(f"Audit report missing production lexeme report for row {row.row_id}.")
        else:
            inserted_production_count += 1
        if not contains_subsequence(publish_entry, report_lines):
            errors.append(f"Publish report missing production lexeme report for row {row.row_id}.")
        if any(line.startswith("NOTE:") for line in audit_entry):
            errors.append(f"Audit entry {row.row_id} still contains NOTE after production insertion.")
        if any(line.startswith("NOTE:") for line in publish_entry):
            errors.append(f"Publish entry {row.row_id} still contains NOTE after production insertion.")

    if inserted_production_count != expected_prod:
        errors.append(
            f"Inserted production report count {inserted_production_count} does not match coverage audit count {expected_prod}."
        )

    placeholder_count = 0
    for row in missing_required_rows:
        audit_entry = audit_entries[row.row_id]
        if not is_placeholder(audit_entry):
            errors.append(f"Audit report missing placeholder for row {row.row_id}.")
        else:
            placeholder_count += 1
        if any(line.startswith("NOTE:") for line in audit_entry):
            errors.append(f"Audit placeholder entry {row.row_id} still contains NOTE.")

    if placeholder_count != expected_missing:
        errors.append(
            f"Placeholder count {placeholder_count} does not match coverage audit count {expected_missing}."
        )

    for row in regular_empty_note_no_prod:
        audit_entry = audit_entries[row.row_id]
        publish_entry = publish_entries[row.row_id]
        if "### Lexeme report" in "\n".join(audit_entry):
            errors.append(f"Audit report inserted lexeme report for regular empty-note row {row.row_id}.")
        if "### Lexeme report" in "\n".join(publish_entry):
            errors.append(f"Publish report inserted lexeme report for regular empty-note row {row.row_id}.")

    adder_row = next(row for row in rows if row.row_id == "1933")
    adder_entry_publish = publish_entries[adder_row.row_id]
    if "### Lexeme report" in "\n".join(adder_entry_publish):
        errors.append("Adder format_test report was inserted into publish output.")
    adder_report_lines = trim_blank_edges(
        (
            args.reports_root.expanduser().resolve() / "pilot/adder.md"
        ).read_text(encoding="utf-8").splitlines()
    )
    if contains_subsequence(adder_entry_publish, adder_report_lines):
        errors.append("Adder format_test prose was inserted into publish output.")

    missing_publish_audit = args.publish_missing_audit.expanduser().resolve().read_text(encoding="utf-8")
    listed_missing = [
        line
        for line in missing_publish_audit.splitlines()
        if line.startswith("| ")
        and not line.startswith("| ID ")
        and not line.startswith("| :--- ")
    ]
    if len(listed_missing) != expected_missing:
        # subtract alignment row
        errors.append(
            "Publish missing-report audit row count does not match coverage audit missing count."
        )

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Production reports inserted: {inserted_production_count}")
    print(f"Placeholders inserted in audit mode: {placeholder_count}")
    print("Assembly validation passed.")


if __name__ == "__main__":
    main()
