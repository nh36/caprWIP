#!/usr/bin/env python3
"""Focused regression for the SC023 scope/stage adjudication (2026).

Adjudication memo: Germanic/docs/sound_changes/audits/sc023-adjudication.md

Protected invariants:

  * The executable rule `PNWGmcNStemNLoss` is unchanged (stable identifier;
    `{*ō} {*n} -> {*ǭ} || _ .#.`) and remains at cascade position 23.
  * Its live firing population is exactly the 17 weak-noun citation stems in
    `*-ōn-`; any 18th firing (or any loss) forces re-adjudication.
  * The verb `do` (`*dōną`) does NOT undergo SC023 — it is a counterfeeding
    (negative) witness only: SC047 later strips `*ą` and the secondary final
    `-n` of `dōn` must survive.
  * PGmc `*sebun`/`*nigun`/`*tehun`/`*hebun-` keep final `-un` (numeral
    analogy, Ringe 2017: 103); the `{*ō}`-restricted proxy must never touch
    them.
  * Canonical historical metadata says (pre-)Proto-Germanic / pan-Germanic,
    not Northwest Germanic, even though the executable identifier keeps the
    `PNWGmc` prefix (stage comes from metadata, not the name prefix).

Run: cd Germanic/tests && python3 -m unittest test_sc023_adjudication
"""
from __future__ import annotations

import csv
import importlib.util
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
SC_DIR = GERMANIC / "docs" / "sound_changes"
BASELINE = SC_DIR / "cascade_baseline" / "cascade_baseline_outputs.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
HISTORICAL_AUDIT = SC_DIR / "cascade_baseline" / "historical_audit_table.tsv"
RENAME_MANIFEST = SC_DIR / "cascade_baseline" / "rename_migration_manifest.tsv"
CARD = SC_DIR / "order_tests" / "chronology_cards" / "SC023-nwgmc-n-stem-n-loss.md"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"

# The adjudicated firing population: weak-noun citation stems in *-ōn-.
EXPECTED_FIRING_CONCEPTS = {
    "adder", "earth", "flask", "heart", "line", "list", "nettle",
    "nightmare", "side", "sun", "swallow", "toe", "tongue", "wart",
    "weasel", "whore", "widow",
}

# -un# inputs that the (pre-)PGmc law's reconstructed lexicon already
# exempts (numeral analogy; Ringe 2017: 103) and the proxy must not touch.
UN_FINAL_CONCEPTS = {"seven", "nine", "ten", "heaven"}


def load_trace_tool():
    spec = importlib.util.spec_from_file_location("oe_full_trace_report", TRACE_TOOL)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def _tsv_rows(path: Path):
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class SC023AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        # Strip only full-line comments; inline stripping would mangle the
        # word-boundary symbol `.#.` inside rule bodies.
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.trace = load_trace_tool()
        with BASELINE.open(encoding="utf-8") as handle:
            cls.baseline = {
                row["concept"]: row
                for row in csv.DictReader(handle, delimiter="\t")
            }
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.positions = {
                row["foma_identifier"]: int(row["position"])
                for row in csv.DictReader(handle, delimiter="\t")
            }

    def stage(self, name, form):
        return self.trace.run_stage(
            BIN_DIR, f"old_english_sandbox_after_{name}.bin", form
        )

    # ------------------------------------------------------------------
    # Executable rule stability
    # ------------------------------------------------------------------

    def test_rule_definition_is_unchanged(self):
        match = re.search(
            r"define\s+PNWGmcNStemNLoss\s*\[\s*\{\*ō\}\s*\{\*n\}\s*->\s*\{\*ǭ\}"
            r"\s*\|\|\s*_\s*\.#\.\s*\];",
            self.uncommented,
        )
        self.assertIsNotNone(
            match,
            "PNWGmcNStemNLoss must stay the byte-stable {*ō}{*n} -> {*ǭ} / _ .#. proxy",
        )

    def test_rule_position_is_23(self):
        # Executable cascade slot is 21 since the SC021 retirement removed a
        # define; the stable identifier ordering (SC023) is asserted against
        # the inventory below.
        self.assertEqual(self.positions.get("PNWGmcNStemNLoss"), 21)
        inventory = {
            r["change_id"]: r for r in _tsv_rows(INVENTORY)
        }
        self.assertEqual(inventory["SC023"]["current_order"], "23")

    # ------------------------------------------------------------------
    # Firing population pinned (live stage bins)
    # ------------------------------------------------------------------

    def test_firing_population_is_exactly_the_17_weak_nouns(self):
        fired = set()
        candidates = {
            concept: row for concept, row in self.baseline.items()
            if row["proto"].endswith("n")
        }
        # Every possible live firing must involve a proto in final -n;
        # censusing only those rows keeps the test fast while remaining
        # exhaustive for this rule (a firing requires a final *ōn match).
        for concept, row in sorted(candidates.items()):
            form = row["proto"].lstrip("*")
            before = self.stage("pnwgmc_mn_dissimilation", form)
            after = self.stage("pnwgmc_n_stem_n_loss", form)
            if before != after:
                fired.add(concept)
        self.assertEqual(
            fired,
            EXPECTED_FIRING_CONCEPTS,
            "SC023 firing population drifted; any change forces re-adjudication "
            "(see sc023-adjudication.md)",
        )

    def test_do_is_not_a_live_application_and_don_keeps_secondary_n(self):
        row = self.baseline["do"]
        self.assertEqual(row["proto"], "*dōną")
        before = self.stage("pnwgmc_mn_dissimilation", "dōną")
        after = self.stage("pnwgmc_n_stem_n_loss", "dōną")
        self.assertEqual(before, after, "do must pass SC023 untouched")
        # Counterfeeding: SC047 creates the secondary final -n and it must
        # survive to the accepted output dōn.
        apocope = self.stage("oe_heavy_syllable_nasal_apocope", "dōną")
        self.assertEqual(apocope, ["*d*ō*n"])
        self.assertEqual(row["outputs"], "dōn")

    def test_un_final_words_are_untouched_by_sc023(self):
        for concept in sorted(UN_FINAL_CONCEPTS):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            before = self.stage("pnwgmc_mn_dissimilation", form)
            after = self.stage("pnwgmc_n_stem_n_loss", form)
            self.assertEqual(
                before, after,
                f"{concept} ({row['proto']}) retained -un must not undergo SC023",
            )

    def test_tongue_normalizes_citation_stem_to_nasalized_nom_sg(self):
        after = self.stage("pnwgmc_n_stem_n_loss", "túngōn")
        self.assertEqual(after, ["*t*ú*n*g*ǭ"])

    # ------------------------------------------------------------------
    # Canonical metadata: stage from metadata, not from the name prefix
    # ------------------------------------------------------------------

    def test_staging_map_says_proto_germanic(self):
        row = {r["sc_id"]: r for r in _tsv_rows(STAGING_MAP)}["SC023"]
        self.assertEqual(row["hist_stage"], "pgmc")
        self.assertEqual(row["hist_scope"], "pan_germanic")
        self.assertEqual(row["display_name"],
                         "Proto-Germanic Word-Final N Loss")
        self.assertEqual(row["action_status"], "metadata_corrected")
        self.assertEqual(row["fst_identifier"], "PNWGmcNStemNLoss")

    def test_inventory_says_proto_germanic_holding_zone(self):
        row = {r["change_id"]: r for r in _tsv_rows(INVENTORY)}["SC023"]
        self.assertEqual(row["stage"], "Proto-Germanic")
        self.assertEqual(row["historical_stage"], "Proto-Germanic")
        self.assertEqual(row["pipeline_stage"], "SC018-SC025 editorial holding zone")
        self.assertEqual(row["trace_occurrence_count"], "17")
        self.assertEqual(row["literature_status"], "adjudicated")
        self.assertIn("counterfeeding", row["notes"])

    def test_historical_audit_and_rename_manifest_are_corrected(self):
        audit = {r["sc_id"]: r for r in _tsv_rows(HISTORICAL_AUDIT)}["SC023"]
        rename = {r["sc_id"]: r for r in _tsv_rows(RENAME_MANIFEST)}["SC023"]
        self.assertEqual(audit["proposed_hist_stage"], "pgmc")
        self.assertEqual(audit["proposed_hist_scope"], "pan_germanic")
        self.assertEqual(audit["required_action"], "metadata_or_prose_only")
        self.assertEqual(rename["canonical_hist_stage"], "pgmc")
        self.assertEqual(rename["canonical_hist_scope"], "pan_germanic")
        self.assertEqual(rename["canonical_foma_identifier"], "PNWGmcNStemNLoss")

    def test_chronology_card_narrates_do_as_counterfeeding_negative_witness(self):
        card = CARD.read_text(encoding="utf-8")
        self.assertIn("counterfeeding", card)
        self.assertIn("negative", card)
        self.assertIn("sc023-adjudication.md", card)
        self.assertNotIn("must feed the later apocope", card)
        # The card must not present the stage as Northwest Germanic.
        self.assertNotIn("# SC023 NWGmc", card)


if __name__ == "__main__":
    unittest.main()
