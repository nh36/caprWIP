"""Freshness and content tests for the rule-coverage census.

The committed census (docs/sound_changes/cascade_baseline/
rule_coverage_census.tsv) must be regenerable byte-for-byte from the
committed full trace report, inventory, and cascade manifest, and the
corpus-maturation-01 coverage facts must hold:

  * SC097 is witnessed by who;
  * SC098 is witnessed by you;
  * SC008 witnesses include you;
  * SC021 remains disputed_or_research_issue (galgu declined);
  * every rule's coverage status is explicit ("every rule must fire" is
    deliberately NOT an invariant).
"""

import csv
import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
CENSUS = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
          / "rule_coverage_census.tsv")
TOOL = GERMANIC / "tools" / "rule_coverage_census.py"

VALID_STATUSES = {
    "witnessed",
    "synthetic_only",
    "historically_obscured",
    "disputed_or_research_issue",
}


def load_tool():
    spec = importlib.util.spec_from_file_location("rule_coverage_census", TOOL)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("rule_coverage_census", mod)
    spec.loader.exec_module(mod)
    return mod


def read_census():
    lines = [ln for ln in CENSUS.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return {r["sc_id"]: r for r in csv.DictReader(lines, delimiter="\t")}


class CensusFreshnessTests(unittest.TestCase):
    def test_committed_census_matches_regeneration(self):
        mod = load_tool()
        regenerated = mod.build_rows()
        committed = read_census()
        self.assertEqual(
            {r["sc_id"]: r for r in regenerated}, committed,
            "rule_coverage_census.tsv is stale: rerun "
            "python3 Germanic/tools/rule_coverage_census.py")

    def test_every_rule_has_explicit_valid_status(self):
        committed = read_census()
        self.assertGreaterEqual(len(committed), 80)
        for sc, row in committed.items():
            self.assertIn(row["coverage_status"], VALID_STATUSES, sc)

    def test_zero_firing_rules_carry_a_note(self):
        for sc, row in read_census().items():
            if int(row["corpus_firing_count"]) == 0:
                self.assertTrue(row["note"].strip(),
                                f"{sc}: zero-firing rule must cite its "
                                "validation or adjudication")


class CorpusMaturationCoverageTests(unittest.TestCase):
    def setUp(self):
        self.census = read_census()

    def test_sc097_witnessed_by_who(self):
        row = self.census["SC097"]
        self.assertEqual(row["coverage_status"], "witnessed")
        self.assertIn("who", row["lexical_witnesses"].split(", "))

    def test_sc098_witnessed_by_you(self):
        row = self.census["SC098"]
        self.assertEqual(row["coverage_status"], "witnessed")
        self.assertIn("you", row["lexical_witnesses"].split(", "))

    def test_sc008_witnesses_include_you(self):
        row = self.census["SC008"]
        self.assertEqual(row["coverage_status"], "witnessed")
        self.assertIn("you", row["lexical_witnesses"].split(", "))

    def test_sc021_disputed_galgu_declined(self):
        row = self.census["SC021"]
        self.assertEqual(row["coverage_status"],
                         "disputed_or_research_issue")
        self.assertIn("galgu", row["note"])

    def test_rhotacism_alias_resolves(self):
        # STAGE_ALIASES must keep SC003 witnessed even though the tracer
        # labels the stage "Rhotacism" rather than "EAFRhotacism".
        row = self.census["SC003"]
        self.assertEqual(row["coverage_status"], "witnessed")
        self.assertGreater(int(row["corpus_firing_count"]), 0)


if __name__ == "__main__":
    unittest.main()
