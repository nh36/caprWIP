from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / "Germanic/docs/assembly"))

import build_full_lexical_volume as volume
import check_publication_references as references

RULES = (
    "OEWWSimplification", "OEAuBrightening", "OEDiphthongLeveling",
    "PWGmcCoronalWAssimilation", "PWGmcUnstressedWordFinalIApocope",
    "PGmcNasalLossBeforeX", "EAFNasalizedLowRounding", "OEBreaking",
    "OEEwLongDiphthong", "OEJGlideIO", "OEJWWSimplification",
    "PWGmcJGemination", "OEAwwjResolution", "PWGmcEndinglessAw",
    "OEAwLongDiphthong",
)


class PublicationTests(unittest.TestCase):
    def test_narrow_trace_panels_reserve_space_for_unbreakable_forms(self):
        for form in ("*skáwōθ", "*abcdef", "*abcdefgh"):
            stats = volume.panel_complexity([("Earlier", [("Input", form)])])
            for panel_width in (0.35, 0.37, 0.40):
                label, form_width = volume.choose_panel_column_widths(panel_width, stats)
                self.assertGreaterEqual(form_width, 0.24)
                self.assertLessEqual(label + form_width, 0.98)
        short = volume.panel_complexity([("Earlier", [("Input", "*abc")])])
        self.assertEqual(volume.choose_panel_column_widths(0.35, short)[1], 0.14)

    def test_reconstructed_regular_outputs_keep_the_default_index_exclusion(self):
        import csv
        import check_reader_facing_semantics as semantics
        directory = ROOT / "Germanic/docs/book"
        def straw_rows(name):
            with (directory / name).open() as handle:
                return [r for r in csv.DictReader(handle, delimiter="\t")
                        if "2224-" in r["source_ref"] and r["form_role"] == "regular_output"]
        self.assertEqual(straw_rows("index_verborum_print_main.tsv"), [])
        excluded = straw_rows("index_verborum_print_excluded.tsv")
        self.assertEqual(len(excluded), 3)
        self.assertTrue(all(r["display"] == "*strēa" and r["sort_key"] == "strea"
                            and r["exclusion_reason"] == "regular_output_default_exclusion"
                            for r in excluded))
        semantics.run_recon_iv_index_display_check()

    def test_generic_mismatch_summary_and_trace_use_reconstruction_semantics(self):
        model = {"metadata": {"PROTO": "*example", "PROTOFORM": "*example",
                              "COUNTERPART": "attested", "DERIVATION_CLASS": "late_analogy"}}
        trace = {"outcome": "regular", "expected": "attested",
                 "table": "| Earlier | Later |\n| --- | --- |\n"
                          "| **PGmc**<br>*example | **OE**<br>Orthography: regular |"}
        self.assertIn("[regular]{.recon form_role=regular_output}", volume.derivation_summary(model, trace))
        self.assertIn(r"\Recon{regular}", "\n".join(volume.render_trace_table(trace)))
        self.assertIn("_attested_", volume.derivation_summary(model, trace))
        trace["outcome"] = "attested"
        self.assertNotIn(".recon", volume.derivation_summary(model, trace))
        self.assertEqual(volume.regular_output_markup(model["metadata"], "*regular"),
                         "[regular]{.recon form_role=regular_output}")

    def test_straw_live_trace_and_source_keep_explicit_mismatch(self):
        path = ROOT / "Germanic/docs/lexeme_reports/model_entries/2224-straw-strēaw.model.md"
        model = volume.parse_model_entry(path)
        traces = volume.parse_trace_entries(volume.TRACE_REPORT_PATH.read_text())
        trace, _, confident = volume.match_trace_entry(model, traces)
        self.assertTrue(confident)
        self.assertEqual((trace["outcome"], trace["expected"]), ("strēa", "strēaw"))
        rendered = volume.rewrite_entry(model, trace)
        self.assertIn("yields regular [strēa]{.recon form_role=regular_output}", rendered)
        self.assertIn(r"\Recon{strēa}", rendered)
        self.assertIn("Old English form: _strēaw_", rendered)
        self.assertIn("regular free simplex unattested", path.read_text())
        self.assertIn("p. 484", path.read_text())
        self.assertNotIn("DEV_NOTES", path.read_text())

    def test_reference_gate_detects_tex_and_actual_build_failures(self):
        tex = r"\hypertarget{local}{}\label{section}\hyperlink{local}{x}\hyperref[section]{y}"
        self.assertEqual(references.problems(tex, "PDF written"), [])
        for command in (r"\hyperlink{missing}{x}", r"\hyperref[missing]{x}",
                        r"\ref{missing}", r"\pageref{missing}"):
            self.assertEqual(references.problems(tex + command, ""),
                             ["undefined internal destination: missing"])
        for log in ("LaTeX Warning: Hyper reference `rule-X' on\n page 2 undefined",
                    "LaTeX Warning: There were undefined references.",
                    "LaTeX Warning: Citation `X' undefined"):
            self.assertTrue(references.problems(tex, log))

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc not provisioned")
    def test_standalone_filter_preserves_local_and_external_links(self):
        markdown = "\n\n".join(
            [f"[SC{i + 1} descriptive {rule}](#rule-{rule})" for i, rule in enumerate(RULES)]
            + ["# Local {#rule-Local}", "[local rule](#rule-Local)",
               "# Lexeme {#lexeme}", "[lexical entry](#lexeme)",
               "[website](https://example.org)", "[new companion](#rule-NewFutureRule)",
               "[later span](#rule-Span)", "[destination]{#rule-Span}"])
        result = subprocess.run(
            ["pandoc", "--from=markdown", "--to=json",
             "--lua-filter=" + str(ROOT / "Germanic/tools/standalone_lexical_links.lua")],
            input=markdown, text=True, capture_output=True, check=True)
        document = json.loads(result.stdout)
        links = []

        def collect(value):
            if isinstance(value, dict):
                if value.get("t") == "Link":
                    links.append(value["c"][-1][0])
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(document)
        self.assertEqual(links, ["#rule-Local", "#lexeme", "https://example.org", "#rule-Span"])
        plain = subprocess.run(["pandoc", "--from=json", "--to=plain"], input=result.stdout,
                               text=True, capture_output=True, check=True).stdout
        for i, rule in enumerate(RULES):
            self.assertIn(f"SC{i + 1} descriptive {rule}", plain)

    def test_all_combined_rule_links_have_real_sections(self):
        import re
        book = (ROOT / "Germanic/docs/assembly/capr_book_draft_alpha_01.md").read_text()
        anchors = set(re.findall(r"\{#(rule-[^\s}]+)", book))
        links = set(re.findall(r"\]\(#(rule-[^)]+)\)", book))
        self.assertTrue(links)
        self.assertEqual(links - anchors, set())
        self.assertIn("rule-PWGmcEndinglessAw", anchors)
        self.assertIn("rule-OEAwLongDiphthong", links)

    def test_both_standalone_wrappers_share_render_filters_and_gate(self):
        for suffix in (".sh", "_docker.sh"):
            wrapper = (ROOT / ("Germanic/docs/assembly/build_full_lexical_volume" + suffix)).read_text()
            for name in ("standalone_lexical_links.lua", "predicted_form_filter.lua",
                         "reconstructed_form_filter.lua", "lex_form_filter.lua",
                         "semantic_form_macros.tex", "check_publication_references.py"):
                self.assertIn(name, wrapper)
        combined = (ROOT / "Germanic/docs/assembly/build_capr_book_draft_docker.sh").read_text()
        self.assertNotIn("standalone_lexical_links.lua", combined)
        self.assertIn("check_publication_references.py", combined)


if __name__ == "__main__":
    unittest.main()
