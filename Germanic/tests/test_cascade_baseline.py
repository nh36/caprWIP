#!/usr/bin/env python3
"""Phase 1 baseline invariants for the historical-cascade-order project.

These tests are host-runnable (no foma/flookup/Docker required). They protect
the frozen baseline artifacts against accidental drift and prove that the
executable-order manifest is an exact, reproducible projection of the current
``germanic.txt`` composition.

The *output-hash* reproducibility contract (that two independent recompiles
produce the same ``outputs_sha256``) is verified by the Docker wrapper
``build_cascade_baseline_docker.sh`` because it requires the transducer; here we
verify the committed artifacts are internally consistent and that the manifest
regenerates identically from source.

Run: cd Germanic/tests && python3 -m unittest test_cascade_baseline
"""
from __future__ import annotations

import csv
import importlib.util
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
BASELINE_DIR = REPO_ROOT / "Germanic/docs/sound_changes/cascade_baseline"
OUTPUTS_TSV = BASELINE_DIR / "cascade_baseline_outputs.tsv"
SUMMARY_JSON = BASELINE_DIR / "cascade_baseline_summary.json"
ORDER_MANIFEST = BASELINE_DIR / "cascade_order_manifest.tsv"
FST_SOURCE = REPO_ROOT / "Germanic/fsts/germanic.txt"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


class BaselineArtifactTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(OUTPUTS_TSV.exists(), f"missing {OUTPUTS_TSV}")
        self.assertTrue(SUMMARY_JSON.exists(), f"missing {SUMMARY_JSON}")
        self.summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
        with OUTPUTS_TSV.open(encoding="utf-8") as handle:
            self.rows = list(csv.DictReader(handle, delimiter="\t"))

    def test_summary_partitions_are_consistent(self):
        s = self.summary
        self.assertEqual(s["accepted"] + s["rejected"], s["total_lexemes"],
                         "accepted + rejected must equal total")
        self.assertEqual(s["matched"] + s["mismatched"], s["total_lexemes"],
                         "matched + mismatched must equal total")

    def test_outputs_hash_is_sha256_hex(self):
        self.assertRegex(self.summary["outputs_sha256"], r"^[0-9a-f]{64}$")

    def test_row_count_matches_summary(self):
        self.assertEqual(len(self.rows), self.summary["total_lexemes"],
                         "per-lexeme row count must equal summary total")

    def test_per_row_flags_are_consistent_with_outputs(self):
        for r in self.rows:
            outs = [o for o in r["outputs"].split("|") if o] if r["outputs"] else []
            self.assertEqual(int(r["output_count"]), len(outs),
                             f"output_count mismatch for {r['proto_norm']!r}")
            self.assertEqual(r["accepted"] == "1", bool(outs),
                             f"accepted flag mismatch for {r['proto_norm']!r}")
            self.assertEqual(r["match"] == "1", r["counterpart"] in outs,
                             f"match flag mismatch for {r['proto_norm']!r}")

    def test_aggregate_flag_counts_match_summary(self):
        accepted = sum(1 for r in self.rows if r["accepted"] == "1")
        matched = sum(1 for r in self.rows if r["match"] == "1")
        ambiguous = sum(1 for r in self.rows if int(r["output_count"]) > 1)
        self.assertEqual(accepted, self.summary["accepted"])
        self.assertEqual(matched, self.summary["matched"])
        self.assertEqual(ambiguous, self.summary["ambiguous_outputs"])

    def test_rows_are_deterministically_sorted(self):
        keys = [(r["proto_norm"], r["counterpart"], r["concept"]) for r in self.rows]
        self.assertEqual(keys, sorted(keys),
                         "baseline rows must be sorted by (proto_norm, counterpart, concept)")


class OrderManifestTests(unittest.TestCase):
    def setUp(self):
        self.mod = _load_module("cascade_order_manifest", TOOLS / "cascade_order_manifest.py")
        self.assertTrue(ORDER_MANIFEST.exists(), f"missing {ORDER_MANIFEST}")
        with ORDER_MANIFEST.open(encoding="utf-8") as handle:
            self.rows = list(csv.DictReader(handle, delimiter="\t"))

    def test_manifest_matches_current_fst_source(self):
        """The committed manifest must be an exact projection of germanic.txt."""
        regenerated = self.mod.build_manifest(FST_SOURCE)
        committed = [
            {"position": r["position"], "foma_identifier": r["foma_identifier"],
             "origin_block": r["origin_block"]}
            for r in self.rows
        ]
        self.assertEqual(regenerated, committed,
                         "cascade_order_manifest.tsv is stale relative to germanic.txt; "
                         "regenerate with tools/cascade_order_manifest.py")

    def test_positions_are_contiguous(self):
        positions = [int(r["position"]) for r in self.rows]
        self.assertEqual(positions, list(range(1, len(positions) + 1)))

    def test_manifest_begins_with_pwgmc_block(self):
        pwgmc = [r for r in self.rows if r["origin_block"] == "EarlyEnglishLineChanges"]
        # The EarlyEnglishLineChanges block is expanded at the head of the pipeline, so its
        # members must occupy the first contiguous positions.
        head = self.rows[: len(pwgmc)]
        self.assertTrue(all(r["origin_block"] == "EarlyEnglishLineChanges" for r in head),
                        "EarlyEnglishLineChanges members must lead the executable order")

    def test_required_local_dependencies_hold_in_current_order(self):
        """Baseline sanity: the demonstrated local dependencies hold in the
        current (old) order. These same edges must be preserved by any reorder.

        SC005 PNWGmcAToUBeforeM < SC017 PNWGmcULowering
        SC010 PWGmcJGemination < SC011 PWGmcSyllabicJ
        SC019 PNWGmcFinalLongORaising < SC020 EAFFinalZDeletion (final-*z* deletion)
        """
        pos = {r["foma_identifier"]: int(r["position"]) for r in self.rows}
        pairs = [
            ("PNWGmcAToUBeforeM", "PNWGmcULowering"),
            ("PWGmcJGemination", "PWGmcSyllabicJ"),
            ("PNWGmcFinalLongORaising", "EAFFinalZDeletion"),
        ]
        for earlier, later in pairs:
            self.assertIn(earlier, pos, f"{earlier} missing from manifest")
            self.assertIn(later, pos, f"{later} missing from manifest")
            self.assertLess(pos[earlier], pos[later],
                            f"expected {earlier} before {later} in current cascade")


if __name__ == "__main__":
    unittest.main()
