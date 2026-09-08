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
import subprocess
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

# Rebaselined 2026 for the `thought` addition (sc025-sc104 memo §12): one
# corpus row added (thought, PGmc *θánxtē > OE þōhte) as the live low-vowel
# witness of SC103 -> SC104. Every pre-existing output is byte-identical, so
# the legacy-380 fingerprint below is unchanged.
EXPECTED_OUTPUTS_SHA256 = (
    "862b0908b2ab44097eeda3bf82f95d76625eb169230efa3a072eb93c1311c35b")
EXPECTED_LEGACY_SUBSET_SHA256 = (
    "a72bdeb8451039206ab0b90110547f50171c209d5b9c08c71219ed45df5165fc")
EXPECTED_ROW_COUNT = 386


def _load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # dataclasses resolve annotations via sys.modules
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


class NoIndependentOrderParserTests(unittest.TestCase):
    """Active chronology tooling must not re-parse the production chain."""

    SCOS = TOOLS / "sound_change_order_sensitivity.py"

    def test_no_private_composition_regex_parser(self):
        text = self.SCOS.read_text(encoding="utf-8")
        for forbidden in (r"define EnglishProtoToOE \(",
                          r"define EarlyEnglishLineChanges \["):
            self.assertNotIn(forbidden, text,
                             "sound_change_order_sensitivity.py reintroduced "
                             "its own production-chain regex parser; use "
                             "oe_pipeline.composition_members_of")

    def test_no_hand_maintained_component_lists(self):
        text = self.SCOS.read_text(encoding="utf-8")
        for name in ("POST_EPENTHESIS_RULES", "PWGMC_COMPONENT_RULES"):
            self.assertNotIn(name, text,
                             f"{name} is a hand-maintained production-order "
                             "copy; derive membership from oe_pipeline")
        self.assertIn("import oe_pipeline", text)

    def test_model_matches_bundle_membership(self):
        # The shared parser is the one authority for bundle components:
        # components must be consecutive named stages of the model.
        comps = oe_pipeline.composition_members_of("EarlyEnglishLineChanges")
        names = [s.foma_identifier for s in oe_pipeline.named_stages()]
        start = names.index(comps[0])
        self.assertEqual(names[start:start + len(comps)], comps)


class NoStaleBinSearchTests(unittest.TestCase):
    """Active OE tools must not search stale/fallback bin locations."""

    FORBIDDEN = (
        re.compile(r"live_bin_candidates"),
        re.compile(r"/usr/backend"),
        re.compile(r"""["']server["']\s*/|/\s*["']server["']"""),
        re.compile(r"""fsts["']?\s*/\s*["']old_english\.bin"""),
    )

    def test_no_candidate_bin_searches(self):
        offenders = []
        for path in sorted(TOOLS.glob("*.py")):
            text = path.read_text(encoding="utf-8")
            for pattern in self.FORBIDDEN:
                if pattern.search(text):
                    offenders.append(f"{path.name}: {pattern.pattern}")
        self.assertEqual(offenders, [],
                         "runtime bins live ONLY in capr_runtime.layout()."
                         "bin_dir (host backend/ == container /usr/app)")


class DerivedCascadePositionTests(unittest.TestCase):
    """Registry cascade_position is derived from the executable model."""

    def test_registry_positions_are_synced_from_model(self):
        mod = _load("sync_registry_cascade_positions")
        views = _load("generate_registry_views")
        committed = views.SC_REGISTRY.read_text(encoding="utf-8")
        self.assertEqual(mod.synced_text(), committed,
                         "sc_registry.tsv cascade_position column is out of "
                         "sync with oe_pipeline; run "
                         "tools/sync_registry_cascade_positions.py")

    def test_registry_header_declares_position_derived(self):
        views = _load("generate_registry_views")
        header = "\n".join(
            line for line in views.SC_REGISTRY.read_text(
                encoding="utf-8").splitlines() if line.startswith("#"))
        self.assertIn("cascade_position is DERIVED", header)

    def test_positions_derive_from_synthetic_composition(self):
        # Moving a rule in a (synthetic) production composition changes the
        # derived positions with no hand-edited position data anywhere.
        template = (
            "define RuleA a -> b;\n"
            "define RuleB b -> c;\n"
            "define RuleC c -> d;\n"
            "define EnglishProtoInput ?*;\n"
            "define OldEnglishSurface ?*;\n"
            "define EnglishProtoToOE ( {order} ); # capr:bundle\n"
            "define OldEnglish EnglishProtoInput .o. EnglishProtoToOE "
            ".o. OldEnglishSurface; # capr:bundle\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            fst = Path(tmp) / "germanic.txt"
            fst.write_text(template.format(order="RuleA .o. RuleB .o. RuleC"),
                           encoding="utf-8")
            before = {s.foma_identifier: s.cascade_position
                      for s in oe_pipeline.parse_stages(fst)
                      if s.cascade_position is not None}
            fst.write_text(template.format(order="RuleB .o. RuleC .o. RuleA"),
                           encoding="utf-8")
            after = {s.foma_identifier: s.cascade_position
                     for s in oe_pipeline.parse_stages(fst)
                     if s.cascade_position is not None}
        self.assertEqual(before, {"RuleA": 1, "RuleB": 2, "RuleC": 3})
        self.assertEqual(after, {"RuleB": 1, "RuleC": 2, "RuleA": 3})


class TraceFreshnessTests(unittest.TestCase):
    """Canonical trace evidence is tied to the validated build (fail-closed)."""

    TRACE = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"

    def setUp(self):
        self.mod = _load("oe_full_trace_report")

    def test_committed_trace_is_canonical_and_fresh(self):
        problems = self.mod.trace_provenance_problems(
            self.TRACE.read_text(encoding="utf-8"))
        self.assertEqual(problems, [],
                         "committed full trace report is stale or "
                         "noncanonical; regenerate via adjudicate.py "
                         "SCNNN --evidence")

    def test_missing_provenance_fails_closed(self):
        problems = self.mod.trace_provenance_problems("=== BUCKET: x ===\n")
        self.assertTrue(problems)

    def test_noncanonical_or_stale_provenance_fails_closed(self):
        live = self.TRACE.read_text(encoding="utf-8")
        # strip the canonical marker -> must be refused
        broken = live.replace("bins_provenance: canonical",
                              "bins_provenance: NONCANONICAL DEBUG")
        self.assertTrue(any("not canonical" in p for p in
                            self.mod.trace_provenance_problems(broken)))
        # corrupt a recorded source hash -> stale
        stale = re.sub(r"(germanic\.txt sha256: )[0-9a-f]{8}",
                       r"\g<1>00000000", live, count=1)
        self.assertTrue(any("STALE" in p for p in
                            self.mod.trace_provenance_problems(stale)))


class CoverageFreshnessTests(unittest.TestCase):
    """Coverage census must refuse stale runtime-derived upstream evidence."""

    def test_census_refuses_stale_trace(self):
        mod = _load("rule_coverage_census")
        with tempfile.TemporaryDirectory() as tmp:
            stale = Path(tmp) / "trace.txt"
            stale.write_text("=== STAGE FIRING SUMMARY ===\n\nRuleA: 0\n",
                             encoding="utf-8")
            mod.FULL_TRACE = stale
            with self.assertRaises(SystemExit):
                mod.build_rows()

    def test_committed_census_is_a_clean_projection(self):
        mod = _load("rule_coverage_census")
        rows = mod.build_rows()
        lines = [mod.PREAMBLE + "\t".join(mod.HEADER)]
        for r in rows:
            lines.append("\t".join(r[h] for h in mod.HEADER))
        expected = "\n".join(lines) + "\n"
        committed = mod.OUTPUT.read_text(encoding="utf-8")
        self.assertEqual(expected, committed,
                         "rule_coverage_census.tsv is stale; regenerate with "
                         "tools/rule_coverage_census.py")


class SandboxEquivalenceTests(unittest.TestCase):
    """Production old_english.bin == final generated sandbox stage,
    semantically, over all selected corpus rows (evidence validated
    fail-closed against the live sources)."""

    def test_equivalence_evidence_is_fresh_and_equivalent(self):
        mod = _load("check_production_sandbox_equivalence")
        path = mod.evidence_path()
        self.assertTrue(path.is_file(),
                        "missing oe_equivalence_report.json; run adjudicate.py "
                        "SCNNN --evidence (or tools/"
                        "check_production_sandbox_equivalence.py in the "
                        "container)")
        report = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "equivalent")
        self.assertEqual(report["rows_compared"], EXPECTED_ROW_COUNT)
        from capr_runtime import sha256_of
        rt = layout()
        live = {
            "germanic.txt": sha256_of(rt.germanic_fst),
            "old_english_sandbox.txt": sha256_of(rt.sandbox_fst),
            "germanic-aligned-final.tsv": sha256_of(rt.corpus_tsv),
        }
        self.assertEqual(report["sources"], live,
                         "equivalence evidence is STALE w.r.t. the live "
                         "sources; re-run the evidence step")
        final_bin = oe_pipeline.named_stages()[-1].snapshot_bin
        self.assertEqual(report["sandbox_final_bin"], final_bin)


class ArchiveCurrentSeparationTests(unittest.TestCase):
    """SOURCE / GENERATED / ARCHIVE are disjoint genres (no hybrids)."""

    ARCHIVES = (
        BASELINE_DIR / "historical_audit_table.tsv",
        BASELINE_DIR / "rename_migration_manifest.tsv",
    )
    ARCHIVE_BUILDERS = ("build_historical_audit_table.py",
                        "build_rename_migration_manifest.py")

    def test_frozen_archives_carry_archive_banner(self):
        for path in self.ARCHIVES:
            first = path.read_text(encoding="utf-8").splitlines()[0]
            self.assertIn("ARCHIVE / FROZEN", first, path.name)

    def test_finalize_never_rewrites_frozen_archives(self):
        adjudicate = (TOOLS / "adjudicate.py").read_text(encoding="utf-8")
        for name in self.ARCHIVE_BUILDERS:
            self.assertNotIn(f'"{name}"', adjudicate.replace("'", '"'),
                             f"{name} must not be in the finalize chain — "
                             "frozen archives are never rewritten")

    def test_archival_builders_refuse_without_explicit_flag(self):
        for name in self.ARCHIVE_BUILDERS:
            proc = subprocess.run([sys.executable, str(TOOLS / name)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 1, name)
            self.assertIn("ARCHIVE", proc.stderr, name)


class FrozenArchivePositionSemanticsTests(unittest.TestCase):
    """`cascade_position` (live) vs frozen `current_cascade_position`.

    Two similarly-named fields mean different things and MUST NOT be
    conflated:

    * `audits/sc001-sc020-chronology-audit.tsv` `cascade_position` is a LIVE
      projection and must track `cascade_baseline/cascade_order_manifest.tsv`;
    * `cascade_baseline/historical_audit_table.tsv` `current_cascade_position`
      is an ARCHIVE field meaning "position current at the time the snapshot
      was frozen". It must never be resynchronized when a later adjudication
      inserts, retires, or moves an executable rule, and drift from the live
      cascade is expected and meaningful.
    """

    FROZEN = BASELINE_DIR / "historical_audit_table.tsv"
    LIVE = SC_DIR / "audits/sc001-sc020-chronology-audit.tsv"
    MANIFEST = BASELINE_DIR / "cascade_order_manifest.tsv"
    ARCHIVE_WRITER = "build_historical_audit_table.py"

    def test_frozen_historical_audit_is_not_a_live_position_authority(self):
        banner = "\n".join(
            line for line in self.FROZEN.read_text(
                encoding="utf-8").splitlines()[:20]
            if line.startswith("#"))
        self.assertIn("ARCHIVE / FROZEN", banner)
        self.assertIn("current_cascade_position", banner,
                      "the frozen archive must document that "
                      "current_cascade_position is audit-time state")
        self.assertRegex(banner, r"MUST NOT be\s*\n?#?\s*synchronized",
                         "the frozen banner must forbid resynchronization")

        # Only the archival builder may write the field; no live tool or test
        # may read it as the current executable position.
        readers = set()
        for path in list((REPO_ROOT / "Germanic/tools").glob("*.py")) + \
                list((REPO_ROOT / "Germanic/tests").glob("*.py")):
            if path.name in (self.ARCHIVE_WRITER, Path(__file__).name):
                continue
            if "current_cascade_position" in path.read_text(encoding="utf-8"):
                readers.add(path.name)
        self.assertEqual(readers, set(),
                         "current_cascade_position is a frozen archive field; "
                         "no active tool/test may treat it as the current "
                         "executable position")

        # The frozen archive is neither generated nor finalized.
        adjudicate = (TOOLS / "adjudicate.py").read_text(encoding="utf-8")
        self.assertNotIn(f'"{self.ARCHIVE_WRITER}"',
                         adjudicate.replace("'", '"'))
        views = _load("generate_registry_views")
        generated = {Path(p).name for p in views.build_all()}
        self.assertNotIn(self.FROZEN.name, generated)

    def test_live_chronology_audit_is_the_current_position_authority(self):
        positions = {row["foma_identifier"]: row["position"]
                     for row in _tsv_rows_skip_comments(self.MANIFEST)}
        checked = 0
        for row in _tsv_rows(self.LIVE):
            pos = (row.get("cascade_position") or "").strip()
            ident = (row.get("foma_identifier") or "").strip()
            if not pos.isdigit() or ident not in positions:
                continue
            checked += 1
            self.assertEqual(pos, positions[ident],
                             f"{row['sc_id']}: live audit cascade_position "
                             "must match the order manifest")
        self.assertGreater(checked, 0, "live audit matrix yielded no rows")

        # The cross-artifact current-position test must read the LIVE matrix,
        # never the frozen archive.
        cross = (REPO_ROOT / "Germanic/tests"
                 / "test_sc_chronology_cross_artifact.py").read_text(
                     encoding="utf-8")
        self.assertIn("sc001-sc020-chronology-audit.tsv", cross)
        self.assertNotIn("historical_audit_table", cross)

    def test_control_plane_documents_the_distinction(self):
        text = (SC_DIR / "registry/CONTROL_PLANE.md").read_text(
            encoding="utf-8")
        self.assertIn("current_cascade_position", text)
        self.assertIn("audits/sc001-sc020-chronology-audit.tsv", text)
        self.assertNotIn("current_order", text,
                         "do not introduce another vague position synonym")


class NoSupersededCurrentFactsTests(unittest.TestCase):
    """Current generated artifacts must not carry superseded facts as
    current (archival files stating them as history are legitimate)."""

    def current_generated_files(self):
        views = _load("generate_registry_views")
        paths = list(views.build_all().keys())
        paths += [BASELINE_DIR / "cascade_order_manifest.tsv",
                  BASELINE_DIR / "executable_model.tsv",
                  BASELINE_DIR / "rule_coverage_census.tsv"]
        return paths

    def test_no_pre_split_sc004_language_in_current_artifacts(self):
        for path in self.current_generated_files():
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("split decision pending", text, path.name)
            self.assertNotIn("split decision precedes", text, path.name)

    def test_current_positions_match_model_not_superseded_claims(self):
        pos = {s.foma_identifier: str(s.cascade_position)
               for s in oe_pipeline.named_stages()
               if s.cascade_position is not None}
        census = _tsv_rows_skip_comments(
            BASELINE_DIR / "rule_coverage_census.tsv")
        for row in census:
            self.assertEqual(row["cascade_position"],
                             pos[row["foma_identifier"]],
                             f"{row['sc_id']}: census position is not the "
                             "executable model's")
        # the superseded audit-time claims must not surface as current
        self.assertNotEqual(pos.get("PNWGmcLongELowering"), "12")
        self.assertNotEqual(pos.get("EAFLongANasalRounding"), "26")


def _tsv_rows_skip_comments(path):
    import csv
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if ln and not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class NestedBundleCascadePositionTests(unittest.TestCase):
    """The numbered cascade is a structural span, not a bundle-name list.

    A nested structural bundle inside the numbered cascade must not silently
    lose cascade positions merely because its name is new.
    """

    TEMPLATE = (
        "define RuleA a -> b;\n"
        "define RuleB b -> c;\n"
        "define RuleC c -> d;\n"
        "define RuleD d -> e;\n"
        "define EnglishProtoInput ?*;\n"
        "define OldEnglishSurface ?*;\n"
        "define BrandNewInnerBundle ( RuleB .o. RuleC ); # capr:bundle\n"
        "define EnglishProtoToOE ( {order} ); # capr:bundle\n"
        "define OldEnglish EnglishProtoInput .o. EnglishProtoToOE "
        ".o. OldEnglishSurface; # capr:bundle\n"
    )

    def _positions(self, tmp, order):
        fst = Path(tmp) / "germanic.txt"
        fst.write_text(self.TEMPLATE.format(order=order), encoding="utf-8")
        return {s.foma_identifier: s.cascade_position
                for s in oe_pipeline.parse_stages(fst)
                if s.cascade_position is not None}

    def test_nested_bundle_members_receive_contiguous_positions(self):
        with tempfile.TemporaryDirectory() as tmp:
            pos = self._positions(
                tmp, "RuleA .o. BrandNewInnerBundle .o. RuleD")
            self.assertEqual(pos, {"RuleA": 1, "RuleB": 2,
                                   "RuleC": 3, "RuleD": 4})

    def test_moving_the_nested_bundle_renumbers_mechanically(self):
        with tempfile.TemporaryDirectory() as tmp:
            pos = self._positions(
                tmp, "RuleA .o. RuleD .o. BrandNewInnerBundle")
            self.assertEqual(pos, {"RuleA": 1, "RuleD": 2,
                                   "RuleB": 3, "RuleC": 4})

    def test_prelude_and_surface_stay_outside_the_numbering(self):
        with tempfile.TemporaryDirectory() as tmp:
            fst = Path(tmp) / "germanic.txt"
            fst.write_text(self.TEMPLATE.format(
                order="RuleA .o. BrandNewInnerBundle .o. RuleD"),
                encoding="utf-8")
            outside = {s.foma_identifier: s.cascade_position
                       for s in oe_pipeline.parse_stages(fst)
                       if s.foma_identifier in ("EnglishProtoInput",
                                                "OldEnglishSurface")}
            self.assertEqual(outside, {"EnglishProtoInput": None,
                                       "OldEnglishSurface": None})

    def test_production_positions_remain_contiguous(self):
        positions = [s.cascade_position for s in oe_pipeline.named_stages()
                     if s.cascade_position is not None]
        self.assertEqual(positions, list(range(1, len(positions) + 1)))


class ScosRegistryIdentityTests(unittest.TestCase):
    """SCOS takes SC -> FST identity from sc_registry.tsv, never from the
    inventory view's rule_source_anchor documentation."""

    def setUp(self):
        self.scos = _load("sound_change_order_sensitivity")

    def test_registry_supplies_fst_identifier(self):
        idents = self.scos.registry_fst_identifiers(
            SC_DIR / "registry/sc_registry.tsv")
        self.assertEqual(idents.get("SC043"), "EAFBrightening")
        self.assertEqual(idents.get("SC020"), "EAFFinalZDeletion")

    def test_load_inventory_uses_registry_not_anchor(self):
        inventory = SC_DIR / "sound_change_inventory.tsv"
        by_id, _ = self.scos.load_inventory(
            inventory,
            self.scos.registry_fst_identifiers(
                SC_DIR / "registry/sc_registry.tsv"))
        self.assertEqual(by_id["SC043"].rule_name, "EAFBrightening")
        # The registry is the ONE identity authority, and since the inventory
        # authority repair it carries an fst_identifier for every SC -- the
        # support and orthography stages included, whose identity used to
        # survive only in a hand-typed annotation anchor.
        idents = self.scos.registry_fst_identifiers(
            SC_DIR / "registry/sc_registry.tsv")
        self.assertEqual(idents.get("SC090"), "OECjCleanup")
        self.assertEqual([sc for sc, name in idents.items() if not name], [])
        # a row with no registry identifier is metadata-only, not a target
        self.assertEqual(
            self.scos.load_inventory(inventory, {})[0]["SC043"].rule_name, "")
        lookup = self.scos.inventory_rule_lookup(list(by_id.values()))
        self.assertNotIn("", lookup)

    def test_no_anchor_based_identity_extraction(self):
        src = (TOOLS / "sound_change_order_sensitivity.py").read_text(
            encoding="utf-8")
        self.assertNotIn("extract_rule_name", src)
        self.assertNotIn('row.get("rule_source_anchor")', src)

    def test_unknown_registry_identifier_fails_clearly(self):
        with tempfile.TemporaryDirectory() as tmp:
            inv = Path(tmp) / "inventory.tsv"
            inv.write_text(
                "change_id\tcurrent_order\tdisplay_name\tentry_type\t"
                "include_in_volume\tnotes\n"
                "SC999\t1\tFake\thistorical_sound_change\tyes\t\n",
                encoding="utf-8")
            with self.assertRaises(SystemExit):
                self.scos.load_inventory(inv, {"SC999": "NoSuchFstRule"})

    def test_every_crossable_profile_rule_resolves_to_an_sc(self):
        """No anonymous crossings: every rule inside either SCOS order
        profile must resolve to an SC via the registry, so an
        order-sensitivity crossing is never mislabeled as a placeholder
        ('blocked_by_runner_limitation') stage."""
        idents = self.scos.registry_fst_identifiers(
            SC_DIR / "registry/sc_registry.tsv")
        _, ordered = self.scos.load_inventory(
            SC_DIR / "sound_change_inventory.tsv", idents)
        lookup = self.scos.inventory_rule_lookup(ordered)
        bundle = self.scos.PWGMC_BUNDLE
        default = oe_pipeline.composition_members_of(
            self.scos.EXPERIMENT_ROOT)
        expanded = [m for r in default for m in
                    (oe_pipeline.composition_members_of(r)
                     if r == bundle else [r])]
        for profile_name, profile in (("default", default),
                                      ("expanded-pwgmc", expanded)):
            unresolved = [r for r in profile
                          if r != bundle and r not in lookup]
            self.assertEqual(
                unresolved, [],
                f"{profile_name} profile rules without registry SC identity "
                "(backfill fst_identifier in sc_registry.tsv)")


class ControlPlaneDocTests(unittest.TestCase):
    """Current routing docs must reflect the derived/frozen architecture."""

    CONTROL_PLANE = SC_DIR / "registry/CONTROL_PLANE.md"

    def _section(self, text, heading):
        start = text.index(heading)
        rest = text[start + len(heading):]
        nxt = rest.find("\n## ")
        return rest if nxt < 0 else rest[:nxt]

    def test_archives_not_classified_as_generated(self):
        text = self.CONTROL_PLANE.read_text(encoding="utf-8")
        generated = self._section(text, "## GENERATED")
        archive = self._section(text, "## ARCHIVE")
        for name in ("historical_audit_table.tsv",
                     "rename_migration_manifest.tsv"):
            self.assertNotIn(name, generated,
                             f"{name} is ARCHIVE/FROZEN, not GENERATED")
            self.assertIn(name, archive)

    def test_control_plane_declares_cascade_position_derived(self):
        text = self.CONTROL_PLANE.read_text(encoding="utf-8")
        self.assertIn("sync_registry_cascade_positions", text)
        self.assertNotIn("executable identifier, cascade position", text)

    def test_docs_readme_lists_archives_as_archive(self):
        text = (REPO_ROOT / "Germanic/docs/README.md").read_text(
            encoding="utf-8")
        generated = self._section(text, "## What is GENERATED")
        self.assertNotIn("historical_audit_table", generated)
        self.assertNotIn("rename_migration_manifest", generated)


class EvidencePrerequisiteTests(unittest.TestCase):
    """--evidence regenerates the mechanical prerequisites itself."""

    def test_mechanical_prereqs_cover_the_generated_checks(self):
        adj = _load("adjudicate")
        prereq_names = {p.name for p in adj.MECHANICAL_PREREQS}
        self.assertEqual(prereq_names, {
            "sync_registry_cascade_positions.py",
            "cascade_order_manifest.py",
            "generate_oe_sandbox.py",
            "sync_chronology_card_positions.py",
        })
        for p in adj.MECHANICAL_PREREQS:
            self.assertTrue(p.is_file(), p)
        # every prerequisite that --evidence later checks is regenerable
        checked = {script for script, _ in adj.GENERATED_CHECKS}
        self.assertEqual(checked, prereq_names)


class CurrentStateFingerprintTests(unittest.TestCase):
    """CURRENT_STATE.md must advertise the canonical current baseline."""

    def test_current_state_matches_cascade_baseline_summary(self):
        summary = json.loads(
            (BASELINE_DIR / "cascade_baseline_summary.json").read_text(
                encoding="utf-8"))
        text = (REPO_ROOT / "Germanic/docs/CURRENT_STATE.md").read_text(
            encoding="utf-8")
        self.assertIn(summary["outputs_sha256"], text)
        self.assertIn(summary["legacy_subset_sha256"], text)
        # no superseded fingerprints advertised as current
        self.assertNotIn(
            "7bed2ba862d91f82a0b7553e1a98fc78d9137483d39d94af0050af5aa18bdd33",
            text)


class TraceBuildIdentityTests(unittest.TestCase):
    """Trace provenance rejects a materially different build configuration."""

    TRACE = REPO_ROOT / "Germanic/docs/debug_snapshots/oe_full_trace_report.txt"

    def setUp(self):
        self.mod = _load("oe_full_trace_report")
        self.live = self.TRACE.read_text(encoding="utf-8")

    def test_mismatched_expected_bin_count_is_rejected(self):
        broken = re.sub(r"build_manifest_expected_bins: \d+",
                        "build_manifest_expected_bins: 7", self.live, count=1)
        self.assertTrue(any("expected-bin count" in p for p in
                            self.mod.trace_provenance_problems(broken)))

    def test_mismatched_foma_version_is_rejected(self):
        manifest = REPO_ROOT / "backend" / "oe_build_manifest.json"
        if not manifest.is_file():
            self.skipTest("foma-version identity check compares against the "
                          "local runtime build manifest (adjudicate "
                          "--evidence); absent in a clean checkout")
        broken = re.sub(r"build_manifest_foma_version: .*",
                        "build_manifest_foma_version: foma 9.9.9",
                        self.live, count=1)
        self.assertTrue(any("Foma version" in p for p in
                            self.mod.trace_provenance_problems(broken)))


class ArchiveNotCurrentAuthorityTests(unittest.TestCase):
    """Frozen archives are never required to track future current metadata."""

    def test_guardrails_do_not_couple_archives_to_live_staging(self):
        src = (REPO_ROOT /
               "Germanic/tests/test_adjudication_protocol_guardrails.py"
               ).read_text(encoding="utf-8")
        self.assertNotIn("disagrees with staging", src)
        self.assertIn("ARCHIVE/FROZEN", src)


class CensusRegistryIdentityTests(unittest.TestCase):
    """rule_coverage_census executable identity comes from the registry,
    never from rule_source_anchor; census scope is the numbered cascade."""

    @classmethod
    def setUpClass(cls):
        cls.census = _load("rule_coverage_census")
        cls.pipeline = _load("oe_pipeline")

    def test_census_source_never_reads_rule_source_anchor(self):
        src = (TOOLS / "rule_coverage_census.py").read_text(encoding="utf-8")
        self.assertNotIn("rule_source_anchor", src.replace(
            "rule_source_anchor is documentation", ""),
            "census must take executable identity from sc_registry.tsv, "
            "not from the inventory's rule_source_anchor annotation")

    def test_no_active_tool_extracts_identity_from_anchor(self):
        """No active tool may regex-extract a Foma identifier from
        rule_source_anchor to decide executable identity. Documentation
        emitters (generate_registry_views, adjudicate reading list) may
        mention the column but must not parse 'define <Ident>' out of it."""
        offenders = []
        for path in sorted(TOOLS.glob("*.py")):
            src = path.read_text(encoding="utf-8")
            if ("rule_source_anchor" in src
                    and "define\\s+([A-Za-z" in src):
                offenders.append(path.name)
        self.assertEqual(offenders, [],
                         "tools parsing executable identity out of "
                         f"rule_source_anchor: {offenders}")

    def test_census_scope_is_the_numbered_cascade(self):
        """Every census row has a numbered cascade position; SC002 (the
        pre-cascade prelude stage PGmcGmSimplification) is deliberately out
        of scope even though it has a registry fst_identifier."""
        rows = {r["sc_id"]: r for r in self.census.build_rows()}
        self.assertNotIn("SC002", rows)
        positions = [int(r["cascade_position"]) for r in rows.values()]
        self.assertTrue(positions and all(p >= 1 for p in positions))
        self.assertIn("SC088", rows)
        self.assertIn("SC089", rows)
        # 91 since SC104 EAFNasalizedLowRounding was inserted at position 29.
        self.assertEqual(rows["SC088"]["cascade_position"], "91")
        self.assertEqual(rows["SC089"]["cascade_position"], "92")
        # SC002's stage is executable but outside the numbered span.
        stage = {s.foma_identifier: s.cascade_position
                 for s in self.pipeline.named_stages()}
        self.assertIn("PGmcGmSimplification", stage)
        self.assertIsNone(stage["PGmcGmSimplification"])

    def test_registry_supplies_identity_for_all_census_rows(self):
        reg = {r["sc_id"]: (r.get("fst_identifier") or "").strip()
               for r in self.census.read_tsv(self.census.SC_REGISTRY)}
        for row in self.census.build_rows():
            self.assertEqual(row["foma_identifier"], reg[row["sc_id"]],
                             f"{row['sc_id']}: census identity must equal "
                             "the registry fst_identifier")


if __name__ == "__main__":
    unittest.main()
