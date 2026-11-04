"""Calibrate the fixed-input counterexample verifier, not the accepted proof."""
import importlib.util
from pathlib import Path
import tarfile

import pytest


PATH = (Path(__file__).resolve().parents[1] / "docs/sound_changes/audits"
        / "full-cascade-functionality/witnesses.py")
SPEC = importlib.util.spec_from_file_location("capr_cascade_witnesses", PATH)
WITNESSES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WITNESSES)


def test_epsilon_output_cycle_acceptance_and_complete_rejection():
    text = "0\t1\t@0@\t@0@\n1\t1\t@0@\tx\n1\t2\ta\tb\n2\n"
    assert WITNESSES.paths(text, "a", "xxb")["output"] == ["x", "x", "b"]
    assert WITNESSES.paths(text, "a")["accepted"]
    assert not WITNESSES.paths(text, "a", "c")["accepted"]
    assert not WITNESSES.paths(text, "z")["accepted"]


def test_character_adapter_rejects_multicharacter_labels():
    with pytest.raises(ValueError, match="single-codepoint"):
        WITNESSES.paths("0\t1\tai\tx\n1\n", "ai")


def test_private_repair_preserves_definition_boundaries_and_comments(monkeypatch):
    root = Path(__file__).resolve().parents[1]
    monkeypatch.syspath_prepend(str(root / "tools"))
    from executable_facts import parse_defines

    spec = importlib.util.spec_from_file_location(
        "capr_private_repair_probe", PATH.parent / "repair_probe.py")
    repair = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(repair)
    source = """define Before a;
define OEVelarPalatalizationStops [
    K
] .o. [
    # This semicolon must not terminate the definition;
    g -> d || _ F,
    g -> d || F _ .#.,
    g -> d || F _ F,
    g -> d || F _ C,
    g g -> d d || _ j
] .o. [g -> d || _ j];
define After z;
"""
    candidates = repair.variants(source, parse_defines(source))
    for candidate in candidates.values():
        facts = parse_defines(candidate)
        assert set(facts) == {"Before", "OEVelarPalatalizationStops", "After"}
        assert facts["Before"].body == "a"
        assert facts["After"].body == "z"
        assert candidate.startswith("define Before a;\n")
        assert candidate.endswith("\ndefine After z;\n")
    assert len(parse_defines(candidates["serial"])[
        "OEVelarPalatalizationStops"].body.split(".o.")) == 4
    assert len(candidates["scoped"]) == len(source) + 1
    assert candidates["scoped"].replace(",,", ",", 1) == source


def test_actual_compiler_context_scoping_calibration():
    texts = {}
    with tarfile.open(PATH.parent / "repair-evidence.tar.gz", "r|gz") as capsule:
        for member in capsule:
            if member.name in ("mini_original.att", "mini_scoped.att"):
                texts[member.name] = capsule.extractfile(member).read().decode()
            if len(texts) == 2:
                break
    original, scoped = texts["mini_original.att"], texts["mini_scoped.att"]
    assert WITNESSES.paths(original, "aae", "bbe")["accepted"]
    assert WITNESSES.paths(original, "aae", "abe")["accepted"]
    assert WITNESSES.paths(scoped, "aae", "abe")["accepted"]
    assert not WITNESSES.paths(scoped, "aae", "bbe")["accepted"]
    assert WITNESSES.paths(scoped, "aaj", "bbj")["accepted"]
    assert not WITNESSES.paths(scoped, "aaj", "abj")["accepted"]
    certificate = WITNESSES.proof.analyze(scoped)
    assert certificate["functional"]
    WITNESSES.proof.verify(scoped, certificate)
