#!/usr/bin/env python3
"""Generate evidence packets for Old English lexeme reports."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

from oe_derivation_report_with_lexeme_reports import BUCKET_PREFIX, extract_field, parse_bucket_name
from oe_lexeme_report_coverage import apply_manifest, load_manifest, load_oe_rows, load_report_files
from oe_paradigm_probe import pilot_specs, render_markdown


PARADIGM_KEYWORD_RE = re.compile(
    r"\b("
    r"gen\.?\s*sg\.?|dat\.?\s*sg\.?|nom\.?\s*sg\.?|acc\.?\s*sg\.?|"
    r"3sg|2sg|3rd singular|2nd singular|imperative|oblique|genitive|dative|"
    r"nominative|accusative|plural|singular|pret\.?|preterite|present|"
    r"paradigm[- ]cell|paradigm cell|cell"
    r")\b",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^#{1,6}\s+")
REF_KEY_RE = re.compile(r"@\w+\{([^,]+),")


@dataclass(frozen=True)
class AlignedRow:
    row_id: str
    fields: Dict[str, str]

    @property
    def concept(self) -> str:
        return self.fields.get("CONCEPT", "")

    @property
    def counterpart(self) -> str:
        return self.fields.get("COUNTERPART", "")

    @property
    def proto(self) -> str:
        return self.fields.get("PROTO", "")

    @property
    def protoform(self) -> str:
        return self.fields.get("PROTOFORM", "")

    @property
    def derivation_class(self) -> str:
        return self.fields.get("DERIVATION_CLASS", "")

    @property
    def note(self) -> str:
        return self.fields.get("NOTE", "")

    @property
    def history(self) -> str:
        return self.fields.get("HISTORY", "")


@dataclass(frozen=True)
class TextHit:
    query_label: str
    path: str
    line_number: int
    heading: str
    snippet: str


def trim_blank_edges(lines: List[str]) -> List[str]:
    start = 0
    end = len(lines)
    while start < end and lines[start] == "":
        start += 1
    while end > start and lines[end - 1] == "":
        end -= 1
    return lines[start:end]


def sanitize_filename_component(text: str) -> str:
    text = text.strip().replace("/", "-")
    text = re.sub(r"[\\:*?\"<>|]", "-", text)
    text = re.sub(r"\s+", "-", text)
    return text


def load_aligned_rows(tsv_path: Path) -> List[AlignedRow]:
    rows: List[AlignedRow] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not counterpart or counterpart == "-":
                continue
            rows.append(
                AlignedRow(
                    row_id=(row.get("ID") or "").strip(),
                    fields={
                        (key or ""): (
                            " | ".join(part.strip() for part in value)
                            if isinstance(value, list)
                            else (value or "").strip()
                        )
                        for key, value in row.items()
                    },
                )
            )
    return rows


def load_known_problems(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_compact_entry_map(path: Path) -> Dict[tuple[str, str, str, str], List[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    current_bucket: str | None = None
    entries: Dict[tuple[str, str, str, str], List[str]] = {}
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
        entry_lines = trim_blank_edges(lines[i:j])
        if current_bucket is None:
            raise SystemExit("Compact report entry appeared before derivation bucket header.")
        concept = entry_lines[0][2:].strip()
        protoform = extract_field(entry_lines, "PROTO:")
        counterpart = extract_field(entry_lines, "EXPECTED:")
        entries[(current_bucket, concept, protoform, counterpart)] = entry_lines
        i = j
    return entries


def nearest_heading(lines: Sequence[str], line_number: int) -> str:
    for index in range(line_number - 1, -1, -1):
        if HEADING_RE.match(lines[index]):
            return lines[index]
    return "(no nearby heading)"


def make_snippet(lines: Sequence[str], line_number: int, context: int = 2) -> str:
    start = max(0, line_number - context - 1)
    end = min(len(lines), line_number + context)
    snippet_lines = [f"{index + 1}: {lines[index]}" for index in range(start, end)]
    return "\n".join(snippet_lines)


def exact_match_line(line: str, query: str) -> bool:
    return query.casefold() in line.casefold()


def concept_match_line(line: str, concept: str) -> bool:
    if not concept:
        return False
    return re.search(rf"\b{re.escape(concept)}\b", line, re.IGNORECASE) is not None


def collect_text_hits(
    path: Path,
    queries: Sequence[tuple[str, str, str]],
    *,
    max_hits_per_query: int = 5,
) -> List[TextHit]:
    lines = path.read_text(encoding="utf-8").splitlines()
    hits: List[TextHit] = []
    seen: set[tuple[str, int]] = set()
    for query_label, query_value, query_kind in queries:
        count = 0
        for line_number, line in enumerate(lines, start=1):
            matched = (
                exact_match_line(line, query_value)
                if query_kind == "exact"
                else concept_match_line(line, query_value)
            )
            if not matched:
                continue
            key = (query_label, line_number)
            if key in seen:
                continue
            seen.add(key)
            hits.append(
                TextHit(
                    query_label=query_label,
                    path=str(path),
                    line_number=line_number,
                    heading=nearest_heading(lines, line_number),
                    snippet=make_snippet(lines, line_number),
                )
            )
            count += 1
            if count >= max_hits_per_query:
                break
    return hits


def collect_directory_hits(
    directories: Iterable[Path],
    queries: Sequence[tuple[str, str, str]],
    *,
    max_hits_per_file: int = 2,
    max_files: int = 16,
) -> List[TextHit]:
    hits: List[TextHit] = []
    files_seen = 0
    for directory in directories:
        if not directory.exists():
            continue
        for path in sorted(p for p in directory.rglob("*") if p.is_file()):
            if files_seen >= max_files:
                return hits
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            lines = text.splitlines()
            file_hits = 0
            for query_label, query_value, query_kind in queries:
                for line_number, line in enumerate(lines, start=1):
                    matched = (
                        exact_match_line(line, query_value)
                        if query_kind == "exact"
                        else concept_match_line(line, query_value)
                    )
                    if not matched:
                        continue
                    hits.append(
                        TextHit(
                            query_label=query_label,
                            path=str(path),
                            line_number=line_number,
                            heading=nearest_heading(lines, line_number),
                            snippet=make_snippet(lines, line_number, context=1),
                        )
                    )
                    file_hits += 1
                    if file_hits >= max_hits_per_file:
                        break
                if file_hits >= max_hits_per_file:
                    break
            if file_hits:
                files_seen += 1
    return hits


def matching_known_problems(row: AlignedRow, problems: List[Dict[str, str]]) -> List[Dict[str, str]]:
    matched: List[Dict[str, str]] = []
    targets = {row.protoform, row.proto}
    for problem in problems:
        proto = (problem.get("proto") or "").strip()
        if proto and proto in targets:
            matched.append(problem)
    return matched


def matching_lexical_rows(path: Path, row: AlignedRow, *, table_kind: str) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        matches = []
        for item in reader:
            if table_kind == "wiktionary":
                english = (item.get("ENGLISH") or "").strip().casefold()
                oe_form = (item.get("OE_FORM") or "").strip().casefold()
                detail = (item.get("DETAIL") or "").strip().casefold()
                if (
                    english == row.concept.casefold()
                    or oe_form == row.counterpart.casefold()
                    or row.counterpart.casefold() in detail
                ):
                    matches.append(item)
            else:
                english = (item.get("ENGLISH") or "").strip().casefold()
                old_english = (item.get("OLD_ENGLISH") or "").strip().casefold()
                if english == row.concept.casefold() or old_english == row.counterpart.casefold():
                    matches.append(item)
        return matches


def parse_bibliography_candidates(path: Path, evidence_text: str) -> List[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: List[tuple[str, List[str]]] = []
    current_key: str | None = None
    current_authors: List[str] = []
    for line in lines:
        key_match = REF_KEY_RE.search(line)
        if key_match:
            if current_key is not None:
                entries.append((current_key, current_authors))
            current_key = key_match.group(1)
            current_authors = []
            continue
        if current_key and "author" in line and "{" in line and "}" in line:
            author_text = line.split("{", 1)[1].rsplit("}", 1)[0]
            for author in author_text.split(" and "):
                author = author.strip()
                if "," in author:
                    surname = author.split(",", 1)[0].strip()
                else:
                    surname = author.split()[-1]
                if surname:
                    current_authors.append(surname)
    if current_key is not None:
        entries.append((current_key, current_authors))

    lowered_evidence = evidence_text.casefold()
    candidates: List[tuple[str, str]] = []
    seen: set[str] = set()
    for key, authors in entries:
        reasons = []
        if key.casefold() in lowered_evidence:
            reasons.append("explicit key mention")
        for surname in authors:
            if re.search(rf"\b{re.escape(surname.casefold())}\b", lowered_evidence):
                reasons.append(f"author mention: {surname}")
                break
        if reasons and key not in seen:
            seen.add(key)
            candidates.append((key, "; ".join(reasons)))
    return candidates


def should_run_probe(row: AlignedRow) -> bool:
    return (
        row.derivation_class in {"late_analogy", "known_unmodelled"}
        or PARADIGM_KEYWORD_RE.search(row.note or "") is not None
    )


def generate_probe_section(row: AlignedRow, repo_root: Path) -> List[str]:
    if not should_run_probe(row):
        return []
    lines = ["## Paradigm probe", ""]
    probe_row = {
        "CONCEPT": row.concept,
        "COUNTERPART": row.counterpart,
        "PROTO": row.proto,
        "PROTOFORM": row.protoform,
        "DERIVATION_CLASS": row.derivation_class,
    }
    key = f"{row.concept}:{row.counterpart}"
    spec_map = pilot_specs(probe_row)
    if key not in spec_map:
        lines.append(
            "No built-in `oe_paradigm_probe.py` specification exists yet for this row, "
            "but the packet flagged it for future probe work because the derivation class "
            "or TSV note points to paradigm-cell reasoning."
        )
        lines.append("")
        return lines
    lines.extend(
        render_markdown(
            row=probe_row,
            target=row.counterpart,
            spec=spec_map[key],
            bin_path=repo_root / "backend" / "old_english.bin",
        ).splitlines()
    )
    lines.append("")
    return lines


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> List[str]:
    if not rows:
        return ["_None_", ""]
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(":---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(str(cell).replace("|", "\\|").replace("\n", "<br>") for cell in row)
            + " |"
        )
    lines.append("")
    return lines


def packet_path_for(row: AlignedRow, packets_dir: Path) -> Path:
    filename = (
        f"{row.row_id}-"
        f"{sanitize_filename_component(row.concept)}-"
        f"{sanitize_filename_component(row.counterpart)}.md"
    )
    return packets_dir / filename


def build_packet(
    row: AlignedRow,
    *,
    manifest_entries,
    compact_entry_map,
    known_problems,
    dev_notes_path: Path,
    analysis_dirs: Sequence[Path],
    wiktionary_path: Path,
    swadesh_path: Path,
    refs_path: Path,
    repo_root: Path,
) -> str:
    manifest_entry = next((entry for entry in manifest_entries if entry.row_id == row.row_id), None)
    compact_entry = compact_entry_map.get(
        (row.derivation_class, row.concept, row.protoform, row.counterpart)
    )
    if compact_entry is None:
        raise SystemExit(
            "Could not find compact derivation entry for "
            f"{row.row_id} / {row.concept} / {row.counterpart}."
        )

    queries = [
        ("exact PROTOFORM", row.protoform, "exact"),
        ("exact COUNTERPART", row.counterpart, "exact"),
        ("concept name", row.concept, "concept"),
    ]
    dev_hits = collect_text_hits(dev_notes_path, queries, max_hits_per_query=6)
    analysis_hits = collect_directory_hits(analysis_dirs, queries, max_hits_per_file=3, max_files=24)
    problem_hits = matching_known_problems(row, known_problems)
    wiktionary_hits = matching_lexical_rows(wiktionary_path, row, table_kind="wiktionary")
    swadesh_hits = matching_lexical_rows(swadesh_path, row, table_kind="swadesh")

    evidence_text = "\n".join(
        [
            row.note,
            row.history,
            *[hit.snippet for hit in dev_hits],
            *[hit.snippet for hit in analysis_hits],
        ]
    )
    bib_candidates = parse_bibliography_candidates(refs_path, evidence_text)

    lines: List[str] = [
        f"# Evidence packet — {row.row_id} {row.concept} / {row.counterpart}",
        "",
        "## TSV row data",
        "",
    ]
    lines.extend(
        markdown_table(
            [
                "ID",
                "CONCEPT",
                "COUNTERPART",
                "PROTO",
                "PROTOFORM",
                "DERIVATION_CLASS",
                "NOTE",
                "HISTORY",
            ],
            [
                [
                    row.row_id,
                    row.concept,
                    row.counterpart,
                    row.proto,
                    row.protoform,
                    row.derivation_class,
                    row.note or "-",
                    row.history or "-",
                ]
            ],
        )
    )

    lines.append("## Manifest status")
    lines.append("")
    if manifest_entry is None:
        lines.append("_No manifest entry._")
        lines.append("")
    else:
        lines.extend(
            markdown_table(
                ["REPORT_PATH", "STATUS"],
                [[manifest_entry.report_path, manifest_entry.status]],
            )
        )

    lines.append("## Compact derivation trace entry")
    lines.append("")
    lines.append("```md")
    lines.extend(compact_entry)
    lines.append("```")
    lines.append("")

    lines.append("## Matching oe_known_problems.tsv entries")
    lines.append("")
    if not problem_hits:
        lines.append("_None_")
        lines.append("")
    else:
        lines.extend(
            markdown_table(
                ["proto", "status", "category", "reason", "refs", "added"],
                [
                    [
                        item.get("proto", ""),
                        item.get("status", ""),
                        item.get("category", ""),
                        item.get("reason", ""),
                        item.get("refs", ""),
                        item.get("added", ""),
                    ]
                    for item in problem_hits
                ],
            )
        )

    lines.append("## DEV_NOTES hits")
    lines.append("")
    if not dev_hits:
        lines.append("_None_")
        lines.append("")
    else:
        for hit in dev_hits:
            lines.append(
                f"### {hit.query_label} — {Path(hit.path).name}:{hit.line_number}"
            )
            lines.append("")
            lines.append(f"- Nearby heading: {hit.heading}")
            lines.append("")
            lines.append("```text")
            lines.extend(hit.snippet.splitlines())
            lines.append("```")
            lines.append("")

    lines.append("## Analysis and dossier hits")
    lines.append("")
    if not analysis_hits:
        lines.append("_None_")
        lines.append("")
    else:
        for hit in analysis_hits:
            relpath = str(Path(hit.path).relative_to(repo_root))
            lines.append(f"### {relpath}:{hit.line_number} ({hit.query_label})")
            lines.append("")
            lines.append(f"- Nearby heading: {hit.heading}")
            lines.append("")
            lines.append("```text")
            lines.extend(hit.snippet.splitlines())
            lines.append("```")
            lines.append("")

    lines.append("## Local lexical-table hits")
    lines.append("")
    lines.append("### old_english_wiktionary.tsv")
    lines.append("")
    lines.extend(
        markdown_table(
            ["ENGLISH", "OE_FORM", "SOURCE", "DETAIL", "PAGE"],
            [
                [
                    item.get("ENGLISH", ""),
                    item.get("OE_FORM", ""),
                    item.get("SOURCE", ""),
                    item.get("DETAIL", ""),
                    item.get("PAGE", ""),
                ]
                for item in wiktionary_hits
            ],
        )
    )
    lines.append("### old_english_swadesh.tsv")
    lines.append("")
    lines.extend(
        markdown_table(
            ["NUMBER", "ENGLISH", "OLD_ENGLISH", "IPA_RAW"],
            [
                [
                    item.get("NUMBER", ""),
                    item.get("ENGLISH", ""),
                    item.get("OLD_ENGLISH", ""),
                    item.get("IPA_RAW", ""),
                ]
                for item in swadesh_hits
            ],
        )
    )

    lines.append("## Bibliography-key candidates")
    lines.append("")
    lines.extend(
        markdown_table(
            ["Key", "Why it was selected"],
            [[key, reason] for key, reason in bib_candidates],
        )
    )

    lines.extend(generate_probe_section(row, repo_root))
    return "\n".join(lines) + "\n"


def parse_missing_ids(path: Path) -> List[str]:
    ids: List[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| "):
            continue
        if line.startswith("| ID ") or line.startswith("| :--- "):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if parts and parts[0].isdigit():
            ids.append(parts[0])
    return ids


def write_packet_for_row(
    row: AlignedRow,
    *,
    packets_dir: Path,
    manifest_entries,
    compact_entry_map,
    known_problems,
    dev_notes_path: Path,
    analysis_dirs: Sequence[Path],
    wiktionary_path: Path,
    swadesh_path: Path,
    refs_path: Path,
    repo_root: Path,
) -> Path:
    content = build_packet(
        row,
        manifest_entries=manifest_entries,
        compact_entry_map=compact_entry_map,
        known_problems=known_problems,
        dev_notes_path=dev_notes_path,
        analysis_dirs=analysis_dirs,
        wiktionary_path=wiktionary_path,
        swadesh_path=swadesh_path,
        refs_path=refs_path,
        repo_root=repo_root,
    )
    out_path = packet_path_for(row, packets_dir)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    return out_path


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    germanic_dir = repo_root / "Germanic"
    parser = argparse.ArgumentParser(description=__doc__)
    selector = parser.add_mutually_exclusive_group(required=True)
    selector.add_argument("--id", help="Old English row ID to packetize")
    selector.add_argument(
        "--missing",
        action="store_true",
        help="Generate packets for IDs listed in the publish missing-report audit",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Optional limit for --missing batch mode",
    )
    parser.add_argument(
        "--packets-dir",
        type=Path,
        default=germanic_dir / "docs" / "lexeme_reports" / "packets",
        help="Output directory for packets (default: %(default)s)",
    )
    parser.add_argument(
        "--tsv",
        type=Path,
        default=germanic_dir / "data" / "germanic-aligned-final.tsv",
    )
    parser.add_argument(
        "--known-problems",
        type=Path,
        default=germanic_dir / "data" / "oe_known_problems.tsv",
    )
    parser.add_argument(
        "--dev-notes",
        type=Path,
        default=germanic_dir / "docs" / "DEV_NOTES.md",
    )
    parser.add_argument(
        "--compact-report",
        type=Path,
        default=germanic_dir
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.compact.md",
    )
    parser.add_argument(
        "--missing-report-audit",
        type=Path,
        default=germanic_dir
        / "docs"
        / "debug_snapshots"
        / "oe_derivation_class_trace_report.with_lexeme_reports.publish.missing_reports.md",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=germanic_dir / "docs" / "lexeme_reports" / "report_manifest.tsv",
    )
    parser.add_argument(
        "--wiktionary",
        type=Path,
        default=germanic_dir / "data" / "old_english_wiktionary.tsv",
    )
    parser.add_argument(
        "--swadesh",
        type=Path,
        default=germanic_dir / "data" / "old_english_swadesh.tsv",
    )
    parser.add_argument(
        "--refs",
        type=Path,
        default=repo_root / "docs" / "refs.bib",
    )
    args = parser.parse_args()

    rows = load_aligned_rows(args.tsv.expanduser().resolve())
    rows_by_id = {row.row_id: row for row in rows}

    manifest_entries = load_manifest(args.manifest.expanduser().resolve())
    coverage_rows = load_oe_rows(args.tsv.expanduser().resolve())
    report_files = load_report_files((germanic_dir / "docs" / "lexeme_reports").resolve())
    manifest_diagnostics, _ = apply_manifest(
        coverage_rows,
        manifest_entries,
        (germanic_dir / "docs" / "lexeme_reports").resolve(),
        report_files,
    )
    if manifest_diagnostics:
        raise SystemExit(
            "Manifest diagnostics must be resolved before generating packets:\n"
            + "\n".join(f"- {item}" for item in manifest_diagnostics)
        )

    compact_entry_map = load_compact_entry_map(args.compact_report.expanduser().resolve())
    known_problems = load_known_problems(args.known_problems.expanduser().resolve())
    packets_dir = args.packets_dir.expanduser().resolve()
    analysis_dirs = [
        germanic_dir / "docs" / "analysis",
        germanic_dir / "docs" / "dossiers",
    ]

    if args.id:
        row = rows_by_id.get(str(args.id))
        if row is None:
            raise SystemExit(f"No Old English TSV row found for ID {args.id}.")
        out_path = write_packet_for_row(
            row,
            packets_dir=packets_dir,
            manifest_entries=manifest_entries,
            compact_entry_map=compact_entry_map,
            known_problems=known_problems,
            dev_notes_path=args.dev_notes.expanduser().resolve(),
            analysis_dirs=analysis_dirs,
            wiktionary_path=args.wiktionary.expanduser().resolve(),
            swadesh_path=args.swadesh.expanduser().resolve(),
            refs_path=args.refs.expanduser().resolve(),
            repo_root=repo_root,
        )
        print(f"Wrote {out_path}")
        return

    missing_ids = parse_missing_ids(args.missing_report_audit.expanduser().resolve())
    if args.limit is not None:
        missing_ids = missing_ids[: args.limit]
    written: List[Path] = []
    for row_id in missing_ids:
        row = rows_by_id.get(row_id)
        if row is None:
            raise SystemExit(f"Missing-report audit referenced unknown row ID {row_id}.")
        written.append(
            write_packet_for_row(
                row,
                packets_dir=packets_dir,
                manifest_entries=manifest_entries,
                compact_entry_map=compact_entry_map,
                known_problems=known_problems,
                dev_notes_path=args.dev_notes.expanduser().resolve(),
                analysis_dirs=analysis_dirs,
                wiktionary_path=args.wiktionary.expanduser().resolve(),
                swadesh_path=args.swadesh.expanduser().resolve(),
                refs_path=args.refs.expanduser().resolve(),
                repo_root=repo_root,
            )
        )
    for path in written:
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
