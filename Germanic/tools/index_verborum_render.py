#!/usr/bin/env python3
"""Centralized Index Verborum rendering and registry logic.

This module is the single Python-side source of truth for:

- loading and validating the language registry;
- loading and validating the Old English variety registry;
- language-order prefixes and language-header construction;
- effective printed-variety lookup;
- hidden MakeIndex variety discrimination;
- rendered index-entry construction (form + optional roman variety suffix);
- LaTeX escaping;
- complete ``\\index[iv]{...}`` command construction.

The Lua filter (``index_verborum_filter.lua``) is a deliberately parallel
implementation; parity tests assert the two produce equivalent MakeIndex
bodies for identical synthetic inputs.

Fixture overrides (parallel to ``CAPR_IV_PRINT_MAIN_TSV``):

- ``CAPR_IV_LANGUAGE_REGISTRY_TSV``
- ``CAPR_IV_VARIETY_REGISTRY_TSV``
"""
from __future__ import annotations

import csv
import os
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_LANGUAGE_REGISTRY = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
_DEFAULT_VARIETY_REGISTRY = REPO_ROOT / "Germanic/docs/book/index_verborum_varieties.tsv"

BOOL_VALUES = {"0", "1"}

# Separator used only inside the hidden MakeIndex sort field to attach a
# per-variety discriminator. It is deliberately a character that can never
# appear in a scholarly sort key (which is [a-z0-9] only), which is what makes
# the (sort_key, variety) -> sort-field mapping injective / collision-proof.
# Its MakeIndex sorting behaviour is exercised by the real makeindex fixture.
DISCRIMINATOR_SEP = "~"


def language_registry_path() -> Path:
    return Path(os.environ.get("CAPR_IV_LANGUAGE_REGISTRY_TSV") or _DEFAULT_LANGUAGE_REGISTRY)


def variety_registry_path() -> Path:
    return Path(os.environ.get("CAPR_IV_VARIETY_REGISTRY_TSV") or _DEFAULT_VARIETY_REGISTRY)


def latex_escape(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


# ── Language registry ────────────────────────────────────────────────────────
@dataclass(frozen=True)
class LanguageEntry:
    code: str
    title: str
    order: int
    index_note: str


def load_language_registry(path: Path | None = None) -> dict[str, LanguageEntry]:
    """Return {code: LanguageEntry} for active languages, preserving file order."""
    registry_path = path or language_registry_path()
    result: dict[str, LanguageEntry] = {}
    with registry_path.open(encoding="utf-8", newline="") as handle:
        order = 0
        for row in csv.DictReader(handle, delimiter="\t"):
            code = (row.get("code") or "").strip()
            active = (row.get("active") or "").strip()
            if not code or active != "1":
                continue
            order += 1
            result[code] = LanguageEntry(
                code=code,
                title=(row.get("title") or "").strip(),
                order=order,
                index_note=(row.get("index_note") or "").strip(),
            )
    return result


def language_prefix(entry: LanguageEntry) -> str:
    return f"{entry.order:02d}{entry.code}"


def language_header_tex(entry: LanguageEntry) -> str:
    """Construct ``\\ivlangheader{Title}{note}`` (note blank => empty group)."""
    title = latex_escape(entry.title)
    note = latex_escape(entry.index_note)
    return rf"\ivlangheader{{{title}}}{{{note}}}"


# ── Variety registry ─────────────────────────────────────────────────────────
@dataclass(frozen=True)
class VarietyEntry:
    language: str
    code: str
    title: str
    printed_label: str
    parent: str
    display_order: int
    suppress_label: bool
    assignable: bool
    active: bool
    notes: str


class VarietyRegistry:
    def __init__(self, entries: dict[str, VarietyEntry]) -> None:
        self.entries = entries

    def get(self, code: str) -> VarietyEntry | None:
        return self.entries.get(code)

    def printed_label(self, code: str) -> str:
        entry = self.entries.get(code)
        if entry is None or entry.suppress_label:
            return ""
        return entry.printed_label

    def display_order(self, code: str) -> int:
        entry = self.entries.get(code)
        return entry.display_order if entry else 0

    def validate_occurrence(self, language: str, variety: str) -> None:
        """Fail-closed validation of a nonblank occurrence variety."""
        if not variety:
            return
        entry = self.entries.get(variety)
        if entry is None:
            raise ValueError(f"Unknown index verborum variety code: {variety!r}")
        if not entry.active:
            raise ValueError(f"Inactive variety code used on occurrence: {variety!r}")
        if not entry.assignable:
            raise ValueError(
                f"Non-assignable variety code used on occurrence: {variety!r} "
                f"(e.g. 'ws' is a taxonomy parent; ordinary West Saxon stays unmarked)"
            )
        if entry.language != language:
            raise ValueError(
                f"Variety {variety!r} belongs to language {entry.language!r}, "
                f"not {language!r}"
            )


def load_variety_registry(path: Path | None = None) -> VarietyRegistry:
    registry_path = path or variety_registry_path()
    rows: list[dict[str, str]] = []
    with registry_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            rows.append({key: (value or "").strip() for key, value in row.items()})
    return _validate_variety_rows(rows)


def _validate_variety_rows(rows: list[dict[str, str]]) -> VarietyRegistry:
    entries: dict[str, VarietyEntry] = {}
    seen_codes: set[str] = set()
    known_languages = set(load_language_registry().keys())
    # Allow fixture language registries that omit codes: fall back permissively
    # only when the language registry could not be loaded meaningfully.
    active_order_by_lang: dict[str, set[int]] = {}

    for row in rows:
        code = row.get("code", "")
        language = row.get("language", "")
        if not code:
            raise ValueError("Variety registry row missing code")
        if code in seen_codes:
            raise ValueError(f"Duplicate variety code: {code!r}")
        seen_codes.add(code)

        active_raw = row.get("active", "")
        assignable_raw = row.get("assignable", "")
        suppress_raw = row.get("suppress_label", "")
        for label, raw in (
            ("active", active_raw),
            ("assignable", assignable_raw),
            ("suppress_label", suppress_raw),
        ):
            if raw not in BOOL_VALUES:
                raise ValueError(f"Variety {code!r}: {label} must be 0 or 1, got {raw!r}")

        order_raw = row.get("display_order", "")
        if not order_raw.isdigit() or int(order_raw) < 1:
            raise ValueError(f"Variety {code!r}: display_order must be a positive integer, got {order_raw!r}")
        display_order = int(order_raw)

        active = active_raw == "1"
        assignable = assignable_raw == "1"
        suppress = suppress_raw == "1"

        if active and language not in known_languages:
            raise ValueError(f"Variety {code!r}: unknown active language {language!r}")
        if assignable and not active:
            raise ValueError(f"Variety {code!r}: assignable variety must be active")
        # An assignable variety must be visibly printable: it needs a real label
        # and must not be suppressed, or an occurrence could be silently invisible.
        printed_label = row.get("printed_label", "")
        if assignable and not printed_label.strip():
            raise ValueError(f"Variety {code!r}: assignable variety must have a nonblank printed_label")
        if assignable and suppress:
            raise ValueError(f"Variety {code!r}: assignable variety must not set suppress_label=1")
        # A suppressed variety carries no printable label and therefore must be a
        # non-assignable taxonomy parent (e.g. 'ws'), never a directly usable code.
        if suppress and assignable:
            raise ValueError(f"Variety {code!r}: suppressed variety must be non-assignable")

        entries[code] = VarietyEntry(
            language=language,
            code=code,
            title=row.get("title", ""),
            printed_label=row.get("printed_label", ""),
            parent=row.get("parent", ""),
            display_order=display_order,
            suppress_label=suppress,
            assignable=assignable,
            active=active,
            notes=row.get("notes", ""),
        )
        if active:
            bucket = active_order_by_lang.setdefault(language, set())
            if display_order in bucket:
                raise ValueError(
                    f"Duplicate active display_order {display_order} within language {language!r}"
                )
            bucket.add(display_order)

    # Parent-graph validation
    for entry in entries.values():
        if not entry.parent:
            continue
        parent = entries.get(entry.parent)
        if parent is None:
            raise ValueError(f"Variety {entry.code!r}: missing parent {entry.parent!r}")
        if parent.language != entry.language:
            raise ValueError(
                f"Variety {entry.code!r}: parent {entry.parent!r} is a different language"
            )
        if entry.active and not parent.active:
            raise ValueError(
                f"Variety {entry.code!r}: active child of inactive parent {entry.parent!r}"
            )

    # Acyclicity
    for entry in entries.values():
        seen: set[str] = set()
        cursor: VarietyEntry | None = entry
        while cursor and cursor.parent:
            if cursor.parent in seen:
                raise ValueError(f"Cyclic variety hierarchy at {entry.code!r}")
            seen.add(cursor.parent)
            cursor = entries.get(cursor.parent)

    return VarietyRegistry(entries)


# ── Rendered entry construction ──────────────────────────────────────────────
def render_form_part(language: str, display: str, variety_label: str) -> str:
    """Return the LaTeX form portion of an index entry.

    Old English forms use ``\\ivoeentry{form}{label}`` so the form is italic and
    the (optional) variety label is roman. A blank label renders identically to
    ``\\emph{form}``. Other languages render the escaped display verbatim.
    """
    escaped = latex_escape(display)
    if language == "oe":
        return rf"\ivoeentry{{{escaped}}}{{{variety_label}}}"
    return escaped


def index_command(
    language: str,
    sort_key: str,
    display: str,
    variety: str,
    *,
    lang_meta: dict[str, LanguageEntry],
    var_registry: VarietyRegistry,
) -> str:
    """Construct a complete ``\\index[iv]{...}`` command.

    The MakeIndex two-level body is ``LANGPREFIX@LANGHEADER!SORT<disc>@FORM``.

    Fail-closed: the occurrence variety is validated here (not only in callers),
    so an unknown, inactive, non-assignable, or wrong-language variety — and in
    particular ``variety=ws`` — raises before any label or discriminator is
    produced.

    Hidden discriminator (collision-proof encoding). Scholarly sort keys are
    lowercase ``[a-z0-9]`` only (see ``transliterate_sort_key``); they never
    contain :data:`DISCRIMINATOR_SEP`. A blank variety appends nothing; a
    labelled variety appends ``SEP + <two-digit display_order>``. Because the
    separator can never occur inside a sort key, the map
    ``(sort_key, variety) -> sort field`` is injective: a labelled key always
    contains the separator while a blank key never does, and two labelled keys
    with the same prefix must share both the separator position and the fixed
    two-digit order. This removes the earlier ambiguity where a blank sort key
    ``form02`` could collide with an EWS occurrence of ``form``. The blank entry
    remains a strict prefix of every labelled sibling, so it still sorts first
    and all variants of one lexical form stay contiguous.
    """
    # Fail closed regardless of caller discipline (validates nonblank varieties).
    var_registry.validate_occurrence(language, variety)

    entry = lang_meta.get(language)
    if entry is not None:
        lang_prefix = language_prefix(entry)
        lang_header = language_header_tex(entry)
    else:
        lang_prefix = f"99{language}"
        lang_header = rf"\ivlangheader{{{latex_escape(language)}}}{{}}"

    escaped_sort = latex_escape(sort_key)
    if variety:
        if DISCRIMINATOR_SEP in escaped_sort:
            raise ValueError(
                f"Sort key {sort_key!r} contains the reserved variety "
                f"discriminator separator {DISCRIMINATOR_SEP!r}; sort keys must "
                f"be [a-z0-9] only so hidden discriminators stay collision-proof"
            )
        variety_label = var_registry.printed_label(variety)
        disc = f"{DISCRIMINATOR_SEP}{var_registry.display_order(variety):02d}"
    else:
        variety_label = ""
        disc = ""
    level2_sort = escaped_sort + disc
    form_part = render_form_part(language, display, variety_label)
    return rf"\index[iv]{{{lang_prefix}@{lang_header}!{level2_sort}@{form_part}}}"
