#!/usr/bin/env python3
"""Permanent tests for Old English Index Verborum variety infrastructure.

Run: cd Germanic/tests && python3 -m unittest test_index_verborum_variety
"""
from __future__ import annotations

import csv
import importlib
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK = REPO_ROOT / "Germanic/docs/book"
TOOLS = REPO_ROOT / "Germanic/tools"
FILTER_LUA = TOOLS / "index_verborum_filter.lua"

import sys

sys.path.insert(0, str(TOOLS))
import index_verborum_render as ivr  # noqa: E402

VARIETY_HEADER = ["language", "code", "title", "printed_label", "parent", "display_order", "suppress_label", "assignable", "active", "notes"]
CANON_ROWS = [
    ["oe", "ws", "West Saxon", "", "", "1", "1", "0", "1", "parent"],
    ["oe", "ews", "Early West Saxon", "EWS", "ws", "2", "0", "1", "1", ""],
    ["oe", "lws", "Late West Saxon", "LWS", "ws", "3", "0", "1", "1", ""],
    ["oe", "angl", "Anglian", "Angl.", "", "4", "0", "1", "1", ""],
    ["oe", "merc", "Mercian", "Merc.", "angl", "5", "0", "1", "1", ""],
    ["oe", "north", "Northumbrian", "North.", "angl", "6", "0", "1", "1", ""],
    ["oe", "kent", "Kentish", "Kent.", "", "7", "0", "1", "1", ""],
]


def write_tsv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as h:
        w = csv.writer(h, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def load_variety(rows: list[list[str]]) -> ivr.VarietyRegistry:
    with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as f:
        path = Path(f.name)
    write_tsv(path, VARIETY_HEADER, rows)
    try:
        return ivr.load_variety_registry(path)
    finally:
        path.unlink(missing_ok=True)


class VarietyRegistryTests(unittest.TestCase):
    def test_valid_registry_loads(self):
        reg = load_variety(CANON_ROWS)
        self.assertEqual(len(reg.entries), 7)

    def test_canonical_parents(self):
        reg = load_variety(CANON_ROWS)
        self.assertEqual(reg.get("merc").parent, "angl")
        self.assertEqual(reg.get("north").parent, "angl")
        self.assertEqual(reg.get("ews").parent, "ws")
        self.assertEqual(reg.get("lws").parent, "ws")

    def test_ws_active_nonassignable_no_label(self):
        reg = load_variety(CANON_ROWS)
        ws = reg.get("ws")
        self.assertTrue(ws.active)
        self.assertFalse(ws.assignable)
        self.assertEqual(reg.printed_label("ws"), "")

    def test_variety_ws_fails_on_occurrence(self):
        reg = load_variety(CANON_ROWS)
        with self.assertRaises(ValueError):
            reg.validate_occurrence("oe", "ws")

    def test_unknown_variety_fails(self):
        reg = load_variety(CANON_ROWS)
        with self.assertRaises(ValueError):
            reg.validate_occurrence("oe", "xyz")

    def test_wrong_language_fails(self):
        reg = load_variety(CANON_ROWS)
        with self.assertRaises(ValueError):
            reg.validate_occurrence("pgmc", "merc")

    def test_inactive_variety_fails(self):
        rows = [r[:] for r in CANON_ROWS]
        rows.append(["oe", "temp", "Temp", "Tmp.", "", "8", "0", "0", "0", ""])  # inactive, non-assignable
        reg = load_variety(rows)
        with self.assertRaises(ValueError):
            reg.validate_occurrence("oe", "temp")

    def test_duplicate_code_fails(self):
        rows = [r[:] for r in CANON_ROWS] + [["oe", "merc", "Dup", "D.", "", "9", "0", "1", "1", ""]]
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_duplicate_active_display_order_fails(self):
        rows = [r[:] for r in CANON_ROWS]
        rows[2][5] = "2"  # lws shares display_order 2 with ews
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_invalid_boolean_fails(self):
        for col in (6, 7, 8):  # suppress_label, assignable, active
            rows = [r[:] for r in CANON_ROWS]
            rows[3][col] = "2"
            with self.assertRaises(ValueError):
                load_variety(rows)

    def test_missing_parent_fails(self):
        rows = [r[:] for r in CANON_ROWS]
        rows[4][4] = "ghost"
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_inactive_parent_of_active_child_fails(self):
        rows = [r[:] for r in CANON_ROWS]
        rows[0][8] = "0"  # ws inactive; ews/lws active children
        # ws inactive & non-assignable is fine, but active child of inactive parent must fail
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_cross_language_parent_fails(self):
        rows = [r[:] for r in CANON_ROWS]
        rows.append(["pgmc", "pchild", "PC", "PC.", "angl", "8", "0", "1", "1", ""])
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_cyclic_hierarchy_fails(self):
        rows = [
            ["oe", "a", "A", "A.", "b", "1", "0", "1", "1", ""],
            ["oe", "b", "B", "B.", "a", "2", "0", "1", "1", ""],
        ]
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_assignable_must_be_active(self):
        rows = [r[:] for r in CANON_ROWS]
        rows.append(["oe", "q", "Q", "Q.", "", "8", "0", "1", "0", ""])  # assignable but inactive
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_hierarchy_no_duplicate_parent_entries(self):
        reg = load_variety(CANON_ROWS)
        # Registry is a flat mapping; parents are metadata, never duplicated as entries.
        self.assertEqual(len([c for c in reg.entries if c == "angl"]), 1)

    def test_assignable_requires_printed_label(self):
        rows = [r[:] for r in CANON_ROWS]
        rows[3][3] = ""  # angl: assignable but blank printed_label
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_assignable_must_not_suppress_label(self):
        rows = [r[:] for r in CANON_ROWS]
        rows[3][6] = "1"  # angl: assignable with suppress_label=1
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_suppressed_must_be_nonassignable(self):
        rows = [r[:] for r in CANON_ROWS]
        # A suppressed + assignable row is contradictory (invisible-yet-usable).
        rows.append(["oe", "sx", "SX", "SX.", "", "8", "1", "1", "1", ""])
        with self.assertRaises(ValueError):
            load_variety(rows)

    def test_canonical_registry_still_valid(self):
        # The canonical on-disk registry must continue to pass unchanged.
        reg = ivr.load_variety_registry()
        self.assertEqual(reg.printed_label("ws"), "")
        self.assertFalse(reg.get("ws").assignable)
        self.assertTrue(reg.get("ws").active)


class RenderingTests(unittest.TestCase):
    def setUp(self):
        self.lang = ivr.load_language_registry()
        self.var = load_variety(CANON_ROWS)

    def cmd(self, display, variety):
        return ivr.index_command("oe", ivr.transliterate if False else "sort", display, variety, lang_meta=self.lang, var_registry=self.var)

    def render(self, display, variety, sort="stregan"):
        return ivr.index_command("oe", sort, display, variety, lang_meta=self.lang, var_registry=self.var)

    def test_blank_no_suffix(self):
        out = self.render("strēgan", "")
        self.assertIn(r"\ivoeentry{strēgan}{}", out)

    def test_labels(self):
        cases = {"ews": "EWS", "lws": "LWS", "angl": "Angl.", "merc": "Merc.", "north": "North.", "kent": "Kent."}
        for code, label in cases.items():
            out = self.render("strēgan", code)
            self.assertIn(rf"\ivoeentry{{strēgan}}{{{label}}}", out)

    def test_no_ws_rendering(self):
        with self.assertRaises(ValueError):
            self.var.validate_occurrence("oe", "ws")

    def test_reconstructed_single_asterisk(self):
        out = self.render("*strīeġan", "angl", sort="striegan")
        self.assertIn(r"\ivoeentry{*strīeġan}{Angl.}", out)
        self.assertEqual(out.count("*strīeġan"), 1)
        self.assertNotIn("**", out)

    def test_hidden_discriminator_in_sort_only(self):
        out = self.render("strēgan", "merc")
        # display_order for merc is 5 -> disc '~05' appended to sort side, not display
        self.assertIn("stregan~05@", out)
        self.assertNotIn("strēgan~05", out)
        self.assertNotIn("strēgan05", out)

    def test_index_command_fail_closed_ws(self):
        # index_command() must reject variety=ws itself, not rely on callers.
        with self.assertRaises(ValueError):
            self.render("strēgan", "ws")

    def test_index_command_fail_closed_unknown(self):
        with self.assertRaises(ValueError):
            self.render("strēgan", "zzz")

    def test_index_command_fail_closed_inactive(self):
        rows = [r[:] for r in CANON_ROWS]
        rows.append(["oe", "old", "Old", "Old.", "", "8", "0", "0", "0", ""])  # inactive
        var = load_variety(rows)
        with self.assertRaises(ValueError):
            ivr.index_command("oe", "sort", "form", "old", lang_meta=self.lang, var_registry=var)

    def test_index_command_fail_closed_wrong_language(self):
        # An Old English variety must not be usable on another language.
        with self.assertRaises(ValueError):
            ivr.index_command("pgmc", "sort", "form", "merc", lang_meta=self.lang, var_registry=self.var)

    def test_index_command_rejects_separator_in_sort_key(self):
        with self.assertRaises(ValueError):
            ivr.index_command("oe", "so~rt", "form", "merc", lang_meta=self.lang, var_registry=self.var)

    def test_collision_proof_sort_fields_distinct(self):
        # Old scheme: blank "col05" and merc "col" both -> "col05". New scheme
        # separates them, so the two hidden sort fields must differ.
        blank = ivr.index_command("oe", "col05", "col05", "", lang_meta=self.lang, var_registry=self.var)
        merc = ivr.index_command("oe", "col", "col", "merc", lang_meta=self.lang, var_registry=self.var)
        blank_sort = blank.split("!", 1)[1].split("@", 1)[0]
        merc_sort = merc.split("!", 1)[1].split("@", 1)[0]
        self.assertNotEqual(blank_sort, merc_sort)
        self.assertEqual(blank_sort, "col05")
        self.assertEqual(merc_sort, "col~05")


class LanguageHeaderTests(unittest.TestCase):
    def test_canonical_note_blank(self):
        lang = ivr.load_language_registry()  # canonical
        oe = lang["oe"]
        self.assertEqual(oe.index_note, "")
        self.assertEqual(ivr.language_header_tex(oe), r"\ivlangheader{Old English}{}")

    def test_fixture_note_renders(self):
        fixture = REPO_ROOT / "Germanic/tests/fixtures/variety/languages_with_note.tsv"
        lang = ivr.load_language_registry(fixture)
        oe = lang["oe"]
        self.assertEqual(
            ivr.language_header_tex(oe),
            r"\ivlangheader{Old English}{West Saxon normalization unmarked}",
        )
        # other language keeps blank note
        self.assertEqual(ivr.language_header_tex(lang["pgmc"]), r"\ivlangheader{Proto-Germanic}{}")


class DecisionMatchingTests(unittest.TestCase):
    def setUp(self):
        self.biv = importlib.import_module("build_index_verborum")

    def occ(self, variety):
        return self.biv.ProductionOccurrence(
            language="oe", form="strēgan", display="strēgan", sort_key="stregan",
            form_role="comparison_form", source_scope="explicit_tag",
            source_ref="x.md", variety=variety,
        )

    def test_blank_decision_not_match_labelled(self):
        d = {"language": "oe", "form": "strēgan", "variety": ""}
        self.assertFalse(self.biv.print_decision_matches_row(d, self.occ("merc")))

    def test_exact_and_parent_nonmatch(self):
        self.assertFalse(self.biv.print_decision_matches_row({"variety": "angl"}, self.occ("merc")))
        self.assertFalse(self.biv.print_decision_matches_row({"variety": "angl"}, self.occ("north")))
        self.assertFalse(self.biv.print_decision_matches_row({"variety": "merc"}, self.occ("angl")))
        self.assertFalse(self.biv.print_decision_matches_row({"variety": "ews"}, self.occ("")))
        self.assertTrue(self.biv.print_decision_matches_row({"variety": "merc"}, self.occ("merc")))

    def test_override_exact_variety(self):
        self.assertTrue(self.biv.override_matches({"form": "strēgan", "variety": "merc"}, form="strēgan", variety="merc"))
        self.assertFalse(self.biv.override_matches({"form": "strēgan", "variety": "angl"}, form="strēgan", variety="merc"))
        self.assertFalse(self.biv.override_matches({"form": "strēgan"}, form="strēgan", variety="merc"))


class RealCorpusInvariantTests(unittest.TestCase):
    def _rows(self, name):
        with (BOOK / name).open(encoding="utf-8", newline="") as h:
            return list(csv.DictReader(h, delimiter="\t"))

    def test_no_real_corpus_variety(self):
        forms = self._rows("index_verborum_forms.tsv")
        self.assertTrue(all((r.get("variety", "") or "") == "" for r in forms))

    def test_no_real_ws(self):
        for name in ("index_verborum_forms.tsv", "index_verborum_print_main.tsv"):
            for r in self._rows(name):
                self.assertNotEqual((r.get("variety", "") or ""), "ws")

    def test_permanent_membership_invariants(self):
        """Relational invariants that must hold BEFORE AND AFTER variety annotation.

        These do not hard-code corpus sizes. They protect against accidental
        addition/removal/reclassification while remaining valid once source-backed
        varieties are later assigned (which may split one lexical form into several
        printed entries but must not change production occurrence membership).
        """
        forms = self._rows("index_verborum_forms.tsv")
        pm = self._rows("index_verborum_print_main.tsv")
        pu = self._rows("index_verborum_print_unique.tsv")
        pe = self._rows("index_verborum_print_excluded.tsv")

        # print_main and print_excluded partition the production forms exactly.
        self.assertEqual(len(pm) + len(pe), len(forms),
                         "print_main + print_excluded must partition production occurrences")
        # Every printed/excluded occurrence is a real production occurrence.
        forms_ident = {(r["language"], r.get("variety", ""), r["form"], r["display"],
                        r["form_role"], r["source_scope"], r["source_ref"]) for r in forms}
        for label, rows in (("print_main", pm), ("print_excluded", pe)):
            for r in rows:
                ident = (r["language"], r.get("variety", ""), r["form"], r["display"],
                         r["form_role"], r["source_scope"], r["source_ref"])
                self.assertIn(ident, forms_ident, f"{label} row absent from production forms: {ident}")
        # Unique printed entries never exceed printed occurrences, and one printed
        # entry exists per (language, display, sort_key, printed_variety) group of
        # print_main (this is exactly the collapsing key used by the generator).
        expected_unique = {(r["language"], r["display"], r["sort_key"],
                            self._printed_variety(r.get("variety", ""))) for r in pm}
        self.assertEqual(len(pu), len(expected_unique),
                         "unique printed entries must equal distinct (language, display, sort_key, printed_variety) of print_main")

    def _printed_variety(self, variety):
        variety = (variety or "").strip()
        if not variety:
            return ""
        return ivr.load_variety_registry().printed_label(variety)

    def test_pre_annotation_baseline_snapshot(self):
        """Task-specific baseline for THIS infrastructure pass only.

        These exact counts prove the infrastructure pass did not alter corpus
        membership. They are expected to change legitimately once source-backed
        varieties are assigned (a form may then yield multiple printed entries),
        at which point this single snapshot test — and not the permanent
        invariants above — should be updated deliberately.
        """
        PRE_ANNOTATION_BASELINE = {
            "production_occurrences": 2259,
            "production_unique_forms": 1141,
            "print_main_occurrences": 2171,
            "unique_printed_entries": 1041,
            "print_excluded_occurrences": 88,
        }
        forms = self._rows("index_verborum_forms.tsv")
        pm = self._rows("index_verborum_print_main.tsv")
        pu = self._rows("index_verborum_print_unique.tsv")
        pe = self._rows("index_verborum_print_excluded.tsv")
        self.assertEqual(len(forms), PRE_ANNOTATION_BASELINE["production_occurrences"])
        self.assertEqual(len({(r["language"], r["form"]) for r in forms}),
                         PRE_ANNOTATION_BASELINE["production_unique_forms"])
        self.assertEqual(len(pm), PRE_ANNOTATION_BASELINE["print_main_occurrences"])
        self.assertEqual(len(pu), PRE_ANNOTATION_BASELINE["unique_printed_entries"])
        self.assertEqual(len(pe), PRE_ANNOTATION_BASELINE["print_excluded_occurrences"])

    def test_canonical_language_note_blank(self):
        with (BOOK / "index_verborum_languages.tsv").open(encoding="utf-8", newline="") as h:
            for r in csv.DictReader(h, delimiter="\t"):
                self.assertEqual((r.get("index_note", "") or ""), "")

    def test_lf_line_endings(self):
        import glob
        for path in glob.glob(str(BOOK / "index_verborum_*.tsv")):
            data = Path(path).read_bytes()
            self.assertNotIn(b"\r\n", data, f"CRLF found in {path}")


class RegistryTexTests(unittest.TestCase):
    def test_single_index_streams(self):
        tex = (REPO_ROOT / "Germanic/docs/assembly/book_draft_index_registry.tex").read_text(encoding="utf-8")
        self.assertEqual(tex.count(r"\makeindex[name=iv"), 1)
        self.assertIn(r"\ivlangheader", tex)
        self.assertIn(r"\ivoeentry", tex)
        self.assertNotIn(r"\makeindex[name=oe", tex)


@unittest.skipIf(shutil.which("pandoc") is None, "pandoc not available")
class LuaParityTests(unittest.TestCase):
    """Prove Lua and Python construct equivalent \\index[iv] bodies."""

    def _run_pandoc(self, markdown: str, env: dict[str, str]) -> str:
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "in.md"
            src.write_text(markdown, encoding="utf-8")
            full_env = dict(os.environ)
            full_env.update(env)
            proc = subprocess.run(
                ["pandoc", "--from", "markdown", "--to", "latex",
                 "--lua-filter", str(FILTER_LUA), str(src)],
                capture_output=True, text=True, env=full_env,
            )
            if proc.returncode != 0:
                self.fail(f"pandoc failed: {proc.stderr}")
            return proc.stdout

    def test_lua_python_parity_and_variety(self):
        lang = ivr.load_language_registry()
        var = ivr.load_variety_registry()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            # print_main fixture whitelisting the explicit tags (with variety)
            pm = tmp / "pm.tsv"
            header = ["language", "variety", "form", "display", "sort_key", "form_role", "source_scope", "source_ref", "origin", "status"]
            cases = [
                ("", "strēgan", "stregan"),
                ("angl", "strēgan", "stregan"),
                ("merc", "geafa", "geafa"),
                ("ews", "stīeran", "stieran"),
            ]
            rows = []
            md_lines = []
            for variety, form, sort in cases:
                ref = "Germanic/docs/assembly/capr_book_intro_alpha_01.md:1"
                rows.append(["oe", variety, form, form, sort, "comparison_form", "explicit_tag", ref, "x", "auto"])
                va = f" variety={variety}" if variety else ""
                md_lines.append(f"[{form}]{{.iv lang=oe{va} sort={sort} role=comparison_form source_ref=\"{ref}\"}}")
            with pm.open("w", encoding="utf-8", newline="") as h:
                w = csv.writer(h, delimiter="\t", lineterminator="\n")
                w.writerow(header)
                w.writerows(rows)
            env = {
                "CAPR_IV_PRINT_MAIN_TSV": str(pm),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
                "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            }
            out = self._run_pandoc("\n\n".join(md_lines) + "\n", env)
            for variety, form, sort in cases:
                py = ivr.index_command("oe", sort, form, variety, lang_meta=lang, var_registry=var)
                self.assertIn(py, out, f"Lua output missing Python-equivalent command for variety={variety!r}")

    def test_lua_rejects_ws(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pm = tmp / "pm.tsv"
            header = ["language", "variety", "form", "display", "sort_key", "form_role", "source_scope", "source_ref", "origin", "status"]
            ref = "Germanic/docs/assembly/capr_book_intro_alpha_01.md:1"
            with pm.open("w", encoding="utf-8", newline="") as h:
                w = csv.writer(h, delimiter="\t", lineterminator="\n")
                w.writerow(header)
                w.writerow(["oe", "ws", "form", "form", "form", "comparison_form", "explicit_tag", ref, "x", "auto"])
            env = dict(os.environ)
            env.update({
                "CAPR_IV_PRINT_MAIN_TSV": str(pm),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
                "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            })
            src = tmp / "in.md"
            src.write_text(f"[form]{{.iv lang=oe variety=ws sort=form source_ref=\"{ref}\"}}\n", encoding="utf-8")
            proc = subprocess.run(
                ["pandoc", "--from", "markdown", "--to", "latex", "--lua-filter", str(FILTER_LUA), str(src)],
                capture_output=True, text=True, env=env,
            )
            self.assertNotEqual(proc.returncode, 0, "pandoc must fail on variety=ws")


if __name__ == "__main__":
    unittest.main()
