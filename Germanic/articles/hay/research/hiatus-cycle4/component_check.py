"""Verify component identity and noninterference with actual Foma exports."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

from components import ComponentBuild


SNAPSHOT = Path(sys.argv[1])
sys.path.insert(0, str(SNAPSHOT / "Germanic/articles/hay/research/hiatus-cycle2"))

from reproduce_stress import run, verify


class First:
    RULES = ("IdAlpha",)

    @staticmethod
    def definitions():
        return "define IdAlpha [{*e} {*i} -> {*ē} || _ {*d}];"


class Second:
    RULES = ("IdBeta",)

    @staticmethod
    def definitions():
        return "define IdBeta [{*e} {*i} -> {*e} {*j} || _ {*n}];"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--stage-cache", type=Path, required=True)
    args = parser.parse_args()
    runtime = subprocess.check_output(["foma", "-v"], text=True).strip()
    source = args.snapshot / "Germanic/fsts/germanic.txt"
    expected = json.loads((run.HERE / "baseline.json").read_text())["source_sha256"]
    verify(run.frozen.sha(source), expected, "frozen source")
    probes = {"d": ["*t*e*i*d"], "n": ["*t*e*i*n"], "old": ["*t*e*j*n"]}
    with tempfile.TemporaryDirectory(prefix="hay4-isolation-") as directory:
        first = ComponentBuild(run.compile_candidates, source, args.stage_cache, directory, First, runtime)
        alpha = first.verify()["component:IdAlpha"]
        before = run.frozen.apply_stage(alpha, probes)
        second = ComponentBuild(run.compile_candidates, source, args.stage_cache, directory, Second, runtime)
        beta = second.verify()["component:IdBeta"]
        verify(alpha.name, beta.name, "exercise the same numbered filename")
        verify(alpha.parent == beta.parent, False, "distinct builds remain isolated")
        after = run.frozen.apply_stage(first.verify()["component:IdAlpha"], probes)
        other = run.frozen.apply_stage(beta, probes)
        verify(before, probes | {"d": ["*t*ē*d"]}, "Alpha positive and negatives")
        verify(after, before, "Alpha still has the same behavior and hash")
        verify(other, probes | {"n": ["*t*e*j*n"]}, "Beta positive and negatives")
        print(json.dumps({"first": first.receipt(), "second": second.receipt(),
                          "input": probes, "alpha_before": before, "alpha_after": after,
                          "beta": other}, ensure_ascii=False))


if __name__ == "__main__":
    main()
