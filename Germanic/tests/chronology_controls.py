"""Live current-model chronology controls; no scientific expectations."""
from collections import Counter
import json
from pathlib import Path
import subprocess
import tempfile
import time
from unittest.mock import patch

from anglo_frisian_experiments import foma_domain

def remainder_plans(variants):
    baseline = variants["current_identity"]
    original = [s.foma_identifier if s.kind == "named" else s.inline_text
                for s in baseline]
    plans = {}
    for name, sequence in variants.items():
        members = [s.foma_identifier if s.kind == "named" else s.inline_text
                   for s in sequence]
        if not members:
            raise ValueError("empty executable chronology sequence")
        if members == original:
            plans[name] = {"mode": "production"}
            continue
        common = 0
        for left, right in zip(original, members):
            if left != right:
                break
            common += 1
        checkpoints = [i for i in range(common)
                       if baseline[i].kind == "named"
                       and original.count(baseline[i].foma_identifier) == 1]
        if not checkpoints or checkpoints[-1] + 1 == len(members):
            plans[name] = {"mode": "full", "members": members,
                           "reason": "no unique common checkpoint with a nonempty remainder"}
            continue
        index = checkpoints[-1]
        plans[name] = {
            "mode": "remainder", "checkpoint": baseline[index].foma_identifier,
            "snapshot": baseline[index].snapshot_bin,
            "members": members[index + 1:], "full_members": members,
        }
    return plans


def prefix_outputs(binary, form):
    """Unlike the final evaluator, retain epsilon for full-composition fallback."""
    proc = subprocess.run(["flookup", "-i", str(binary)], input=(form + "\n").encode(),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    outputs = []
    seen = False
    for line in proc.stdout.decode().splitlines():
        if not line:
            continue
        head, separator, output = line.partition("\t")
        if not separator or head != form:
            raise RuntimeError("unrecognized cumulative-prefix lookup output")
        seen = True
        if output != "+?" and output not in outputs:
            outputs.append(output)
    if not seen:
        raise RuntimeError("missing cumulative-prefix lookup output")
    return outputs


def effective_plan(plan, states):
    if plan["mode"] == "remainder" and any("" in values for values in states.values()):
        return {"mode": "full", "members": plan["full_members"],
                "reason": "epsilon intermediate requires complete composition"}
    return plan


def continue_outputs(states, lookup):
    if "" in states:
        raise ValueError("epsilon intermediate requires complete composition")
    outputs = []
    for state in states:
        for output in lookup(state):
            if output not in outputs:
                outputs.append(output)
    return outputs


def run_controls(payload, profile):
    from anglo_frisian_experiments import _compile_foma, definition_image_source
    from capr_runtime import check_build_manifest, layout
    from oe_pipeline import apply_down, evaluation_input, expected_snapshot_bins

    profile["phase"] = "validate canonical bins"
    problems = check_build_manifest(expected_snapshot_bins() + ["old_english.bin"])
    if problems:
        raise RuntimeError("canonical chronology bins are not fresh: " + "; ".join(problems))
    rt = layout()
    rows = payload["rows"]
    inputs = {row["concept"]: evaluation_input(row) for row in rows}
    result, states, plans, domains, appendix = {}, {}, {}, {}, ""
    profile["phase"] = "production and cumulative-prefix lookups"
    for name, planned in payload["plans"].items():
        if planned["mode"] == "production":
            result[name] = {concept: apply_down(rt.bin_dir / "old_english.bin", form)
                            for concept, form in inputs.items()}
            continue
        if planned["mode"] not in {"remainder", "full"}:
            raise ValueError("unknown chronology execution mode")
        states[name] = {}
        if planned["mode"] == "remainder":
            states[name] = {
                concept: prefix_outputs(rt.bin_dir / planned["snapshot"], form)
                for concept, form in inputs.items()}
        plan = effective_plan(planned, states[name])
        plans[name] = plan
        identifier = "Chronology" + str(len(plans))
        expression = " .o. ".join(plan["members"])
        if plan["mode"] == "remainder":
            domains[name] = sorted({form for values in states[name].values() for form in values})
            expression = foma_domain(domains[name]) + " .o. " + expression
        appendix += (f"\ndefine {identifier} " + expression +
                     f";\nclear stack\nregex {identifier};\nsave stack {name}.bin\n")
    with tempfile.TemporaryDirectory(prefix="capr_chronology_remainders_") as temporary:
        root = Path(temporary)
        if plans:
            profile["phase"] = "definition image validation"
            definitions = definition_image_source(rt.germanic_fst.read_text(), root)
            profile["shared_definitions"] = definitions.startswith("load defined ")
            script = root / "remainders.foma"
            script.write_text(definitions + appendix + "\nquit\n")
            profile["phase"] = "remainder/full-fallback compilation"
            _compile_foma(script, root)
        profile["phase"] = "remainder/full-fallback lookups"
        for name, plan in plans.items():
            binary = root / (name + ".bin")
            if not binary.is_file() or not binary.stat().st_size:
                raise RuntimeError(name + ": missing chronology network")
            result[name] = {
                concept: (
                    apply_down(binary, form) if plan["mode"] == "full" else
                    continue_outputs(states[name][concept],
                                     lambda state: apply_down(binary, state)))
                for concept, form in inputs.items()}
    profile.update({
        "inputs": inputs, "prefix_states": states, "plans": payload["plans"],
        "effective_plans": plans, "finite_domains": domains,
        "complete_roots": sum(p["mode"] == "full" for p in plans.values()),
        "remainders": sum(p["mode"] == "remainder" for p in plans.values()),
    })
    return result


def main(payload):
    profile = {"subprocesses": []}
    original_run = subprocess.run

    def measured(argv, *args, **kwargs):
        started = time.perf_counter()
        result = original_run(argv, *args, **kwargs)
        profile["subprocesses"].append({
            "command": Path(argv[0]).name, "phase": profile["phase"],
            "compilation": Path(argv[0]).name == "foma" and "-f" in argv,
            "seconds": time.perf_counter() - started, "returncode": result.returncode})
        return result

    started = time.perf_counter()
    with patch.object(subprocess, "run", side_effect=measured):
        outputs = run_controls(payload, profile)
    profile["seconds"] = time.perf_counter() - started
    profile["subprocess_counts"] = dict(Counter(p["command"] for p in profile["subprocesses"]))
    profile["compiler_calls"] = sum(p["compilation"] for p in profile["subprocesses"])
    print(json.dumps({"outputs": outputs, "execution": profile}, ensure_ascii=False))


if __name__ == "__main__":
    main(PAYLOAD)
