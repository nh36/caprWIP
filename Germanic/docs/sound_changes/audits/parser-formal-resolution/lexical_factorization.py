#!/usr/bin/env python3
"""Verify exact productive-parser equivalence after lexical factorization."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

import alignment
import canonical_experiment
import experiment
import functionality
import production_assay


NAMES = ["PGCellCanonical", "PGCellStrip", "PGCellInput", "EnglishProtoInput"]


def worker(output):
    import adoption_assay
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image

    output.mkdir()
    fst = adoption_assay.G / "fsts/germanic.txt"
    fst.write_text(production_assay.canonical_source(fst.read_text()))
    (output / "candidatefst.txt").write_text(fst.read_text())
    report, sources = dict(components={}), {}
    with tempfile.TemporaryDirectory(prefix="capr_lexical_factor_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(fst, directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        recipe = dict(
            definitions="", insert_after="", insert_rule="", replace={},
            component_checks=[dict(component=name) for name in NAMES])
        bins = compile_isolated(fst, recipe, [], directory, components_only=True)
        for name in NAMES:
            path = output / (name + ".att")
            commands = ["load stack " + str(bins["component:" + name]), "print size",
                        "test functional", "test unambiguous", "write att > " + str(path), "quit"]
            argv = ["foma", "-q"]
            for command in commands:
                argv.extend(["-e", command])
            result = subprocess.run(argv, capture_output=True, text=True, check=True, timeout=180)
            sources[name] = path.read_text()
            proof = functionality.analyze(sources[name])
            if proof["functional"]:
                functionality.verify(sources[name], proof)
            (output / (name + "-proof.json")).write_text(json.dumps(proof))
            report["components"][name] = dict(
                stdout=result.stdout, stderr=result.stderr,
                independent={k: v for k, v in proof.items() if k != "delays"})
        union = canonical_experiment.relation_union(
            sources["PGCellCanonical"], sources["PGCellInput"])
        proof = functionality.analyze(union)
        if proof["functional"]:
            functionality.verify(union, proof)
        (output / "equivalence-union.att").write_text(union)
        (output / "equivalence-proof.json").write_text(json.dumps(proof))
        report["same_outputs"] = proof["functional"]
        report["same_domain"] = alignment.domain_check(
            [sources["PGCellCanonical"], sources["PGCellInput"]], lambda f: f[0] == f[1])
    (output / "report.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--worker", type=Path)
    args = parser.parse_args()
    if args.worker:
        worker(args.worker)
    else:
        experiment.host(args.id, entry=Path(__file__), extra_files=[
            Path(m.__file__) for m in (experiment, alignment, canonical_experiment, production_assay)])
