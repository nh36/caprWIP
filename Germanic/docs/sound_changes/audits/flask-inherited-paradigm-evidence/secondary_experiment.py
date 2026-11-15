"""Immutable raw-input flask variants and independently labelled stage entries."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HEAD = "2805d98ae5ecf7df33c65dc0caf7d9df2ed22077"


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def host():
    root = Path.cwd()
    sys.path.insert(0, str(root / "Germanic/tools"))
    import experiment_snapshot
    import adjudication_control as control
    import oe_pipeline
    from anglo_frisian_experiments import corpus_rows
    from executable_facts import parse_defines

    work = Path(__file__).resolve().parent
    if "--secondary-n" in sys.argv:
        work /= "secondary-n"
        work.mkdir(exist_ok=True)
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip() == HEAD
    stages = oe_pipeline.stages()
    original = [s.inline_text if s.kind == "inline" else s.foma_identifier for s in stages]
    source = root / "Germanic/fsts/germanic.txt"
    facts = parse_defines(source.read_text())
    sk = facts["OESkPalatalization"].body
    following = "[\n    {*s} {*k} -> {*ʃ} || (EnglishStarConsonant | .#.) _ EnglishStarFrontVowel\n]"
    assert sk.count(following) == 1
    late = sk.replace(" .o. " + following, "", 1)
    assert late != sk and late.count("_ EnglishStarFrontVowel") == 0
    definitions = [
        "define AFSkF Ctx(" + following + ");",
        "define AFSkL " + late + ";",
        "define AFHold Ctx([[{*á} -> {*a} || _ {*s} {*k} {*ā} .#.] .o. EAFBrighteningStressed]);",
        "define AFRet FootCtx([{*æ} -> {*a} || _ {*s} {*k} {*ā} .#.]);",
        "define AFSt FootCtx([{*æ} -> {*a} || _ {*s} [{*k}|{*t}] {*ā} .#.]);",
        "define AFHigh " + sk.replace("EnglishStarFrontVowel", "[{*i}|{*í}|{*ì}|{*ī}|{*y}|{*ȳ}]") + ";",
        "define AFNUnr Ctx([{*ō} -> {*ā} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*n} .#.]);",
    ]
    orders = {"identity": original}
    for name in ["retain", "retract", "whole_sk_negative", "st_negative", "high_only_negative"]:
        order = list(original)
        if name in ["retain", "whole_sk_negative", "high_only_negative"]:
            order[order.index("EAFBrightening")] = "AFHold"
        if name in ["retract", "st_negative"]:
            order.insert(order.index("EAFBrighteningLongFinal"), "AFRet" if name == "retract" else "AFSt")
        if name == "whole_sk_negative":
            order.remove("OESkPalatalization")
            order.insert(order.index("EAFBrighteningLongFinal"), "OESkPalatalization")
        elif name == "high_only_negative":
            order[order.index("OESkPalatalization")] = "AFHigh"
        else:
            order[order.index("OESkPalatalization")] = "AFSkL"
            order.insert(order.index("EAFBrighteningLongFinal"), "AFSkF")
        orders[name] = order
    secondary = "--secondary-n" in sys.argv
    if secondary:
        early = list(original)
        early.remove("PNWGmcNStemNLoss")
        early.insert(early.index("PWGmcEarlyIApocope"), "PNWGmcNStemNLoss")
        unrounded = list(early)
        unrounded.insert(unrounded.index("PWGmcSurvivingBimoricOUnrounding"), "AFNUnr")
        orders = {"identity": original, "n_loss_before_i": early,
                  "n_loss_before_i_and_unrounding": unrounded}
    roots = {}
    for number, (name, order) in enumerate(orders.items()):
        roots[name] = "AFV" + str(number)
        definitions.append("define " + roots[name] + " " + " .o. ".join(order) + ";")
    recipe = {
        "id": "flask-raw-variants", "insert_rule": None, "insert_after": None,
        "replace": {}, "definitions": "\n".join(definitions),
        "component_checks": [{"component": s} for s in dict.fromkeys(
            [s for order in orders.values() for s in order] + list(roots.values()))],
    }
    probes = []
    for stem in ["flásk", "túng", "ásk"]:
        for cell, ending in [("nompl_gen", "ōniz"), ("accsg", "ōnų"),
                             ("datsg", "ōni"), ("datpl", "ōmaz")]:
            probes.append({"id": stem + "-" + cell, "raw": stem + ending,
                           "entry": "*" + "*".join(stem + ending),
                           "before": "PGmcGmSimplification",
                           "status": "CAPR application of Ringe2017 pp312–313 generic feminine paradigm"})
        probes.append({"id": stem + "-secondary-n", "entry": "*" + "*".join(stem + "ōn"),
                       "before": "EAFNasalSpirantLengthening",
                       "status": "Post-apocope diagnostic immediately after SC023, not ordinary raw entry"})
    for raw in ["námô", "náminiz", "námini", "námaniz", "dōną",
                "wáskō", "þérskō", "wáskô", "þérskô", "dískiz", "dískas"]:
        probes.append({"id": raw, "raw": raw, "entry": "*" + "*".join(raw),
                       "before": "PGmcGmSimplification",
                       "status": "Quantity/cell hypothesis; historical input must be verified independently"})
    probes.extend([
        {"id": "do-secondary-n", "entry": "*d*ō*n", "before": "EAFNasalSpirantLengthening",
         "status": "Negative control for secondary n survival"},
        {"id": "clay", "entry": "*θ*á*n*x*ō*n", "before": "PGmcNasalLossBeforeX",
         "status": "Documented glossary witness entry after tokenization"},
        {"id": "fringe", "entry": "*w*l*ō*x*u*m", "before": "OEHLoss",
         "status": "Normalized attested dative plural; h represented x"},
    ])
    payload = {"reference_sha": HEAD, "orders": orders, "roots": roots,
               "rows": corpus_rows(root / "Germanic/data/germanic-aligned-final.tsv"),
               "probes": probes}
    dump(work / "payload.json", payload)
    dump(work / "recipe.json", recipe)
    snapshot = experiment_snapshot.create_snapshot(
        "flask-secondary-n-2805d98a-v1" if secondary else "flask-raw-2805d98a-v2",
        "Raw-input variants and inherited-cell diagnostics; no production adoption.",
        {"source": source, "corpus": root / "Germanic/data/germanic-aligned-final.tsv",
         "contexts": root / "Germanic/data/entry_context_metadata.tsv",
         "payload": work / "payload.json", "recipe": work / "recipe.json",
         "driver": Path(__file__).resolve(), "pipeline": root / "Germanic/tools/oe_pipeline.py",
         "compiler": root / "Germanic/tools/anglo_frisian_experiments.py"},
        variants={k: " .o. ".join(v) for k, v in orders.items()},
        probes=probes, expected_outcomes={"identity_matches": 385, "accepted": 394},
        negative_controls=["whole sk movement: wascan", "st retraction: ræste",
                           "high-only trigger: wasċe, þersċe", "secondary n: dōn"])
    dump(work / "snapshot.json", {"root": str(snapshot.root)})
    compiled = snapshot.compile_isolated("source", "recipe", components_only=True)
    dump(work / "compile.json", compiled)
    args = [compiled["container_source"] + "/" + snapshot.input_path(k).name
            for k in ["driver", "payload"]]
    output = compiled["container_output"] + "/observed.json"
    receipt = control.run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-u",
         *args, json.dumps(compiled["bins"]), output],
        label="flask-2805-raw-assay", log_dir=snapshot.staging_dir)
    dump(work / "assay-receipt.json", receipt)
    if not receipt["ok"]:
        print(Path(receipt["stderr_log"]).read_text())
        raise SystemExit(receipt["returncode"])
    subprocess.run(["docker", "compose", "cp", "backend:" + output,
                    str(snapshot.staging_dir / "observed.json")], check=True)
    dump(snapshot.staging_dir / "compile.json", compiled)
    stdout = Path(receipt["stdout_log"]).read_text()
    snapshot.complete("passed", "Actual results measured; hypotheses adjudicated separately.",
                      [compiled["receipt"], receipt])
    dump(work / "observed.json", json.loads((snapshot.results_dir / "observed.json").read_text()))
    print(stdout)


def worker(payload_path, bins_json, output):
    sys.path.insert(0, "/usr/app/tools")
    from sound_change_order_sensitivity import batch_apply_down
    payload = json.loads(payload_path.read_text())
    bins = {k.removeprefix("component:"): Path(v) for k, v in json.loads(bins_json).items()}
    protected = [Path("/usr/app/fsts/germanic.txt"), Path("/usr/app/data/germanic-aligned-final.tsv")]
    protected += list(Path("/usr/app/docs/sound_changes/cascade_baseline").glob("*"))
    before = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected if p.is_file()}
    rows = payload["rows"]
    forms = [r["fst_input"] for r in rows]
    baseline = batch_apply_down(bins[payload["roots"]["identity"]], forms)
    assert len(rows) == 394 and all(len(v) == 1 and v[0] != "+?" for v in baseline)
    assert sum(v == [r["counterpart"]] for r, v in zip(rows, baseline)) == 385
    result = {"reference_sha": HEAD, "protected_before": before, "variants": {}}

    def trace(order, values):
        state = [[v] for v in values]
        history = [[] for _ in values]
        for stage in order:
            flattened = [v for alternatives in state for v in alternatives]
            applied = iter(batch_apply_down(bins[stage], flattened) if flattened else [])
            next_state = []
            for i, alternatives in enumerate(state):
                current = sorted({v for _ in alternatives for v in next(applied)})
                history[i].append({"stage": stage, "before": alternatives, "after": current})
                next_state.append(current)
            state = next_state
        return state, history

    # The inherited nominative plural is the first noncorpus ordinary-input probe.
    first = batch_apply_down(bins[payload["roots"]["identity"]], ["fláskōniz"])[0]
    result["first_nompl_raw"] = first
    print("FIRST ordinary fláskōniz", first, flush=True)
    for name, order in payload["orders"].items():
        finals = batch_apply_down(bins[payload["roots"][name]], forms)
        traced, histories = trace(order, forms)
        assert finals == traced, (name, "full-composition/component disagreement")
        assert all(len(v) == 1 and v[0] != "+?" for v in finals), (name, "corpus ambiguity/rejection")
        record = {"order": order,
                  "matched": sum(v == [r["counterpart"]] for r, v in zip(rows, finals)),
                  "rows": [{**r, "baseline": b, "output": f, "trace": h}
                           for r, b, f, h in zip(rows, baseline, finals, histories)],
                  "changed": [{"id": r["id"], "concept": r["concept"], "before": b, "after": f}
                              for r, b, f in zip(rows, baseline, finals) if b != f],
                  "probes": []}
        for probe in payload["probes"]:
            p = dict(probe)
            if "raw" in p:
                values, history = trace(order, [p["raw"]])
                actual = batch_apply_down(bins[payload["roots"][name]], [p["raw"]])[0]
                assert values[0] == actual
                p["raw_output"], p["raw_trace"] = actual, history[0]
            boundary = order.index(p["before"])
            values, history = trace(order[boundary:], [p["entry"]])
            p["diagnostic_output"], p["diagnostic_trace"] = values[0], history[0]
            if p["id"] == "fringe":
                assert next(x["after"] for x in history[0] if x["stage"] == "OEHLoss") == ["*w*l*ō*u*m"]
            record["probes"].append(p)
        result["variants"][name] = record
        dump(output, result)
        print(name, record["matched"], record["changed"], flush=True)
    after = {p: hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in before}
    assert before == after, "production source/corpus/baseline changed during isolated experiment"
    result["protected_after"] = after
    dump(output, result)


if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1:] == ["--secondary-n"]:
        host()
    else:
        worker(Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]))
