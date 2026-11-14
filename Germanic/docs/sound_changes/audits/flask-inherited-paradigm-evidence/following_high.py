"""Counterfeeding and shortening/nasalization experiment using frozen stage bins."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudication_control as control
import experiment_snapshot

WORKER = r'''
import hashlib,json,sys
from pathlib import Path
sys.path.insert(0,"/usr/app/tools")
from sound_change_order_sensitivity import batch_apply_down
bins={k.removeprefix("component:"):Path(v) for k,v in json.loads(sys.argv[1]).items()}
payload=json.loads(Path(sys.argv[2]).read_text())
original=payload["orders"]["identity"]
early=list(original);early.remove("PNWGmcNStemNLoss")
early.insert(early.index("PWGmcEarlyIApocope"),"PNWGmcNStemNLoss")
short=list(early);short.remove("OEEarlyOShortening")
short.insert(short.index("OESecondaryNasalization"),"OEEarlyOShortening")
orders={"identity":original,"n_loss_before_i":early,
        "n_loss_and_shortening_before_nasalization":short}
if payload.get("research_mode")=="following-high":
    high=list(original)
    high[high.index("EAFBrightening")]="AFHold"
    i=high.index("OESkPalatalization")
    high[i:i+1]=["AFHigh","AFSkL"]
    orders={"identity":original,"following_high_only":high}
    payload["probes"] += [
        {"id":name,"entry":form,"before":"OESkPalatalization",
         "status":"Attested structural control at palatalization, not a PGmc cell"}
        for name,form in [("control-wasce","*w*a*s*k*e"),
                          ("control-thersce","*θ*e*r*s*k*e"),
                          ("control-disces","*d*i*s*k*e*s"),
                          ("control-discas","*d*i*s*k*a*s")]]
hashes={k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()}
rows=payload["rows"]
result={"reference_sha":payload["reference_sha"],
        "execution":"Exact composition of frozen canonical stage relations, including raw tokenizer",
        "bin_hashes":hashes,"variants":{}}
def trace(order,forms):
    states=[[x] for x in forms];histories=[[] for x in forms]
    for stage in order:
        flat=[x for group in states for x in group]
        applied=iter(batch_apply_down(bins[stage],flat) if flat else [])
        next_states=[]
        for i,group in enumerate(states):
            output=sorted({x for _ in group for x in next(applied)})
            histories[i].append({"stage":stage,"before":group,"after":output})
            next_states.append(output)
        states=next_states
    return states,histories
baseline=None
for name,order in orders.items():
    finals,histories=trace(order,[r["fst_input"] for r in rows])
    assert all(len(x)==1 and x[0]!="+?" for x in finals),name
    if baseline is None:baseline=finals
    item={"order":order,"matched":sum(x==[r["counterpart"]] for r,x in zip(rows,finals)),
          "changed":[{"id":r["id"],"concept":r["concept"],"before":b,"after":f}
                     for r,b,f in zip(rows,baseline,finals) if b!=f],
          "rows":[{**r,"baseline":b,"output":f,"trace":h}
                  for r,b,f,h in zip(rows,baseline,finals,histories)],"probes":[]}
    for probe in payload["probes"]:
        p=dict(probe)
        if "raw" in p:
            f,h=trace(order,[p["raw"]]);p["raw_output"],p["raw_trace"]=f[0],h[0]
        boundary=p["before"] if p["before"] in order else "AFHigh"
        f,h=trace(order[order.index(boundary):],[p["entry"]])
        p["actual_before"]=boundary
        p["diagnostic_output"],p["diagnostic_trace"]=f[0],h[0]
        item["probes"].append(p)
    result["variants"][name]=item
    Path(sys.argv[3]).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(name,item["matched"],item["changed"],flush=True)
assert hashes=={k:hashlib.sha256(v.read_bytes()).hexdigest() for k,v in bins.items()}
'''

work = ROOT / ".capr-work/flask-research"
compiled = json.loads((work / "compile.json").read_text())
payload = json.loads((work / "payload.json").read_text())
high_mode = "--following-high" in sys.argv
payload_path = work / "payload.json"
if high_mode:
    payload["research_mode"] = "following-high"
    payload_path = work / "following-high-payload.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
order = list(payload["orders"]["identity"])
order.remove("PNWGmcNStemNLoss")
order.insert(order.index("PWGmcEarlyIApocope"), "PNWGmcNStemNLoss")
order.remove("OEEarlyOShortening")
order.insert(order.index("OESecondaryNasalization"), "OEEarlyOShortening")
variant = "n_loss_and_shortening"
if high_mode:
    order = list(payload["orders"]["identity"])
    order[order.index("EAFBrightening")] = "AFHold"
    i = order.index("OESkPalatalization")
    order[i:i + 1] = ["AFHigh", "AFSkL"]
    variant = "following_high_only"
snapshot = experiment_snapshot.create_snapshot(
    "flask-following-high-2805d98a-v1" if high_mode else "flask-shortening-order-2805d98a-v1",
    "Following-vowel-only high trigger; preceding-front clause preserved." if high_mode else
    "Test the specific secondary-n and late-created-a mechanism; no production adoption.",
    {"driver": Path(__file__).resolve(), "compiled": work / "compile.json",
     "payload": payload_path, "source": ROOT / "Germanic/fsts/germanic.txt"},
    variants={variant: " .o. ".join(order)},
    probes=payload["probes"], expected_outcomes={"measure_all": 394},
    negative_controls=["dōn", "all unchanged selected inputs and targets"])
container = snapshot.stage_in_container()
output = compiled["container_output"] + ("/following-high.json" if high_mode else "/shortening-order.json")
receipt = control.run_logged(
    ["docker", "compose", "exec", "-T", "backend", "python3", "-c", WORKER,
     json.dumps(compiled["bins"]), container + "/" + snapshot.input_path("payload").name, output],
    label="flask-shortening-order", log_dir=snapshot.staging_dir)
if not receipt["ok"]:
    raise RuntimeError(Path(receipt["stderr_log"]).read_text())
stdout = Path(receipt["stdout_log"]).read_text()
subprocess.run(["docker", "compose", "cp", "backend:" + output,
                str(snapshot.staging_dir / "observed.json")], check=True)
snapshot.complete("passed", "All actual deltas recorded, not silently accepted.", [receipt])
(work / ("following-high.json" if high_mode else "shortening-order.json")).write_text(
    (snapshot.results_dir / "observed.json").read_text())
print(stdout)
