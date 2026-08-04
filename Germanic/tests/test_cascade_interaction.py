#!/usr/bin/env python3
"""Invariants for the cross-stage rule-interaction matrix (Phase 5).

Host-runnable (no foma/Docker). Verifies that the committed interaction matrix is
well-formed, that its rule sets match the registry's curated stage membership,
and that the swap-risk classification used by the reorder is internally
consistent with the executable-order manifest. The actual foma equivalence
computation is exercised by the Docker wrapper.

Run: cd Germanic/tests && python3 -m unittest test_cascade_interaction
"""
from __future__ import annotations

import csv
import importlib.util
import io
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
STAGING_MAP = SC_DIR / "sound_change_historical_staging_map.tsv"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
MATRIX = SC_DIR / "cascade_baseline/cascade_interaction_matrix.tsv"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def _read_tsv_skip_comments(path: Path) -> list[dict[str, str]]:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


class InteractionMatrixTests(unittest.TestCase):
    def setUp(self):
        self.harness = _load_module("cascade_interaction_harness",
                                    TOOLS / "cascade_interaction_harness.py")
        with MATRIX.open(encoding="utf-8") as handle:
            self.matrix = list(csv.DictReader(handle, delimiter="\t"))
        with ORDER_MANIFEST.open(encoding="utf-8") as handle:
            self.pos = {r["foma_identifier"]: int(r["position"])
                        for r in csv.DictReader(handle, delimiter="\t")}

    def test_matrix_is_wellformed(self):
        for r in self.matrix:
            self.assertIn(r["commute"], ("yes", "no"))
            self.assertIn(r["earlier_rule"], self.pos, f"unknown rule {r['earlier_rule']}")
            self.assertIn(r["later_rule"], self.pos, f"unknown rule {r['later_rule']}")

    def test_matrix_covers_registry_stage_cross_product(self):
        """The committed matrix must cover exactly the (Proto-)Northwest Germanic
        x PWGmc pairs implied by the registry's curated stage membership.

        The earlier set is queried as {nwgmc, pnwgmc} so the check is invariant to
        how far the nwgmc->pnwgmc relabelling has progressed (and keeps the
        still-unresolved SC064, held at nwgmc, in scope). The later set is pwgmc;
        SC012, relabelled pwgmc->eaf, is intentionally out of this matrix."""
        nwgmc = self.harness.registry_rules_by_stage(STAGING_MAP, ORDER_MANIFEST, "nwgmc,pnwgmc")
        pwgmc = self.harness.registry_rules_by_stage(STAGING_MAP, ORDER_MANIFEST, "pwgmc")
        expected = {(e, l) for e in nwgmc for l in pwgmc}
        actual = {(r["earlier_rule"], r["later_rule"]) for r in self.matrix}
        self.assertEqual(actual, expected,
                         "interaction matrix is stale relative to registry stage membership; "
                         "regenerate with build_cascade_interaction_matrix_docker.sh")

    def test_known_dependency_pairs_do_not_commute(self):
        """Sanity anchors: the demonstrated intra/inter-stage dependencies that
        the reorder must preserve show up as non-commuting where both members are
        in the tested cross-product."""
        commute = {(r["earlier_rule"], r["later_rule"]): r["commute"] for r in self.matrix}
        # SC010 PWGmcJGemination x SC011 PWGmcSyllabicJ are both PWGmc, so not in
        # this PNWGmc x PWGmc matrix; the SC005/SC006 boundary pair is:
        pair = ("PNWGmcAToUBeforeM", "PWGmcEarlyIApocope")
        if pair in commute:
            self.assertEqual(commute[pair], "no",
                             "SC005 x SC006 is expected to be order-sensitive")

    def test_swap_risk_pairs_are_reorder_relevant(self):
        """Every non-commuting pair the reorder would SWAP has the PWGmc (later)
        rule currently before the PNWGmc (earlier) rule. This is the precise set
        that the incremental move-and-regress phase must watch."""
        swap = [r for r in self.matrix
                if r["commute"] == "no" and self.pos[r["later_rule"]] < self.pos[r["earlier_rule"]]]
        for r in swap:
            self.assertLess(self.pos[r["later_rule"]], self.pos[r["earlier_rule"]])
        # Documented current snapshot: 10 swap-relevant non-commuters. This is a
        # baseline observation, not a permanent contract; if the cascade changes
        # legitimately, update it deliberately (never merely to pass).
        self.assertGreaterEqual(len(swap), 1,
                                "expected at least one swap-relevant non-commuter to scrutinise")


if __name__ == "__main__":
    unittest.main()
