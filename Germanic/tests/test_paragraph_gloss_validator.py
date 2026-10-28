"""Regression tests for lexical forms versus sound notation in book prose."""
from pathlib import Path
import shutil
import subprocess
import unittest


FILTER = Path(__file__).resolve().parents[1] / "tools/paragraph_gloss_validator.lua"


@unittest.skipUnless(shutil.which("pandoc"), "pandoc is required")
class ParagraphGlossValidatorTests(unittest.TestCase):
    def validate(self, markdown):
        return subprocess.run(
            [
                "pandoc", "--from=markdown+raw_tex+citations", "--to=json",
                f"--lua-filter={FILTER}",
            ],
            input=markdown, text=True, capture_output=True, timeout=30,
        )

    def test_part_one_sound_notation_is_not_lexical(self):
        for form in ("ā", "ō", "ą̄", "ēa", "īe", "īo", "sċ", "xst", "*ai", "*au"):
            with self.subTest(form=form):
                result = self.validate(f"The sequence *{form}* changes.\n")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("Total violations: 0", result.stderr)

    def test_short_lexical_forms_still_require_glosses(self):
        for form in ("cū", "cȳ", "bā", "āk", "gōs", "stān", "giftiz"):
            with self.subTest(form=form):
                result = self.validate(f"Old English *{form}* survives.\n")
                # Plain ASCII forms are checked when explicitly marked lexical.
                if form == "giftiz":
                    result = self.validate("[giftiz]{.recon .iv lang=pgmc} survives.\n")
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn(f"missing gloss for *{form}*", result.stderr)

    def test_explicit_lexical_segments_are_not_silently_exempted(self):
        for cls in ("iv", "lex"):
            for form in ("ā", "īo"):
                with self.subTest(cls=cls, form=form):
                    result = self.validate(f"[{form}]{{.{cls}}} survives.\n")
                    self.assertEqual(result.returncode, 2, result.stderr)

    def test_sc032_explicit_variants_share_existing_paragraph_gloss(self):
        result = self.validate(
            "The input of *hēafod* 'head' is realized. "
            "Campbell records both *hēafud* and *hēafod*, with varying vowels.\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_shared_gloss_allowance_requires_context_and_prior_local_gloss(self):
        variants = "Campbell records both *hēafud* and *hēafod*."
        for markdown in (
            variants,
            "*hēafod* is realized. " + variants,
            "*hēafod* 'head' is realized.\n\n" + variants,
            "*hēafod* 'head' is realized. Another word is *hēafud*.",
            variants + " Later *hēafod* 'head' is realized.",
            "# Word-by-word derivations\n\n#### Old English evidence\n\n"
            "*hēafod* 'head' is realized. " + variants,
        ):
            with self.subTest(markdown=markdown):
                result = self.validate(markdown)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("missing gloss for *hēafud*", result.stderr)

    def test_released_sc032_reader_passes_without_prose_edits(self):
        reader = FILTER.parents[1] / "docs/sound_changes/reader_facing/032-diphthong-leveling.md"
        result = self.validate(reader.read_text(encoding="utf-8"))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_sc087_byforms_share_only_their_explicit_local_gloss(self):
        for text in (
            "Campbell records byforms such as *gærs* 'grass' beside *græs*.",
            "The requirement changes *græs* 'grass' to attested *gærs*.",
        ):
            result = self.validate(text)
            self.assertEqual(result.returncode, 0, result.stderr)
        for text in (
            "The requirement changes *græs* to attested *gærs*.",
            "*græs* 'grass' is known.\n\nThe requirement changes to attested *gærs*.",
        ):
            result = self.validate(text)
            self.assertEqual(result.returncode, 2, result.stderr)

    def test_curated_repeated_context_requires_an_established_gloss(self):
        context = "The *reġnboga* test exposes an annotation dependency."
        result = self.validate(context)
        self.assertEqual(result.returncode, 2, result.stderr)
        result = self.validate("*reġnboga* 'rainbow' is known.\n\n" + context)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = self.validate("*reġnboga* 'rainbow' is known.\n\nAgain *reġnboga*.")
        self.assertEqual(result.returncode, 2, result.stderr)

    def test_documented_inflections_share_the_local_dictionary_lemma_gloss(self):
        prefix = "# Word-by-word derivations\n\n"
        paragraph = (
            "Bosworth–Toller gives *regn-boga* 'rainbow', with nominative "
            "[rénboga]{.iv lang=oe} and accusative [rénbogan]{.iv lang=oe}."
        )
        result = self.validate(prefix + paragraph)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = self.validate(prefix + paragraph.replace("'rainbow'", ""))
        self.assertEqual(result.returncode, 2, result.stderr)

    def test_glossed_forms_pass(self):
        result = self.validate(
            "*cȳ* 'cow' and [giftiz]{.recon .iv lang=pgmc} 'gift' survive.\n"
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_first_occurrence_is_per_paragraph(self):
        result = self.validate("*cū* 'cow' and *cū*.\n\nAgain *cū*.\n")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("Para 2: missing gloss for *cū*", result.stderr)
        self.assertNotIn("Para 1: missing", result.stderr)

    def test_prediction_and_example_exemptions_remain(self):
        result = self.validate("[cȳ]{.pred} and [giftiz]{.ex}.\n")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_reconstructed_regular_output_is_not_a_new_lexical_citation(self):
        for key in ("role", "form_role"):
            with self.subTest(key=key):
                result = self.validate(f"[strēa]{{.recon .iv {key}=regular_output}}.\n")
                self.assertEqual(result.returncode, 0, result.stderr)
        for role in ("evidence_form", "input", "target"):
            with self.subTest(role=role):
                result = self.validate(f"[strēa]{{.recon form_role={role}}}.\n")
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_combining_marks_do_not_hide_lexical_forms(self):
        result = self.validate("*cū* survives.\n")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("missing gloss for *cū*", result.stderr)

    def test_part_two_notation_and_lexical_boundary(self):
        prefix = "# Word-by-word derivations\n\n### Cow\n\n#### Old English evidence\n\n"
        notation = self.validate(prefix + "*ą̄* and *ēa*.\n")
        self.assertEqual(notation.returncode, 0, notation.stderr)
        lexical = self.validate(prefix + "*cȳ* survives.\n")
        self.assertEqual(lexical.returncode, 2, lexical.stderr)


if __name__ == "__main__":
    unittest.main()
