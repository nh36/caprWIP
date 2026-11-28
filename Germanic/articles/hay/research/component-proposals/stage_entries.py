"""Audit frozen alphabet consumers and exercise explicitly graded later entries."""

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
import tempfile

from component_check import ComponentBuild, run, verify
from components import digest
from nucleus_check import PRIVATE, family


@dataclass(frozen=True)
class Entry:
    kind: str
    stage: str
    source: str
    form: str = ""

    def path(self, order):
        if not self.source:
            raise ValueError("An entry requires an evidence statement")
        if self.kind == "observation" and not self.form and not self.stage:
            return ()
        if not self.form:
            raise ValueError("Executable entry has no input")
        if self.kind == "full" and self.stage == "@proto" and "*" not in self.form:
            return tuple(order)
        if self.kind == "local" and self.form.startswith("*"):
            if self.stage == "research-pre-HVD":
                return ("NxGate", "NxHvd")
            if self.stage == "pre-h-loss" and not set(self.form.split("*")) & set(PRIVATE):
                return tuple(order[order.index("OEHLoss"):])
        raise ValueError(f"{self.kind}: input is incompatible with {self.stage}")


ENTRIES = {
    "native-control": Entry("full", "@proto", "Synthetic native-admission control", "tédiz"),
    "clay-exact": Entry("local", "pre-h-loss", "Ringe and Taylor 314; Epinal Glossary 3",
                        "*θ*ō*x*æ"),
    "marked-light": Entry("local", "research-pre-HVD", "Synthetic light-nucleus assay", "*t*éi*d*i"),
    "marked-heavy": Entry("local", "research-pre-HVD", "Synthetic heavy-nucleus assay", "*t*ḗi*d*i"),
    "unknown": Entry("local", "research-pre-HVD", "Deliberately invalid symbol", "*t*λ*d*i"),
    "flame": Entry("observation", "", "Sweet 1885: 222, 307, 341; no historical input selected"),
}
INVALID = (
    Entry("full", "@proto", "Synthetic wrong input tier", "*t*ēi*d*i"),
    Entry("local", "pre-h-loss", "Synthetic unsupported type", "*t*ēi*d*i"),
    Entry("local", "sc999", "No approved entry site", "*t*e*i"),
    Entry("observation", "", "Must not be executed", "*t*e*i"),
    Entry("local", "pre-h-loss", "", "*t*e*i"),
)
PROBES = {
    "hiatus": "*t*e*i*d*i", "long-hiatus": "*t*ē*i*d*i",
    "light": "*t*ėi*d*i", "light-acute": "*t*éi*d*i",
    "heavy": "*t*ēi*d*i", "heavy-acute": "*t*ḗi*d*i",
    "inherited-ei": "*t*ei*d*i", "approximant": "*t*e*j*d*i",
    "fricative": "*t*e*ʝ*d*i", "secondary-acute": "*t*á*k*è*d*i",
    "secondary-ordinary": "*t*á*k*e*d*i", "foot": "*ᶠ*ʝ*e*k*e*d*i",
    "io": "*l*īo*d", "eo": "*l*ēo*d", "iu": "*l*iu*d",
}


def audit(order, paths):
    states = {name: [form] for name, form in PROBES.items()}
    records = {}
    for stage in order[order.index("OEStressFootContext"):]:
        after = run.frozen.apply_stage(paths[f"component:{stage}"], states)
        records[stage] = {
            "rejected": [key for key, result in after.items() if not result],
            "rewritten": {key: result for key, result in after.items()
                          if result and result != states[key]},
        }
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    baseline = json.loads((run.HERE / "baseline.json").read_text(encoding="utf-8"))
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    orders = {"canonical": canonical, **alternatives}
    verify(digest(source), baseline["source_sha256"], "frozen source")
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    models = {}
    with tempfile.TemporaryDirectory(prefix="capr-entry-") as directory:
        recipe = family(source)
        build = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                               directory, recipe, runtime)
        paths = frozen | build.verify()
        for model, order in orders.items():
            for entry in INVALID:
                try:
                    entry.path(order)
                except ValueError:
                    continue
                raise AssertionError(f"Incorrect admission: {entry}")
            traces = {}
            for name, entry in ENTRIES.items():
                route = entry.path(order)
                traces[name] = (run.evaluate(route, paths, {name: entry.form}, set(route))[name]
                                if route else None)
            for key, result in {"clay-exact": ["þōæ"], "marked-light": ["*t*éi*d*i"],
                                "marked-heavy": ["*t*ḗi*d"], "unknown": []}.items():
                verify(traces[key]["output"], result, f"{model} {key}")
            census = audit(order, frozen)
            for key in ("light", "light-acute", "heavy", "heavy-acute"):
                assert key in census["OEHighVowelApocope"]["rejected"], (model, key)
            models[model] = {"entries": traces, "independent_stage_audit": census}
        print(json.dumps({
            "base": run.BASE, "orders": orders, "source_sha256": digest(source),
            "runner_sha256": digest(Path(__file__)), "build": build.receipt(),
            "definitions": recipe.definitions(),
            "frozen_exports": {key: digest(value) for key, value in frozen.items()},
            "entries": {key: vars(entry) for key, entry in ENTRIES.items()},
            "refused": [vars(entry) for entry in INVALID], "probes": PROBES, "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
