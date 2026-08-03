#!/usr/bin/env python3
"""Tests for the .iv-anchor shadow-mode emission infrastructure.

Run: cd Germanic/tests && python3 -m unittest test_index_verborum_anchor

Covers:
  * valid plan and marker tests
  * invalid plan loader tests (14 cases)
  * invalid marker contract tests (13 cases)
  * production builder raw/anchor mode invariants
  * full shadow parity check
"""
from __future__ import annotations

import csv
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK = REPO_ROOT / "Germanic/docs/book"
TOOLS = REPO_ROOT / "Germanic/tools"
ASSEMBLY = REPO_ROOT / "Germanic/docs/assembly"
FILTER_LUA = TOOLS / "index_verborum_filter.lua"

sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(ASSEMBLY))


def _make_emission_row(**overrides) -> dict:
    base = {
        "emission_id": "emit:abc123",
        "representative_occurrence_id": "heading:abc123",
        "emission_path": "heading_injection",
        "site": "test — OE test",
        "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!test@\iventry{test}{}}",
        "language": "oe",
        "variety": "",
        "display": "test",
        "sort_key": "test",
        "form_role": "target_form",
        "source_scope": "lexical_heading",
        "source_ref": "test — OE test",
        "source_occurrence_count": "1",
        "source_occurrence_ids": "heading:abc123",
    }
    base.update(overrides)
    return base


def _write_emissions_tsv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def _run_pandoc_with_plan(md_text: str, emissions_tsv: Path | None = None,
                          env_extra: dict | None = None) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env.update({
        "CAPR_IV_PRINT_MAIN_TSV": str(BOOK / "index_verborum_print_main.tsv"),
        "CAPR_IV_BOOK_EMISSIONS_TSV": str(emissions_tsv or BOOK / "index_verborum_book_emissions.tsv"),
        "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
        "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
    })
    if env_extra:
        env.update(env_extra)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "in.md"
        src.write_text(md_text, encoding="utf-8")
        return subprocess.run(
            ["pandoc", str(src), "--from", "markdown+raw_tex", "--to", "latex",
             "--lua-filter", str(FILTER_LUA)],
            capture_output=True, text=True, env=env, cwd=str(REPO_ROOT),
        )


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class ValidPlanAndMarkerTests(unittest.TestCase):
    """Valid plan and marker tests from the spec."""

    def _make_plan_tsv(self, rows, tmp):
        p = Path(tmp) / "emissions.tsv"
        _write_emissions_tsv(p, rows)
        return p

    def test_valid_block_anchor_emits_stored_command(self):
        """Valid block anchor emits the stored command exactly."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row()
            plan = self._make_plan_tsv([row], tmp)
            md = f'::: {{.iv-anchor emission_id="emit:abc123"}}\n:::\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertIn(row["index_command"], proc.stdout)

    def test_valid_inline_anchor_emits_stored_command(self):
        """Valid inline anchor emits the stored command exactly."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row()
            plan = self._make_plan_tsv([row], tmp)
            md = '[]{.iv-anchor emission_id="emit:abc123"}\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertIn(row["index_command"], proc.stdout)

    def test_block_anchor_uses_rawblock(self):
        """Block anchor output is a RawBlock (disappears in HTML)."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row()
            plan = self._make_plan_tsv([row], tmp)
            md = '::: {.iv-anchor emission_id="emit:abc123"}\n:::\n'
            env = dict(os.environ)
            env.update({
                "CAPR_IV_PRINT_MAIN_TSV": str(BOOK / "index_verborum_print_main.tsv"),
                "CAPR_IV_BOOK_EMISSIONS_TSV": str(plan),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
                "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            })
            with tempfile.TemporaryDirectory() as tmp2:
                src = Path(tmp2) / "in.md"
                src.write_text(md, encoding="utf-8")
                proc = subprocess.run(
                    ["pandoc", str(src), "--from", "markdown+raw_tex", "--to", "html",
                     "--lua-filter", str(FILTER_LUA)],
                    capture_output=True, text=True, env=env, cwd=str(REPO_ROOT),
                )
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            # Block RawBlock disappears from HTML output
            self.assertNotIn(r"\index[iv]", proc.stdout)
            self.assertNotIn("iv-anchor", proc.stdout)

    def test_inline_anchor_uses_rawinline_latex(self):
        """Inline anchor emits RawInline latex — visible in HTML as empty."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row()
            plan = self._make_plan_tsv([row], tmp)
            md = 'Before []{.iv-anchor emission_id="emit:abc123"} after\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertIn(row["index_command"], proc.stdout)
            # No extra visible content around the command
            self.assertIn("Before", proc.stdout)
            self.assertIn("after", proc.stdout)

    def test_anchor_produces_no_visible_html(self):
        """Anchor markers produce no visible HTML output."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row()
            plan = self._make_plan_tsv([row], tmp)
            md = '::: {.iv-anchor emission_id="emit:abc123"}\n:::\n'
            env = dict(os.environ)
            env.update({
                "CAPR_IV_PRINT_MAIN_TSV": str(BOOK / "index_verborum_print_main.tsv"),
                "CAPR_IV_BOOK_EMISSIONS_TSV": str(plan),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
                "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            })
            with tempfile.TemporaryDirectory() as tmp2:
                src = Path(tmp2) / "in.md"
                src.write_text(md, encoding="utf-8")
                proc = subprocess.run(
                    ["pandoc", str(src), "--from", "markdown+raw_tex", "--to", "html",
                     "--lua-filter", str(FILTER_LUA)],
                    capture_output=True, text=True, env=env, cwd=str(REPO_ROOT),
                )
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertNotIn("iv-anchor", proc.stdout)
            self.assertEqual(proc.stdout.strip(), "")

    def test_multiple_anchors_emit_in_order(self):
        """Several different anchors emit in document order."""
        with tempfile.TemporaryDirectory() as tmp:
            rows = [
                _make_emission_row(emission_id="emit:first",
                                   representative_occurrence_id="heading:first",
                                   source_occurrence_ids="heading:first",
                                   index_command=r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!aaa@\iventry{aaa}{}}"),
                _make_emission_row(emission_id="emit:second",
                                   representative_occurrence_id="heading:second",
                                   source_occurrence_ids="heading:second",
                                   index_command=r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!bbb@\iventry{bbb}{}}"),
            ]
            plan = self._make_plan_tsv(rows, tmp)
            md = '::: {.iv-anchor emission_id="emit:first"}\n:::\n\n::: {.iv-anchor emission_id="emit:second"}\n:::\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            pos_first = proc.stdout.find(rows[0]["index_command"])
            pos_second = proc.stdout.find(rows[1]["index_command"])
            self.assertGreater(pos_first, -1)
            self.assertGreater(pos_second, pos_first, "Second anchor must appear after first")

    def test_collapsed_emission_loads_correctly(self):
        """Emission with multiple source occurrence IDs loads without error."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row(
                # representative must be one of the source_occurrence_ids
                representative_occurrence_id="heading:occ1",
                source_occurrence_count="3",
                source_occurrence_ids="heading:occ1|heading:occ2|heading:occ3",
            )
            plan = self._make_plan_tsv([row], tmp)
            md = '::: {.iv-anchor emission_id="emit:abc123"}\n:::\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertIn(row["index_command"], proc.stdout)

    def test_all_source_occurrence_ids_map_to_one_emission(self):
        """Multiple source occurrence IDs all map to the same emission."""
        with tempfile.TemporaryDirectory() as tmp:
            row = _make_emission_row(
                emission_id="emit:shared",
                representative_occurrence_id="heading:occ1",
                source_occurrence_count="2",
                source_occurrence_ids="heading:occ1|heading:occ2",
            )
            plan = self._make_plan_tsv([row], tmp)
            md = '::: {.iv-anchor emission_id="emit:shared"}\n:::\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertIn(row["index_command"], proc.stdout)

    def test_builder_raw_mode_byte_identical(self):
        """Shared builder raw mode is byte-identical to tracked canonical MD."""
        from build_capr_book_draft import build_book_markdown
        prod = ASSEMBLY / "capr_book_draft_alpha_01.md"
        if not prod.exists():
            self.skipTest("Production MD not present")
        self.assertEqual(
            build_book_markdown(render_mode="raw"),
            prod.read_text(encoding="utf-8"),
        )

    def test_builder_anchor_mode_produces_448_ids(self):
        """Shared builder anchor mode produces exactly 448 anchor block markers."""
        import re
        from build_capr_book_draft import build_book_markdown
        anchor_md = build_book_markdown(render_mode="anchor")
        ids = re.findall(
            r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}',
            anchor_md,
        )
        self.assertEqual(len(ids), 448, f"Expected 448 anchor IDs, got {len(ids)}")
        self.assertEqual(len(set(ids)), 448, "All anchor IDs must be unique")

    def test_full_shadow_check_passes(self):
        """Full shadow parity check passes."""
        from check_iv_anchor_shadow import check
        self.assertTrue(check(), "Shadow parity check must pass")


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class InvalidPlanLoaderTests(unittest.TestCase):
    """Invalid plan loader tests — loader must fail closed on each condition."""

    def _fail(self, rows: list[dict], expected_fragment: str) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            plan = Path(tmp) / "e.tsv"
            _write_emissions_tsv(plan, rows)
            md = f'::: {{.iv-anchor emission_id="{rows[0]["emission_id"] if rows else "emit:x"}"}}\n:::\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertNotEqual(proc.returncode, 0,
                                 f"Expected failure containing {expected_fragment!r}")
            self.assertIn(expected_fragment, proc.stderr,
                          f"Error must mention {expected_fragment!r}; got: {proc.stderr[:300]}")

    def test_blank_emission_id(self):
        r = _make_emission_row(emission_id="")
        self._fail([r], "blank or missing emission_id")

    def test_duplicate_emission_id(self):
        r = _make_emission_row()
        self._fail([r, r], "duplicate emission_id")

    def test_blank_index_command(self):
        r = _make_emission_row(index_command="")
        self._fail([r], "blank index_command")

    def test_blank_representative_occurrence_id(self):
        r = _make_emission_row(representative_occurrence_id="")
        self._fail([r], "blank representative_occurrence_id")

    def test_blank_source_occurrence_ids(self):
        r = _make_emission_row(source_occurrence_ids="")
        self._fail([r], "blank source_occurrence_ids")

    def test_invalid_non_integer_count(self):
        r = _make_emission_row(source_occurrence_count="not_a_number")
        self._fail([r], "invalid source_occurrence_count")

    def test_zero_count(self):
        r = _make_emission_row(source_occurrence_count="0")
        self._fail([r], "invalid source_occurrence_count")

    def test_negative_count(self):
        r = _make_emission_row(source_occurrence_count="-1")
        self._fail([r], "invalid source_occurrence_count")

    def test_count_list_mismatch(self):
        r = _make_emission_row(source_occurrence_count="3", source_occurrence_ids="heading:a|heading:b")
        self._fail([r], "source_occurrence_count=3 but found 2")

    def test_blank_id_in_occurrence_ids(self):
        r = _make_emission_row(source_occurrence_count="2", source_occurrence_ids="heading:a|")
        self._fail([r], "blank occurrence_id")

    def test_duplicate_source_occurrence_id(self):
        r = _make_emission_row(
            source_occurrence_count="2",
            source_occurrence_ids="heading:abc123|heading:abc123",
        )
        self._fail([r], "duplicate occurrence_id")

    def test_representative_missing_from_ids(self):
        r = _make_emission_row(
            representative_occurrence_id="heading:nothere",
        )
        self._fail([r], "does not appear in source_occurrence_ids")

    def test_one_occurrence_mapped_to_two_emissions(self):
        r1 = _make_emission_row(emission_id="emit:first")
        r2 = _make_emission_row(
            emission_id="emit:second",
            representative_occurrence_id="heading:abc123",
            source_occurrence_ids="heading:abc123",
        )
        with tempfile.TemporaryDirectory() as tmp:
            plan = Path(tmp) / "e.tsv"
            _write_emissions_tsv(plan, [r1, r2])
            md = '::: {.iv-anchor emission_id="emit:first"}\n:::\n'
            proc = _run_pandoc_with_plan(md, plan)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("appears in both emission", proc.stderr)

    def test_blank_emission_path(self):
        r = _make_emission_row(emission_path="")
        self._fail([r], "unsupported emission_path")

    def test_unsupported_emission_path(self):
        r = _make_emission_row(emission_path="unknown_path")
        self._fail([r], "unsupported emission_path")


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class InvalidMarkerTests(unittest.TestCase):
    """Invalid marker contract tests — Lua must fail closed on each condition."""

    def _make_real_plan_and_row(self) -> tuple[Path, dict, str]:
        """Return (plan_tsv, row, emission_id) using a real non-explicit emission."""
        import tempfile
        rows = list(csv.DictReader(
            (BOOK / "index_verborum_book_emissions.tsv").open(encoding="utf-8"),
            delimiter="\t",
        ))
        row = next(r for r in rows if r["emission_path"] == "heading_injection")
        return BOOK / "index_verborum_book_emissions.tsv", row, row["emission_id"]

    def _fail_marker(self, md: str, expected_fragment: str,
                     plan: Path | None = None) -> None:
        proc = _run_pandoc_with_plan(md, plan)
        self.assertNotEqual(proc.returncode, 0,
                             f"Expected failure containing {expected_fragment!r}")
        self.assertIn(expected_fragment, proc.stderr,
                      f"Error must mention {expected_fragment!r}; got: {proc.stderr[:400]}")

    def test_missing_emission_id_attribute(self):
        md = '::: {.iv-anchor}\n:::\n'
        self._fail_marker(md, "blank or missing emission_id")

    def test_blank_emission_id_attribute(self):
        md = '::: {.iv-anchor emission_id=""}\n:::\n'
        self._fail_marker(md, "blank or missing emission_id")

    def test_unknown_emission_id(self):
        md = '::: {.iv-anchor emission_id="emit:nonexistent_xxxxxxxx"}\n:::\n'
        self._fail_marker(md, "not found in emission plan")

    def test_explicit_tag_emission_must_not_be_anchored(self):
        """Anchor referring to explicit_tag emission must fail."""
        rows = list(csv.DictReader(
            (BOOK / "index_verborum_book_emissions.tsv").open(encoding="utf-8"),
            delimiter="\t",
        ))
        explicit_row = next(r for r in rows if r["emission_path"] == "explicit_tag")
        eid = explicit_row["emission_id"]
        md = f'::: {{.iv-anchor emission_id="{eid}"}}\n:::\n'
        self._fail_marker(md, "explicit_tag")

    def test_duplicate_anchor_in_document(self):
        _, _, eid = self._make_real_plan_and_row()
        md = (f'::: {{.iv-anchor emission_id="{eid}"}}\n:::\n\n'
              f'::: {{.iv-anchor emission_id="{eid}"}}\n:::\n')
        self._fail_marker(md, "duplicate anchor")

    def test_nonempty_inline_anchor(self):
        """[{}]{.iv-anchor ...} has non-empty content and must fail."""
        _, _, eid = self._make_real_plan_and_row()
        md = f'[{{}}]{{.iv-anchor emission_id="{eid}"}}\n'
        self._fail_marker(md, "non-empty inline content")

    def test_nonempty_block_anchor(self):
        """Block anchor with content inside the fences must fail."""
        _, _, eid = self._make_real_plan_and_row()
        md = f'::: {{.iv-anchor emission_id="{eid}"}}\nsome content here\n:::\n'
        self._fail_marker(md, "non-empty block content")

    def test_iv_iv_anchor_contradiction(self):
        _, _, eid = self._make_real_plan_and_row()
        md = f'[]{{{{"iv iv-anchor emission_id="{eid}"}}}}\n'
        # Build the span attrs properly
        md = f'[]{{.iv .iv-anchor emission_id="{eid}"}}\n'
        self._fail_marker(md, "contradictory class")

    def test_recon_iv_anchor_contradiction(self):
        _, _, eid = self._make_real_plan_and_row()
        md = f'[]{{.recon .iv-anchor emission_id="{eid}"}}\n'
        self._fail_marker(md, "contradictory class")

    def test_pred_iv_anchor_contradiction(self):
        _, _, eid = self._make_real_plan_and_row()
        md = f'[]{{.pred .iv-anchor emission_id="{eid}"}}\n'
        self._fail_marker(md, "contradictory class")

    def test_lex_iv_anchor_contradiction(self):
        _, _, eid = self._make_real_plan_and_row()
        md = f'[]{{.lex .iv-anchor emission_id="{eid}"}}\n'
        self._fail_marker(md, "contradictory class")

    def test_ex_iv_anchor_contradiction(self):
        _, _, eid = self._make_real_plan_and_row()
        md = f'[]{{.ex .iv-anchor emission_id="{eid}"}}\n'
        self._fail_marker(md, "contradictory class")

    def test_production_md_has_no_anchor_markers(self):
        """Regression: the production capr_book_draft_alpha_01.md has no anchor markers."""
        prod_md = ASSEMBLY / "capr_book_draft_alpha_01.md"
        if not prod_md.exists():
            self.skipTest("Production MD not present")
        self.assertNotIn(".iv-anchor", prod_md.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
