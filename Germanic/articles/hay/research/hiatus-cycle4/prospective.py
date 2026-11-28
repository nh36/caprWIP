"""Replay a pinned prospective family without modifying production Foma or targets."""

import argparse
from collections import Counter
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from time import perf_counter

from component_check import ComponentBuild, SNAPSHOT, run, verify
from components import digest
from stress_handoff import Stress

sys.path.insert(0, str(SNAPSHOT / "Germanic/articles/hay/research/hiatus-cycle3"))

from audit import audit_delta, corpus_run, FREEZE_SHA
from matched import trial
from panel import inventory
from quantity_check import ENTRIES as LONG
from reproduce_stress import DELETION
from revised import Components, EDGE, HOLDOUT_SHA, WIDE, batches
from source_entry_check import ENTRIES, LATER_ENTRIES
from sources import AFTER_H, BACK, CLUSTER, H


PANEL_SHA = {
    "validation-h-loss-v1.tsv": "afea0d656f99928606faa23e4e8fe90ccae52c988cb4e07adf46ad0873e1831f",
    "validation-nuclei-v1.tsv": "cbc7cef8abbfcb428df146c93d273f2c01911c3e6d288732257eba3964f958ba",
}
GROUPS = {
    "back": ((BACK, "BkWL"), (BACK, "BkNu")),
    "hw": ((CLUSTER, "HwMed"),),
    "h": tuple((AFTER_H, name) for name in ("HLBroken", "HbFront", "HbIden")),
}
HANDOFF = ((AFTER_H, "StStrip"),)
FRINGE_SENSITIVITY = ((AFTER_H, "HbOU"),)
REUSED = {"high-weak-oblique", "pupil-acc"}


class Shared:
    RULES = tuple(name for group in (*GROUPS.values(), FRINGE_SENSITIVITY) for _, name in group)

    @staticmethod
    def definitions():
        return Components.definitions()


class StressHandoff:
    RULES = ("StFoot", "StKeepH", "StStrip")

    @staticmethod
    def definitions():
        return Stress.definitions()


class Mechanisms:
    RULES = tuple(sorted({name for group in (*WIDE.values(), *EDGE.values()) for name in group}))

    @staticmethod
    def definitions():
        return Components.definitions()


def plans(order):
    p2 = sum(GROUPS.values(), ())

    def sort(placements):
        return tuple(sorted(placements, key=lambda pair: (order.index(pair[0]), pair[1] == "StStrip")))

    yield "P0", False, ()
    yield "P1", True, HANDOFF
    for label, group in GROUPS.items():
        yield f"P1+{label}", True, sort(group + HANDOFF)
        yield f"P2-without-{label}", True, sort(tuple(pair for pair in p2 if pair not in group) + HANDOFF)
    yield "P2", True, sort(p2 + HANDOFF)
    yield "P2+fringe-sensitivity", True, sort(p2 + FRINGE_SENSITIVITY + HANDOFF)
    for letter, steps in WIDE.items():
        late = tuple((AFTER_H, step) for step in steps)
        yield f"P3-{letter}", True, sort(p2 + late + HANDOFF)
    for letter, steps in EDGE.items():
        yield f"edge-{letter}", True, sort(p2 + tuple((AFTER_H, step) for step in steps) + HANDOFF)


def research_entries(order, catalogue, legacy):
    seen = {key for forms in legacy.values() for key in forms}
    for prefix, rows in (("source-audit", ENTRIES), ("back-h-audit", LATER_ENTRIES), ("long-audit", LONG)):
        for anchor, forms in rows.items():
            legacy.setdefault(anchor, {}).update({f"{prefix}:{key}": val for key, val in forms.items()})
    for row in catalogue:
        key = "new:" + row["id"]
        if key in seen:
            raise RuntimeError(f"Duplicate trace identity: {key}")
        seen.add(key)
        if row["anchor"] == "@observe":
            continue
        anchor = order[0] if row["anchor"] == "@proto" else row["anchor"]
        legacy.setdefault(anchor, {})[key] = row["executable_input"]
    return legacy


def panel_summary(catalogue, traces):
    records = {}
    for row in catalogue:
        key = row["id"]
        trace = traces.get("new:" + key)
        population = ("previously-used-structure" if key in REUSED
                      else row.get("population") or "validation")
        # Spelling comparison is an aid to review, not a historically adjudicated score.
        output = trace["output"] if trace else []
        status = ("observation" if trace is None else "no-output" if not output else
                  "first-reported-form" if row["reported_form"].split(";")[0] in output else "other")
        records[key] = {"population": population, "grade": row["grade"],
                        "output": output, "comparison": status}
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    canonical, alternatives, definitions = run.frozen.model_sources(source)
    baseline = json.loads((run.HERE / "baseline.json").read_text())
    verify(digest(source), baseline["source_sha256"], "frozen source")
    orders = {"canonical": canonical, **alternatives}
    verify(orders, baseline["orders"], "frozen orders")
    frozen = run.cached_stages(args.stage_cache, source, definitions, orders)
    archive_path = run.HERE / "joint-corpus.json"
    archive = json.loads(archive_path.read_text())
    root = args.snapshot / "Germanic/articles/hay/research"
    old = root / "hiatus-cycle2/benchmark.tsv"
    holdout = root / "hiatus-cycle3/holdouts-v1.tsv"
    verify(digest(old), FREEZE_SHA, "prior benchmark")
    verify(digest(holdout), HOLDOUT_SHA, "prior holdout")
    inherited, extension = inventory()
    catalogue = []
    for name, expected in PANEL_SHA.items():
        file = Path(__file__).with_name(name)
        verify(digest(file), expected, name)
        catalogue.extend(run.dsv(file))
    verify(len({row["id"] for row in catalogue}), 42, "frozen records")
    models, builds, timing = {}, {}, {}
    with tempfile.TemporaryDirectory(prefix="hay4-prospective-") as directory:
        for label, family in (("shared", Shared), ("handoff", StressHandoff), ("mechanisms", Mechanisms)):
            start = perf_counter()
            builds[label] = ComponentBuild(run.compile_candidates, source, args.stage_cache,
                                           directory, family, runtime)
            timing[label] = round(perf_counter() - start, 3)
        paths = frozen | builds["shared"].verify() | builds["handoff"].verify() | builds["mechanisms"].verify()
        repaired = paths | {f"component:{DELETION}": paths["component:StFoot"],
                            f"component:{H}": paths["component:StKeepH"]}
        for model, order in orders.items():
            archive_rows = archive["models"][model]["baseline"]
            verify(Counter(key.split(":")[0] for key in archive_rows),
                   Counter({"archived": 394, "active": 396}), f"{model} archive")
            inputs = {key: row["fst_input"] for key, row in archive_rows.items()}
            legacy, untraced = batches(order, inherited, extension, archive_rows, run.dsv(old), run.dsv(holdout))
            entries = research_entries(order, catalogue, legacy)
            report = {"legacy_observations": untraced, "arms": {}}
            control = shared = None
            for label, is_repaired, placements in plans(order):
                start = perf_counter()
                substrate = repaired if is_repaired else frozen
                wide = corpus_run(order, substrate, inputs, placements)
                historical = trial(order, substrate, entries, placements)
                elapsed = round(perf_counter() - start, 3)
                if label == "P0":
                    control = wide
                    verify({key: record["output"] for key, record in control.items()},
                           {key: row["output"] for key, row in archive_rows.items()}, f"{model} P0")
                if label == "P2":
                    shared = wide
                arm = {"placements": placements, "wall_seconds": elapsed,
                       "wide": audit_delta(wide, control), "historical": historical,
                       "new": panel_summary(catalogue, historical)}
                if shared is not None and label != "P2":
                    arm["vs_P2"] = audit_delta(wide, shared)
                report["arms"][label] = arm
            report["P0-wide"] = control
            models[model] = report
        print(json.dumps({
            "base": run.BASE, "orders": orders, "source_sha256": digest(source),
            "archive_sha256": digest(archive_path), "prior_panel_sha256": [digest(old), digest(holdout)],
            "new_panel_sha256": PANEL_SHA, "runner_sha256": digest(Path(__file__)),
            "frozen_component_hashes": {key: digest(value) for key, value in frozen.items()},
            "components": {label: item.receipt() for label, item in builds.items()},
            "definitions": {label: family.definitions() for label, family in
                            (("shared", Shared), ("handoff", StressHandoff), ("mechanisms", Mechanisms))},
            "compile_seconds": timing, "models": models,
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
