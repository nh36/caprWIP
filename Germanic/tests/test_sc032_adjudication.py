"""SC032's complete atomic census and quantity/chronology distinctions."""

from __future__ import annotations

import collections
import csv
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GERMANIC = ROOT / "Germanic"
sys.path.insert(0, str(GERMANIC / "tools"))

from generate_registry_views import EDGE_REGISTRY, SC_REGISTRY, read_tsv  # noqa: E402
from oe_full_trace_report import trace_provenance_problems  # noqa: E402

SC = GERMANIC / "docs/sound_changes"
TRACE = GERMANIC / "docs/debug_snapshots/oe_full_trace_report.txt"
EXPECTED = {
    "áeu": {
        "1944", "1961", "1962", "1966", "1989", "1995", "2018", "2061",
        "2063", "2074", "2094", "2097", "2116", "2135", "2151", "2170",
        "2184", "2224", "2225", "2227", "2241",
    },
    "éu": {"1968", "1976", "1988", "2019", "2022", "2028", "2029",
           "2032", "2102", "2246"},
    "íu": {"2033", "2326"},
}
CLAUSES = (
    (("aeu",), "ēa"), (("áeu",), "ēa"),
    (("eu",), "ēo"), (("éu",), "ēo"),
    (("iu",), "ēo"), (("íu",), "ēo"),
    (("e", "u"), "eo"), (("é", "u"), "éo"), (("i", "u"), "eo"),
)


def tokens(form):
    return re.findall(r"\*([^*]+)", form)


def trace_records():
    with (GERMANIC / "data/germanic-aligned-final.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        corpus = list(csv.DictReader(handle, delimiter="\t"))
    selected = {}
    for row in corpus:
        if row["DOCULECT"] == "Old_English":
            selected[row["CONCEPT"], row["PROTOFORM"]] = row["ID"]
    records = {}
    for block in re.split(r"\n--- ", TRACE.read_text(encoding="utf-8"))[1:]:
        concept = block.split(" ---", 1)[0]
        proto_match = re.search(r"^PROTO: (.+)$", block, re.MULTILINE)
        if proto_match is None:
            continue
        proto = proto_match[1]
        forms = dict(re.findall(
            r"^([A-Za-z][A-Za-z0-9]*)(?: \[no-change\])?: (.+)$",
            block, re.MULTILINE,
        ))
        records[selected[concept, proto]] = (concept, proto, forms)
    return records


class SC032AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = trace_records()

    def test_trace_is_fresh_and_complete(self):
        self.assertEqual(trace_provenance_problems(TRACE.read_text(encoding="utf-8")), [])
        self.assertEqual(len(self.records), 389)
        self.assertEqual({"2333", "2334"} <= set(self.records), True)
        for identifier in ("2333", "2334"):
            forms = self.records[identifier][2]
            self.assertEqual(forms["OEJGlideIO"], forms["OEDiphthongLeveling"])

    def test_nine_clauses_preserve_atomic_long_and_split_short_quantities(self):
        text = (GERMANIC / "fsts/germanic.txt").read_text(encoding="utf-8")
        body = text.split("define OEDiphthongLeveling [", 1)[1].split("];", 1)[0]
        body = re.sub(r"#[^\n]*", "", body)
        clauses = re.findall(
            r"((?:\{\*[^}]+\}\s*)+) -> \{\*([^}]+)\}", body,
        )
        actual = tuple((tuple(re.findall(r"\{\*([^}]+)\}", left)), right)
                       for left, right in clauses)
        self.assertEqual(actual, CLAUSES)
        self.assertNotIn((("í", "u"), "eo"), actual)

    def test_new_controls_preserve_released_recipe_pins_and_all_clause_checks(self):
        from anglo_frisian_experiments import load_recipes

        directory = SC / "literature_dossiers/anglo_frisian"
        controls = load_recipes(directory / "oe_sc032_controls.json")
        released = json.loads((directory / "oe_post_hue_controls.json").read_text(
            encoding="utf-8"))
        for field in ("baseline_fst_sha256", "baseline_corpus_sha256",
                      "baseline_context_sha256", "baseline_context_helper_sha256"):
            self.assertEqual(controls[field], released[field])
        recipe = controls["recipes"][1]
        self.assertFalse(any(recipe[field] for field in (
            "definitions", "insert_after", "insert_rule", "replace",
        )))
        self.assertEqual(len(recipe["component_checks"]), 16)
        for check, (left, right) in zip(recipe["component_checks"], CLAUSES):
            self.assertEqual((tokens(check["input"]), tokens(check["expected"])),
                             (list(left), [right]))

    def test_full_census_and_overlapping_clause_applications(self):
        populations = collections.defaultdict(set)
        for identifier, (_, _, forms) in self.records.items():
            before, after = forms["OEJGlideIO"], forms["OEDiphthongLeveling"]
            symbols = tokens(before)
            applications = []
            for left, right in CLAUSES:
                for position in range(len(symbols) - len(left) + 1):
                    if tuple(symbols[position:position + len(left)]) == left:
                        applications.append((position, left, right))
            self.assertEqual(bool(applications), before != after, identifier)
            self.assertLessEqual(len(applications), 1, identifier)
            if applications:
                position, left, right = applications[0]
                predicted = symbols[:position] + [right] + symbols[position + len(left):]
                self.assertEqual("*" + "*".join(predicted), after, identifier)
                populations["+".join(left)].add(identifier)
        self.assertEqual(dict(populations), EXPECTED)

    def test_original380_membership_is_not_the_immutable_old_input(self):
        with (SC / "cascade_baseline/cascade_baseline_outputs_legacy380.tsv").open(
            encoding="utf-8", newline=""
        ) as handle:
            legacy = {(row["concept"], row["proto"])
                      for row in csv.DictReader(handle, delimiter="\t")}
        firing_ids = set().union(*EXPECTED.values())
        original = {identifier for identifier in firing_ids
                    if self.records[identifier][:2] in legacy}
        self.assertEqual(original, firing_ids - {"2326"})

    def test_early_glide_feeders_retain_the_second_glide(self):
        for identifier, old, new in (
            ("1976", "*k*é*w*w*a*n*ą", "*k*éu*w*a*n*ą"),
            ("1989", "*d*á*w*w*ō", "*d*áu*w*ō"),
            ("2029", "*f*é*w*w*a*r", "*f*éu*w*a*r"),
            ("2074", "*x*á*w*w*a*n*ą", "*x*áu*w*a*n*ą"),
            ("2326", "*í*w*w*i*z", "*íu*w*i*z"),
        ):
            forms = self.records[identifier][2]
            self.assertEqual(forms["PWGmcCoronalWAssimilation"], old)
            self.assertEqual(forms["OEWWSimplification"], new)
            self.assertIn("*w", forms["OEDiphthongLeveling"])

    def test_contraction_and_prosodic_controls_remain_distinct(self):
        friend = self.records["2033"][2]
        self.assertEqual(friend["PWGmcIjContraction"], "*f*r*íu*n*d*z")
        you = self.records["2326"][2]
        self.assertEqual(you["PWGmcUnstressedWordFinalIApocope"], "*íu*w")
        self.assertEqual(you["OEDiphthongLeveling"], "*ēo*w")
        self.assertEqual(you["OEIUmlaut"], "*ēo*w")

    def test_hue_knee_and_singleton_aw_are_negative_controls(self):
        hue = self.records["2332"][2]
        self.assertEqual(hue["OEEwLongDiphthong"], "*x*íu*w*j*ą")
        self.assertEqual(hue["OEJGlideIO"], "*x*īo*w*j*ą")
        self.assertEqual(hue["OEDiphthongLeveling"], "*x*īo*w*j*ą")
        self.assertEqual(hue["OEIUmlaut"], "*ç*īe*w*j")
        knee = self.records["2085"][2]
        self.assertEqual(knee["OEDiphthongLeveling"], "*k*n*é*w*ē")
        self.assertEqual(knee["OEBreaking"], "*k*n*éo*w*ē")
        for identifier in ("2186", "2317", "2318"):
            forms = self.records[identifier][2]
            self.assertEqual(forms["OEJGlideIO"], forms["OEDiphthongLeveling"])
        straw = self.records["2224"][2]
        self.assertEqual(straw["PWGmcEndinglessAw"], "*s*t*r*áu")
        self.assertEqual(straw["OEJGlideIO"], "*s*t*r*áeu")
        self.assertEqual(straw["OEDiphthongLeveling"], "*s*t*r*ēa")

    def test_head_dependency_is_internal_vowel_recognition(self):
        text = (GERMANIC / "fsts/germanic.txt").read_text(encoding="utf-8")
        vocalic = text.split("define PGmcStarVocalic [", 1)[1].split("];", 1)[0]
        self.assertEqual(re.sub(r"\s+", "", vocalic),
                         "PGmcStarVowel|PGmcStarDiphthong")
        members = "".join(text.split(f"define {name} [", 1)[1].split("];", 1)[0]
                          for name in ("PGmcStarVowel", "PGmcStarDiphthong"))
        self.assertNotIn("{*aeu}", members)
        self.assertNotIn("{*áeu}", members)
        self.assertIn("{*ēa}", members)
        self.assertIn("define EnglishStarVocalic PGmcStarVocalic;", text)
        head = self.records["2063"][2]
        self.assertEqual(head["OEDiphthongLeveling"], "*x*ēa*b*u*d*ą")
        self.assertEqual(head["OEMedUnstressedULowering"], "*ç*ēa*β*o*d")

    def test_registry_verdict_and_component_scoped_chronology(self):
        row = next(row for row in read_tsv(SC_REGISTRY) if row["sc_id"] == "SC032")
        self.assertEqual((row["adjudication_status"], row["verdict"]),
                         ("adjudicated", "REFORMULATE"))
        self.assertEqual((row["hist_stage"], row["hist_scope"]), ("oe", "english_specific"))
        edges = {(row["source_change_id"], row["target_change_id"]): row
                 for row in read_tsv(EDGE_REGISTRY)}
        head = edges["SC032", "SC040"]
        self.assertEqual((head["relation_type"], head["evidence_basis"]),
                         ("technical_computational", "technical"))
        for source in ("SC030", "SC031"):
            edge = edges[source, "SC032"]
            self.assertEqual((edge["evidence_basis"], edge["witness_role"]),
                             ("independently_demonstrated", "feeding"))


if __name__ == "__main__":
    unittest.main()
