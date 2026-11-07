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

    def test_sc037_reconstructions_require_the_prior_local_lemma_gloss(self):
        forms = (
            "Orel prints [sali-warđaz]{.recon .iv lang=pgmc} and "
            "[sali-warđuz]{.recon .iv lang=pgmc}."
        )
        anchor = "[*seleweard*]{.iv lang=oe} 'hall-warden' is attested. "
        self.assertEqual(self.validate(anchor + forms).returncode, 0)
        for text in (
            forms,
            forms + " " + anchor,
            anchor + "\n\n" + forms,
            anchor + forms.replace("Orel prints", "Another word is"),
            "# Word-by-word derivations\n\n" + anchor + forms,
        ):
            with self.subTest(text=text):
                result = self.validate(text)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("missing gloss for *sali-warđaz*", result.stderr)

    def test_sc037_names_are_exempt_only_in_the_explicit_name_comparison(self):
        forms = "[*Sigfrið*]{.iv lang=oe} and [*Hyglāc*]{.iv lang=oe}."
        context = (
            "The older names matter. The handbooks recognize high-vowel loss "
            "after light first roots, including "
        )
        self.assertEqual(self.validate(context + forms).returncode, 0)
        for text in (
            forms,
            context.replace("The older names matter. ", "") + forms,
            context.replace("light first roots", "other roots") + forms,
            "# Word-by-word derivations\n\n" + context + forms,
        ):
            with self.subTest(text=text):
                result = self.validate(text)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn("missing gloss for *Sigfrið*", result.stderr)

    def test_sc037_reader_passes_without_checker_driven_prose_edits(self):
        reader = FILTER.parents[1] / "docs/sound_changes/reader_facing/037-compound-linking-syncope.md"
        target = reader.with_name("115-post-umlaut-high-syncope.md")
        result = self.validate(reader.read_text(encoding="utf-8") + "\n\n" + target.read_text(encoding="utf-8"))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_stage_reconstructions_share_only_their_explicit_following_gloss(self):
        cases = (
            ("Ringe and Taylor reconstruct pre-Old-English [ūtumist]{.recon}, "
             "then [ȳtymist]{.recon}, and [*ȳtmest*]{.iv} 'furthest'.",
             "Ringe and Taylor reconstruct pre-Old-English"),
            ("Hogg's [gaduling]{.recon} gives [*gædeling*]{.iv} 'companion'.", "gives"),
            ("The bailiff reconstruction provides [skuldihātijā]{.recon}, then "
             "[sċyldihǣtjā]{.recon}, with [*sċyldhǣta*]{.iv} 'bailiff'.",
             "The bailiff reconstruction provides"),
            ("The inherited [wiđuwōn]{.recon} and [*widuwe*]{.iv} 'widow' agree.",
             "The inherited"),
        )
        for text, context in cases:
            with self.subTest(text=text):
                self.assertEqual(self.validate(text).returncode, 0)
                for wrong in (
                    text.replace(context, "Another word is"),
                    text.replace(".iv", ".pred"),
                    text.replace(" 'furthest'", "").replace(" 'companion'", "")
                        .replace(" 'bailiff'", "").replace(" 'widow'", ""),
                    "# Word-by-word derivations\n\n" + text,
                ):
                    self.assertEqual(self.validate(wrong).returncode, 2, wrong)

    def test_stage_reference_requires_actual_target_and_glossed_lexical_anchor(self):
        mention = (
            "The independent *ūtumist* history is discussed with "
            "[SC115](#rule-OEHighLinkSyncope).\n\n"
        )
        target = "## The high component {#rule-OEHighLinkSyncope}\n\n*ȳtmest* 'furthest'."
        self.assertEqual(self.validate(mention + target).returncode, 0)
        for wrong in (
            mention,
            mention.replace("The independent", "An unrelated") + target,
            mention.replace("#rule-OEHighLinkSyncope", "#wrong") + target,
            mention + target.replace(" {#rule-OEHighLinkSyncope}", ""),
            mention + target.replace(" 'furthest'", ""),
            mention + target.replace("*ȳtmest*", "[ȳtmest]{.pred}"),
            mention + "# Word-by-word derivations\n\n" + target,
        ):
            self.assertEqual(self.validate(wrong).returncode, 2, wrong)

    def test_widow_variant_requires_prior_gloss_and_exact_context(self):
        anchor = "*widuwe* 'widow' is recorded.\n\n"
        context = "The selected root-vowel variant [*wuduwe*]{.iv} retains the vowel."
        self.assertEqual(self.validate(anchor + context).returncode, 0)
        for wrong in (context, context + "\n\n" + anchor,
                      anchor + context.replace("selected root-vowel variant", "other form"),
                      "# Word-by-word derivations\n\n" + anchor + context):
            self.assertEqual(self.validate(wrong).returncode, 2, wrong)

    def test_sc040_projections_require_the_prior_lemma_and_exact_context(self):
        context = (
            "In *eorþ.cun.de*, the syllables differ. "
            "The genitive control *eorþcundes* has the same contrast."
        )
        antecedent = "*eorþcunde* 'earthly' is the selected witness.\n\n"
        result = self.validate(antecedent + context)
        self.assertEqual(result.returncode, 0, result.stderr)
        for text in (
            context,
            context + "\n\n" + antecedent,
            antecedent + "Other forms are *eorþ.cun.de* and *eorþcundes*.",
            "# Word-by-word derivations\n\n#### Old English evidence\n\n"
            + antecedent + context,
        ):
            with self.subTest(text=text):
                result = self.validate(text)
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_released_sc040_reader_passes_without_repeating_lemma_glosses(self):
        reader = FILTER.parents[1] / "docs/sound_changes/reader_facing/040-medial-unstressed-u-lowering.md"
        result = self.validate(reader.read_text(encoding="utf-8"))
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
        for classes in (".recon .iv", ".iv lang=oe"):
            for key in ("role", "form_role"):
                with self.subTest(classes=classes, key=key):
                    result = self.validate(f"[strēa]{{{classes} {key}=regular_output}}.\n")
                    self.assertEqual(result.returncode, 0, result.stderr)
        for role in ("evidence_form", "input", "target"):
            with self.subTest(role=role):
                result = self.validate(f"[strēa]{{.recon form_role={role}}}.\n")
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_four_cell_derivation_context_requires_the_prior_lemma(self):
        prefix = "# Word-by-word derivations\n\n"
        paragraph = (
            "Dental hardening gives [fúndanē]{.iv .recon lang=preoe}, "
            "then [fúndnē]{.iv .recon lang=preoe}.\n"
        )
        antecedent = "[fundne]{.iv lang=oe} 'found' is the selected plural.\n\n"
        self.assertEqual(self.validate(prefix + antecedent + paragraph).returncode, 0)
        for text in (
            prefix + paragraph,
            prefix + paragraph + antecedent,
            prefix + antecedent + "Other forms are [fúndanē]{.iv .recon lang=preoe}.",
            antecedent + paragraph,
        ):
            with self.subTest(text=text):
                result = self.validate(text)
                self.assertEqual(result.returncode, 2, result.stderr)

    def test_same_cell_comparison_requires_its_actual_local_gloss(self):
        prefix = "# Word-by-word derivations\n\n"
        paragraph = (
            "[hameres]{.iv lang=oe} 'of a hammer' and [hamores]{.iv lang=oe} "
            "retains a second oblique tradition.\n"
        )
        self.assertEqual(self.validate(prefix + paragraph).returncode, 0)
        for text in (
            prefix + paragraph.replace("'of a hammer'", ""),
            prefix + paragraph.replace("retains a second oblique tradition", "are other forms"),
        ):
            result = self.validate(text)
            self.assertEqual(result.returncode, 2, result.stderr)

    def test_selected_four_cell_articles_pass_without_repeated_gloss_prose_edits(self):
        models = FILTER.parents[1] / "docs/lexeme_reports/model_entries"
        for name in (
            "2011-find-fundene.model.md", "2053-hammer-hameres.model.md",
            "2201-soul-sāwle.model.md", "2282-west-west.model.md",
        ):
            with self.subTest(name=name):
                result = self.validate(
                    "# Word-by-word derivations\n\n" + (models / name).read_text()
                )
                self.assertEqual(result.returncode, 0, result.stderr)

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
