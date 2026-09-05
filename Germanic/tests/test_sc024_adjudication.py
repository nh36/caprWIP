#!/usr/bin/env python3
"""Focused regression for the SC024 historical adjudication (2026).

Adjudication memo: Germanic/docs/sound_changes/audits/sc024-adjudication.md

Protected invariants:

  * The executable rule `PNWGmcLongELowering` is unchanged (stable
    identifier; `{*ē}/{*ḗ} -> {*ǣ}` before a non-nasal consonant) and
    remains at executable cascade slot 22.
  * Its live firing population is exactly 18 lexemes: 13 in-domain
    stressed root *ē₁ witnesses plus 5 unstressed selected-input proxies
    (father, mother, sister, have, live). Any drift forces
    re-adjudication.
  * The nasal branch is complementary, not overlapping: `month`
    (`*mḗnōθz`) and `spoon` (`*spḗnuz`) must pass SC024 untouched and be
    changed by SC025 `PNWGmcLongENasalRounding` instead (> ō: mōnaþ,
    spōn).
  * `ā < *ai` is never fronted: `stone` (`*stáinaz`) and `home`
    (`*xáimaz`) pass SC024 untouched and surface with ā (stān, hām).
    The Campbell §132 / R&T pp. 169–170 ordering (fronting before
    completion of *ai > ā) is encoded architecturally by symbol
    separation, and this disjointness is what these controls pin.
  * The five unstressed proxy firings surface with SHORT vowels
    (fæder, mōder, swester, hæfeþ, lifeþ) — their ǣ is an internal
    implementation pathway, not a claim that unstressed *ē took the
    stressed detour.
  * Canonical historical metadata says early Anglo-Frisian scope for the
    fronted outcome (`eaf` / `anglo_frisian`), not pan-Northwest-Germanic,
    even though the executable identifier keeps the `PNWGmc` prefix
    (stage comes from metadata, not the name prefix).

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
CARD = SC_DIR / "order_tests" / "chronology_cards" / "SC024-nwgmc-long-e-lowering.md"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
MEMO = SC_DIR / "audits" / "sc024-adjudication.md"
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"

# The adjudicated firing population (sc024-adjudication.md §3).
IN_DOMAIN_CONCEPTS = {
    "adder", "bier", "deed", "eel", "hair", "let", "meal", "needle",
    "read", "sheep", "sleep", "weapon", "year",
}
UNSTRESSED_PROXY_CONCEPTS = {"father", "mother", "sister", "have", "live"}
EXPECTED_FIRING_CONCEPTS = IN_DOMAIN_CONCEPTS | UNSTRESSED_PROXY_CONCEPTS

# Nasal-branch negative controls: same vowel, nasal environment -> SC025.
NASAL_BRANCH_CONCEPTS = {"month", "spoon"}

# *ai-branch negative controls: ā < *ai must never be fronted.
AI_BRANCH_CONTROLS = {"stone": "stān", "home": "hām"}

# Unstressed proxies surface with short vowels (no stressed detour).
PROXY_ATTESTED = {
    "father": "fæder", "mother": "mōder", "sister": "swester",
    "have": "hæfeþ", "live": "lifeþ",
}


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


class SC024AdjudicationTests(unittest.TestCase):
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

    def before_after(self, form):
        before = self.stage("pnwgmc_n_stem_n_loss", form)
        after = self.stage("pnwgmc_long_e_lowering", form)
        return before, after

    # ------------------------------------------------------------------
    # Executable rule stability
    # ------------------------------------------------------------------

    def test_rule_definition_is_unchanged(self):
        match = re.search(
            r"define\s+PNWGmcLongELowering\s*\[\s*"
            r"\{\*ē\}\s*->\s*\{\*ǣ\}\s*\|\|\s*_\s*"
            r"\[EnglishStarConsonant\s*-\s*EnglishStarNasal\]\s*,\s*"
            r"\{\*ḗ\}\s*->\s*\{\*ǣ\}\s*\|\|\s*_\s*"
            r"\[EnglishStarConsonant\s*-\s*EnglishStarNasal\]\s*\];",
            self.uncommented,
        )
        self.assertIsNotNone(
            match,
            "PNWGmcLongELowering must stay the byte-stable one-step "
            "{*ē}/{*ḗ} -> {*ǣ} non-nasal proxy (sc024-adjudication.md §2)",
        )

    def test_rule_position_is_22_and_inventory_order_24(self):
        self.assertEqual(self.positions.get("PNWGmcLongELowering"), 22)
        inventory = {r["change_id"]: r for r in _tsv_rows(INVENTORY)}
        self.assertEqual(inventory["SC024"]["current_order"], "24")

    # ------------------------------------------------------------------
    # Firing population pinned (live stage bins)
    # ------------------------------------------------------------------

    def test_firing_population_is_exactly_the_18_adjudicated_lexemes(self):
        fired = set()
        # A live firing requires a literal long-e symbol; no earlier
        # cascade rule creates {*ē}/{*ḗ}, so protos containing one are an
        # exhaustive candidate set (the full --evidence census over all
        # 383 rows finds the same 18).
        candidates = {
            concept: row for concept, row in self.baseline.items()
            if ("ē" in row["proto"] or "ḗ" in row["proto"])
        }
        for concept, row in sorted(candidates.items()):
            before, after = self.before_after(row["proto"].lstrip("*"))
            if before != after:
                fired.add(concept)
        self.assertEqual(
            fired,
            EXPECTED_FIRING_CONCEPTS,
            "SC024 firing population drifted; any change forces "
            "re-adjudication (see sc024-adjudication.md §3)",
        )

    def test_sheep_and_year_are_live_in_domain_witnesses(self):
        self.assertEqual(
            self.before_after("skḗpą"), (["*s*k*ḗ*p*ą"], ["*s*k*ǣ*p*ą"])
        )
        self.assertEqual(
            self.before_after("jḗrą"), (["*j*ḗ*r*ą"], ["*j*ǣ*r*ą"])
        )
        self.assertEqual(self.baseline["sheep"]["outputs"], "sċēap")
        self.assertEqual(self.baseline["year"]["outputs"], "ġēar")

    # ------------------------------------------------------------------
    # Nasal branch: complementary conditioning, handled by SC025
    # ------------------------------------------------------------------

    def test_nasal_environment_is_untouched_by_sc024_and_taken_by_sc025(self):
        for concept in sorted(NASAL_BRANCH_CONCEPTS):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            before, after = self.before_after(form)
            self.assertEqual(
                before, after,
                f"{concept} ({row['proto']}) is nasal-branch (SC025) and "
                "must pass SC024 untouched",
            )
            rounded = self.stage("pnwgmc_long_e_nasal_rounding", form)
            self.assertNotEqual(
                after, rounded,
                f"{concept} must be changed by SC025 PNWGmcLongENasalRounding",
            )
            self.assertIn("*ō", rounded[0])
        self.assertEqual(self.baseline["month"]["outputs"], "mōnaþ")
        self.assertEqual(self.baseline["spoon"]["outputs"], "spōn")

    # ------------------------------------------------------------------
    # ā < *ai is never fronted (architectural encoding of Campbell §132)
    # ------------------------------------------------------------------

    def test_ai_monophthongization_outputs_keep_a(self):
        for concept, attested in sorted(AI_BRANCH_CONTROLS.items()):
            row = self.baseline[concept]
            form = row["proto"].lstrip("*")
            before, after = self.before_after(form)
            self.assertEqual(
                before, after,
                f"{concept} ({row['proto']}) has *ai, not *ē₁; SC024 must "
                "not touch it",
            )
            self.assertEqual(
                row["outputs"], attested,
                f"{concept} must surface with unfronted ā ({attested})",
            )

    # ------------------------------------------------------------------
    # Unstressed proxies: implementation pathway, short attested vowels
    # ------------------------------------------------------------------

    def test_unstressed_proxy_firings_surface_with_short_vowels(self):
        for concept, attested in sorted(PROXY_ATTESTED.items()):
            row = self.baseline[concept]
            before, after = self.before_after(row["proto"].lstrip("*"))
            self.assertNotEqual(
                before, after,
                f"{concept} is a documented unstressed proxy firing",
            )
            self.assertEqual(
                row["outputs"], attested,
                f"{concept} must surface with a short unstressed vowel "
                f"({attested}); the SC024 ǣ is an internal pathway only",
            )

    # ------------------------------------------------------------------
    # Canonical metadata: Anglo-Frisian scope, not the name prefix
    # ------------------------------------------------------------------

    def test_staging_map_says_anglo_frisian(self):
        row = {r["sc_id"]: r for r in _tsv_rows(STAGING_MAP)}["SC024"]
        self.assertEqual(row["hist_stage"], "eaf")
        self.assertEqual(row["hist_scope"], "anglo_frisian")
        self.assertEqual(row["display_name"],
                         "Long E Lowering with Anglo-Frisian Fronting")
        self.assertEqual(row["action_status"], "metadata_corrected")
        self.assertEqual(row["fst_identifier"], "PNWGmcLongELowering")

    def test_inventory_is_adjudicated_with_corrected_stage(self):
        row = {r["change_id"]: r for r in _tsv_rows(INVENTORY)}["SC024"]
        self.assertEqual(row["historical_stage"], "Early Anglo-Frisian")
        self.assertEqual(row["literature_status"], "adjudicated")
        self.assertEqual(row["trace_occurrence_count"], "18")
        self.assertIn("Anglo-Frisian", row["notes"])
        self.assertIn("sc024-adjudication.md", row["notes"])

    def test_historical_audit_and_rename_manifest_are_corrected(self):
        audit = {r["sc_id"]: r for r in _tsv_rows(HISTORICAL_AUDIT)}["SC024"]
        rename = {r["sc_id"]: r for r in _tsv_rows(RENAME_MANIFEST)}["SC024"]
        self.assertEqual(audit["proposed_hist_stage"], "eaf")
        self.assertEqual(audit["proposed_hist_scope"], "anglo_frisian")
        self.assertEqual(rename["canonical_hist_stage"], "eaf")
        self.assertEqual(rename["canonical_hist_scope"], "anglo_frisian")
        self.assertEqual(rename["canonical_foma_identifier"],
                         "PNWGmcLongELowering")

    # ------------------------------------------------------------------
    # Chronology: edge interpretation pinned
    # ------------------------------------------------------------------

    def test_sc056_edge_is_independently_demonstrated_with_sheep_year(self):
        rows = [r for r in _tsv_rows(EDGES)
                if r["source_change_id"] == "SC024"
                and r["target_change_id"] == "SC056"]
        self.assertEqual(len(rows), 1)
        edge = rows[0]
        self.assertEqual(edge["evidence_basis"], "independently_demonstrated")
        self.assertEqual(edge["representative_lexemes"], "sheep; year")
        self.assertIn("sc024-adjudication.md", edge["notes"])

    def test_earlier_side_stays_runner_limited(self):
        rows = [r for r in _tsv_rows(EDGES)
                if r["source_change_id"] == "SC024"
                and r["target_change_id"] == "PWGmcChanges"]
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["relation_type"], "runner_limited_boundary")
        self.assertIn("not a lower boundary", rows[0]["notes"])

    def test_card_records_the_adjudicated_interpretation(self):
        card = CARD.read_text(encoding="utf-8")
        self.assertIn("sc024-adjudication.md", card)
        self.assertIn("independently demonstrated", card)
        self.assertIn("symbol separation", card)

    def test_memo_exists_with_matching_registry_verdict(self):
        memo = MEMO.read_text(encoding="utf-8")
        self.assertIn("Registry-verdict: SC024=REFORMULATE/RETAIN", memo)
        registry = {r["sc_id"]: r
                    for r in _tsv_rows(SC_DIR / "registry" / "sc_registry.tsv")}
        self.assertEqual(registry["SC024"]["verdict"], "REFORMULATE/RETAIN")
        self.assertEqual(registry["SC024"]["adjudication_status"], "adjudicated")


if __name__ == "__main__":
    unittest.main()
