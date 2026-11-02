#!/usr/bin/env python3
"""Research-only soul experiments using immutable snapshots and the CAPR compiler."""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
GERMANIC = HERE.parents[3]
sys.path.insert(0, str(GERMANIC / "tools"))
BASE = "637b30dbfa2455f57f3f467088743d73f8b536b9"

DEFINITIONS = """
define SCon OEAnyConsonant;
define SShort [EnglishStarShortVowel|EnglishStarShortDiphthong];
define SLong [EnglishStarLongVowel|EnglishStarLongDiphthong|{*ô}];
define SHeavy [SLong SCon+|SShort SCon SCon+];
define SFollowing [SCon SLong SCon*|SCon EnglishStarVocalic SCon+];
define SNonHigh [{*a}|{*æ}|{*e}];
define SWeak [SNonHigh|{*i}|{*u}|{*y}];
define SIdentity ?*;
define SCellStem [
    [a:{*a}|e:{*e}|i:{*i}|u:{*u}|ī:{*ī}] pgrmCodaSimple
];
define SCellEnd [
    ō:{*ō}|ǭ:{*ǭ}|ō:{*ō} z:{*z}|ô:{*ô} z:{*z}|
    ô:{*ô} i:{*i}|a:{*a} s:{*s}
];
define SInput [EnglishProtoInput|pgrmStrongPlainHeavy SCellStem SCellEnd];
define SAccUnround Ctx([{*ǭ} -> {*ā} || _ .#.]);
define SFulkSyn Ctx([
    SWeak -> 0 || .#. SCon* SHeavy _ SFollowing .#.
]);
define SNonHighSyn Ctx([
    SNonHigh -> 0 || .#. SCon* SHeavy _ SFollowing .#.
]);
define STradSyn Ctx([
    SNonHigh -> 0 || EnglishStarVocalic SCon+ _ SCon EnglishStarVocalic
]);
define SFulkApo Ctx([
    [{*i}|{*u}|{*ų}] -> 0 || .#. SCon* SHeavy _ .#.,
    [{*i}|{*u}|{*ų}] -> 0 ||
        .#. SCon* SShort SCon SShort SCon+ _ .#.,
    [{*i}|{*u}|{*ų}] -> 0 ||
        .#. SCon* SHeavy EnglishStarVocalic SCon SCon+ _ .#.,
    [{*i}|{*u}|{*ų}] -> 0 || {*x} _ .#.,
    {*i} -> 0 || EnglishStarLongVowel _ .#.
] .o. [{*ᶜ} -> 0]);
define SLInsert [
    {*l} -> {*E} {*l} || EnglishStarVocalic SCon* [SCon - [{*t}|{*d}]] _ .#.
];
define SLBack [
    {*E} -> {*o} || EnglishStarBackVowel SCon+ _ {*l} .#.
];
define SLFront [{*E} -> {*e}];
define SLate [OEEpentheticVowel .o. SLInsert .o. SLBack .o. SLFront];
"""

CANDIDATES = {
    "soul-nom": "*sáiwalō",
    "soul-acc": "*sáiwalǭ",
    "soul-gen-ringe": "*sáiwalōz",
    "soul-gen-fulk": "*sáiwalôz",
    "soul-dat-fulk": "*sáiwalôi",
    "idle-fem": "*ḯdalō",
    "blessed-fem": "*áudagō",
    "head-neut-pl": "*xáubudō",
    "head-gen": "*xáubudas",
    "cattle-neut-pl": "*náutīnō",
}

# Stage inputs, not invented complete Proto-Germanic reconstructions.
CONTROLS = {
    "soul-light": ("sāwalu", "sāwalu"),
    "soul-long-nasal": ("sāwalǭ", "sāwlǭ"),
    "soul-prematurely-shortened": ("sāwalæ", "sāwalæ"),
    "idle-light": ("īdalu", "īdalu"),
    "idle-closed": ("īdalan", "īdlan"),
    "blessed-light": ("ēadagu", "ēadagu"),
    "blessed-closed-u": ("ēadagum", "ēadgum"),
    "head-light": ("xēaβudu", "xēaβudu"),
    "head-closed": ("xēaβudes", "xēaβdes"),
    "cattle-shortened-light": ("nēatinu", "nēatinu"),
    "cattle-shortened-long": ("nēatinô", "nēatnô"),
    "light-initial": ("werudu", "werudu"),
    "closed-medial": ("sāwalkǭ", "sāwalkǭ"),
    "long-medial": ("sāwālǭ", "sāwālǭ"),
    "stressed-medial": ("sāwálǭ", "sāwálǭ"),
    "nonsoul-nonhigh": ("tādakǭ", "tādkǭ"),
}

EPENTHESIS = {
    "bird": "fugl",
    "star": "tungl",
    "banner": "cumbl",
    "soul": "sāwl",
    "oblique": "sāwle",
    "dental-negative": "setl",
    "retained-vowel": "sāwul",
}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def star(text):
    return "".join("*" + token for token in re.findall(
        r"ēa|ēo|īe|īo|ea|eo|ie|io|ai|au|eu|iu|.", text))


def models(original):
    def replace(sequence, old, new):
        result = list(sequence)
        result[result.index(old)] = new
        return result

    def insert(sequence, rule):
        result = list(sequence)
        result.insert(result.index("OEHighVowelApocope"), rule)
        return result

    coverage = replace(original, "EnglishProtoInput", "SInput")
    no_proxy = replace(coverage, "OEInterStressRaising", "OELHWeakRaising")
    fulk = insert(no_proxy, "SFulkSyn")
    fulk = replace(fulk, "OEHighVowelApocope", "SFulkApo")
    for old in ("OEMedialSyncope", "OELAdjacentSyncope"):
        fulk = replace(fulk, old, "SIdentity")
    traditional = insert(no_proxy, "STradSyn")
    unrounded = list(fulk)
    unrounded.insert(unrounded.index("PWGmcSurvivingBimoricOUnrounding") + 1,
                     "SAccUnround")
    return {
        "identity": original,
        "input-coverage": coverage,
        "C-no-proxy": no_proxy,
        "C-nonhigh": insert(no_proxy, "SNonHighSyn"),
        "A-fulk": fulk,
        "A-unrounded-ending": unrounded,
        "B-no-new-epenthesis": traditional,
        "B-general-l-epenthesis": replace(
            traditional, "OEEpentheticVowel", "SLate"),
    }


def apply_sets(binary, states):
    from sound_change_order_sensitivity import batch_apply_down
    inputs = sorted({form for forms in states for form in forms})
    lookup = dict(zip(inputs, batch_apply_down(binary, inputs))) if inputs else {}
    return [sorted({value for form in forms for value in lookup[form]})
            for forms in states]


def trace(sequence, bins, inputs):
    states = [[value] for value in inputs]
    steps = []
    for stage in sequence:
        before = states
        states = apply_sets(bins["component:" + stage], states)
        if any(len(values) > 1 for values in states):
            raise RuntimeError("Ambiguous experimental stage: " + stage)
        steps.append(dict(stage=stage, before=before, after=states))
    return states, steps


def worker(output):
    import oe_pipeline
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from capr_runtime import RuntimeLayout
    from sound_change_order_sensitivity import batch_apply_down

    if not Path("/.dockerenv").exists() or GERMANIC == Path("/usr/app"):
        raise RuntimeError("Worker requires a container-private immutable source tree")
    canonical = RuntimeLayout(Path("/usr/app"), Path("/usr/app"), Path("/usr/app"), True)
    protected = [*canonical.fsts_dir.rglob("*"), *canonical.data_dir.rglob("*"),
                 *canonical.docs_dir.rglob("*"), *canonical.tools_dir.glob("*.py"),
                 *canonical.bin_dir.glob("*.bin"), canonical.build_manifest]
    before = {str(p): digest(p) for p in protected if p.is_file()}
    for relative in ("fsts/germanic.txt", "data/germanic-aligned-final.tsv"):
        if digest(GERMANIC / relative) != digest(canonical.germanic_dir / relative):
            raise RuntimeError("Baseline source drift: " + relative)
    rows = oe_pipeline.load_rows(GERMANIC / "data/germanic-aligned-final.tsv")
    population = [oe_pipeline.evaluation_input(row) for row in rows]
    baseline_dir = GERMANIC / "docs/sound_changes/cascade_baseline"
    with (baseline_dir / "cascade_baseline_outputs_legacy380.tsv").open() as handle:
        legacy = list(csv.DictReader(handle, delimiter="\t"))
    immutable = [oe_pipeline.evaluation_input(row) for row in legacy]
    candidates = [oe_pipeline.evaluation_input(
        {"proto_norm": oe_pipeline.normalize_proto(raw)}) for raw in CANDIDATES.values()]
    inputs = population + immutable + candidates
    original = [s.foma_identifier if s.kind == "named" else s.inline_text
                for s in oe_pipeline.stages()]
    sequences = models(original)
    definitions = DEFINITIONS
    for number, sequence in enumerate(sequences.values()):
        definitions += "\ndefine SWhole" + str(number) + " [" + " .o. ".join(sequence) + "];\n"
    components = sorted({item for sequence in sequences.values() for item in sequence}
                        | {"SFulkSyn", "SFulkApo", "SLate"}
                        | {"SWhole" + str(i) for i in range(len(sequences))})
    recipe = dict(definitions=definitions, insert_after="", insert_rule="", replace={},
                  component_checks=[dict(component=name) for name in components])
    results = {}
    with tempfile.TemporaryDirectory(prefix="capr_soul_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(GERMANIC / "fsts/germanic.txt", directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        bins = compile_isolated(GERMANIC / "fsts/germanic.txt", recipe, [], directory,
                                components_only=True)
        production = batch_apply_down(canonical.bin_dir / "old_english.bin", population)
        for number, (name, sequence) in enumerate(sequences.items()):
            print("model " + name, file=sys.stderr, flush=True)
            final, steps = trace(sequence, bins, inputs)
            whole = batch_apply_down(bins["component:SWhole" + str(number)], inputs)
            if whole != final:
                raise RuntimeError("Composed/component disagreement: " + name)
            if name == "identity":
                if final[:len(rows)] != production:
                    raise RuntimeError("Identity/production disagreement")
                immutable_identity = final[len(rows):len(rows) + len(legacy)]
            offset = len(rows) + len(legacy)
            results[name] = dict(
                order=sequence, final=final[:len(rows)],
                matched=sum(row["counterpart"] in values
                            for row, values in zip(rows, final)),
                deltas=[dict(row_id=row["row_id"], concept=row["concept"], old=old, new=new)
                        for row, old, new in zip(rows, production, final) if old != new],
                immutable380_deltas=[
                    dict(concept=row["concept"], input=row["proto_norm"], old=old, new=new)
                    for row, old, new in zip(
                        legacy, immutable_identity, final[len(rows):offset]) if old != new],
                candidates={
                    label: dict(input=raw, final=final[index],
                                steps=[dict(stage=s["stage"], before=s["before"][index],
                                            after=s["after"][index]) for s in steps])
                    for index, (label, raw) in enumerate(CANDIDATES.items(), offset)},
                transitions=[
                    dict(stage=s["stage"], changes=[
                        dict(row_id=row["row_id"], before=old, after=new)
                        for row, old, new in zip(rows, s["before"], s["after"]) if old != new])
                    for s in steps], composed_crosscheck=True)
        component = {}
        for rule in ("SFulkSyn", "SFulkApo", "SLate"):
            forms = [star(pair[0]) for pair in CONTROLS.values()]
            component[rule] = dict(zip(CONTROLS, batch_apply_down(
                bins["component:" + rule], forms)))
        epenthesis = dict(zip(EPENTHESIS, batch_apply_down(
            bins["component:SLate"], [star(form) for form in EPENTHESIS.values()])))
        # Inspect suffix development separately from the input grammar.
        staged = {}
        for name, sequence in sequences.items():
            if name not in ("identity", "A-fulk"):
                continue
            start = sequence.index("OEHighVowelApocope" if name == "identity" else "SFulkSyn")
            stage_inputs = [star(pair[0]) for pair in CONTROLS.values()]
            final, steps = trace(sequence[start:], bins, stage_inputs)
            staged[name] = dict(zip(CONTROLS, [
                dict(final=values, changes=[
                    dict(stage=s["stage"], before=s["before"][i], after=s["after"][i])
                    for s in steps if s["before"][i] != s["after"][i]])
                for i, values in enumerate(final)]))
        formal = {}
        for rule in ("SFulkSyn", "SFulkApo", "SLate"):
            binary = bins["component:" + rule]
            command = subprocess.run(
                ["foma", "-q", "-e", "load stack " + binary.name,
                 "-e", "test functional", "-e", "quit"],
                cwd=directory, text=True, capture_output=True, check=True, timeout=120)
            formal[rule] = dict(stdout=command.stdout, stderr=command.stderr)
    after = {str(p): digest(p) for p in protected if p.is_file()}
    if before != after:
        raise RuntimeError("Canonical production files changed")
    report = dict(base=BASE, definitions=DEFINITIONS, candidates=CANDIDATES,
                  controls=CONTROLS, rows=rows, models=results, component=component,
                  epenthesis=epenthesis,
                  staged=staged, formal=formal, production_unchanged=True,
                  protected_before=before, protected_after=after,
                  runtime=subprocess.check_output(["foma", "-v"], text=True).strip())
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, sort_keys=True)


def launch(experiment_id):
    from adjudication_control import run_logged
    from experiment_snapshot import create_snapshot

    root = GERMANIC.parent
    paths = sorted(set(
        list((GERMANIC / "tools").glob("*.py"))
        + list((GERMANIC / "data").glob("*.tsv"))
        + list((GERMANIC / "docs/sound_changes/cascade_baseline").glob("*.tsv"))
        + list((GERMANIC / "docs/sound_changes/cascade_baseline").glob("*.json"))
        + [GERMANIC / "fsts/germanic.txt", GERMANIC / "fsts/old_english_sandbox.txt",
           root / "backend/oe_input_context.py", root / "backend/compare_fst.py",
           Path(__file__)]))
    mapping = {f"file{i:03d}": str(p.relative_to(root)) for i, p in enumerate(paths)}
    manifest = root / ".capr-work/soul-layout.json"
    manifest.write_text(json.dumps(mapping))
    inputs = {label: root / relative for label, relative in mapping.items()}
    inputs["layout"] = manifest
    snapshot = create_snapshot(
        experiment_id, "Compare soul accounts without production adoption", inputs,
        variants={"phonological_hypotheses": DEFINITIONS},
        expected_outcomes={
            "A-fulk": "accusative sawle; preserve H+L+u, medial quality unresolved",
            "B": "syncope plus epenthesis cannot explain early metrical distribution",
            "C": "remove proxy alone is insufficient",
            "population": "report every delta, never refreeze"},
        negative_controls=[name for name in CONTROLS if name not in
                           ("soul-long-nasal", "idle-closed", "blessed-closed-u",
                            "head-closed", "cattle-shortened-long", "nonsoul-nonhigh")],
        environment={"runner": "capr-soul-fulk backend", "base": BASE})
    container = snapshot.stage_in_container()
    bootstrap = """
import json,shutil,sys,tempfile
from pathlib import Path
src=Path(sys.argv[1]); receipt=json.loads((src/'layout.json').read_text())
root=Path(tempfile.mkdtemp(prefix='capr_soul_source_'))
for label,relative in receipt.items():
    files=list(src.glob(label+'.*'))
    if len(files)!=1: raise RuntimeError(label)
    target=root/relative; target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(files[0],target)
for name in ('compare_fst.py','oe_input_context.py'):
    shutil.copyfile(root/'backend'/name,root/'Germanic'/name)
import subprocess
worker=root/'Germanic/docs/sound_changes/audits/soul-fulk-oblique/experiment.py'
subprocess.run(['python3',str(worker),'--worker','--output',sys.argv[2]],check=True)
"""
    destination = container + "/../" + experiment_id + "-results.json.gz"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c",
         bootstrap, container, destination], label="soul-models", log_dir=snapshot.staging_dir)
    if receipt["ok"]:
        subprocess.run(["docker", "compose", "cp", "backend:" + destination,
                        str(snapshot.staging_dir / "results.json.gz")], check=True)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Experimental execution only; no scientific adoption",
                      command_receipts=[receipt])
    print(snapshot.root)
    if not receipt["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--experiment-id")
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.worker:
        worker(args.output)
    elif args.experiment_id:
        launch(args.experiment_id)
    else:
        parser.error("--experiment-id or --worker is required")
