"""Authenticate research trials; these are not fresh counterfactual execution."""
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from executable_facts import parse_defines

EVIDENCE = ROOT / "Germanic/docs/sound_changes/audits/rainbow-stress-evidence"


def trials():
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    for name, digest in manifest["members"].items():
        assert hashlib.sha256((EVIDENCE / name).read_bytes()).hexdigest() == digest
    provenance = json.loads((EVIDENCE / "provenance.json").read_text())
    observed = {}
    for label in ("initial", "annotation", "final"):
        record = provenance[label]
        receipt = record["completion"]["command_receipts"][0]
        payload = gzip.decompress((EVIDENCE / f"{label}-observed.json.gz").read_bytes())
        assert hashlib.sha256(payload).hexdigest() == receipt["stdout_sha256"]
        assert hashlib.sha256(record["stderr"].encode()).hexdigest() == receipt["stderr_sha256"]
        assert receipt["ok"] and record["completion"]["outcome"] == "passed"
        assert record["snapshot"]["inputs"]["source"]["sha256"] == manifest["source_sha256"]
        assert record["snapshot"]["inputs"]["corpus"]["sha256"] == manifest["corpus_sha256"]
        for member in ("worker.py", "plan.json", "assessment.md"):
            assert hashlib.sha256((EVIDENCE / f"{label}-{member}").read_bytes()).hexdigest() == (
                record["snapshot"]["inputs"][member.split(".")[0]]["sha256"])
        observed[label] = json.loads(payload)
    return observed


def values(observed, query):
    row = observed["queries"][query]
    return dict(zip(row["inputs"], row["outputs"]))


def test_joint_intervention_and_every_corpus_delta_are_authenticated():
    for observed in trials().values():
        assert len(observed["rows"]) == 394
        assert sum(row["counterpart"] in row["baseline"] for row in observed["rows"]) == 386
        for label, comparison in observed["corpus"].items():
            assert len({row["row_id"] for row in comparison["rows"]}) == 394
            assert comparison["rejected"] == comparison["ambiguous"] == 0
            assert {row["row_id"]: (row["baseline"], row["outputs"])
                    for row in comparison["rows"] if row["changed"]} == (
                {"2148": (["reġnboga"], ["reġneafoga"])} if label == "restoration" else {})
        for label in ("baseline", "restoration", "back_mutation", "joint"):
            final = values(observed, label + ":raw_final")
            assert final["régna-bùgô"] == [
                "reġneafoga" if label == "restoration" else "reġnboga"]
            for source, expected in {
                    "búgô": "boga", "érθa-kùnðǭ": "eorþcunde",
                    "bákaną": "bacan", "wádaną": "wadan",
                    "xébun": "heofon", "sébun": "seofon",
                    "wír-àldiz": "weorold"}.items():
                assert final[source] == [expected]
        assert observed["queries"]["joint:OEBackMutation"]["outputs"] == [
            ["*r*é*ʝ*n*æ*b*o*g*ô"], ["*éo*r*θ*æ*k*ù*n*d*ǣ"]]
        assert observed["queries"]["joint:OENonHighSyn"]["outputs"] == [
            ["*r*é*ʝ*n*b*o*g*ô"], ["*éo*r*θ*k*ù*n*d*ǣ"]]
        assert observed["queries"]["joint:PGmcBAllophony"]["outputs"][0] == [
            "*r*é*ʝ*n*b*o*g*ô"]


def test_stressed_ae_positive_and_secondary_decoding_limits_are_not_hidden():
    observed = trials()
    initial = observed["initial"]
    assert values(initial, "stress59:local")["*æ*l*u"] == ["*ea*l*u"]
    assert values(initial, "stress59:local")["*s*t*æ*ð*u*l"] == ["*s*t*æ*ð*u*l"]
    assert values(initial, "stress59:local")["*g*e*b*æ*b*u"] == ["*g*e*b*æ*b*u"]
    assert values(initial, "stress59:local")["*g*e*b*ǽ*b*u"] == ["*g*e*b*ea*b*u"]
    assert initial["queries"]["schema:OEBreaking"]["outputs"][0] == (
        initial["queries"]["schema:OEBreaking"]["outputs"][1])
    final = observed["final"]
    marked, weak = "régna-bàkaną", "régna-bakaną"
    restored = values(final, "joint:schema:OEARestoration")
    assert restored[marked] == ["*r*é*g*n*æ*b*à*k*a*n*ą"]
    assert restored[weak] == ["*r*é*g*n*æ*b*æ*k*a*n*ą"]
    syncopated = values(final, "joint:schema:OENonHighSyn")
    assert syncopated[marked] == ["*r*é*ʝ*n*b*a*k*ą*n"]
    assert syncopated[weak] == ["*r*é*ʝ*n*b*k*ą*n"]
    mutated = values(final, "joint:schema:OEBackMutation")
    assert mutated["régna-xèbun"] == ["*r*é*ʝ*n*æ*ç*eo*b*u*n"]
    assert mutated["régna-xebun"] == ["*r*é*ʝ*n*æ*ç*e*b*u*n"]
    endpoints = values(final, "joint:raw_final")
    assert endpoints[marked] == ["reġnbecan"]  # Later weak fronting remains unresolved.
    assert endpoints["régna-xèbun"] == ["reġnheofon"]
    assert endpoints["gabákaną"] == ["ġefacan"]
    assert endpoints["gasébun"] == ["ġeseofon"]


def test_unapplied_review_diff_matches_the_exact_compiled_definitions():
    trials()
    manifest = json.loads((EVIDENCE / "manifest.json").read_text())
    source = subprocess.check_output(
        ["git", "show", manifest["base_commit"] + ":Germanic/fsts/germanic.txt"], cwd=ROOT)
    assert hashlib.sha256(source).hexdigest() == manifest["source_sha256"]
    with tempfile.TemporaryDirectory() as temporary:
        candidate = Path(temporary) / "Germanic/fsts/germanic.txt"
        candidate.parent.mkdir(parents=True)
        candidate.write_bytes(source)
        subprocess.run(["git", "apply", str(EVIDENCE / "proposed-joint-stress.patch")],
                       cwd=temporary, check=True, capture_output=True)
        payload = candidate.read_bytes()
    assert hashlib.sha256(payload).hexdigest() == manifest["candidate_sha256"]
    before, after = parse_defines(source.decode()), parse_defines(payload.decode())
    mapping = manifest["candidate_definitions"]
    assert set(after) - set(before) == {"OESecondaryFrontDecode"}
    assert {name for name in before if before[name].body != after[name].body} == (
        set(mapping.values()) - {"OESecondaryFrontDecode"})
    plan = json.loads((EVIDENCE / "final-plan.json").read_text())
    import re
    for key, name in mapping.items():
        definition = re.sub(r"\b(" + "|".join(mapping) + r")\b",
                            lambda match: mapping[match[0]], plan["variants"][key])
        assert after[name].body == parse_defines(definition)[name].body
