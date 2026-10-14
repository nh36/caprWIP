"""Measure raw parser admission separately from starred sound-law domains."""
import copy
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import layout

root = Path("/research")
runtime = layout()
data = assay.load_recipes(root / "recipes-context-v2.json")
identity = json.loads((root / "identity-replay.json").read_text())
protected = {Path(path): checksum for path, checksum
             in identity["canonical_protected_hashes"].items()}
if any(assay.digest(path) != checksum for path, checksum in protected.items()):
    raise RuntimeError("Protected private state changed before pathway assay")
destination = root / "pathway.json"
if destination.exists():
    raise RuntimeError("Pathway receipt already exists")

recipe = copy.deepcopy(next(item for item in data["recipes"]
                            if item["id"] == "b-conditioning-only"))
recipe["definitions"] += """
define AFInput [
    EnglishProtoInput |
    [{ᵘ}:{*ᵘ}|{ᶜ}:{*ᶜ}|0]
    [pgrmStrongPlainHeavy | pgrmStrongPlainHeavyPrefixed |
     pgrmStrongNasal | pgrmStrongNasalPrefixed] ǭ:{*ǭ}
];
"""
recipe["replace"]["EnglishProtoInput"] = "AFInput"
components = [
    "PGmcStarVowel", "PGmcStarVocalic", "EnglishStarNonHighVowel",
    "EnglishStarAlphabet", "pgrmWeakTailVowel", "EnglishProtoInput",
    "AFInput", "PNWGmcULowering", "AFUL", "PNWGmcFinalLongORaising",
    "PNWGmcStressedMonosyllableORaising",
]
# Compilation-only component selectors; these are not fabricated predictions.
recipe["component_checks"] = [{"component": component} for component in components]
with tempfile.TemporaryDirectory(prefix="capr_wull_pathway_") as temporary:
    bins = assay.compile_isolated(runtime.germanic_fst, recipe, [],
                                  Path(temporary), components_only=True)
    def lookup(component, inputs):
        outputs = assay.batch_apply_down(bins[f"component:{component}"], inputs)
        return [{"input": form, "outputs": result}
                for form, result in zip(inputs, outputs)]

    raw = sorted({
        cell["raw_input"] for cell in identity["paradigms"]
    } | {"wullō", "wullǭ", "wúllōn", "wúllanǭ", "wúllô", "wúllōz", "wúllôz"})
    raw_result = lookup("EnglishProtoInput", raw)
    admitted = lookup("AFInput", raw)
    symbols = ["*ō", "*ǭ", "*ô", "*u", "*ą"]
    starred = [
        "".join("*" + char for char in form)
        for form in ("wullō", "wullǭ", "wúllō", "wúllǭ", "wúllô",
                     "wúllōz", "wúllôz", "wúllōn")
    ]
    starred += ["*ᵘ*w*ú*l*l*ǭ", "*ᶜ*w*ú*l*l*ǭ", "*d*ō", "*d*ū"]
    selected = assay.corpus_rows(runtime.corpus_tsv)
    selected_forms = [oe_pipeline.evaluation_input(row) for row in selected]
    baseline_parsed = assay.batch_apply_down(
        bins["component:EnglishProtoInput"], selected_forms)
    expanded_parsed = assay.batch_apply_down(bins["component:AFInput"], selected_forms)
    if baseline_parsed != expanded_parsed:
        raise RuntimeError("General accusative adapter changes existing selected tokenizations")
    for row, outputs in zip(identity["rows"], baseline_parsed):
        first_probe = next(iter(row["intermediates"]))
        if row["intermediates"][first_probe]["baseline"] != outputs:
            raise RuntimeError("Parser component disagrees with independent complete prefix")
    nom = next(item for item in raw_result if item["input"] == "wúllō")
    acc = next(item for item in raw_result if item["input"] == "wúllǭ")
    fixed = next(item for item in admitted if item["input"] == "wúllǭ")
    if nom["outputs"] != ["*w*ú*l*l*ō"] or acc["outputs"] or fixed["outputs"] != ["*w*ú*l*l*ǭ"]:
        raise RuntimeError("Declared raw wool pathway diagnosis failed")
    after = {str(path): assay.digest(path) for path in protected}
    before = {str(path): checksum for path, checksum in protected.items()}
    if before != after:
        raise RuntimeError("Protected private state changed during pathway assay")
    report = {
        "scientific_source": "Ringe2017 pp.242-243; Fulk2018 pp.82,155",
        "general_adapter_definition": recipe["definitions"],
        "raw_baseline_parser": raw_result, "raw_extended_parser": admitted,
        "classes": {component: lookup(component, symbols)
                    for component in components[:4]},
        "weak_tail_parser": lookup("pgrmWeakTailVowel", ["ō", "ǭ", "ô", "anǭ", "ōz", "ôz"]),
        "sound_law_domains": {
            component: lookup(component, starred) for component in components[7:]},
        "selected_parser_rows": len(selected),
        "selected_tokenizations_unchanged": baseline_parsed == expanded_parsed,
        "selected_tokenizations": [
            {"id": row["id"], "input": form, "outputs": output}
            for row, form, output in zip(selected, selected_forms, baseline_parsed)],
        "canonical_protected_hashes": before,
        "canonical_artifacts_unchanged": True,
        "interpretation": (
            "Bare inherited accusative ǭ is distinct from accepted anǭ and citation ōn. "
            "The general private admission control is parser-only, not an analogical "
            "sound law and not an adopted production repair. Full historical paradigm "
            "assays enter already-tokenized PGmc cells after EnglishProtoInput."),
    }
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "raw_wool_nom": nom, "raw_wool_acc": acc, "extended_wool_acc": fixed,
        "selected_parser_rows": len(selected), "selected_tokenizations_unchanged": True,
        "canonical_artifacts_unchanged": True,
    }, ensure_ascii=False))
