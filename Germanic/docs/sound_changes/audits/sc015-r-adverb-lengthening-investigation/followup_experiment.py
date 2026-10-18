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
import gzip
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INVESTIGATION = Path(__file__).resolve().parent
TOOLS = ROOT / "tools"
sys.path.insert(0, str(INVESTIGATION))
sys.path.insert(0, str(TOOLS))

import experiment as base
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import container_command, layout
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


HISTORICAL_COMMIT = "3f3deb56f81a76324eefcc68401887f03a15a674"
REVIEWED_COMMIT = "8e14930b26f7b0c57ad6566970212bd727d88ad1"
RECEIPT_SHA256 = "059993fe139d03b5cdd1475e0a22e29f79844020201db959055f15a3300ac252"
COMPRESSED_SHA256 = "1c10e6908f8aa309693e9c7c6b9ccf859aa7ce5ab40cb6ed5617b15f262b760c"
CONTEXT_SHA256 = "6a69a8d450a0ad5898bed7150136dc70e5731422c29803608825cdefc6b0f914"
CONTEXT_HELPER_SHA256 = "b770b83ffc2bd863c9cd5dec6bcae67ecda60efe8ce0af7fa8cdf136e077b961"
SCIENTIFIC_FIELDS = (
    "recipe", "order", "traces", "census", "outputs", "probes",
    "source_native_outputs", "summary", "candidate_results", "probe_results",
)


def recipes():
    return [
        recipe("early-before-rhotacism", "EAFRhotacism", "before"),
        recipe("intermediate-before-short-a-brightening", "EAFBrightening", "before"),
        recipe("late-after-short-a-brightening", "OEHighVowelApocope", "after", late=True),
    ]


def historical_deltas(rows, baseline, outputs):
    identifiers = {row["id"] for row in rows}
    base.require(len(identifiers) == len(rows) and set(baseline) == identifiers,
                 "historical baseline IDs differ from original population")
    base.require(identifiers <= outputs.keys(), "model is missing original IDs")
    return [
        {"id": row["id"], "concept": row["concept"],
         "baseline": baseline[row["id"]], "variant": outputs[row["id"]]}
        for row in sorted(rows, key=lambda row: row["id"])
        if baseline[row["id"]] != outputs[row["id"]]
    ]


def load_receipt(path):
    compressed = path.read_bytes()
    base.require(hashlib.sha256(compressed).hexdigest() == COMPRESSED_SHA256,
                 "compressed historical receipt identity changed")
    raw = gzip.decompress(compressed)
    base.require(hashlib.sha256(raw).hexdigest() == RECEIPT_SHA256,
                 "decompressed historical receipt identity changed")
    receipt = json.loads(raw)
    base.require(receipt["status"] == "complete" and receipt["protected_unchanged"],
                 "historical receipt is incomplete or unprotected")
    return receipt


def validate_inputs(directory, receipt):
    for name, expected in (
        ("germanic.txt", receipt["source_sha256"]),
        ("germanic-aligned-final.tsv", receipt["canonical_corpus_sha256"]),
        ("candidate_expansion.tsv", receipt["candidate_sha256"]),
        ("entry_context_metadata.tsv", CONTEXT_SHA256),
        ("oe_input_context.py", CONTEXT_HELPER_SHA256),
    ):
        base.require(digest(directory / name) == expected, f"historical pin changed: {name}")
    for name, module in (
        ("oe_input_context.py", sys.modules[InputContext.__module__]),
        ("oe_pipeline.py", oe_pipeline),
        ("anglo_frisian_experiments.py", assay),
    ):
        base.require(digest(Path(module.__file__)) == digest(directory / name),
                     f"runtime helper differs from historical source: {name}")
    original = assay.corpus_rows(directory / "germanic-aligned-final.tsv")
    candidates = read_candidates(directory / "candidate_expansion.tsv")
    base.require(len(original) == 387, "387 historical selections required")
    base.require(original + candidates == receipt["rows"],
                 "historical corpus identities or context differ from receipt")
    base.require(candidates == receipt["candidate_rows"], "candidate identities differ")
    order = base.source_order(directory / "germanic.txt")
    plan = recipes()
    base.require(plan == receipt["recipes"], "historical recipes differ")
    base.require(len(receipt["models"]) == len(plan), "historical model population differs")
    for index, current in enumerate(plan):
        model = receipt["models"][index]
        base.require(model["recipe"] == current, "historical model identity differs")
        base.require(model["order"] == base.edited_order(order, current),
                     f"receipt executable order differs from pinned source: {current['id']}")
    return original, candidates, order


def verify_model(model, historical):
    for field in SCIENTIFIC_FIELDS:
        base.require(model[field] == historical[field],
                     f"historical replay differs: {historical['recipe']['id']} / {field}")
    scientific = {field: model[field] for field in SCIENTIFIC_FIELDS}
    return hashlib.sha256(
        json.dumps(scientific, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


def replay(directory, receipt):
    original, candidates, order = validate_inputs(directory, receipt)
    source = (directory / "germanic.txt").read_text(encoding="utf-8")
    identity_dir = directory / "identity"
    identity_dir.mkdir()
    identity_recipe = {"id": "historical-identity", "definitions": {},
                       "source_replacements": [], "edits": []}
    identity = base.evaluate(source, identity_recipe, order, original, [], identity_dir)
    base.require(
        identity["source_native_outputs"] == [
            identity["outputs"][row["id"]] for row in original
        ], "historical native binary differs from parsed executable baseline",
    )
    baseline = identity["outputs"]
    base.verify_baseline(original, baseline, layout(), directory / "baseline.tsv")
    baseline_summary = selected_summary(original, baseline)
    base.require(baseline_summary == receipt["baseline_existing"],
                 "historical baseline differs from preserved summary")
    version = subprocess.run(["foma", "-v"], check=True, capture_output=True, text=True)
    report = {
        "schema_version": 1, "status": "equivalent",
        "historical_commit": HISTORICAL_COMMIT,
        "receipt_sha256": RECEIPT_SHA256, "compressed_receipt_sha256": COMPRESSED_SHA256,
        "source_sha256": digest(directory / "germanic.txt"),
        "corpus_sha256": digest(directory / "germanic-aligned-final.tsv"),
        "context_sha256": digest(directory / "entry_context_metadata.tsv"),
        "context_helper_sha256": digest(directory / "oe_input_context.py"),
        "baseline": {
            "origin": "isolated compilation of pinned historical Foma source",
            "binary_sha256": digest(identity_dir / "old_english.bin"),
            "script_sha256": identity["compiler"]["script_sha256"],
            "foma_version": (version.stdout + version.stderr).strip(),
            "summary": baseline_summary,
        },
        "compared_scientific_fields": list(SCIENTIFIC_FIELDS),
        "excluded_fields": {
            "compiler": "logs and absolute workspace paths vary; order/traces/native outputs checked",
            "original_deltas": "legacy comparison used inconsistent baselines; recomputed by stable ID",
        },
        "models": [],
    }
    rows = original + candidates
    for index, current in enumerate(recipes()):
        model_dir = directory / current["id"]
        model_dir.mkdir()
        model = base.evaluate(
            source, current, base.edited_order(order, current), rows, probe_set(), model_dir
        )
        model["summary"] = selected_summary(rows, model["outputs"])
        model["candidate_results"] = [
            {"id": row["id"], "concept": row["concept"], "input": row["fst_input"],
             "target": row["counterpart"], "outputs": model["outputs"][row["id"]],
             "match": row["counterpart"] in model["outputs"][row["id"]]}
            for row in candidates
        ]
        model["probe_results"] = [
            {key: probe[key] for key in ("id", "outputs", "firing_events")}
            for probe in model["probes"]
        ]
        scientific_sha = verify_model(model, receipt["models"][index])
        report["models"].append({
            "id": current["id"], "scientific_sha256": scientific_sha,
            "original_rows_compared": len(original), "candidate_rows_compared": len(candidates),
            "events_compared": len(model["order"]),
            "summary": model["summary"], "candidate_results": model["candidate_results"],
            "historical_baseline_deltas": historical_deltas(original, baseline, model["outputs"]),
        })
    return report


def historical_bundle(rt):
    paths = {
        "germanic.txt": "Germanic/fsts/germanic.txt",
        "germanic-aligned-final.tsv": "Germanic/data/germanic-aligned-final.tsv",
        "entry_context_metadata.tsv": "Germanic/data/entry_context_metadata.tsv",
        "oe_input_context.py": "backend/oe_input_context.py",
        "oe_pipeline.py": "Germanic/tools/oe_pipeline.py",
        "anglo_frisian_experiments.py": "Germanic/tools/anglo_frisian_experiments.py",
    }
    files = {
        name: subprocess.check_output(
            ["git", "show", f"{HISTORICAL_COMMIT}:{path}"], cwd=rt.repo_root
        ).decode("utf-8")
        for name, path in paths.items()
    }
    frozen = "Germanic/docs/sound_changes/cascade_baseline/cascade_baseline_outputs_pre_sc112_expansion.tsv"
    files["baseline.tsv"] = subprocess.check_output(
        ["git", "show", f"{REVIEWED_COMMIT}:{frozen}"], cwd=rt.repo_root
    ).decode("utf-8")
    files["candidate_expansion.tsv"] = (INVESTIGATION / "candidate_expansion.tsv").read_text(
        encoding="utf-8"
    )
    return files


def execute_bundle(files, receipt):
    rt = layout()
    base.require(rt.is_container, "historical Foma execution requires the backend container")
    before = base.protected_hashes(rt)
    try:
        with tempfile.TemporaryDirectory(prefix="sc112-replay-") as temporary:
            directory = Path(temporary)
            base.require(set(files) == {
                "germanic.txt", "germanic-aligned-final.tsv", "entry_context_metadata.tsv",
                "oe_input_context.py", "oe_pipeline.py", "anglo_frisian_experiments.py",
                "baseline.tsv", "candidate_expansion.tsv",
            }, "unexpected historical bundle files")
            for name, text in files.items():
                (directory / name).write_text(text, encoding="utf-8")
            report = replay(directory, receipt)
    finally:
        base.require(base.protected_hashes(rt) == before,
                     "protected repository artifacts changed during historical replay")
    report["temporary_workspace_cleaned"] = not directory.exists()
    report["protected_unchanged"] = True
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="write the small verification report (never raw traces)")
    parser.add_argument("--execute-replay", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    receipt = load_receipt(INVESTIGATION / "followup-receipt.json.gz")
    rt = layout()
    if args.execute_replay:
        report = execute_bundle(json.load(sys.stdin), receipt)
    else:
        base.require(not rt.is_container, "start replay from the host Git checkout")
        base.require(args.report is None or not args.report.exists(),
                     "refusing to overwrite a verification report")
        files = historical_bundle(rt)
        # Validate before launching any Foma execution, including context/helper pins.
        with tempfile.TemporaryDirectory(prefix="sc112-replay-preflight-") as temporary:
            directory = Path(temporary)
            for name, text in files.items():
                (directory / name).write_text(text, encoding="utf-8")
            validate_inputs(directory, receipt)
        command = container_command(
            "python3 -B /usr/app/docs/sound_changes/audits/"
            "sc015-r-adverb-lengthening-investigation/followup_experiment.py --execute-replay"
        )
        result = subprocess.run(command, input=json.dumps(files), text=True,
                                capture_output=True, cwd=rt.repo_root)
        if result.returncode:
            raise RuntimeError(
                f"historical replay failed ({result.returncode}):\n{result.stderr}\n{result.stdout}"
            )
        report = json.loads(result.stdout)
        base.require(report["status"] == "equivalent", "container replay did not verify equivalence")
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        with args.report.open("x", encoding="utf-8") as handle:
            handle.write(text)
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
