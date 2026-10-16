#!/usr/bin/env python3
"""Reproduce the adopted SC015 component controls and selected learn cells."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/usr/app/tools")
import anglo_frisian_experiments as assay
import oe_pipeline
from capr_runtime import check_build_manifest, layout

HERE = Path(__file__).resolve().parent
RULE = "PNWGmcILowering"
CASES = [
    ("nistan", "nistan", "nestan", "positive", "Hill2017 p.153"),
    ("mizdon", "mizdōn", "mezdōn", "positive", "Hill2017 p.153"),
    ("wiraz", "wiraz", "weraz", "positive", "Hill2017 p.156"),
    ("iz", "iz", "ez", "positive", "Hill2017 p.153"),
    ("hiz", "xiz", "xez", "positive", "Hill2017 p.153; h normalized x"),
    ("hir", "xir", "xer", "positive", "Hill2017 pp.156–158; conditional precursor"),
    ("fish", "fiskaz", "fiskaz", "negative", "Hill2017 p.154"),
    ("wisko", "wiskō", "wiskō", "negative", "Hill2017 pp.154–155"),
    ("bitanaz", "bitanaz", "bitanaz", "negative", "Hill2017 pp.151–152; participial probe"),
    ("bithanaz", "biðanaz", "biðanaz", "negative", "Hill2017 pp.151–152; Verner participial probe"),
    ("nidana", "nidana", "nidana", "negative", "Hill2017 p.152; schematic WGmc adverb"),
    ("lid", "xlídą", "xlídą", "negative", "live row2100; Lloyd1966 p.738"),
    ("long", "wīraz", "wīraz", "domain_control", "synthetic long-vowel exclusion"),
    ("later_nucleus", "anistą", "anistą", "domain_control", "synthetic noninitial nucleus"),
    ("intervocalic_z", "wizam", "wizam", "domain_control", "synthetic z-before-vowel"),
    ("velar_onset", "kiraz", "keraz", "domain_control", "synthetic onset-velar contrast"),
    ("acute", "nístą", "néstą", "domain_control", "acute notation of selected nest"),
    ("high_following", "nistijan", "nestijan", "domain_control", "Hill2017 p.153; mutation precursor"),
    ("list", "listiz", "lestiz", "domain_control", "Hill2017 p.153; before mutation"),
    ("twine", "twizna", "twezna", "counterevidence", "Orel2003 p.414; NOT a correct reflex"),
]


def starred(form: str) -> str:
    return "".join("*" + char for char in form)


def main() -> None:
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("run this bounded probe inside the backend container")
    errors = check_build_manifest(
        ["old_english.bin", *oe_pipeline.expected_snapshot_bins()], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    checks = [
        {"id": name, "component": RULE, "input": starred(form),
         "expected": starred(expected), "role": role, "basis": basis}
        for name, form, expected, role, basis in CASES
    ]
    checks += [
        {"id": name + "_mutation", "component": "AFMut", "input": starred(form),
         "expected": starred(form), "role": "masking_control", "basis": "Hill2017 p.153"}
        for name, form in (("nistijan", "nistijan"), ("listiz", "listiz"))
    ]
    recipe = {
        "id": "sc015_adopted_components", "insert_rule": "", "insert_after": "",
        "replace": {}, "definitions": "define AFMut [PNWGmcILowering .o. OEIUmlaut];",
        "component_checks": checks,
    }
    with tempfile.TemporaryDirectory(prefix="sc015-adopt-") as directory:
        bins = assay.compile_isolated(
            runtime.germanic_fst, recipe, [], Path(directory), components_only=True)
        components = assay.check_component_predictions(recipe, bins)
    rows = {row["row_id"]: row for row in oe_pipeline.load_rows(runtime.corpus_tsv)}
    paradigm = []
    for identifier, cell in (("2095", "infinitive"), ("2313", "imperative2sg"),
                             ("2314", "present_indicative3sg")):
        row = rows[identifier]
        output = assay.batch_apply_down(
            runtime.bin_dir / "old_english.bin", [row["fst_input"]])[0]
        if output != [row["counterpart"]]:
            raise RuntimeError(f"learn cell no longer matches: {identifier}: {output}")
        paradigm.append({"row_id": identifier, "cell": cell, "input": row["proto"],
                         "target": row["counterpart"], "outputs": output})
    receipt = {
        "fst_sha256": hashlib.sha256(runtime.germanic_fst.read_bytes()).hexdigest(),
        "corpus_sha256": hashlib.sha256(runtime.corpus_tsv.read_bytes()).hexdigest(),
        "components": components, "learn_paradigm": paradigm,
        "scope": "Supplementary comparative and synthetic component probes, not corpus admissions. "
                 "Twine's lowered prediction is documented counterevidence, not historical validation.",
    }
    (HERE / "probes.json").write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(components)} component predictions; {len(paradigm)} selected learn cells")


if __name__ == "__main__":
    main()
