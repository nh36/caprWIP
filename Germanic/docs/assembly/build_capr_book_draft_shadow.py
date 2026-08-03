#!/usr/bin/env python3
"""Build capr_book_draft_shadow.md for shadow-mode anchor validation.

This builder is identical to build_capr_book_draft.py except that
heading_injection and line_injection sites emit .iv-anchor Span markers
instead of raw \\index[iv]{...} commands.

The output file (capr_book_draft_shadow.md) is used only by the shadow check
(check_anchor_shadow.py) and is never committed as a tracked canonical output.

The production builder and production output are NOT changed.

Shadow mode contract
--------------------
* Explicit .iv spans remain unchanged; they still emit through the Lua
  span_to_index path as in production.
* For each heading/line injection site, the shadow builder inserts:
    []{.iv-anchor emission_id="emit:xxx"}
  as a Span in a paragraph, replacing the raw command.
* The Lua filter's anchor handler looks up the emission_id in
  book_emissions.tsv and emits the precomputed index_command.

This proves that heading/line injections could be fully served through the
anchor path with exactly the same TeX commands as the production builder.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
from index_verborum_emission import load_model_entry_headings, load_print_main, build_emission_table

INTRO_PATH = SCRIPT_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
LEXICAL_PATH = SCRIPT_DIR / "lexical_volume_alpha_01.md"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
MANIFEST_PATH = SCRIPT_DIR / "manifest_all_by_class.tsv"
OUTPUT_PATH = SCRIPT_DIR / "capr_book_draft_shadow.md"

NESTED_RECON_IV_RE = re.compile(r"\[\[(?P<form>[^\]]+)\]\{\.recon\}(?P<tail>.*?)\]\{(?P<attrs>[^}]*)\}")
EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{(?P<attrs>[^}]*)\}")


def has_tag_class(raw_attrs: str, cls: str) -> bool:
    return re.search(rf"(^|\s)\.{re.escape(cls)}(?=\s|$)", raw_attrs) is not None


def load_language_order() -> list[str]:
    with LANGUAGE_REGISTRY_PATH.open(encoding="utf-8") as handle:
        return [row["code"] for row in csv.DictReader(handle, delimiter="\t") if (row.get("active") or "").strip() == "1"]


LANGUAGE_ORDER = load_language_order()


def oe_target_display(counterpart: str, derivation_class: str) -> str:
    return f"*{counterpart}" if derivation_class == "reconstructed_oe" else counterpart


def heading_ref(lexical_item: str, counterpart: str, derivation_class: str = "") -> str:
    return f"{lexical_item} — OE {oe_target_display(counterpart, derivation_class)}"


def anchor_marker(emission_id: str) -> str:
    """Return a Pandoc Span anchor marker for the given emission_id."""
    eid_safe = emission_id.replace('"', "&quot;")
    return f'[{{}}]{{.iv-anchor emission_id="{eid_safe}"}}'


def load_shadow_injection_map() -> tuple[
    dict[str, str],           # heading → anchor_marker
    dict[str, dict[int, str]],  # rel_path → {line_no → anchor_marker}
]:
    """Build heading/line anchor maps from the canonical book emission plan."""
    heading_anchors: dict[str, str] = {}
    line_anchors: dict[str, dict[int, str]] = defaultdict(dict)

    main_rows = load_print_main()
    emission_rows = build_emission_table(main_rows, load_model_entry_headings())
    seen_emission_ids: set[str] = set()

    for row in emission_rows:
        if row.get("in_book") != "1":
            continue
        emission_id = row.get("emission_id", "")
        if emission_id in seen_emission_ids:
            continue
        seen_emission_ids.add(emission_id)
        path = row.get("emission_path", "")
        if path == "explicit_tag":
            continue
        site = row.get("site", "")
        marker = anchor_marker(emission_id)
        if path == "heading_injection":
            heading_anchors[site] = heading_anchors.get(site, "") + (" " if site in heading_anchors else "") + marker
        elif path == "line_injection":
            if ".md:" not in site:
                continue
            path_part, line_part = site.rsplit(":", 1)
            if not line_part.isdigit():
                continue
            line_no = int(line_part)
            prev = line_anchors[path_part].get(line_no, "")
            line_anchors[path_part][line_no] = (prev + " " + marker).strip()

    return heading_anchors, dict(line_anchors)


def annotate_explicit_tags_in_line(line: str, rel_path: str, line_no: int) -> str:
    source_ref = f'{rel_path}:{line_no}'
    span_counter = [0]

    def _make_attrs(existing_attrs: str) -> str | None:
        if re.search(r'(^|\s)source_ref=', existing_attrs):
            return None
        span_counter[0] += 1
        occ_id = f'{source_ref}:{span_counter[0]}'
        body = existing_attrs.strip()
        new_attrs = f'source_ref="{source_ref}" occ_id="{occ_id}"'
        return f'{body} {new_attrs}' if body else new_attrs

    def repl_nested(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if not (has_tag_class(attrs, "iv") or has_tag_class(attrs, "pred")):
            return match.group(0)
        new_attrs = _make_attrs(attrs)
        if new_attrs is None:
            return match.group(0)
        return f"[[{match.group('form')}]{{.recon}}{match.group('tail')}]{{{new_attrs}}}"

    def repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if not (has_tag_class(attrs, "iv") or has_tag_class(attrs, "pred")):
            return match.group(0)
        new_attrs = _make_attrs(attrs)
        if new_attrs is None:
            return match.group(0)
        return f"[{match.group('content')}]{{{new_attrs}}}"

    line = NESTED_RECON_IV_RE.sub(repl_nested, line)
    return EXPLICIT_TAG_RE.sub(repl, line)


def annotate_explicit_tags_with_source_ref(path: Path, text: str) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    return "\n".join(
        annotate_explicit_tags_in_line(line, rel, line_no)
        for line_no, line in enumerate(text.splitlines(), start=1)
    )


def inject_line_shadow(path: Path, line_anchors: dict[str, dict[int, str]]) -> str:
    """Like inject_line_commands but inserts .iv-anchor markers instead of raw cmds."""
    rel = path.relative_to(REPO_ROOT).as_posix()
    anchors_for_file = line_anchors.get(rel, {})
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    for idx, line in enumerate(lines, start=1):
        out.append(annotate_explicit_tags_in_line(line, rel, idx))
        if idx in anchors_for_file:
            out.append(anchors_for_file[idx])
    return "\n".join(out).rstrip()


def strip_title_block(text: str) -> str:
    lines = text.rstrip().splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).rstrip()


def strip_references(text: str) -> str:
    marker = "\n# References\n"
    return text.split(marker, 1)[0].rstrip() if marker in text else text.rstrip()


def strip_lexical_terminal_references(text: str) -> str:
    import re as _re
    return _re.sub(r'\s*\\clearpage\s*\n\s*## References.*$', '', text, flags=_re.DOTALL)


_HIST_CHAPTER_RE = re.compile(r"^# Chapter \d+\. (.+)$")


def transform_chronology(text: str) -> str:
    """Same heading-level transformation as production builder."""
    out: list[str] = []
    preamble: list[str] = []
    seen_chapter = False
    in_intro = False

    for line in strip_title_block(strip_references(text)).splitlines():
        m = _HIST_CHAPTER_RE.match(line)
        if m:
            if not seen_chapter and preamble:
                out.append("# Sound-change overview {.unnumbered}")
                for p in preamble:
                    if p.startswith("## ") and not p.rstrip().endswith("{.unnumbered}"):
                        out.append(p.rstrip() + " {.unnumbered}")
                    else:
                        out.append(p)
                preamble = []
                out.append("")
            seen_chapter = True
            in_intro = True
            out.append("# " + m.group(1))
        elif not seen_chapter:
            preamble.append(line)
        elif line.startswith("# "):
            in_intro = False
            out.append("## " + line[2:])
        elif line.startswith("## "):
            if in_intro:
                out.append(line)
            else:
                out.append("### " + line[3:])
        elif line.startswith("### "):
            if in_intro:
                out.append(line)
            else:
                out.append("#### " + line[4:])
        else:
            out.append(line)

    return "\n".join(out).rstrip()


_PART_HEADING_RE = re.compile(r"^## Part [IVX]+\.\s+(.+)$")


def transform_lexical_shadow(text: str, heading_anchors: dict[str, str]) -> str:
    """Like transform_lexical but injects .iv-anchor markers instead of raw commands."""
    out: list[str] = []
    preamble: list[str] = []
    seen_part = False

    lines = strip_title_block(text).splitlines()
    if lines and lines[0].startswith("_Alpha 01"):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]

    for line in lines:
        m_part = _PART_HEADING_RE.match(line)
        if m_part:
            if not seen_part and preamble:
                out.append("# Word-by-word derivations {.unnumbered}")
                for p in preamble:
                    if p.startswith("## ") and not p.rstrip().endswith("{.unnumbered}"):
                        out.append(p.rstrip() + " {.unnumbered}")
                    else:
                        out.append(p)
                preamble = []
                out.append("")
            seen_part = True
            out.append("# " + m_part.group(1))
        elif not seen_part:
            preamble.append(line)
        elif line.startswith("### "):
            entry_text = line[3:]
            out.append("##" + entry_text)
            # Shadow: inject .iv-anchor marker for heading injection site
            ref = line[4:].strip()
            if " — OE _" in ref and ref.endswith("_"):
                lexical_item, target = ref.split(" — OE ", 1)
                cleaned_target = target[1:-1].replace('\\*', '*')
                ref = f"{lexical_item} — OE {cleaned_target}"
            marker = heading_anchors.get(ref, "")
            if marker:
                out.append("")
                out.append(marker)
        elif line.startswith("#### "):
            out.append("###" + line[4:])
        elif line.startswith("##### "):
            out.append("####" + line[5:])
        else:
            out.append(line)

    return "\n".join(out).rstrip()


def build_shadow_markdown() -> str:
    heading_anchors, line_anchors = load_shadow_injection_map()
    intro = inject_line_shadow(INTRO_PATH, line_anchors)
    chronology = transform_chronology(inject_line_shadow(CHRONOLOGY_PATH, line_anchors))
    lexical_text = annotate_explicit_tags_with_source_ref(LEXICAL_PATH, LEXICAL_PATH.read_text(encoding="utf-8"))
    lexical = transform_lexical_shadow(
        strip_lexical_terminal_references(lexical_text),
        heading_anchors,
    )
    index_parts = [r"\printindex[iv]"]
    parts = [
        r"\mainmatter",
        intro,
        r"\part{Sound changes, formalization, and relative chronology}",
        chronology,
        r"\part{Lexical derivations}",
        lexical,
        r"\backmatter",
        "# References",
        "",
        "::: {#refs}",
        ":::",
        "",
        r"\part*{Index verborum}",
        r"\addcontentsline{toc}{part}{Index verborum}",
        *index_parts,
    ]
    return "\n\n".join(parts) + "\n"


def main() -> None:
    OUTPUT_PATH.write_text(build_shadow_markdown(), encoding="utf-8")
    print(f"Generated shadow Markdown: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
