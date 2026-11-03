#!/usr/bin/env python3
"""Canonical stress disambiguation and equivalent native-checkable alignment."""
import argparse
import gzip
import json
import os
from pathlib import Path
import subprocess
import tempfile

import alignment
import experiment
import functionality


EXTRA = """
define PGRaw [PGCellPlain | PGCellPrefixed];
define PGCanonBuiltin [
    _unambpart(EnglishProtoNative) |
    _unambpart([[PGRaw.u - EnglishProtoNative.u] .o. PGRaw])
];
"""
NAMES = ["EnglishProtoNative", "PGCellRoot", "PGCellPlain", "PGCellInput",
         "PGNew", "PGRaw", "PGCanonBuiltin"]
PROBES = [
    "biu", "bíu", "biú", "gailanai", "gáilanai", "gaílanai",
    "biulanai", "bíulanai", "biúlanai", "gaiu", "gáiu", "gaíu",
    "gaiulō", "gáiulō", "gaíulō", "sáiwalǭ", "fúnðanai", "xámaraz", "wéstą",
    "", "bn", "lanai", "fúnðanaí", "fúnðanainai", "fúnðnanai",
    "gailanananai", "gáilanananai", "gaílanananai",
    "biulanananai", "bíulanananai", "biúlanananai",
    "fúnð" + "an" * 24 + "ai",
    "gáil" + "an" * 24 + "ai",
    "gaíl" + "an" * 24 + "ai",
]


def relation_union(left, right):
    a, af = functionality.read_att(left)
    b, bf = functionality.read_att(right)
    offset = 1 + max([0, *[s for arc in a for s in arc[:2]], *af])
    arcs = [(0, 1, "@0@", "@0@"), (0, offset + 1, "@0@", "@0@")]
    arcs += [(p + 1, q + 1, x, y) for p, q, x, y in a]
    arcs += [(p + offset + 1, q + offset + 1, x, y) for p, q, x, y in b]
    finals = {p + 1 for p in af} | {p + offset + 1 for p in bf}
    return alignment.att_text(arcs, finals)


def worker(output):
    import adoption_assay
    from anglo_frisian_experiments import compile_isolated, prepare_definition_image
    from sound_change_order_sensitivity import batch_apply_down

    if not Path("/.dockerenv").exists():
        raise RuntimeError("Container-only native execution")
    output.mkdir()
    report, sources = dict(components={}, checks={}), {}

    def native(name, commands):
        argv = ["foma", "-q"]
        for command in commands + ["print size", "test functional", "test unambiguous",
                                   "write att > " + str(output / (name + ".att")), "quit"]:
            argv.extend(["-e", command])
        completed = subprocess.run(argv, capture_output=True, text=True, check=True, timeout=300)
        text = (output / (name + ".att")).read_text()
        proof = functionality.analyze(text)
        if proof["functional"]:
            functionality.verify(text, proof)
        (output / (name + "-proof.json")).write_text(json.dumps(proof))
        report["components"][name] = dict(
            stdout=completed.stdout, stderr=completed.stderr,
            independent={k: v for k, v in proof.items() if k != "delays"})
        sources[name] = text
        return proof["functional"]

    with tempfile.TemporaryDirectory(prefix="capr_canonical_") as temporary:
        directory = Path(temporary)
        image = prepare_definition_image(adoption_assay.G / "fsts/germanic.txt", directory)
        if image:
            os.environ["CAPR_FOMA_DEFINITION_IMAGE"] = str(image)
        recipe = dict(
            definitions=experiment.DEFINITIONS + EXTRA, insert_after="", insert_rule="", replace={},
            component_checks=[dict(component=name) for name in NAMES])
        binaries = compile_isolated(
            adoption_assay.G / "fsts/germanic.txt", recipe, [], directory, components_only=True)
        for name in NAMES:
            print("export " + name, flush=True)
            native(name, ["load stack " + str(binaries["component:" + name])])
        for name in ("EnglishProtoNative", "PGRaw"):
            print("complete ambiguity domain " + name, flush=True)
            domain, certificate = alignment.ambiguity_domain(sources[name])
            sources[name + "Bad"] = domain
            (output / (name + "-ambiguous-domain.att")).write_text(domain)
            (output / (name + "-ambiguity-certificate.json")).write_text(json.dumps(certificate))
            report["checks"][name + "_ambiguity_states"] = len(certificate)
        print("compare exact canonical input domain", flush=True)
        report["checks"]["canonical_domain"] = alignment.domain_check(
            [sources[n] for n in ("EnglishProtoNative", "EnglishProtoNativeBad", "PGRaw",
                                  "PGRawBad", "PGCanonBuiltin")],
            lambda f: f[4] == ((f[0] and not f[1]) or (f[2] and not f[0] and not f[3])))
        report["checks"]["productive_domain_conserved"] = alignment.domain_check(
            [sources["PGCellInput"], sources["PGRaw"]], lambda f: f[0] == f[1])
        for name in ("PGCellRoot", "PGCellPlain", "PGNew", "PGCanonBuiltin"):
            if not report["components"][name]["independent"]["functional"]:
                continue
            print("subsequential alignment " + name, flush=True)
            text, certificate = alignment.subsequentialize(sources[name])
            raw = output / (name + "-aligned-source.att")
            raw.write_text(text)
            (output / (name + "-alignment-certificate.json")).write_text(json.dumps(certificate))
            aligned = name + "Aligned"
            binary = directory / (aligned + ".bin")
            native(aligned, ["read att " + str(raw), "minimize", "save stack " + str(binary)])
            binaries["component:" + aligned] = binary
            union = relation_union(sources[name], sources[aligned])
            proof = functionality.analyze(union)
            if proof["functional"]:
                functionality.verify(union, proof)
            (output / (name + "-equivalence-union.att")).write_text(union)
            (output / (name + "-equivalence-proof.json")).write_text(json.dumps(proof))
            report["checks"][name + "_same_outputs"] = proof["functional"]
            report["checks"][name + "_same_domain"] = alignment.domain_check(
                [sources[name], sources[aligned]], lambda f: f[0] == f[1])
        research = json.loads(gzip.decompress(
            (adoption_assay.G / "docs/sound_changes/audits/soul-lexical-reassessment/"
             "results.json.gz").read_bytes()))
        inputs = research["input_order"] + PROBES
        names = ["EnglishProtoNative", "PGCellInput", "PGRaw", "PGCanonBuiltin"]
        if "PGCanonBuiltinAligned" in sources:
            names.append("PGCanonBuiltinAligned")
        mappings = {name: batch_apply_down(binaries["component:" + name], inputs)
                    for name in names}
        report["mappings"] = [
            dict(index=i, input=word, outputs={n: mappings[n][i] for n in names})
            for i, word in enumerate(inputs)]
        for name in names:
            report["components"][name]["probe_paths"] = {
                word: experiment.fixed_paths(sources[name], word) for word in PROBES}
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(json.dumps(report["checks"], indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--worker", type=Path)
    args = parser.parse_args()
    if args.worker:
        worker(args.worker)
    else:
        experiment.host(args.id, entry=Path(__file__), extra_files=[
            Path(alignment.__file__), Path(experiment.__file__),
            experiment.ROOT / "Germanic/docs/sound_changes/audits/"
            "soul-lexical-reassessment/results.json.gz"])
