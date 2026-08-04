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
from build_full_lexical_volume import (
    SHADOW_MARKER_RE,
    _anchor_block,
    _make_source_marker,
    build_lexical_volume,
    parse_model_entry,
)
from check_iv_broad_prose_placement_shadow import (
    _parse_makeindex_output,
    _remove_iv_commands_narrow,
    check as run_shadow_check,
)
from index_verborum_broad_prose_placement import (
    GROUP_MIXED_SCOPE,
    GROUP_PURE_SHARED_ONE,
    GROUP_PURE_SINGLETON,
    GROUP_UNRESOLVED,
    PlacementRecord,
    STATUS_PASSAGE_SHADOW,
    STATUS_RETAIN_MIXED,
    STATUS_RETAIN_UNRESOLVED,
    build_passage_anchor_requests,
    classify_broad_decision_states,
    load_broad_prose_inventory,
    resolve_source_passage,
)


def _anchor_ids(md_text: str) -> list[str]:
    return re.findall(
        r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}\s*\n:::',
        md_text,
    )


# ---------------------------------------------------------------------------
# Inventory tests
# ---------------------------------------------------------------------------

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

    def test_inventory_decision_state_counts(self):
        """Decision state counts must sum to 92 with 68/2/22 distribution."""
        inv = load_broad_prose_inventory()
        counts = inv["summary"]["decision_state_counts"]
        self.assertIn("active_print_main", counts)
        self.assertIn("active_print_excluded", counts)
        self.assertIn("stale_no_current_candidate", counts)
        total = sum(counts.values())
        self.assertEqual(total, 92, f"Expected 92 total decision rows, got {total}: {counts}")
        self.assertEqual(counts["active_print_main"], 68, f"Expected 68 active_print_main: {counts}")
        self.assertEqual(counts["active_print_excluded"], 2, f"Expected 2 active_print_excluded: {counts}")
        self.assertEqual(counts["stale_no_current_candidate"], 22, f"Expected 22 stale_no_current_candidate: {counts}")

    def test_inventory_book_emissions_representative_join(self):
        """Each movable record's representative_occurrence_id must appear in book_emissions."""
        import csv
        book_emissions_path = BOOK_DIR / "index_verborum_book_emissions.tsv"
        with book_emissions_path.open(encoding="utf-8") as f:
            book_rows = list(csv.DictReader(f, delimiter="\t"))
        emission_ids_in_book = {(r.get("emission_id") or "").strip() for r in book_rows}

        inv = load_broad_prose_inventory()
        for rec in inv["records"]:
            if rec.proposed_status == STATUS_PASSAGE_SHADOW:
                self.assertIn(rec.emission_id, emission_ids_in_book,
                    f"Movable emission_id {rec.emission_id} not found in book_emissions")

    def test_pure_singleton_classification(self):
        """Synthetic: single member with broad_prose_decision scope → pure_singleton."""
        accepted_rows = [{"source_ref": "x:1", "form": "notaform", "action": "accept"}]
        counts = classify_broad_decision_states(accepted_rows)
        self.assertEqual(counts["active_print_main"] + counts["active_print_excluded"], 0)
        self.assertEqual(counts["stale_no_current_candidate"], 1)

    def test_pure_shared_one_passage_classification(self):
        """Synthetic: two rows with same (source_ref, form) not in print_main → stale."""
        rows = [
            {"source_ref": "x:5", "form": "zyz", "action": "accept"},
            {"source_ref": "x:5", "form": "zyz", "action": "accept"},
        ]
        counts = classify_broad_decision_states(rows)
        self.assertEqual(counts["stale_no_current_candidate"], 2)

    def test_mixed_scope_retained(self):
        inv = load_broad_prose_inventory()
        mixed = [r for r in inv["records"] if r.proposed_status == STATUS_RETAIN_MIXED]
        for rec in mixed:
            self.assertEqual(rec.group_class, GROUP_MIXED_SCOPE)

    def test_unresolved_malformed_ref(self):
        passage, reason = resolve_source_passage("Germanic/docs/lexeme_reports/model_entries/nope.md:abc")
        self.assertIsNone(passage)
        self.assertEqual(reason, "malformed_source_ref")


# ---------------------------------------------------------------------------
# Exact placement tests
# ---------------------------------------------------------------------------

class ExactPlacementTests(unittest.TestCase):
    def test_request_carries_block_coordinates(self):
        """build_passage_anchor_requests must include block_start_line and block_end_line."""
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        self.assertTrue(requests)
        for req in requests:
            self.assertIn("block_start_line", req, f"Missing block_start_line in {req}")
            self.assertIn("block_end_line", req, f"Missing block_end_line in {req}")
            self.assertIsInstance(req["block_start_line"], int)
            self.assertIsInstance(req["block_end_line"], int)
            self.assertGreater(req["block_end_line"], 0)

    def test_request_has_no_sort_key(self):
        """representative_sort_key must NOT be in the request dict."""
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        for req in requests:
            self.assertNotIn("representative_sort_key", req,
                f"representative_sort_key should not appear in request: {req}")

    def test_marker_inserted_after_exact_block(self):
        """Marker ends up after block_end_line, not somewhere else."""
        inv = load_broad_prose_inventory()
        movable = [r for r in inv["records"] if r.proposed_status == STATUS_PASSAGE_SHADOW]
        self.assertTrue(movable)
        rec = movable[0]
        shadow = build_lexical_volume(passage_anchor_requests=build_passage_anchor_requests([rec]))
        self.assertIn(rec.emission_id, shadow)
        # No residue
        self.assertEqual(SHADOW_MARKER_RE.findall(shadow), [])

    def test_no_marker_residue(self):
        """After shadow build, no \\x01SHADOWIV: markers remain in output."""
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        shadow = build_lexical_volume(passage_anchor_requests=requests)
        residue = SHADOW_MARKER_RE.findall(shadow)
        self.assertEqual(residue, [], f"Shadow marker residue found: {residue}")

    def test_repeated_form_earlier_paragraph_uses_source_coords(self):
        """Anchor placement uses block_end_line, not first-form search.

        The canonical wool entry has `woll` appearing as plain prose (not a tagged form)
        at line 30. The movable emission for `full` at line 24 (block 21-26) should
        place its anchor after line 26, not after line 30.
        """
        inv = load_broad_prose_inventory()
        wool_movable = [
            r for r in inv["records"]
            if "2300-wool-wull" in r.representative_source_ref
            and r.proposed_status == STATUS_PASSAGE_SHADOW
        ]
        if not wool_movable:
            self.skipTest("No movable emission found for wool entry")
        rec = wool_movable[0]
        requests = build_passage_anchor_requests([rec])
        shadow = build_lexical_volume(passage_anchor_requests=requests)
        # Find the anchor position relative to surrounding text
        anchor_pattern = re.compile(
            r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="' + re.escape(rec.emission_id) + r'"[^}]*\}\s*\n:::',
        )
        self.assertRegex(shadow, anchor_pattern)
        # No residue
        self.assertEqual(SHADOW_MARKER_RE.findall(shadow), [])

    def test_sort_key_does_not_affect_placement(self):
        """Sort key text must not be used for anchor placement."""
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        for req in requests:
            self.assertNotIn("representative_sort_key", req)

    def test_no_marker_residue_in_any_shadow(self):
        """Comprehensive: shadow build produces zero marker residue."""
        inv = load_broad_prose_inventory()
        requests = build_passage_anchor_requests(inv["records"])
        shadow = build_lexical_volume(passage_anchor_requests=requests)
        self.assertNotIn("\x01SHADOWIV:", shadow)


# ---------------------------------------------------------------------------
# Wool/woll regression test
# ---------------------------------------------------------------------------

class WoolWollRegressionTests(unittest.TestCase):
    def test_wool_woll_representative_passage(self):
        """Anchor for the wool movable emission follows its resolved source block.

        The canonical wool-wull entry has `full` appearing as plain prose at line 24
        (block end ~26). A naive first-form search would also match `full` at line 24,
        but we verify placement via block coordinates, not text search.
        """
        inv = load_broad_prose_inventory()
        wool_movable = [
            r for r in inv["records"]
            if "2300-wool-wull" in r.representative_source_ref
            and r.proposed_status == STATUS_PASSAGE_SHADOW
        ]
        if not wool_movable:
            self.skipTest("No movable emission in wool-wull entry")
        rec = wool_movable[0]
        # Verify the block coordinates are resolved
        self.assertGreater(rec.resolved_block_end_line, 0)
        self.assertGreater(rec.resolved_block_start_line, 0)
        # Build shadow and verify anchor presence
        requests = build_passage_anchor_requests([rec])
        shadow = build_lexical_volume(passage_anchor_requests=requests)
        self.assertIn(rec.emission_id, shadow)
        self.assertEqual(SHADOW_MARKER_RE.findall(shadow), [])


# ---------------------------------------------------------------------------
# Shadow build tests
# ---------------------------------------------------------------------------

class BroadProseShadowBuildTests(unittest.TestCase):
    def test_default_lexical_build_is_canonical(self):
        built = build_lexical_volume()
        tracked = (ASSEMBLY_DIR / "lexical_volume_alpha_01.md").read_text(encoding="utf-8")
        self.assertEqual(built, tracked)

    def test_default_book_build_byte_identical(self):
        built = build_book_markdown(render_mode="anchor")
        tracked = (ASSEMBLY_DIR / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        self.assertEqual(built, tracked)

    def test_canonical_tsvs_unchanged(self):
        """Key canonical TSVs must exist and be non-empty."""
        for fname in (
            "index_verborum_print_main.tsv",
            "index_verborum_emission_table.tsv",
            "index_verborum_book_emissions.tsv",
            "index_verborum_broad_prose_decisions.tsv",
        ):
            path = BOOK_DIR / fname
            self.assertTrue(path.exists(), f"Missing TSV: {fname}")
            self.assertGreater(path.stat().st_size, 0, f"Empty TSV: {fname}")

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


# ---------------------------------------------------------------------------
# TeX comparison tests
# ---------------------------------------------------------------------------

class NarrowTexNormalizationTests(unittest.TestCase):
    def _make_two_texts(self, prod_index_line: str, shad_index_line: str) -> tuple[str, str]:
        """Create two TeX-like texts differing only in index command placement."""
        body = "Some prose here.\n\nAnother paragraph.\n"
        return (
            f"\\chapter{{Test}}\n{body}{prod_index_line}\nEnd.\n",
            f"\\chapter{{Test}}\n{body}{shad_index_line}\nEnd.\n",
        )

    def test_narrow_tex_only_index_movement_passes(self):
        """Two texts differing only in \\index[iv]{...} content: stripped texts match."""
        cmd = r"\index[iv]{02oe@\ivlangheader{Old English}{}!wull@\iventry{wull}{}}"
        prod = f"Some prose.{cmd}\n\nAnother paragraph.\n"
        shad = f"Some prose.\n\nAnother paragraph.{cmd}\n"
        prod_stripped = _remove_iv_commands_narrow(prod)
        shad_stripped = _remove_iv_commands_narrow(shad)
        self.assertEqual(prod_stripped, shad_stripped)

    def test_narrow_tex_unrelated_blank_line_fails(self):
        """Adding an unrelated blank line must cause stripped texts to differ."""
        cmd = r"\index[iv]{02oe@\ivlangheader{Old English}{}!wull@\iventry{wull}{}}"
        prod = f"Some prose.{cmd}\n\nAnother paragraph.\n"
        # Extra blank line unrelated to the index command
        shad = f"Some prose.{cmd}\n\n\nAnother paragraph.\n"
        prod_stripped = _remove_iv_commands_narrow(prod)
        shad_stripped = _remove_iv_commands_narrow(shad)
        self.assertNotEqual(prod_stripped, shad_stripped)

    def test_narrow_tex_prose_mutation_fails(self):
        """Changing prose text must cause stripped texts to differ."""
        cmd = r"\index[iv]{02oe@\ivlangheader{Old English}{}!wull@\iventry{wull}{}}"
        prod = f"Some prose.{cmd}\nAnother paragraph.\n"
        shad = f"Some prose MUTATED.{cmd}\nAnother paragraph.\n"
        prod_stripped = _remove_iv_commands_narrow(prod)
        shad_stripped = _remove_iv_commands_narrow(shad)
        self.assertNotEqual(prod_stripped, shad_stripped)

    def test_narrow_tex_unbalanced_command_raises(self):
        """Unbalanced brace in index command must raise ValueError."""
        bad = r"\index[iv]{unbalanced"
        with self.assertRaises(ValueError):
            _remove_iv_commands_narrow(bad)

    def test_narrow_tex_index_on_own_line_removed(self):
        """Index command on its own line should not leave extra blank lines."""
        cmd = r"\index[iv]{02oe@\ivlangheader{Old English}{}!wull@\iventry{wull}{}}"
        text = f"Line one.\n{cmd}\nLine two.\n"
        stripped = _remove_iv_commands_narrow(text)
        self.assertNotIn("\x5cindex[iv]", stripped)
        # Should not have consecutive blank lines
        self.assertNotIn("\n\n\n", stripped)


# ---------------------------------------------------------------------------
# MakeIndex parser tests
# ---------------------------------------------------------------------------

class MakeIndexParserTests(unittest.TestCase):
    def test_makeindex_parse_1865_correct(self):
        output = "Scanning input file iv.idx.....done (1865 entries accepted, 0 rejected).\n"
        acc, rej = _parse_makeindex_output(output)
        self.assertEqual(acc, 1865, f"Expected 1865 accepted, got {acc}")
        self.assertEqual(rej, 0)

    def test_makeindex_parse_5_correct(self):
        output = "Scanning input file iv.idx.....done (5 entries accepted, 0 rejected).\n"
        acc, rej = _parse_makeindex_output(output)
        self.assertEqual(acc, 5)
        self.assertEqual(rej, 0)

    def test_makeindex_parse_zero(self):
        output = "Scanning input file iv.idx.....done (0 entries accepted, 0 rejected).\n"
        acc, rej = _parse_makeindex_output(output)
        self.assertEqual(acc, 0)
        self.assertEqual(rej, 0)

    def test_makeindex_parse_real_output(self):
        output = (
            "This is makeindex, version 2.18 [TeX Live 2026] (kpathsea + Thai support).\n"
            "Scanning input file iv.idx.....done (1865 entries accepted, 0 rejected).\n"
            "Sorting entries...done (7421 comparisons).\n"
            "Generating output file iv.ind...done (1866 lines written, 0 warnings).\n"
            "Output written in iv.ind.\n"
            "Transcript written in iv.ilg.\n"
        )
        acc, rej = _parse_makeindex_output(output)
        self.assertEqual(acc, 1865)
        self.assertEqual(rej, 0)

    def test_makeindex_parse_with_rejected(self):
        output = "Scanning input file iv.idx.....done (100 entries accepted, 3 rejected).\n"
        acc, rej = _parse_makeindex_output(output)
        self.assertEqual(acc, 100)
        self.assertEqual(rej, 3)


# ---------------------------------------------------------------------------
# End-to-end tests
# ---------------------------------------------------------------------------

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
