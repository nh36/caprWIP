#!/usr/bin/env python3
"""Live domain assay; artificial contrasts are not historical attestations."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools"))
from anglo_frisian_experiments import compile_isolated
from capr_runtime import layout

previous = Path(__file__).parent.parent / "sc035-prosody/experiment.py"
spec = importlib.util.spec_from_file_location("sc035_prosody_helpers", previous)
prosody = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prosody)
apply = prosody.historical.checked_apply


def cases():
    groups = {}
    annotation = []
    for onset in ("", "*b", "*b*l", "*ʝ"):
        for weak in ("a", "e", "i", "o", "u", "æ"):
            for bridge in ("*t", "*s*t", "*l*n"):
                for head in ("á", "ḯ", "ḗ", "áu"):
                    form = onset + "*" + weak + bridge + "*" + head
                    annotation.append((form, "*ᶠ" + form))
    for form in (
        "*ʝ*æ*t", "*ʝ*æ*t*ā", "*ʝ*æ*t*à", "*ʝ*ǣ*t*á",
        "*ʝ*ā*t*á", "*ʝ*æ*á", "*ʝ*æ*t*e*t*á",
        "*b*á*ʝ*æ*t*á", "*ʝ*æ*t*ā*t*á", "*ʝ*æ*t*à*t*á",
    ):
        annotation.append((form, form))
    for context in ("*ᵘ", "*ᶜ"):
        annotation.append((context + "*ʝ*æ*t*á", context + "*ᶠ*ʝ*æ*t*á"))
    groups["annotation"] = ("OEStressFootContext", annotation)

    raising = []
    for onset in ("*ʝ", "*b*ʝ", "*s*t*ʝ"):
        for tail in ("*t*á", "*s*t*ḯ", "*l*ēa*β*j*ą*n"):
            form = "*ᶠ" + onset + "*æ" + tail
            raising.append((form, form.replace("*æ", "*i", 1)))
    for trigger in ("b", "g", "ɣ", "j", "ʃ", "ʧ", "ʤ"):
        form = "*ᶠ*" + trigger + "*æ*t*á"
        raising.append((form, form))
    for vowel in ("a", "e", "i", "ǣ", "ā", "á", "é"):
        form = "*ᶠ*ʝ*" + vowel + "*t*á"
        raising.append((form, form))
    for form in ("*ʝ*æ*t*á", "*ᶠ*b*æ*ʝ*æ*t*á", "*b*á*ʝ*æ*t"):
        raising.append((form, form))
    for context in ("*ᵘ", "*ᶜ"):
        raising.append((context + "*ᶠ*ʝ*æ*t*á", context + "*ᶠ*ʝ*i*t*á"))
    groups["raising"] = ("OEPrefixAReduction", raising)

    groups["diphthongization"] = ("OEWsPalatalDiphthongization", [
        ("*ᶠ*ʝ*æ*ʃ*æ*f*t", "*ᶠ*ʝ*æ*ʃ*ea*f*t"),
        ("*ᶠ*b*æ*ʝ*æ*t", "*ᶠ*b*æ*ʝ*ea*t"),
        ("*ʝ*æ*t", "*ʝ*ea*t"),
        ("*ʝ*é*β*a*n", "*ʝ*íe*β*a*n"),
    ])
    groups["ae_merger"] = ("OEUnstressedAEMerger", [
        ("*ᶠ*ʝ*æ*t*á", "*ᶠ*ʝ*e*t*á"),
        ("*ᶠ*b*æ*t*á", "*ᶠ*b*e*t*á"),
        ("*ʝ*æ*t", "*ʝ*æ*t"),
        ("*ᶠ*ʝ*ǣ*t*á", "*ᶠ*ʝ*ǣ*t*á"),
        ("*ᶠ*ʝ*i*t*á", "*ᶠ*ʝ*i*t*á"),
    ])
    groups["i_lowering"] = ("OEPrefixIReduction", [
        ("*ᶠ*ʝ*i*s*t*ḯ*g*a", "*ʝ*e*s*t*ḯ*g*a"),
        ("*ᶠ*b*i*g*í*n*n*a*n", "*b*e*g*í*n*n*a*n"),
        ("*ᶠ*ʝ*i*d*y*r*s*t*i*ʝ", "*ʝ*e*d*y*r*s*t*i*ʝ"),
        ("*ᶠ*ʝ*i*b*ēa*t*æ*n", "*ʝ*e*b*ēa*t*æ*n"),
        ("*ᶠ*n*i*t*á", "*n*e*t*á"),
        ("*b*í*n*d*a*n", "*b*í*n*d*a*n"),
        ("*n*i", "*n*i"),
        ("*ᶠ*ʝ*ī*t*á", "*ʝ*ī*t*á"),
    ])
    return groups


def run():
    runtime = layout()
    if not runtime.is_container:
        raise RuntimeError("run in the backend container; host Foma is prohibited")
    groups = cases()
    recipe = {
        "definitions": "", "insert_after": "", "insert_rule": "", "replace": {},
        "component_checks": [{"component": identifier}
                             for identifier, _ in groups.values()],
    }
    results = {}
    with tempfile.TemporaryDirectory(prefix="capr_sc035_generality_") as temporary:
        bins = compile_isolated(runtime.germanic_fst, recipe, [], Path(temporary),
                                components_only=True)
        for name, (identifier, pairs) in groups.items():
            inputs, expected = zip(*pairs)
            outputs = apply(bins["component:" + identifier], list(inputs), name)
            failures = [(form, want, got)
                        for form, want, got in zip(inputs, expected, outputs)
                        if got != [want]]
            if failures:
                raise RuntimeError(f"{name}: unexpected domain behavior: {failures}")
            results[name] = [
                {"input": form, "output": output[0]}
                for form, output in zip(inputs, outputs)
            ]
    return {
        "accepted_base_commit": "c1b573078c521121dde670e735f3907e7494cb16",
        "source_sha256": hashlib.sha256(runtime.germanic_fst.read_bytes()).hexdigest(),
        "interpretation": (
            "Artificial domain controls except the explicitly normalized "
            "post-raising lowering comparisons; no new PGmc inputs or attestations."
        ),
        "controls": results,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
