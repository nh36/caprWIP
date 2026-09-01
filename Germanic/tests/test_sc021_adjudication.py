"""Regression coverage for the SC021 adjudication and its successor rules."""

from __future__ import annotations

import csv
import importlib.util
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
MANIFEST = (GERMANIC / "docs" / "sound_changes" / "cascade_baseline"
            / "cascade_order_manifest.tsv")
TRACE_TOOL = GERMANIC / "tools" / "oe_full_trace_report.py"
BIN_DIR = REPO_ROOT / "backend"


def load_trace_tool():
    spec = importlib.util.spec_from_file_location("oe_full_trace_report", TRACE_TOOL)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class SC021AdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)#.*$", "", cls.text)
        with MANIFEST.open(encoding="utf-8") as handle:
            cls.positions = {
                row["foma_identifier"]: int(row["position"])
                for row in csv.DictReader(handle, delimiter="\t")
            }
        cls.trace = load_trace_tool()

    def stage(self, name, form):
        return self.trace.run_stage(
            BIN_DIR, f"old_english_sandbox_after_{name}.bin", form
        )

    def test_sc021_is_retired_not_silently_repurposed(self):
        self.assertNotRegex(
            self.uncommented, r"define\s+PNWGmcUnstressedORaising\b"
        )
        self.assertNotIn("PNWGmcUnstressedORaising", self.positions)

    def test_successors_follow_shortening_and_precede_sc040(self):
        self.assertLess(
            self.positions["OELateOShortening"],
            self.positions["OEMedUnstressedORaising"],
        )
        self.assertLess(
            self.positions["OEMedUnstressedORaising"],
            self.positions["OEFinalUnstressedOLowering"],
        )
        self.assertLess(
            self.positions["OEFinalUnstressedOLowering"],
            self.positions["OEMedUnstressedULowering"],
        )

    def test_wundude_has_the_source_backed_medial_path(self):
        form = "wúndōdē"
        self.assertEqual(
            self.stage("oe_late_o_shortening", form), ["*w*ú*n*d*o*d*ē"]
        )
        self.assertEqual(
            self.stage("oe_med_unstressed_o_raising", form), ["*w*ú*n*d*u*d*ē"]
        )
        self.assertEqual(
            self.stage("oe_final_unstressed_o_lowering", form), ["*w*ú*n*d*u*d*ē"]
        )
        self.assertEqual(
            self.stage("old_english_surface", form), ["wundude"]
        )

    def test_final_shortened_o_does_not_use_the_medial_rule(self):
        form = "mḗnōθz"
        self.assertEqual(
            self.stage("oe_late_o_shortening", form), ["*m*ō*n*o*θ"]
        )
        self.assertEqual(
            self.stage("oe_med_unstressed_o_raising", form), ["*m*ō*n*o*θ"]
        )
        self.assertEqual(
            self.stage("oe_final_unstressed_o_lowering", form), ["*m*ō*n*a*θ"]
        )
        self.assertEqual(
            self.stage("old_english_surface", form), ["mōnaþ"]
        )

    def test_late_sc040_remains_distinct_from_the_new_chain(self):
        form = "xébun"
        self.assertEqual(
            self.stage("oe_final_unstressed_o_lowering", form), ["*ç*éo*β*u*n"]
        )
        self.assertEqual(
            self.stage("oe_med_unstressed_u_lowering", form), ["*ç*éo*β*o*n"]
        )
        self.assertEqual(
            self.stage("old_english_surface", form), ["heofon"]
        )


if __name__ == "__main__":
    unittest.main()
