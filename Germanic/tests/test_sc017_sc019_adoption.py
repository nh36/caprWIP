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
TECHNICAL_COMMIT = "dcafc62590c9b4cb71328207aab70d153dc6f88e"
ADOPTION_COMMIT = "9b08edc6538ec3d5c1fcd9c156b38b5f40fc4fca"


def text_at_commit(revision, path):
    return subprocess.check_output(
        ["git", "show", f"{revision}:{path.as_posix()}"],
        cwd=ROOT,
        text=True,
    )


def rows_at_commit(revision, path):
    text = text_at_commit(revision, path)
    return list(csv.DictReader(
        io.StringIO("\n".join(
            line for line in text.splitlines()
            if line and not line.startswith("#")
        )),
        delimiter="\t",
    ))


class ChronologyAdoptionTests(unittest.TestCase):
    def test_selected_wool_and_published_explanation_remain_current(self):
        model = (MODELS / "2300-wool-wull.model.md").read_text()
        for field in ("PROTO: *wúllō", "PROTOFORM: *wúllō",
                      "COUNTERPART: wull", "DERIVATION_CLASS: unexplained_unmodelled"):
            self.assertIn(field, model)
        self.assertIn("plausible but unproved", model)
        self.assertIn("SC019 PNWGmcFinalLongORaising", model)

    def test_adoption_did_not_modify_sc018(self):
        before = rows_at_commit(TECHNICAL_COMMIT, REGISTRY / "sc_registry.tsv")
        after = rows_at_commit(ADOPTION_COMMIT, REGISTRY / "sc_registry.tsv")
        self.assertEqual([r for r in before if r["sc_id"] == "SC018"],
                         [r for r in after if r["sc_id"] == "SC018"])

    def test_displacement_observations_survive_reclassification(self):
        old = rows_at_commit(TECHNICAL_COMMIT, REGISTRY / "chronology_edges.tsv")
        new = rows_at_commit(ADOPTION_COMMIT, REGISTRY / "chronology_edges.tsv")
        expected = {("SC017", "SC019"), ("SC019", "SC017")}
        self.assertEqual(len(old), len(new))
        changed = []
        for before, after in zip(old, new):
            if before == after:
                continue
            pair = (after["source_change_id"], after["target_change_id"])
            changed.append(pair)
            for key in before:
                if key not in {"relation_type", "evidence_basis", "notes"}:
                    self.assertEqual(before[key], after[key], key)
            self.assertEqual(after["relation_type"], "technical_computational")
            self.assertEqual(after["evidence_basis"], "boundary_observation")
            self.assertIn(pair, expected)
        self.assertEqual(len(changed), 2)
        self.assertEqual(set(changed), expected)

    def test_current_sc017_sc019_edges_remain_conditional_computational(self):
        text = (ROOT / REGISTRY / "chronology_edges.tsv").read_text()
        current = csv.DictReader(
            (line for line in text.splitlines() if line and not line.startswith("#")),
            delimiter="\t",
        )
        expected = {("SC017", "SC019"), ("SC019", "SC017")}
        selected = [row for row in current
                    if (row["source_change_id"], row["target_change_id"]) in expected]
        self.assertEqual(len(selected), 2)
        self.assertEqual(
            {(row["source_change_id"], row["target_change_id"]) for row in selected},
            expected,
        )
        for row in selected:
            with self.subTest(source=row["source_change_id"], target=row["target_change_id"]):
                self.assertEqual(row["relation_type"], "technical_computational")
                self.assertEqual(row["evidence_basis"], "boundary_observation")

    def test_adoption_commit_preserved_executable_and_frozen_research(self):
        paths = ["Germanic/fsts/germanic.txt",
                 "Germanic/docs/sound_changes/audits/sc017-sc019-wull-investigation"]
        result = subprocess.check_output(
            ["git", "diff", "--name-only", TECHNICAL_COMMIT,
             ADOPTION_COMMIT, "--", *paths], cwd=ROOT, text=True
        )
        self.assertEqual(result.strip(), "")

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
