#!/usr/bin/env python3
"""index_verborum_emission.py — Central emission-planning module.

This module owns:
  * occurrence-ID construction
  * book-inclusion classification (corpus-wide vs. book-specific)
  * canonical index-command generation
  * emission-table record construction
  * book_main and book_print_unique TSV generation

Every other module (builder, assembler, checker, tests) must import
from here rather than duplicating this logic.

Occurrence-ID format
--------------------
  <source_ref>:<ordinal>

where:
  source_ref  = canonical path:line (e.g. "Germanic/.../entry.model.md:21")
                or heading string (e.g. "bake — OE bacan")
                or structured field tag (e.g. "lexical_heading:bake—OEbacan")
  ordinal     = 1-based integer, disambiguating multiple identical occurrences
                at the same source location

For the first (and usually only) occurrence at a location, ordinal=1.

Book-inclusion classification
------------------------------
A printable row belongs to the assembled book if its source material is
represented in capr_book_draft_alpha_01:

  * explicit_tag rows: included if their source_ref path is in the set of
    paths assembled into the book (model entries in the manifest, intro,
    chronology)
  * heading/line injection rows: included if their injection site resolves
    to a known heading in the assembled book
  * rows with source_ref = heading string: included iff that string appears
    as a lexical heading in the assembled book (i.e. the model entry is in
    the manifest)

Corpus-wide print_main rows whose sources are NOT in the assembled book
are classified as source_not_in_book. They are valid corpus-wide printable
occurrences but must not be checked against the assembled book's index.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import NamedTuple

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "docs" / "assembly"))

import index_verborum_render as ivr
from build_full_lexical_volume import normalize_print_text as npt

# ── File paths ────────────────────────────────────────────────────────────────
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
MANIFEST_PATH = ASSEMBLY_DIR / "manifest_all_by_class.tsv"
PRINT_MAIN_PATH = BOOK_DIR / "index_verborum_print_main.tsv"
BOOK_MAIN_PATH = BOOK_DIR / "index_verborum_book_main.tsv"
BOOK_PRINT_UNIQUE_PATH = BOOK_DIR / "index_verborum_book_print_unique.tsv"
EMISSION_TABLE_PATH = BOOK_DIR / "index_verborum_emission_table.tsv"
INTRO_PATH = ASSEMBLY_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = (
    REPO_ROOT
    / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
)

_LINE_INJ_SCOPES = frozenset(
    {"table_semantic_auto", "table_semantic_decision", "broad_prose_decision"}
)

# ── Language / variety registries ─────────────────────────────────────────────
_LANG_META: dict | None = None
_VAR_REG: object | None = None


def _lang_meta() -> dict:
    global _LANG_META
    if _LANG_META is None:
        _LANG_META = ivr.load_language_registry()
    return _LANG_META


def _var_reg() -> object:
    global _VAR_REG
    if _VAR_REG is None:
        _VAR_REG = ivr.load_variety_registry()
    return _VAR_REG


# ── Occurrence ID ─────────────────────────────────────────────────────────────

def make_occurrence_id(source_ref: str, ordinal: int = 1) -> str:
    """Construct a stable occurrence ID from source_ref + ordinal.

    The ID distinguishes separate visible spans even when all semantic
    fields (language, form, display, role, variety) and source line are
    identical. The ordinal (1-based) counts identical identities at the
    same source location.

    Ordinal=1 is the only value for the vast majority of occurrences.
    """
    return f"{source_ref}:{ordinal}"


def parse_occurrence_id(occ_id: str) -> tuple[str, int]:
    """Split an occurrence ID back into (source_ref, ordinal)."""
    last_colon = occ_id.rfind(":")
    if last_colon < 0:
        return occ_id, 1
    suffix = occ_id[last_colon + 1 :]
    if suffix.isdigit():
        return occ_id[:last_colon], int(suffix)
    return occ_id, 1


# ── Model-entry heading map ────────────────────────────────────────────────────

def load_model_entry_headings() -> dict[str, str]:
    """Return {model_entry_path → heading_string} from the manifest."""
    headings: dict[str, str] = {}
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            mp = (row.get("model_entry_path") or "").strip()
            li = (row.get("lexical_item") or "").strip()
            ct = (row.get("counterpart") or "").strip()
            dc = (row.get("derivation_class") or "").strip()
            if mp and li:
                headings[mp] = f"{li} — OE {'*' + ct if dc == 'reconstructed_oe' else ct}"
    return headings


# ── Book-inclusion classification ─────────────────────────────────────────────

class EmissionClassification(NamedTuple):
    """Result of classifying one print_main row's emission path."""

    emission_path: str   # "explicit_tag" | "heading_injection" | "line_injection" | "source_not_in_book"
    site: str            # heading string or "path:line"
    index_command: str
    in_book: bool        # True if the source material is in the assembled book


def classify_emission(
    row: dict[str, str],
    model_entry_headings: dict[str, str],
) -> EmissionClassification:
    """Classify one print_main row and return its emission path, site, and command."""
    scope = (row.get("source_scope") or "").strip()
    ref = (row.get("source_ref") or "").strip()
    cmd = make_index_command(row)
    manifest_heading_set = set(model_entry_headings.values())

    book_paths = {
        INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
        CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
        *model_entry_headings.keys(),
    }
    book_headings = manifest_heading_set

    if scope == "explicit_tag":
        path_part = ref.rsplit(":", 1)[0] if ":" in ref else ref
        in_book = path_part in book_paths
        return EmissionClassification("explicit_tag", ref, cmd, in_book)

    if not ref:
        return EmissionClassification("source_not_in_book", ref, cmd, False)

    if ".md:" in ref:
        path_part, line_part = ref.rsplit(":", 1)
        if scope in _LINE_INJ_SCOPES and line_part.isdigit() and path_part not in model_entry_headings:
            in_book = path_part in {
                INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
                CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
            }
            return EmissionClassification("line_injection", f"{path_part}:{line_part}", cmd, in_book)
        if path_part in model_entry_headings:
            heading = model_entry_headings[path_part]
            return EmissionClassification("heading_injection", heading, cmd, True)
        if line_part.isdigit():
            in_book = path_part in book_paths
            return EmissionClassification("line_injection", f"{path_part}:{line_part}", cmd, in_book)
        return EmissionClassification("source_not_in_book", ref, cmd, False)

    # Heading string ref (no ".md:")
    in_book = ref in book_headings
    if in_book:
        return EmissionClassification("heading_injection", ref, cmd, True)
    return EmissionClassification("source_not_in_book", ref, cmd, False)


# ── Index command generation ───────────────────────────────────────────────────

def make_index_command(row: dict[str, str]) -> str:
    """Generate the canonical \\index[iv]{...} command for a print_main row."""
    return ivr.index_command(
        row.get("language", ""),
        row.get("sort_key", ""),
        npt(row.get("display", "")),
        (row.get("variety") or "").strip(),
        lang_meta=_lang_meta(),
        var_registry=_var_reg(),
    )


# ── Emission table ─────────────────────────────────────────────────────────────

_EMISSION_TABLE_FIELDS = [
    "occurrence_id",
    "source_ref",
    "ordinal",
    "source_scope",
    "emission_path",
    "site",
    "in_book",
    "language",
    "variety",
    "form",
    "display",
    "sort_key",
    "form_role",
    "index_command",
]


def build_emission_table(
    main_rows: list[dict[str, str]],
    model_entry_headings: dict[str, str],
) -> list[dict[str, str]]:
    """Produce a full emission table from print_main rows.

    Each row gets an occurrence_id = source_ref:ordinal, where ordinal
    distinguishes rows that share the same source_ref but differ in their
    semantic identity within the same source location.
    """
    # Ordinal counter: count ALL occurrences at each source_ref regardless
    # of semantic identity.  This guarantees globally unique occurrence IDs
    # because each (source_ref, ordinal) pair is unique.
    ordinal_counter: Counter[str] = Counter()
    records: list[dict[str, str]] = []

    for row in main_rows:
        ref = (row.get("source_ref") or "").strip()
        ordinal_counter[ref] += 1
        ordinal = ordinal_counter[ref]
        occ_id = make_occurrence_id(ref, ordinal)

        ec = classify_emission(row, model_entry_headings)
        records.append(
            {
                "occurrence_id": occ_id,
                "source_ref": ref,
                "ordinal": str(ordinal),
                "source_scope": (row.get("source_scope") or "").strip(),
                "emission_path": ec.emission_path,
                "site": ec.site,
                "in_book": "1" if ec.in_book else "0",
                "language": row.get("language", ""),
                "variety": row.get("variety", ""),
                "form": row.get("form", ""),
                "display": row.get("display", ""),
                "sort_key": row.get("sort_key", ""),
                "form_role": row.get("form_role", ""),
                "index_command": ec.index_command,
            }
        )

    return records


def write_emission_table(records: list[dict[str, str]], path: Path = EMISSION_TABLE_PATH) -> None:
    """Write the emission table to a TSV file (LF line endings)."""
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=_EMISSION_TABLE_FIELDS, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(records)


def load_emission_table(path: Path = EMISSION_TABLE_PATH) -> list[dict[str, str]]:
    """Load the emission table from disk."""
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


# ── Book-main view ─────────────────────────────────────────────────────────────

def book_main_rows(
    main_rows: list[dict[str, str]] | None = None,
    model_entry_headings: dict[str, str] | None = None,
) -> list[dict[str, str]]:
    """Return the subset of print_main rows whose sources are in the assembled book."""
    if main_rows is None:
        main_rows = list(
            csv.DictReader(PRINT_MAIN_PATH.open(encoding="utf-8"), delimiter="\t")
        )
    if model_entry_headings is None:
        model_entry_headings = load_model_entry_headings()

    result: list[dict[str, str]] = []
    # For heading/line injection: deduplicate per site+cmd (same as builder)
    seen_sites: set[tuple[str, str]] = set()

    for row in main_rows:
        ec = classify_emission(row, model_entry_headings)
        if not ec.in_book:
            continue
        if ec.emission_path == "explicit_tag":
            result.append(row)
        elif ec.emission_path in ("heading_injection", "line_injection"):
            key = (ec.site, ec.index_command)
            if key not in seen_sites:
                seen_sites.add(key)
                result.append(row)
            # else: collapsed_same_site → not separately represented in book_main
        # source_not_in_book: excluded

    return result


# ── Collision checks ───────────────────────────────────────────────────────────

def check_no_occurrence_id_collisions(records: list[dict[str, str]]) -> None:
    """Assert that every record in the emission table has a unique occurrence_id."""
    seen: Counter[str] = Counter(r["occurrence_id"] for r in records)
    dupes = {k: v for k, v in seen.items() if v > 1}
    assert not dupes, (
        f"Emission table has {len(dupes)} duplicate occurrence_ids:\n"
        + "\n".join(f"  {k}: {v}" for k, v in sorted(dupes.items())[:5])
    )


def check_sortkey_fallback_no_collision(sortkey_tsv_path: Path) -> None:
    """Assert that the sort-key fallback has no key → multiple distinct forms."""
    if not sortkey_tsv_path.exists():
        return
    from collections import defaultdict
    key_to_forms: defaultdict[tuple, set] = defaultdict(set)
    with sortkey_tsv_path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            key = (
                (row.get("language") or "").strip(),
                (row.get("form_role") or "").strip(),
                (row.get("sort_key") or "").strip(),
                (row.get("source_ref") or "").strip(),
                (row.get("variety") or "").strip(),
            )
            key_to_forms[key].add((row.get("form", ""), row.get("display", "")))
    collisions = {k: v for k, v in key_to_forms.items() if len(v) > 1}
    assert not collisions, (
        f"Sort-key allowlist has {len(collisions)} key(s) mapping to multiple "
        f"distinct form/display values — fallback would admit wrong occurrence:\n"
        + "\n".join(f"  {k}: {sorted(v)}" for k, v in sorted(collisions.items())[:3])
    )


# ── Utility: load print_main ───────────────────────────────────────────────────

def load_print_main() -> list[dict[str, str]]:
    return list(csv.DictReader(PRINT_MAIN_PATH.open(encoding="utf-8"), delimiter="\t"))


# ── CLI entry point ────────────────────────────────────────────────────────────

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-book-main", action="store_true")
    parser.add_argument("--write-emission-table", action="store_true")
    parser.add_argument("--check-collisions", action="store_true")
    args = parser.parse_args()

    main_rows = load_print_main()
    mehmap = load_model_entry_headings()

    if args.write_book_main or args.write_emission_table:
        et = build_emission_table(main_rows, mehmap)
        if args.write_emission_table:
            write_emission_table(et)
            print(f"Wrote {len(et)} rows to {EMISSION_TABLE_PATH}")
        if args.write_book_main:
            bm = book_main_rows(main_rows, mehmap)
            fields = list(main_rows[0].keys()) if main_rows else []
            with BOOK_MAIN_PATH.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
                writer.writeheader()
                writer.writerows(bm)
            print(f"Wrote {len(bm)} rows to {BOOK_MAIN_PATH}")

    if args.check_collisions:
        et = build_emission_table(main_rows, mehmap)
        check_no_occurrence_id_collisions(et)
        sortkey_path = BOOK_DIR / "index_verborum_explicit_allow_sortkey.tsv"
        check_sortkey_fallback_no_collision(sortkey_path)
        print("No emission-table collisions. No sort-key fallback collisions.")


if __name__ == "__main__":
    main()
