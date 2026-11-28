"""Verify contiguous SC085 factoring formally and on immutable corpus traces."""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest


LOSS = "OEHLoss"
STRIP = "StStrip"
NEXT = "OEContraction"


class Handoff:
    RULES = ("StKeepH", STRIP)

    @staticmethod
    def definitions():
        return (
            "define StKeepH FootCtx([[{*x}|{*ç}] -> 0 || EnglishStarVocalic _ EnglishStarVocalic]);\n"
            "define StStrip [{*ᶠ} -> 0];\n"
        )


def prove(source, cache, directory):
    obligations = (
        ("domains", ("regex OEHLoss.u;", "regex StJoined.u;", "test equivalent"), 1),
        ("agreement", ("regex [OEHLoss|StJoined];", "test functional"), 1),
        ("domain-sentinel", ("regex [a:b].u;", "regex [b:c].u;", "test equivalent"), 0),
        ("agreement-sentinel", ("regex [a:b|a:c];", "test functional"), 0),
    )
    prefix = run.frozen.compiler.definition_image_source(
        source.read_text(encoding="utf-8"), Path(directory), cache / "defined.bin")
    if not prefix.startswith("load defined "):
        raise RuntimeError("Formal comparison requires the verified definition image")
    commands = [prefix, Handoff.definitions(),
                "define StJoined [StKeepH .o. StStrip];"]
    for _, steps, _ in obligations:
        commands += ["clear stack", *steps]
    script = Path(directory) / "handoff.foma"
    script.write_text("\n".join(commands + ["quit", ""]), encoding="utf-8")
    result = subprocess.run(["foma", "-f", str(script)], text=True, capture_output=True, check=True)
    output = result.stdout + result.stderr
    outcomes = [int(value) for value in re.findall(r"^([01]) \(1 = TRUE, 0 = FALSE\)", output, re.M)]
    if "error" in result.stderr.lower():
        raise RuntimeError(result.stderr)
    verify(outcomes, [expected for _, _, expected in obligations], f"formal Foma checks:\n{output}")
    return {"script": script.read_text(), "transcript": output,
            "outcomes": {label: value for (label, _, _), value in zip(obligations, outcomes)}}


def fused(trace):
    before, mid = trace["anchors"][LOSS]
    strip_in, after = trace["anchors"][STRIP]
    verify(strip_in, mid, "contiguity")
    changes = []
    for stage, forms in trace["changes"]:
        if stage == STRIP or stage == LOSS:
            if not changes or changes[-1][0] != LOSS:
                if before != after:
                    changes.append([LOSS, after])
        else:
            changes.append([stage, forms])
    return {**trace, "changes": changes, "anchors": {LOSS: [before, after], NEXT: trace["anchors"][NEXT]}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    baseline = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(digest(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    paths = run.cached_stages(args.stage_cache, source, definitions, orders)
    examples = {
        "clay-front": ("*θ*ō*x*æ", "*θ*ō*æ"),
        "strike-palatal": ("*s*l*e*ç*i*θ", "*s*l*e*i*θ"),
        "fringe-back": ("*w*l*ō*x*u*m", "*w*l*ō*u*m"),
        "behind-pretonic": ("*ᶠ*b*e*x*í*n*d*a*n", "*ᶠ*b*e*x*í*n*d*a*n"),
        "sieve-geminate": ("*s*í*x*x*a*n", "*s*í*x*x*a*n"),
        "catch-final": ("*f*ō*x", "*f*ō*x"),
        "prefixed-posthead": ("*ᶠ*ʝ*e*s*e*ç*i*θ", "*ᶠ*ʝ*e*s*e*i*θ"),
        "sentence-final": ("*ᵘ*ᶠ*ʝ*e*s*e*ç*i*θ", "*ᵘ*ᶠ*ʝ*e*s*e*i*θ"),
    }
    models = {}
    with tempfile.TemporaryDirectory(prefix="capr-sc085-proposal-") as directory:
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, Handoff, runtime)
        candidate = paths | build.verify()
        candidate[f"component:{LOSS}"] = candidate["component:StKeepH"]
        formal = prove(source, args.stage_cache, directory)
        for model, order in orders.items():
            rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in rows),
                   Counter(archived=394, active=396), f"{model} panel populations")
            inputs = {key: row["fst_input"] for key, row in rows.items()}
            order_split = run.overlay_order(order, ((NEXT, STRIP),))
            verify(order_split.index(STRIP), order_split.index(LOSS) + 1, "strip immediately after loss")
            before = run.evaluate(order, paths, inputs, {LOSS, NEXT})
            split = run.evaluate(order_split, candidate, inputs, {LOSS, STRIP, NEXT})
            verify({key: row["output"] for key, row in before.items()},
                   {key: row["output"] for key, row in rows.items()}, f"{model} archived endpoints")
            verify({key: fused(row) for key, row in split.items()}, before, f"{model} unchanged cascade")
            firings = {key: row["anchors"] | {"input": row["input"], "output": row["output"]}
                       for key, row in split.items()
                       if any(a != b for a, b in (row["anchors"][stage] for stage in (LOSS, STRIP)))}
            local = run.evaluate(order_split[order_split.index(LOSS):], candidate,
                                 {key: form for key, (form, _) in examples.items()}, {LOSS, STRIP, NEXT})
            for key, (_, expected) in examples.items():
                verify(local[key]["anchors"][LOSS][1], [expected], f"{model} {key}")
            compare = dict(local)
            for key in ("active:2302", "active:1944"):
                compare[key] = split[key]
            models[model] = {"panel_size": len(rows), "order": order_split, "firings": firings,
                             "regression": compare, "fused_trace_differences": 0}
        text = source.read_text(encoding="utf-8")
        incumbent = re.search(r"^define OEHLoss FootCtx\(\[.*?^]\) \.o\. \[\{\*ᶠ\} -> 0\];",
                              text, re.S | re.M).group()
        print(json.dumps({
            "base": run.BASE, "source_sha256": digest(source), "archive_sha256": digest(archive_path),
            "runner_sha256": digest(Path(__file__)), "incumbent": incumbent,
            "candidate": Handoff.definitions(), "formal": formal, "component": build.receipt(),
            "frozen_exports": {key: digest(path) for key, path in paths.items()}, "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
