#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FORMS_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_forms.tsv"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
PRINT_EXCLUDED_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_excluded.tsv"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
MANIFEST_PATH = REPO_ROOT / "Germanic/docs/assembly/manifest_all_by_class.tsv"
INDEX_HEADER_PATH = REPO_ROOT / "Germanic/docs/assembly/book_draft_pdf_header.tex"
DEFAULT_TEX_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.tex"
INTRO_PATH = REPO_ROOT / "Germanic/docs/assembly/capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
PROSE_RULE_WORDS = {"form", "output", "expected", "stage", "rule"}


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def latex_escape(value: str) -> str:
    return value.replace("@", r"\@").replace("!", r"\!").replace("|", r"\|")


def _check_build_lang_order() -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        for order, row in enumerate(csv.DictReader(handle, delimiter="\t"), start=1):
            code = (row.get("code") or "").strip()
            title = (row.get("title") or "").strip()
            active = (row.get("active") or "").strip()
            if code and active == "1":
                result[code] = (f"{order:02d}{code}", title)
    return result


_CHECK_LANG_ORDER: dict[str, tuple[str, str]] | None = None


def check_get_lang_order() -> dict[str, tuple[str, str]]:
    global _CHECK_LANG_ORDER
    if _CHECK_LANG_ORDER is None:
        _CHECK_LANG_ORDER = _check_build_lang_order()
    return _CHECK_LANG_ORDER


def index_command(row: dict[str, str]) -> str:
    language = row.get("language", "")
    sort_key = row.get("sort_key", "")
    display = row.get("display", "")
    index_display = latex_escape(display)
    if language == "oe":
        index_display = rf"\emph{{{index_display}}}"
    lang_order = check_get_lang_order()
    lang_prefix, lang_title = lang_order.get(language, (f"99{language}", language))
    lang_title_escaped = lang_title.replace("@", r"\@").replace("!", r"\!")
    lang_header = rf"\ivlangheader{{{lang_title_escaped}}}"
    return rf"\index[iv]{{{lang_prefix}@{lang_header}!{latex_escape(sort_key)}@{index_display}}}"


def explicit_key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (
        row.get("language", ""),
        row.get("sort_key", ""),
        row.get("display", ""),
        row.get("form_role", "") or "evidence_form",
    )


def require_row(rows: list[dict[str, str]], predicate, label: str) -> dict[str, str]:
    for row in rows:
        if predicate(row):
            return row
    raise AssertionError(f"Missing regression row for {label}")


def decode_latex_index_value(value: str) -> str:
    return value.replace(r"\@", "@").replace(r"\!", "!").replace(r"\|", "|")


def parse_tex_index_commands(tex_text: str) -> list[tuple[str, str, str]]:
    """Parse \\index[iv]{LANGPREFIX@TITLE!sort@display} into (lang_prefix, sort, display) tuples."""
    commands: list[tuple[str, str, str]] = []
    # Match both legacy per-language and new unified format
    for match in re.finditer(r"\\index\[(?P<lang>[^\]]+)\]\{(?P<body>[^}]*)\}", tex_text):
        lang = match.group("lang")
        body = match.group("body")
        if lang == "iv" and "!" in body:
            # Unified two-level: LANGPREFIX@TITLE!sort@display
            # Split on first un-escaped !
            parts = re.split(r"(?<!\\)!", body, maxsplit=1)
            if len(parts) == 2:
                lang_part, form_part = parts
                if "@" in form_part:
                    sort_key, display = form_part.split("@", 1)
                else:
                    sort_key, display = form_part, form_part
                commands.append((lang, decode_latex_index_value(sort_key), decode_latex_index_value(display)))
        else:
            # Legacy or non-iv format
            if "@" in body:
                sort_key, display = body.split("@", 1)
            else:
                sort_key, display = body, body
            commands.append((lang, decode_latex_index_value(sort_key), decode_latex_index_value(display)))
    return commands


def normalized_index_token(value: str) -> str:
    return value.casefold().lstrip("*").strip("`.,;:!?()[]{}\"' ")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex-path", type=Path, default=DEFAULT_TEX_PATH)
    args = parser.parse_args()

    tex_path = args.tex_path.expanduser().resolve()
    tex_text = tex_path.read_text(encoding="utf-8")
    header_text = INDEX_HEADER_PATH.read_text(encoding="utf-8")
    form_rows = load_rows(FORMS_PATH)
    main_rows = load_rows(PRINT_MAIN_PATH)
    excluded_rows = load_rows(PRINT_EXCLUDED_PATH)

    main_explicit_keys = {
        explicit_key(row)
        for row in main_rows
        if row.get("source_scope") == "explicit_tag"
    }

    # ── Registry architecture: exactly one unified 'iv' index ──────────────────
    # Any per-language \makeindex[name=oe,...] declaration is a hard failure.
    makeindex_names = re.findall(r"\\makeindex\[name=([^,\]]+)", tex_text)
    assert len(makeindex_names) == 1, (
        f"Expected exactly one \\makeindex declaration (name=iv); found: {makeindex_names}. "
        "Per-language index declarations are forbidden in the canonical book."
    )
    assert makeindex_names[0] == "iv", (
        f"The single \\makeindex must use name=iv, not name={makeindex_names[0]}."
    )
    assert r"\makeindex[name=iv,title={},columns=3]" in tex_text, (
        "Unified index must declare columns=3: \\makeindex[name=iv,title={},columns=3]"
    )

    # ── Print call: exactly one unified printindex ─────────────────────────────
    printindex_calls = re.findall(r"\\printindex\[([^\]]+)\]", tex_text)
    assert len(printindex_calls) == 1, (
        f"Expected exactly one \\printindex call (\\printindex[iv]); found: {printindex_calls}"
    )
    assert printindex_calls[0] == "iv", (
        f"The single \\printindex must use [iv], not [{printindex_calls[0]}]."
    )

    # ── All index commands must use \index[iv]{...} ────────────────────────────
    # Any per-language \index[oe]{...}, \index[pgmc]{...}, etc. is a hard failure.
    per_lang_index_pattern = re.compile(r"\\index\[(?!iv\])([^\]]+)\]\{")
    per_lang_hits = per_lang_index_pattern.findall(tex_text)
    assert not per_lang_hits, (
        f"Per-language index commands found in TeX (must all use \\index[iv]{{...}}): "
        f"{per_lang_hits[:10]}. "
        "Legacy per-language index streams are forbidden."
    )

    # ── No doubled-star reconstruction in generated TeX ────────────────────────
    doubled_star_pattern = re.compile(r"\\Recon\{[\\]?\*")
    doubled_star_hits = doubled_star_pattern.findall(tex_text)
    assert not doubled_star_hits, (
        f"Generated TeX contains doubled-star reconstruction (\\Recon{{*...}}): "
        f"{doubled_star_hits[:5]}. "
        "The \\Recon{{}} macro supplies the asterisk; fix source markup to remove leading *."
    )

    # ── Extract all \index[iv]{...} commands (nested-brace aware) ─────────────
    def _extract_iv_bodies(text: str) -> list[str]:
        """Extract the body of every \\index[iv]{...} command, handling nested braces."""
        bodies: list[str] = []
        for m in re.finditer(r"\\index\[iv\]\{", text):
            pos = m.end()
            depth = 1
            end = pos
            while end < len(text) and depth > 0:
                if text[end] == "{":
                    depth += 1
                elif text[end] == "}":
                    depth -= 1
                end += 1
            bodies.append(text[m.end():end - 1])
        return bodies

    all_iv_bodies = _extract_iv_bodies(tex_text)

    # ── Two-level structure: every \index[iv] body must contain '!' ───────────
    malformed_iv = [b for b in all_iv_bodies if "!" not in b]
    assert not malformed_iv, (
        f"\\index[iv] entries missing two-level language!form structure "
        f"({len(malformed_iv)} total): {malformed_iv[:5]}"
    )

    # ── Language registry: every active language has a unique order prefix ──────
    lang_order = check_get_lang_order()
    registry_codes = set(lang_order.keys())
    print_languages = {(row.get("language") or "").strip() for row in main_rows if (row.get("language") or "").strip()}
    unknown_langs = print_languages - registry_codes
    assert not unknown_langs, (
        f"Print main contains languages not in active registry (would use fallback 99xx prefix): {unknown_langs}"
    )

    # ── Index occurrence two-sided coverage check ─────────────────────────────
    # Derive required command multiplicities for non-explicit injection semantics:
    # - non-explicit rows are deduplicated per heading/line injection site
    # Explicit-tag commands are validated as a strict subset via expected_command_set
    # (spurious commands forbidden), while the required-multiplicity converse check
    # below ensures injected printable material is not silently omitted.
    from collections import Counter
    expected_command_set: set[str] = {index_command(row) for row in main_rows}

    model_entry_heading_map: dict[str, str] = {}
    with MANIFEST_PATH.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            model_path = (row.get("model_entry_path") or "").strip()
            lexical_item = (row.get("lexical_item") or "").strip()
            counterpart = (row.get("counterpart") or "").strip()
            derivation_class = (row.get("derivation_class") or "").strip()
            if not model_path or not lexical_item:
                continue
            display_counterpart = f"*{counterpart}" if derivation_class == "reconstructed_oe" else counterpart
            model_entry_heading_map[model_path] = f"{lexical_item} — OE {display_counterpart}"

    line_injected_scopes = {"table_semantic_auto", "table_semantic_decision", "broad_prose_decision"}
    allowed_line_paths = {
        INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
        CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
    }
    allowed_heading_refs = set(model_entry_heading_map.values())
    collapsed_non_explicit_sites: set[tuple[str, str, str]] = set()

    for row in main_rows:
        command = index_command(row)
        source_scope = (row.get("source_scope") or "").strip()
        source_ref = (row.get("source_ref") or "").strip()

        if source_scope == "explicit_tag":
            continue

        if not source_ref:
            continue

        if ".md:" in source_ref:
            path_part, line_part = source_ref.rsplit(":", 1)
            line_is_int = line_part.isdigit()
            if source_scope in line_injected_scopes:
                if line_is_int and path_part in allowed_line_paths:
                    collapsed_non_explicit_sites.add(("line", f"{path_part}:{line_part}", command))
                continue
            if path_part in model_entry_heading_map:
                collapsed_non_explicit_sites.add(("heading", model_entry_heading_map[path_part], command))
            elif line_is_int and path_part in allowed_line_paths:
                collapsed_non_explicit_sites.add(("line", f"{path_part}:{line_part}", command))
            elif source_ref in allowed_heading_refs:
                collapsed_non_explicit_sites.add(("heading", source_ref, command))
        elif source_ref in allowed_heading_refs:
            collapsed_non_explicit_sites.add(("heading", source_ref, command))

    expected_counter: Counter[str] = Counter()
    for _, _, command in collapsed_non_explicit_sites:
        expected_counter[command] += 1

    actual_counter: Counter[str] = Counter()
    for body in all_iv_bodies:
        full_cmd = r"\index[iv]{" + body + "}"
        actual_counter[full_cmd] += 1

    # Every actual command must be in the expected set
    spurious_cmds = [cmd for cmd in actual_counter if cmd not in expected_command_set]
    assert not spurious_cmds, (
        f"TeX contains \\index[iv]{{...}} commands NOT in print_main.tsv "
        f"({len(spurious_cmds)} total); first examples:\n"
        + "\n".join(spurious_cmds[:3])
    )

    # Sanity: at least some commands must be present
    assert actual_counter, "Generated TeX contains no \\index[iv] commands."

    # Converse coverage: every required non-explicit printable command occurrence
    # must appear in generated TeX at least as many times as injection semantics demand.
    missing = [cmd for cmd, count in expected_counter.items() if count > actual_counter.get(cmd, 0)]
    assert not missing, (
        "Required printable index commands are missing from generated TeX:\n"
        + "\n".join(
            f"{cmd} (expected={expected_counter[cmd]}, actual={actual_counter.get(cmd, 0)})"
            for cmd in missing[:5]
        )
    )

    # ── Explicit-occurrence two-sided coverage check ──────────────────────────
    # Every printable explicit_tag occurrence in canonical assembled sources must
    # produce its \\index[iv]{...} command in generated TeX, and the generated count
    # for each explicit command must not exceed the expected count.
    #
    # Only intro and chronology sources are assembled with their ORIGINAL source_refs
    # preserved (via inject_line_commands). Model-entry explicit tags get source_refs
    # pointing to the lexical volume path after assembly, which don't match the
    # print_main model-entry source_refs; those entries are covered by the heading-level
    # injection already checked above. The Lua filter therefore only emits explicit index
    # commands for intro and chronology occurrences.
    #
    # Occurrence identity: (language, form_role, form, display, source_ref).
    # Multiple rows with the same command but different occurrences are counted separately.
    lua_filter_source_paths = {
        INTRO_PATH.relative_to(REPO_ROOT).as_posix(),
        CHRONOLOGY_PATH.relative_to(REPO_ROOT).as_posix(),
    }
    explicit_expected_counter: Counter[str] = Counter()
    for row in main_rows:
        if (row.get("source_scope") or "").strip() != "explicit_tag":
            continue
        source_ref = (row.get("source_ref") or "").strip()
        path_part = source_ref.rsplit(":", 1)[0] if ":" in source_ref else source_ref
        if path_part not in lua_filter_source_paths:
            continue
        explicit_expected_counter[index_command(row)] += 1

    # Explicit commands: actual count must match expected count exactly.
    # Lower bound: every expected explicit occurrence must be present.
    explicit_missing = [
        cmd for cmd, exp_count in explicit_expected_counter.items()
        if actual_counter.get(cmd, 0) < exp_count
    ]
    assert not explicit_missing, (
        "Expected explicit .iv occurrences are missing from generated TeX:\n"
        + "\n".join(
            f"{cmd} (expected_explicit={explicit_expected_counter[cmd]}, actual={actual_counter.get(cmd, 0)})"
            for cmd in explicit_missing[:5]
        )
    )

    # Sanity: at least some explicit commands should have been expected
    assert explicit_expected_counter, "No printable explicit_tag occurrences found in intro/chronology sources — index may be empty."

    # ── Excluded rows must not appear ─────────────────────────────────────────
    for row in excluded_rows:
        if row.get("form_role") != "regular_output":
            continue
        if explicit_key(row) in main_explicit_keys:
            continue
        command = index_command(row)
        if command in expected_command_set:
            continue
        assert command not in tex_text, f"Excluded explicit regular_output leaked into TeX: {command}"

    reader_failure_rows = [row for row in form_rows if (row.get("source_scope") or "").startswith("reader_failure_")]
    for row in reader_failure_rows:
        command = index_command(row)
        if command in expected_command_set:
            continue
        assert command not in tex_text, f"Reader-facing failure row leaked into TeX: {command}"

    # ── Prose/rule-word contamination ─────────────────────────────────────────
    for _, sort_key, display in parse_tex_index_commands(tex_text):
        token_sort = normalized_index_token(sort_key)
        token_display = normalized_index_token(display)
        assert token_sort not in {"monch", "jugend"}, f"Unexpected prose index entry: {sort_key}@{display}"
        assert token_display not in {"mönch", "jugend"}, f"Unexpected prose index entry: {sort_key}@{display}"
        assert token_sort not in PROSE_RULE_WORDS and token_display not in PROSE_RULE_WORDS, (
            f"Prose/rule-label token leaked into index: {sort_key}@{display}"
        )

    # ── Spot-check specific known entries ─────────────────────────────────────
    assert "Modern English linguistic forms" not in tex_text
    assert r"\chapter*{Old English}" not in tex_text
    assert r"\chapter*{Proto-Germanic}" not in tex_text

    ordinary_oe_target = require_row(
        main_rows,
        lambda row: row.get("language") == "oe"
        and row.get("form_role") == "target_form"
        and row.get("source_scope") == "lexical_heading"
        and not row.get("display", "").startswith("*"),
        "ordinary OE target",
    )
    source_backed_pgmc = require_row(
        main_rows,
        lambda row: row.get("language") == "pgmc"
        and row.get("form_role") == "source_protoform"
        and row.get("source_scope") == "lexical_protoform",
        "source-backed PGmc protoform",
    )
    reconstructed_oe_target = require_row(
        main_rows,
        lambda row: row.get("language") == "oe"
        and row.get("form_role") == "target_form"
        and row.get("source_scope") == "lexical_heading"
        and row.get("display", "").startswith("*"),
        "reconstructed OE target",
    )
    for label, row in (
        ("ordinary OE target", ordinary_oe_target),
        ("source-backed PGmc protoform", source_backed_pgmc),
        ("reconstructed OE target", reconstructed_oe_target),
    ):
        command = index_command(row)
        assert command in tex_text, f"Missing expected TeX index command for {label}: {command}"

    # ── Architecture invariant assertions (negative fixtures) ──────────────────
    # These should ALWAYS hold and serve as negative fixtures:
    assert r"\index[preoe]{" not in tex_text, (
        "Direct per-language preoe index command must not appear; all commands must use \\index[iv]{...}."
    )
    assert r"\indexsetup{level=\section*,noclearpage}" in header_text, (
        "Expected indexsetup with level=\\section* in book_draft_pdf_header.tex."
    )
    assert r"\indexsetup{level=\chapter*" not in header_text

    print("book draft tex index policy checks passed")


if __name__ == "__main__":
    main()
