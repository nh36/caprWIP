"""Calibrate the fixed-input counterexample verifier, not the accepted proof."""
import importlib.util
from pathlib import Path

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
