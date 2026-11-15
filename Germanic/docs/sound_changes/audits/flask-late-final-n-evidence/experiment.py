"""Full raw-input comparison of the exact archived late_final_n candidate."""
import argparse
import json
from pathlib import Path
import runpy
import subprocess
import sys

REFERENCE = "1bad32cd15dfdc10c154c3e90fcfe9afd0e42eb4"
RECIPE_SHA256 = "91c1e6c199ab21578c9085736bf7c9378d04dacbf7a603d824700c8e7ec8bbeb"
WORKER = r'''
import csv,hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
from oe_pipeline import normalize_proto
p=json.loads(Path(sys.argv[1]).read_text())
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[2]).items()}
out=Path(sys.argv[3]);out.mkdir()
hashes={k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()}
if p["reuse_components"]:
    assert hashes==p["expected_binary_sha256"],"Cached component identity changed"
histories={}
def run(label,order,rows):
    states={r["id"]:[r["fst_input"]] for r in rows}
    traces={r["id"]:[] for r in rows}
    for stage in order:
        active=[(key,form) for key,forms in states.items() for form in forms]
        if not active:break
        applied=batch_apply_down(bins[stage],[form for _,form in active])
        after={key:set() for key in states}
        for (key,_),outputs in zip(active,applied):
            after[key].update(outputs)
        for key,before in states.items():
            if before:
                traces[key].append({"stage":stage,"before":before,
                                    "after":sorted(after[key])})
        states={key:sorted(forms) for key,forms in after.items()}
    histories[label]=traces
    result={}
    for row in rows:
        key=row["id"];history=traces[key]
        result[key]={"input":row["fst_input"],"counterpart":row["counterpart"],
            "gateway":history[0]["after"],"admitted":bool(history[0]["after"]),
            "output":states[key],"match":row["counterpart"] in states[key],
            "failed_at":next((s["stage"] for s in history if not s["after"]),None),
            "ambiguities":[{"stage":s["stage"],"outputs":s["after"]}
                           for s in history if len(s["after"])>1]}
    print(label,json.dumps({"rows":len(rows),
        "admitted":sum(r["admitted"] for r in result.values()),
        "matches":sum(r["match"] for r in result.values()),
        "ambiguous":sum(bool(r["ambiguities"]) for r in result.values())}),flush=True)
    return result
def differences(before,after):
    result=[]
    for key in before:
        a,b=before[key],after[key]
        changes=[field for field in ("admitted","output","match")
                 if a[field]!=b[field]]
        if len(a["gateway"])!=len(b["gateway"]):changes.append("gateway_cardinality")
        aliases={"FPGateway":"EnglishProtoInput","FLEarly":"OEEarlyOShortening"}
        canonical=lambda r:[(aliases.get(s["stage"],s["stage"]),s["outputs"])
                            for s in r["ambiguities"]]
        if canonical(a)!=canonical(b):changes.append("intermediate_ambiguity")
        if changes:
            result.append({"id":key,"changed":changes,"before":a,"after":b})
    return result
orders=p["orders"];rows=p["rows"]
variants={}
variants["production"]=run("production",orders["production"],rows)
variants["late_final_n"]=run("late_final_n",orders["late_final_n"],rows)
selected=[dict(r) for r in rows]
flask=next(r for r in selected if r["id"]=="2016")
assert flask==p["flask_original"]
flask.update(p["flask_selection"])
assert all(a==b for a,b in zip(rows,selected) if a["id"]!="2016")
variants["selected"]=run("selected",orders["late_final_n"],selected)
unchanged=differences(variants["production"],variants["late_final_n"])
selection=differences(variants["late_final_n"],variants["selected"])
against_reference=differences(variants["production"],variants["selected"])
if any(r["id"]!="2016" for r in unchanged+selection):
    for label in ("gateway_only","protected_n"):
        variants[label]=run(label,orders[label],rows)
controls=[{"id":key,"fst_input":normalize_proto(raw),"counterpart":""}
          for key,raw in p["raw"].items()]
control_results={}
for label in ("production","late_final_n"):
    control_results[label]=run("controls_"+label,orders[label],controls)
for key,record in control_results["late_final_n"].items():
    assert record["gateway"]==["*"+"*".join(normalize_proto(p["raw"][key]))],key
control_changes=[{"id":key,"before":p["previous_controls"][key],
                 "after":record["output"]}
    for key,record in control_results["late_final_n"].items()
    if record["output"]!=p["previous_controls"][key]]
summary={label:{"rows":len(records),
    "admitted":sum(r["admitted"] for r in records.values()),
    "with_output":sum(bool(r["output"]) for r in records.values()),
    "matches":sum(r["match"] for r in records.values()),
    "gateway_ambiguities":sum(len(r["gateway"])>1 for r in records.values()),
    "intermediate_ambiguities":sum(bool(r["ambiguities"]) for r in records.values()),
    "final_ambiguities":sum(len(r["output"])>1 for r in records.values())}
    for label,records in variants.items()}
result={"reference_sha":p["reference_sha"],"recipe_sha256":p["recipe_sha256"],
    "reused_components":p["reuse_components"],"binary_sha256":hashes,"orders":orders,
    "summary":summary,"variants":variants,"controls":control_results,
    "unchanged_vocabulary_diff":unchanged,"selection_only_diff":selection,
    "selected_vs_production_diff":against_reference,"control_changes":control_changes}
(out/"observed.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
(out/"all_traces.json").write_text(json.dumps(histories,ensure_ascii=False)+"\n")
with (out/"corpus.tsv").open("w") as handle:
    writer=csv.writer(handle,delimiter="\t")
    writer.writerow(["id","concept","input","counterpart","production","candidate",
                     "production_match","candidate_match","selected_input",
                     "selected_counterpart","selected_output","selected_match"])
    for row,new in zip(rows,selected):
        key=row["id"];a,b,c=[variants[label][key]
                             for label in ("production","late_final_n","selected")]
        writer.writerow([key,row["concept"],row["proto"],row["counterpart"],
            " | ".join(a["output"])," | ".join(b["output"]),int(a["match"]),
            int(b["match"]),new["proto"],new["counterpart"],
            " | ".join(c["output"]),int(c["match"])])
with (out/"decisive_traces.tsv").open("w") as handle:
    writer=csv.writer(handle,delimiter="\t")
    writer.writerow(["run","id","ordinal","stage","before","after"])
    changed={r["id"] for r in unchanged+selection+against_reference}
    for label,traces in histories.items():
        for key,history in traces.items():
            if not label.startswith("controls_") and key not in changed:continue
            for index,step in enumerate(history,1):
                writer.writerow([label,key,index,step["stage"],
                    " | ".join(step["before"])," | ".join(step["after"])])
print(json.dumps({"summary":summary,"unchanged_diff_ids":[r["id"] for r in unchanged],
    "selection_diff_ids":[r["id"] for r in selection],
    "control_changes":control_changes},ensure_ascii=False),flush=True)
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", default="flask-late-n-1bad32cd-v1")
    parser.add_argument("--reuse-components", type=Path)
    args = parser.parse_args()
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import hashlib
    import experiment_snapshot
    import oe_pipeline
    from adjudication_control import run_logged
    from anglo_frisian_experiments import corpus_rows

    audits = Path(__file__).resolve().parent.parent
    previous_dir = audits / "flask-attested-cells-evidence"
    previous = json.loads((previous_dir / "observed.json").read_text())
    driver = runpy.run_path(str(previous_dir / "experiment.py"))
    old_snapshot = root / ".capr-work/experiments/flask-cells-a829dfcb-v1/snapshot"
    recipe_path = old_snapshot / "recipe.json"
    if not recipe_path.exists():
        older = runpy.run_path(str(audits / "flask-nominative-plural-evidence/experiment.py"))
        definitions = older["DEFINITIONS"].replace(
            "define FPTails [",
            "define FPTails [ ō:{*ō} n:{*n} u:{*u} n:{*n} z:{*z} |") + driver["EXTRA"]
        components = list(dict.fromkeys(
            stage for order in previous["orders"].values() for stage in order))
        recipe = {"id": "flask-cells", "replace": {}, "insert_rule": None,
                  "insert_after": None, "definitions": definitions,
                  "component_checks": [{"component": s} for s in components]}
        work = root / ".capr-work/flask-late-n-1bad32cd"
        work.mkdir(parents=True, exist_ok=True)
        recipe_path = work / "recipe.json"
        recipe_path.write_text(json.dumps(recipe, ensure_ascii=False, indent=2) + "\n")
    assert hashlib.sha256(recipe_path.read_bytes()).hexdigest() == RECIPE_SHA256
    source = root / "Germanic/fsts/germanic.txt"
    pipeline = root / "Germanic/tools/oe_pipeline.py"
    for path in (source, pipeline):
        assert path.read_bytes() == subprocess.check_output(
            ["git", "show", REFERENCE + ":" + str(path.relative_to(root))])
    original = [s.inline_text if s.kind == "inline" else s.foma_identifier
                for s in oe_pipeline.stages()]
    assert original == previous["orders"]["production"]
    orders = dict(previous["orders"])
    orders["gateway_only"] = ["FPGateway", *original[1:]]
    tsv = root / "Germanic/data/germanic-aligned-final.tsv"
    rows = corpus_rows(tsv)
    assert len(rows) == len({r["id"] for r in rows}) == 394
    flask = next(r for r in rows if r["id"] == "2016")
    context = oe_pipeline.context_for_row(
        flask["id"], flask["proto"], oe_pipeline.contexts_for_tsv(tsv))
    norm = oe_pipeline.normalize_proto("*fláskōniz")
    payload = {"reference_sha": REFERENCE, "recipe_sha256": RECIPE_SHA256,
        "orders": orders, "rows": rows, "flask_original": flask,
        "flask_selection": {"proto": "*fláskōniz", "proto_norm": norm,
                            "fst_input": context.encode(norm), "counterpart": "flascan"},
        "raw": driver["RAW"], "reuse_components": bool(args.reuse_components),
        "expected_binary_sha256": previous["binary_sha256"],
        "previous_controls": {k: v["normal_entry"]["output"]
                             for k, v in previous["variants"]["late_final_n"].items()}}
    work = root / ".capr-work/flask-late-n-1bad32cd"
    work.mkdir(parents=True, exist_ok=True)
    payload_path = work / "payload.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    inputs = {"source": source, "pipeline": pipeline, "corpus": tsv,
        "context": tsv.with_name(oe_pipeline.METADATA_FILENAME),
        "driver": Path(__file__).resolve(), "recipe": recipe_path, "payload": payload_path,
        "previous_evidence": previous_dir / "observed.json",
        "lookup_helper": root / "Germanic/tools/sound_change_order_sensitivity.py",
        "context_helper": Path(oe_pipeline.context_for_row.__code__.co_filename),
        "predictions": audits / "flask-late-final-n-adoption.md"}
    if args.reuse_components:
        inputs["cached_manifest"] = args.reuse_components
    snapshot = experiment_snapshot.create_snapshot(
        args.snapshot_id, "Mandatory 394-row exact-candidate and selection comparisons.",
        inputs, variants={k: " .o. ".join(v) for k, v in orders.items()},
        probes=[{"id": r["id"], "input": r["fst_input"]} for r in rows],
        expected_outcomes={"unchanged": "zero output changes",
                           "selection": "only 2016, flæsċe → flascan"},
        negative_controls=["SC051 fixed", "other 393 rows", "all 15 prior controls"])
    receipts = []
    if args.reuse_components:
        container = snapshot.stage_in_container()
        bins = json.loads(args.reuse_components.read_text())
    else:
        compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
        container, bins = compiled["container_source"], compiled["bins"]
        receipts.append(compiled["receipt"])
    output = container + "-results"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u", "-c", WORKER,
         container + "/" + snapshot.input_path("payload").name, json.dumps(bins), output],
        label="flask-late-n-full-corpus", log_dir=snapshot.staging_dir)
    receipts.append(receipt)
    if not receipt["ok"]:
        snapshot.complete("failed", "Corpus worker failed; inspect sealed stderr.", receipts)
        raise RuntimeError("Inspect the failed experiment's results logs.")
    names = ("observed.json", "all_traces.json", "corpus.tsv", "decisive_traces.tsv")
    for name in names:
        subprocess.run(["docker", "compose", "cp", "backend:" + output + "/" + name,
                        str(snapshot.staging_dir / name)], check=True)
    snapshot.complete("passed", "Measured both complete comparisons and independent controls.",
                      receipts, evidence={"cached_components_verified": bool(args.reuse_components)})
    for name in names:
        if name != "all_traces.json":
            (Path(__file__).resolve().parent / name).write_bytes(
                (snapshot.results_dir / name).read_bytes())
    print((snapshot.results_dir / Path(receipt["stdout_log"]).name).read_text())


if __name__ == "__main__":
    main()
