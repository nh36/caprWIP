"""Ordinary-entry weak-feminine cells; fixed production root and SC051 rules."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

REFERENCE = "1181f62303972f9538a3a4d8d18dd63ab2f35c70"
PROBES = {
    "flask_nompl": "*fláskōniz",
    "tongue_nompl": "*túngōniz",
    "tongue_nomsg": "*túngōn",
    "flask_nomsg": "*fláskōn",
    "ashes_nompl_conditional": "*áskōniz",
    "tongue_accsg": "*túngōnų",
    "flask_accsg": "*fláskōnų",
    "foldu_accsg_conditional": "*fúldōnų",
    "eorthu_accsg_conditional": "*érθōnų",
    "tongue_datpl": "*túngōmaz",
    "do_secondary_n": "*dōną",
}
DEFINITIONS = """
define FPTails [
    ō:{*ō} n:{*n} i:{*i} z:{*z} |
    ō:{*ō} n:{*n} i:{*i} |
    ō:{*ō} n:{*n} ų:{*ų} |
    ō:{*ō} m:{*m} a:{*a} z:{*z}
];
define FPNative [
    EnglishProtoNative |
    [{ᵘ}:{*ᵘ} | {ᶜ}:{*ᶜ} | 0]
    [pgrmStrongPlainHeavy | pgrmStrongPlainHeavyPrefixed |
     pgrmStrongNasal | pgrmStrongNasalPrefixed] FPTails
];
define FPGateway [
    _unambpart(FPNative) |
    _unambpart([[PGCellRaw.u - FPNative.u] .o. PGCellRaw])
];
define FPUnround Ctx([{*ō} -> {*ā} ||
    EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*n} .#.]);
"""
WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
from oe_pipeline import normalize_proto
p=json.loads(Path(sys.argv[1]).read_text())
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[2]).items()}
def trace(order,form):
    states=[form];history=[]
    for stage in order:
        after=sorted({y for xs in batch_apply_down(bins[stage],states) for y in xs})
        history.append({"stage":stage,"before":states,"after":after})
        states=after
        if not states:break
        assert len(states)==1 and states!=["+?"], (stage,states)
    return {"output":states,"trace":history}
result={"reference_sha":p["reference_sha"],
        "binary_sha256":{k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()},
        "orders":p["orders"],"admission":{},"variants":{}}
for relation,forms in {
    "EnglishProtoNative":["fláskōniz","túngōniz"],
    "PGCellRaw":["fláskōniz","túngōniz"],
    "pgrmInputTailVowel":["ōn","ōniz"],
    "PGCellStem":["an","ōn"],"FPTails":["ōniz","ōni","ōnų","ōmaz"],
}.items():
    result["admission"][relation]=dict(zip(forms,batch_apply_down(bins[relation],forms)))
for variant,order in p["orders"].items():
    result["variants"][variant]={}
    for name,raw in p["probes"].items():
        normalized=normalize_proto(raw)
        normal=trace(order,normalized)
        record={"raw":raw,"normalized_input":normalized,"normal_entry":normal}
        if normal["output"]:
            assert normal["trace"][0]["after"]==["*"+"*".join(normalized)], (variant,name)
        else:
            record["after_gateway_diagnostic"]=trace(order[1:],"*"+"*".join(normalized))
        result["variants"][variant][name]=record
Path(sys.argv[3]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({v:{n:r["normal_entry"]["output"] for n,r in ns.items()}
    for v,ns in result["variants"].items()},ensure_ascii=False,indent=2))
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", default="flask-nompl-1181f623-v1")
    args = parser.parse_args()
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    import oe_pipeline
    from adjudication_control import run_logged
    work = root / ".capr-work/flask-nompl-1181f623"
    work.mkdir(parents=True, exist_ok=True)
    source = work / "reference.txt"
    source.write_bytes(subprocess.check_output([
        "git", "show", REFERENCE + ":Germanic/fsts/germanic.txt"]))
    assert source.read_bytes() == (root / "Germanic/fsts/germanic.txt").read_bytes()
    pipeline = root / "Germanic/tools/oe_pipeline.py"
    assert pipeline.read_bytes() == subprocess.check_output([
        "git", "show", REFERENCE + ":Germanic/tools/oe_pipeline.py"])
    original = [s.inline_text if s.kind == "inline" else s.foma_identifier
                for s in oe_pipeline.stages()]
    admitted = list(original)
    assert admitted[0] == "EnglishProtoInput"
    admitted[0] = "FPGateway"
    secondary = list(admitted)
    secondary.remove("PNWGmcNStemNLoss")
    secondary.insert(secondary.index("PWGmcEarlyIApocope"), "PNWGmcNStemNLoss")
    short = list(secondary)
    short.remove("OEEarlyOShortening")
    short.insert(short.index("OESecondaryNasalization"), "OEEarlyOShortening")
    unround = list(secondary)
    unround.insert(unround.index("PWGmcSurvivingBimoricOUnrounding"), "FPUnround")
    orders = {"production": original, "admission_only": admitted,
              "secondary_n_only": secondary, "early_shortening": short,
              "early_unrounding": unround}
    components = list(dict.fromkeys([
        *(s for order in orders.values() for s in order),
        "EnglishProtoNative", "PGCellRaw", "pgrmInputTailVowel", "PGCellStem", "FPTails"]))
    recipe = {"id": "flask-nompl", "replace": {}, "insert_rule": None,
              "insert_after": None, "definitions": DEFINITIONS,
              "component_checks": [{"component": s} for s in components]}
    payload = {"reference_sha": REFERENCE, "orders": orders, "probes": PROBES}
    for name, value in (("recipe.json", recipe), ("payload.json", payload)):
        (work / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    note = Path(__file__).resolve().parent.parent / "flask-nominative-plural-followup.md"
    snapshot = experiment_snapshot.create_snapshot(
        args.snapshot_id, "Normal-entry inherited cells and two existing ending experiments.",
        {"source": source, "driver": Path(__file__).resolve(), "recipe": work / "recipe.json",
         "payload": work / "payload.json", "predictions": note, "pipeline": pipeline,
         "compiler": root / "Germanic/tools/anglo_frisian_experiments.py"},
        variants={k: " .o. ".join(v) for k, v in orders.items()},
        probes=[{"id": k, "input": v} for k, v in PROBES.items()],
        expected_outcomes={"see": "pre-execution predictions document"},
        negative_controls=["tunge nominative", "dōn secondary nasal", "fixed SC051"])
    compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
    output = compiled["container_output"] + "/observed.json"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u", "-c", WORKER,
         compiled["container_source"] + "/" + snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]), output],
        label="flask-nompl-focused", log_dir=snapshot.staging_dir)
    if not receipt["ok"]:
        snapshot.complete("failed", "Focused execution failed.", [compiled["receipt"], receipt])
        raise RuntimeError(Path(receipt["stderr_log"]).read_text())
    subprocess.run(["docker", "compose", "cp", "backend:" + output,
                    str(snapshot.staging_dir / "observed.json")], check=True)
    snapshot.complete("passed", "Measured focused experiments; no production adoption.",
                      [compiled["receipt"], receipt])
    observed = json.loads((snapshot.results_dir / "observed.json").read_text())
    checkpoints = {
        "EnglishProtoInput", "FPGateway", "PNWGmcNStemNLoss", "PWGmcEarlyIApocope",
        "EAFFinalZDeletion", "FPUnround", "EAFBrightening", "EAFBrighteningLongFinal",
        "OEARestoration", "OEHeavySyllableNasalApocope", "OEEarlyOShortening",
        "OESecondaryNasalization", "OEUnstressedFrontingEarly",
        "OEUnstressedLongVowelShortening", "OESkPalatalization"}
    for probes in observed["variants"].values():
        for probe in probes.values():
            for entry in ("normal_entry", "after_gateway_diagnostic"):
                if entry not in probe:
                    continue
                history = probe[entry]["trace"]
                probe[entry]["trace"] = [
                    s for s in history
                    if s["stage"] in checkpoints or s["before"] != s["after"] or s is history[-1]]
    (Path(__file__).resolve().parent / "observed.json").write_text(
        json.dumps(observed, ensure_ascii=False, indent=2) + "\n")
    print((snapshot.results_dir / Path(receipt["stdout_log"]).name).read_text())


if __name__ == "__main__":
    main()
