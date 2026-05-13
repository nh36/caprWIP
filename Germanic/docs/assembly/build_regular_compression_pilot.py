#!/usr/bin/env python3
from __future__ import annotations

import csv
import sys
from pathlib import Path

import build_full_lexical_volume as full


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
REGULAR_MANIFEST_PATH = SCRIPT_DIR / "manifest_regular.tsv"
PILOT_MANIFEST_PATH = SCRIPT_DIR / "regular_compression_pilot_manifest.tsv"
OUTPUT_PATH = SCRIPT_DIR / "regular_compression_pilot_01.md"
TRACE_REPORT_PATH = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md"

CORE_COMMENTARY_HEADINGS = {
    "Reconstruction and comparative evidence",
    "Old English evidence",
    "Development to Old English",
}
NOTE_HEADINGS = {
    "Source note",
    "Dialect note",
    "Form note",
    "Development note",
}
COMPARISON_HEADINGS = {
    "Form comparison",
    "Variant comparison",
    "Comparison",
}

SAMPLE_SELECTION = [
    (
        "1934",
        "ordinary weak verb with straightforward regular prose",
        "simple verb; baseline regular commentary",
    ),
    (
        "1942",
        "very simple regular noun with compact explanatory prose",
        "simple noun; minimal-style candidate",
    ),
    (
        "1949",
        "simple noun with a short Source note",
        "simple noun; source-note retention case",
    ),
    (
        "1958",
        "monosyllabic numeral with a manual comparison table and paradigm complexity",
        "manual comparison table; paradigm complexity",
    ),
    (
        "1961",
        "ordinary weak verb with a compact but nontrivial developmental chain",
        "ordinary verb; fuller regular narrative",
    ),
    (
        "2003",
        "ordinary strong verb with simple evidence and development prose",
        "ordinary verb; baseline compression target",
    ),
    (
        "2049",
        "regular noun with an explicit Dialect note",
        "dialect-note retention case",
    ),
    (
        "2095",
        "regular verb with dialect framing and a manual comparison table",
        "manual comparison table; dialect complexity",
    ),
    (
        "2104",
        "very simple regular noun with a brief Form note",
        "simple noun; form-note retention case",
    ),
    (
        "2129",
        "regular kinship noun whose final section is a short comparison note rather than a table",
        "comparison prose without table",
    ),
    (
        "2186",
        "ordinary regular verb with an orthographic Form note",
        "verb; form-note retention case",
    ),
    (
        "2278",
        "regular noun with unbroken/broken-form commentary in a Form note",
        "noun; form-note retention case",
    ),
]


def section_name(heading: str) -> str:
    return heading.removeprefix("### ").strip()


def section_has_table(body: str) -> bool:
    return any(line.lstrip().startswith("|") for line in body.splitlines())


def entry_shell(model: dict[str, object], trace_entry: dict[str, str] | None) -> list[str]:
    lines = [f"### {model['title']}", "", full.derivation_summary(model, trace_entry)]
    if trace_entry is not None:
        lines.extend(
            [
                "",
                "#### Derivation trace",
                "",
                f"Proto input: {full.italicize_form(trace_entry['proto_input'])}",
                "",
                *full.render_trace_table(trace_entry),
            ]
        )
    return lines


def render_variant_a(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    return full.rewrite_entry(model, trace_entry)


def render_variant_b(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    lines = entry_shell(model, trace_entry)
    commentary_parts: list[str] = []
    retained_sections: list[tuple[str, str]] = []

    for heading, body in model["sections"]:
        name = section_name(heading)
        if name == "Transducer input and output":
            continue
        cleaned = full.tidy_prose(body)
        if not cleaned:
            continue
        if name in CORE_COMMENTARY_HEADINGS:
            commentary_parts.append(cleaned)
            continue
        if name in COMPARISON_HEADINGS:
            retained_sections.append(("Comparison", cleaned))
            continue
        retained_sections.append((name, cleaned))

    if commentary_parts:
        lines.extend(["", "#### Commentary", "", "\n\n".join(commentary_parts)])

    for heading, cleaned in retained_sections:
        lines.extend(["", f"#### {heading}", "", cleaned])

    return "\n".join(lines).strip()


def render_variant_c(model: dict[str, object], trace_entry: dict[str, str] | None) -> str:
    lines = entry_shell(model, trace_entry)

    for heading, body in model["sections"]:
        name = section_name(heading)
        if name == "Transducer input and output":
            continue
        cleaned = full.tidy_prose(body)
        if not cleaned:
            continue
        if name in NOTE_HEADINGS:
            lines.extend(["", f"#### {name}", "", cleaned])
            continue
        if name in COMPARISON_HEADINGS:
            lines.extend(
                [
                    "",
                    "#### Comparison",
                    "",
                    "_Manual comparison retained only in fuller variants._"
                    if section_has_table(body)
                    else cleaned,
                ]
            )

    return "\n".join(lines).strip()


def load_sample_rows() -> list[dict[str, str]]:
    with REGULAR_MANIFEST_PATH.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))

    by_row_id = {row["row_id"]: row for row in rows}
    selected_rows: list[dict[str, str]] = []
    for row_id, reason, features in SAMPLE_SELECTION:
        row = by_row_id.get(row_id)
        if row is None:
            raise ValueError(f"sample row {row_id} missing from {REGULAR_MANIFEST_PATH}")
        enriched = dict(row)
        enriched["pilot_reason"] = reason
        enriched["pilot_features"] = features
        selected_rows.append(enriched)
    return selected_rows


def write_pilot_manifest(rows: list[dict[str, str]]) -> None:
    fieldnames = list(rows[0].keys())
    with PILOT_MANIFEST_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def build_document(rows: list[dict[str, str]]) -> str:
    trace_entries = full.parse_trace_entries(TRACE_REPORT_PATH.read_text(encoding="utf-8"))
    lines: list[str] = [
        "# Regular-entry compression pilot 01",
        "",
        "_Assembly-only pilot comparing the current full regular-entry rendering with shorter book-like variants. Source model entries are unchanged._",
        "",
        "## Sample",
        "",
        "This pilot samples 12 regular entries chosen to cover very simple nouns, ordinary verbs, short note sections, dialect/source notes, and manual comparison cases.",
        "",
        "See `regular_compression_pilot_manifest.tsv` for the selected rows and sample reasons.",
        "",
        "## Variant A: current style baseline",
        "",
    ]

    variant_b_entries: list[str] = []
    variant_c_entries: list[str] = []

    for row in rows:
        entry_path = REPO_ROOT / row["model_entry_path"]
        model = full.parse_model_entry(entry_path)
        trace_entry, basis, confident = full.match_trace_entry(model, trace_entries)
        if trace_entry is None or not confident:
            raise ValueError(f"trace match unresolved for {entry_path.name} ({basis})")
        print(
            f"Matched {entry_path.name} -> {trace_entry['title']} / {trace_entry['proto']} / {trace_entry['outputs']} ({basis})",
            file=sys.stderr,
        )
        lines.extend([render_variant_a(model, trace_entry), ""])
        variant_b_entries.extend([render_variant_b(model, trace_entry), ""])
        variant_c_entries.extend([render_variant_c(model, trace_entry), ""])

    lines.extend(
        [
            r"\clearpage",
            "",
            "## Variant B: compact regular style",
            "",
            "These entries keep the heading, derivation line, and boxed trace, but merge the three standard prose sections into one commentary block and retain only shorter note/comparison sections separately.",
            "",
            *variant_b_entries,
            r"\clearpage",
            "",
            "## Variant C: minimal regular style (experimental)",
            "",
            "These entries keep the heading, derivation line, and boxed trace, then retain only explicit short note sections. Manual comparison tables are replaced by a mechanical editorial placeholder.",
            "",
            *variant_c_entries,
            r"\clearpage",
            "",
            "## References",
            "",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    rows = load_sample_rows()
    write_pilot_manifest(rows)
    OUTPUT_PATH.write_text(build_document(rows), encoding="utf-8")
    print(f"Generated {PILOT_MANIFEST_PATH}")
    print(f"Generated {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
