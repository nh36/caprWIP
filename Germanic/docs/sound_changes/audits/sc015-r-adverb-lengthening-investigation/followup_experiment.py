#!/usr/bin/env python3
"""Bounded SC015 follow-up experiment for *there* and *where*.

This driver reuses the source validation, isolated Foma compilation,
checkpoint tracing, and protected-artifact contract from ``experiment.py``.
It adds only the two source-backed candidate rows and compares three
general final-*r* lengthening placements.  It never writes production files.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INVESTIGATION = Path(__file__).resolve().parent
TOOLS = ROOT / "Germanic" / "tools"
sys.path.insert(0, str(INVESTIGATION))
sys.path.insert(0, str(TOOLS))

import experiment as base
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import layout
from oe_input_context import InputContext


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_candidates(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    required = {
        "ID", "PROTOFORM", "COUNTERPART", "DOCULECT", "CONCEPT",
        "GLOSSID", "COGIDS", "DERIVATION_CLASS",
    }
    if not rows or not required <= set(rows[0]):
        raise ValueError("candidate dataset lacks required corpus columns")
    result = []
    for row in rows:
        if row["DOCULECT"] != "Old_English":
            raise ValueError("candidate dataset must contain Old_English rows only")
        norm = oe_pipeline.normalize_proto(row["PROTOFORM"])
        context = InputContext("stressed", "final")
        result.append({
            "id": row["ID"],
            "row_id": row["ID"],
            "concept": row["CONCEPT"],
            "proto": row["PROTOFORM"],
            "proto_norm": norm,
            "fst_input": context.encode(norm),
            "word_stress": context.word_stress,
            "phonological_finality": context.phonological_finality,
            "counterpart": row["COUNTERPART"],
            "glossid": row["GLOSSID"],
            "cogids": row["COGIDS"],
        })
    if {row["id"] for row in result} != {"2333", "2334"}:
        raise ValueError("candidate IDs must be exactly 2333 and 2334")
    return result


def lengthening_expression(late: bool = False) -> str:
    mappings = [
        ("á", "ā"), ("é", "ē"), ("í", "ī"), ("ó", "ō"), ("ú", "ū"),
    ]
    if late:
        mappings.append(("æ", "ǣ"))
    rewrites = ",\n    ".join(
        "{*" + source + "} -> {*" + target + "}"
        for source, target in mappings
    )
    return (
        "[ [EnglishStarAlphabet* .o. [\n    " + rewrites
        + "\n    || .#. EnglishStarConsonant* _ {*r} .#.\n] ] ]"
    )


def recipe(recipe_id: str, anchor: str, side: str, late: bool = False) -> dict:
    return {
        "id": recipe_id,
        "architecture": "A",
        "representation": "production-e-acute",
        "evidence": (
            "Source-backed short-a antecedents *hwar and *þar from the "
            "verified SC015 adverb evidence package; experiment only."
        ),
        "assumptions": (
            "General stressed monosyllabic final-r lengthening; the early "
            "model preserves inherited-r identity by preceding rhotacism. "
            + ("The late model must inspect post-brightening æ and therefore "
               "tests the loss of acute stress marking explicitly." if late else
               "No historical strict edge is inferred from executable position.")
        ),
        "definitions": {"XRAdverbLen": lengthening_expression(late)},
        "source_replacements": [],
        "symbols": [],
        "edits": [{"action": "insert", "rule": "XRAdverbLen",
                   "target": anchor, "side": side}],
        "probes": [],
    }


def probe_set() -> list[dict[str, str]]:
    return [
        {
            "id": "candidate-there", "fst_input": "θár",
            "kind": "adopted candidate witness",
            "evidence": "WITNESSES.tsv OE05/PG03",
            "historical_stage": "short-a antecedent; date disputed",
            "reconstruction_level": "source-backed conditional input",
        },
        {
            "id": "candidate-where", "fst_input": "xwár",
            "kind": "adopted candidate witness",
            "evidence": "WITNESSES.tsv OE02/PG02",
            "historical_stage": "short-a antecedent; date disputed",
            "reconstruction_level": "source-backed conditional input",
        },
        {
            "id": "disyllabic-there", "fst_input": "θára",
            "kind": "negative disyllabic control",
            "evidence": "WITNESSES.tsv RT02 control",
            "historical_stage": "comparative control",
            "reconstruction_level": "negative control",
        },
        {
            "id": "disyllabic-where", "fst_input": "xwára",
            "kind": "negative disyllabic control",
            "evidence": "WITNESSES.tsv RT02 control",
            "historical_stage": "comparative control",
            "reconstruction_level": "negative control",
        },
        {
            "id": "secondary-r", "fst_input": "*áza",
            "kind": "secondary-r stress/context control",
            "evidence": "Technical control for z > r and later loss of the final vowel",
            "historical_stage": "synthetic cascade control",
            "reconstruction_level": "negative control",
        },
        {
            "id": "inherited-r", "fst_input": "wíraz",
            "kind": "SC015 and z-environment control",
            "evidence": "WITNESSES.tsv hill-man-r-lowering",
            "historical_stage": "short-i inherited-r comparator",
            "reconstruction_level": "comparative control",
        },
        {
            "id": "inherited-e1", "fst_input": "xḗr",
            "kind": "inherited long-e1 control",
            "evidence": "WITNESSES.tsv synthetic-inherited-e1",
            "historical_stage": "inherited ē1 comparator",
            "reconstruction_level": "negative control",
        },
    ]


def selected_summary(rows: list[dict], outputs: dict[str, list[str]]) -> dict:
    matches = sum(row["counterpart"] in outputs[row["id"]] for row in rows)
    mismatches = [
        {
            "id": row["id"], "concept": row["concept"],
            "outputs": outputs[row["id"]], "target": row["counterpart"],
        }
        for row in rows if row["counterpart"] not in outputs[row["id"]]
    ]
    return {
        "selected_rows": len(rows),
        "matched": matches,
        "mismatched": len(mismatches),
        "mismatches": mismatches,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-tsv", type=Path, required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    rt = layout()
    if not rt.is_container:
        raise SystemExit("follow-up execution must run inside the backend container")
    if args.receipt.exists():
        raise SystemExit(f"refusing to overwrite {args.receipt}")
    candidates = read_candidates(args.candidate_tsv.resolve())
    original = assay.corpus_rows(rt.corpus_tsv)
    if len(original) != 387:
        raise SystemExit(f"expected 387 existing selected rows, got {len(original)}")
    rows = original + candidates
    source = rt.germanic_fst.read_text(encoding="utf-8")
    probes = probe_set()
    recipes = [
        recipe("early-before-rhotacism", "EAFRhotacism", "before"),
        recipe("intermediate-before-short-a-brightening", "EAFBrightening", "before"),
        recipe("late-after-short-a-brightening", "OEHighVowelApocope", "after", late=True),
    ]
    base_order = base.source_order(rt.germanic_fst)
    before = base.protected_hashes(rt)
    report = {
        "schema_version": 1,
        "status": "started",
        "candidate_sha256": digest(args.candidate_tsv.resolve()),
        "source_sha256": digest(rt.germanic_fst),
        "canonical_corpus_sha256": digest(rt.corpus_tsv),
        "candidate_rows": candidates,
        "recipes": recipes,
        "rows": rows,
        "models": [],
    }
    args.work_dir.mkdir(parents=True, exist_ok=True)
    try:
        version = __import__("subprocess").run(
            ["foma", "-v"], check=True, capture_output=True, text=True
        )
        report["foma_version"] = version.stdout + version.stderr
        for current in recipes:
            order = base.edited_order(base_order, current)
            directory = args.work_dir / current["id"]
            directory.mkdir()
            model = base.evaluate(source, current, order, rows, probes, directory)
            model["summary"] = selected_summary(rows, model["outputs"])
            model["original_deltas"] = [
                {
                    "id": row["id"], "concept": row["concept"],
                    "baseline": base_output,
                    "variant": model["outputs"][row["id"]],
                }
                for row, base_output in zip(
                    original,
                    report["models"][0]["outputs"].values()
                    if report["models"] else base.apply(
                        rt.bin_dir / "old_english.bin",
                        [oe_pipeline.evaluation_input(row) for row in original],
                    )
                )
                if base_output != model["outputs"][row["id"]]
            ]
            model["candidate_results"] = [
                {
                    "id": row["id"], "concept": row["concept"],
                    "input": row["fst_input"],
                    "target": row["counterpart"],
                    "outputs": model["outputs"][row["id"]],
                    "match": row["counterpart"] in model["outputs"][row["id"]],
                }
                for row in candidates
            ]
            model["probe_results"] = [
                {
                    "id": probe["id"], "outputs": probe["outputs"],
                    "firing_events": probe["firing_events"],
                }
                for probe in model["probes"]
            ]
            report["models"].append(model)
        report["baseline_existing"] = selected_summary(
            original,
            {row["id"]: base.apply(
                rt.bin_dir / "old_english.bin",
                [oe_pipeline.evaluation_input(row)]
            )[0] for row in original},
        )
        report["status"] = "complete"
    finally:
        after = base.protected_hashes(rt)
        report["protected_unchanged"] = before == after
        report["protected_changes"] = sorted(
            set(before) | set(after),
        )
        report["protected_changes"] = [
            path for path in report["protected_changes"]
            if before.get(path) != after.get(path)
        ]
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if not report["protected_unchanged"]:
        raise SystemExit("protected artifacts changed during experiment")
    print(json.dumps({
        "status": report["status"],
        "models": [
            {"id": model["recipe"]["id"], **model["summary"],
             "original_deltas": len(model["original_deltas"])}
            for model in report["models"]
        ],
        "receipt": str(args.receipt),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
