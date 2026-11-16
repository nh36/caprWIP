"""Execution-plan and relational-composition controls, not historical claims."""
import json
from pathlib import Path
import subprocess

import pytest

import chronology_controls as controls
import oe_pipeline
from capr_runtime import run_in_runner
from test_chronology_consistency import _current_variants


def stage(name, index=1):
    return oe_pipeline.Stage(index, name, "test", "named")


def test_boundaries_follow_executable_sequences_and_preserve_inline_members():
    a, b, c, d = [stage(name) for name in "ABCD"]
    inline = oe_pipeline.Stage(2, "", "test", "inline", inline_text="[a:b]")
    plans = controls.remainder_plans({
        "current_identity": [a, inline, b, c], "changed": [a, inline, d, c],
        "identical": [a, inline, b, c], "shortened": [a], "no_prefix": [d, c],
    })
    assert plans["changed"]["checkpoint"] == "A"
    assert plans["changed"]["members"] == ["[a:b]", "D", "C"]
    assert plans["identical"] == {"mode": "production"}
    assert plans["shortened"]["mode"] == plans["no_prefix"]["mode"] == "full"
    assert plans["shortened"]["members"] == ["A"]
    duplicate = controls.remainder_plans({
        "current_identity": [a, a, b], "changed": [a, a, c]})
    assert duplicate["changed"]["mode"] == "full"
    with pytest.raises(ValueError, match="empty executable"):
        controls.remainder_plans({"current_identity": [a], "changed": []})


def test_current_boundaries_are_derived_without_losing_any_variant_members():
    variants = _current_variants()
    plans = controls.remainder_plans(variants)
    assert plans["current_identity"] == {"mode": "production"}
    expected = {
        "current_without_glide": "OldEnglishOrthography",
        "current_earlier_lowering": "OEFinalUnstressedOLowering",
        "current_before_umlaut": "OEInterStressRaising",
        "current_delayed_umlaut": "OEInterStressRaising",
    }
    for name, checkpoint in expected.items():
        plan = plans[name]
        assert plan["checkpoint"] == checkpoint
        members = [s.foma_identifier if s.kind == "named" else s.inline_text
                   for s in variants[name]]
        assert members[:members.index(checkpoint) + 1] + plan["members"] == members


@pytest.mark.parametrize("stdout,expected", [
    (b"a\tb\na\tc\na\tb\n\n", ["b", "c"]),
    (b"a\t\n\n", [""]),
    (b"a\t+?\n\n", []),
])
def test_prefix_parser_distinguishes_epsilon_rejection_and_branching(monkeypatch, stdout, expected):
    monkeypatch.setattr(controls.subprocess, "run", lambda *a, **k:
                        subprocess.CompletedProcess(a, 0, stdout=stdout))
    assert controls.prefix_outputs(Path("prefix.bin"), "a") == expected


@pytest.mark.parametrize("stdout", [b"", b"bad\n", b"other\tb\n"])
def test_prefix_parser_fails_closed_on_missing_or_malformed_results(monkeypatch, stdout):
    monkeypatch.setattr(controls.subprocess, "run", lambda *a, **k:
                        subprocess.CompletedProcess(a, 0, stdout=stdout))
    with pytest.raises(RuntimeError, match="cumulative-prefix"):
        controls.prefix_outputs(Path("prefix.bin"), "a")


def test_continuation_deduplicates_all_branches_and_never_looks_up_rejection():
    calls = []
    def lookup(form):
        calls.append(form)
        return {"b": ["x", "y"], "c": ["y", "z"]}[form]
    assert controls.continue_outputs([], lookup) == []
    assert calls == []
    assert controls.continue_outputs(["b", "c"], lookup) == ["x", "y", "z"]
    assert calls == ["b", "c"]
    with pytest.raises(ValueError, match="complete composition"):
        controls.continue_outputs([""], lookup)
    plan = {"mode": "remainder", "members": ["B"], "full_members": ["A", "B"]}
    assert controls.effective_plan(plan, {"a": []}) is plan
    assert controls.effective_plan(plan, {"a": [""]})["members"] == ["A", "B"]


def test_stale_manifest_fails_before_any_canonical_lookup(monkeypatch):
    import capr_runtime
    monkeypatch.setattr(capr_runtime, "check_build_manifest", lambda names: ["stale bins"])
    def forbidden(*args, **kwargs):
        pytest.fail("stale manifest reached a lookup or compiler")
    monkeypatch.setattr(controls.subprocess, "run", forbidden)
    with pytest.raises(RuntimeError, match="not fresh: stale bins"):
        controls.run_controls({"plans": {}, "rows": []}, {})


def test_instrumentation_distinguishes_compilation_from_version_queries(monkeypatch, capsys):
    def assay(payload, profile):
        profile["phase"] = "measurement control"
        for argv in (["foma", "-v"], ["foma", "-q", "-f", "test.foma"],
                     ["flookup", "-i", "test.bin"]):
            subprocess.run(argv, check=True)
        return {"live": True}
    monkeypatch.setattr(controls, "run_controls", assay)
    monkeypatch.setattr(controls.subprocess, "run", lambda argv, **kwargs:
                        subprocess.CompletedProcess(argv, 0))
    controls.main({})
    report = json.loads(capsys.readouterr().out)
    assert report["outputs"] == {"live": True}
    profile = report["execution"]
    assert profile["compiler_calls"] == 1
    assert profile["subprocess_counts"] == {"foma": 2, "flookup": 1}
    assert all(p["phase"] == "measurement control" and p["returncode"] == 0
               for p in profile["subprocesses"])


@pytest.mark.parametrize("form", ["", "a\nb", "a\tb"])
def test_finite_domain_fails_closed_for_epsilon_and_record_separators(form):
    with pytest.raises(ValueError, match="unsupported finite-domain"):
        controls.foma_domain([form])


@pytest.mark.runtime
def test_live_relational_remainder_matches_full_composition_for_branching_epsilon_and_rejection():
    worker = Path(controls.__file__).read_text().split('if __name__ == "__main__":')[0]
    script = """import sys
sys.path.insert(0, "/usr/app/tools")
""" + worker + """
from anglo_frisian_experiments import _compile_foma
from oe_pipeline import apply_down
with tempfile.TemporaryDirectory(prefix="capr_chronology_relational_") as directory:
    root = Path(directory)
    script = root / "test.foma"
    literals = ["ab", "0", "*?[]%|:", "\\u00e9*\\u1d9c"]
    script.write_text('''
define Prefix [a:b|a:c|e:0];
define Suffix [b:x|b:y|c:y|0:w];
define Complete Prefix .o. Suffix;
''' + "define BoundedSuffix " + foma_domain(["b", "c"]) + " .o. Suffix;\\n" +
        "define LiteralDomain " + foma_domain(literals) + ";\\n" +
        "define EmptyDomain " + foma_domain([]) + ";\\n" +
        "define SymbolBoundary " + foma_domain(["ab"]) + " .o. [{ab}:c];\\n" + '''
clear stack
regex Prefix;
save stack prefix.bin
clear stack
regex BoundedSuffix;
save stack suffix.bin
clear stack
regex Complete;
save stack full.bin
clear stack
regex LiteralDomain;
save stack literals.bin
clear stack
regex EmptyDomain;
save stack empty.bin
clear stack
regex SymbolBoundary;
save stack symbols.bin
quit
''')
    _compile_foma(script, root)
    for literal in literals:
        assert apply_down(root / "literals.bin", literal) == [literal], literal
    assert apply_down(root / "literals.bin", "unselected") == []
    assert apply_down(root / "symbols.bin", "ab") == ["c"]
    assert apply_down(root / "empty.bin", "a") == []
    results = {}
    plan = {"mode": "remainder", "members": ["Suffix"],
            "full_members": ["Prefix", "Suffix"]}
    for form in ("a", "e", "q"):
        states = prefix_outputs(root / "prefix.bin", form)
        selected = effective_plan(plan, {form: states})
        expected = apply_down(root / "full.bin", form)
        actual = (apply_down(root / "full.bin", form) if selected["mode"] == "full"
                  else continue_outputs(states, lambda s: apply_down(root / "suffix.bin", s)))
        assert set(actual) == set(expected), (form, states, actual, expected)
        results[form] = {"states": states, "outputs": actual, "mode": selected["mode"]}
    assert set(results["a"]["states"]) == {"b", "c"}
    assert set(results["a"]["outputs"]) == {"x", "y"}
    assert results["e"] == {"states": [""], "outputs": ["w"], "mode": "full"}
    assert results["q"]["states"] == results["q"]["outputs"] == []
print(json.dumps(results))
"""
    proc = run_in_runner(
        't=$(mktemp) && cat > "$t" && python3 "$t"; rc=$?; rm -f "$t"; exit $rc',
        input=script, text=True, capture_output=True, check=True, timeout=60)
    assert set(json.loads(proc.stdout)) == {"a", "e", "q"}
