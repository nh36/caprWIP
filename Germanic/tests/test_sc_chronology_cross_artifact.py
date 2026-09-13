"""Source-level stage-vocabulary discipline plus book-order projections.

The former cross-artifact agreement tests compared four artifacts (live audit
matrix, inventory, staging map, order manifest) and failed when hand-synced
mirrors drifted. That architecture is retired: the SC001-SC020 audit matrix is
now ARCHIVE/FROZEN, and every current view is a generated projection of
registry/sc_registry.tsv + oe_pipeline whose freshness is enforced by
test_registry_consolidation.GeneratedViewTests. What remains here are
source-level invariants on the registry itself (two human vocabularies that
must stay semantically consistent) and the book-order-matches-cascade
invariant.

Run: cd Germanic/tests && python3 -m unittest test_sc_chronology_cross_artifact
"""

import csv
import io
import re
import unittest
from pathlib import Path

SC_DIR = Path(__file__).resolve().parents[1] / "docs" / "sound_changes"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
STAGING = SC_DIR / "sound_change_historical_staging_map.tsv"
MANIFEST = SC_DIR / "cascade_baseline" / "cascade_order_manifest.tsv"

# SC021 is retained as a stable retired identifier in its adjudication dossier
# and aliases, but has no live inventory/staging-map rule after retirement.
SC_IDS = [f"SC{i:03d}" for i in range(1, 21) if i != 21]

# The registry carries TWO human stage vocabularies: hist_stage (short internal
# code) and historical_stage_label (reader-facing display label). Both are
# human judgements in ONE source file; this map pins which display labels each
# code may legitimately carry (corridor codes admit finer reader-facing
# stages). A pairing outside this map is a source-level contradiction.
ALLOWED_STAGE_LABELS = {
    "pgmc": {"Proto-Germanic"},
    "pnwgmc": {"Northwest Germanic"},
    "nwgmc": {"Northwest Germanic"},
    "pwgmc": {"Proto-West Germanic", "Northern West Germanic"},
    # EAF is CAPR's post-PWGmc executable corridor; the reader-facing label may
    # record the finer historical stage established by adjudication.
    "eaf": {"Early Anglo-Frisian", "Anglo-Frisian", "North Sea Germanic",
            "Northern West Germanic", "West Germanic", "Old English"},
    "preoe": {"Old English"},
    "oe": {"Old English"},
    "oe_ws": {"Old English"},
    "ws_oe": {"Old English"},
    "": {"", "Old English", "Orthography & surface", "Proto-Germanic",
         "Technical"},
}


def _read(path, key):
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return {r[key]: r for r in csv.DictReader(io.StringIO("\n".join(lines)), delimiter="\t")}


class RegistryStageVocabularyTests(unittest.TestCase):
    """Semantic discipline between the registry's two human stage columns."""

    @classmethod
    def setUpClass(cls):
        cls.reg = _read(REGISTRY, "sc_id")
        cls.staging = _read(STAGING, "sc_id")

    def test_all_sc001_sc020_present_in_registry(self):
        for sc in SC_IDS:
            self.assertIn(sc, self.reg, f"{sc} missing from sc_registry.tsv")

    def test_stage_code_and_display_label_are_consistent(self):
        for sc, r in self.reg.items():
            code = r["hist_stage"].strip()
            label = r["historical_stage_label"].strip()
            self.assertIn(code, ALLOWED_STAGE_LABELS,
                          f"{sc}: unknown hist_stage code {code!r}")
            self.assertIn(label, ALLOWED_STAGE_LABELS[code],
                          f"{sc}: display label {label!r} contradicts "
                          f"hist_stage {code!r}")

    def test_sc012_is_northern_wgmc_scope(self):
        """SC012: northern WGmc scope, display stage Northern West Germanic
        (R/T pp.170-171; Campbell §414: lþ>ld clearest in northern WGmc).
        Chapter assignment is a separate editorial fact and is tested against
        the cascade by the book-order tests below."""
        self.assertEqual(self.reg["SC012"]["hist_scope"], "north_wgmc")
        self.assertEqual(self.reg["SC012"]["historical_stage_label"],
                         "Northern West Germanic")
        self.assertEqual(self.staging["SC012"]["hist_scope"], "north_wgmc")

    def test_sc020_stage_is_proto_west_germanic(self):
        """Dossier B (sc020-three-rule-adjudication.md): PWGmc stage
        (R/T 2014 pp.44-45, 212)."""
        self.assertEqual(self.reg["SC020"]["historical_stage_label"],
                         "Proto-West Germanic")

    def test_sc004_principal_identifier_is_not_the_legacy_alias(self):
        """SC004's principal rule is EAFAiMonophthongization; the legacy
        PWGmcAiMonophthongization alias must never return as principal id."""
        self.assertEqual(self.reg["SC004"]["fst_identifier"],
                         "EAFAiMonophthongization")
        self.assertEqual(self.staging["SC004"]["fst_identifier"],
                         "EAFAiMonophthongization")


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
