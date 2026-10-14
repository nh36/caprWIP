"""Generate fresh session-only recipes from the protected, derived cascade."""
import csv
import json
from pathlib import Path
import sys

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import layout

ROOT = Path("/research")
runtime = layout()
stages = oe_pipeline.stages()
order = assay.complete_variant_order({"insert_rule": "", "replace": {}})
probes = []
stage_map = []
for stage, expression in zip(stages, order):
    if order.count(expression) != 1:
        raise ValueError(f"Nonunique checkpoint: {expression}")
    identifier = f"k{stage.exec_index:03d}"
    probes.append({"id": identifier, "stage": expression, "side": "after"})
    stage_map.append({
        "probe": identifier, "exec_index": stage.exec_index,
        "cascade_position": stage.cascade_position,
        "identifier": stage.foma_identifier, "expression": expression,
        "kind": stage.kind,
    })

corrected = """define AFUL [Ctx([
    {*u} -> {*o}, {*ú} -> {*ó} ||
    .#. EnglishStarConsonant* _
    [EnglishStarConsonantNoJ - EnglishStarNasal]
    EnglishStarConsonantNoJ* [EnglishStarNonHighVowel | {*ǭ}]
])];"""
early = "define AFEarly [PNWGmcStressedMonosyllableORaising .o. PNWGmcFinalLongORaising];"
identities = "define AFId18 [[EnglishStarAlphabet]*];\ndefine AFId19 [[EnglishStarAlphabet]*];"
revaluation = """define AFReval [Ctx([
    {*o} -> {*u}, {*ó} -> {*ú} ||
    .#. EnglishStarConsonant* _
    [EnglishStarConsonantNoJ - EnglishStarNasal]
    EnglishStarConsonantNoJ* {*u} .#.
])];"""
sources = [
    {"key": "RingeTaylor2014", "pages": "15-16,27-34,58-60,267,298-300"},
    {"key": "Ringe2017", "pages": "171-173,242-244"},
    {"key": "Fulk2018", "pages": "55-57,82-86,154-156"},
    {"key": "Stiles2012", "pages": "44-60"},
]

def recipe(name, description, definitions="", insert_after="", insert_rule="", replace=None):
    return {
        "id": name, "description": description,
        "definitions": definitions, "insert_after": insert_after,
        "insert_rule": insert_rule, "replace": replace or {},
        "sources": [] if name == "identity" else sources,
        "assumptions": (
            "No intervention." if name == "identity" else
            "Historical quantities and inflectional cells remain distinct. "
            "Selected corpus inputs and contexts are unchanged; analogy is not a sound law."
        ),
        "limitations": (
            "D specifically ASSUMES that conditioned [o] remains synchronically "
            "reversible until AFTER final oral ō becomes u. Stiles 2012 pp.54-59 "
            "allows reversion as a possibility, not an inevitable consequence; "
            "pp.47-48 show early runic o outside its original conditioning. "
            "The new operation is a research counterfactual, NOT a proposed "
            "attested historical law or evidence for its date."
            if name == "d-live-allophony" else
            "Executable checkpoints are not historical dates. Missing nasal "
            "trigger recognition and input admission are separate questions."
        ),
    }

recipes = [
    recipe("identity", "Released source and full-wrapper identity"),
    recipe("a-order-only", "A: unchanged SC018 and SC019 before unchanged SC017",
           early + "\n" + identities, "PNWGmcILowering", "AFEarly",
           {"PNWGmcStressedMonosyllableORaising": "AFId18",
            "PNWGmcFinalLongORaising": "AFId19"}),
    recipe("b-conditioning-only", "B: admit nasal ǭ into SC017 trigger domain only",
           "define AFPass [[EnglishStarAlphabet]*];\n" + corrected,
           "PNWGmcILowering", "AFPass", {"PNWGmcULowering": "AFUL"}),
    recipe("c-combined", "C: early SC018/SC019 and corrected SC017 trigger domain",
           early + "\n" + identities + "\n" + corrected,
           "PNWGmcILowering", "AFEarly",
           {"PNWGmcStressedMonosyllableORaising": "AFId18",
            "PNWGmcFinalLongORaising": "AFId19", "PNWGmcULowering": "AFUL"}),
    recipe("d-live-allophony", "D: early lowering, final raising, then live-allophone revaluation",
           corrected + "\n" + revaluation,
           "PNWGmcFinalLongORaising", "AFReval", {"PNWGmcULowering": "AFUL"}),
]
data = {
    "schema_version": 1, "fixture_file": "wull_fixtures.tsv",
    "baseline_fst_sha256": assay.digest(runtime.germanic_fst),
    "baseline_corpus_sha256": assay.digest(runtime.corpus_tsv),
    "baseline_context_sha256": assay.digest(runtime.data_dir / assay.METADATA_FILENAME),
    "baseline_context_helper_sha256": assay.digest(runtime.bin_dir / "oe_input_context.py"),
    "probes": probes, "recipes": recipes,
}
path = ROOT / "recipes.json"
if path.exists():
    raise RuntimeError("Fresh recipes already exist; do not overwrite executed assumptions")
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
assay.load_recipes(path)
(ROOT / "stage_map.json").write_text(json.dumps(stage_map, ensure_ascii=False, indent=2) + "\n")
with (ROOT / "wull_fixtures.tsv").open("w") as handle:
    handle.write("fixture_id\trecipe\trow_id\tprobe\tbaseline_prediction\tvariant_prediction\n")
(ROOT / "predictions.json").write_text(json.dumps({
    "a-order-only": {
        "wool_nom_after_sc017": "*w*ú*l*l*u",
        "wool_acc_after_sc017": "*w*ú*l*l*ǭ",
        "expected_changed_final_ids": ["2143", "2185", "2200", "2300"],
    },
    "b-conditioning-only": {
        "wool_nom_after_sc017": "*w*ó*l*l*ō",
        "wool_acc_after_sc017": "*w*ó*l*l*ǭ",
        "expected_changed_final_ids": [],
    },
    "c-combined": {
        "wool_nom_after_sc017": "*w*ú*l*l*u",
        "wool_acc_after_sc017": "*w*ó*l*l*ǭ",
        "expected_changed_final_ids": ["2143", "2185", "2200", "2300"],
    },
    "d-live-allophony": {
        "wool_nom_after_sc017": "*w*ó*l*l*ō",
        "wool_nom_after_revaluation": "*w*ú*l*l*u",
        "wool_acc_after_sc017": "*w*ó*l*l*ǭ",
        "expected_changed_final_ids": ["2143", "2185", "2200", "2300"],
    },
    "important_limit": (
        "Bare accusative ǭ is absent from the production weak-tail parser. "
        "These predictions concern properly tokenized PGmc cells entered AFTER "
        "EnglishProtoInput, not a silent production parser repair. "
        "The separate pathway assay will measure actual input rejection."
    ),
}, ensure_ascii=False, indent=2) + "\n")
print(f"Prepared five recipes with {len(probes)} full-cascade checkpoints.")
