#!/usr/bin/env python3
"""Tests for the Stage 2 production .iv-anchor emission infrastructure.

Run: cd Germanic/tests && python3 -m unittest test_index_verborum_anchor

Covers:
  * valid plan and marker tests
  * invalid plan loader tests (14 cases)
  * invalid marker contract tests (13 cases)
  * production builder raw/anchor mode invariants
  * full production anchor parity check
"""
from __future__ import annotations

import csv
import os
import re
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

    def test_builder_raw_mode_available_for_parity(self):
        """Legacy raw mode remains available as an explicit parity fixture."""
        from build_capr_book_draft import build_book_markdown
        raw_md = build_book_markdown(render_mode="raw")
        self.assertIn(r"\index[iv]{", raw_md)
        self.assertNotIn(".iv-anchor", raw_md)

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

    def test_full_production_check_passes(self):
        """Full production parity check passes."""
        from check_iv_anchor_production import check
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

    def test_production_md_has_anchors(self):
        """Stage 2 production Markdown now contains generated .iv-anchor markers."""
        prod_md = ASSEMBLY / "capr_book_draft_alpha_01.md"
        if not prod_md.exists():
            self.skipTest("Production MD not present")
        content = prod_md.read_text(encoding="utf-8")
        self.assertIn(".iv-anchor", content)


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class Stage2ProductionParityTests(unittest.TestCase):
    """Stage 2 production-activation checks."""

    def _canonical_anchor_md(self) -> str:
        return (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")

    def _expected_nonexplicit_ids(self) -> list[str]:
        rows = list(csv.DictReader((BOOK / "index_verborum_book_emissions.tsv").open(encoding="utf-8"), delimiter="\t"))
        return [
            r["emission_id"]
            for r in rows
            if (r.get("emission_path") or "").strip() in ("heading_injection", "line_injection")
        ]

    def test_build_book_markdown_defaults_to_anchor_mode(self):
        from build_capr_book_draft import build_book_markdown
        md_default = build_book_markdown()
        md_anchor = build_book_markdown(render_mode="anchor")
        self.assertEqual(md_default, md_anchor)
        self.assertIn(".iv-anchor", md_default)

    def test_default_builder_output_equals_tracked_canonical(self):
        from build_capr_book_draft import build_book_markdown
        self.assertEqual(build_book_markdown(), self._canonical_anchor_md())

    def test_canonical_markdown_anchor_counts(self):
        content = self._canonical_anchor_md()
        block_ids = re.findall(r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}', content)
        inline_ids = re.findall(r'\[\]\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}', content)
        self.assertEqual(len(block_ids), 448)
        self.assertEqual(len(inline_ids), 0)

    def test_canonical_has_zero_raw_nonexplicit_commands(self):
        content = self._canonical_anchor_md()
        raw_nonexplicit = [
            ln for ln in content.splitlines()
            if ln.strip().startswith(r"\index[iv]{")
        ]
        self.assertEqual(raw_nonexplicit, [])

    def test_canonical_anchor_ids_match_expected_set(self):
        content = self._canonical_anchor_md()
        actual = re.findall(r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}', content)
        self.assertEqual(set(actual), set(self._expected_nonexplicit_ids()))
        self.assertEqual(len(actual), len(set(actual)))

    def test_anchor_sequence_equals_production_rendering_trace(self):
        from build_capr_book_draft import build_book_markdown
        trace = []
        anchor_md = build_book_markdown(render_mode="anchor", emission_trace=trace)
        ids_from_md = re.findall(r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}', anchor_md)
        ids_from_trace = [e.emission_id for e in trace]
        self.assertEqual(ids_from_md, ids_from_trace)
        self.assertEqual(len(ids_from_trace), 448)

    def test_raw_and_anchor_trace_records_equal(self):
        from build_capr_book_draft import build_book_markdown
        raw_trace = []
        anchor_trace = []
        build_book_markdown(render_mode="raw", emission_trace=raw_trace)
        build_book_markdown(render_mode="anchor", emission_trace=anchor_trace)
        self.assertEqual(raw_trace, anchor_trace)
        self.assertEqual(len(raw_trace), 448)
        self.assertEqual(len({e.emission_id for e in raw_trace}), 448)

    def test_no_explicit_tag_ids_in_canonical_anchors(self):
        rows = list(csv.DictReader((BOOK / "index_verborum_book_emissions.tsv").open(encoding="utf-8"), delimiter="\t"))
        explicit_ids = {r["emission_id"] for r in rows if (r.get("emission_path") or "").strip() == "explicit_tag"}
        content = self._canonical_anchor_md()
        ids = set(re.findall(r':::\s*\{[^}]*\.iv-anchor[^}]*emission_id="([^"]+)"[^}]*\}', content))
        self.assertEqual(explicit_ids.intersection(ids), set())

    def test_production_checker_detects_deleted_anchor(self):
        from check_iv_anchor_production import check
        content = self._canonical_anchor_md()
        mutated = re.sub(
            r'\n?:::\s*\{[^}]*\.iv-anchor[^}]*emission_id="[^"]+"[^}]*\}\n:::\n?',
            "\n",
            content,
            count=1,
        )
        self.assertFalse(check(canonical_md_override=mutated))

    def test_production_checker_detects_duplicate_anchor(self):
        from check_iv_anchor_production import check
        content = self._canonical_anchor_md()
        m = re.search(r'(:::\s*\{[^}]*\.iv-anchor[^}]*emission_id="[^"]+"[^}]*\}\n:::\n?)', content)
        self.assertIsNotNone(m)
        mutated = content + "\n" + m.group(1)
        self.assertFalse(check(canonical_md_override=mutated))

    def test_production_checker_detects_unknown_anchor(self):
        from check_iv_anchor_production import check
        content = self._canonical_anchor_md()
        mutated = content + '\n::: {.iv-anchor emission_id="emit:unknown_nonexistent"}\n:::\n'
        self.assertFalse(check(canonical_md_override=mutated))

    def test_production_checker_detects_raw_nonexplicit_in_anchor_md(self):
        from check_iv_anchor_production import check
        content = self._canonical_anchor_md()
        mutated = content.replace(
            "\\printindex[iv]",
            "\\index[iv]{02oe@\\ivlangheader{Old English}{West Saxon normalization unmarked}!intruder@\\iventry{intruder}{}}\n\\printindex[iv]",
            1,
        )
        self.assertFalse(check(canonical_md_override=mutated))

    def test_production_checker_detects_swapped_same_command_anchor_ids(self):
        from check_iv_anchor_production import check
        rows = list(csv.DictReader((BOOK / "index_verborum_book_emissions.tsv").open(encoding="utf-8"), delimiter="\t"))
        groups: dict[str, list[str]] = {}
        for r in rows:
            if (r.get("emission_path") or "").strip() not in ("heading_injection", "line_injection"):
                continue
            groups.setdefault(r["index_command"], []).append(r["emission_id"])
        pair = None
        for ids in groups.values():
            if len(ids) >= 2:
                pair = (ids[0], ids[1])
                break
        self.assertIsNotNone(pair, "Need at least one same-command pair")
        a, b = pair
        content = self._canonical_anchor_md()
        # swap two IDs with same command text; command parity alone would miss this
        tmp = "__SWAP_TMP__"
        mutated = content.replace(f'emission_id="{a}"', f'emission_id="{tmp}"')
        mutated = mutated.replace(f'emission_id="{b}"', f'emission_id="{a}"')
        mutated = mutated.replace(f'emission_id="{tmp}"', f'emission_id="{b}"')
        self.assertFalse(check(canonical_md_override=mutated))

    def test_narrow_tex_normalization_accepts_index_whitespace_only(self):
        from check_iv_anchor_production import _narrow_tex_normalize
        base = "A\n\\index[iv]{X}\nB\n"
        variant = "A\n\n\\index[iv]{X}\n\nB\n"
        self.assertEqual(_narrow_tex_normalize(base), _narrow_tex_normalize(variant))

    def test_narrow_tex_normalization_rejects_paragraph_boundary_change(self):
        from check_iv_anchor_production import _narrow_tex_normalize
        a = "Para one.\n\nPara two.\n\\index[iv]{X}\n"
        b = "Para one. Para two.\n\\index[iv]{X}\n"
        self.assertNotEqual(_narrow_tex_normalize(a), _narrow_tex_normalize(b))

    def test_narrow_tex_normalization_rejects_changed_heading_or_prose(self):
        from check_iv_anchor_production import _narrow_tex_normalize
        a = "\\section{Heading A}\nText.\n\\index[iv]{X}\n"
        b = "\\section{Heading B}\nText.\n\\index[iv]{X}\n"
        self.assertNotEqual(_narrow_tex_normalize(a), _narrow_tex_normalize(b))

    def test_raw_and_anchor_modes_emit_same_ordered_commands(self):
        from check_iv_anchor_production import _extract_iv_commands, _run_pandoc
        from build_capr_book_draft import build_book_markdown
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            raw_tex = _run_pandoc(build_book_markdown(render_mode="raw"), tmp_path, "raw")
            anchor_tex = _run_pandoc(build_book_markdown(render_mode="anchor"), tmp_path, "anchor")
        self.assertEqual(_extract_iv_commands(raw_tex), _extract_iv_commands(anchor_tex))


if __name__ == "__main__":
    unittest.main()
