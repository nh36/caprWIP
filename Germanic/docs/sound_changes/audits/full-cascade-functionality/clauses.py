#!/usr/bin/env python3
"""Bounded clause-isolation exports; no production definition is changed."""
import json
from pathlib import Path
import sys

from probe import native


if __name__ == "__main__":
    sys.path.insert(0, "/usr/app/tools")
    from executable_facts import define_facts

    parent = Path(sys.argv[1])
    output = parent / "clause-isolation"
    output.mkdir()
    source = parent / "germanic.txt"
    body = define_facts(source)["OEVelarPalatalizationStops"].body
    block = body.split(".o.")[1].strip()
    assert block.startswith("[") and block.endswith("]")
    clauses = block[1:-1].split(",")
    assert len(clauses) == 5
    cases = {f"clause-{i + 1}": "[" + clause + "]"
             for i, clause in enumerate(clauses)}
    cases["first-four"] = "[" + ",".join(clauses[:4]) + "]"
    cases["all-five"] = block
    commands = [f"source {source}", "clear stack"]
    for label, expression in cases.items():
        commands += ["clear stack", f"regex [{{*g*g*ē}} .o. [{expression}]];",
                     f"write att > {label}.att"]
    receipt = native(commands, output)
    (output / "native.json").write_text(json.dumps(receipt, indent=2))
    (output / "expressions.json").write_text(json.dumps(cases, indent=2))
    assert receipt["returncode"] == 0
