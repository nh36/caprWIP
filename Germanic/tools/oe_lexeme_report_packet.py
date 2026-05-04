#!/usr/bin/env python3
"""Generate evidence packets for Old English lexeme reports."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence

from oe_derivation_report_with_lexeme_reports import (
    BUCKET_PREFIX,
    extract_field,
    parse_bucket_name,
)
from oe_lexeme_report_coverage import (
    apply_manifest,
    load_manifest,
    load_oe_rows,
    load_report_files,
)
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
EXPLICIT_PARADIGM_DEPENDENCE_RE = re.compile(
    r"paradigm[- ]cell|using\s+(?:gen|dat|nom|acc)\.?\s*sg\.?|"
    r"every\s+paradigm\s+cell|no\s+.*paradigm\s+cell|"
    r"1/3\s*sg\.?\s*pret\.?|3pl\s*pret\.?|retargeted\s+from",
    re.IGNORECASE,
)
PHILOLOGICAL_FORM_NOTE_RE = re.compile(
    r"\b(?:nom\.?\s*sg\.?|oblique|oblique form|gen\.?\s*sg\.?|dat\.?\s*sg\.?)\b",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^#{1,6}\s+")
REF_KEY_RE = re.compile(r"@\w+\{([^,]+),")
YEAR_RE = re.compile(r"\b(1[0-9]{3}|20[0-9]{2})\b")
FILENAME_REF_RE = re.compile(r"([\w-]+\.md)")
SURNAME_YEAR_RE_TEMPLATE = r"\b{surname}\b(?:[^0-9]{{0,16}})(?P<year>1[0-9]{{3}}|20[0-9]{{2}})"
TECHNICAL_NOTE_KEYWORDS = [
    "A-restoration",
    "a-umlaut",
    "i-umlaut",
    "u-lowering",
    "palatalization",
    "breaking",
    "smoothing",
    "Anglian",
    "West Saxon",
    "dat.sg.",
    "gen.sg.",
    "1/3 sg pret.",
]
DIAGNOSTIC_PATH_MARKERS = (
    "mismatch",
    "todo",
    "snapshot",
    "sandbox",
    "english_sandbox",
    "english-sandbox",
)


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


@dataclass(frozen=True)
class BibEntry:
    key: str
    authors: tuple[str, ...]
    year: str


QUERY_PRIORITY = {
    "row ID": 0,
    "exact pair": 1,
    "exact PROTOFORM": 2,
    "exact COUNTERPART": 3,
    "note keyword": 4,
    "concept name": 5,
}


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


def row_id_match_line(line: str, row_id: str) -> bool:
    return (
        re.search(rf"\brow\s+{re.escape(row_id)}\b", line, re.IGNORECASE) is not None
        or f"| {row_id} |" in line
        or re.search(rf"^\s*{re.escape(row_id)}\b", line) is not None
    )


def pair_match_line(line: str, pair: tuple[str, str]) -> bool:
    protoform, counterpart = pair
    lowered = line.casefold()
    return protoform.casefold() in lowered and counterpart.casefold() in lowered


def match_query(line: str, query_value: Any, query_kind: str) -> bool:
    if query_kind == "exact":
        return exact_match_line(line, query_value)
    if query_kind == "concept":
        return concept_match_line(line, query_value)
    if query_kind == "row_id":
        return row_id_match_line(line, query_value)
    if query_kind == "pair":
        return pair_match_line(line, query_value)
    raise ValueError(f"Unsupported query kind: {query_kind}")


def collect_text_hits(
    path: Path,
    queries: Sequence[tuple[str, Any, str]],
    *,
    max_hits_per_query: int = 5,
) -> List[TextHit]:
    lines = path.read_text(encoding="utf-8").splitlines()
    hits: List[TextHit] = []
    seen: set[tuple[str, int]] = set()
    for query_label, query_value, query_kind in queries:
        count = 0
        for line_number, line in enumerate(lines, start=1):
            if not match_query(line, query_value, query_kind):
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


def query_priority(label: str) -> int:
    for prefix, priority in QUERY_PRIORITY.items():
        if label == prefix or label.startswith(prefix + ":"):
            return priority
    return 99


def dedupe_hits(hits: Sequence[TextHit]) -> List[TextHit]:
    best: Dict[tuple[str, int], TextHit] = {}
    for hit in hits:
        key = (hit.path, hit.line_number)
        current = best.get(key)
        if current is None or query_priority(hit.query_label) < query_priority(current.query_label):
            best[key] = hit
    return sorted(best.values(), key=lambda item: (item.path, item.line_number, item.query_label))


def collect_directory_hits(
    directories: Iterable[Path],
    queries: Sequence[tuple[str, Any, str]],
    *,
    max_hits_per_file: int = 3,
    max_files: int = 24,
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
                    if not match_query(line, query_value, query_kind):
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


def parse_bibliography_entries(path: Path) -> List[BibEntry]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: List[BibEntry] = []
    current_key: str | None = None
    current_authors: List[str] = []
    current_year = ""
    for line in lines:
        key_match = REF_KEY_RE.search(line)
        if key_match:
            if current_key is not None:
                entries.append(
                    BibEntry(
                        key=current_key,
                        authors=tuple(current_authors),
                        year=current_year,
                    )
                )
            current_key = key_match.group(1)
            current_authors = []
            current_year = ""
            continue
        if current_key and "author" in line and "{" in line and "}" in line:
            author_text = line.split("{", 1)[1].rsplit("}", 1)[0]
            for author in author_text.split(" and "):
                author = author.strip()
                surname = author.split(",", 1)[0].strip() if "," in author else author.split()[-1]
                if surname:
                    current_authors.append(surname)
        if current_key and line.strip().startswith("year") and "{" in line and "}" in line:
            current_year = line.split("{", 1)[1].rsplit("}", 1)[0].strip()
    if current_key is not None:
        entries.append(BibEntry(key=current_key, authors=tuple(current_authors), year=current_year))
    return entries


def rank_bibliography_candidates(path: Path, evidence_text: str) -> tuple[List[tuple[str, str]], List[tuple[str, str]]]:
    entries = parse_bibliography_entries(path)
    lowered_evidence = evidence_text.casefold()
    explicit_years = set(YEAR_RE.findall(evidence_text))
    authors_to_entries: Dict[str, List[BibEntry]] = {}
    for entry in entries:
        for surname in entry.authors:
            authors_to_entries.setdefault(surname, []).append(entry)

    scored: Dict[str, tuple[int, str]] = {}
    low_confidence: List[tuple[str, str]] = []

    for surname, surname_entries in authors_to_entries.items():
        surname_match = re.search(rf"\b{re.escape(surname.casefold())}\b", lowered_evidence)
        if not surname_match:
            continue

        year_match = re.search(
            SURNAME_YEAR_RE_TEMPLATE.format(surname=re.escape(surname.casefold())),
            lowered_evidence,
        )
        preferred_key: str | None = None

        for entry in surname_entries:
            reasons: List[str] = []
            score = 0
            if entry.key.casefold() in lowered_evidence:
                score += 100
                reasons.append("explicit key mention")
            if year_match and entry.year and year_match.group("year") == entry.year:
                score += 90
                reasons.append(f"author + year mention ({surname} {entry.year})")
            elif entry.year and entry.year in explicit_years and surname.casefold() in lowered_evidence:
                score += 60
                reasons.append(f"explicit year mention ({entry.year})")
            elif surname.casefold() in lowered_evidence:
                if surname == "Kroonen" and entry.key == "Kroonen2013":
                    score += 80
                    reasons.append("default Proto-Germanic etymology key for Kroonen")
                elif len(surname_entries) == 1:
                    score += 70
                    reasons.append(f"single available key for {surname}")
                else:
                    score += 20
                    reasons.append(f"surname mention only: {surname}")
            if score > 0:
                scored[entry.key] = (score, "; ".join(reasons))

        if surname == "Kroonen" and "Kroonen2013" in scored:
            preferred_key = "Kroonen2013"
        elif year_match:
            for entry in surname_entries:
                if entry.year == year_match.group("year") and entry.key in scored:
                    preferred_key = entry.key
                    break
        else:
            ranked = sorted(
                [entry for entry in surname_entries if entry.key in scored],
                key=lambda entry: scored[entry.key][0],
                reverse=True,
            )
            if len(ranked) == 1:
                preferred_key = ranked[0].key
            elif ranked and scored[ranked[0].key][0] >= 100:
                preferred_key = ranked[0].key

        for entry in surname_entries:
            if entry.key not in scored:
                continue
            score, reason = scored[entry.key]
            if preferred_key == entry.key:
                continue
            if len(surname_entries) > 1 or score < 70:
                low_confidence.append((entry.key, reason))

    preferred = sorted(
        [
            (key, reason)
            for key, (score, reason) in scored.items()
            if all(key != low_key for low_key, _ in low_confidence)
        ],
        key=lambda item: scored[item[0]][0],
        reverse=True,
    )

    seen_low: set[str] = set()
    filtered_low: List[tuple[str, str]] = []
    for key, reason in low_confidence:
        if key in seen_low or any(key == pref_key for pref_key, _ in preferred):
            continue
        seen_low.add(key)
        filtered_low.append((key, reason))

    return preferred, filtered_low


def note_keyword_queries(note: str) -> List[tuple[str, Any, str]]:
    lowered = note.casefold()
    queries: List[tuple[str, Any, str]] = []
    for phrase in TECHNICAL_NOTE_KEYWORDS:
        if phrase.casefold() in lowered:
            queries.append((f"note keyword: {phrase}", phrase, "exact"))
    return queries


def referenced_markdown_files(text: str) -> set[str]:
    return {match.group(1) for match in FILENAME_REF_RE.finditer(text)}


def hit_combined_text(hit: TextHit) -> str:
    return f"{hit.heading}\n{hit.snippet}".casefold()


def mentions_exact_pair(hit: TextHit, row: AlignedRow) -> bool:
    text = hit_combined_text(hit)
    return row.protoform.casefold() in text and row.counterpart.casefold() in text


def mentions_row_id(hit: TextHit, row: AlignedRow) -> bool:
    text = hit_combined_text(hit)
    return row_id_match_line(text, row.row_id)


def stale_diagnostic_hit(hit: TextHit, row: AlignedRow) -> bool:
    path_lower = hit.path.casefold()
    text = hit_combined_text(hit)
    if any(marker in path_lower for marker in DIAGNOSTIC_PATH_MARKERS):
        return True
    if hit.query_label == "concept name":
        return True
    if "expected " in text and row.counterpart.casefold() not in text:
        return True
    if "former expected" in text or "old target" in text or "previous target" in text:
        return True
    return False


def classify_dev_hit(hit: TextHit, row: AlignedRow) -> str:
    if mentions_row_id(hit, row) or mentions_exact_pair(hit, row):
        return "high"
    if stale_diagnostic_hit(hit, row):
        return "diagnostic"
    if hit.query_label in {"exact PROTOFORM", "exact COUNTERPART"} or hit.query_label.startswith("note keyword:"):
        return "supporting"
    return "diagnostic"


def classify_analysis_hit(hit: TextHit, row: AlignedRow, referenced_files: set[str]) -> str:
    basename = Path(hit.path).name
    if mentions_row_id(hit, row):
        return "high"
    if basename in referenced_files:
        return "high"
    if stale_diagnostic_hit(hit, row):
        return "diagnostic"
    if hit.query_label in {"exact PROTOFORM", "exact COUNTERPART"} or hit.query_label.startswith("note keyword:"):
        return "supporting"
    return "diagnostic"


def split_hits(
    hits: Sequence[TextHit],
    classifier,
) -> tuple[List[TextHit], List[TextHit], List[TextHit]]:
    high: List[TextHit] = []
    supporting: List[TextHit] = []
    diagnostic: List[TextHit] = []
    for hit in hits:
        bucket = classifier(hit)
        if bucket == "high":
            high.append(hit)
        elif bucket == "supporting":
            supporting.append(hit)
        else:
            diagnostic.append(hit)
    return high, supporting, diagnostic


def should_probe_row(row: AlignedRow) -> str | None:
    if row.derivation_class in {"late_analogy", "known_unmodelled"}:
        return "required"
    if EXPLICIT_PARADIGM_DEPENDENCE_RE.search(row.note or ""):
        return "required"
    if row.derivation_class == "regular" and PHILOLOGICAL_FORM_NOTE_RE.search(row.note or ""):
        return "philological_note"
    return None


def generate_probe_section(row: AlignedRow, repo_root: Path) -> List[str]:
    reason = should_probe_row(row)
    if reason is None:
        return []

    lines = ["## Paradigm probe", ""]
    if reason == "philological_note":
        lines.append(
            "Philological note; no paradigm probe required for this row under the current "
            "classification. The note mentions paradigm forms, but it does not yet depend on "
            "a paradigm-cell solution."
        )
        lines.append("")
        return lines

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
            "Paradigm probe required for this row, but no built-in "
            "`oe_paradigm_probe.py` specification exists yet. This packet should be "
            "used to draft the probe configuration before prose drafting."
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


def render_hits_section(title: str, hits: Sequence[TextHit], repo_root: Path) -> List[str]:
    lines = [f"### {title}", ""]
    if not hits:
        lines.append("_None_")
        lines.append("")
        return lines
    for hit in hits:
        relpath = str(Path(hit.path).relative_to(repo_root))
        lines.append(f"#### {relpath}:{hit.line_number} ({hit.query_label})")
        lines.append("")
        lines.append(f"- Nearby heading: {hit.heading}")
        lines.append("")
        lines.append("```text")
        lines.extend(hit.snippet.splitlines())
        lines.append("```")
        lines.append("")
    return lines


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

    queries: List[tuple[str, Any, str]] = [
        ("row ID", row.row_id, "row_id"),
        ("exact pair", (row.protoform, row.counterpart), "pair"),
        ("exact PROTOFORM", row.protoform, "exact"),
        ("exact COUNTERPART", row.counterpart, "exact"),
        ("concept name", row.concept, "concept"),
        *note_keyword_queries(row.note or ""),
    ]
    dev_hits = collect_text_hits(dev_notes_path, queries, max_hits_per_query=6)
    dev_hits = dedupe_hits(dev_hits)
    analysis_hits = collect_directory_hits(
        analysis_dirs,
        queries,
        max_hits_per_file=3,
        max_files=32,
    )
    analysis_hits = dedupe_hits(analysis_hits)
    referenced_files = referenced_markdown_files("\n".join([row.note, row.history]))
    dev_high, dev_supporting, dev_diagnostic = split_hits(
        dev_hits,
        lambda hit: classify_dev_hit(hit, row),
    )
    analysis_high, analysis_supporting, analysis_diagnostic = split_hits(
        analysis_hits,
        lambda hit: classify_analysis_hit(hit, row, referenced_files),
    )

    problem_hits = matching_known_problems(row, known_problems)
    wiktionary_hits = matching_lexical_rows(wiktionary_path, row, table_kind="wiktionary")
    swadesh_hits = matching_lexical_rows(swadesh_path, row, table_kind="swadesh")

    evidence_text = "\n".join(
        [
            row.note,
            row.history,
            *[hit.snippet for hit in dev_high],
            *[hit.snippet for hit in dev_supporting],
            *[hit.snippet for hit in analysis_high],
            *[hit.snippet for hit in analysis_supporting],
        ]
    )
    preferred_bib, low_conf_bib = rank_bibliography_candidates(refs_path, evidence_text)

    lines: List[str] = [
        f"# Evidence packet — {row.row_id} {row.concept} / {row.counterpart}",
        "",
        "> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.",
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

    lines.append("## High-confidence evidence")
    lines.append("")
    lines.append("### Compact derivation trace entry")
    lines.append("")
    lines.append("```md")
    lines.extend(compact_entry)
    lines.append("```")
    lines.append("")

    lines.append("### Matching oe_known_problems.tsv entries")
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

    lines.extend(render_hits_section("DEV_NOTES hits", dev_high, repo_root))
    lines.extend(render_hits_section("Analysis and dossier hits", analysis_high, repo_root))

    lines.append("## Supporting/background evidence")
    lines.append("")
    lines.extend(render_hits_section("DEV_NOTES hits", dev_supporting, repo_root))
    lines.extend(render_hits_section("Analysis and dossier hits", analysis_supporting, repo_root))

    lines.append("### Local lexical-table hits")
    lines.append("")
    lines.append("#### old_english_wiktionary.tsv")
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
    lines.append("#### old_english_swadesh.tsv")
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

    lines.append("## Possibly stale or diagnostic evidence")
    lines.append("")
    lines.extend(render_hits_section("DEV_NOTES hits", dev_diagnostic, repo_root))
    lines.extend(render_hits_section("Analysis and dossier hits", analysis_diagnostic, repo_root))

    lines.append("## Bibliography-key candidates")
    lines.append("")
    lines.append("### Preferred candidates")
    lines.append("")
    lines.extend(markdown_table(["Key", "Why it was selected"], preferred_bib))
    lines.append("### Low-confidence candidates")
    lines.append("")
    lines.extend(markdown_table(["Key", "Why it was selected"], low_conf_bib))

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

    def write(row_id: str) -> Path:
        row = rows_by_id.get(row_id)
        if row is None:
            raise SystemExit(f"No Old English TSV row found for ID {row_id}.")
        return write_packet_for_row(
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

    if args.id:
        out_path = write(str(args.id))
        print(f"Wrote {out_path}")
        return

    missing_ids = parse_missing_ids(args.missing_report_audit.expanduser().resolve())
    if args.limit is not None:
        missing_ids = missing_ids[: args.limit]
    for row_id in missing_ids:
        print(f"Wrote {write(row_id)}")


if __name__ == "__main__":
    main()
