"""Pinned SC051 matrix; compose every named stage from complete raw inputs."""
import json
from pathlib import Path
import subprocess
import sys

REFERENCE = "77f314bf85035c23706b6b09b3a1855aa23c0620"
WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
from capr_runtime import layout,check_build_manifest
import oe_pipeline
p=json.loads(Path(sys.argv[1]).read_text())
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[2]).items()}
out=Path(sys.argv[3])
def trace(order,forms):
    states=[[f] for f in forms];histories=[[] for f in forms]
    for stage in order:
        flat=[x for group in states for x in group]
        applied=iter(batch_apply_down(bins[stage],flat) if flat else [])
        result=[]
        for i,group in enumerate(states):
            after=sorted({x for _ in group for x in next(applied)})
            histories[i].append({"stage":stage,"before":group,"after":after})
            result.append(after)
        states=result
    return states,histories
result={"reference_sha":p["reference_sha"],"variants":{}}
baseline=None
rt=layout()
assert not check_build_manifest(oe_pipeline.expected_snapshot_bins()+["old_english.bin"])
canonical=batch_apply_down(rt.bin_dir/"old_english.bin",[r["fst_input"] for r in p["rows"]])
for name,order in p["orders"].items():
    composed,histories=trace(order,[r["fst_input"] for r in p["rows"]])
    finals=composed
    assert all(len(s["after"])==1 and s["after"][0]!="+?"
               for h in histories for s in h),(name,"non-singleton selected intermediate")
    if baseline is None:
        assert finals==canonical, "reference full/component disagreement"
        baseline=finals
    item={"order":order,"matched":sum(v==[r["counterpart"]] for r,v in zip(p["rows"],finals)),
          "changed":[{"id":r["id"],"concept":r["concept"],"before":b,"after":f}
                     for r,b,f in zip(p["rows"],baseline,finals) if b!=f],
          "rows":[{**r,"output":f,"trace":h} for r,f,h in zip(p["rows"],finals,histories)],
          "controls":[]}
    components=p["control_orders"][name]
    for control in p["controls"]:
        actual,h=trace(components,[control["input"]])
        first_sk=next(s for s in order if s in ("OESkPalatalization","AGSkG","AGSkF"))
        suffix,sh=trace(order[order.index(first_sk):],[control["input"]])
        item["controls"].append({**control,"atomic_output":actual[0],
            "passes":actual[0]==[control["expected"]],"component_trace":h[0],
            "suffix_entry_before":first_sk,"suffix_output":suffix[0],"suffix_trace":sh[0]})
    for key,entry,before in [
        ("clay","*θ*á*n*x*ō*n","PGmcNasalLossBeforeX"),
        ("fringe","*w*l*ō*x*u*m","OEHLoss")]:
        final,h=trace(order[order.index(before):],[entry])
        item[key]={"entry":entry,"before":before,"output":final[0],"trace":h[0]}
    assert item["clay"]["output"]==["þō"]
    assert next(s["after"] for s in item["fringe"]["trace"] if s["stage"]=="OEHLoss")==["*w*l*ō*u*m"]
    result["variants"][name]=item
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(name,item["matched"],item["changed"],
          "controls",sum(c["passes"] for c in item["controls"]),"/",len(p["controls"]),flush=True)
'''


def main():
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    from adjudication_control import run_logged
    from anglo_frisian_experiments import corpus_rows
    from executable_facts import parse_defines
    import oe_pipeline
    work = root / ".capr-work/sc051-guard-77f314bf"
    work.mkdir(exist_ok=True)
    source = work / "reference.txt"
    source.write_bytes(subprocess.check_output([
        "git", "show", REFERENCE + ":Germanic/fsts/germanic.txt"]))
    for path in ("Germanic/tools/oe_pipeline.py", "Germanic/tools/anglo_frisian_experiments.py",
                 "Germanic/data/germanic-aligned-final.tsv", "Germanic/data/entry_context_metadata.tsv"):
        assert (root / path).read_bytes() == subprocess.check_output(["git", "show", REFERENCE + ":" + path]), path
    original = [s.inline_text if s.kind == "inline" else s.foma_identifier for s in oe_pipeline.stages()]
    sk = parse_defines(source.read_text())["OESkPalatalization"].body
    old = "EnglishStarFrontVowel _ (EnglishStarConsonant | .#.)"
    assert sk.count(old) == 1
    guarded = sk.replace(old, "EnglishStarFrontVowel _ [EnglishStarConsonant | .#.]")
    following = "[\n    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel\n]"
    assert guarded.count(" .o. " + following) == 1
    late = guarded.replace(" .o. " + following, "", 1)
    definitions = [
        "define AGSkG " + guarded + ";",
        "define AGSkL " + late + ";",
        "define AGSkF Ctx(" + following + ");",
        "define AGHold Ctx([[{*á} -> {*a} || _ {*s} {*k} {*ā} .#.] .o. EAFBrighteningStressed]);",
        "define AGRet FootCtx([{*æ} -> {*a} || _ {*s} {*k} {*ā} .#.]);",
    ]
    orders = {"identity": original}
    control_orders = {"identity": ["OESkPalatalization"]}
    for name in ("guard_only", "guard_split_early", "guard_retain_late",
                 "guard_retract_late", "guard_early_retain", "guard_early_retract"):
        order = list(original)
        early = name in ("guard_split_early", "guard_early_retain", "guard_early_retract")
        order[order.index("OESkPalatalization")] = "AGSkL" if early else "AGSkG"
        if early:
            order.insert(order.index("EAFBrighteningLongFinal"), "AGSkF")
        if "retain" in name:
            order[order.index("EAFBrightening")] = "AGHold"
        if "retract" in name:
            order.insert(order.index("EAFBrighteningLongFinal"), "AGRet")
        orders[name] = order
        control_orders[name] = ["AGSkF", "AGSkL"] if early else ["AGSkG"]
    controls = []
    for label, value, expected in [
        ("fisces","fiskes","fiʃes"), ("fiscas","fiskas","fiskas"),
        ("fixas-ks","fiksas","fiksas"), ("disces","diskes","diʃes"),
        ("discas","diskas","diskas"), ("wasce","waske","waʃe"),
        ("wascan","waskan","waskan"), ("thersce","θerske","θerʃe"),
        ("therscan","θerskan","θerskan"), ("threscan-context","θreskan","θreskan"),
        ("initial-front","skæp","ʃæp"), ("initial-back","skuldra","ʃuldra"),
        ("final-front","fisk","fiʃ"), ("final-back","ask","ask")]:
        controls.append({"id":label,"input":"*"+"*".join(value),
                         "expected":"*"+"*".join(expected),
                         "status":"noncorpus normalized stage-entry consonant control, not a complete PGmc derivation"})
    recipe = {"id":"sc051-required-context","replace":{},"insert_rule":None,"insert_after":None,
              "definitions":"\n".join(definitions),
              "component_checks":[{"component":s} for s in dict.fromkeys(
                  [s for order in orders.values() for s in order])]}
    payload = {"reference_sha":REFERENCE,"orders":orders,"control_orders":control_orders,
               "rows":corpus_rows(root / "Germanic/data/germanic-aligned-final.tsv"),"controls":controls}
    for name, value in (("recipe.json",recipe),("payload.json",payload)):
        (work/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n")
    snapshot = experiment_snapshot.create_snapshot(
        "sc051-guard-77f314bf-v2",
        "Isolate required following context, following-clause timing, and flask root alternatives.",
        {"source":source,"driver":Path(__file__).resolve(),"recipe":work/"recipe.json",
         "payload":work/"payload.json","corpus":root/"Germanic/data/germanic-aligned-final.tsv",
         "contexts":root/"Germanic/data/entry_context_metadata.tsv",
         "pipeline":root/"Germanic/tools/oe_pipeline.py","compiler":root/"Germanic/tools/anglo_frisian_experiments.py"},
        variants={k:" .o. ".join(v) for k,v in orders.items()},probes=controls,
        expected_outcomes={"measure":394,"baseline_matches":385},
        negative_controls=["fiscas","fixas","discas","wascan","therscan","final-back","all394"])
    compiled = snapshot.compile_isolated("source","recipe",components_only=True)
    (work/"compile.json").write_text(json.dumps(compiled,indent=2)+"\n")
    output = compiled["container_output"]+"/guard-results.json"
    receipt = run_logged(
        ["docker","compose","exec","-T","backend","python3","-u","-c",WORKER,
         compiled["container_source"]+"/"+snapshot.input_path("payload").name,
         json.dumps(compiled["bins"]),output],
        label="sc051-guard-seven-variants",log_dir=snapshot.staging_dir)
    if not receipt["ok"]:
        raise RuntimeError(Path(receipt["stderr_log"]).read_text())
    stdout = Path(receipt["stdout_log"]).read_text()
    subprocess.run(["docker","compose","cp","backend:"+output,str(snapshot.staging_dir/"observed.json")],check=True)
    snapshot.complete("passed","All actual deltas and control failures measured; no production adoption.",[compiled["receipt"],receipt])
    (work/"observed.json").write_text((snapshot.results_dir/"observed.json").read_text())
    print(stdout)


if __name__ == "__main__":
    main()
