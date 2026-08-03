#!/usr/bin/env python3
"""Tests for Stage 3A explicit occurrence plan shadow pipeline."""
from __future__ import annotations

import csv
import os
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK = REPO_ROOT / "Germanic/docs/book"
TOOLS = REPO_ROOT / "Germanic/tools"
ASSEMBLY = REPO_ROOT / "Germanic/docs/assembly"
FILTER_LUA = TOOLS / "index_verborum_filter.lua"

sys.path.insert(0, str(TOOLS))

from index_verborum_explicit_plan import (
    EXPLICIT_PLAN_FIELDS,
    build_explicit_plan_from_paths,
    inventory_spans,
    render_explicit_plan_tsv,
    scan_explicit_spans,
    validate_explicit_plan_from_paths,
)


def _load_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def _run_pandoc(md_text: str, *, explicit_mode: str, explicit_plan_tsv: Path, print_main_tsv: Path, book_emissions_tsv: Path, require_completeness: bool = False) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env.update(
        {
            "CAPR_IV_EXPLICIT_MODE": explicit_mode,
            "CAPR_IV_EXPLICIT_PLAN_TSV": str(explicit_plan_tsv),
            "CAPR_IV_PRINT_MAIN_TSV": str(print_main_tsv),
            "CAPR_IV_BOOK_EMISSIONS_TSV": str(book_emissions_tsv),
            "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
            "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            "CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS": "1" if require_completeness else "0",
        }
    )
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "in.md"
        src.write_text(md_text, encoding="utf-8")
        return subprocess.run(
            ["pandoc", str(src), "--from", "markdown+raw_tex", "--to", "latex", "--lua-filter", str(FILTER_LUA)],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
            env=env,
        )


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class ExplicitPlanGenerationTests(unittest.TestCase):
    def test_plan_generation_counts(self):
        rows = build_explicit_plan_from_paths()
        counts = Counter((r.get("disposition") or "").strip() for r in rows)
        self.assertEqual(len(rows), 1496)
        self.assertEqual(counts["emit"], 1417)
        self.assertEqual(counts["suppress"], 79)
        self.assertEqual(counts["emit"] + counts["suppress"], 1496)

    def test_plan_order_equals_assembled_order(self):
        rows = build_explicit_plan_from_paths()
        md = (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        spans = [
            s for s in scan_explicit_spans(md)
            if s["span_class"] in {"iv", "pred"} and (s.get("language") or "").strip() and ">" not in (s.get("normalized_visible_form") or "")
        ]
        self.assertEqual([r["occurrence_id"] for r in rows], [s["occurrence_id"] for s in spans])

    def test_generated_plan_matches_tracked(self):
        generated = render_explicit_plan_tsv(build_explicit_plan_from_paths())
        tracked = (BOOK / "index_verborum_book_explicit_plan.tsv").read_text(encoding="utf-8")
        self.assertEqual(generated, tracked)

    def test_emit_join_and_suppress_join(self):
        rows = build_explicit_plan_from_paths()
        emissions = _load_tsv(BOOK / "index_verborum_book_emissions.tsv")
        excluded = _load_tsv(BOOK / "index_verborum_print_excluded.tsv")
        em_by_id = {(r["emission_id"]): r for r in emissions}
        ex_by_occ = {(r["occurrence_id"]): r for r in excluded if r.get("source_scope") == "explicit_tag"}
        for row in rows:
            if row["disposition"] == "emit":
                em = em_by_id[row["emission_id"]]
                self.assertEqual(em["emission_path"], "explicit_tag")
                self.assertEqual(em["representative_occurrence_id"], row["occurrence_id"])
                self.assertEqual(em["index_command"], row["index_command"])
            else:
                ex = ex_by_occ[row["occurrence_id"]]
                self.assertEqual(ex["exclusion_reason"], row["exclusion_reason"])

    def test_validate_explicit_plan_from_paths(self):
        rows = build_explicit_plan_from_paths()
        validate_explicit_plan_from_paths(rows)


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class ExplicitPlanLuaModeTests(unittest.TestCase):
    def _base_row(self, **overrides) -> dict[str, str]:
        row = {
            "occurrence_id": "occ:1",
            "disposition": "emit",
            "emission_id": "occ:1",
            "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!ascaef@\iventry{āsceaf}{}}",
            "exclusion_reason": "",
            "language": "oe",
            "variety": "",
            "form": "āsceaf",
            "display": "āsceaf",
            "sort_key": "ascaef",
            "form_role": "evidence_form",
            "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
        }
        row.update(overrides)
        return row

    def _print_main(self, **overrides) -> list[dict[str, str]]:
        row = {
            "language": "oe",
            "variety": "",
            "form": "āsceaf",
            "display": "āsceaf",
            "sort_key": "ascaef",
            "form_role": "evidence_form",
            "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "occurrence_id": "occ:1",
            "origin": "test",
            "status": "test",
        }
        row.update(overrides)
        return [row]

    def _book_emissions(self, **overrides) -> list[dict[str, str]]:
        row = {
            "emission_id": "occ:1",
            "representative_occurrence_id": "occ:1",
            "emission_path": "explicit_tag",
            "site": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!ascaef@\iventry{āsceaf}{}}",
            "language": "oe",
            "variety": "",
            "display": "āsceaf",
            "sort_key": "ascaef",
            "form_role": "evidence_form",
            "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "source_occurrence_count": "1",
            "source_occurrence_ids": "occ:1",
        }
        row.update(overrides)
        return [row]

    def _write_fixture_files(self, tmp: str, plan_rows, main_rows, emission_rows):
        p = Path(tmp)
        plan = p / "plan.tsv"
        main = p / "main.tsv"
        em = p / "em.tsv"
        _write_tsv(plan, plan_rows, EXPLICIT_PLAN_FIELDS)
        _write_tsv(main, main_rows, list(main_rows[0].keys()))
        _write_tsv(em, emission_rows, list(emission_rows[0].keys()))
        return plan, main, em

    def test_plan_mode_emit_and_suppress(self):
        with tempfile.TemporaryDirectory() as tmp:
            emit = self._base_row()
            suppress = self._base_row(
                occurrence_id="occ:2",
                disposition="suppress",
                emission_id="",
                index_command="",
                exclusion_reason="print_policy_excluded",
                form="sċēaf",
                display="sċēaf",
                sort_key="sceaf",
                source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2",
            )
            plan, main, em = self._write_fixture_files(
                tmp,
                [emit, suppress],
                self._print_main(),
                self._book_emissions(),
            )
            md = (
                '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
                '[sċēaf]{.iv lang=oe sort=sceaf role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2" occ_id="occ:2"}\n'
            )
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertEqual(proc.stdout.count(r"\index[iv]{"), 1)
            self.assertIn(r"\index[iv]{02oe@", proc.stdout)

    def test_plan_mode_missing_occ_id_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan, main, em = self._write_fixture_files(tmp, [self._base_row()], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("requires nonblank occ_id", proc.stderr)

    def test_plan_mode_unknown_occ_id_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan, main, em = self._write_fixture_files(tmp, [self._base_row()], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:unknown"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("not found in explicit plan", proc.stderr)

    def test_plan_loader_validation_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            row = self._base_row(disposition="")
            plan, main, em = self._write_fixture_files(tmp, [row], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("blank disposition", proc.stderr)

    def test_unsupported_explicit_mode_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan, main, em = self._write_fixture_files(tmp, [self._base_row()], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="bogus_mode", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("unsupported CAPR_IV_EXPLICIT_MODE", proc.stderr)

    def test_compare_mode_command_mismatch_fails_and_mentions_occ_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Plan and book_emissions both carry the same wrong command so that
            # cross-validation at plan-load time passes; the compare-mode
            # runtime then catches the mismatch vs the legacy-computed command.
            wrong_cmd = r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!WRONG@\iventry{wrong}{}}"
            row = self._base_row(index_command=wrong_cmd)
            em = self._book_emissions(index_command=wrong_cmd)
            plan, main, em_f = self._write_fixture_files(tmp, [row], self._print_main(), em)
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="compare", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em_f)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("occ:1", proc.stderr)
            self.assertIn("compare command mismatch", proc.stderr)

    def test_compare_mode_emit_suppress_disagreement_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            row = self._base_row(disposition="suppress", emission_id="", index_command="", exclusion_reason="print_policy_excluded")
            # book_emissions must NOT have occ:1 for the suppress cross-validation to pass.
            # Provide an unrelated explicit_tag row so the TSV is well-formed.
            em_other = self._book_emissions()
            em_other[0]["emission_id"] = "occ:other"
            em_other[0]["representative_occurrence_id"] = "occ:other"
            em_other[0]["source_occurrence_ids"] = "occ:other"
            plan, main, em_f = self._write_fixture_files(tmp, [row], self._print_main(), em_other)
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="compare", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em_f)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("legacy=emit plan=suppress", proc.stderr)

    def test_nfd_nfc_occ_id_resolution_without_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            nfc = unicodedata.normalize("NFC", "āsceaf")
            nfd = unicodedata.normalize("NFD", "āsceaf")
            self.assertNotEqual(nfc.encode("utf-8"), nfd.encode("utf-8"))
            row = self._base_row(form=nfc, display=nfc)
            pm = self._print_main(form=nfc, display=nfc)
            ems = self._book_emissions(display=nfc)
            plan, main, em = self._write_fixture_files(tmp, [row], pm, ems)
            md = f'[{nfd}]{{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertIn(r"\index[iv]{", proc.stdout)

    def test_duplicate_visible_forms_different_occ_ids_resolve_independently(self):
        with tempfile.TemporaryDirectory() as tmp:
            row1 = self._base_row(occurrence_id="occ:1", emission_id="occ:1", source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1")
            row2 = self._base_row(occurrence_id="occ:2", emission_id="occ:2", source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2")
            em1 = self._book_emissions()[0]
            em2 = dict(em1)
            em2["emission_id"] = "occ:2"
            em2["representative_occurrence_id"] = "occ:2"
            em2["source_occurrence_ids"] = "occ:2"
            em2["source_ref"] = "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2"
            plan, main, em = self._write_fixture_files(tmp, [row1, row2], self._print_main(), [em1, em2])
            md = (
                '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
                '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2" occ_id="occ:2"}\n'
            )
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertEqual(proc.returncode, 0, proc.stderr[:300])
            self.assertEqual(proc.stdout.count(r"\index[iv]{"), 2)


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class ExplicitPlanShadowCheckerTests(unittest.TestCase):
    def test_full_shadow_checker_passes(self):
        from check_iv_explicit_plan_shadow import check
        check()

    def test_checker_fails_if_plan_row_removed(self):
        from check_iv_explicit_plan_shadow import check
        rows = _load_tsv(BOOK / "index_verborum_book_explicit_plan.tsv")
        with self.assertRaises(SystemExit):
            check(plan_rows_override=rows[:-1])

    def test_checker_fails_if_disposition_changed(self):
        from check_iv_explicit_plan_shadow import check
        rows = _load_tsv(BOOK / "index_verborum_book_explicit_plan.tsv")
        target = next(r for r in rows if r["disposition"] == "emit")
        target["disposition"] = "suppress"
        target["emission_id"] = ""
        target["index_command"] = ""
        target["exclusion_reason"] = "forced_test_mismatch"
        with self.assertRaises(SystemExit):
            check(plan_rows_override=rows)


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class ExplicitPlanBookEmissionsJoinTests(unittest.TestCase):
    """Tests for the book_emissions cross-validation added in Stage 3B."""

    def _base_row(self, **overrides) -> dict[str, str]:
        row = {
            "occurrence_id": "occ:1",
            "disposition": "emit",
            "emission_id": "occ:1",
            "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!ascaef@\iventry{āsceaf}{}}",
            "exclusion_reason": "",
            "language": "oe",
            "variety": "",
            "form": "āsceaf",
            "display": "āsceaf",
            "sort_key": "ascaef",
            "form_role": "evidence_form",
            "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
        }
        row.update(overrides)
        return row

    def _print_main(self) -> list[dict[str, str]]:
        return [{
            "language": "oe", "variety": "", "form": "āsceaf", "display": "āsceaf",
            "sort_key": "ascaef", "form_role": "evidence_form", "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "occurrence_id": "occ:1", "origin": "test", "status": "test",
        }]

    def _book_emissions(self, **overrides) -> list[dict[str, str]]:
        row = {
            "emission_id": "occ:1", "representative_occurrence_id": "occ:1",
            "emission_path": "explicit_tag",
            "site": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!ascaef@\iventry{āsceaf}{}}",
            "language": "oe", "variety": "", "display": "āsceaf", "sort_key": "ascaef",
            "form_role": "evidence_form", "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "source_occurrence_count": "1", "source_occurrence_ids": "occ:1",
        }
        row.update(overrides)
        return [row]

    def _write_fixture(self, tmp: str, plan_rows, main_rows, em_rows):
        p = Path(tmp)
        plan = p / "plan.tsv"
        main = p / "main.tsv"
        em = p / "em.tsv"
        _write_tsv(plan, plan_rows, EXPLICIT_PLAN_FIELDS)
        _write_tsv(main, main_rows, list(main_rows[0].keys()))
        _write_tsv(em, em_rows, list(em_rows[0].keys()))
        return plan, main, em

    def test_emit_with_correct_book_emissions_succeeds(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan, main, em = self._write_fixture(tmp, [self._base_row()], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertEqual(proc.returncode, 0, proc.stderr[:400])

    def test_emit_missing_in_book_emissions_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            # emit row but book_emissions TSV is empty
            em_rows = [{"emission_id": "", "representative_occurrence_id": "", "emission_path": "heading_injection",
                        "site": "", "index_command": "", "language": "", "variety": "", "display": "",
                        "sort_key": "", "form_role": "", "source_scope": "", "source_ref": "",
                        "source_occurrence_count": "1", "source_occurrence_ids": ""}]
            plan, main, em = self._write_fixture(tmp, [self._base_row()], self._print_main(), em_rows)
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("not found in book_explicit_emissions", proc.stderr)

    def test_emit_book_emissions_index_command_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            em = self._book_emissions(index_command=r"\index[iv]{WRONG}")
            plan, main, em_f = self._write_fixture(tmp, [self._base_row()], self._print_main(), em)
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em_f)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("index_command mismatch", proc.stderr)

    def test_suppress_not_in_book_emissions_succeeds(self):
        with tempfile.TemporaryDirectory() as tmp:
            suppress = self._base_row(
                disposition="suppress", emission_id="", index_command="", exclusion_reason="print_policy_excluded",
            )
            # no book_emissions row for occ:1 (suppress should NOT be in emissions)
            em_rows = [{
                "emission_id": "occ:other", "representative_occurrence_id": "occ:other",
                "emission_path": "explicit_tag",
                "site": "x:1", "index_command": r"\index[iv]{X}", "language": "oe", "variety": "",
                "display": "x", "sort_key": "x", "form_role": "evidence_form", "source_scope": "explicit_tag",
                "source_ref": "x:1", "source_occurrence_count": "1", "source_occurrence_ids": "occ:other",
            }]
            plan, main, em = self._write_fixture(tmp, [suppress], self._print_main(), em_rows)
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertEqual(proc.returncode, 0, proc.stderr[:400])

    def test_suppress_found_in_book_emissions_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            suppress = self._base_row(
                disposition="suppress", emission_id="", index_command="", exclusion_reason="print_policy_excluded",
            )
            # book_emissions has occ:1 as explicit_tag — should fail
            plan, main, em = self._write_fixture(tmp, [suppress], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main, book_emissions_tsv=em)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("unexpectedly found in book_explicit_emissions", proc.stderr)


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class ExplicitPlanCompletenessTests(unittest.TestCase):
    """Tests for CAPR_IV_REQUIRE_EXPLICIT_COMPLETENESS=1 document tracking."""

    def _base_row(self, **overrides) -> dict[str, str]:
        row = {
            "occurrence_id": "occ:1",
            "disposition": "emit",
            "emission_id": "occ:1",
            "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!ascaef@\iventry{āsceaf}{}}",
            "exclusion_reason": "",
            "language": "oe", "variety": "", "form": "āsceaf", "display": "āsceaf",
            "sort_key": "ascaef", "form_role": "evidence_form", "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
        }
        row.update(overrides)
        return row

    def _print_main(self) -> list[dict[str, str]]:
        return [{
            "language": "oe", "variety": "", "form": "āsceaf", "display": "āsceaf",
            "sort_key": "ascaef", "form_role": "evidence_form", "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "occurrence_id": "occ:1", "origin": "test", "status": "test",
        }]

    def _book_emissions(self) -> list[dict[str, str]]:
        return [{
            "emission_id": "occ:1", "representative_occurrence_id": "occ:1",
            "emission_path": "explicit_tag",
            "site": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "index_command": r"\index[iv]{02oe@\ivlangheader{Old English}{West Saxon normalization unmarked}!ascaef@\iventry{āsceaf}{}}",
            "language": "oe", "variety": "", "display": "āsceaf", "sort_key": "ascaef",
            "form_role": "evidence_form", "source_scope": "explicit_tag",
            "source_ref": "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1",
            "source_occurrence_count": "1", "source_occurrence_ids": "occ:1",
        }]

    def _write_fixture(self, tmp: str, plan_rows, main_rows, em_rows):
        p = Path(tmp)
        plan = p / "plan.tsv"
        main = p / "main.tsv"
        em = p / "em.tsv"
        _write_tsv(plan, plan_rows, EXPLICIT_PLAN_FIELDS)
        _write_tsv(main, main_rows, list(main_rows[0].keys()))
        _write_tsv(em, em_rows, list(em_rows[0].keys()))
        return plan, main, em

    def test_completeness_passes_when_all_plan_ids_seen(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan, main, em = self._write_fixture(tmp, [self._base_row()], self._print_main(), self._book_emissions())
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main,
                               book_emissions_tsv=em, require_completeness=True)
            self.assertEqual(proc.returncode, 0, proc.stderr[:400])

    def test_completeness_fails_when_plan_occurrence_missing_from_document(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Plan has 2 rows but document only has 1 span
            row2 = dict(self._base_row())
            row2["occurrence_id"] = "occ:2"
            row2["emission_id"] = "occ:2"
            row2["source_ref"] = "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2"
            em2 = dict(self._book_emissions()[0])
            em2["emission_id"] = "occ:2"
            em2["representative_occurrence_id"] = "occ:2"
            em2["source_occurrence_ids"] = "occ:2"
            em2["source_ref"] = "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2"
            plan, main, em = self._write_fixture(
                tmp, [self._base_row(), row2], self._print_main(), [self._book_emissions()[0], em2]
            )
            # Document only has occ:1, missing occ:2
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main,
                               book_emissions_tsv=em, require_completeness=True)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("completeness failure", proc.stderr)

    def test_completeness_off_allows_partial_document(self):
        """Without completeness=1, a partial document (not all plan IDs seen) is accepted."""
        with tempfile.TemporaryDirectory() as tmp:
            row2 = dict(self._base_row())
            row2["occurrence_id"] = "occ:2"
            row2["emission_id"] = "occ:2"
            row2["source_ref"] = "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2"
            em2 = dict(self._book_emissions()[0])
            em2["emission_id"] = "occ:2"
            em2["representative_occurrence_id"] = "occ:2"
            em2["source_occurrence_ids"] = "occ:2"
            em2["source_ref"] = "Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:2"
            plan, main, em = self._write_fixture(
                tmp, [self._base_row(), row2], self._print_main(), [self._book_emissions()[0], em2]
            )
            md = '[āsceaf]{.iv lang=oe sort=ascaef role=evidence_form source_ref="Germanic/docs/lexeme_reports/model_entries/0000-test.model.md:1" occ_id="occ:1"}\n'
            proc = _run_pandoc(md, explicit_mode="plan", explicit_plan_tsv=plan, print_main_tsv=main,
                               book_emissions_tsv=em, require_completeness=False)
            self.assertEqual(proc.returncode, 0, proc.stderr[:400])


class ExplicitPlanMembershipTests(unittest.TestCase):
    """Tests verifying .pred spans are excluded from plan membership."""

    def test_pred_spans_not_in_plan(self):
        """No .pred span should appear in the explicit plan."""
        rows = build_explicit_plan_from_paths()
        # All plan rows must come from explicit_tag .iv spans
        md = (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        all_spans = scan_explicit_spans(md)
        pred_occ_ids = {s["occurrence_id"] for s in all_spans if s["span_class"] == "pred" and s["occurrence_id"]}
        plan_occ_ids = {r["occurrence_id"] for r in rows}
        overlap = pred_occ_ids & plan_occ_ids
        self.assertEqual(overlap, set(), f".pred occ_ids found in plan: {sorted(overlap)[:5]}")

    def test_iv_span_with_deriv_chain_not_in_plan(self):
        """The one derivation-chain .iv span (> in form) is not in the plan."""
        rows = build_explicit_plan_from_paths()
        plan_occ_ids = {r["occurrence_id"] for r in rows}
        md = (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        all_spans = scan_explicit_spans(md)
        deriv_spans = [s for s in all_spans if s["span_class"] == "iv" and ">" in (s.get("normalized_visible_form") or "")]
        self.assertEqual(len(deriv_spans), 1)
        self.assertNotIn(deriv_spans[0]["occurrence_id"], plan_occ_ids)


class InventorySpansTests(unittest.TestCase):
    """Tests for the inventory_spans() function."""

    def test_canonical_counts(self):
        md = (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        result = inventory_spans(md)
        self.assertEqual(result.total_iv, 1497)
        self.assertEqual(result.iv_in_plan, 1496)
        self.assertEqual(result.iv_derivation_chain, 1)
        self.assertEqual(result.pred_in_plan, 0)

    def test_derivation_chain_count_is_one(self):
        md = (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        result = inventory_spans(md)
        self.assertEqual(result.iv_derivation_chain, 1)

    def test_pred_in_plan_is_zero(self):
        md = (ASSEMBLY / "capr_book_draft_alpha_01.md").read_text(encoding="utf-8")
        result = inventory_spans(md)
        self.assertEqual(result.pred_in_plan, 0)

    def test_synthetic_derivation_chain_detected(self):
        md = '[*knúbbô > *cnobba]{.iv lang=oe occ_id="test:1" source_ref="x:1"}\n'
        result = inventory_spans(md)
        self.assertEqual(result.total_iv, 1)
        self.assertEqual(result.iv_derivation_chain, 1)
        self.assertEqual(result.iv_in_plan, 0)

    def test_pred_counted_but_not_in_plan(self):
        md = '[form]{.pred lang=oe occ_id="test:pred:1" source_ref="x:1"}\n'
        result = inventory_spans(md)
        self.assertEqual(result.pred_total, 1)
        self.assertEqual(result.pred_in_plan, 0)
        self.assertEqual(result.total_iv, 0)


if __name__ == "__main__":
    unittest.main()

