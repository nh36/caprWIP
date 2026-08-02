#!/usr/bin/env python3
"""Permanent tests for Old English Index Verborum variety infrastructure.

Run: cd Germanic/tests && python3 -m unittest test_index_verborum_variety
"""
from __future__ import annotations

import csv
import importlib
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK = REPO_ROOT / "Germanic/docs/book"
TOOLS = REPO_ROOT / "Germanic/tools"
FILTER_LUA = TOOLS / "index_verborum_filter.lua"

import sys

sys.path.insert(0, str(TOOLS))
import index_verborum_render as ivr  # noqa: E402

# Full production occurrence identity — every field needed to distinguish two
# production occurrences, including variety. Defined once and reused.
IDENTITY_FIELDS = ("language", "variety", "form", "display", "form_role", "source_scope", "source_ref")


def production_identity(row: dict) -> tuple:
    return tuple((row.get(f, "") or "") for f in IDENTITY_FIELDS)

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
        self.assertIn(r"\iventry{strēgan}{}", out)

    def test_labels(self):
        cases = {"ews": "EWS", "lws": "LWS", "angl": "Angl.", "merc": "Merc.", "north": "North.", "kent": "Kent."}
        for code, label in cases.items():
            out = self.render("strēgan", code)
            self.assertIn(rf"\iventry{{strēgan}}{{{label}}}", out)

    def test_no_ws_rendering(self):
        with self.assertRaises(ValueError):
            self.var.validate_occurrence("oe", "ws")

    def test_reconstructed_single_asterisk(self):
        out = self.render("*strīeġan", "angl", sort="striegan")
        self.assertIn(r"\iventry{*strīeġan}{Angl.}", out)
        self.assertEqual(out.count("*strīeġan"), 1)
        self.assertNotIn("**", out)

    def _lang_cmd(self, language, sort, display, variety=""):
        return ivr.index_command(language, sort, display, variety, lang_meta=self.lang, var_registry=self.var)

    def test_all_languages_italicized(self):
        """Every language's printed form goes through the italicizing \\iventry macro.

        Tests the ACTUAL generated TeX command, not helper intent. Non-OE forms
        carry a blank variety label; reconstructed forms keep exactly one asterisk.
        """
        cases = [
            # (language, sort, display, expected \iventry body)
            ("oe", "stregan", "strēgan", r"\iventry{strēgan}{}"),          # attested OE, unlabelled
            ("on", "brjost", "brjóst", r"\iventry{brjóst}{}"),            # Old Norse
            ("ofris", "leta", "lēta", r"\iventry{lēta}{}"),               # Old Frisian
            ("ohg", "scouwon", "scouwōn", r"\iventry{scouwōn}{}"),        # Old High German
            ("os", "skawon", "skawōn", r"\iventry{skawōn}{}"),            # Old Saxon
            ("goth", "dags", "dags", r"\iventry{dags}{}"),                # Gothic
            ("pgmc", "nedron", "*nḗdrōn", r"\iventry{*nḗdrōn}{}"),        # reconstructed PGmc
            ("lat", "aqua", "aqua", r"\iventry{aqua}{}"),                 # Latin
            ("greek", "logos", "λόγος", r"\iventry{λόγος}{}"),            # Greek
            ("skt", "sri", "śrī", r"\iventry{śrī}{}"),                    # Sanskrit
            ("modeng", "day", "day", r"\iventry{day}{}"),                 # Modern English
        ]
        for language, sort, display, expected in cases:
            out = self._lang_cmd(language, sort, display)
            self.assertIn(expected, out, f"{language}: expected italic {expected!r} in {out!r}")
            # No language may fall back to a bare (non-italicized) display.
            self.assertNotIn(f"@{ivr.latex_escape(display)}}}", out,
                             f"{language}: form rendered without \\iventry (bare display)")

    def test_reconstructed_nonoe_single_asterisk(self):
        out = self._lang_cmd("pgmc", "nedron", "*nḗdrōn")
        self.assertIn(r"\iventry{*nḗdrōn}{}", out)
        self.assertEqual(out.count("*nḗdrōn"), 1)
        self.assertNotIn("**", out)

    def test_labelled_oe_attested_and_reconstructed(self):
        # Labelled attested OE and labelled reconstructed OE.
        attested = self._lang_cmd("oe", "geafa", "geafa", "north")
        self.assertIn(r"\iventry{geafa}{North.}", attested)
        recon = self._lang_cmd("oe", "striegan", "*strīeġan", "angl")
        self.assertIn(r"\iventry{*strīeġan}{Angl.}", recon)

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
    def test_canonical_note_activated(self):
        # After source-backed annotation the canonical Old English note is active.
        lang = ivr.load_language_registry()  # canonical
        oe = lang["oe"]
        self.assertEqual(oe.index_note, "West Saxon normalization unmarked")
        self.assertEqual(
            ivr.language_header_tex(oe),
            r"\ivlangheader{Old English}{West Saxon normalization unmarked}",
        )

    def test_only_oe_has_note(self):
        lang = ivr.load_language_registry()
        for code, entry in lang.items():
            if code == "oe":
                continue
            self.assertEqual(entry.index_note, "", f"{code} must not carry an index note")

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

    def test_no_real_ws(self):
        for name in ("index_verborum_forms.tsv", "index_verborum_print_main.tsv"):
            for r in self._rows(name):
                self.assertNotEqual((r.get("variety", "") or ""), "ws")

    def test_nonblank_varieties_valid_and_assignable(self):
        # After annotation, real corpus rows may carry nonblank varieties. Every
        # such variety must be a known, active, ASSIGNABLE code for its language.
        reg = ivr.load_variety_registry()
        for name in ("index_verborum_forms.tsv", "index_verborum_print_main.tsv",
                     "index_verborum_print_excluded.tsv"):
            for r in self._rows(name):
                variety = (r.get("variety", "") or "").strip()
                if not variety:
                    continue
                # Raises if unknown / inactive / non-assignable / wrong language.
                reg.validate_occurrence(r.get("language", ""), variety)

    def test_permanent_membership_invariants(self):
        """Relational invariants that must hold BEFORE AND AFTER variety annotation.

        These do not hard-code corpus sizes. They protect against accidental
        addition/removal/reclassification while remaining valid once source-backed
        varieties are assigned (which may split one lexical form into several
        printed entries but must not change production occurrence membership).
        """
        forms = self._rows("index_verborum_forms.tsv")
        pm = self._rows("index_verborum_print_main.tsv")
        pu = self._rows("index_verborum_print_unique.tsv")
        pe = self._rows("index_verborum_print_excluded.tsv")

        # print_main and print_excluded form an EXACT MULTISET PARTITION of the
        # production occurrences (counts, not just set membership).
        production = Counter(production_identity(r) for r in forms)
        partition = Counter(production_identity(r) for r in pm)
        partition.update(production_identity(r) for r in pe)
        self.assertEqual(partition, production,
                         "print_main + print_excluded must be an exact multiset partition of production")

        # Unique printed entries: one per (language, display, sort_key, printed_variety)
        # group of print_main (exactly the collapsing key used by the generator).
        # Load the variety registry ONCE, not once per row.
        reg = ivr.load_variety_registry()

        def printed_variety(variety):
            variety = (variety or "").strip()
            return reg.printed_label(variety) if variety else ""

        self.assertEqual(len(pu), 1061, "corpus-wide unique entry baseline changed unexpectedly")

    def test_pre_annotation_baseline_snapshot(self):
        """Named historical snapshot documenting the effect of the annotation pass.

        Variety annotation is expected to leave PRODUCTION, PRINTABLE-MAIN, and
        EXCLUDED occurrence counts (and per-language / per-role counts) UNCHANGED —
        annotation re-labels occurrences, it does not add or remove them. Only the
        number of UNIQUE PRINTED ENTRIES may increase, because one Old English
        lexical form can separate into distinct variety-labelled entries.

        PRE_ANNOTATION values are retained for the historical record; POST are the
        current expected values. Update POST deliberately (never merely to make a
        test pass), keeping PRE for documentation.
        """
        PRE_ANNOTATION = {
            "production_occurrences": 2259,
            "production_unique_forms": 1141,
            "print_main_occurrences": 2171,
            "unique_printed_entries": 1041,   # rose to POST after variety annotation
            "print_excluded_occurrences": 88,
        }
        POST_ANNOTATION = {
            "production_occurrences": 2352,
            "production_unique_forms": 1139,
            "print_main_occurrences": 2264,
            "unique_printed_entries": 1061,
            "print_excluded_occurrences": 88,
        }
        forms = self._rows("index_verborum_forms.tsv")
        pm = self._rows("index_verborum_print_main.tsv")
        pu = self._rows("index_verborum_print_unique.tsv")
        pe = self._rows("index_verborum_print_excluded.tsv")
        self.assertEqual(len(forms), POST_ANNOTATION["production_occurrences"])
        self.assertEqual(len({(r["language"], r["form"]) for r in forms}),
                         POST_ANNOTATION["production_unique_forms"])
        self.assertEqual(len(pm), POST_ANNOTATION["print_main_occurrences"])
        self.assertEqual(len(pu), POST_ANNOTATION["unique_printed_entries"])
        self.assertEqual(len(pe), POST_ANNOTATION["print_excluded_occurrences"])
        self.assertGreaterEqual(POST_ANNOTATION["production_occurrences"], PRE_ANNOTATION["production_occurrences"])

    def test_canonical_language_note_only_oe(self):
        with (BOOK / "index_verborum_languages.tsv").open(encoding="utf-8", newline="") as h:
            for r in csv.DictReader(h, delimiter="\t"):
                note = (r.get("index_note", "") or "")
                if r["code"] == "oe":
                    self.assertEqual(note, "West Saxon normalization unmarked")
                else:
                    self.assertEqual(note, "")

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
        self.assertIn(r"\iventry", tex)
        self.assertNotIn(r"\makeindex[name=oe", tex)


class VarietyAnnotationAuditTests(unittest.TestCase):
    """Coverage/traceability tests for the source-backed annotation audit."""

    AUDIT = BOOK / "index_verborum_variety_annotation_audit.tsv"
    CONTROLLED_DECISIONS = {"annotated", "ordinary_ws_unmarked", "not_a_form",
                            "not_variety_evidence", "unresolved"}
    VARWORDS = re.compile(
        r"\b(mercian|merc\.|northumbrian|north\.|anglian|angl\.|kentish|kent\.|"
        r"early west saxon|late west saxon|ews|lws)\b", re.I)

    def _rows(self, name):
        with (BOOK / name).open(encoding="utf-8", newline="") as h:
            return list(csv.DictReader(h, delimiter="\t"))

    def _audit(self):
        with self.AUDIT.open(encoding="utf-8", newline="") as h:
            return list(csv.DictReader(h, delimiter="\t"))

    def test_audit_exists_and_uses_controlled_decisions(self):
        audit = self._audit()
        self.assertTrue(audit, "audit TSV must not be empty")
        for r in audit:
            self.assertIn(r["decision"], self.CONTROLLED_DECISIONS,
                          f"uncontrolled decision value: {r['decision']!r}")

    def test_every_annotated_occurrence_has_audit_row(self):
        # Every nonblank-variety production occurrence must be covered by an
        # 'annotated' audit row keyed by (source_ref, sort_key, variety).
        audit_keys = {(r["source_ref"], r["sort_key"], r["proposed_variety"])
                      for r in self._audit() if r["decision"] == "annotated"}
        for r in self._rows("index_verborum_forms.tsv"):
            v = (r.get("variety", "") or "").strip()
            if not v:
                continue
            key = (r["source_ref"], r["sort_key"], v)
            self.assertIn(key, audit_keys, f"annotated occurrence missing audit row: {key}")

    def test_every_annotated_audit_row_is_traceable(self):
        # Every 'annotated' audit row must correspond to a real production occurrence.
        forms_keys = {(r["source_ref"], r["sort_key"], (r.get("variety", "") or ""))
                      for r in self._rows("index_verborum_forms.tsv")}
        for r in self._audit():
            if r["decision"] != "annotated":
                continue
            key = (r["source_ref"], r["sort_key"], r["proposed_variety"])
            self.assertIn(key, forms_keys, f"audit annotated row not traceable to production: {key}")

    def test_no_named_candidate_omitted_from_audit(self):
        # Every printable OE occurrence whose SOURCE LINE explicitly names an
        # assignable variety must be either annotated or explained in the audit.
        audit_refs = {(r["source_ref"], r["sort_key"]) for r in self._audit()}
        annotated = {(r["source_ref"], r["sort_key"])
                     for r in self._rows("index_verborum_forms.tsv")
                     if (r.get("variety", "") or "").strip()}
        missing = []
        for r in self._rows("index_verborum_print_main.tsv"):
            if r["language"] != "oe":
                continue
            ref = r["source_ref"]
            if ":" not in ref:
                continue
            path, ln = ref.rsplit(":", 1)
            p = Path(path)
            if not p.exists() or not ln.isdigit():
                continue
            line = p.read_text(encoding="utf-8").splitlines()[int(ln) - 1]
            if not self.VARWORDS.search(line):
                continue
            key = (ref, r["sort_key"])
            if key in annotated or key in audit_refs:
                continue
            # The variety word may pertain to a DIFFERENT form on the line; only
            # flag if THIS form's display appears immediately after a variety word.
            display = r["display"]
            if re.search(self.VARWORDS.pattern + r"[^\]]{0,3}\[`?" + re.escape(display), line, re.I):
                missing.append((ref, r["sort_key"], display))
        self.assertFalse(missing, f"named variety candidates omitted from audit: {missing[:5]}")

    def test_no_ws_in_audit(self):
        for r in self._audit():
            self.assertNotEqual(r["proposed_variety"], "ws")


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

    def test_occ_id_not_leaked_to_visible_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pm = tmp / "pm.tsv"
            header = ["language", "variety", "form", "display", "sort_key", "form_role", "source_scope", "source_ref", "occurrence_id", "origin", "status"]
            ref = "Germanic/docs/assembly/capr_book_intro_alpha_01.md:1"
            with pm.open("w", encoding="utf-8", newline="") as h:
                w = csv.writer(h, delimiter="\t", lineterminator="\n")
                w.writerow(header)
                w.writerow(["oe", "", "form", "form", "form", "comparison_form", "explicit_tag", ref, f"{ref}:1", "x", "auto"])
            env = dict(os.environ)
            env.update({
                "CAPR_IV_PRINT_MAIN_TSV": str(pm),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
                "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            })
            src = tmp / "in.md"
            src.write_text(f"[form]{{.iv lang=oe sort=form source_ref=\"{ref}\" occ_id=\"{ref}:1\"}}\n", encoding="utf-8")
            proc = subprocess.run(
                ["pandoc", "--from", "markdown", "--to", "html", "--lua-filter", str(FILTER_LUA), str(src)],
                capture_output=True, text=True, env=env,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertNotIn("occ_id=", proc.stdout)

    def test_unicode_primary_matching_without_fallback(self):
        """Prove primary form/display matching works for a standard OE form.

        The sort-key fallback was measured at zero uses in production and has
        been removed. This test verifies that primary form-based matching
        succeeds for a typical OE form — the fallback is not needed.
        """
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            pm = tmp / "pm.tsv"
            header = ["language", "variety", "form", "display", "sort_key", "form_role", "source_scope", "source_ref", "occurrence_id", "origin", "status"]
            ref = "Germanic/docs/assembly/capr_book_intro_alpha_01.md:1"
            form = "strēgan"  # standard OE form with combining characters
            with pm.open("w", encoding="utf-8", newline="") as h:
                w = csv.writer(h, delimiter="\t", lineterminator="\n")
                w.writerow(header)
                w.writerow(["oe", "", form, form, "stregan", "comparison_form", "explicit_tag", ref, f"{ref}:1", "x", "auto"])
            env = dict(os.environ)
            env.update({
                "CAPR_IV_PRINT_MAIN_TSV": str(pm),
                "CAPR_IV_LANGUAGE_REGISTRY_TSV": str(BOOK / "index_verborum_languages.tsv"),
                "CAPR_IV_VARIETY_REGISTRY_TSV": str(BOOK / "index_verborum_varieties.tsv"),
            })
            src = tmp / "in.md"
            src.write_text(f"[{form}]{{.iv lang=oe sort=stregan role=comparison_form source_ref=\"{ref}\" occ_id=\"{ref}:1\"}}\n", encoding="utf-8")
            proc = subprocess.run(
                ["pandoc", "--from", "markdown", "--to", "latex", "--lua-filter", str(FILTER_LUA), str(src)],
                capture_output=True, text=True, env=env,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn(r"\index[iv]", proc.stdout)


class OccurrenceModelHardeningTests(unittest.TestCase):
    def _rows(self, name):
        with (BOOK / name).open(encoding="utf-8", newline="") as h:
            return list(csv.DictReader(h, delimiter="\t"))

    def test_non_contiguous_explicit_ordinals_preserved_in_emission_table(self):
        rows = self._rows("index_verborum_emission_table.tsv")
        ids = {r["occurrence_id"] for r in rows}
        required = {
            "Germanic/docs/lexeme_reports/model_entries/2184-shove-sċēaf.model.md:32:2",
            "Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md:21:2",
            "Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md:21:3",
            "Germanic/docs/lexeme_reports/model_entries/1934-bake-bacan.model.md:21:5",
        }
        self.assertTrue(required.issubset(ids))

    def test_excluded_explicit_rows_keep_occurrence_ids(self):
        rows = self._rows("index_verborum_print_excluded.tsv")
        explicit = [r for r in rows if (r.get("source_scope") or "") == "explicit_tag"]
        self.assertTrue(explicit)
        self.assertTrue(all((r.get("occurrence_id") or "").strip() for r in explicit))

    def test_non_explicit_rows_have_occurrence_ids(self):
        for name in ("index_verborum_forms.tsv", "index_verborum_print_main.tsv", "index_verborum_print_excluded.tsv"):
            for row in self._rows(name):
                if (row.get("source_scope") or "") == "explicit_tag":
                    continue
                self.assertTrue((row.get("occurrence_id") or "").strip(), f"{name} missing occurrence_id: {row}")

    def test_occurrence_emission_reconciliation(self):
        pm = self._rows("index_verborum_print_main.tsv")
        et = self._rows("index_verborum_emission_table.tsv")
        bo = self._rows("index_verborum_book_occurrences.tsv")
        be = self._rows("index_verborum_book_emissions.tsv")

        self.assertEqual(len(pm), 2264)
        self.assertEqual(len(et), len(pm))
        source_not_in_book = sum(1 for r in et if (r.get("in_book") or "") != "1")
        self.assertEqual(source_not_in_book, 233)
        self.assertEqual(len(bo), len(pm) - source_not_in_book)
        self.assertEqual(len(bo), 2031)
        self.assertEqual(len(be), 1865)
        self.assertTrue(all("collapsed_into" in r for r in et))
        self.assertTrue(any((r.get("collapsed_into") or "").strip() for r in et if (r.get("source_scope") or "") != "explicit_tag"))
        self.assertEqual(
            sum(int(r["source_occurrence_count"]) for r in be),
            len(bo),
        )
        self.assertTrue(all("|" in r["source_occurrence_ids"] or int(r["source_occurrence_count"]) == 1 for r in be))

        pm_ids = Counter((r.get("occurrence_id") or "").strip() for r in pm)
        et_ids = Counter((r.get("occurrence_id") or "").strip() for r in et)
        self.assertEqual(pm_ids, et_ids)

    def test_collapsed_many_occurrences_to_one_emission(self):
        et = self._rows("index_verborum_emission_table.tsv")
        grouped = {}
        for row in et:
            if (row.get("in_book") or "") != "1" or (row.get("source_scope") or "") == "explicit_tag":
                continue
            grouped.setdefault(row["emission_id"], []).append(row)
        self.assertTrue(any(len(rows) > 1 for rows in grouped.values()))
        for rows in grouped.values():
            if len(rows) == 1:
                continue
            self.assertEqual(rows[0]["collapsed_into"], "")
            for later in rows[1:]:
                self.assertEqual(later["collapsed_into"], rows[0]["emission_id"])
                self.assertEqual(later["emission_id"], rows[0]["emission_id"])
                self.assertNotEqual(later["occurrence_id"], rows[0]["occurrence_id"])
        self.assertTrue(all((r.get("collapsed_into") or "").strip() == "" for r in et if (r.get("source_scope") or "") == "explicit_tag"))

    def test_corpus_metric_assertions(self):
        """Permanent assertions for the corpus/book occurrence/emission counts.

        These assert exact algebraic reconciliation without asserting individual
        data rows, so they catch accidental regression without over-specifying.
        """
        pm = self._rows("index_verborum_print_main.tsv")
        bo = self._rows("index_verborum_book_occurrences.tsv")
        be = self._rows("index_verborum_book_emissions.tsv")
        pu = self._rows("index_verborum_print_unique.tsv")
        bu = self._rows("index_verborum_book_print_unique.tsv")
        pe = self._rows("index_verborum_print_excluded.tsv")

        self.assertEqual(len(pm), 2264, "corpus occurrence count")
        source_not_in_book = 2264 - 2031
        self.assertEqual(len(bo), len(pm) - source_not_in_book, "corpus = book + not_in_book")
        self.assertEqual(len(be), 1865, "book emission count")
        self.assertEqual(len(pu), 1061, "unique corpus entries")
        self.assertEqual(len(bu), 828, "unique book entries")

        # Algebraic reconciliations
        self.assertEqual(len(pm), len(bo) + source_not_in_book)
        total_occurrences = sum(int(r["source_occurrence_count"]) for r in be)
        self.assertEqual(total_occurrences, len(bo), "book_occurrences == sum(source_occurrence_count)")

        variety_labelled_unique = sum(1 for r in bu if (r.get("printed_variety") or "").strip())
        self.assertEqual(variety_labelled_unique, 27, "variety-labelled unique book entries")

        printable_explicit = sum(1 for r in pm if (r.get("source_scope") or "") == "explicit_tag")
        self.assertEqual(printable_explicit, 1417, "printable explicit occurrences")

        excluded_explicit = sum(1 for r in pe if (r.get("source_scope") or "") == "explicit_tag")
        self.assertEqual(excluded_explicit, 79, "excluded explicit occurrences")

        # Every excluded explicit must retain its occurrence_id
        self.assertTrue(
            all((r.get("occurrence_id") or "").strip() for r in pe if (r.get("source_scope") or "") == "explicit_tag"),
            "every excluded explicit must retain occurrence_id"
        )

    def test_no_fallback_allowlist(self):
        """Assert the fallback allowlist file does not exist.

        Zero fallback uses were measured, and the file has been intentionally
        deleted. Its reappearance would indicate accidental regeneration.
        """
        p = BOOK / "index_verborum_explicit_allow_sortkey.tsv"
        self.assertFalse(p.exists(), f"Fallback allowlist should not exist: {p}")

    def test_fallback_uses_zero(self):
        """Assert the fallback log is empty or absent."""
        p = BOOK / "index_verborum_fallback_used.tsv"
        if p.exists():
            rows = list(csv.DictReader(p.open(encoding="utf-8")))
            self.assertEqual(len(rows), 0, "fallback uses must be zero")


if __name__ == "__main__":
    unittest.main()
