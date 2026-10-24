from __future__ import annotations

import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SC = ROOT / "Germanic/docs/sound_changes"
SOURCE = ROOT / "Germanic/fsts/germanic.txt"
sys.path.insert(0, str(ROOT / "Germanic/tools"))
import oe_pipeline


def rows(path):
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(
            (line for line in handle if not line.startswith("#")),
            delimiter="\t"))


def definition(text, name):
    bodies = oe_pipeline._define_bodies(oe_pipeline._strip_comments(text))
    if name not in bodies:
        raise AssertionError(f"undefined Foma network: {name}")
    return re.sub(r"\s+", " ", bodies[name]).strip()


def segmental_definition(text, name):
    """Compare segmental kernels; SC035 tests separately verify context lifting."""
    body = definition(text, name)
    if body.startswith(("Ctx(", "FootCtx(")):
        body = body[body.index("(") + 1:-1]
    return body


class FrontingComponentTests(unittest.TestCase):
    def test_exact_laws_and_order_are_preserved(self):
        text = SOURCE.read_text(encoding="utf-8")
        self.assertEqual(segmental_definition(text, "EAFBrightening"),
                         "[ EAFBrighteningStressed ]")
        self.assertEqual(definition(text, "EAFBrighteningStressed"),
                         "[ {*á} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal | .#.] ]")
        self.assertEqual(segmental_definition(text, "EAFBrighteningUnstressed"),
                         "[ {*a} -> {*æ} || _ [EnglishStarConsonant - EnglishStarNasal] ]")
        self.assertEqual(segmental_definition(text, "EAFBrighteningLongFinal"),
                         "[ {*ā} -> {*ǣ} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#. ]")
        self.assertRegex(text, r"\.o\. EAFBrighteningUnstressed\s+"
                         r"\.o\. EAFBrightening\s+"
                         r"\.o\. EAFBrighteningLongFinal\s+\.o\. OEBreaking")

    def test_historical_identity_is_not_assigned_to_support_helpers(self):
        registry = {row["sc_id"]: row for row in rows(SC / "registry/sc_registry.tsv")}
        ordinary = registry["SC043"]
        self.assertEqual((ordinary["hist_stage"], ordinary["hist_scope"],
                          ordinary["verdict"]),
                         ("preoe", "english_specific", "REFORMULATE/SPLIT"))
        for identifier, network in (("SC107", "EAFBrighteningUnstressed"),
                                    ("SC108", "EAFBrighteningLongFinal")):
            row = registry[identifier]
            self.assertEqual(row["entry_type"], "support_stage")
            self.assertEqual(row["fst_identifier"], network)
            for field in ("hist_stage", "hist_scope", "confidence", "verdict"):
                self.assertEqual(row[field], "", (identifier, field))
        self.assertEqual(registry["SC070"]["fst_identifier"], "OEUnstressedFrontingEarly")

    def test_current_reader_definitions_match_real_source(self):
        source = SOURCE.read_text(encoding="utf-8")
        registry = {row["sc_id"]: row for row in rows(SC / "registry/sc_registry.tsv")}
        reader = "\n".join(
            (SC / "reader_facing" / registry[sc]["source_reader_facing_file"]).read_text()
            for sc in ("SC043", "SC107", "SC108"))
        blocks = re.findall(r"```foma\n([\s\S]*?)```", reader)
        self.assertEqual(len(blocks), 4)
        for block in blocks:
            names = re.findall(r"\bdefine (\w+)", block)
            self.assertEqual(len(names), 1)
            name = names[0]
            self.assertEqual(segmental_definition(block, name),
                             segmental_definition(source, name), name)
        self.assertNotIn("AngloFrisianBrighteningStressed", reader)

    def test_prefix_and_final_quantity_constraints_are_component_local(self):
        edges = rows(SC / "registry/chronology_edges.tsv")
        pairs = {(row["source_change_id"], row["target_change_id"]): row for row in edges}
        for pair in (("SC035", "SC107"), ("SC042", "SC108"), ("SC108", "SC042")):
            self.assertEqual(pairs[pair]["evidence_basis"], "technical")
        for pair in (("SC035", "SC043"), ("SC042", "SC043"), ("SC043", "SC042")):
            self.assertNotIn(pair, pairs)


if __name__ == "__main__":
    unittest.main()
