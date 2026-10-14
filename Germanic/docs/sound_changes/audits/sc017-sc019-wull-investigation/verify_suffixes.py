"""Independently verify every staged paradigm suffix and early nested event."""
import copy
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
from capr_runtime import layout

root = Path("/research")
runtime = layout()
destination = root / "independent-equivalence.json"
if destination.exists():
    raise RuntimeError("Independent verification already exists")
original = json.loads((root / "identity.json").read_text())
replay = json.loads((root / "identity-replay.json").read_text())
old_rows = {row["id"]: row for row in original["rows"]}
if len(old_rows) != 387:
    raise RuntimeError("Original identity row population failed")
comparisons = 0
for row in replay["rows"]:
    for probe, pair in row["intermediates"].items():
        if pair["baseline"] != old_rows[row["id"]]["intermediates"][probe]["variant"]:
            raise RuntimeError(f"Independent original full prefix differs: {row['id']}/{probe}")
        comparisons += 1
if comparisons != 387 * 107:
    raise RuntimeError("Independent prefix comparison denominator failed")
protected = replay["canonical_protected_hashes"]
if any(assay.digest(Path(path)) != digest for path, digest in protected.items()):
    raise RuntimeError("Private protected state changed before independent verification")
results = []
for recipe in assay.load_recipes(root / "recipes-context-v2.json")["recipes"]:
    report = json.loads((root / f"{recipe['id']}-replay.json").read_text())
    compiler = copy.deepcopy(recipe)
    order = assay.complete_variant_order(recipe)
    inputs = [cell["tokenized_input"] for cell in report["paradigms"]]
    acceptor = " | ".join(
        " ".join("{" + token + "}" for token in form.split("*")[1:]
                 for token in ["*" + token])
        for form in inputs
    )
    suffix = order[order.index("EnglishProtoInput") + 1:]
    compiler["definitions"] += (
        "\ndefine AFFixtures [[" + acceptor + "] .o. "
        + "\n .o. ".join(suffix) + "];\n"
    )
    compiler["component_checks"] = [
        {"component": name} for name in (
            "PNWGmcStressedMonosyllableORaising", "PNWGmcFinalLongORaising",
            "EAFFinalZDeletion", "AFFixtures",
        )
    ]
    print("VERIFY SUFFIX", recipe["id"], flush=True)
    with tempfile.TemporaryDirectory(prefix="capr_wull_suffix_") as temporary:
        bins = assay.compile_isolated(runtime.germanic_fst, compiler, [], Path(temporary),
                                      components_only=True)
        outputs = assay.batch_apply_down(bins["component:AFFixtures"], inputs)
        if outputs != [cell["outputs"] for cell in report["paradigms"]]:
            raise RuntimeError(f"Complete suffix differs from replay: {recipe['id']}")
        nested = []
        if recipe["insert_rule"] == "AFEarly":
            before = [
                row["intermediates"]["k019"]["variant"] for row in report["rows"]
            ]
            if any(len(value) != 1 for value in before):
                raise RuntimeError("Non-deterministic pre-insertion state")
            mono = assay.batch_apply_down(
                bins["component:PNWGmcStressedMonosyllableORaising"],
                [value[0] for value in before])
            oral = assay.batch_apply_down(
                bins["component:PNWGmcFinalLongORaising"],
                [value[0] for value in mono])
            if oral != [row["inserted_states"]["AFEarly"] for row in report["rows"]]:
                raise RuntimeError("Nested early events differ from compiled early group")
            nested = [
                {"id": row["id"], "before": prior, "after_sc018": middle,
                 "after_sc019": after}
                for row, prior, middle, after in zip(report["rows"], before, mono, oral)
            ]
        results.append({
            "recipe": recipe["id"],
            "all_16_suffix_outputs_equal_replay": True,
            "paradigm_missing_ids": [
                cell["id"] for cell, output in zip(report["paradigms"], outputs) if not output],
            "paradigm_ambiguous_ids": [
                cell["id"] for cell, output in zip(report["paradigms"], outputs) if len(output) > 1],
            "nested_early_events": nested,
            "trimoric_genitive_sc020_control": assay.batch_apply_down(
                bins["component:EAFFinalZDeletion"], ["*w*ú*l*l*ô*z", "*w*ú*l*l*ō*z"]),
        })
if any(assay.digest(Path(path)) != digest for path, digest in protected.items()):
    raise RuntimeError("Private protected state changed during independent verification")
destination.write_text(json.dumps({
    "original_independent_identity_prefix_comparisons": comparisons,
    "all_original_107_prefixes_equal_stage_replay": True,
    "paradigm_input_contract": (
        "Independent complete derived suffix composition is intersected with a "
        "finite identity acceptor of all 16 declared PGmc cells. The acceptor "
        "restricts diagnostic inputs, not any sound-law definition or domain. "
        "An initial unrestricted starred suffix compile was operationally stopped "
        "before completion; it supplies no scientific result."),
    "results": results, "canonical_artifacts_unchanged": True,
    "canonical_protected_hashes": protected,
}, ensure_ascii=False, indent=2) + "\n")
print("VERIFIED", comparisons, "independent baseline checkpoints and all complete suffixes")
