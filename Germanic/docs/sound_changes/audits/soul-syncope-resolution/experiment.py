#!/usr/bin/env python3
"""Focused immutable factorial assays; never modifies production."""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
GERMANIC = HERE.parents[3]
ROOT = GERMANIC.parent
sys.path.insert(0, str(GERMANIC / "tools"))
OLD_PATH = HERE.parent / "soul-fulk-oblique/experiment.py"
spec = importlib.util.spec_from_file_location("soul_prior", OLD_PATH)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
BASE = "22de1004cea8829c775ea25c21c07db943d4b8e2"
EXTRA = """
define TInput [
    SInput|pgrmStrongPlainHeavy SCellStem SCellStem SCellEnd
];
define TNonHigh Ctx([
    SNonHigh -> 0 || .#. SCon* EnglishStarVocalic SCon+ _ SFollowing .#.
]);
"""


def models(original):
    def replace(seq, old, new):
        answer = list(seq)
        answer[answer.index(old)] = new
        return answer

    def insert(seq, rule):
        answer = list(seq)
        answer.insert(answer.index("OEHighVowelApocope"), rule)
        return answer

    coverage = replace(original, "EnglishProtoInput", "TInput")
    bare = replace(coverage, "OEInterStressRaising", "OELHWeakRaising")
    c = insert(bare, "SNonHighSyn")
    d = replace(c, "OEHighVowelApocope", "SFulkApo")
    e = replace(d, "SNonHighSyn", "SFulkSyn")
    return {
        "A-production": original,
        "A-coverage": coverage,
        "B-no-proxy": bare,
        "C-nonhigh": c,
        "D-nonhigh-fulk-apo": d,
        "E-high-old-apo": replace(e, "SFulkApo", "OEHighVowelApocope"),
        "E-high-retained": e,
        "E-no65": replace(e, "OEMedialSyncope", "SIdentity"),
        "E-no66": replace(e, "OELAdjacentSyncope", "SIdentity"),
        "F-old-broad-A": replace(
            replace(e, "OEMedialSyncope", "SIdentity"),
            "OELAdjacentSyncope", "SIdentity"),
        "G-light-nonhigh": replace(c, "SNonHighSyn", "TNonHigh"),
    }


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def worker(output):
    import oe_pipeline
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from capr_runtime import RuntimeLayout
    from sound_change_order_sensitivity import batch_apply_down

    if not Path("/.dockerenv").exists() or GERMANIC == Path("/usr/app"):
        raise RuntimeError("Requires container-private frozen sources")
    canonical = RuntimeLayout(Path("/usr/app"), Path("/usr/app"), Path("/usr/app"), True)
    paths = [*canonical.fsts_dir.rglob("*"), *canonical.data_dir.rglob("*"),
             *canonical.docs_dir.rglob("*"), *canonical.tools_dir.glob("*.py"),
             *canonical.bin_dir.glob("*.bin"), canonical.build_manifest]
    protected = {str(p): sha(p) for p in paths if p.is_file()}
    for relative in ("fsts/germanic.txt", "data/germanic-aligned-final.tsv"):
        if sha(GERMANIC / relative) != sha(Path("/usr/app") / relative):
            raise RuntimeError("Canonical scientific baseline drift")
    rows = oe_pipeline.load_rows(GERMANIC / "data/germanic-aligned-final.tsv")
    with (GERMANIC / "docs/sound_changes/cascade_baseline/"
          "cascade_baseline_outputs_legacy380.tsv").open() as handle:
        legacy = list(csv.DictReader(handle, delimiter="\t"))
    candidates = {**prior.CANDIDATES, "good-acc": "*gōdanǭ",
                  "blind-acc": "*blíndanǭ", "find-complete-acc": "*fúnðananǭ"}
    additional = json.loads((HERE / "controls.json").read_text())
    controls = {**prior.CONTROLS, **{
        c["id"]: (c["input"], c["expected"].replace(" ", "")) for c in additional}}
    inputs = [oe_pipeline.evaluation_input(row) for row in rows + legacy]
    inputs += [oe_pipeline.evaluation_input(
        {"proto_norm": oe_pipeline.normalize_proto(raw)}) for raw in candidates.values()]
    original = [s.foma_identifier if s.kind == "named" else s.inline_text
                for s in oe_pipeline.stages()]
    sequences = models(original)
    definitions = prior.DEFINITIONS + EXTRA
    for i, sequence in enumerate(sequences.values()):
        definitions += "\ndefine TWhole" + str(i) + " [" + " .o. ".join(sequence) + "];\n"
    names = sorted({s for seq in sequences.values() for s in seq}
                   | {"SFulkSyn", "SNonHighSyn", "SFulkApo", "TNonHigh"}
                   | {"TWhole" + str(i) for i in range(len(sequences))})
    recipe = dict(definitions=definitions, insert_after="", insert_rule="", replace={},
                  component_checks=[dict(component=name) for name in names])
    results, formal = {}, {}
    with tempfile.TemporaryDirectory(prefix="capr_syncope_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(GERMANIC / "fsts/germanic.txt", directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        bins = compile_isolated(GERMANIC / "fsts/germanic.txt", recipe, [], directory,
                                components_only=True)
        production = batch_apply_down(canonical.bin_dir / "old_english.bin", inputs[:len(rows)])
        for i, (name, sequence) in enumerate(sequences.items()):
            print("model " + name, file=sys.stderr, flush=True)
            final, steps = prior.trace(sequence, bins, inputs)
            if final != batch_apply_down(bins["component:TWhole" + str(i)], inputs):
                raise RuntimeError("Whole/component disagreement: " + name)
            if i == 0:
                identity = final
                if final[:len(rows)] != production:
                    raise RuntimeError("Production/identity disagreement")
            offset = len(rows) + len(legacy)
            results[name] = dict(
                order=sequence, final=final,
                matched=sum(row["counterpart"] in values
                            for row, values in zip(rows, final)),
                deltas=[dict(row_id=row["row_id"], concept=row["concept"], old=a, new=b)
                        for row, a, b in zip(rows, identity, final) if a != b],
                immutable380_deltas=[
                    dict(concept=row["concept"], input=row["proto_norm"], old=a, new=b)
                    for row, a, b in zip(legacy, identity[len(rows):offset],
                                         final[len(rows):offset]) if a != b],
                candidates={key: dict(input=raw, final=final[index])
                            for index, (key, raw) in enumerate(candidates.items(), offset)},
                transitions=[dict(stage=s["stage"], changes=[
                    dict(index=j, before=a, after=b)
                    for j, (a, b) in enumerate(zip(s["before"], s["after"])) if a != b])
                    for s in steps],
                traces={row["row_id"]: [
                    dict(stage=s["stage"], before=s["before"][j], after=s["after"][j])
                    for s in steps]
                    for j, row in enumerate(rows)
                    if row["row_id"] in {"2011", "2201", "2282", "2139", "2208", "2250",
                                         "2335", "2148", "2302", "2336"}},
                candidate_traces={key: [
                    dict(stage=s["stage"], before=s["before"][j], after=s["after"][j])
                    for s in steps] for j, key in enumerate(candidates, offset)},
                composed_crosscheck=True,
                finite_ambiguity=[j for j, values in enumerate(final) if len(values) > 1])
        component = {rule: dict(zip(controls, batch_apply_down(
            bins["component:" + rule], [prior.star(pair[0]) for pair in controls.values()])))
            for rule in ("SNonHighSyn", "SFulkSyn", "SFulkApo", "TNonHigh")}
        for rule in ["SNonHighSyn", "SFulkSyn", "SFulkApo", "TNonHigh",
                     *("TWhole" + str(i) for i in range(len(sequences)))]:
            result = subprocess.run(
                ["foma", "-q", "-e", "load stack " + bins["component:" + rule].name,
                 "-e", "test functional", "-e", "quit"], cwd=directory,
                text=True, capture_output=True, check=True, timeout=120)
            formal[rule] = dict(stdout=result.stdout, stderr=result.stderr)
    after = {str(p): sha(p) for p in paths if p.is_file()}
    if protected != after:
        raise RuntimeError("Canonical files changed during experiment")
    report = dict(base=BASE, definitions=definitions, rows=rows, immutable380=legacy,
                  input_order=inputs, candidates=candidates, controls=controls,
                  additional_control_evidence=additional, models=results,
                  component=component, formal=formal, production_unchanged=True,
                  protected_before=protected, protected_after=after,
                  runtime=subprocess.check_output(["foma", "-v"], text=True).strip())
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, sort_keys=True)


def launch(experiment_id):
    from adjudication_control import run_logged
    from experiment_snapshot import create_snapshot

    paths = sorted(set(
        list((GERMANIC / "tools").glob("*.py"))
        + list((GERMANIC / "data").glob("*.tsv"))
        + list((GERMANIC / "docs/sound_changes/cascade_baseline").glob("*.tsv"))
        + list((GERMANIC / "docs/sound_changes/cascade_baseline").glob("*.json"))
        + [GERMANIC / "fsts/germanic.txt", GERMANIC / "fsts/old_english_sandbox.txt",
           ROOT / "backend/oe_input_context.py", ROOT / "backend/compare_fst.py",
           Path(__file__), OLD_PATH, HERE / "controls.json", HERE / "preregistration.md"]))
    mapping = {f"file{i:03d}": str(p.relative_to(ROOT)) for i, p in enumerate(paths)}
    manifest = ROOT / ".capr-work/syncope-layout.json"
    manifest.write_text(json.dumps(mapping))
    inputs = {label: ROOT / relative for label, relative in mapping.items()}
    inputs["layout"] = manifest
    snapshot = create_snapshot(
        experiment_id, "Separate nonhigh syncope, apocope and old syncope fragments",
        inputs, variants={"definitions": prior.DEFINITIONS + EXTRA},
        expected_outcomes={"question": "Classify every delta; no zero-delta presumption",
                           "controls": "Source-selected before execution"},
        negative_controls=[c["id"] for c in json.loads((HERE / "controls.json").read_text())
                           if c["input"] == c["expected"]],
        environment={"runner": "private capr-soul-syncope backend", "base": BASE})
    evidence = ROOT / ".capr-work/snapshot.json"
    evidence.write_text(json.dumps({"snapshot_root": str(snapshot.root)}))
    subprocess.run([sys.executable, str(GERMANIC / "tools/adjudicate.py"),
                    "SC065", "--run", "advance", "SNAPSHOT", "--evidence", str(evidence)],
                   check=True)
    container = snapshot.stage_in_container()
    bootstrap = """
import json,shutil,sys,tempfile,subprocess
from pathlib import Path
src=Path(sys.argv[1]); layout=json.loads((src/'layout.json').read_text())
root=Path(tempfile.mkdtemp(prefix='capr_syncope_source_'))
for label,relative in layout.items():
    files=list(src.glob(label+'.*'))
    if len(files)!=1: raise RuntimeError(label)
    dest=root/relative; dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(files[0],dest)
for name in ('compare_fst.py','oe_input_context.py'):
    shutil.copyfile(root/'backend'/name,root/'Germanic'/name)
worker=root/'Germanic/docs/sound_changes/audits/soul-syncope-resolution/experiment.py'
subprocess.run(['python3',str(worker),'--worker','--output',sys.argv[2]],check=True)
"""
    destination = container + "/../" + experiment_id + "-results.json.gz"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c",
         bootstrap, container, destination], label="syncope-factorial",
        log_dir=snapshot.staging_dir)
    if receipt["ok"]:
        subprocess.run(["docker", "compose", "cp", "backend:" + destination,
                        str(snapshot.staging_dir / "results.json.gz")], check=True)
    snapshot.complete("passed" if receipt["ok"] else "failed",
                      "Execution outcome only, not a scientific adoption decision",
                      command_receipts=[receipt])
    (snapshot.root / "staging").symlink_to("results", target_is_directory=True)
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
