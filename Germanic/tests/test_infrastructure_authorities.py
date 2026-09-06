"""Infrastructure authority guardrails (2026 consistency pass).

These tests enforce "one logical authority for each fact":

* executable order/stages: fsts/germanic.txt, parsed by tools/oe_pipeline.py;
* generated projections (manifest, executable model, sandbox, card-index
  positions) are clean regenerations of that authority;
* the registry resolves SC -> fst_identifier -> executable position without
  contradiction;
* runtime locations come from tools/capr_runtime.py;
* compiled-bin freshness is the explicit build manifest (fail-closed);
* no active tool reintroduces an independent hand-written stage list;
* corpus outputs remain byte-identical (semantic fingerprints pinned).
"""

import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS = REPO_ROOT / "Germanic/tools"
sys.path.insert(0, str(TOOLS))

import oe_pipeline  # noqa: E402
from capr_runtime import (  # noqa: E402
    MIN_BIN_BYTES,
    RuntimeLayout,
    check_build_manifest,
    layout,
    write_build_manifest,
)

SC_DIR = REPO_ROOT / "Germanic/docs/sound_changes"
BASELINE_DIR = SC_DIR / "cascade_baseline"
CARD_INDEX = (SC_DIR / "order_tests/chronology_cards"
              / "chronology_card_index.tsv")

EXPECTED_OUTPUTS_SHA256 = (
    "1309dbc301916a3fa8cd8810d808e56c12da142c849a4e4f7de9df5923eacd31")
EXPECTED_LEGACY_SUBSET_SHA256 = (
    "a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc")
EXPECTED_ROW_COUNT = 385


def _load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _tsv_rows(path):
    import csv
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


class ExecutableModelTests(unittest.TestCase):
    """oe_pipeline is a complete, consistent projection of germanic.txt."""

    def test_model_is_complete_and_contiguous(self):
        stages = oe_pipeline.named_stages()
        self.assertEqual([s.exec_index for s in stages],
                         list(range(1, len(stages) + 1)))
        positions = [s.cascade_position for s in stages
                     if s.cascade_position is not None]
        self.assertEqual(positions, list(range(1, len(positions) + 1)))

    def test_every_stage_has_exactly_one_snapshot_bin(self):
        bins = [s.snapshot_bin for s in oe_pipeline.named_stages()]
        self.assertEqual(len(bins), len(set(bins)),
                         "duplicate snapshot bin names in the model")
        for name in bins:
            self.assertRegex(name, r"^old_english_sandbox_after_[a-z0-9_]+\.bin$")

    def test_expected_snapshot_bins_match_model(self):
        self.assertEqual(oe_pipeline.expected_snapshot_bins(),
                         [s.snapshot_bin for s in oe_pipeline.named_stages()])


class GeneratedProjectionTests(unittest.TestCase):
    """Every generated projection is a clean regeneration of its authority."""

    def test_cascade_order_manifest_is_clean(self):
        mod = _load("cascade_order_manifest")
        committed = (BASELINE_DIR / "cascade_order_manifest.tsv").read_text(
            encoding="utf-8")
        self.assertEqual(mod.manifest_text(), committed,
                         "cascade_order_manifest.tsv is stale; regenerate with "
                         "tools/cascade_order_manifest.py")

    def test_executable_model_view_is_clean(self):
        mod = _load("cascade_order_manifest")
        committed = (BASELINE_DIR / "executable_model.tsv").read_text(
            encoding="utf-8")
        self.assertEqual(mod.model_text(), committed,
                         "executable_model.tsv is stale; regenerate with "
                         "tools/cascade_order_manifest.py")

    def test_generated_sandbox_is_clean(self):
        committed = (REPO_ROOT / "Germanic/fsts/old_english_sandbox.txt"
                     ).read_text(encoding="utf-8")
        self.assertEqual(oe_pipeline.sandbox_text(), committed,
                         "old_english_sandbox.txt is stale; regenerate with "
                         "tools/generate_oe_sandbox.py")

    def test_card_index_positions_are_clean(self):
        mod = _load("sync_chronology_card_positions")
        committed = CARD_INDEX.read_text(encoding="utf-8")
        self.assertEqual(mod.synced_text(), committed,
                         "chronology_card_index.tsv cascade_position column is "
                         "stale; regenerate with "
                         "tools/sync_chronology_card_positions.py")

    def test_card_index_uses_cascade_position_column(self):
        header = CARD_INDEX.read_text(encoding="utf-8").splitlines()[0]
        self.assertIn("cascade_position", header.split("\t"))
        self.assertNotIn("current_order", header.split("\t"))


class RegistryModelResolutionTests(unittest.TestCase):
    """SC id -> fst_identifier -> executable position, no contradictions."""

    def setUp(self):
        views = _load("generate_registry_views")
        self.rows = views.read_tsv(views.SC_REGISTRY)

    def test_every_active_executable_sc_resolves(self):
        for row in self.rows:
            ident = row["fst_identifier"]
            if row["lifecycle_status"] != "active" or not ident:
                continue
            stage = oe_pipeline.stage_for(ident)  # must not raise
            if row["cascade_position"]:
                self.assertEqual(str(stage.cascade_position),
                                 row["cascade_position"],
                                 f"{row['sc_id']}: registry cascade_position "
                                 "contradicts the executable model")

    def test_retired_scs_have_no_cascade_position(self):
        for row in self.rows:
            if row["lifecycle_status"] == "retired":
                self.assertEqual(row["cascade_position"], "",
                                 f"{row['sc_id']} is retired but has a "
                                 "cascade_position")


class RuntimeLayoutTests(unittest.TestCase):
    def test_host_layout_resolves_logical_resources(self):
        rt = layout()
        self.assertTrue(rt.germanic_fst.is_file())
        self.assertTrue(rt.sandbox_fst.is_file())
        self.assertTrue(rt.corpus_tsv.is_file())
        if not rt.is_container:
            self.assertEqual(rt.bin_dir, rt.repo_root / "backend")
            self.assertTrue(rt.bin_dir.is_dir())
        else:
            self.assertEqual(rt.bin_dir, rt.germanic_dir)


class BuildManifestTests(unittest.TestCase):
    """The build manifest is the fail-closed freshness contract."""

    def _fake_layout(self, root: Path) -> RuntimeLayout:
        (root / "fsts").mkdir()
        (root / "data").mkdir()
        (root / "bin").mkdir()
        (root / "fsts/germanic.txt").write_text("define X a -> b;\n")
        (root / "fsts/old_english_sandbox.txt").write_text("source ...\n")
        (root / "data/germanic-aligned-final.tsv").write_text("ID\n1\n")
        return RuntimeLayout(germanic_dir=root, repo_root=root,
                             bin_dir=root / "bin", is_container=False)

    def test_fresh_bins_pass_and_source_change_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rt = self._fake_layout(root)
            expected = ["stage_one.bin"]
            (rt.bin_dir / "stage_one.bin").write_bytes(b"x" * (MIN_BIN_BYTES + 1))
            write_build_manifest(expected, runner="local", rt=rt)
            self.assertEqual(check_build_manifest(expected, rt=rt), [])
            # mutate a source WITHOUT rebuilding -> must fail clearly
            (root / "fsts/germanic.txt").write_text("define X a -> c;\n")
            problems = check_build_manifest(expected, rt=rt)
            self.assertTrue(any("germanic.txt" in p and "stale" in p
                                for p in problems), problems)

    def test_missing_manifest_and_degenerate_bin_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rt = self._fake_layout(root)
            expected = ["stage_one.bin"]
            problems = check_build_manifest(expected, rt=rt)
            self.assertTrue(any("missing build manifest" in p for p in problems))
            (rt.bin_dir / "stage_one.bin").write_bytes(b"tiny")
            write_build_manifest(expected, runner="local", rt=rt)
            problems = check_build_manifest(expected, rt=rt)
            self.assertTrue(any("degenerate bin" in p for p in problems))

    def test_expected_bin_set_change_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rt = self._fake_layout(root)
            (rt.bin_dir / "stage_one.bin").write_bytes(b"x" * (MIN_BIN_BYTES + 1))
            write_build_manifest(["stage_one.bin"], runner="local", rt=rt)
            problems = check_build_manifest(["stage_one.bin", "stage_two.bin"],
                                            rt=rt)
            self.assertTrue(any("expected bin set differs" in p
                                for p in problems), problems)


class NoDuplicateStageListTests(unittest.TestCase):
    """No active tool may reintroduce an independent stage universe."""

    # literal hand-written stage list: STAGES = [ ("Name", "bin"), ...
    FORBIDDEN = re.compile(r"STAGES\s*=\s*\[\s*\(\s*['\"]")

    def test_no_hand_written_stage_lists_in_active_tools(self):
        offenders = []
        for path in sorted(TOOLS.glob("*.py")):
            if self.FORBIDDEN.search(path.read_text(encoding="utf-8")):
                offenders.append(path.name)
        self.assertEqual(offenders, [],
                         "hand-written STAGES lists are forbidden; derive "
                         "stages from oe_pipeline")

    def test_no_alias_tables_in_active_tools(self):
        for path in sorted(TOOLS.glob("*.py")):
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("STAGE_ALIASES", text,
                             f"{path.name}: alias tables are retired — use "
                             "canonical Foma identifiers")
            self.assertNotIn("TRACER_NAME", text,
                             f"{path.name}: alias tables are retired — use "
                             "canonical Foma identifiers")

    def test_retired_instrumentation_stays_deleted(self):
        for name in ("trace_old_english_sandbox.py",
                     "annotate_old_english_sandbox_results.py",
                     "run_old_english_sandbox_workflow.sh"):
            self.assertFalse((TOOLS / name).exists(),
                             f"{name} was retired in the 2026 infrastructure "
                             "pass; the generated sandbox is the only "
                             "instrumentation")
        fst = (REPO_ROOT / "Germanic/fsts/germanic.txt").read_text(
            encoding="utf-8")
        self.assertNotIn("EnglishAfterProtoInput", fst)
        self.assertNotIn("english_after_", fst)


class OutputIdentityTests(unittest.TestCase):
    """The refactor must not change corpus outputs (semantic fingerprints)."""

    def test_semantic_fingerprints_unchanged(self):
        summary = json.loads(
            (BASELINE_DIR / "cascade_baseline_summary.json").read_text(
                encoding="utf-8"))
        text = json.dumps(summary)
        self.assertIn(EXPECTED_OUTPUTS_SHA256, text,
                      "corpus outputs fingerprint changed — the "
                      "infrastructure refactor altered scientific outputs")
        self.assertIn(EXPECTED_LEGACY_SUBSET_SHA256, text)
        self.assertIn(str(EXPECTED_ROW_COUNT), text)


if __name__ == "__main__":
    unittest.main()
