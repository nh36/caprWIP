#!/usr/bin/env python3
"""Compact a trace report: drop [no-change] lines, collapse internal stars.

Reads a trace report produced by oe_full_trace_report.py or
oe_derivation_class_trace_report.py and:
  1. Drops every stage line tagged ``[no-change]``.
  2. Rewrites starred forms so only the leading star survives, e.g.
     ``*n*ḗ*d*r*ō*n`` → ``*nḗdrōn``.
  3. Reflows the three development subsections (Proto-Northwest Germanic,
     Proto-West Germanic, Old English) into a two-column Markdown table.
  4. Moves NOTE fields to the end of each lexical entry.

Pure post-processing: takes a report path in, writes a new report out.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List

# Match a starred form: a leading `*`, followed by one or more star-segmented
# characters (each an optional `*` plus exactly one printable non-space char).
# Internal `*`s between characters are collapsed; the leading `*` is kept.
STARRED_FORM_RE = re.compile(r"\*(?:\*?[^\s*,])+")
# "## Section 4: Old English" -> "## Old English"
SECTION_PREFIX_RE = re.compile(r"^(#{1,6})\s+Section\s+\d+:\s*")
# "--- beech ---" -> lemma marker
LEMMA_RE = re.compile(r"^---\s+(.*?)\s+---$")
# Stage line label: "OEMedUnstressedULowering: ..."
STAGE_LABEL_RE = re.compile(r"^([A-Za-z][A-Za-z0-9]*):")
PWGMC_HEADER = "### Proto-West Germanic developments"
NWGMC_HEADER = "### Northwest Germanic developments"
OE_HEADER = "### Old English"
ORTHOGRAPHY_HEADER = "### Orthography & surface"


def split_camel(name: str) -> str:
    # "EAFFinalZDeletion" -> "PGmc Final Z Deletion"
    # Split "OE" prefix when followed by another capital (handles OEJ/OEI runs
    # where the camel-case heuristics below otherwise can't see a boundary).
    name = re.sub(r"^OE([A-Z])", r"OE \1", name)
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    name = re.sub(r"([A-Z])([A-Z][a-z])", r"\1 \2", name)
    # Re-merge well-known prefix tokens that the rules above split.
    name = name.replace("NW Gmc", "NWGmc")
    name = name.replace("PW Gmc", "PWGmc")
    name = name.replace("P Gmc", "PGmc")
    return name


def collapse_stars(token: str) -> str:
    # Token starts with `*`. Strip every other `*` after the first char.
    return "*" + token[1:].replace("*", "")


def compact_line(line: str) -> str:
    line = STARRED_FORM_RE.sub(lambda m: collapse_stars(m.group(0)), line)
    line = SECTION_PREFIX_RE.sub(lambda m: m.group(1) + " ", line)
    if line.startswith("OldEnglishRemoveStars:"):
        line = "Outcome:" + line[len("OldEnglishRemoveStars:") :]
    lemma = LEMMA_RE.match(line)
    if lemma:
        line = f"# {lemma.group(1)}"
    stage = STAGE_LABEL_RE.match(line)
    if stage:
        label = stage.group(1)
        # Skip a hard-coded set of single-word labels we don't want split.
        if label not in {"PROTO", "EXPECTED", "OUTPUTS", "NOTE", "Outcome"}:
            spaced = split_camel(label)
            if spaced != label:
                line = spaced + line[len(label):]
    return line


def trim_blank_edges(lines: List[str]) -> List[str]:
    start = 0
    end = len(lines)
    while start < end and lines[start] == "":
        start += 1
    while end > start and lines[end - 1] == "":
        end -= 1
    return lines[start:end]


def pad_section_headings(lines: List[str], blank_lines: int = 3) -> List[str]:
    padded: List[str] = []
    for line in lines:
        if line.startswith(("=== ", "# ", "### ")) and padded:
            while padded and padded[-1] == "":
                padded.pop()
            padded.extend([""] * blank_lines)
        padded.append(line)
    return padded


def format_table_cell(label: str, body_lines: List[str]) -> str:
    parts = [f"**{label}**"]
    if body_lines:
        parts.append("<br>".join(body_lines))
    return "<br>".join(parts)


def extract_section_body(lines: List[str], start: int) -> tuple[List[str], int]:
    body: List[str] = []
    i = start + 1
    while i < len(lines):
        line = lines[i]
        if line.startswith("### ") or line.startswith("# ") or line.startswith("=== "):
            break
        body.append(line)
        i += 1
    return trim_blank_edges(body), i


def rewrite_entry_development_sections(lines: List[str]) -> tuple[List[str], bool]:
    notes = [line for line in lines if line.startswith("NOTE:")]
    lines = [line for line in lines if not line.startswith("NOTE:")]
    headers = (PWGMC_HEADER, NWGMC_HEADER, OE_HEADER, ORTHOGRAPHY_HEADER)
    if any(lines.count(header) != 1 for header in headers):
        return lines, False

    pwgmc = lines.index(PWGMC_HEADER)
    nwgmc = lines.index(NWGMC_HEADER)
    old_english = lines.index(OE_HEADER)
    orthography = lines.index(ORTHOGRAPHY_HEADER)
    if not (pwgmc < nwgmc < old_english < orthography):
        return lines, False

    pwgmc_body, next_index = extract_section_body(lines, pwgmc)
    if next_index != nwgmc:
        return lines, False
    nwgmc_body, next_index = extract_section_body(lines, nwgmc)
    if next_index != old_english:
        return lines, False
    old_english_body, next_index = extract_section_body(lines, old_english)
    if next_index != orthography:
        return lines, False

    left_cell = (
        format_table_cell("Proto-Northwest Germanic", nwgmc_body)
        + "<br><br>"
        + format_table_cell("Proto-West Germanic", pwgmc_body)
    )
    right_cell = format_table_cell("Old English", old_english_body)

    prefix = trim_blank_edges(lines[:pwgmc])
    suffix = trim_blank_edges(lines[orthography:])
    rewritten = [
        *prefix,
        "",
        "| Earlier Germanic developments | Old English developments |",
        "|:---|:---|",
        f"| {left_cell} | {right_cell} |",
        "",
        *suffix,
    ]
    if notes:
        rewritten.extend(["", *notes])
    return rewritten, True


def rewrite_development_tables(lines: List[str]) -> tuple[List[str], List[str]]:
    rewritten: List[str] = []
    failed_entries: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.startswith("# "):
            rewritten.append(line)
            i += 1
            continue

        j = i + 1
        while j < len(lines) and not lines[j].startswith("# ") and not lines[j].startswith("=== "):
            j += 1
        entry = lines[i:j]
        updated_entry, transformed = rewrite_entry_development_sections(entry)
        if not transformed and any(header in entry for header in (PWGMC_HEADER, NWGMC_HEADER, OE_HEADER)):
            failed_entries.append(line[2:].strip())
        rewritten.extend(updated_entry)
        i = j

    return rewritten, failed_entries


def compact_report(text: str) -> str:
    filtered = []
    for line in text.splitlines():
        if "[no-change]" in line:
            continue
        filtered.append(compact_line(line))

    # Promote section headers from `##` to `###` so lemma `#` is more prominent.
    filtered = [
        ("### " + line[len("## "):]) if line.startswith("## ") else line
        for line in filtered
    ]

    # If a section header has no stage lines beneath it (all were dropped),
    # insert "[no change]" so empty sections are visible.
    out_lines: List[str] = []
    i = 0
    while i < len(filtered):
        line = filtered[i]
        out_lines.append(line)
        if line.startswith("### "):
            # Look ahead past blank lines to see if any content follows before
            # the next section/lexeme/bucket boundary.
            j = i + 1
            while j < len(filtered) and filtered[j] == "":
                j += 1
            terminates = (
                j >= len(filtered)
                or filtered[j].startswith("### ")
                or filtered[j].startswith("# ")
                or filtered[j].startswith("=== ")
            )
            if terminates:
                out_lines.append("")
                out_lines.append("[no change]")
        i += 1
    rewritten, _failed_entries = rewrite_development_tables(out_lines)
    padded = pad_section_headings(rewritten)
    return "\n".join(padded) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Trace report to compact")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output path (default: <input>.compact.txt)",
    )
    args = parser.parse_args()

    in_path: Path = args.input.expanduser().resolve()
    out_path: Path = (
        args.output.expanduser().resolve()
        if args.output
        else in_path.with_suffix(".compact.txt")
    )
    text = in_path.read_text(encoding="utf-8")
    out_path.write_text(compact_report(text), encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
