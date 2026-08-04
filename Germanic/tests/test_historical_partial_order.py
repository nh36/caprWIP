#!/usr/bin/env python3
"""Invariants for the supported historical partial order (Phase 3).

Host-runnable. Verifies the curated partial-order edges use controlled
vocabularies, that every cascade-relevant edge is satisfied by the current
executable order (the scoping-note edge, explicitly not a cascade constraint, is
excluded), and that the cascade edges are acyclic. This encodes the pivotal
finding that the current rule sequence already honours every evidence-backed
historical constraint — so the adjudicated corrections are renames/metadata, not
moves.

Run: cd Germanic/tests && python3 -m unittest test_historical_partial_order
"""
from __future__ import annotations

import collections
import csv
import io
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
PARTIAL_ORDER = SC_DIR / "cascade_baseline/historical_partial_order.tsv"
ORDER_MANIFEST = SC_DIR / "cascade_baseline/cascade_order_manifest.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"

TYPE_VALUES = {"historical_stage", "historical_relative_chronology",
               "fst_dependency", "technical_dependency"}
CONFIDENCE_VALUES = {"A", "B", "C"}
_DEFINE_RE = re.compile(r"define\s+([A-Za-z][A-Za-z0-9_]*)")
_SCOPING_NOTE = "not a cascade constraint"


def _load_edges() -> list[dict[str, str]]:
    lines = [ln for ln in PARTIAL_ORDER.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return list(csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t"))


def _sc_to_position() -> dict[str, int]:
    with INVENTORY.open(encoding="utf-8") as handle:
        sc2foma = {}
        for r in csv.DictReader(handle, delimiter="\t"):
            m = _DEFINE_RE.search(r.get("rule_source_anchor", "") or "")
            if m:
                sc2foma[r["change_id"]] = m.group(1)
    with ORDER_MANIFEST.open(encoding="utf-8") as handle:
        pos = {r["foma_identifier"]: int(r["position"]) for r in csv.DictReader(handle, delimiter="\t")}
    # Rules not in EnglishProtoToOE (e.g. EAFRhotacism in PGmcConsonantRules)
    # are pre-pipeline -> position 0.
    return {sc: pos.get(foma, 0) for sc, foma in sc2foma.items()}


class PartialOrderTests(unittest.TestCase):
    def setUp(self):
        self.edges = _load_edges()
        self.pos = _sc_to_position()

    def test_controlled_vocabularies(self):
        for e in self.edges:
            self.assertIn(e["type_of_edge"], TYPE_VALUES, f"bad type: {e}")
            self.assertIn(e["confidence"], CONFIDENCE_VALUES, f"bad confidence: {e}")

    def test_edges_reference_known_rules(self):
        for e in self.edges:
            self.assertIn(e["earlier_sc"], self.pos, f"unknown earlier_sc {e['earlier_sc']}")
            self.assertIn(e["later_sc"], self.pos, f"unknown later_sc {e['later_sc']}")

    def test_cascade_edges_hold_in_current_order(self):
        """Every cascade-relevant edge is already satisfied by the current
        executable order. The scoping-note edge is excluded by design."""
        violations = []
        for e in self.edges:
            if _SCOPING_NOTE in e["evidence"]:
                continue
            a, b = self.pos[e["earlier_sc"]], self.pos[e["later_sc"]]
            # a == 0 means pre-pipeline (before all EnglishProtoToOE positions).
            if not (a < b or a == 0):
                violations.append((e["earlier_sc"], e["later_sc"], a, b))
        self.assertEqual(violations, [],
                         f"current cascade violates supported historical edges: {violations}")

    def test_cascade_edges_are_acyclic(self):
        adj = collections.defaultdict(list)
        for e in self.edges:
            if _SCOPING_NOTE in e["evidence"]:
                continue
            adj[e["earlier_sc"]].append(e["later_sc"])
        color = collections.defaultdict(int)  # 0 white, 1 gray, 2 black
        cycle = [False]

        def dfs(u):
            color[u] = 1
            for v in adj[u]:
                if color[v] == 1:
                    cycle[0] = True
                elif color[v] == 0:
                    dfs(v)
            color[u] = 2

        for node in list(adj):
            if color[node] == 0:
                dfs(node)
        self.assertFalse(cycle[0], "supported partial order contains a cycle")

    def test_scoping_note_edge_is_documented(self):
        """The one historical edge that runs counter to the current cascade order
        must be explicitly marked as implemented via scoping, not ordering."""
        counter = [e for e in self.edges
                   if self.pos[e["earlier_sc"]] and self.pos[e["later_sc"]]
                   and self.pos[e["earlier_sc"]] > self.pos[e["later_sc"]]]
        for e in counter:
            self.assertIn(_SCOPING_NOTE, e["evidence"],
                          f"edge {e['earlier_sc']}->{e['later_sc']} runs counter to the cascade "
                          "but is not marked as a non-cascade (scoping) constraint")


if __name__ == "__main__":
    unittest.main()
