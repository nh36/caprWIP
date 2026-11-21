"""Opt-in SC047 A/B comparison; run inside the Germanic backend container."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch

BASE = Path(__file__).resolve().parent
CONTROL = BASE.parent / "labial_review" / "plan.json"
ROOT = next(p for p in BASE.parents if (p / "fsts/germanic.txt").exists())
sys.path.insert(0, str(ROOT / "tools"))

FIRST = "PNWGmcLongELowering"
LAST = "OldEnglishSurface"
CONTROLS = (
    "net", "bed", "hay", "hue", "strew", "deer", "door", "there", "where",
    "rest", "hedge", "dill", "straw", "believe", "sea", "show",
)


def recipe():
    original = json.loads(CONTROL.read_text())
    variants = {label: original["configurations"][previous]
                for label, previous in (("A", "early"), ("B", "split"))}
    definitions = {name: original["definitions"][name] for name in ("FW", "FNU", "FON")}
    cells = dict(zip(original["probe_ids"],
                     original["queries"][f"identity:cell:{LAST}"]["inputs"], strict=True))
    cells.pop("nett.dat.pl.retained_o")
    cells.update({
        "bedd.dat.sg": "bádjai",
        "mete.i_stem": "mátiz",
        "mete.gen.sg.i_stem_probe": "mátis",
        "cynn.direct": "kúnją",
        "cynn.gen.sg": "kúnjas",
        "cynn.dat.sg": "kúnjai",
    })
    for word, stem in (("wedd", "wádj"), ("mene.proposed_neuter", "mánj")):
        for cell, ending in (("direct", "ą"), ("gen.sg", "as"), ("dat.sg", "ai")):
            cells[f"{word}.{cell}"] = stem + ending
    for word, stem in (("hyll", "xúlj"), ("hyse.proposed_ja", "xúsj"),
                       ("dili.proposed_ja", "délj")):
        for cell, ending in (("nom.sg", "az"), ("acc.sg", "ą"), ("dat.sg", "ai")):
            cells[f"{word}.{cell}"] = stem + ending
    cells.update({
        "secg.dat.sg": "ságjai",
        "dili.proposed_i.nom.sg": "déliz",
    })
    return variants, definitions, cells


def order_for(canonical, operations):
    result = list(canonical)
    for op in operations:
        if "replace" in op:
            result[result.index(op["replace"])] = op["with"]
        elif "move" in op or "insert" in op:
            stage = op.get("move") or op["insert"]
            if "move" in op:
                result.remove(stage)
            result.insert(result.index(op["after"]) + 1, stage)
        else:
            raise ValueError(op)
    return result


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    import anglo_frisian_experiments as compiler
    from capr_runtime import check_build_manifest, layout
    import oe_pipeline
    from sound_change_order_sensitivity import batch_apply_down

    runtime = layout()
    error = check_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])
    if error:
        raise RuntimeError(f"Canonical reference bins are not fresh: {error}")
    source = runtime.germanic_fst
    corpus_path = runtime.corpus_tsv
    inputs = [source, corpus_path, corpus_path.with_name("entry_context_metadata.tsv"),
              CONTROL, Path(__file__), *(ROOT / "tools" / name for name in (
                  "anglo_frisian_experiments.py", "oe_pipeline.py", "capr_runtime.py",
                  "sound_change_order_sensitivity.py", "executable_facts.py"))]
    hashes = {p.name: digest(p) for p in inputs}
    variants, extra_definitions, cells = recipe()
    definitions = list(extra_definitions.values())
    rows = oe_pipeline.load_rows(corpus_path)
    canonical = [stage.foma_identifier for stage in oe_pipeline.stages()]
    first = canonical.index(FIRST) + 1
    raw = [row["fst_input"] for row in rows]
    incoming = batch_apply_down(runtime.bin_dir / oe_pipeline.stage_for(FIRST).snapshot_bin, raw)
    baseline = batch_apply_down(runtime.bin_dir / "old_english.bin", raw)
    assert all(len(output) == 1 for output in incoming + baseline)
    assert len(rows) == 394 and sum(row["counterpart"] in output
                                   for row, output in zip(rows, baseline, strict=True)) == 386
    indices = [i for i, row in enumerate(rows) if row["concept"] in CONTROLS]
    orders = {label: order_for(canonical, ops) for label, ops in variants.items()}
    probes = [oe_pipeline.CITATION_CONTEXT.encode(form) for form in cells.values()]
    probe_inputs = probes + [raw[i] for i in indices]
    queries = {}

    def add(key, forms, members):
        symbol = f"PAB{len(queries)}"
        definitions.append(f"define {symbol} {compiler.foma_domain(forms)} .o. "
                           + " .o. ".join(members) + ";")
        queries[key] = (symbol, forms)

    add("identity:corpus", [value[0] for value in incoming], canonical[first:])
    add("shared:prefix", probe_inputs, canonical[:first])
    for label, order in orders.items():
        assert order[:first] == canonical[:first]
        add(label + ":corpus", [value[0] for value in incoming], order[first:])
        for stop in range(first, len(order)):
            add(f"{label}:{order[stop]}", probe_inputs, order[:stop + 1])

    with tempfile.TemporaryDirectory(prefix="capr-sc047-parallel-") as path:
        work = Path(path)
        image = compiler.prepare_definition_image(source, work)
        if image is None:
            raise RuntimeError("Source does not support isolated definition images")
        with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
            bins = compiler.compile_isolated(source, {
                "definitions": "\n".join(definitions), "replace": {},
                "insert_rule": None, "insert_after": None,
                "component_checks": [{"component": name} for name, _ in queries.values()],
            }, [], work, components_only=True)
        assert (work / "experiment.foma").read_text().startswith("load defined ")
        output = {key: batch_apply_down(bins[f"component:{name}"], forms)
                  for key, (name, forms) in queries.items()}
    assert output.pop("identity:corpus") == baseline
    for path in inputs:
        assert digest(path) == hashes[path.name], path
    return {
        "inputs_sha256": hashes, "configurations": orders, "prefix": FIRST,
        "cells": dict(zip(cells, probes, strict=True)),
        "controls": [rows[i]["row_id"] for i in indices],
        "corpus": [{**row, "identity": baseline[i],
                    **{label: output[f"{label}:corpus"][i] for label in orders}}
                   for i, row in enumerate(rows)],
        "traces": {key: values for key, values in output.items() if not key.endswith(":corpus")},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(json.dumps(run(), ensure_ascii=False, separators=(",", ":")))
