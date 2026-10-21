"""Stage resolution has one scientific implementation, separate from lexical presentation.

The reconstruction survey and the lexical assembler both consume
Germanic/tools/entry_stages.py. The survey's provenance must therefore track
that module and never an editorial assembler, so that changing where lexical
entries are published cannot change recorded scientific dependencies.
"""

import ast
import csv
import json
import subprocess
import sys
import unittest
import warnings
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "Germanic/tools"
ASSEMBLY = ROOT / "Germanic/docs/assembly"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(ASSEMBLY))

import build_class_manifests as manifests
import entry_stages
import pgmc_reconstruction_survey as survey

SURVEY_RECEIPT = ROOT / survey.DIRECTORY / "survey_provenance.json"
LEXICAL_RECEIPT = ASSEMBLY / "lexical_source_provenance.json"
STAGES = "Germanic/tools/entry_stages.py"


def tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


class StageResolutionAuthorityTests(unittest.TestCase):
    def test_there_is_exactly_one_implementation_consumed_by_both_pipelines(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", SyntaxWarning)
            definitions = [
                path.relative_to(ROOT).as_posix()
                for path in (ROOT / "Germanic").rglob("*.py")
                if "archive" not in path.parts and "__pycache__" not in path.parts
                and any(isinstance(node, ast.FunctionDef) and node.name == "resolve_stages"
                        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))))
            ]
        self.assertEqual(definitions, [STAGES])
        self.assertIs(survey.resolve_stages, entry_stages.resolve_stages)
        self.assertIs(manifests.resolve_stages, entry_stages.resolve_stages)
        self.assertIs(manifests.load_stage_metadata, entry_stages.load_stage_metadata)

    def test_stage_module_is_scientific_code_without_editorial_dependencies(self):
        tree = ast.parse((ROOT / STAGES).read_text(encoding="utf-8"))
        imported = {
            (node.module if isinstance(node, ast.ImportFrom) else alias.name).split(".")[0]
            for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))
            for alias in (node.names if isinstance(node, ast.Import) else [node])
        }
        self.assertLessEqual(imported, set(sys.stdlib_module_names))

    def test_survey_does_not_load_the_editorial_assembler(self):
        probe = (
            "import sys; sys.path.insert(0, sys.argv[1]); "
            "import pgmc_reconstruction_survey; "
            "print('build_class_manifests' in sys.modules)"
        )
        result = subprocess.run([sys.executable, "-c", probe, str(TOOLS)],
                                capture_output=True, text=True, check=True)
        self.assertEqual(result.stdout.strip(), "False")

    def test_survey_provenance_tracks_stage_code_and_no_assembly_file(self):
        inputs = json.loads(SURVEY_RECEIPT.read_text(encoding="utf-8"))["inputs"]
        self.assertIn(STAGES, inputs)
        self.assertEqual([key for key in inputs if key.startswith("Germanic/docs/assembly/")], [])

    def test_lexical_provenance_tracks_stage_code_and_editorial_inputs(self):
        inputs = json.loads(LEXICAL_RECEIPT.read_text(encoding="utf-8"))["inputs"]
        for key in (STAGES, "Germanic/docs/assembly/build_class_manifests.py",
                    "Germanic/docs/assembly/lexical_editorial_order.tsv"):
            self.assertIn(key, inputs)

    def test_published_manifest_stages_equal_survey_stage_assignments(self):
        survey_rows = {row["row_id"]: row for row in survey.inventory()}
        manifest = tsv(ASSEMBLY / "manifest_all_by_class.tsv")
        self.assertEqual(len(manifest), 167)
        for row in manifest:
            expected = survey_rows[row["row_id"]]
            self.assertEqual(
                (row["proto_stage"], row["protoform_stage"], row["protoform_variety"]),
                (expected["proto_stage"], expected["input_stage"], expected["input_variety"]),
                row["row_id"])

    def test_unresolved_stage_fails_closed_for_both_consumers(self):
        stages = entry_stages.resolve_stages("0", "*a", "*b", {})
        self.assertEqual(stages[:3], ("pgmc", "", ""))
        self.assertTrue(stages[3])
        self.assertEqual(entry_stages.resolve_stages("0", "*a", "*a", {}), ("pgmc", "pgmc", "", []))


if __name__ == "__main__":
    unittest.main()
