#!/usr/bin/env python3
"""Canonical explicit-span plan builder and validator.

Stage 3B contract:
  * every visible explicit .iv occurrence in assembled book has one row
  * row disposition is explicit: emit or suppress
  * emit rows join exactly to explicit_tag book emissions
  * suppress rows join exactly to explicit_tag print-excluded rows
"""
from __future__ import annotations

import csv
import io
import re
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
MANIFEST_PATH = ASSEMBLY_DIR / "manifest_all_by_class.tsv"
INTRO_PATH = ASSEMBLY_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = (
    REPO_ROOT
    / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
)

DEFAULT_FORMS_PATH = BOOK_DIR / "index_verborum_forms.tsv"
DEFAULT_PRINT_MAIN_PATH = BOOK_DIR / "index_verborum_print_main.tsv"
DEFAULT_PRINT_EXCLUDED_PATH = BOOK_DIR / "index_verborum_print_excluded.tsv"
DEFAULT_BOOK_EMISSIONS_PATH = BOOK_DIR / "index_verborum_book_emissions.tsv"
DEFAULT_BOOK_MD = ASSEMBLY_DIR / "capr_book_draft_alpha_01.md"
DEFAULT_EXPLICIT_PLAN_PATH = BOOK_DIR / "index_verborum_book_explicit_plan.tsv"

EXPECTED_TOTAL = 1496
EXPECTED_EMIT = 1417
EXPECTED_SUPPRESS = 79

EXPLICIT_PLAN_FIELDS = [
    "occurrence_id",
    "disposition",
    "emission_id",
    "index_command",
    "exclusion_reason",
    "language",
    "variety",
    "form",
    "display",
    "sort_key",
    "form_role",
    "source_scope",
    "source_ref",
]

EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{(?P<attrs>[^}]*)\}")
NESTED_RECON_IV_RE = re.compile(r"\[\[(?P<form>[^\]]+)\]\{\.recon\}(?P<tail>.*?)\]\{(?P<attrs>[^}]*)\}")


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def parse_attr_string(raw: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for key, value in re.findall(r'([A-Za-z0-9_:-]+)\s*=\s*"([^"]*)"', raw):
        attrs[key] = value
    for key, value in re.findall(r"([A-Za-z0-9_:-]+)\s*=\s*([^\s}]+)", raw):
        attrs.setdefault(key, value)
    return attrs


def has_tag_class(raw_attrs: str, cls: str) -> bool:
    return re.search(rf"(^|\s)\.{re.escape(cls)}(?=\s|$)", raw_attrs) is not None


def normalize_form(text: str) -> str:
    value = text.strip()
    if value.startswith("`") and value.endswith("`"):
        value = value[1:-1]
    if value.startswith("_") and value.endswith("_") and len(value) > 2:
        value = value[1:-1]
    value = value.replace(r"\*", "*")
    if value.startswith("*") and value.endswith("*") and len(value) > 2:
        value = value[1:-1]
    return value.strip()


def normalize_display(text: str) -> str:
    value = text.strip()
    if value.startswith("_") and value.endswith("_") and len(value) > 2:
        value = value[1:-1]
    if value.startswith("`") and value.endswith("`") and len(value) > 2:
        value = value[1:-1]
    value = re.sub(r"(\*[^`\s|<>]*-?)\*$", r"\1", value)
    return value.strip()


def scan_explicit_spans(markdown_text: str) -> list[dict[str, str]]:
    """Parse explicit .iv/.pred spans in assembled-book order."""
    rows: list[dict[str, str]] = []
    for line_no, line in enumerate(markdown_text.splitlines(), start=1):
        line_counter = 0
        nested_spans = [(m.start(), m.end()) for m in NESTED_RECON_IV_RE.finditer(line)]
        for m in NESTED_RECON_IV_RE.finditer(line):
            attrs_raw = m.group("attrs")
            if not (has_tag_class(attrs_raw, "iv") or has_tag_class(attrs_raw, "pred")):
                continue
            line_counter += 1
            attrs = parse_attr_string(attrs_raw)
            rows.append(
                {
                    "occurrence_id": (attrs.get("occ_id") or "").strip(),
                    "source_ref": (attrs.get("source_ref") or "").strip(),
                    "language": (attrs.get("lang") or "").strip(),
                    "form_role": (attrs.get("role") or "evidence_form").strip(),
                    "variety": (attrs.get("variety") or "").strip(),
                    "sort_key": (attrs.get("sort") or normalize_form(m.group("form"))).strip(),
                    "display": normalize_display((attrs.get("display") or f"*{normalize_form(m.group('form'))}").strip()),
                    "normalized_visible_form": normalize_form(m.group("form")),
                    "reconstruction_status": "1",
                    "span_class": "pred" if has_tag_class(attrs_raw, "pred") else "iv",
                    "line_span_ordinal": str(line_counter),
                    "line_no": str(line_no),
                }
            )
        scrubbed = list(line)
        for s, e in nested_spans:
            for i in range(s, e):
                scrubbed[i] = " "
        scrubbed_line = "".join(scrubbed)
        for m in EXPLICIT_TAG_RE.finditer(scrubbed_line):
            attrs_raw = m.group("attrs")
            if not (has_tag_class(attrs_raw, "iv") or has_tag_class(attrs_raw, "pred")):
                continue
            line_counter += 1
            attrs = parse_attr_string(attrs_raw)
            content = normalize_form(m.group("content"))
            is_recon = has_tag_class(attrs_raw, "recon")
            rows.append(
                {
                    "occurrence_id": (attrs.get("occ_id") or "").strip(),
                    "source_ref": (attrs.get("source_ref") or "").strip(),
                    "language": (attrs.get("lang") or "").strip(),
                    "form_role": (attrs.get("role") or "evidence_form").strip(),
                    "variety": (attrs.get("variety") or "").strip(),
                    "sort_key": (attrs.get("sort") or content).strip(),
                    "display": normalize_display((attrs.get("display") or (f"*{content}" if is_recon else content)).strip()),
                    "normalized_visible_form": content,
                    "reconstruction_status": "1" if is_recon else "0",
                    "span_class": "pred" if has_tag_class(attrs_raw, "pred") else "iv",
                    "line_span_ordinal": str(line_counter),
                    "line_no": str(line_no),
                }
            )
    return rows


def load_model_entry_headings(path: Path = MANIFEST_PATH) -> dict[str, str]:
    headings: dict[str, str] = {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            mp = (row.get("model_entry_path") or "").strip()
            li = (row.get("lexical_item") or "").strip()
            ct = (row.get("counterpart") or "").strip()
            dc = (row.get("derivation_class") or "").strip()
            if mp and li:
                headings[mp] = f"{li} — OE {'*' + ct if dc == 'reconstructed_oe' else ct}"
    return headings


def book_source_paths() -> set[str]:
    headings = load_model_entry_headings()
    return {
        INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
        CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
        *headings.keys(),
    }


def explicit_in_book(rows: list[dict[str, str]], valid_paths: set[str]) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        if (row.get("source_scope") or "").strip() != "explicit_tag":
            continue
        occ_id = (row.get("occurrence_id") or "").strip()
        source_ref = (row.get("source_ref") or "").strip()
        if not occ_id or not source_ref:
            continue
        path_part = source_ref.rsplit(":", 1)[0] if ":" in source_ref else source_ref
        if path_part not in valid_paths:
            continue
        out[occ_id] = row
    return out


def _tsv_text(rows: list[dict[str, str]], fieldnames: list[str]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def build_explicit_plan(
    *,
    forms_rows: list[dict[str, str]],
    print_main_rows: list[dict[str, str]],
    print_excluded_rows: list[dict[str, str]],
    book_emission_rows: list[dict[str, str]],
    book_markdown_text: str,
) -> list[dict[str, str]]:
    """Build ordered explicit plan rows by assembled-book explicit span order."""
    valid_paths = book_source_paths()
    in_book_forms = explicit_in_book(forms_rows, valid_paths)
    in_book_main = explicit_in_book(print_main_rows, valid_paths)
    in_book_excluded = explicit_in_book(print_excluded_rows, valid_paths)

    emit_ids = set(in_book_main)
    suppress_ids = set(in_book_excluded)
    all_expected = set(in_book_forms)
    if emit_ids | suppress_ids != all_expected:
        raise AssertionError("in-book explicit IDs must partition into emit and suppress")
    if emit_ids & suppress_ids:
        raise AssertionError("emit/suppress explicit IDs overlap")

    explicit_em_by_occ: dict[str, dict[str, str]] = {}
    for row in book_emission_rows:
        if (row.get("emission_path") or "").strip() != "explicit_tag":
            continue
        rep = (row.get("representative_occurrence_id") or "").strip()
        if rep:
            explicit_em_by_occ[rep] = row

    suppressed_reason_by_occ: dict[str, str] = {}
    for row in print_excluded_rows:
        if (row.get("source_scope") or "").strip() != "explicit_tag":
            continue
        occ = (row.get("occurrence_id") or "").strip()
        if occ in suppress_ids:
            suppressed_reason_by_occ[occ] = (row.get("exclusion_reason") or "").strip()

    spans = [
        s
        for s in scan_explicit_spans(book_markdown_text)
        if s["span_class"] == "iv"
    ]
    occ_ids = [s["occurrence_id"] for s in spans]
    if any(not oid for oid in occ_ids):
        raise AssertionError("assembled explicit span missing occ_id")
    if len(set(occ_ids)) != len(occ_ids):
        dup = [k for k, v in Counter(occ_ids).items() if v > 1][:5]
        raise AssertionError(f"duplicate assembled explicit occ_id(s): {dup}")
    unknown = [oid for oid in occ_ids if oid not in all_expected]
    missing = [oid for oid in all_expected if oid not in set(occ_ids)]
    if unknown:
        raise AssertionError(f"assembled explicit unknown occ_id(s): {unknown[:5]}")
    if missing:
        raise AssertionError(f"assembled explicit missing occ_id(s): {missing[:5]}")

    rows: list[dict[str, str]] = []
    for span in spans:
        occ_id = span["occurrence_id"]
        frow = in_book_forms[occ_id]
        base = {
            "occurrence_id": occ_id,
            "language": (frow.get("language") or "").strip(),
            "variety": (frow.get("variety") or "").strip(),
            "form": (frow.get("form") or "").strip(),
            "display": (frow.get("display") or "").strip(),
            "sort_key": (frow.get("sort_key") or "").strip(),
            "form_role": (frow.get("form_role") or "").strip(),
            "source_scope": (frow.get("source_scope") or "").strip(),
            "source_ref": (frow.get("source_ref") or "").strip(),
        }
        if occ_id in emit_ids:
            em = explicit_em_by_occ.get(occ_id)
            if em is None:
                raise AssertionError(f"emit occurrence has no explicit_tag emission row: {occ_id}")
            emission_id = (em.get("emission_id") or "").strip()
            if emission_id != occ_id:
                raise AssertionError(
                    f"emit occurrence emission_id mismatch: occurrence_id={occ_id} emission_id={emission_id!r}"
                )
            rows.append(
                {
                    **base,
                    "disposition": "emit",
                    "emission_id": emission_id,
                    "index_command": (em.get("index_command") or "").strip(),
                    "exclusion_reason": "",
                }
            )
        elif occ_id in suppress_ids:
            reason = suppressed_reason_by_occ.get(occ_id, "")
            rows.append(
                {
                    **base,
                    "disposition": "suppress",
                    "emission_id": "",
                    "index_command": "",
                    "exclusion_reason": reason,
                }
            )
        else:
            raise AssertionError(f"occurrence {occ_id} is neither emit nor suppress")
    return rows


def validate_explicit_plan(
    plan_rows: list[dict[str, str]],
    *,
    forms_rows: list[dict[str, str]],
    print_main_rows: list[dict[str, str]],
    print_excluded_rows: list[dict[str, str]],
    book_emission_rows: list[dict[str, str]],
    book_markdown_text: str,
) -> None:
    valid_paths = book_source_paths()
    in_book_forms = explicit_in_book(forms_rows, valid_paths)
    in_book_main = explicit_in_book(print_main_rows, valid_paths)
    in_book_excluded = explicit_in_book(print_excluded_rows, valid_paths)
    expected_emit = set(in_book_main)
    expected_suppress = set(in_book_excluded)
    expected_all = set(in_book_forms)

    if len(plan_rows) != EXPECTED_TOTAL:
        raise AssertionError(f"explicit plan row count {len(plan_rows)} != {EXPECTED_TOTAL}")

    counts = Counter((r.get("disposition") or "").strip() for r in plan_rows)
    if counts.get("emit", 0) != EXPECTED_EMIT:
        raise AssertionError(f"explicit plan emit count {counts.get('emit', 0)} != {EXPECTED_EMIT}")
    if counts.get("suppress", 0) != EXPECTED_SUPPRESS:
        raise AssertionError(f"explicit plan suppress count {counts.get('suppress', 0)} != {EXPECTED_SUPPRESS}")
    unsupported = [k for k in counts if k not in {"emit", "suppress"}]
    if unsupported:
        raise AssertionError(f"explicit plan has unsupported dispositions: {unsupported}")

    occ_ids = [(r.get("occurrence_id") or "").strip() for r in plan_rows]
    if any(not oid for oid in occ_ids):
        raise AssertionError("explicit plan has blank occurrence_id")
    dup = [k for k, v in Counter(occ_ids).items() if v > 1]
    if dup:
        raise AssertionError(f"duplicate explicit plan occurrence_id(s): {dup[:5]}")

    spans = [
        s
        for s in scan_explicit_spans(book_markdown_text)
        if s["span_class"] == "iv"
    ]
    assembled_occ = [s["occurrence_id"] for s in spans]
    if occ_ids != assembled_occ:
        raise AssertionError("explicit plan row order must equal assembled explicit span order")
    if set(occ_ids) != expected_all:
        raise AssertionError("explicit plan occurrence coverage does not equal in-book explicit occurrence set")

    by_emission = {(r.get("emission_id") or "").strip(): r for r in book_emission_rows if (r.get("emission_id") or "").strip()}
    excluded_by_occ = {
        (r.get("occurrence_id") or "").strip(): r
        for r in print_excluded_rows
        if (r.get("source_scope") or "").strip() == "explicit_tag"
    }
    emitted_occ_set = set()
    suppressed_occ_set = set()
    seen_emit_emission_ids: set[str] = set()

    for row in plan_rows:
        occ = (row.get("occurrence_id") or "").strip()
        disp = (row.get("disposition") or "").strip()
        emission_id = (row.get("emission_id") or "").strip()
        idx_cmd = (row.get("index_command") or "").strip()
        reason = (row.get("exclusion_reason") or "").strip()
        scope = (row.get("source_scope") or "").strip()
        if scope != "explicit_tag":
            raise AssertionError(f"plan row has non-explicit source_scope: {occ} -> {scope!r}")

        frow = in_book_forms.get(occ)
        if frow is None:
            raise AssertionError(f"plan occurrence not in in-book forms set: {occ}")
        for key in ("language", "variety", "form", "display", "sort_key", "form_role", "source_ref"):
            if (row.get(key) or "").strip() != (frow.get(key) or "").strip():
                raise AssertionError(
                    f"plan semantic field mismatch for {occ} key={key}: "
                    f"plan={(row.get(key) or '').strip()!r} forms={(frow.get(key) or '').strip()!r}"
                )

        if disp == "emit":
            emitted_occ_set.add(occ)
            if not emission_id:
                raise AssertionError(f"emit row has blank emission_id: {occ}")
            if emission_id != occ:
                raise AssertionError(f"emit row emission_id must equal occurrence_id: {occ} -> {emission_id}")
            if emission_id in seen_emit_emission_ids:
                raise AssertionError(f"duplicate emit emission_id in explicit plan: {emission_id}")
            seen_emit_emission_ids.add(emission_id)
            if not idx_cmd:
                raise AssertionError(f"emit row has blank index_command: {occ}")
            if reason:
                raise AssertionError(f"emit row has nonblank exclusion_reason: {occ}")
            em = by_emission.get(emission_id)
            if em is None:
                raise AssertionError(f"emit row references missing emission_id {emission_id} for {occ}")
            if (em.get("emission_path") or "").strip() != "explicit_tag":
                raise AssertionError(f"emit row emission_path not explicit_tag: {occ} -> {emission_id}")
            if (em.get("representative_occurrence_id") or "").strip() != occ:
                raise AssertionError(f"emit row representative_occurrence_id mismatch: {occ} -> {emission_id}")
            if (em.get("source_occurrence_count") or "").strip() != "1":
                raise AssertionError(f"emit row source_occurrence_count != 1: {occ} -> {emission_id}")
            if (em.get("source_occurrence_ids") or "").strip() != occ:
                raise AssertionError(f"emit row source_occurrence_ids mismatch: {occ} -> {emission_id}")
            if (em.get("index_command") or "").strip() != idx_cmd:
                raise AssertionError(f"emit row index_command mismatch with emission table: {occ}")
        elif disp == "suppress":
            suppressed_occ_set.add(occ)
            if emission_id:
                raise AssertionError(f"suppress row has nonblank emission_id: {occ}")
            if idx_cmd:
                raise AssertionError(f"suppress row has nonblank index_command: {occ}")
            if not reason:
                raise AssertionError(f"suppress row has blank exclusion_reason: {occ}")
            ex = excluded_by_occ.get(occ)
            if ex is None:
                raise AssertionError(f"suppress row not found in print_excluded explicit rows: {occ}")
            ex_reason = (ex.get("exclusion_reason") or "").strip()
            if ex_reason != reason:
                raise AssertionError(
                    f"suppress row exclusion_reason mismatch for {occ}: "
                    f"plan={reason!r} excluded={ex_reason!r}"
                )
        else:
            raise AssertionError(f"unsupported disposition for {occ}: {disp!r}")

    if emitted_occ_set != expected_emit:
        raise AssertionError("emit occurrence set mismatch against print_main explicit in-book set")
    if suppressed_occ_set != expected_suppress:
        raise AssertionError("suppress occurrence set mismatch against print_excluded explicit in-book set")


def build_explicit_plan_from_paths(
    *,
    forms_path: Path = DEFAULT_FORMS_PATH,
    print_main_path: Path = DEFAULT_PRINT_MAIN_PATH,
    print_excluded_path: Path = DEFAULT_PRINT_EXCLUDED_PATH,
    book_emissions_path: Path = DEFAULT_BOOK_EMISSIONS_PATH,
    book_md_path: Path = DEFAULT_BOOK_MD,
) -> list[dict[str, str]]:
    return build_explicit_plan(
        forms_rows=load_rows(forms_path),
        print_main_rows=load_rows(print_main_path),
        print_excluded_rows=load_rows(print_excluded_path),
        book_emission_rows=load_rows(book_emissions_path),
        book_markdown_text=book_md_path.read_text(encoding="utf-8"),
    )


def validate_explicit_plan_from_paths(
    plan_rows: list[dict[str, str]],
    *,
    forms_path: Path = DEFAULT_FORMS_PATH,
    print_main_path: Path = DEFAULT_PRINT_MAIN_PATH,
    print_excluded_path: Path = DEFAULT_PRINT_EXCLUDED_PATH,
    book_emissions_path: Path = DEFAULT_BOOK_EMISSIONS_PATH,
    book_md_path: Path = DEFAULT_BOOK_MD,
) -> None:
    validate_explicit_plan(
        plan_rows,
        forms_rows=load_rows(forms_path),
        print_main_rows=load_rows(print_main_path),
        print_excluded_rows=load_rows(print_excluded_path),
        book_emission_rows=load_rows(book_emissions_path),
        book_markdown_text=book_md_path.read_text(encoding="utf-8"),
    )


def render_explicit_plan_tsv(rows: list[dict[str, str]]) -> str:
    return _tsv_text(rows, EXPLICIT_PLAN_FIELDS)


def write_explicit_plan(path: Path, rows: list[dict[str, str]]) -> None:
    path.write_text(render_explicit_plan_tsv(rows), encoding="utf-8")


class InventoryResult:
    """Summary counts from inventory_spans()."""

    __slots__ = (
        "total_iv",
        "iv_with_lang",
        "iv_blank_lang",
        "iv_with_source_ref",
        "iv_blank_source_ref",
        "iv_with_occ_id",
        "iv_blank_occ_id",
        "iv_in_plan",
        "iv_with_gt",
        "pred_total",
        "pred_in_plan",
    )

    def __init__(self, **kwargs: int) -> None:
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, 0))

    def __repr__(self) -> str:
        parts = ", ".join(f"{k}={getattr(self, k)}" for k in self.__slots__)
        return f"InventoryResult({parts})"


def inventory_spans(
    markdown_text: str,
    *,
    explicit_plan_path: Path = DEFAULT_EXPLICIT_PLAN_PATH,
) -> InventoryResult:
    """Return per-class inventory counts for explicit spans in assembled Markdown.

    Expected values for the canonical assembled book:
      total_iv           = 1496
      iv_with_lang       = 1496
      iv_with_occ_id     = 1496
      iv_in_plan         = 1496
      iv_with_gt         = 0
      pred_total         = 158
      pred_in_plan       = 0    (.pred spans are excluded from plan membership)
    """
    plan_ids: set[str] = set()
    if explicit_plan_path.exists():
        for row in load_rows(explicit_plan_path):
            occ = (row.get("occurrence_id") or "").strip()
            if occ:
                plan_ids.add(occ)

    all_spans = scan_explicit_spans(markdown_text)

    iv_spans = [s for s in all_spans if s["span_class"] == "iv"]
    pred_spans = [s for s in all_spans if s["span_class"] == "pred"]

    return InventoryResult(
        total_iv=len(iv_spans),
        iv_with_lang=sum(1 for s in iv_spans if (s.get("language") or "").strip()),
        iv_blank_lang=sum(1 for s in iv_spans if not (s.get("language") or "").strip()),
        iv_with_source_ref=sum(1 for s in iv_spans if (s.get("source_ref") or "").strip()),
        iv_blank_source_ref=sum(1 for s in iv_spans if not (s.get("source_ref") or "").strip()),
        iv_with_occ_id=sum(1 for s in iv_spans if (s.get("occurrence_id") or "").strip()),
        iv_blank_occ_id=sum(1 for s in iv_spans if not (s.get("occurrence_id") or "").strip()),
        iv_in_plan=sum(1 for s in iv_spans if (s.get("occurrence_id") or "").strip() in plan_ids),
        iv_with_gt=sum(1 for s in iv_spans if ">" in (s.get("normalized_visible_form") or "")),
        pred_total=len(pred_spans),
        pred_in_plan=sum(
            1 for s in pred_spans if (s.get("occurrence_id") or "").strip() in plan_ids
        ),
    )
