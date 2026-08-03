#!/usr/bin/env python3
"""Assemble capr_book_draft_alpha_01.md from production sources.

Two render modes are supported:

``raw``   (default, production)
    Non-explicit index emissions are inserted as raw ``\\index[iv]{...}``
    commands in the Markdown.  This is the canonical production path used by
    ``main()`` and the Docker build.  The output must be byte-identical to the
    tracked ``capr_book_draft_alpha_01.md``.

``anchor``  (shadow validation only — never written to the canonical path)
    Non-explicit emissions are replaced by strict ``.iv-anchor`` block markers::

        ::: {.iv-anchor emission_id="emit:xxx"}
        :::

    The Lua filter looks up each ``emission_id`` in ``book_emissions.tsv`` and
    emits the Python-precomputed ``index_command`` verbatim.  This mode is used
    by ``check_anchor_shadow.py`` to prove that the anchor path produces exactly
    the same ``\\index[iv]`` commands as the raw path.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "Germanic" / "tools"))
from index_verborum_emission import build_emission_table, load_model_entry_headings, load_print_main
INTRO_PATH = SCRIPT_DIR / "capr_book_intro_alpha_01.md"
CHRONOLOGY_PATH = REPO_ROOT / "Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_19.md"
LEXICAL_PATH = SCRIPT_DIR / "lexical_volume_alpha_01.md"
PRINT_MAIN_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_print_main.tsv"
LANGUAGE_REGISTRY_PATH = REPO_ROOT / "Germanic/docs/book/index_verborum_languages.tsv"
MANIFEST_PATH = SCRIPT_DIR / "manifest_all_by_class.tsv"
OUTPUT_PATH = SCRIPT_DIR / "capr_book_draft_alpha_01.md"
NESTED_RECON_IV_RE = re.compile(r"\[\[(?P<form>[^\]]+)\]\{\.recon\}(?P<tail>.*?)\]\{(?P<attrs>[^}]*)\}")
EXPLICIT_TAG_RE = re.compile(r"\[(?P<content>[^\]]+)\]\{(?P<attrs>[^}]*)\}")


# ── Emission record ───────────────────────────────────────────────────────────

@dataclass(frozen=True)
class BookEmission:
    """One canonical planned book emission from ``book_emissions.tsv``."""
    emission_id: str
    representative_occurrence_id: str
    emission_path: str
    site: str
    index_command: str

    def as_raw(self) -> str:
        """The raw ``\\index[iv]{...}`` command used by the production path."""
        return self.index_command

    def as_anchor(self) -> str:
        """A strict block ``.iv-anchor`` marker used by the shadow/anchor path.

        Only ``emission_id`` is carried on the marker. No semantic fields
        (language, form, sort key, command text, etc.) appear in the Markdown;
        they are resolved at build time by the Lua filter from ``book_emissions.tsv``.
        """
        eid = self.emission_id.replace('"', "&quot;")
        return f'::: {{.iv-anchor emission_id="{eid}"}}\n:::'


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


def load_production_rows() -> tuple[
    dict[str, list[BookEmission]],
    dict[str, dict[int, list[BookEmission]]],
    list[str],
]:
    """Load the canonical book emission plan and return ordered emission maps.

    Returns:
        emissions_by_heading_ref: heading site → ordered list of BookEmission
        emissions_by_line_ref:    path → {line_no → ordered list of BookEmission}
        unused:                   empty list (retained for API compatibility)
    """
    emissions_by_heading_ref: dict[str, list[BookEmission]] = defaultdict(list)
    emissions_by_line_ref: dict[str, dict[int, list[BookEmission]]] = defaultdict(
        lambda: defaultdict(list)
    )
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
        epath = row.get("emission_path", "")
        if epath == "explicit_tag":
            continue
        emission = BookEmission(
            emission_id=emission_id,
            representative_occurrence_id=row.get("representative_occurrence_id", ""),
            emission_path=epath,
            site=row.get("site", ""),
            index_command=row.get("index_command", ""),
        )
        site = emission.site
        if epath == "heading_injection":
            emissions_by_heading_ref[site].append(emission)
        elif epath == "line_injection":
            if ".md:" not in site:
                continue
            path_part, line_part = site.rsplit(":", 1)
            if not line_part.isdigit():
                continue
            emissions_by_line_ref[path_part][int(line_part)].append(emission)
    return emissions_by_heading_ref, emissions_by_line_ref, []


def annotate_explicit_tags_in_line(line: str, rel_path: str, line_no: int) -> str:
    source_ref = f'{rel_path}:{line_no}'
    span_counter = [0]  # mutable for closure; counts ALL .iv/.pred spans on this line

    def _make_attrs_with_provenance(existing_attrs: str) -> str | None:
        """Return augmented attrs string or None if span already has source_ref."""
        if re.search(r'(^|\s)source_ref=', existing_attrs):
            return None  # already annotated by upstream (model-entry builder)
        span_counter[0] += 1
        occ_id = f'{source_ref}:{span_counter[0]}'
        body = existing_attrs.strip()
        new_attrs = f'source_ref="{source_ref}" occ_id="{occ_id}"'
        return f'{body} {new_attrs}' if body else new_attrs

    def repl_nested(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if not (has_tag_class(attrs, "iv") or has_tag_class(attrs, "pred")):
            return match.group(0)
        new_attrs = _make_attrs_with_provenance(attrs)
        if new_attrs is None:
            return match.group(0)
        return f"[[{match.group('form')}]{{.recon}}{match.group('tail')}]{{{new_attrs}}}"

    def repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if not (has_tag_class(attrs, "iv") or has_tag_class(attrs, "pred")):
            return match.group(0)
        new_attrs = _make_attrs_with_provenance(attrs)
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


def _render_emissions(
    emissions: list[BookEmission],
    render_mode: str,
) -> list[str]:
    """Convert a list of BookEmissions to renderable strings for the given mode.

    raw:    one ``\\index[iv]{...}`` string per emission
    anchor: one ``::: {.iv-anchor emission_id="emit:..."}\n:::`` block per emission
    """
    if render_mode == "raw":
        return [e.as_raw() for e in emissions]
    elif render_mode == "anchor":
        return [e.as_anchor() for e in emissions]
    else:
        raise ValueError(f"Unknown render_mode {render_mode!r}; expected 'raw' or 'anchor'")


def inject_line_commands(
    path: Path,
    line_emissions: dict[str, dict[int, list[BookEmission]]],
    render_mode: str = "raw",
) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    emissions_for_file = line_emissions.get(rel, {})
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    for idx, line in enumerate(lines, start=1):
        out.append(annotate_explicit_tags_in_line(line, rel, idx))
        if idx in emissions_for_file:
            out.extend(_render_emissions(emissions_for_file[idx], render_mode))
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
    """Remove trailing \clearpage + ## References that terminates the standalone lexical volume."""
    text = re.sub(r'\s*\\clearpage\s*\n\s*## References.*$', '', text, flags=re.DOTALL)
    return text


_HIST_CHAPTER_RE = re.compile(r"^# Chapter \d+\. (.+)$")


def transform_chronology(text: str) -> str:
    """Emit the reader-facing chronology at correct heading levels for the book.

    The preamble before the first historical chapter (Scope and orientation,
    Numbering note) becomes an unnumbered chapter so it consumes no chapter
    number.  Its sections become unnumbered sections.

    Each ``# Chapter N. TITLE`` heading in the source becomes a real numbered
    book chapter at ``#`` level (``# TITLE``, dropping the ``Chapter N.`` prefix).

    Individual sound-change entries (``# Name``) are demoted to ``##`` sections
    within their historical chapter.

    Headings that appear directly under a historical chapter introduction
    (``## ...``) stay at ``##`` level.  Headings that appear inside a
    sound-change entry (``## Historical discussion``, ``## SC049. ...``) are
    demoted to ``###`` subsections.  This is tracked via the ``in_intro`` flag
    which is True after a ``# Chapter N.`` heading and False after the first
    plain ``# SoundChange`` heading within a chapter.

    ``###`` headings in chapter introductions (e.g. ``### West Germanic rhotacism
    (SC003)`` in the Chapter 3 intro) stay at ``###``.
    """
    out: list[str] = []
    preamble: list[str] = []
    seen_chapter = False
    in_intro = False          # True = inside historical chapter intro
                              # False = inside a sound-change entry

    for line in strip_title_block(strip_references(text)).splitlines():
        m = _HIST_CHAPTER_RE.match(line)
        if m:
            # Historical chapter heading
            if not seen_chapter and preamble:
                # Emit accumulated preamble as an unnumbered chapter so it
                # sits visibly between the \part heading and Chapter 2
                # without consuming a chapter counter number.
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
            # Still accumulating preamble
            preamble.append(line)
        elif line.startswith("# "):
            # Sound-change entry (not a historical chapter heading)
            in_intro = False
            out.append("## " + line[2:])
        elif line.startswith("## "):
            if in_intro:
                # Chapter-introduction section → stays at ## (section in chapter)
                out.append(line)
            else:
                # Sound-change subsection → ### (subsection of sound-change section)
                out.append("### " + line[3:])
        elif line.startswith("### "):
            if in_intro:
                # Chapter-introduction sub-section (e.g. SC list in chap3 intro)
                out.append(line)
            else:
                # Deeper nesting inside a sound-change entry → ####
                out.append("#### " + line[4:])
        else:
            out.append(line)

    return "\n".join(out).rstrip()


_PART_HEADING_RE = re.compile(r"^## Part [IVX]+\.\s+(.+)$")


def transform_lexical(
    text: str,
    emissions_by_ref: dict[str, list[BookEmission]],
    render_mode: str = "raw",
) -> str:
    """Emit lexical material at correct heading levels for the book.

    Front matter (Introduction, Data and sources, Transducer and derivation
    method, Derivation classes) becomes an unnumbered ``# Word-by-word
    derivations {.unnumbered}`` chapter so it consumes no chapter number,
    analogous to the Part I Sound-change overview.

    Each ``## Part N. TITLE`` heading becomes a real book chapter (``# TITLE``).
    Lexical entries (``### word — OE form``) become sections (``## word — OE form``).
    Entry subsections (``#### Derivation trace`` etc.) become subsections (``###``).
    """
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
                # Emit front matter as unnumbered chapter with unnumbered sections
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
            # Lexical entry heading: demote to ## (section within derivation-class chapter)
            entry_text = line[3:]  # keep the leading space from "### "
            out.append("##" + entry_text)
            # Inject index emissions after each entry heading
            ref = line[4:].strip()
            if " — OE _" in ref and ref.endswith("_"):
                lexical_item, target = ref.split(" — OE ", 1)
                cleaned_target = target[1:-1].replace('\\*', '*')
                ref = f"{lexical_item} — OE {cleaned_target}"
            emissions = emissions_by_ref.get(ref, [])
            if emissions:
                out.append("")
                out.extend(_render_emissions(emissions, render_mode))
        elif line.startswith("#### "):
            # Entry subsection (Derivation trace, Reconstruction...) → ###
            out.append("###" + line[4:])
        elif line.startswith("##### "):
            out.append("####" + line[5:])
        else:
            out.append(line)

    return "\n".join(out).rstrip()


def build_book_markdown(render_mode: str = "raw") -> str:
    """Assemble the full book Markdown.

    ``render_mode`` controls how non-explicit index emissions are rendered:

    ``"raw"``     (default) — inserts precomputed ``\\index[iv]{...}`` commands.
                  Used by ``main()`` and the Docker build.  The output must be
                  byte-identical to the tracked ``capr_book_draft_alpha_01.md``.

    ``"anchor"``  — inserts ``.iv-anchor`` block markers with ``emission_id``
                  attributes only.  Used by the shadow check to prove that the
                  Lua anchor path produces the same commands as the raw path.
                  Never written to the canonical output file.
    """
    if render_mode not in ("raw", "anchor"):
        raise ValueError(f"render_mode must be 'raw' or 'anchor', got {render_mode!r}")
    emissions_by_ref, line_emissions, _ = load_production_rows()
    intro = inject_line_commands(INTRO_PATH, line_emissions, render_mode)
    chronology = transform_chronology(inject_line_commands(CHRONOLOGY_PATH, line_emissions, render_mode))
    lexical_text = annotate_explicit_tags_with_source_ref(LEXICAL_PATH, LEXICAL_PATH.read_text(encoding="utf-8"))
    lexical = transform_lexical(
        strip_lexical_terminal_references(lexical_text),
        emissions_by_ref,
        render_mode,
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
    OUTPUT_PATH.write_text(build_book_markdown(), encoding="utf-8")
    print(f"Generated {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
