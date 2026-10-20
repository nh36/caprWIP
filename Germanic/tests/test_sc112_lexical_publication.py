"""Two-entry publication delta against the reviewed SC112 scientific closure."""

import csv
from io import StringIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
BASE = "5a3fced14d616ccaef5d703278d5cba2ffbca5cb"
ASSEMBLY = ROOT / "Germanic/docs/assembly"
MODELS = ROOT / "Germanic/docs/lexeme_reports/model_entries"
sys.path.insert(0, str(ASSEMBLY))
sys.path.insert(0, str(ROOT / "Germanic/tools"))
sys.path.insert(0, str(ROOT / "Germanic/docs/sound_changes/reader_facing"))
import build_class_manifests as manifests
import build_full_lexical_volume as volume
import check_reader_facing_semantics as semantics
import check_bibliographic_section_locators as locators
import check_reader_facing_crossrefs as crossrefs
import reader_facing_check_utils as reader


def committed(path):
    return subprocess.check_output(
        ["git", "show", f"{BASE}:{path.relative_to(ROOT)}"], cwd=ROOT, text=True)


def table(text):
    return list(csv.DictReader(StringIO(text), delimiter="\t"))


class Sc112LexicalPublicationTests(unittest.TestCase):
    def test_sc112_companion_heading_and_links_follow_existing_reader_contract(self):
        path = reader.ROOT / "112-monosyllabic-final-r-lengthening.md"
        headings = reader.extract_rule_headings(path)
        self.assertEqual(len(headings), 1)
        self.assertEqual((headings[0].sc_number, headings[0].rule_name, headings[0].anchor),
                         ("SC112", "PNWGmcMonosyllabicFinalRLengthening",
                          "#rule-PNWGmcMonosyllabicFinalRLengthening"))
        current = reader.build_rule_heading_map()
        all_rules = reader.build_all_source_rule_heading_map()
        issues, _ = crossrefs.scan_file(
            path, current, all_rules,
            {(heading.sc_number, heading.rule_name) for heading in current.values()},
        )
        self.assertEqual(issues, [])

    def test_source_locator_gate_matches_rendered_gate_not_audit_metadiscussion(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.md"
            for text in (
                "no residual sect/sects citation locators in TeX or PDF",
                "[@Hill2017, pp. 142--148]", "[@Campbell1959, §125]",
            ):
                path.write_text(text)
                self.assertEqual(locators.scan_file(path), [], text)
            for text in (
                "[@Campbell1959, sect. 125]", "[@Campbell1959, sects 125--126]",
                "Campbell (1959), Sect. 125", "SECTS. 125 and 126",
            ):
                path.write_text(text)
                self.assertEqual(locators.scan_file(path), [(1, text)])

    def test_only_two_regular_entries_are_added_to_the_reviewed_manifest(self):
        path = ASSEMBLY / "manifest_all_by_class.tsv"
        old = {row["row_id"]: row for row in table(committed(path))}
        current = table(path.read_text())
        now = {row["row_id"]: row for row in current}
        self.assertEqual(len(current), len(now))
        self.assertEqual((len(old), len(now)), (165, 167))
        self.assertEqual(set(now) - set(old), {"2333", "2334"})
        self.assertEqual(set(old) - set(now), set())
        self.assertEqual(sum(r["derivation_class"] == "regular" for r in current), 88)
        # Positions are editorial (see test_lexical_editorial_order); every
        # scientific column of every pre-existing entry must be unchanged.
        presentation = {"global_order", "class_order"}
        for row_id, before in old.items():
            after = now[row_id]
            self.assertEqual(
                {k: v for k, v in after.items() if k not in presentation},
                {k: v for k, v in before.items() if k not in presentation},
            )
        for row_id, word, target, proto in (
            ("2333", "there", "þǣr", "*θár"), ("2334", "where", "hwǣr", "*xwár"),
        ):
            row = now[row_id]
            self.assertEqual((row["lexical_item"], row["counterpart"], row["proto"],
                              row["protoform"], row["derivation_class"]),
                             (word, target, proto, proto, "regular"))
            self.assertEqual(row["trace_match_status"], "confident")
            self.assertEqual(row["section_title"], "Regular derivations")
            regular = table((ASSEMBLY / "manifest_regular.tsv").read_text())
            self.assertEqual([r for r in regular if r["row_id"] == row_id], [row])

    def test_each_book_includes_each_entry_once_with_its_own_trace(self):
        traces = volume.parse_trace_entries(volume.TRACE_REPORT_PATH.read_text())
        for word, target, proto in (("there", "þǣr", "*θár"), ("where", "hwǣr", "*xwár")):
            path = next(MODELS.glob(f"*-{word}-{target}.model.md"))
            model = volume.parse_model_entry(path)
            trace, _, confident = volume.match_trace_entry(model, traces)
            self.assertTrue(confident)
            self.assertEqual((trace["title"], trace["proto"], trace["expected"], trace["outcome"]),
                             (word, proto, target, target))
            self.assertFalse(manifests.parse_model_entry(path)["missing_metadata"])
            self.assertTrue(path.with_name(path.name.replace(".model.", ".source_ledger.")).is_file())
            if word == "where":
                rewritten = volume.rewrite_entry(model, trace)
                self.assertIn(r"while \emph{*xw-} represents", rewritten)
                self.assertIn(r"orthographically as \emph{hw-}", rewritten)
                self.assertNotIn("*xw-*", rewritten)
            for filename, start, stop in (
                ("lexical_volume_alpha_01.md", "## Part I. Regular derivations",
                 "## Part II. Attested variants"),
                ("capr_book_draft_alpha_01.md", "# Regular derivations",
                 "# Attested variants"),
            ):
                text = (ASSEMBLY / filename).read_text()
                heading = f"{word} — OE _{target}_"
                self.assertEqual(text.count(heading), 1)
                self.assertLess(text.index(start), text.index(heading))
                self.assertLess(text.index(heading), text.index(stop))
                entry = text[text.index(heading):].split("Reconstruction and comparative evidence", 1)[0]
                self.assertIn(f"Proto input: _\\{proto}_", entry)
                self.assertIn(f"Old English form: _{target}_", entry)
                self.assertIn("PNWGmc Monosyllabic Final R Lengthening", entry)

    def test_publication_index_delta_has_only_exact_new_provenance(self):
        path = semantics.ALLOWLIST_TSV
        fields = ("action", "language", "form", "form_role", "source_scope", "source_ref")
        keys = lambda rows: {tuple(row[field] for field in fields) for row in rows}
        old = keys(table(committed(path)))
        current = keys(table(path.read_text()))
        self.assertEqual(old - current, set())
        prefix = "Germanic/docs/lexeme_reports/model_entries/"
        there = prefix + "2333-there-þǣr.model.md"
        where = prefix + "2334-where-hwǣr.model.md"
        expected = {
            ("oe", "þǣr", "target_form", "explicit_tag", there),
            ("oe", "ðǣr", "comparison_form", "explicit_tag", there),
            ("oe", "ðēr", "comparison_form", "explicit_tag", there),
            ("oe", "hwǣr", "target_form", "explicit_tag", where),
            ("oe", "hwēr", "comparison_form", "explicit_tag", where),
            ("pgmc", "þar", "source_protoform", "explicit_tag", there),
            ("pgmc", "hwar", "source_protoform", "explicit_tag", where),
            ("pgmc", "xwar", "source_protoform", "explicit_tag", where),
            ("pgmc", "θár", "selected_input", "explicit_tag", there),
            ("pgmc", "xwár", "selected_input", "explicit_tag", where),
            ("pgmc", "*θár", "source_protoform", "lexical_protoform", "there — OE þǣr"),
            ("pgmc", "*xwár", "source_protoform", "lexical_protoform", "where — OE hwǣr"),
        }
        self.assertEqual(current - old, {("add", *row) for row in expected})
        semantics.run_index_fingerprint_checks()

    def test_scientific_sources_and_protected_receipts_are_unchanged(self):
        paths = (
            "Germanic/data", "Germanic/fsts", "Germanic/docs/sound_changes/registry",
            "Germanic/docs/sound_changes/cascade_baseline",
            "Germanic/docs/sound_changes/audits/sc015-r-adverb-lengthening-investigation",
            "Germanic/docs/lexeme_reports/pgmc_reconstructions",
        )
        changed = subprocess.check_output(
            ["git", "diff", BASE, "--name-only", "--", *paths], cwd=ROOT, text=True).split()
        # The survey receipt hashes the class-manifest generator it imports
        # resolve_stages from; a presentation-order edit to that generator
        # legitimately refreshes only that one code-input hash.
        receipt = "Germanic/docs/lexeme_reports/pgmc_reconstructions/survey_provenance.json"
        if receipt in changed:
            generator = "Germanic/docs/assembly/build_class_manifests.py"
            now = json.loads((ROOT / receipt).read_text(encoding="utf-8"))
            base = json.loads(committed(ROOT / receipt))
            for record in (now, base):
                record["inputs"].pop(generator)
            self.assertEqual(now, base)
            changed.remove(receipt)
        # CONTROL_PLANE.md is the prose SOURCE/GENERATED map living beside the
        # registries; documenting a new editorial SOURCE there is not a change
        # to any registry fact.
        changed = [path for path in changed
                   if path != "Germanic/docs/sound_changes/registry/CONTROL_PLANE.md"]
        self.assertEqual(changed, [])


if __name__ == "__main__":
    unittest.main()
