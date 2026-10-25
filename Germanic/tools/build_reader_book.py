#!/usr/bin/env python3
"""Assemble the Version 1 reader-facing book section from the generated manifest.

The book's file list and chapter boundaries are NOT typed here: they come from
the GENERATED registry/reader_manifest.tsv (sources: sc_registry.tsv +
oe_pipeline + reader_chapters.tsv boundary anchors). Chapter titles and intro
files come from the human registry/reader_chapters.tsv. This builder holds only
presentation logic (front matter, chapter blocks, heading wrapping, link
resolution) plus the manifest-coverage report.

Outputs (both under docs/sound_changes/reader_facing/):
  * reader_facing_local_section_20.md
  * reader_facing_manifest_coverage_08.md

Usage:
    python3 Germanic/tools/build_reader_book.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import generate_registry_views

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
REGISTRY_DIR = SC_DIR / "registry"
READER_MANIFEST = REGISTRY_DIR / "reader_manifest.tsv"
READER_CHAPTERS = REGISTRY_DIR / "reader_chapters.tsv"
READER_ROOT = SC_DIR / "reader_facing"
REPORT_MANIFEST = SC_DIR / "change_reports/report_manifest.tsv"

OUT_MD = READER_ROOT / "reader_facing_local_section_20.md"
OUT_COVERAGE = READER_ROOT / "reader_facing_manifest_coverage_08.md"

rule_heading_re = re.compile(
    r"^##\s+(SC\d{3})\.\s+(.*?)\s+\(`([^`]+)`\)\s+\{#(rule-[^}]+)\}\s*$")
link_re = re.compile(r"\[([^\]]+)\]\((#rule-[^)]+)\)")
long_rule_heading_threshold = 65

# Front-matter prose for the assembled section. Editorial content, owned here.
parts_front: list[str] = [
    "# The ordered sound-change sequence",
    "",
    "## Scope and orientation",
    "",
    "The sequence follows the executable reconstruction from its early Germanic"
    " developments through the Old English written surface.",
    "",
    "Rhotacism, brightening, breaking, umlaut, and apocope alternate with narrowly"
    " conditioned changes whose relative order rests on particular witness words.",
    "",
    "The evidence ranges from broadly attested sound laws to lexical constraints"
    " that establish only one chronological boundary.",
    "",
    "## Numbering note",
    "",
    "SC numbers remain stable legacy identifiers, not chronological positions."
    " Each published entry has one authoritative source. The book automatically"
    " follows the individual stages of the canonical executable reconstruction;"
    " neither filenames nor chapter membership can override that order.",
    "",
    "This is the order adopted by the executable reconstruction, not a claim"
    " that every pairwise historical chronology has been independently proved."
    " Adjudication records distinguish demonstrated chronology, stage-entailed"
    " relations and computational serialization. Chapter boundaries and titles"
    " remain editorial; they divide the sequence without rearranging its entries.",
    "",
    "Explicitly retained technical explanations are published at their executable"
    " positions without becoming adjudicated historical sound laws.",
    "",
    "SC038, SC062, and SC084 mark technical or prosodic stages rather than sound"
    " changes; SC113 annotates stress-foot context and is not a published law."
    " SC077 is unused.",
    "",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def load_manifest() -> tuple[list[dict[str, str]], dict[str, dict[str, str]]]:
    expected = generate_registry_views.build_reader_manifest(
        generate_registry_views.read_tsv(generate_registry_views.SC_REGISTRY),
        read_tsv(READER_CHAPTERS), reader_root=READER_ROOT)
    if READER_MANIFEST.read_text(encoding="utf-8") != expected:
        raise ValueError("Reader manifest is stale: run "
                         "python3 Germanic/tools/adjudicate.py --refresh")
    manifest = read_tsv(READER_MANIFEST)
    chapters = {c["chapter_id"]: c for c in read_tsv(READER_CHAPTERS)}
    return manifest, chapters


def heading_visible_text(sc_number: str, title: str, rule_name: str) -> str:
    visible = title
    visible = re.sub(r"\\[A-Za-z]+\{([^{}]*)\}", r"\1", visible)
    visible = visible.replace("{", "").replace("}", "")
    visible = re.sub(r"\\[A-Za-z]+", "", visible)
    visible = re.sub(r"\s+", " ", visible).strip()
    return f"{sc_number}. {visible} ({rule_name})"


def wrap_long_rule_headings(text: str) -> str:
    wrapped: list[str] = []
    for line in text.splitlines():
        match = rule_heading_re.match(line.strip())
        if not match:
            wrapped.append(line)
            continue
        sc_number, title, rule_name, anchor = match.groups()
        if len(heading_visible_text(sc_number, title, rule_name)) <= long_rule_heading_threshold:
            wrapped.append(line)
            continue
        latex_title = title.replace(r"\*", "*")
        wrapped.append(
            f"## \\CAPRRuleHeading{{{sc_number}. {latex_title}}}"
            f"{{{rule_name}}} {{#{anchor}}}"
        )
    return "\n".join(wrapped)


def nest_entry_headings(text: str) -> str:
    """Keep entry titles and their subsections below the five real chapters."""
    lines = []
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and re.match(r"^#{1,6} ", line):
            if line.startswith("###### "):
                raise ValueError("Reader entry heading is too deep to nest below a chapter")
            line = "#" + line
        lines.append(line)
    return "\n".join(lines)


def inject_chapter_block(chapter_num: str, title: str, intro_file: str) -> list[str]:
    """Return markdown lines for a chapter heading and intro."""
    block: list[str] = [
        "",
        r"\newpage",
        "",
        f"# Chapter {chapter_num}. {title}",
        "",
    ]
    intro_path = READER_ROOT / intro_file
    intro_text = intro_path.read_text(encoding="utf-8").strip()
    # The chapter title is rendered above, not repeated from its source.
    intro_lines = intro_text.splitlines()
    if intro_lines and intro_lines[0].startswith("# "):
        intro_lines = intro_lines[1:]
    block.extend(intro_lines)
    block.append("")
    return block


def render() -> dict[Path, str]:
    """Render every output to text without touching the filesystem."""
    manifest, chapters = load_manifest()
    manifest_files = [row["reader_file"] for row in manifest]

    active_anchors: set[str] = set()
    file_sc_map: dict[str, list[str]] = {}
    reader_sc_numbers: list[str] = []
    seen_sc: set[str] = set()

    for name in manifest_files:
        text = (READER_ROOT / name).read_text(encoding="utf-8")
        scs: list[str] = []
        for line in text.splitlines():
            match = rule_heading_re.match(line.strip())
            if not match:
                continue
            sc_number = match.group(1)
            scs.append(sc_number)
            active_anchors.add(f"#{match.group(4)}")
            if sc_number not in seen_sc:
                seen_sc.add(sc_number)
                reader_sc_numbers.append(sc_number)
        file_sc_map[name] = sorted(set(scs), key=lambda item: int(item[2:]))

    def resolve_links(text: str) -> str:
        return link_re.sub(
            lambda match: match.group(0) if match.group(2) in active_anchors
            else match.group(1), text)

    parts = list(parts_front)
    prev_chapter = None
    for row in manifest:
        name = row["reader_file"]
        chapter_id = row["chapter_id"]
        if chapter_id != prev_chapter:
            chapter = chapters[chapter_id]
            parts.extend(inject_chapter_block(
                chapter_id, chapter["title"], chapter["intro_file"]))
            prev_chapter = chapter_id
        parts.append("")
        chapter_text = resolve_links(
            (READER_ROOT / name).read_text(encoding="utf-8").rstrip())
        parts.append(nest_entry_headings(wrap_long_rule_headings(chapter_text)))

    parts.extend([
        "",
        r"\newpage",
        "",
        "# References",
        "",
        "::: {#refs}",
        ":::",
        "",
    ])

    return {
        OUT_MD: "\n".join(parts),
        OUT_COVERAGE: render_coverage_report(
            manifest_files, file_sc_map, reader_sc_numbers),
    }


def build() -> None:
    for path, text in render().items():
        path.write_text(text, encoding="utf-8")


def render_coverage_report(manifest_files: list[str],
                           file_sc_map: dict[str, list[str]],
                           reader_sc_numbers: list[str]) -> str:
    reg = read_tsv(generate_registry_views.SC_REGISTRY)
    published = {r["sc_id"]: r for r in reg if r["lifecycle_status"] == "active"
                 and r["include_in_volume"] == r["is_reader_facing"] == "yes"}
    # load_manifest owns exact executable parity; coverage checks the actual
    # sections against the independently classified registry population.
    expected = reader_sc_numbers
    if set(expected) != published.keys() or len(expected) != len(published):
        raise ValueError("Reader coverage differs from canonical publication "
                         "registry; run adjudicate.py --refresh")
    if manifest_files != [published[sc]["source_reader_facing_file"] for sc in expected]:
        raise ValueError("Reader coverage has incorrect canonical source ownership")
    for sc, name in zip(expected, manifest_files):
        if file_sc_map[name] != [sc] or not (READER_ROOT / name).is_file():
            raise ValueError(f"Reader coverage: missing or conflicting {sc} source {name}")

    status = {}
    for r in reg:
        status[r["sc_id"]] = (
            "retired" if r["lifecycle_status"] == "retired" else
            "published technical support" if r["sc_id"] in published
            and r["entry_type"] == "support_stage" else
            "published " + r["entry_type"] if r["sc_id"] in published else
            "active, deliberately unpublished")
    lines = [
        "# Reader-facing manifest coverage 08", "",
        "## Canonical publication coverage", "",
        "Authority: `registry/sc_registry.tsv` publication/lifecycle/source ownership "
        "and the canonical `oe_pipeline` stage sequence. The generated reader manifest "
        "and actual section sequence must agree exactly; omissions fail the build.", "",
        f"Published identities: {len(expected)}. Missing or erroneous omissions: 0.", "",
        "| Reader position | Identity | Classification | Authoritative source |",
        "| --- | --- | --- | --- |",
    ]
    for i, sc in enumerate(expected, 1):
        lines.append(f"| {i} | {sc} | {status[sc]} | "
                     f"`{published[sc]['source_reader_facing_file']}` |")
    lines += ["", "## Retired and deliberately unpublished identities", "",
              "| Identity | Classification |", "| --- | --- |"]
    for r in reg:
        if r["sc_id"] not in published:
            lines.append(f"| {r['sc_id']} | {status[r['sc_id']]} |")
    lines += ["", "## Secondary historical change-report comparison", "",
              "`change_reports/report_manifest.tsv` records a different, older "
              "report population, not the current publication specification. "
              "Absence from it is not a publication error. Its retired or deliberately "
              "unpublished identities are classified rather than called missing.", "",
              "| Historical report | Identities and current classification |",
              "| --- | --- |"]
    historical_ids = set()
    for row in read_tsv(REPORT_MANIFEST):
        scs = [sc.strip() for sc in row["CHANGE_IDS"].split(";") if sc.strip()]
        historical_ids.update(scs)
        unknown = set(scs) - status.keys()
        if unknown:
            raise ValueError(f"Historical report {row['ID']} has unknown identities: {sorted(unknown)}")
        lines.append(f"| {row['ID']} | " +
                     "; ".join(f"{sc}: {status[sc]}" for sc in scs) + " |")
    lines += ["", "Published identities outside that historical report population: " +
              ", ".join(sc for sc in expected if sc not in historical_ids) + ".", ""]
    return "\n".join(lines)


def main() -> int:
    build()
    print(f"Generated {OUT_MD}")
    print(f"Generated {OUT_COVERAGE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
