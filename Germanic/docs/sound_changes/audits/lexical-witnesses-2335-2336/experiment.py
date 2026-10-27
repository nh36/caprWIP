#!/usr/bin/env python3
"""Trace lexical witnesses, optionally extending only the isolated input gate."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
import oe_pipeline
from anglo_frisian_experiments import compile_isolated
from capr_runtime import check_build_manifest, layout
from cascade_baseline import build_baseline
from sound_change_order_sensitivity import batch_apply_down


BASE = "0dd533e3f15c85f20a976a3781a9b4d79bf6f928"
CANDIDATES = {
    "which-inherited": "*xwílīkaz",
    "which-compound-notation": "*xwí-līkaz",
    "which-a-alternative": "*xwálīkaz",
    "which-a-compound-alternative": "*xwá-līkaz",
    "earthly-proposed-plain": "*érθakundaz",
    "earthly-plain-compound": "*érθa-kundaz",
    "earthly-proposed-grave": "*érθa-kùndaz",
    "earthly-source-dental": "*érθakunðaz",
    "earthly-source-dental-compound": "*érθa-kunðaz",
    "earthly-genitive-feminine": "*érθakunðaizōz",
    "earthly-genitive-feminine-compound": "*érθa-kunðaizōz",
    "earthly-genitive-feminine-grave": "*érθa-kùnðaizōz",
    "lord-deferred-plain": "*xláiba-warðaz",
    "lord-deferred-grave": "*xláiba-wàrðaz",
    "lord-underlying-stop-plain": "*xláiba-wardaz",
    "lord-underlying-stop-grave": "*xláiba-wàrdaz",
    "lord-source-beta-notation": "*xláiβa-warðaz",
    "world-selected-control": "*wír-àldiz",
    "rainbow-selected-control": "*régna-bùgô",
    "godcund-comparison-plain": "*gúðakundaz",
    "godcund-comparison-compound": "*gúða-kundaz",
    "godcund-comparison-grave": "*gúða-kùndaz",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


GATE_DEFINITIONS = """
define AFGenFem [{ai}:{*ai} z:{*z} ō:{*ō} z:{*z} | i:{*i} z:{*z} ō:{*ō} z:{*z}];
define AFWord [
    pgrmWord |
    (pgrmStrongPlainHeavy | pgrmStrongPlainHeavyPrefixed) AFGenFem |
    pgrmCompoundFirst pgrmCompoundSep pgrmStrongPlainHeavy AFGenFem
];
define AFGate [[{ᵘ}:{*ᵘ} | {ᶜ}:{*ᶜ} | 0] AFWord];
"""


def run(extend_input_gate: bool = False) -> dict:
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("Run in the backend container; no host-local Foma.")
    errors = check_build_manifest(
        oe_pipeline.expected_snapshot_bins() + ["old_english.bin"], runtime)
    if errors:
        raise RuntimeError("; ".join(errors))
    protected = [
        runtime.germanic_fst, runtime.sandbox_fst, runtime.corpus_tsv,
        runtime.build_manifest,
        *(runtime.docs_dir / "sound_changes/cascade_baseline").glob("*"),
    ]
    protected = [path for path in protected if path.is_file()]
    before = {str(path): digest(path) for path in protected}
    stages = oe_pipeline.stages()
    sequence = [
        stage.foma_identifier if stage.kind == "named" else stage.inline_text
        for stage in stages
    ]
    recipe = dict(
        definitions="", insert_after="", insert_rule="", replace={},
        component_checks=[dict(component=item) for item in dict.fromkeys(sequence)],
    )
    inputs = [
        oe_pipeline.evaluation_input(
            {"proto_norm": oe_pipeline.normalize_proto(raw)})
        for raw in CANDIDATES.values()
    ]
    results = [
        dict(name=name, input=raw, evaluator_input=value, steps=[], rejection=None)
        for (name, raw), value in zip(CANDIDATES.items(), inputs)
    ]
    with tempfile.TemporaryDirectory(prefix="capr_lexical_witnesses_") as temporary:
        source = runtime.germanic_fst
        if extend_input_gate:
            source = Path(temporary) / "gate_source.foma"
            source.write_text(
                runtime.germanic_fst.read_text(encoding="utf-8")
                + GATE_DEFINITIONS + "\ndefine EnglishProtoInput AFGate;\n",
                encoding="utf-8",
            )
        bins = compile_isolated(source, recipe, [], Path(temporary))
        existing = oe_pipeline.load_rows(runtime.corpus_tsv)
        existing_inputs = [oe_pipeline.evaluation_input(row) for row in existing]
        production = batch_apply_down(runtime.bin_dir / "old_english.bin", existing_inputs)
        isolated = batch_apply_down(bins["final"], existing_inputs)
        if isolated != production:
            raise RuntimeError("Isolated identity differs from production.")
        final_outputs = batch_apply_down(bins["final"], inputs)
        states = list(inputs)
        live = list(range(len(states)))
        for position, identifier in enumerate(sequence, 1):
            outputs = batch_apply_down(
                bins["component:" + identifier], [states[index] for index in live])
            accepted = []
            for index, values in zip(live, outputs):
                result = results[index]
                result["steps"].append(dict(
                    position=position, stage=identifier,
                    before=states[index], outputs=values,
                    changed=values != [states[index]],
                ))
                if not values:
                    result["rejection"] = dict(
                        position=position, stage=identifier, input=states[index])
                elif len(values) != 1:
                    raise RuntimeError(f"Ambiguous component: {result['name']}: {identifier}")
                else:
                    states[index] = values[0]
                    accepted.append(index)
            live = accepted
        for index, result in enumerate(results):
            result["parser_accepted"] = bool(result["steps"][0]["outputs"])
            result["final_outputs"] = final_outputs[index]
            incremental = [states[index]] if index in live else []
            if incremental != final_outputs[index]:
                raise RuntimeError(f"Incremental/final disagreement: {result['name']}")
    baseline = build_baseline(runtime.corpus_tsv, runtime.bin_dir / "old_english.bin")
    if before != {str(path): digest(path) for path in protected}:
        raise RuntimeError("Private experiment changed protected production files.")
    return dict(
        base_commit=BASE, input_gate_extension=extend_input_gate,
        gate_definitions=GATE_DEFINITIONS if extend_input_gate else "",
        source_sha256=digest(runtime.germanic_fst),
        sandbox_sha256=digest(runtime.sandbox_fst),
        corpus_sha256=digest(runtime.corpus_tsv), order=sequence,
        production_equivalent=True, existing_population=baseline,
        candidates=results,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extend-input-gate", action="store_true")
    args = parser.parse_args()
    print(json.dumps(run(args.extend_input_gate), ensure_ascii=False, indent=2))
