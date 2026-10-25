"""Related manuscript evidence and the adopted bounded phonological domain."""
from collections import Counter
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

import pytest

ROOT = Path(__file__).resolve().parents[2]
ASSAY = ROOT / "Germanic/docs/sound_changes/audits/sc035-generality"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import adjudicate
from capr_runtime import run_in_runner
from check_bibliography_sanity import parse_entries


def table(name):
    with (ASSAY / name).open() as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def test_attestations_have_unique_identity_and_explicit_witness_provenance():
    witnesses = table("witnesses.tsv")
    assert len({row["witness"] for row in witnesses}) == len(witnesses)
    dates = {row["witness"]: row for row in witnesses}
    rows = table("attestations.tsv")
    assert len(rows) == len({row["id"] for row in rows}) == 51
    for row in witnesses + rows:
        assert None not in row
        assert all(value and value.strip() for value in row.values())
    for row in rows:
        assert row["witness"] in dates
        assert row["source_key"] in {"Sweet1885", "Sweet1871", "Stevenson1840", "RuneSPforzen"}
        assert row["spelling_status"] and row["prosody"] and row["independence_group"]
    assert "disputed" in dates["Erfurt"]["date_of_surviving_witness"]
    assert "exemplar" in dates["Erfurt"]["exemplar_or_linguistic_layer"]
    assert "9c" in dates["Corpus"]["date_of_surviving_witness"]


def test_nine_related_glossary_alignments_reproduce_toller_without_independent_votes():
    rows = table("attestations.tsv")
    groups = {}
    for row in rows:
        if row["id"].split("-")[0] in {
            "EE189", "EE191", "EE196", "EE197", "EE201", "EE203", "EE205", "EE207", "EE214",
        }:
            groups.setdefault(row["id"].split("-")[0], {})[row["witness"]] = row
    assert len(groups) == 9
    pairs = Counter()
    for group in groups.values():
        assert set(group) == {"Epinal", "Erfurt", "Corpus"}
        pairs[(group["Epinal"]["form"][:2], group["Erfurt"]["form"][:2])] += 1
        assert group["Corpus"]["form"].startswith("ge")
        assert len({row["independence_group"] for row in group.values()}) == 1
    assert pairs == {("gi", "gi"): 4, ("ge", "ge"): 1, ("gi", "ge"): 2, ("ge", "gi"): 2}
    assert "Corpus503" in groups["EE189"]["Corpus"]["locator"]
    assert "Corpus505" in groups["EE191"]["Corpus"]["locator"]
    assert "corrected from i" in groups["EE207"]["Epinal"]["spelling_status"]
    forms = {row["id"]: row["form"] for row in rows}
    assert forms["EE76-Erf"] == "gaeadun"
    assert forms["EE228-Ep"] == "gybyrdid"
    assert forms["Corpus2152"] == "gibrec"
    assert forms["EE140-Ep"] == "gibeataen"


def test_new_observation_is_traceable_without_overwriting_earlier_experiments():
    record = json.loads((ASSAY / "evidence.json").read_text())
    source = subprocess.check_output([
        "git", "show", record["accepted_base_commit"] + ":Germanic/fsts/germanic.txt",
    ], cwd=ROOT)
    assert hashlib.sha256(source).hexdigest() == record["source_sha256"]
    for directory in ("sc035-prefix-reduction", "sc035-model-comparison", "sc035-prosody"):
        path = f"Germanic/docs/sound_changes/audits/{directory}/evidence.json"
        old = subprocess.check_output([
            "git", "show", record["accepted_base_commit"] + ":" + path,
        ], cwd=ROOT)
        assert (ROOT / path).read_bytes() == old
    spec = importlib.util.spec_from_file_location("sc035_generality_assay", ASSAY / "verify.py")
    assay = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(assay)
    groups = assay.cases()
    assert sum(len(pairs) for _, pairs in groups.values()) == 345
    assert record["controls"] == {
        name: [{"input": form, "output": expected} for form, expected in pairs]
        for name, (_, pairs) in groups.items()
    }


def test_current_verdict_confidence_and_publication_sources_are_coherent():
    row = adjudicate.load_registry_row("SC035")
    assert row["verdict"] == "RETAIN"
    assert row["confidence"] == "B"
    assert (row["hist_stage"], row["hist_scope"]) == ("preoe", "english_specific")
    assert row["adjudication_memo"].endswith("sc035-generality-adjudication.md")
    assert adjudicate.check_memo("SC035", row=row) == []
    entries = parse_entries((ROOT / "docs/refs.bib").read_text())
    reader = (ROOT / "Germanic/docs/sound_changes/reader_facing" /
              row["source_reader_facing_file"]).read_text()
    resources = (ROOT / "docs/references/README_resources.md").read_text()
    index = (ROOT / "Germanic/docs/REFERENCES.md").read_text()
    for key in ("Sweet1885", "Sweet1871", "Stevenson1840",
                "LucasLucas2012", "Lucas2016", "RuneSPforzen"):
        assert len([entry for entry in entries if entry.key == key]) == 1
        assert "@" + key + "," in reader
        assert key in resources and key in index
    assert "@Toller1921, p. 284" in reader


def test_pforzen_record_keeps_object_date_distinct_from_excavation():
    path = ROOT / "docs/references/runes_pforzen_201.xml"
    root = ET.parse(path).getroot()
    ns = {"l": "http://www.lido-schema.org"}
    ranges = {
        (event.findtext(".//l:earliestDate", namespaces=ns),
         event.findtext(".//l:latestDate", namespaces=ns))
        for event in root.findall(".//l:event", ns)
    }
    assert ("585", "610") in ranges
    assert ("1991-1996", "1991-1996") in ranges
    assert "https://creativecommons.org/licenses/by-sa/4.0/" in path.read_text()


@pytest.mark.runtime
def test_fresh_phonological_domain_and_registered_original_holdings():
    holdings = {
        "sweet_1885_oldest_english_texts.pdf":
            "7f13fd3e587fa915b89fcbdce6908809619540fff594ceb8defeaf2fb236940a",
        "sweet_1871_pastoral_care.pdf":
            "ad5c16e2caefd04f7511702f790ce8ca335958c61130230bd0dad7b328dfded5",
        "stevenson_1840_durham_ritual.pdf":
            "6645fd2946b425c12c9c2972a78c92cf17e45608db2e5de464c179c1821e3cf3",
        "lucas_lucas_2012_epinal_72.pdf":
            "53153917589fabb10333bf201c00f2b0f262ab42cfd7eaa829ef1ee7d70914dc",
        "lucas_2016_corpus_144.pdf":
            "1f4941dd93037c9b13239c2eb27e3c4f23bf62121ac29d426b920273465774d4",
    }
    for name, digest in holdings.items():
        assert hashlib.sha256((ROOT / "docs/references" / name).read_bytes()).hexdigest() == digest
    result = run_in_runner(
        "python3 docs/sound_changes/audits/sc035-generality/verify.py",
        text=True, capture_output=True, check=True, timeout=1800)
    current = json.loads(result.stdout)
    observed = json.loads((ASSAY / "evidence.json").read_text())
    assert current["controls"] == observed["controls"]
