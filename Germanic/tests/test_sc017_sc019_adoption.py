"""Scientific adoption preserves measured evidence without making it proof."""

import csv
import io
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = Path("Germanic/docs/sound_changes/registry")
MODELS = ROOT / "Germanic/docs/lexeme_reports/model_entries"
PARENT = "dcafc625"


def rows(path, historical=False):
    text = subprocess.check_output(
        ["git", "show", f"{PARENT}:{path}"], cwd=ROOT, text=True
    ) if historical else (ROOT / path).read_text()
    return list(csv.DictReader(
        io.StringIO("\n".join(line for line in text.splitlines()
                             if line and not line.startswith("#"))), delimiter="\t"
    ))


class ChronologyAdoptionTests(unittest.TestCase):
    def test_selected_wool_and_all_sc018_metadata_are_unchanged(self):
        model = (MODELS / "2300-wool-wull.model.md").read_text()
        for field in ("PROTO: *wúllō", "PROTOFORM: *wúllō",
                      "COUNTERPART: wull", "DERIVATION_CLASS: unexplained_unmodelled"):
            self.assertIn(field, model)
        self.assertIn("plausible but unproved", model)
        self.assertIn("SC019 PNWGmcFinalLongORaising", model)
        old = rows(REGISTRY / "sc_registry.tsv", True)
        new = rows(REGISTRY / "sc_registry.tsv")
        self.assertEqual([r for r in old if r["sc_id"] == "SC018"],
                         [r for r in new if r["sc_id"] == "SC018"])

    def test_displacement_observations_survive_reclassification(self):
        old = rows(REGISTRY / "chronology_edges.tsv", True)
        new = rows(REGISTRY / "chronology_edges.tsv")
        self.assertEqual(len(old), len(new))
        changed = []
        for before, after in zip(old, new):
            if before == after:
                continue
            changed.append(after)
            for key in before:
                if key not in {"relation_type", "evidence_basis", "notes"}:
                    self.assertEqual(before[key], after[key], key)
            self.assertEqual(after["relation_type"], "technical_computational")
            self.assertEqual(after["evidence_basis"], "boundary_observation")
            self.assertIn("SC017", str(after))
            self.assertIn("SC019", str(after))
        self.assertEqual(len(changed), 2)

    def test_no_further_executable_or_archive_changes(self):
        paths = ["Germanic/fsts/germanic.txt",
                 "Germanic/docs/sound_changes/audits/sc017-sc019-wull-investigation"]
        result = subprocess.check_output(
            ["git", "diff", PARENT, "--", *paths], cwd=ROOT, text=True
        )
        self.assertEqual(result, "")

    def test_readers_keep_actual_definitions_and_qualified_argument(self):
        import sys
        sys.path.insert(0, str(ROOT / "Germanic/tools"))
        from executable_facts import parse_defines
        definitions = parse_defines((ROOT / "Germanic/fsts/germanic.txt").read_text())
        readers = ROOT / "Germanic/docs/sound_changes/reader_facing"
        for filename, name in [
            ("017-nwgmc-u-lowering.md", "PNWGmcULowering"),
            ("019-nwgmc-final-long-o-raising.md", "PNWGmcFinalLongORaising"),
        ]:
            text = (readers / filename).read_text()
            excerpt = parse_defines(text.split("```foma\n", 1)[1].split("```", 1)[0])
            self.assertEqual(re.sub(r"\s+", "", excerpt[name].body),
                             re.sub(r"\s+", "", definitions[name].body))
        main = (readers / "019-nwgmc-final-long-o-raising.md").read_text()
        for phrase in ("explanatory economy", "not refute", "plausible but",
                       "not a claim of novelty", "separate positive chronological",
                       "trimoric", "Campbell", "Bülbring"):
            self.assertIn(phrase, main)


if __name__ == "__main__":
    unittest.main()
