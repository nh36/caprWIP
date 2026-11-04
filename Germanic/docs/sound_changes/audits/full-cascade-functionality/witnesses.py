#!/usr/bin/env python3
"""Verify exact accepting paths, and look for domain-loss counterexamples."""
from collections import defaultdict, deque
import importlib.util
import json
from pathlib import Path
import sys

HELPERS = Path(__file__).resolve().parents[1] / "parser-formal-resolution"
spec = importlib.util.spec_from_file_location("cascade_witness_proof", HELPERS / "functionality.py")
proof = importlib.util.module_from_spec(spec)
spec.loader.exec_module(proof)


def paths(text, word, output=None):
    arcs, finals = proof.read_att(text)
    if any(len(label) != 1 for arc in arcs for label in arc[2:]
           if label != proof.EPSILON):
        raise ValueError("This character-string witness adapter requires single-codepoint labels")
    outgoing = defaultdict(list)
    for index, (p, q, upper, lower) in enumerate(arcs):
        outgoing[p].append(index)
    start = (0, 0, 0)
    pending, parents = deque([start]), {start: None}
    accepting = None
    while pending:
        state, i, j = key = pending.popleft()
        if i == len(word) and state in finals and (output is None or j == len(output)):
            accepting = key
            break
        for index in outgoing[state]:
            p, q, upper, lower = arcs[index]
            i2, j2 = i, j
            if upper != proof.EPSILON:
                if i == len(word) or upper != word[i]:
                    continue
                i2 += 1
            if output is not None and lower != proof.EPSILON:
                if j == len(output) or lower != output[j]:
                    continue
                j2 += 1
            next_key = q, i2, j2
            if next_key not in parents:
                parents[next_key] = key, index
                pending.append(next_key)
    if accepting is None:
        return dict(accepted=False, explored_states=len(parents),
                    method="complete fixed-input reachability; not global enumeration")
    indices = []
    current = accepting
    while parents[current] is not None:
        current, index = parents[current]
        indices.append(index)
    indices.reverse()
    state, actual_input, actual_output = 0, [], []
    for index in indices:
        p, q, upper, lower = arcs[index]
        assert p == state
        state = q
        if upper != proof.EPSILON:
            actual_input.append(upper)
        if lower != proof.EPSILON:
            actual_output.append(lower)
    assert state in finals and actual_input == list(word)
    assert output is None or actual_output == list(output)
    return dict(accepted=True, arc_path=indices, input=actual_input,
                output=actual_output, final_state=state)


if __name__ == "__main__":
    directory = Path(sys.argv[1])
    actual = (directory / "actual.att").read_text()
    parser = (directory / "prefix-000.att").read_text()
    results = dict(
        canonical_input=paths(parser, "ggai"),
        actual_outputs=[paths(actual, "ggai", value) for value in ("gġē", "ġġē")],
        explicit_stress_ambiguity=dict(
            canonical_input=paths(parser, "g-géua"),
            actual_outputs=[paths(actual, "g-géua", value)
                            for value in ("gġēo", "ġġēo")]),
        totality_counterexample=dict(input="b", parser=paths(parser, "b"),
                                     actual=paths(actual, "b")),
        explicit_stress_totality=dict(input="ɣó", parser=paths(parser, "ɣó"),
                                      actual=paths(actual, "ɣó")),
    )
    assert results["canonical_input"]["accepted"]
    assert all(r["accepted"] for r in results["actual_outputs"])
    assert results["totality_counterexample"]["parser"]["accepted"]
    assert not results["totality_counterexample"]["actual"]["accepted"]
    assert results["explicit_stress_ambiguity"]["canonical_input"]["accepted"]
    assert all(r["accepted"] for r in results["explicit_stress_ambiguity"]["actual_outputs"])
    assert results["explicit_stress_totality"]["parser"]["accepted"]
    assert not results["explicit_stress_totality"]["actual"]["accepted"]
    (directory / "verified-witnesses.json").write_text(json.dumps(results, indent=2))
    print(json.dumps(results, ensure_ascii=False))
