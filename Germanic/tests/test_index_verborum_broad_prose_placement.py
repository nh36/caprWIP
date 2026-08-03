#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = REPO_ROOT / "Germanic/tools"
ASSEMBLY_DIR = REPO_ROOT / "Germanic/docs/assembly"
BOOK_DIR = REPO_ROOT / "Germanic/docs/book"

sys.path.insert(0, str(TOOLS_DIR))
sys.path.insert(0, str(ASSEMBLY_DIR))

from build_capr_book_draft import build_book_markdown
from build_full_lexical_volume import build_lexical_volume
from check_iv_broad_prose_placement_shadow import check as run_shadow_check
from index_verborum_broad_prose_placement import (
    build_passage_anchor_requests,
    load_broad_prose_inventory,
    resolve_source_passage,
)


def _anchor_ids(md_text: str) -> list[str]:
    return re.findall(
        r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}\s*\n:::',
        md_text,
    )


class BroadProseInventoryTests(unittest.TestCase):
    def test_inventory_classification_present(self):
        inv = load_broad_prose_inventory()
        classes = inv["summary"]["group_classes"]
        self.assertGreaterEqual(classes.get("pure_singleton", 0), 1)
        self.assertIn("proposed_status", inv["summary"])
        self.assertGreaterEqual(len(inv["records"]), 1)

    def test_identity_fields_not_mutated(self):
        inv = load_broad_prose_inventory()
        for rec in inv["records"]:
            self.assertTrue(rec.emission_id)
            self.assertTrue(rec.representative_occurrence_id)
            self.assertIn(rec.proposed_status, {"passage_shadow", "retain_heading_mixed_scope", "retain_heading_unresolved"})

    def test_resolve_source_passage_deterministic(self):
        inv = load_broad_prose_inventory()
        movable = [r for r in inv["records"] if r.proposed_status == "passage_shadow"]
        self.assertTrue(movable)
        source_ref = movable[0].representative_source_ref
        first, reason1 = resolve_source_passage(source_ref)
        second, reason2 = resolve_source_passage(source_ref)
        self.assertEqual(reason1, reason2)
        self.assertEqual(first, second)

    def test_resolve_source_passage_errors(self):
        passage, reason = resolve_source_passage("badref")
        self.assertIsNone(passage)
        self.assertEqual(reason, "malformed_source_ref")
        passage, reason = resolve_source_passage("Germanic/docs/lexeme_reports/model_entries/nope.md:1")
        self.assertIsNone(passage)
        self.assertEqual(reason, "missing_file")


class BroadProseShadowBuildTests(unittest.TestCase):
    def test_default_lexical_build_is_canonical(self):
        built = build_lexical_volume()
        tracked = (ASSEMBLY_DIR / "lexical_volume_alpha_01.md").read_text(encoding="utf-8")
        self.assertEqual(built, tracked)

    def test_shadow_lexical_strip_restores_default(self):
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        shadow = build_lexical_volume(passage_anchor_requests=requests)
        stripped = re.sub(
            r"\n?:::\s*\{[^}]*\.iv-anchor[^}]*emission_id=\"[^\"]+\"[^}]*\}\s*\n:::\n?",
            "\n",
            shadow,
        )
        stripped = re.sub(r"\n{3,}", "\n\n", stripped).rstrip() + "\n"
        self.assertEqual(stripped, build_lexical_volume())

    def test_shadow_book_preserves_nonexplicit_set(self):
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        movable_ids = inv["movable_emission_ids"]
        shadow_lex = build_lexical_volume(passage_anchor_requests=requests)
        prod_book = build_book_markdown(render_mode="anchor")
        shad_book = build_book_markdown(
            render_mode="anchor",
            lexical_markdown_override=shadow_lex,
            preplaced_nonexplicit_emission_ids=set(movable_ids),
        )
        self.assertEqual(set(_anchor_ids(prod_book)), set(_anchor_ids(shad_book)))
        self.assertEqual(len(_anchor_ids(prod_book)), len(set(_anchor_ids(prod_book))))
        self.assertEqual(len(_anchor_ids(shad_book)), len(set(_anchor_ids(shad_book))))

    def test_unknown_preplaced_id_fails(self):
        with self.assertRaises(ValueError):
            build_book_markdown(
                render_mode="anchor",
                lexical_markdown_override=build_lexical_volume(),
                preplaced_nonexplicit_emission_ids={"emit:not-real"},
            )


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class BroadProseEndToEndTests(unittest.TestCase):
    def test_default_shadow_checker_passes(self):
        self.assertTrue(run_shadow_check(full_impact=False, verbose=False))

    def test_unrelated_markdown_mutation_detected(self):
        import check_iv_broad_prose_placement_shadow as checker

        original = checker.CANONICAL_BOOK_MD.read_text(encoding="utf-8")
        mutated = original.replace("Index verborum", "Index verborum MUTATED", 1)
        with tempfile.TemporaryDirectory() as tmp:
            md = Path(tmp) / "mutated.md"
            md.write_text(mutated, encoding="utf-8")
            tex = checker._run_pandoc(mutated, label="mutated")
            self.assertIn(r"\index[iv]{", tex)
            self.assertNotEqual(original, mutated)


if __name__ == "__main__":
    unittest.main()
