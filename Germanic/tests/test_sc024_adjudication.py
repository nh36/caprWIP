#!/usr/bin/env python3
"""Regression for the *ē₁-complex re-adjudication (SC024/SC025/SC101, 2026).

Governing memo:
Germanic/docs/sound_changes/audits/sc024-sc025-sc101-e1-complex-adjudication.md
(supersedes in implementation sc024-adjudication.md).

Protected scientific conclusions:

  * Change A exists independently: SC024 `PNWGmcLongELowering` is
    `{*ḗ} -> {*ā}` — stressed tier only, unconditioned (nasal forms
    included), producing the reconstructed intermediate *ā (R/T 2014
    pp. 11–13, *mānōþ-, *spānuz) — at executable position 12.
  * Change B exists independently and consumes the correct input:
    SC101 `EAFLongAFronting` is `{*ā} -> {*ǣ}` before non-nasal C, at
    position 27; SC025 `EAFLongANasalRounding` is `{*ā} -> {*ō}` before
    nasal, at position 26. Both are fed by SC024.
  * *ā < *ai arises too late to be fronted or rounded: SC004 stands at
    position 28, after both (Campbell §132; R/T pp. 169–170) — stone,
    home, loath, rope, token, soul, ghost keep back ā.
  * The old one-step `*ē/*ḗ -> *ǣ` telescoping must not silently return.
  * The five unstressed selected-input tokens (father, mother, sister,
    have, live) are NOT SC024 witnesses: their plain unstressed {*ē}
    passes the stressed rule untouched and takes the §6.8.3
    unstressed-shortening path, still surfacing short (fæder etc.).
  * SC101 < SC056: WS palatal diphthongization operated on the
    already-fronted vowel (sheep sċēap, year ġēar).
  * Canonical registry metadata matches each distinct historical change
    (SC024 pnwgmc/pan_pnwgmc; SC025 and SC101 eaf/north_sea_germanic;
    all confidence B) and each has its own reader-facing write-up.

Run: cd Germanic/tests && python3 -m unittest test_sc024_adjudication
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
CARDS = SC_DIR / "order_tests" / "chronology_cards"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
MEMO = SC_DIR / "audits" / "sc024-sc025-sc101-e1-complex-adjudication.md"
OLD_MEMO = SC_DIR / "audits" / "sc024-adjudication.md"
READER = SC_DIR / "reader_facing"
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"

# Change A census: 13 stressed oral roots + the two nasal-branch lexemes,
# which historically DID undergo *ē₁ > *ā (R/T p. 11: *mānōþ-, *spānuz).
ORAL_ROOT_CONCEPTS = {
    "adder", "bier", "deed", "eel", "hair", "let", "meal", "needle",
    "read", "sheep", "sleep", "weapon", "year",
}
NASAL_BRANCH_CONCEPTS = {"month", "spoon"}
SC024_FIRING_CONCEPTS = ORAL_ROOT_CONCEPTS | NASAL_BRANCH_CONCEPTS

# Unstressed selected-input tokens: plain {*ē}, outside the stressed law.
UNSTRESSED_CONCEPTS = {"father", "mother", "sister", "have", "live"}
UNSTRESSED_ATTESTED = {
    "father": "fæder", "mother": "mōder", "sister": "swester",
    "have": "hæfeþ", "live": "lifeþ",
}

# ā < *ai negative controls (never fronted/rounded).
AI_BRANCH_CONTROLS = {"stone": "stān", "home": "hām"}


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


class E1ComplexAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
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

    def across_sc024(self, form):
        before = self.stage("pwgmc_dental_hardening", form)
        after = self.stage("pnwgmc_long_e_lowering", form)
        return before, after

    def across_rounding(self, form):
        before = self.stage("pnwgmc_preconsonantal_x_loss", form)
        after = self.stage("eaf_long_a_nasal_rounding", form)
        return before, after

    def across_fronting(self, form):
        before = self.stage("eaf_long_a_nasal_rounding", form)
        after = self.stage("eaf_long_a_fronting", form)
        return before, after

    # ------------------------------------------------------------------
    # Executable rules: two changes, correct inputs and outputs
    # ------------------------------------------------------------------

    def test_change_a_is_unconditioned_stressed_lowering_to_a(self):
        match = re.search(
            r"define\s+PNWGmcLongELowering\s*\[\s*\{\*ḗ\}\s*->\s*\{\*ā\}\s*\];",
            self.uncommented,
        )
        self.assertIsNotNone(
            match,
            "SC024 must be the unconditioned stressed lowering "
            "{*ḗ} -> {*ā} (Change A of the e1 complex)",
        )

    def test_change_b_rules_consume_long_a(self):
        self.assertIsNotNone(re.search(
            r"define\s+EAFLongANasalRounding\s*\[\s*\{\*ā\}\s*->\s*\{\*ō\}"
            r"\s*\|\|\s*_\s*EnglishStarNasal\s*\];",
            self.uncommented,
        ), "SC025 must round the historical *ā before nasals")
        self.assertIsNotNone(re.search(
            r"define\s+EAFLongAFronting\s*\[\s*\{\*ā\}\s*->\s*\{\*ǣ\}"
            r"\s*\|\|\s*_\s*\[EnglishStarConsonant\s*-\s*EnglishStarNasal\]\s*\];",
            self.uncommented,
        ), "SC101 must front the historical non-nasalized *ā")

    def test_one_step_telescoping_cannot_silently_return(self):
        self.assertIsNone(
            re.search(r"\{\*ē\}\s*->\s*\{\*ǣ\}|\{\*ḗ\}\s*->\s*\{\*ǣ\}",
                      self.uncommented),
            "the retired one-step *ē/*ḗ -> *ǣ telescoping has returned",
        )
        self.assertIsNone(
            re.search(r"\{\*ē\}\s*->\s*\{\*ō\}|\{\*ḗ\}\s*->\s*\{\*ō\}",
                      self.uncommented),
            "the retired direct *ē -> *ō nasal bypass has returned",
        )

    def test_cascade_positions_encode_the_chronology(self):
        self.assertEqual(self.positions.get("PNWGmcLongELowering"), 12)
        self.assertEqual(self.positions.get("EAFLongANasalRounding"), 26)
        self.assertEqual(self.positions.get("EAFLongAFronting"), 27)
        self.assertEqual(self.positions.get("EAFAiMonophthongization"), 28)
        # SC101 < SC056 (sheep/year: diphthongization of already-fronted ǣ)
        self.assertLess(self.positions["EAFLongAFronting"],
                        self.positions["OEWsPalatalDiphthongization"])

    # ------------------------------------------------------------------
    # Change A firing census (live stage bins)
    # ------------------------------------------------------------------

    def test_change_a_fires_on_exactly_the_15_stressed_e1_lexemes(self):
        fired = set()
        candidates = {
            concept: row for concept, row in self.baseline.items()
            if ("ē" in row["proto"] or "ḗ" in row["proto"])
        }
        for concept, row in sorted(candidates.items()):
            before, after = self.across_sc024(row["proto"].lstrip("*"))
            if before != after:
                fired.add(concept)
        self.assertEqual(
            fired,
            SC024_FIRING_CONCEPTS,
            "SC024 (Change A) census drifted; expected the 13 stressed "
            "oral roots plus month and spoon (which pass through *ā)",
        )

    def test_change_a_produces_the_reconstructed_intermediate_a(self):
        self.assertEqual(
            self.across_sc024("skḗpą"), (["*s*k*ḗ*p*ą"], ["*s*k*ā*p*ą"])
        )
        self.assertEqual(
            self.across_sc024("mḗnōθz"), (["*m*ḗ*n*ō*θ*z"], ["*m*ā*n*ō*θ*z"])
        )
        self.assertEqual(
            self.across_sc024("spḗnuz"), (["*s*p*ḗ*n*u*z"], ["*s*p*ā*n*u*z"])
        )

    def test_unstressed_tokens_do_not_fire_and_surface_short(self):
        for concept in sorted(UNSTRESSED_CONCEPTS):
            row = self.baseline[concept]
            before, after = self.across_sc024(row["proto"].lstrip("*"))
            self.assertEqual(
                before, after,
                f"{concept} carries unstressed *ē and must not undergo "
                "the stressed lowering (R/T p. 13 n. 3)",
            )
            self.assertEqual(
                row["outputs"], UNSTRESSED_ATTESTED[concept],
                f"{concept} must still surface with its short unstressed "
                "vowel via the §6.8.3 shortening path",
            )

    # ------------------------------------------------------------------
    # Change B: rounding and fronting consume the *ā
    # ------------------------------------------------------------------

    def test_nasal_branch_rounds_the_intermediate_a(self):
        for concept in sorted(NASAL_BRANCH_CONCEPTS):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            before, after = self.across_rounding(form)
            self.assertNotEqual(
                before, after,
                f"{concept} must be rounded by SC025 EAFLongANasalRounding",
            )
            self.assertIn("*ō", after[0])
        self.assertEqual(self.baseline["month"]["outputs"], "mōnaþ")
        self.assertEqual(self.baseline["spoon"]["outputs"], "spōn")

    def test_oral_branch_fronts_the_intermediate_a(self):
        self.assertEqual(
            self.across_fronting("skāpą"), (["*s*k*ā*p*ą"], ["*s*k*ǣ*p*ą"])
        )
        self.assertEqual(
            self.across_fronting("jārą"), (["*j*ā*r*ą"], ["*j*ǣ*r*ą"])
        )
        self.assertEqual(self.baseline["sheep"]["outputs"], "sċēap")
        self.assertEqual(self.baseline["year"]["outputs"], "ġēar")

    def test_a_from_ai_arises_too_late_to_front_or_round(self):
        for concept, attested in sorted(AI_BRANCH_CONTROLS.items()):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            # untouched by A (no *ē₁), by rounding and by fronting
            # (its ā does not exist yet at positions 26–27)
            for probe in (self.across_sc024, self.across_rounding,
                          self.across_fronting):
                before, after = probe(form)
                self.assertEqual(
                    before, after,
                    f"{concept} ({row['proto']}) has *ai, whose ā arises "
                    "only at SC004; it must pass positions 12/26/27 untouched",
                )
            self.assertEqual(row["outputs"], attested)

    # ------------------------------------------------------------------
    # Canonical registry metadata
    # ------------------------------------------------------------------

    def test_registry_metadata_matches_the_two_change_architecture(self):
        registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        sc024, sc025, sc101 = registry["SC024"], registry["SC025"], registry["SC101"]
        self.assertEqual(sc024["fst_identifier"], "PNWGmcLongELowering")
        self.assertEqual(sc024["hist_stage"], "pnwgmc")
        self.assertEqual(sc024["hist_scope"], "pan_pnwgmc")
        self.assertEqual(sc024["verdict"], "SPLIT/REFORMULATE/REORDER")
        self.assertEqual(sc025["fst_identifier"], "EAFLongANasalRounding")
        self.assertEqual(sc025["hist_stage"], "eaf")
        self.assertEqual(sc025["hist_scope"], "north_sea_germanic")
        self.assertEqual(sc025["verdict"], "REFORMULATE/REORDER")
        self.assertEqual(sc101["fst_identifier"], "EAFLongAFronting")
        self.assertEqual(sc101["hist_stage"], "eaf")
        self.assertEqual(sc101["hist_scope"], "north_sea_germanic")
        self.assertEqual(sc101["verdict"], "SPLIT")
        for row in (sc024, sc025, sc101):
            self.assertEqual(row["confidence"], "B",
                             "the two-step reconstruction is disputed "
                             "(Fulk 2018 §4.6); confidence must stay B")
            self.assertEqual(row["adjudication_status"], "adjudicated")
            self.assertIn("sc024-sc025-sc101-e1-complex-adjudication.md",
                          row["adjudication_memo"])

    def test_staging_map_view_matches(self):
        staging = {r["sc_id"]: r for r in _tsv_rows(STAGING_MAP)}
        self.assertEqual(staging["SC024"]["hist_stage"], "pnwgmc")
        self.assertEqual(staging["SC025"]["fst_identifier"],
                         "EAFLongANasalRounding")
        self.assertEqual(staging["SC101"]["fst_identifier"],
                         "EAFLongAFronting")

    def test_rename_manifest_records_the_sc025_second_migration(self):
        rename = {r["sc_id"]: r for r in _tsv_rows(RENAME_MANIFEST)}
        self.assertEqual(rename["SC025"]["canonical_foma_identifier"],
                         "EAFLongANasalRounding")
        self.assertEqual(rename["SC025"]["canonical_hist_stage"], "eaf")
        self.assertEqual(rename["SC024"]["canonical_hist_stage"], "pnwgmc")

    # ------------------------------------------------------------------
    # Chronology edges
    # ------------------------------------------------------------------

    def edge(self, src, tgt):
        rows = [r for r in _tsv_rows(EDGES)
                if r["source_change_id"] == src
                and r["target_change_id"] == tgt]
        self.assertEqual(len(rows), 1, f"expected exactly one {src}->{tgt} edge")
        return rows[0]

    def test_feeding_edges_from_change_a(self):
        for tgt in ("SC025", "SC101"):
            edge = self.edge("SC024", tgt)
            self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
            self.assertEqual(edge["relation_type"], "one_sided_chronology")

    def test_pre_sc004_edges_encode_campbell_132(self):
        self.assertEqual(self.edge("SC025", "SC004")["representative_lexemes"],
                         "stone; home")
        self.assertIn("ghost", self.edge("SC101", "SC004")["representative_lexemes"])

    def test_sheep_year_sc056_edge_now_attaches_to_sc101(self):
        edge = self.edge("SC101", "SC056")
        self.assertEqual(edge["representative_lexemes"], "sheep; year")
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertFalse(
            [r for r in _tsv_rows(EDGES)
             if r["source_change_id"] == "SC024"
             and r["target_change_id"] == "SC056"],
            "the old SC024->SC056 edge must not survive; it belongs to SC101",
        )

    def test_earlier_side_of_change_a_stays_runner_limited(self):
        edge = self.edge("SC024", "PWGmcChanges")
        self.assertEqual(edge["relation_type"], "runner_limited_boundary")
        self.assertIn("not a lower boundary", edge["notes"])

    # ------------------------------------------------------------------
    # Memos and reader-facing write-ups
    # ------------------------------------------------------------------

    def test_governing_memo_and_supersession(self):
        memo = MEMO.read_text(encoding="utf-8")
        self.assertTrue(memo.splitlines()[2].startswith(
            "Registry-verdict: SC024=SPLIT/REFORMULATE/REORDER; "
            "SC025=REFORMULATE/REORDER; SC101=SPLIT"))
        old = OLD_MEMO.read_text(encoding="utf-8")
        self.assertIn("SUPERSEDED IN IMPLEMENTATION", old)

    def test_each_change_has_its_own_reader_chapter(self):
        for fname, anchor, cite in (
            ("024-long-e-lowering.md", "{#rule-PNWGmcLongELowering}",
             "[@RingeTaylor2014, pp. 11--13]"),
            ("025-long-a-nasal-rounding.md", "{#rule-EAFLongANasalRounding}",
             "[@RingeTaylor2014, pp. 150--152]"),
            ("101-long-a-fronting.md", "{#rule-EAFLongAFronting}",
             "[@RingeTaylor2014, pp. 146--150"),
        ):
            text = (READER / fname).read_text(encoding="utf-8")
            self.assertIn(anchor, text, fname)
            self.assertIn(cite, text, f"{fname} must cite its sources")
        # the dispute must be recorded, not suppressed
        self.assertIn("@Fulk2018",
                      (READER / "024-long-e-lowering.md").read_text(encoding="utf-8"))

    def test_chronology_cards_exist_for_all_three(self):
        for fname in ("SC024-nwgmc-long-e-lowering.md",
                      "SC025-eaf-long-a-nasal-rounding.md",
                      "SC101-eaf-long-a-fronting.md"):
            card = (CARDS / fname).read_text(encoding="utf-8")
            self.assertIn("sc024-sc025-sc101-e1-complex-adjudication.md", card)


if __name__ == "__main__":
    unittest.main()
