"""Focused root-vowel comparisons; production source and SC051 stay fixed."""
import json
from pathlib import Path
import subprocess
import sys

REFERENCE = "e7a9bed5c22b000131bf21252d2af7bda873c313"
PROBES = [
    ("flask", "*fláskōn", False),
    ("ashes", "*áskōn", False),
    ("wash_inf", "*wáskaną", False),
    ("mesh_acc_pl", "*máskō", False),
    ("mesh_wa_acc_pl_conditional", "*máskwō", False),
    ("mesh_wa_early_glide_loss_diagnostic", "*máskwō", True),
    ("mesh_dat_pl", "*máskamaz", False),
    ("rest_negative", "*rástōz", False),
]
DEFINITIONS = """
define WMHold Ctx([[{*á} -> {*a} || _ {*s} {*k} {*ā} .#.]
    .o. EAFBrighteningStressed]);
define WMRet FootCtx([{*æ} -> {*a} || _ {*s} {*k} {*ā} .#.]);
define WMBroad Ctx([[{*á} -> {*a} || _
    [EnglishStarConsonant | EnglishStarGeminate | {*s} {*k} | {*s} {*t}]
    [EnglishStarBackVowel | {*ą} | {*ô}]]
    .o. EAFBrighteningStressed]);
define WMGlideLoss Ctx([{*w} -> 0 || EnglishStarConsonant _ {*u} .#.]);
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
        if not states:
            break
        assert len(states)==1 and states!=["+?"], (stage,states)
    return {"output":states,"trace":history}
result={"reference_sha":p["reference_sha"],"predictions_sha256":p["predictions_sha256"],
        "binary_sha256":{k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()},
        "variants":{}}
for variant,original in p["orders"].items():
    result["variants"][variant]={}
    for name,raw,bridge in p["probes"]:
        order=list(original)
        if bridge:
            order.insert(order.index("PNWGmcFinalLongORaising")+1,"WMGlideLoss")
        normalized=normalize_proto(raw)
        normal=trace(order,normalized)
        tokenized="*"+"*".join(normalized)
        diagnostic=trace(order[1:],tokenized)
        if normal["output"]:
            assert normal["output"]==diagnostic["output"], (variant,name)
        result["variants"][variant][name]={
            "raw":raw,"normalized_raw_input":normalized,"normal_entry":normal,
            "setup":"Ringe–Taylor p.16 early w-loss diagnostic" if bridge else "unchanged non-root stages",
            "diagnostic_entry":"immediately after EnglishProtoInput",
            "tokenized_input":tokenized,"post_tokenization_diagnostic":diagnostic}
Path(sys.argv[3]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({v:{n:{"normal":d["normal_entry"]["output"],
    "diagnostic":d["post_tokenization_diagnostic"]["output"]} for n,d in ns.items()}
    for v,ns in result["variants"].items()},ensure_ascii=False,indent=2))
'''


def main():
    import hashlib
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    from adjudication_control import run_logged
    import oe_pipeline
    work = root / ".capr-work/wash-mesh-e7a9bed5"
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
    assert original[0] == "EnglishProtoInput"
    orders = {"baseline": original}
    for variant, relation in (("narrow_retention", "WMHold"), ("broad_retention", "WMBroad")):
        order = list(original)
        order[order.index("EAFBrightening")] = relation
        orders[variant] = order
    retract = list(original)
    retract.insert(retract.index("EAFBrighteningLongFinal"), "WMRet")
    orders["narrow_retraction"] = retract
    note = Path(__file__).resolve().parent.parent / "wash-mesh-external-controls.md"
    recipe = {
        "id": "wash-mesh-root-only", "replace": {}, "insert_rule": None, "insert_after": None,
        "definitions": DEFINITIONS,
        "component_checks": [{"component": s} for s in dict.fromkeys([
            *(s for order in orders.values() for s in order), "WMGlideLoss"])],
    }
    payload = {"reference_sha": REFERENCE, "orders": orders, "probes": PROBES,
               "predictions_sha256": hashlib.sha256(note.read_bytes()).hexdigest()}
    for name, value in (("recipe.json", recipe), ("payload.json", payload)):
        (work / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    snapshot = experiment_snapshot.create_snapshot(
        "wash-mesh-root-only-e7a9bed5",
        "Evidence-fixed wash/net cells; predictions frozen before execution; fixed SC051.",
        {"source": source, "driver": Path(__file__).resolve(), "recipe": work / "recipe.json",
         "payload": work / "payload.json", "predictions": note, "pipeline": pipeline,
         "compiler": root / "Germanic/tools/anglo_frisian_experiments.py"},
        variants={k: " .o. ".join(v) for k, v in orders.items()},
        probes=[{"id": n, "input": f, "early_glide_loss_diagnostic": b}
                for n, f, b in PROBES],
        expected_outcomes={"predictions_sha256": payload["predictions_sha256"]},
        negative_controls=["rest", "unchanged SC051 and timing"])
    compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
    output = compiled["container_output"] + "/observed.json"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u", "-c", WORKER,
         compiled["container_source"] + "/" + snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]), output],
        label="wash-mesh-four-root-treatments", log_dir=snapshot.staging_dir)
    if not receipt["ok"]:
        snapshot.complete("failed", "Focused probe execution failed.", [compiled["receipt"], receipt])
        raise RuntimeError(Path(receipt["stderr_log"]).read_text())
    subprocess.run(["docker", "compose", "cp", "backend:" + output,
                    str(snapshot.staging_dir / "observed.json")], check=True)
    stdout = Path(receipt["stdout_log"]).read_text()
    snapshot.complete("passed", "Focused probes only; no production adoption.",
                      [compiled["receipt"], receipt])
    observed = json.loads((snapshot.results_dir / "observed.json").read_text())
    checkpoints = {
        "EnglishProtoInput", "PNWGmcAToUBeforeM", "PNWGmcFinalLongORaising",
        "WMGlideLoss", "PNWGmcNStemNLoss", "PWGmcFinalBareALoss",
        "PWGmcSurvivingBimoricOUnrounding", "EAFBrightening", "WMHold", "WMRet",
        "WMBroad", "EAFBrighteningLongFinal", "OEARestoration", "OESkPalatalization",
    }
    for probes in observed["variants"].values():
        for probe in probes.values():
            for entry in ("normal_entry", "post_tokenization_diagnostic"):
                history = probe[entry]["trace"]
                probe[entry]["trace"] = [
                    s for s in history
                    if s["stage"] in checkpoints or s["before"] != s["after"] or s is history[-1]]
    observed["trace_policy"] = "Changed relations, named checkpoints, final; full histories in sealed snapshot."
    (Path(__file__).resolve().parent / "observed.json").write_text(
        json.dumps(observed, ensure_ascii=False, indent=2) + "\n")
    print(stdout)


if __name__ == "__main__":
    main()
