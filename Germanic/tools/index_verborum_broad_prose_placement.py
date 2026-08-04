#!/usr/bin/env python3
"""Stage 4A shadow-only inventory and placement planning for broad prose rows."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))
from build_full_lexical_volume import normalize_print_text

BOOK_DIR = REPO_ROOT / "Germanic/docs/book"

PRINT_MAIN_TSV = BOOK_DIR / "index_verborum_print_main.tsv"
PRINT_EXCLUDED_TSV = BOOK_DIR / "index_verborum_print_excluded.tsv"
EMISSION_TABLE_TSV = BOOK_DIR / "index_verborum_emission_table.tsv"
BOOK_EMISSIONS_TSV = BOOK_DIR / "index_verborum_book_emissions.tsv"
BROAD_DECISIONS_TSV = BOOK_DIR / "index_verborum_broad_prose_decisions.tsv"

GROUP_PURE_SINGLETON = "pure_singleton"
GROUP_PURE_SHARED_ONE = "pure_shared_one_passage"
GROUP_PURE_SHARED_MULTI = "pure_shared_multiple_passages"
GROUP_MIXED_SCOPE = "mixed_scope"
GROUP_UNRESOLVED = "unresolved"

STATUS_PASSAGE_SHADOW = "passage_shadow"
STATUS_RETAIN_MIXED = "retain_heading_mixed_scope"
STATUS_RETAIN_UNRESOLVED = "retain_heading_unresolved"


@dataclass(frozen=True)
class SourcePassage:
    source_path: str
    source_ref: str
    block_kind: str
    start_line: int
    end_line: int
    block_text: str


@dataclass(frozen=True)
class PlacementRecord:
    emission_id: str
    representative_occurrence_id: str
    representative_source_ref: str
    representative_display: str
    representative_form: str
    representative_sort_key: str
    current_emission_path: str
    current_site: str
    group_class: str
    proposed_status: str
    resolved_block_kind: str
    resolved_block_start_line: int
    resolved_block_end_line: int
    note: str
    canonical_index_key: str = ""


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _extract_index_key(index_command: str) -> str:
    prefix = r"\index[iv]{"
    if not index_command.startswith(prefix):
        raise ValueError(f"not an index command: {index_command!r}")
    i = len(prefix)
    depth = 1
    while i < len(index_command) and depth > 0:
        if index_command[i] == "{":
            depth += 1
        elif index_command[i] == "}":
            depth -= 1
        i += 1
    if depth != 0:
        raise ValueError(f"unbalanced braces in index command: {index_command!r}")
    return index_command[len(prefix) : i - 1]


def _parse_source_ref(source_ref: str) -> tuple[str, int] | None:
    source_ref = (source_ref or "").strip()
    if ":" not in source_ref:
        return None
    path_part, line_part = source_ref.rsplit(":", 1)
    if not line_part.isdigit():
        return None
    return path_part, int(line_part)


def _norm(text: str) -> str:
    return normalize_print_text((text or "").replace(r"\*", "*")).lower().strip()


def _contains_form(passage_text: str, display: str, form: str) -> bool:
    p = _norm(passage_text)
    return (_norm(display) in p) or (_norm(form) in p)


def _is_table_line(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|")


def _is_list_line(line: str) -> bool:
    return bool(re.match(r"\s*(?:[-*+]\s|\d+\.\s)", line))


def _is_heading_line(line: str) -> bool:
    return line.lstrip().startswith("#")


def _is_metadata_line(line: str) -> bool:
    return bool(re.match(r"^[A-Z][A-Z0-9_]+:\s", line.strip()))


def _build_code_fence_map(lines: list[str]) -> set[int]:
    in_fence = False
    fence_lines: set[int] = set()
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            fence_lines.add(i)
            continue
        if in_fence:
            fence_lines.add(i)
    return fence_lines


def resolve_source_passage(source_ref: str) -> tuple[SourcePassage | None, str]:
    parsed = _parse_source_ref(source_ref)
    if not parsed:
        return None, "malformed_source_ref"
    rel_path, line_no = parsed
    source_path = REPO_ROOT / rel_path
    if not source_path.exists():
        return None, "missing_file"
    lines = source_path.read_text(encoding="utf-8").splitlines()
    if line_no < 1 or line_no > len(lines):
        return None, "line_out_of_range"

    line = lines[line_no - 1]
    code_lines = _build_code_fence_map(lines)
    if line_no in code_lines:
        return None, "inside_fenced_code"
    if _is_heading_line(line):
        return None, "heading_target"
    if _is_metadata_line(line):
        return None, "metadata_target"
    if line.lstrip().startswith("\\"):
        return None, "raw_tex_target"
    if line.strip() == "":
        return None, "blank_line"

    if _is_table_line(line):
        start = line_no
        while start > 1 and _is_table_line(lines[start - 2]):
            start -= 1
        end = line_no
        while end < len(lines) and _is_table_line(lines[end]):
            end += 1
        block_text = "\n".join(lines[start - 1:end])
        return SourcePassage(rel_path, source_ref, "table", start, end, block_text), "ok"

    if _is_list_line(line):
        start = line_no
        while start > 1 and (_is_list_line(lines[start - 2]) or lines[start - 2].startswith("  ")):
            start -= 1
        end = line_no
        while end < len(lines) and (_is_list_line(lines[end]) or lines[end].startswith("  ")):
            end += 1
        block_text = "\n".join(lines[start - 1:end])
        return SourcePassage(rel_path, source_ref, "list", start, end, block_text), "ok"

    start = line_no
    while start > 1:
        prev = lines[start - 2]
        if (
            prev.strip() == ""
            or _is_heading_line(prev)
            or _is_table_line(prev)
            or _is_list_line(prev)
            or _is_metadata_line(prev)
        ):
            break
        start -= 1
    end = line_no
    while end < len(lines):
        nxt = lines[end]
        if (
            nxt.strip() == ""
            or _is_heading_line(nxt)
            or _is_table_line(nxt)
            or _is_list_line(nxt)
            or _is_metadata_line(nxt)
        ):
            break
        end += 1
    block_text = "\n".join(lines[start - 1:end])
    return SourcePassage(rel_path, source_ref, "paragraph", start, end, block_text), "ok"


def load_broad_prose_inventory() -> dict[str, object]:
    print_main = _load_rows(PRINT_MAIN_TSV)
    emission_table = _load_rows(EMISSION_TABLE_TSV)
    book_emissions = _load_rows(BOOK_EMISSIONS_TSV)
    broad_decisions = _load_rows(BROAD_DECISIONS_TSV)

    in_book_rows = [r for r in emission_table if (r.get("in_book") or "").strip() == "1"]
    by_occurrence = {
        (r.get("occurrence_id") or "").strip(): r
        for r in in_book_rows
        if (r.get("occurrence_id") or "").strip()
    }
    by_emission: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in in_book_rows:
        eid = (row.get("emission_id") or "").strip()
        if eid:
            by_emission[eid].append(row)

    be_by_emission_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in book_emissions:
        eid = (row.get("emission_id") or "").strip()
        if eid:
            be_by_emission_id[eid].append(row)

    broad_main_rows = [
        row
        for row in print_main
        if (row.get("source_scope") or "").strip() == "broad_prose_decision"
    ]
    broad_occurrence_ids = [
        (row.get("occurrence_id") or "").strip()
        for row in broad_main_rows
        if (row.get("occurrence_id") or "").strip()
    ]
    broad_occurrence_set = set(broad_occurrence_ids)

    broad_emission_ids = []
    for occ_id in broad_occurrence_ids:
        eid = (by_occurrence.get(occ_id, {}).get("emission_id") or "").strip()
        if eid:
            broad_emission_ids.append(eid)
    broad_emission_ids = list(dict.fromkeys(broad_emission_ids))

    plan_order = [
        (row.get("emission_id") or "").strip()
        for row in book_emissions
        if (row.get("emission_path") or "").strip() in {"heading_injection", "line_injection"}
    ]
    order_rank = {eid: i for i, eid in enumerate(plan_order)}
    broad_emission_ids.sort(key=lambda eid: order_rank.get(eid, 10**9))

    records: list[PlacementRecord] = []
    unresolved_reasons: Counter[str] = Counter()
    block_kind_counter: Counter[str] = Counter()

    for emission_id in broad_emission_ids:
        members = by_emission.get(emission_id, [])
        if not members:
            continue

        be_rows = be_by_emission_id.get(emission_id, [])
        if len(be_rows) != 1:
            raise ValueError(
                f"emission {emission_id}: expected exactly 1 book_emissions row, got {len(be_rows)}"
            )
        be = be_rows[0]
        be_rep_occurrence_id = (be.get("representative_occurrence_id") or "").strip()
        if not be_rep_occurrence_id:
            raise ValueError(f"emission {emission_id}: blank representative_occurrence_id in book_emissions")
        be_count_raw = (be.get("source_occurrence_count") or "").strip()
        try:
            be_count = int(be_count_raw)
        except ValueError as exc:
            raise ValueError(
                f"emission {emission_id}: invalid source_occurrence_count {be_count_raw!r}"
            ) from exc
        if be_count <= 0:
            raise ValueError(f"emission {emission_id}: source_occurrence_count must be positive, got {be_count}")
        be_occurrence_ids_raw = (be.get("source_occurrence_ids") or "").strip()
        if not be_occurrence_ids_raw:
            raise ValueError(f"emission {emission_id}: blank source_occurrence_ids in book_emissions")
        be_emission_path = (be.get("emission_path") or "").strip()
        if be_emission_path != "heading_injection":
            raise ValueError(
                f"emission {emission_id}: expected book_emissions emission_path heading_injection, got {be_emission_path!r}"
            )
        be_index_command = (be.get("index_command") or "").strip()
        if not be_index_command:
            raise ValueError(f"emission {emission_id}: blank index_command in book_emissions")

        be_occ_ids = {part.strip() for part in be_occurrence_ids_raw.split("|") if part.strip()}
        if not be_occ_ids:
            raise ValueError(f"emission {emission_id}: no source_occurrence_ids parsed from book_emissions")
        member_occ_ids = {(m.get("occurrence_id") or "").strip() for m in members}
        if member_occ_ids != be_occ_ids:
            raise ValueError(
                f"emission {emission_id}: member occurrence IDs {sorted(member_occ_ids)} != book_emissions IDs {sorted(be_occ_ids)}"
            )
        if len(members) != be_count:
            raise ValueError(
                f"emission {emission_id}: member count {len(members)} != source_occurrence_count {be_count}"
            )

        reps = [m for m in members if not (m.get("collapsed_into") or "").strip()]
        if not reps:
            raise ValueError(f"emission {emission_id}: no representative (zero collapsed_into=='' rows)")
        if len(reps) > 1:
            raise ValueError(f"emission {emission_id}: {len(reps)} representatives found (expected 1)")
        representative = reps[0]
        rep_occurrence_id = (representative.get("occurrence_id") or "").strip()
        if rep_occurrence_id != be_rep_occurrence_id:
            raise ValueError(
                f"emission {emission_id}: representative occurrence {rep_occurrence_id!r} != book_emissions representative {be_rep_occurrence_id!r}"
            )
        canonical_index_key = _extract_index_key(be_index_command)

        scopes = {(m.get("source_scope") or "").strip() for m in members}
        broad_members = [
            m for m in members if (m.get("source_scope") or "").strip() == "broad_prose_decision"
        ]

        rep_source_ref = (representative.get("source_ref") or "").strip()
        rep_display = (representative.get("display") or "").strip()
        rep_form = (representative.get("form") or "").strip()
        rep_sort = (representative.get("sort_key") or "").strip()

        group_class = GROUP_PURE_SINGLETON
        proposed_status = STATUS_PASSAGE_SHADOW
        note = ""

        if scopes != {"broad_prose_decision"}:
            group_class = GROUP_MIXED_SCOPE
            proposed_status = STATUS_RETAIN_MIXED
            note = f"mixed_scopes={sorted(scopes)}"
            rep_passage = None
        else:
            resolved_sites: set[tuple[str, int, int]] = set()
            failure_reason = ""
            for member in broad_members:
                source_ref = (member.get("source_ref") or "").strip()
                passage, reason = resolve_source_passage(source_ref)
                if passage is None:
                    failure_reason = reason
                    break
                if not _contains_form(
                    passage.block_text,
                    (member.get("display") or ""),
                    (member.get("form") or ""),
                ):
                    failure_reason = "representative_form_absent"
                    break
                resolved_sites.add((passage.source_path, passage.start_line, passage.end_line))
            rep_passage, rep_reason = resolve_source_passage(rep_source_ref)
            if failure_reason:
                group_class = GROUP_UNRESOLVED
                proposed_status = STATUS_RETAIN_UNRESOLVED
                note = failure_reason
                unresolved_reasons[failure_reason] += 1
            elif rep_passage is None:
                group_class = GROUP_UNRESOLVED
                proposed_status = STATUS_RETAIN_UNRESOLVED
                note = rep_reason
                unresolved_reasons[rep_reason] += 1
            elif not _contains_form(rep_passage.block_text, rep_display, rep_form):
                group_class = GROUP_UNRESOLVED
                proposed_status = STATUS_RETAIN_UNRESOLVED
                note = "representative_form_absent"
                unresolved_reasons["representative_form_absent"] += 1
            else:
                block_kind_counter[rep_passage.block_kind] += 1
                if len(broad_members) == 1:
                    group_class = GROUP_PURE_SINGLETON
                elif len(resolved_sites) == 1:
                    group_class = GROUP_PURE_SHARED_ONE
                else:
                    group_class = GROUP_PURE_SHARED_MULTI

        record = PlacementRecord(
            emission_id=emission_id,
            representative_occurrence_id=be_rep_occurrence_id,
            representative_source_ref=rep_source_ref,
            representative_display=rep_display,
            representative_form=rep_form,
            representative_sort_key=rep_sort,
            current_emission_path=be_emission_path,
            current_site=(be.get("site") or "").strip(),
            group_class=group_class,
            proposed_status=proposed_status,
            resolved_block_kind=(rep_passage.block_kind if proposed_status == STATUS_PASSAGE_SHADOW and rep_passage else ""),
            resolved_block_start_line=(rep_passage.start_line if proposed_status == STATUS_PASSAGE_SHADOW and rep_passage else 0),
            resolved_block_end_line=(rep_passage.end_line if proposed_status == STATUS_PASSAGE_SHADOW and rep_passage else 0),
            note=note,
            canonical_index_key=canonical_index_key,
        )
        records.append(record)

    accepted_rows = [
        row for row in broad_decisions if (row.get("action") or "").strip() == "accept"
    ]

    decision_state_counts, decision_state_records = classify_broad_decision_states(accepted_rows)

    summary = {
        "accepted_broad_prose_decision_rows": len(accepted_rows),
        "matching_print_main_occurrences": len(broad_main_rows),
        "distinct_broad_occurrence_ids": len(broad_occurrence_set),
        "distinct_containing_emission_ids": len(broad_emission_ids),
        "group_classes": dict(Counter(r.group_class for r in records)),
        "proposed_status": dict(Counter(r.proposed_status for r in records)),
        "source_files_involved": len(
            {(row.get("source_ref") or "").split(":")[0] for row in broad_main_rows if row.get("source_ref")}
        ),
        "source_references_involved": len(
            {(row.get("source_ref") or "") for row in broad_main_rows if row.get("source_ref")}
        ),
        "resolved_block_kinds": dict(block_kind_counter),
        "unresolved_reasons": dict(unresolved_reasons),
        "decision_state_counts": decision_state_counts,
    }

    return {
        "summary": summary,
        "records": records,
        "decision_state_records": decision_state_records,
        "movable_emission_ids": [r.emission_id for r in records if r.proposed_status == STATUS_PASSAGE_SHADOW],
        "retained_mixed_emission_ids": [r.emission_id for r in records if r.proposed_status == STATUS_RETAIN_MIXED],
        "retained_unresolved_emission_ids": [r.emission_id for r in records if r.proposed_status == STATUS_RETAIN_UNRESOLVED],
    }


def build_passage_anchor_requests(records: list[PlacementRecord]) -> list[dict]:
    """Return per-emission anchor placement requests carrying exact block coordinates.

    Block coordinates (block_start_line, block_end_line) come from the resolved
    SourcePassage so that placement is determined by source location, not by
    searching for form text in the rendered output.
    """
    requests: list[dict] = []
    for record in records:
        if record.proposed_status != STATUS_PASSAGE_SHADOW:
            continue
        parsed = _parse_source_ref(record.representative_source_ref)
        if not parsed:
            continue
        rel_path, _ = parsed
        # Reconstruct the full relative source path (rel_path includes the file path only).
        # resolved_block_start/end_line come from the PlacementRecord (set during inventory).
        requests.append(
            {
                "emission_id": record.emission_id,
                "representative_occurrence_id": record.representative_occurrence_id,
                "representative_source_ref": record.representative_source_ref,
                "source_path": rel_path,
                "block_start_line": record.resolved_block_start_line,
                "block_end_line": record.resolved_block_end_line,
                "representative_form": record.representative_form,
                "representative_display": record.representative_display,
            }
        )
    return requests


def classify_broad_decision_states(
    accepted_rows: list[dict[str, str]],
) -> tuple[dict[str, int], list[dict[str, str]]]:
    """Classify each accepted broad-prose decision row by its current print state."""
    print_main_rows = _load_rows(PRINT_MAIN_TSV)
    broad_main_set: set[tuple[str, str, str, str, str]] = {
        (
            (r.get("source_ref") or "").strip(),
            (r.get("form") or "").strip(),
            (r.get("language") or "").strip(),
            (r.get("variety") or "").strip(),
            (r.get("form_role") or "").strip(),
        )
        for r in print_main_rows
        if (r.get("source_scope") or "").strip() == "broad_prose_decision"
    }

    excluded_set: set[tuple[str, str, str, str, str]] = set()
    if PRINT_EXCLUDED_TSV.exists():
        excluded_rows = _load_rows(PRINT_EXCLUDED_TSV)
        excluded_set = {
            (
                (r.get("source_ref") or "").strip(),
                (r.get("form") or "").strip(),
                (r.get("language") or "").strip(),
                (r.get("variety") or "").strip(),
                (r.get("form_role") or "").strip(),
            )
            for r in excluded_rows
            if (r.get("source_scope") or "").strip() == "broad_prose_decision"
        }

    counts = {"active_print_main": 0, "active_print_excluded": 0, "stale_no_current_candidate": 0}
    classification_records: list[dict[str, str]] = []
    for row in accepted_rows:
        key = (
            (row.get("source_ref") or "").strip(),
            (row.get("form") or "").strip(),
            (row.get("language") or "").strip(),
            (row.get("variety") or "").strip(),
            (row.get("form_role") or "").strip(),
        )
        if key in broad_main_set:
            state = "active_print_main"
        elif key in excluded_set:
            state = "active_print_excluded"
        else:
            state = "stale_no_current_candidate"
        counts[state] += 1
        classification_records.append(
            {
                "source_ref": key[0],
                "form": key[1],
                "language": key[2],
                "variety": key[3],
                "form_role": key[4],
                "action": (row.get("action") or "").strip(),
                "state": state,
            }
        )
    return counts, classification_records


def write_report(path: Path, records: list[PlacementRecord]) -> None:
    fieldnames = [
        "emission_id",
        "representative_occurrence_id",
        "representative_source_ref",
        "representative_display",
        "representative_form",
        "representative_sort_key",
        "current_emission_path",
        "current_site",
        "group_class",
        "proposed_status",
        "resolved_block_kind",
        "resolved_block_start_line",
        "resolved_block_end_line",
        "note",
        "canonical_index_key",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        for record in records:
            writer.writerow({name: getattr(record, name) for name in fieldnames})


def cli() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Optional TSV report output path")
    args = parser.parse_args()

    inventory = load_broad_prose_inventory()
    summary = inventory["summary"]
    print("broad prose placement inventory:")
    for key in (
        "accepted_broad_prose_decision_rows",
        "matching_print_main_occurrences",
        "distinct_broad_occurrence_ids",
        "distinct_containing_emission_ids",
        "source_files_involved",
        "source_references_involved",
    ):
        print(f"  {key}: {summary.get(key)}")
    print(f"  group_classes: {summary.get('group_classes')}")
    print(f"  proposed_status: {summary.get('proposed_status')}")
    print(f"  resolved_block_kinds: {summary.get('resolved_block_kinds')}")
    if summary.get("unresolved_reasons"):
        print(f"  unresolved_reasons: {summary.get('unresolved_reasons')}")

    if args.report:
        write_report(args.report, inventory["records"])
        print(f"wrote report: {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
