#!/usr/bin/env python3
"""Regression tests for the Index Verborum historical-stage architecture.

Core principle under test: a reconstruction asterisk means *reconstructed*, NOT
*Proto-Germanic*. Historical stage is a separate, explicit axis. Computational
convenience must never silently become historical metadata:

  * reconstructed forms are never *silently* coerced to ``pgmc``;
  * the historical stage is declared explicitly by the canonical source
    (the ``entry_stage_metadata.tsv`` sidecar, propagated through the manifest);
  * an absent or unknown stage fails closed instead of defaulting to ``pgmc``
    (or ``preoe``);
  * source-scholar transcription (Ringe & Taylor ``h``) and CAPR canonical
    transcription (``x``) are dated to the *same* stage, so one lexeme never
    acquires duplicate chronological labels.

Run: cd Germanic/tests && python3 -m unittest test_index_verborum_stage_architecture
"""
from __future__ import annotations

import csv
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOK = REPO_ROOT / "Germanic/docs/book"
ASSEMBLY = REPO_ROOT / "Germanic/docs/assembly"
DATA = REPO_ROOT / "Germanic/data"
TOOLS = REPO_ROOT / "Germanic/tools"

sys.path.insert(0, str(TOOLS))
import build_index_verborum as biv  # noqa: E402

RECONSTRUCTED_STAGES = set(biv.RECONSTRUCTED_STAGE_CODES)


def _rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _forms() -> list[dict[str, str]]:
    return _rows(BOOK / "index_verborum_forms.tsv")


class RequireReconstructedStageTests(unittest.TestCase):
    """The fail-closed stage resolver never invents pgmc."""

    def test_valid_stage_passes_through(self):
        for code in RECONSTRUCTED_STAGES:
            self.assertEqual(
                biv.require_reconstructed_stage(code, form="*x", scope="s", source_ref="r"),
                code,
            )

    def test_blank_stage_fails_closed(self):
        with self.assertRaises(ValueError):
            biv.require_reconstructed_stage("", form="*xébun", scope="lexical_protoform", source_ref="r")

    def test_whitespace_stage_fails_closed(self):
        with self.assertRaises(ValueError):
            biv.require_reconstructed_stage("   ", form="*x", scope="s", source_ref="r")

    def test_unknown_stage_fails_closed(self):
        with self.assertRaises(ValueError):
            biv.require_reconstructed_stage("nwgmc-northsea", form="*x", scope="s", source_ref="r")

    def test_pgmc_is_not_a_hardcoded_fallback(self):
        # A blank stage must NOT silently resolve to pgmc.
        with self.assertRaises(ValueError):
            biv.require_reconstructed_stage(None, form="*x", scope="s", source_ref="r")  # type: ignore[arg-type]


class TableSemanticInferenceFailsClosedTests(unittest.TestCase):
    """A starred form with no stage signal is never inferred as pgmc."""

    def _mention(self, form: str, cell_text: str = "", row_text: str = ""):
        return biv.TableFormMention(
            form=form,
            source_ref="Germanic/docs/lexeme_reports/model_entries/9999-x.model.md:1",
            source_path="Germanic/docs/lexeme_reports/model_entries/9999-x.model.md",
            line_no=1,
            heading="### Test",
            line_text="",
            row_label="row",
            row_text=row_text,
            cell_header="",
            cell_kind="input",
            cell_text=cell_text,
        )

    def test_starred_selected_input_without_hint_is_unresolved(self):
        lang, confident = biv.infer_table_semantic_language(
            self._mention("*xyzaz"), "selected_input", set()
        )
        self.assertEqual(lang, "", "reconstructed selected input with no hint must fail closed")
        self.assertFalse(confident)

    def test_starred_source_protoform_without_hint_is_unresolved(self):
        lang, _ = biv.infer_table_semantic_language(
            self._mention("*xyzaz"), "source_protoform", set()
        )
        self.assertEqual(lang, "")

    def test_explicit_later_stage_hint_is_honoured(self):
        lang, confident = biv.infer_table_semantic_language(
            self._mention("*xébun", cell_text="northern West Germanic *xébun", row_text=""),
            "selected_input",
            set(),
        )
        # An explicit later-stage hint must win; it must not be flattened to pgmc.
        self.assertNotEqual(lang, "pgmc")


class ProductionStageInvariantTests(unittest.TestCase):
    """Every reconstructed production occurrence carries an explicit valid stage."""

    RECON_SCOPES = {"lexical_proto", "lexical_protoform", "trace_proto_input"}

    def test_reconstructed_lexical_and_trace_rows_have_valid_stage(self):
        for row in _forms():
            if row["source_scope"] in self.RECON_SCOPES:
                self.assertIn(
                    row["language"],
                    RECONSTRUCTED_STAGES,
                    f"{row['source_scope']} {row['form']} has non-reconstructed stage {row['language']!r}",
                )

    def test_no_production_row_has_blank_language(self):
        for row in _forms():
            self.assertTrue(row["language"], f"blank language for {row['form']} ({row['source_scope']})")


class HeavenStageTests(unittest.TestCase):
    """Heaven: selected input is post-PGmc; the deeper obliques stay PGmc."""

    def setUp(self):
        self.by_form: dict[str, set[str]] = {}
        for row in _forms():
            self.by_form.setdefault(row["form"], set()).add(row["language"])

    def test_selected_input_and_source_forms_are_northern_west_germanic(self):
        for form in ("*xébun", "xébun", "hebun", "hebunas"):
            self.assertIn(form, self.by_form, f"{form} missing from index")
            self.assertEqual(
                self.by_form[form], {"nsgmc"},
                f"{form} should be dated nsgmc (northern West Germanic) only, got {self.by_form[form]}",
            )

    def test_deeper_obliques_and_citation_stay_pgmc(self):
        for form in ("*xémenaz", "xémenaz", "xémnas", "xémni", "xémnum", "hemnaz", "hemō"):
            self.assertIn(form, self.by_form, f"{form} missing from index")
            self.assertEqual(
                self.by_form[form], {"pgmc"},
                f"{form} should stay pgmc, got {self.by_form[form]}",
            )

    def test_no_heaven_form_is_labelled_proto_germanic_selected_input(self):
        # *xébun is the selected input; it must never be pgmc, nor undifferentiated
        # pwgmc, nor conflated with Proto-Northwest Germanic (pnwgmc).
        for stray in ("pgmc", "pwgmc", "pnwgmc"):
            self.assertNotIn(stray, self.by_form.get("*xébun", set()))
            self.assertNotIn(stray, self.by_form.get("xébun", set()))


class OccurrenceStageInvariantTests(unittest.TestCase):
    """Each indexed occurrence carries exactly one explicit, valid stage.

    Historical identity and orthographic identity are separate: the SAME
    reconstructed spelling may legitimately occur at more than one stage (an
    unchanged form can persist across stages, or two distinct reconstructions may
    coincide in spelling). We therefore do NOT require a literal string to map to
    exactly one stage across the whole book. We require that every occurrence has
    a single defensible stage and that no *identical occurrence* is emitted with
    conflicting stages.
    """

    def test_every_occurrence_has_a_single_valid_stage(self):
        for row in _forms():
            self.assertTrue(row["language"], f"blank stage: {row['form']} @ {row['source_ref']}")

    def test_no_identical_occurrence_has_conflicting_stage(self):
        # Genuine accidental-duplicate detection: the same occurrence_id must not
        # appear with two different languages/stages.
        by_occ: dict[str, set[str]] = {}
        for row in _forms():
            occ = row.get("occurrence_id") or ""
            if occ:
                by_occ.setdefault(occ, set()).add(row["language"])
        conflicts = {occ: langs for occ, langs in by_occ.items() if len(langs) > 1}
        self.assertEqual(conflicts, {}, f"occurrences with conflicting stage: {conflicts}")

    def test_hebun_lexeme_has_a_single_stage(self):
        # This is a lexeme-specific regression (not a global string rule): the
        # heaven source form *hebun is ONE reconstruction (R&T's northern West
        # Germanic sky-word), so all its occurrences share one stage. It must not
        # regress to the earlier duplicate pgmc/pwgmc labelling.
        stages = {row["language"] for row in _forms() if row["form"] == "hebun"}
        self.assertEqual(stages, {"nsgmc"}, f"*hebun must have one stage, got {stages}")


class StemStageTests(unittest.TestCase):
    """Stem: PGmc i-stem input, distinct from the OE voice/sound homonym."""

    def setUp(self):
        self.by_form: dict[str, set[str]] = {}
        for row in _forms():
            self.by_form.setdefault(row["form"], set()).add(row["language"])

    def test_stem_proto_and_protoform_are_pgmc(self):
        for form in ("*stámnaz", "*stámniz"):
            self.assertEqual(self.by_form.get(form), {"pgmc"}, f"{form}: {self.by_form.get(form)}")

    def test_stefn_is_old_english(self):
        self.assertEqual(self.by_form.get("stefn"), {"oe"})


class StageMetadataSidecarTests(unittest.TestCase):
    """The canonical stage sidecar is complete, valid, and matches the manifest."""

    def setUp(self):
        self.sidecar = {r["row_id"]: r for r in _rows(DATA / "entry_stage_metadata.tsv")}
        self.manifest = _rows(ASSEMBLY / "manifest_all_by_class.tsv")

    def test_unequal_population_has_stage_declarations(self):
        """Every PROTOFORM != PROTO manifest row carries an explicit sidecar
        decision. Equality rows are auto-pgmc in code and are NOT required here
        (testing model-entry membership was the wrong criterion: it forced
        equality rows into the sidecar and bloated it)."""
        unequal = {
            r["row_id"]
            for r in self.manifest
            if r["proto"].strip() and r["proto"].strip() != r["protoform"].strip()
        }
        missing = unequal - set(self.sidecar)
        self.assertEqual(missing, set(), f"unequal rows missing a sidecar decision: {missing}")

    def test_sidecar_is_exception_only(self):
        """The sidecar records ONLY exception (PROTOFORM != PROTO) rows; an
        equality row must never appear (it is auto-pgmc in code, not data)."""
        manifest_by_id = {r["row_id"]: r for r in self.manifest}
        for rid in self.sidecar:
            r = manifest_by_id.get(rid)
            if r is None:
                continue
            self.assertNotEqual(
                r["proto"].strip(), r["protoform"].strip(),
                f"equality row {rid} must not be in the exception-only sidecar",
            )

    def test_all_sidecar_stages_are_valid(self):
        for rid, row in self.sidecar.items():
            self.assertIn(row["proto_stage"], RECONSTRUCTED_STAGES, rid)
            self.assertIn(row["protoform_stage"], RECONSTRUCTED_STAGES, rid)

    def test_heaven_protoform_is_northern_west_germanic_proto_is_pgmc(self):
        self.assertEqual(self.sidecar["2068"]["protoform_stage"], "nsgmc")
        self.assertEqual(self.sidecar["2068"]["proto_stage"], "pgmc")

    def test_manifest_stage_matches_sidecar(self):
        for row in self.manifest:
            rid = row["row_id"]
            if rid in self.sidecar:
                self.assertEqual(row["proto_stage"], self.sidecar[rid]["proto_stage"], rid)
                self.assertEqual(row["protoform_stage"], self.sidecar[rid]["protoform_stage"], rid)

    def test_no_manifest_row_has_blank_stage(self):
        for row in self.manifest:
            self.assertTrue(row["proto_stage"], f"blank proto_stage row {row['row_id']}")
            self.assertTrue(row["protoform_stage"], f"blank protoform_stage row {row['row_id']}")


class AuditSidecarAgreementTests(unittest.TestCase):
    """The human-readable audit ledger and the canonical sidecar are one source
    of truth: the stage label and variety must never diverge between them."""

    def setUp(self):
        self.sidecar = {r["row_id"]: r for r in _rows(DATA / "entry_stage_metadata.tsv")}
        self.audit = {r["row_id"]: r for r in _rows(DATA / "protoform_stage_audit.tsv")}

    def test_same_population(self):
        self.assertEqual(set(self.sidecar), set(self.audit))

    def test_stage_and_variety_agree(self):
        for rid, s in self.sidecar.items():
            a = self.audit[rid]
            self.assertEqual(
                s["protoform_stage"], a["proposed_protoform_stage"],
                f"{rid}: stage label diverges between sidecar and audit",
            )
            self.assertEqual(
                (s.get("protoform_variety") or ""), (a.get("protoform_variety") or ""),
                f"{rid}: variety label diverges between sidecar and audit",
            )

    def test_label_is_independent_of_confidence(self):
        """The stage/variety label must not be derived from confidence: a
        provisional-confidence row still carries its full explicit label, and no
        confidence-derived review_status column exists."""
        self.assertNotIn("review_status", next(iter(self.audit.values())).keys())
        world = self.audit["2302"]
        self.assertEqual(world["confidence"], "provisional")
        self.assertEqual(world["proposed_protoform_stage"], "pgmc")
        self.assertEqual(world["protoform_variety"], "transponent")


class TransponentVarietyTests(unittest.TestCase):
    """`transponent` is a cross-stage variety (parallel to OE dialect labels),
    orthogonal to the base stage and fail-closed validated."""

    def setUp(self):
        import index_verborum_render as ivr
        self.reg = ivr.load_variety_registry()

    def test_registered_and_printed(self):
        entry = self.reg.get("transponent")
        self.assertIsNotNone(entry)
        self.assertEqual(self.reg.printed_label("transponent"), "transp.")

    def test_attaches_to_any_reconstructed_stage(self):
        for stage in ("pgmc", "pnwgmc", "pwgmc", "nsgmc", "paf", "preoe"):
            self.reg.validate_occurrence(stage, "transponent")

    def test_rejected_on_non_reconstructed_language(self):
        with self.assertRaises(ValueError):
            self.reg.validate_occurrence("oe", "transponent")

    def test_transponent_rows_keep_honest_base_stage(self):
        sidecar = {r["row_id"]: r for r in _rows(DATA / "entry_stage_metadata.tsv")}
        expect = {"2109": "preoe", "2205": "preoe", "2252": "preoe", "2302": "pgmc"}
        for rid, stage in expect.items():
            self.assertEqual(sidecar[rid]["protoform_variety"], "transponent", rid)
            self.assertEqual(sidecar[rid]["protoform_stage"], stage, rid)


class NonModelStageFailClosedTests(unittest.TestCase):
    """§6: a non-model selected input equal to PROTO (modulo stress/compound
    hyphen encoding) is pgmc; a genuinely different one is never silently pgmc."""

    def test_encoding_only_difference_is_equal(self):
        # rainbow: *régna-bùgô vs *régnabùgô differ only by a compound hyphen.
        self.assertEqual(
            biv.transliterate_sort_key("*régna-bùgô"),
            biv.transliterate_sort_key("*régnabùgô"),
        )

    def test_genuine_stage_difference_is_not_equal(self):
        # thousand: jō-stem *θūs-undī vs OE-oriented *θūs-èndi are truly distinct.
        self.assertNotEqual(
            biv.transliterate_sort_key("*θūs-undī"),
            biv.transliterate_sort_key("*θūs-èndi"),
        )


if __name__ == "__main__":
    unittest.main()
