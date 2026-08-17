"""Cross-artifact consistency invariants for the SC001-SC020 chronology audit.

Branch sc001-sc020-chronology-audit. These tests compare the four artifacts that
describe the same SC001-SC020 rules and fail if their shared fields drift apart:

  * docs/sound_changes/audits/sc001-sc020-chronology-audit.tsv  (audit matrix)
  * docs/sound_changes/sound_change_inventory.tsv               (per-rule inventory)
  * docs/sound_changes/sound_change_historical_staging_map.tsv  (reader registry)
  * docs/sound_changes/cascade_baseline/cascade_order_manifest.tsv (executable order)

Fields that intentionally use different controlled vocabularies are compared
through explicit mappings (documented below), NOT by hard-coding four copies of
the same answer.

Run: cd Germanic/tests && python3 -m unittest test_sc_chronology_cross_artifact
"""

import csv
import io
import re
import unittest
from pathlib import Path

SC_DIR = Path(__file__).resolve().parents[1] / "docs" / "sound_changes"
AUDIT = SC_DIR / "audits" / "sc001-sc020-chronology-audit.tsv"
INVENTORY = SC_DIR / "sound_change_inventory.tsv"
STAGING = SC_DIR / "sound_change_historical_staging_map.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"

SC_IDS = [f"SC{i:03d}" for i in range(1, 21)]

# Historical stage: the audit matrix and the inventory use long-form display
# labels; the staging map uses short internal codes. Map them onto one canonical
# long form. Only map values that actually occur for SC001-SC020.
STAGE_TO_CANONICAL = {
    # audit proposed_historical_stage / staging hist_stage short codes
    "eaf": "Early Anglo-Frisian",
    "wgmc": "West Germanic",
    "nsgmc": "Northern West Germanic",
    "pnwgmc": "Northwest Germanic",
    "pwgmc": "Proto-West Germanic",
    "pgmc": "Proto-Germanic",
    "oe_ws": "Old English",
    "Technical": "Technical",
    "Technical (support stage)": "Technical",
    # inventory / staging long forms (identity)
    "Early Anglo-Frisian": "Early Anglo-Frisian",
    "West Germanic": "West Germanic",
    "Northern West Germanic": "Northern West Germanic",
    "Northwest Germanic": "Northwest Germanic",
    "Proto-West Germanic": "Proto-West Germanic",
    "Proto-Germanic": "Proto-Germanic",
    "Old English": "Old English",
}
# SC020's audit stage carries a parenthetical refinement; normalize its head.
STAGE_HEAD_ONLY = {"SC020"}  # "wgmc (early rule: PWGmc)" -> head "wgmc"

# Historical scope: audit and staging both use short codes already; inventory
# does not carry a separate scope column (folded into pipeline_stage).
SCOPE_FIELDS_AGREE = ("audit", "staging")  # only these two have a scope column


def _read(path, key):
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return {r[key]: r for r in csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")}


def _canon_stage(sc, raw):
    raw = (raw or "").strip()
    if sc in STAGE_HEAD_ONLY:
        raw = raw.split("(")[0].strip()
    return STAGE_TO_CANONICAL.get(raw, raw)


class CrossArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = _read(AUDIT, "sc_id")
        cls.inv = _read(INVENTORY, "change_id")
        cls.staging = _read(STAGING, "sc_id")
        # order manifest: foma_identifier -> position
        mlines = [ln for ln in MANIFEST.read_text(encoding="utf-8").splitlines()
                  if not ln.startswith("#")]
        cls.manifest = {r["foma_identifier"]: int(r["position"])
                        for r in csv.DictReader(io.StringIO("\n".join(mlines)), delimiter="\t")}

    def test_all_sc001_sc020_present_everywhere(self):
        for sc in SC_IDS:
            self.assertIn(sc, self.audit, f"{sc} missing from audit matrix")
            self.assertIn(sc, self.inv, f"{sc} missing from inventory")
            if sc not in ("SC001", "SC002"):  # support/early stages absent from staging map
                self.assertIn(sc, self.staging, f"{sc} missing from staging map")

    def test_foma_identifier_agrees_audit_vs_staging(self):
        """The canonical Foma identifier must match between the audit matrix and
        the staging map (this catches the SC004 PWGmc->EAF alias error)."""
        for sc in SC_IDS:
            if sc not in self.staging:
                continue  # SC001/SC002 are support stages, not in the reader registry
            a = self.audit[sc]["foma_identifier"].strip()
            s = self.staging[sc]["fst_identifier"].strip()
            self.assertEqual(a, s,
                             f"{sc}: audit foma id {a!r} != staging fst id {s!r}")

    def test_foma_identifier_is_principal_not_legacy_alias(self):
        """SC004's principal rule is EAFAiMonophthongization; the legacy
        PWGmcAiMonophthongization alias must not be recorded as the principal id."""
        self.assertEqual(self.audit["SC004"]["foma_identifier"].strip(),
                         "EAFAiMonophthongization")
        self.assertEqual(self.staging["SC004"]["fst_identifier"].strip(),
                         "EAFAiMonophthongization")
        # Position 28 since the SC016/SC017 repair moved SC016 out of the
        # early cascade (was 29 after the 2026 SC098 insertion; 28 before it).
        self.assertEqual(self.manifest.get("EAFAiMonophthongization"), 28)

    def test_historical_stage_agrees_audit_inventory_staging(self):
        """Historical stage (canonical long form) must agree across audit,
        inventory, and staging map for every SC001-SC020 that all three cover."""
        for sc in SC_IDS:
            audit_stage = _canon_stage(sc, self.audit[sc]["proposed_historical_stage"])
            inv_stage = _canon_stage(sc, self.inv[sc]["historical_stage"])
            self.assertEqual(audit_stage, inv_stage,
                             f"{sc}: audit stage {audit_stage!r} != inventory {inv_stage!r}")
            if sc in self.staging:
                st_stage = _canon_stage(sc, self.staging[sc]["hist_stage"])
                # EAF is CAPR's post-PWGmc corridor; the audit/inventory record the
                # finer reader-facing stage (e.g. Northern West Germanic / West
                # Germanic). Both map to the same corridor. Only require agreement
                # when staging uses a specific (non-EAF) code.
                if self.staging[sc]["hist_stage"].strip() != "eaf":
                    self.assertEqual(audit_stage, st_stage,
                                     f"{sc}: audit stage {audit_stage!r} != staging {st_stage!r}")

    def test_historical_scope_agrees_audit_vs_staging(self):
        """Historical scope must agree between audit matrix and staging map
        (the two artifacts that carry a scope column)."""
        for sc in SC_IDS:
            if sc not in self.staging:
                continue
            a = self.audit[sc]["proposed_historical_scope"].strip()
            s = self.staging[sc]["hist_scope"].strip()
            self.assertEqual(a, s,
                             f"{sc}: audit scope {a!r} != staging scope {s!r}")

    def test_cascade_position_matches_order_manifest(self):
        """The audit matrix cascade_position must equal the executable position
        in the order manifest for rules that execute inside EnglishProtoToOE.
        (Support/early rules not in the manifest are skipped.)"""
        for sc in SC_IDS:
            foma = self.audit[sc]["foma_identifier"].strip()
            if foma not in self.manifest:
                continue  # support / pre-pipeline rule
            manifest_pos = self.manifest[foma]
            audit_pos = self.audit[sc]["cascade_position"].strip()
            self.assertTrue(audit_pos.isdigit(),
                            f"{sc}: audit cascade_position {audit_pos!r} not numeric but rule is in manifest")
            self.assertEqual(int(audit_pos), manifest_pos,
                             f"{sc}: audit cascade_position {audit_pos} != manifest {manifest_pos}")

    def test_reader_chapter_agrees_audit_vs_staging(self):
        """Proposed reader chapter in the audit matrix must match the staging
        map's chapter (catches SC012 Ch2 -> Ch3 drift)."""
        for sc in SC_IDS:
            if sc not in self.staging:
                continue
            a = self.audit[sc]["proposed_reader_chapter"].strip()
            s = self.staging[sc]["v1_chapter"].strip()
            self.assertEqual(a, s,
                             f"{sc}: audit proposed chapter {a!r} != staging chapter {s!r}")

    def test_sc012_is_northern_wgmc_scope(self):
        """SC012: northern WGmc scope, display stage Northern West Germanic.
        Reader chapters are now contiguous executable-position intervals, so
        SC012 (cascade position 10) sits in chapter 1; scope/stage labels are
        independent of chapter assignment until the rename pass."""
        self.assertEqual(self.audit["SC012"]["proposed_historical_stage"].split("(")[0].strip(), "nsgmc")
        self.assertEqual(self.audit["SC012"]["proposed_historical_scope"].strip(), "north_wgmc")
        self.assertEqual(self.inv["SC012"]["historical_stage"], "Northern West Germanic")
        self.assertEqual(self.staging["SC012"]["hist_scope"], "north_wgmc")
        self.assertEqual(self.staging["SC012"]["v1_chapter"], "1")


class BookOrderMatchesManifestTests(unittest.TestCase):
    """Hard-wired invariant: for part one of the book, the reader-facing
    (sub)chapter presentation order NECESSARILY matches the executable cascade
    order recorded in cascade_order_manifest.tsv.

    Chapter assignment is by contiguous manifest-position intervals; subchapter
    files are ordered by the minimum manifest position of the SCs they contain
    (a file may bundle several adjacent SCs). FST identifier names are historic
    residue and carry no ordering authority."""

    BUILD_SCRIPT = (SC_DIR / "reader_facing"
                    / "build_reader_facing_local_section_20_docker.sh")

    @classmethod
    def setUpClass(cls):
        slines = [ln for ln in STAGING.read_text(encoding="utf-8").splitlines()
                  if not ln.startswith("#")]
        cls.staging_rows = list(csv.DictReader(io.StringIO("\n".join(slines)),
                                               delimiter="\t"))
        mlines = [ln for ln in MANIFEST.read_text(encoding="utf-8").splitlines()
                  if not ln.startswith("#")]
        cls.manifest = {r["foma_identifier"]: int(r["position"])
                        for r in csv.DictReader(io.StringIO("\n".join(mlines)),
                                                delimiter="\t")}
        # file -> (chapter, min reader position, min manifest position)
        files = {}
        for r in cls.staging_rows:
            fst = r["fst_identifier"].strip()
            cls_pos = cls.manifest.get(fst)
            key = r["source_reader_facing_file"].strip()
            ch = int(r["v1_chapter"])
            rp = int(r["v1_reader_position"])
            ent = files.setdefault(key, {"chapter": ch, "reader": rp,
                                         "manifest": cls_pos,
                                         "positions": []})
            ent["chapter"] = min(ent["chapter"], ch)
            ent["reader"] = min(ent["reader"], rp)
            ent["manifest"] = min(ent["manifest"], cls_pos)
            ent["positions"].append(cls_pos)
        cls.files = files

    def test_every_staged_rule_has_a_manifest_position(self):
        for r in self.staging_rows:
            fst = r["fst_identifier"].strip()
            self.assertIn(fst, self.manifest,
                          f"{r['sc_id']}: {fst} missing from cascade manifest")

    def test_staging_cascade_position_matches_manifest(self):
        for r in self.staging_rows:
            fst = r["fst_identifier"].strip()
            self.assertEqual(int(r["cascade_position"]), self.manifest[fst],
                             f"{r['sc_id']}: stale cascade_position")

    def test_subchapter_order_is_manifest_order(self):
        """Files sorted by (chapter, reader position) must be strictly
        increasing in minimum manifest position: book order == cascade order."""
        ordered = sorted(self.files.values(),
                         key=lambda e: (e["chapter"], e["reader"]))
        mins = [e["manifest"] for e in ordered]
        self.assertEqual(mins, sorted(mins),
                         "subchapter file order does not follow the cascade "
                         f"manifest: {mins}")
        self.assertEqual(len(mins), len(set(mins)),
                         "two subchapter files claim the same minimum "
                         "manifest position")

    def test_chapters_are_contiguous_manifest_intervals(self):
        """Every chapter must own a contiguous block of manifest positions:
        the maximum position in chapter N is below the minimum in chapter N+1."""
        by_ch = {}
        for e in self.files.values():
            by_ch.setdefault(e["chapter"], []).extend(e["positions"])
        chapters = sorted(by_ch)
        self.assertEqual(chapters, list(range(1, len(chapters) + 1)),
                         "chapter numbers are not 1..N")
        for a, b in zip(chapters, chapters[1:]):
            self.assertLess(max(by_ch[a]), min(by_ch[b]),
                            f"chapters {a} and {b} overlap in manifest positions")

    def test_build_script_file_order_matches_staging_map(self):
        """The section-20 build script's chapter_files list must equal the
        staging map's file order, so the rendered book cannot drift from the
        cascade."""
        text = self.BUILD_SCRIPT.read_text(encoding="utf-8")
        m = re.search(r"chapter_files = \[(.*?)\n\]", text, re.S)
        self.assertIsNotNone(m, "chapter_files list not found in build script")
        script_files = re.findall(r'"([^"]+\.md)"', m.group(1))
        staging_files = [k for k, _ in sorted(
            self.files.items(), key=lambda kv: (kv[1]["chapter"], kv[1]["reader"]))]
        self.assertEqual(script_files, staging_files)


if __name__ == "__main__":
    unittest.main()
