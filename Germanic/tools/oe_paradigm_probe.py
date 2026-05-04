#!/usr/bin/env python3
"""Probe candidate Proto-Germanic paradigm cells against the OE FST.

This is an intentionally small, explicit first pass for the lexeme-report
pilot. It supports:

1. Built-in pilot probes keyed by concept + optional counterpart.
2. Manual probes assembled from explicit --candidate specifications.

The tool does NOT attempt full Proto-Germanic morphology generation. Instead it
uses hand-specified cell templates for the pilot entries and records omitted
cells explicitly so the limitations are visible in the output.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from oe_full_trace_report import apply_down, normalize_proto


@dataclass(frozen=True)
class ProbeCandidate:
    cell: str
    candidate_input: str
    comment: str


@dataclass(frozen=True)
class ProbeSpec:
    concept: str
    counterpart: Optional[str]
    derivation_class: str
    morphology_note: str
    omitted_cells: tuple[str, ...]
    bypass_proto_gate: bool
    candidates: tuple[ProbeCandidate, ...]


def load_rows(tsv_path: Path) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    with tsv_path.open(encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("DOCULECT") != "Old_English":
                continue
            proto = (row.get("PROTOFORM") or "").strip()
            counterpart = (row.get("COUNTERPART") or "").strip()
            if not proto or not counterpart or counterpart == "-":
                continue
            rows.append(row)
    return rows


def find_row(
    rows: Iterable[Dict[str, str]],
    *,
    concept: Optional[str],
    counterpart: Optional[str],
) -> Dict[str, str]:
    matches = []
    for row in rows:
        if concept and row.get("CONCEPT") != concept:
            continue
        if counterpart and row.get("COUNTERPART") != counterpart:
            continue
        matches.append(row)
    if not matches:
        raise SystemExit("No matching Old English row found.")
    if len(matches) > 1:
        targets = ", ".join(sorted({row.get("COUNTERPART", "") for row in matches}))
        raise SystemExit(
            f"Concept lookup is ambiguous; pass --counterpart. Candidates: {targets}"
        )
    return matches[0]


def pilot_specs(row: Dict[str, str]) -> Dict[str, ProbeSpec]:
    return {
        "ban:bannes": ProbeSpec(
            concept="ban",
            counterpart="bannes",
            derivation_class="late_analogy",
            morphology_note="Hand-specified pilot comparison for n-stem singular cells.",
            omitted_cells=(
                "dat.sg. and plural cells omitted in v1; the pilot only compares the citation-form nomination against the selected gen.sg. cell.",
            ),
            bypass_proto_gate=False,
            candidates=(
                ProbeCandidate("nom.sg.", row["PROTO"], "Citation-form comparison."),
                ProbeCandidate("gen.sg.", row["PROTOFORM"], "Chosen paradigm-cell input in TSV."),
            ),
        ),
        "berry:berġes": ProbeSpec(
            concept="berry",
            counterpart="berġes",
            derivation_class="late_analogy",
            morphology_note="Hand-specified pilot comparison for ja-stem citation vs. selected gen.sg. cell.",
            omitted_cells=(
                "dat.sg. and plural cells omitted in v1; the pilot focuses on the nominative/genitive contrast discussed in the TSV note.",
            ),
            bypass_proto_gate=False,
            candidates=(
                ProbeCandidate("nom.sg.", row["PROTO"], "Citation proto."),
                ProbeCandidate("gen.sg.", row["PROTOFORM"], "Chosen gen.sg. cell in TSV."),
            ),
        ),
        "span:spanne": ProbeSpec(
            concept="span",
            counterpart="spanne",
            derivation_class="late_analogy",
            morphology_note="Hand-specified pilot comparison for feminine ō-stem singular cells.",
            omitted_cells=(
                "gen.sg. and plural cells omitted in v1; dat.sg. is the only selected cell explicitly justified in the row note and DEV_NOTES.",
            ),
            bypass_proto_gate=False,
            candidates=(
                ProbeCandidate("nom.sg.", row["PROTO"], "Citation nominative singular."),
                ProbeCandidate("dat.sg.", row["PROTOFORM"], "Chosen dative singular cell in TSV."),
            ),
        ),
        "thistle:þistles": ProbeSpec(
            concept="thistle",
            counterpart="þistles",
            derivation_class="late_analogy",
            morphology_note="Hand-specified pilot comparison for citation nom.sg. vs. selected gen.sg. cell.",
            omitted_cells=(
                "Alternative *i-root nominative and other oblique cells omitted in v1; they should be added once the raising/epenthesis question is formalized.",
            ),
            bypass_proto_gate=False,
            candidates=(
                ProbeCandidate("nom.sg.", row["PROTO"], "Citation proto used for comparison."),
                ProbeCandidate("gen.sg.", row["PROTOFORM"], "Chosen genitive singular cell in TSV."),
            ),
        ),
        "fire:fȳre": ProbeSpec(
            concept="fire",
            counterpart="fȳre",
            derivation_class="known_unmodelled",
            morphology_note="Hand-specified pilot comparison for the dat.sg. row input and the documented nominative-like outcome.",
            omitted_cells=(
                "The inherited citation-form template is not yet generated automatically in v1; the probe centers on the TSV dat.sg. input and the known-problems interpretation.",
            ),
            bypass_proto_gate=False,
            candidates=(
                ProbeCandidate("dat.sg.", row["PROTOFORM"], "TSV input; attested target has analogically restored -e."),
            ),
        ),
        "tap:tæppa": ProbeSpec(
            concept="tap",
            counterpart="tæppa",
            derivation_class="known_unmodelled",
            morphology_note="Hand-specified pilot comparison for n-stem singular cells drawn from DEV_NOTES and oe_known_problems.tsv.",
            omitted_cells=(
                "Plural cells omitted in v1; the ledger already states that no paradigm cell yields lautgesetzlich tæpp-.",
            ),
            bypass_proto_gate=False,
            candidates=(
                ProbeCandidate("nom.sg.", row["PROTOFORM"], "TSV input; ledger says this yields regular tappa."),
                ProbeCandidate("gen./dat./acc. stem", "*táppan", "Representative oblique-stem comparison from DEV_NOTES."),
            ),
        ),
    }


def parse_candidate(raw: str) -> ProbeCandidate:
    parts = [piece.strip() for piece in raw.split("|")]
    if len(parts) != 3 or not all(parts):
        raise SystemExit(
            "--candidate must use the form 'CELL | CANDIDATE_INPUT | COMMENT'"
        )
    return ProbeCandidate(parts[0], parts[1], parts[2])


def match_status(outputs: List[str], target: str) -> str:
    if not outputs:
        return "no"
    if target in outputs:
        return "yes" if len(outputs) == 1 else "partial"
    return "no"


def render_markdown(
    *,
    row: Optional[Dict[str, str]],
    target: str,
    spec: ProbeSpec,
    bin_path: Path,
) -> str:
    results = []
    for candidate in spec.candidates:
        outputs = apply_down(bin_path, normalize_proto(candidate.candidate_input))
        results.append(
            {
                "cell": candidate.cell,
                "candidate_input": candidate.candidate_input,
                "fst_output": ", ".join(outputs) if outputs else "+?",
                "status": match_status(outputs, target),
                "comment": candidate.comment,
            }
        )

    winners = [item for item in results if item["status"] == "yes"]
    unique_winner = "yes" if len(winners) == 1 else "no"

    lines = []
    title = target if row is None else f"{row['CONCEPT']} / {target}"
    lines.append(f"### Paradigm probe — {title}")
    lines.append("")
    if row is not None:
        lines.append(f"- PROTO: {row['PROTO']}")
        lines.append(f"- PROTOFORM: {row['PROTOFORM']}")
        lines.append(f"- DERIVATION_CLASS: {row['DERIVATION_CLASS']}")
    lines.append(f"- Morphology source: {spec.morphology_note}")
    lines.append(f"- ProtoGate bypassed: {'yes' if spec.bypass_proto_gate else 'no'}")
    lines.append(
        "- Generated cells: "
        + ", ".join(candidate.cell for candidate in spec.candidates)
    )
    if spec.omitted_cells:
        for item in spec.omitted_cells:
            lines.append(f"- Omitted cells: {item}")
    lines.append(f"- Winning form unique: {unique_winner}")
    lines.append("")
    lines.append("| Cell | Candidate input | FST output | Match? | Comment |")
    lines.append("|:---|:---|:---|:---|:---|")
    for item in results:
        lines.append(
            f"| {item['cell']} | {item['candidate_input']} | {item['fst_output']} | {item['status']} | {item['comment']} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--concept", help="OE concept label from the TSV")
    parser.add_argument("--counterpart", help="OE counterpart / target form")
    parser.add_argument(
        "--tsv",
        type=Path,
        default=repo_root / "Germanic" / "data" / "germanic-aligned-final.tsv",
        help="Aligned OE TSV (default: %(default)s)",
    )
    parser.add_argument(
        "--bin",
        type=Path,
        default=repo_root / "backend" / "old_english.bin",
        help="OE FST binary (default: %(default)s)",
    )
    parser.add_argument(
        "--proto",
        help="Manual-mode source proto label for display only.",
    )
    parser.add_argument(
        "--protoform",
        help="Manual-mode FST input label for display only.",
    )
    parser.add_argument(
        "--target",
        help="Manual-mode target form; also accepted as an alias for --counterpart in manual mode.",
    )
    parser.add_argument(
        "--derivation-class",
        default="manual_probe",
        help="Manual-mode derivation-class label (default: %(default)s)",
    )
    parser.add_argument(
        "--stem-class",
        default="manual",
        help="Manual-mode morphology label (default: %(default)s)",
    )
    parser.add_argument(
        "--candidate",
        action="append",
        default=[],
        help="Manual probe candidate in the form 'CELL | CANDIDATE_INPUT | COMMENT'.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional file path for the Markdown report. Defaults to stdout.",
    )
    args = parser.parse_args()

    bin_path = args.bin.expanduser().resolve()

    if args.concept:
        rows = load_rows(args.tsv.expanduser().resolve())
        row = find_row(rows, concept=args.concept, counterpart=args.counterpart)
        spec_map = pilot_specs(row)
        key = f"{row['CONCEPT']}:{row['COUNTERPART']}"
        if key not in spec_map:
            raise SystemExit(
                f"No built-in pilot probe is configured for {row['CONCEPT']} / {row['COUNTERPART']}."
            )
        markdown = render_markdown(
            row=row,
            target=row["COUNTERPART"],
            spec=spec_map[key],
            bin_path=bin_path,
        )
    else:
        if not args.target or not args.candidate:
            raise SystemExit(
                "Manual mode requires --target and at least one --candidate."
            )
        spec = ProbeSpec(
            concept=args.concept or "manual",
            counterpart=args.target,
            derivation_class=args.derivation_class,
            morphology_note=f"Manual probe ({args.stem_class}).",
            omitted_cells=(),
            bypass_proto_gate=False,
            candidates=tuple(parse_candidate(raw) for raw in args.candidate),
        )
        row = {
            "CONCEPT": args.concept or "manual",
            "COUNTERPART": args.target,
            "PROTO": args.proto or "",
            "PROTOFORM": args.protoform or args.proto or "",
            "DERIVATION_CLASS": args.derivation_class,
        }
        markdown = render_markdown(
            row=row,
            target=args.target,
            spec=spec,
            bin_path=bin_path,
        )

    if args.output:
        output_path = args.output.expanduser().resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown + "\n", encoding="utf-8")
        print(f"Wrote {output_path}")
    else:
        print(markdown)


if __name__ == "__main__":
    main()
