import importlib.util
from pathlib import Path
import sys

import pytest


PATH = (Path(__file__).resolve().parents[1] /
        "docs/sound_changes/audits/parser-formal-resolution/functionality.py")
SPEC = importlib.util.spec_from_file_location("parser_functionality", PATH)
proof = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(proof)
sys.modules["functionality"] = proof
ALIGNMENT_SPEC = importlib.util.spec_from_file_location("parser_alignment", PATH.with_name("alignment.py"))
alignment = importlib.util.module_from_spec(ALIGNMENT_SPEC)
ALIGNMENT_SPEC.loader.exec_module(alignment)


@pytest.mark.parametrize(("arcs", "finals", "functional"), [
    ([(0, 1, "a", "x")], [1], True),
    ([(0, 1, "a", "x"), (0, 1, "b", "x")], [1], True),
    ([(0, 1, "a", "x"), (0, 1, "a", "y")], [1], False),
    ([(0, 1, "a", "@0@"), (1, 2, "@0@", "a")], [2], True),
    ([(0, 0, "a", "x")], [0], True),
    ([(0, 0, "@0@", "x")], [0], False),
    ([(0, 1, "b", "*b"), (1, 2, "i", "*i"), (2, 3, "u", "*u"),
      (1, 4, "i", "*iu"), (4, 3, "u", "@0@")], [3], False),
    ([(0, 1, "a", "@0@"), (0, 2, "@0@", "a"),
      (1, 3, "@0@", "a"), (2, 3, "a", "@0@")], [3], True),
    ([(0, 1, "@0@", "@0@"), (1, 2, "a", "a")], [2], True),
    ([(0, 1, "a", "x"), (0, 2, "a", "y"),
      (2, 2, "b", "z")], [1], True),
    ([(0, 1, "a", "x"), (0, 2, "a", "@0@"),
      (1, 1, "b", "x"), (2, 2, "b", "x"),
      (1, 3, "c", "@0@"), (2, 3, "c", "x")], [3], True),
])
def test_complete_twin_proof(arcs, finals, functional):
    text = "".join("\t".join(map(str, arc)) + "\n" for arc in arcs)
    text += "".join(str(state) + "\n" for state in finals)
    result = proof.analyze(text)
    assert result["functional"] is functional
    if functional:
        proof.verify(text, result)
    else:
        assert result["witness"]["outputs"][0] != result["witness"]["outputs"][1]


def test_symbolic_arcs_are_not_silently_approximated():
    with pytest.raises(ValueError, match="different proof"):
        proof.analyze("0\t1\t@_IDENTITY_SYMBOL_@\t@_IDENTITY_SYMBOL_@\n1\n")


@pytest.mark.parametrize("corruption", ["missing_state", "wrong_delay", "wrong_network"])
def test_certificate_verifier_rejects_tampering(corruption):
    source = "0\t1\ta\t@0@\n1\t2\t@0@\tx\n2\n"
    certificate = proof.analyze(source)
    if corruption == "missing_state":
        certificate["delays"].pop()
    elif corruption == "wrong_delay":
        certificate["delays"][0][2] = ["not-an-output"]
    else:
        certificate["att_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="certificate"):
        proof.verify(source, certificate)


def test_ambiguity_domain_counts_outputs_not_computational_paths():
    source = (
        "0\t1\ta\t@0@\n0\t2\t@0@\tx\n1\t3\t@0@\tx\n2\t3\ta\t@0@\n"
        "0\t4\tb\tx\n0\t4\tb\ty\n3\n4\n")
    ambiguous, certificate = alignment.ambiguity_domain(source)
    expected = "0\t1\tb\tb\n1\n"
    assert certificate
    assert alignment.domain_check([ambiguous, expected], lambda f: f[0] == f[1])["valid"]


def test_cyclic_ambiguity_domain_is_complete():
    source = "0\t0\ta\tx\n0\t0\ta\ty\n0\n"
    ambiguous, _ = alignment.ambiguity_domain(source)
    expected = "0\t1\ta\ta\n1\t1\ta\ta\n1\n"
    assert alignment.domain_check([ambiguous, expected], lambda f: f[0] == f[1])["valid"]


def test_subsequential_alignment_preserves_delayed_and_cyclic_outputs():
    source = "0\t1\ta\t@0@\n1\t2\t@0@\tx\n2\t3\tb\t@0@\n3\t0\t@0@\ty\n0\n"
    aligned, certificate = alignment.subsequentialize(source)
    assert certificate["subsets"]
    assert alignment.domain_check([source, aligned], lambda f: f[0] == f[1])["valid"]
    source_arcs, source_finals = proof.read_att(source)
    new_arcs, new_finals = proof.read_att(aligned)
    offset = 1 + max(p for arc in source_arcs for p in arc[:2])
    union = [(0, 1, "@0@", "@0@"), (0, offset + 1, "@0@", "@0@")]
    union += [(p + 1, q + 1, a, b) for p, q, a, b in source_arcs]
    union += [(p + offset + 1, q + offset + 1, a, b) for p, q, a, b in new_arcs]
    finals = {p + 1 for p in source_finals} | {p + offset + 1 for p in new_finals}
    assert proof.analyze(alignment.att_text(union, finals))["functional"]


def test_domain_check_returns_real_distinguishing_input():
    result = alignment.domain_check(
        ["0\t1\tatomic-ai\tatomic-ai\n1\n", ""], lambda f: f[0] == f[1])
    assert result == dict(valid=False, input=["atomic-ai"], flags=[True, False])


def test_subsequential_alignment_rejects_live_epsilon_output_cycles():
    with pytest.raises(ValueError, match="functional relation"):
        alignment.subsequentialize("0\t0\t@0@\tx\n0\n")
