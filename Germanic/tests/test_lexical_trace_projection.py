import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "Germanic/tools"))
import oe_derivation_class_trace_report as report
import oe_full_trace_report as full_report
import sound_change_order_sensitivity as order


class LexicalProjectionTests(unittest.TestCase):
    def setUp(self):
        self.row = {"concept": "gift", "proto": "*gíftiz", "counterpart": "ġift",
                    "derivation_class": "regular", "note": "Source-backed input."}
        self.text = ("=== MATCHES ===\n--- gift ---\nPROTO: *gíftiz\n"
                     "EXPECTED: ġift\nOUTPUTS: ġift\n\n"
                     "OEWsPalatalDiphthongization [no-change]: *ʤ*í*f*t*i\n\n"
                     "=== STAGE FIRING SUMMARY ===\nOEWsPalatalDiphthongization: 7\n")

    def project(self, text, rows=None):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trace.txt"
            path.write_text(text)
            with patch.object(report, "trace_provenance_problems", return_value=[]), \
                    patch.object(report, "apply_down", side_effect=AssertionError("must reuse evidence")), \
                    patch.object(report, "trace_lexeme", side_effect=AssertionError("must reuse evidence")):
                return report.project_full_trace(rows or [self.row], path)

    def test_regroups_exact_fresh_evidence_without_lookup(self):
        result = self.project(self.text)
        self.assertIn("=== DERIVATION_CLASS: regular (1) ===", result)
        self.assertIn("NOTE: Source-backed input.", result)
        self.assertIn("OEWsPalatalDiphthongization [no-change]: *ʤ*í*f*t*i", result)
        self.assertNotIn("STAGE FIRING SUMMARY", result)

    def test_stale_duplicate_and_wrong_identity_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "trace.txt"
            path.write_text(self.text)
            with patch.object(report, "trace_provenance_problems", return_value=["stale"]):
                with self.assertRaisesRegex(ValueError, "stale"):
                    report.project_full_trace([self.row], path)
        for text in (self.text + self.text, self.text.replace("*gíftiz", "*géftiz")):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.project(text)

    def test_duplicate_corpus_rows_cannot_hide_omitted_evidence(self):
        other = self.text.replace("--- gift ---", "--- other ---")
        with self.assertRaisesRegex(ValueError, "duplicate corpus identity"):
            self.project(self.text + other, [self.row, self.row])

    def test_selected_context_header_is_checked_without_becoming_a_segment(self):
        text = self.text.replace(
            "EXPECTED:", "INPUT_CONTEXT: SC098; stress=stressed; finality=final\nEXPECTED:"
        )
        row = {**self.row, "word_stress": "stressed", "phonological_finality": "final"}
        result = self.project(text, [row])
        self.assertIn("PROTO: *gíftiz", result)
        self.assertNotIn("INPUT_CONTEXT:", result)
        with self.assertRaisesRegex(ValueError, "context mismatch"):
            self.project(text.replace("stress=stressed", "stress=unstressed"), [row])

    def test_cached_outputs_preserve_scalar_rejection_and_no_change_behavior(self):
        stages = [("First", "first.bin"), ("Rejected", "reject.bin"), ("Same", "same.bin")]
        with patch.object(full_report, "STAGES", stages), \
                patch.object(full_report, "run_stage", side_effect=[["*a"], ["+?"], ["*a"]]):
            scalar = full_report.trace_lexeme("a", Path("."))
        with patch.object(full_report, "STAGES", stages), \
                patch.object(full_report, "run_stage", side_effect=AssertionError("must use batch")):
            cached = full_report.trace_lexeme(
                "a", Path("."), {"first.bin": ["*a"], "reject.bin": [], "same.bin": ["*a"]},
            )
        self.assertEqual(cached, scalar)

    def test_annotation_only_steps_are_not_published_as_vowel_changes(self):
        stages = [("First", "first.bin"), ("Context", "context.bin"), ("Fronting", "front.bin")]
        with patch.object(full_report, "STAGES", stages):
            traced = full_report.trace_lexeme("ga", Path("."), {
                "first.bin": ["*g*a"], "context.bin": ["*ᶠ*g*a"],
                "front.bin": ["*ᶠ*g*æ"],
            })
        self.assertEqual(traced, [
            ("First", ["*g*a"]),
            ("Context [no-change]", ["*ᶠ*g*a"]),
            ("Fronting", ["*ᶠ*g*æ"]),
        ])

    def test_parallel_report_keeps_stage_order_and_bounds_readers(self):
        stages = [
            ("First", "old_english_sandbox_after_eaf_brightening.bin"),
            ("Second", "old_english_sandbox_after_oe_a_restoration.bin"),
            ("Rejected", "reject.bin"), ("Last", "last.bin"),
        ]
        barrier = threading.Barrier(4)
        completed = []
        lock = threading.Lock()
        def evaluate(path, forms):
            if path.name != "final.bin":
                barrier.wait(timeout=5)
                time.sleep(0.03 if path.name == stages[0][1] else 0.001)
            with lock:
                completed.append(path.name)
            return [[] if path.name == "reject.bin" else
                    ["a"] if path.name == "final.bin" else ["*a"]
                    for form in forms]
        row = dict(concept="example", proto="*a", proto_norm="a",
                   fst_input="a", counterpart="a")
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(full_report, "STAGES", stages), \
                patch.object(order, "batch_apply_down", side_effect=evaluate) as batch:
            path = Path(directory) / "report.txt"
            full_report.write_report([row], Path("final.bin"), Path("."),
                                     path, trace_all=True)
            text = path.read_text()
        self.assertEqual(batch.call_count, 5)
        self.assertEqual(set(completed), {name for _, name in stages} | {"final.bin"})
        self.assertLess(completed.index("reject.bin"), completed.index(stages[0][1]))
        self.assertLess(text.index("First:"), text.index("Second [no-change]:"))
        self.assertLess(text.index("Second [no-change]:"),
                        text.index("Rejected [no-change]:"))
        self.assertIn("Rejected: rejected", text)

    def test_failed_parallel_lookup_does_not_replace_report(self):
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(order, "batch_apply_down", side_effect=RuntimeError("lookup failed")):
            path = Path(directory) / "report.txt"
            path.write_text("previous evidence")
            with self.assertRaisesRegex(RuntimeError, "lookup failed"):
                full_report.write_report([], Path("final.bin"), Path("."), path)
            self.assertEqual(path.read_text(), "previous evidence")


if __name__ == "__main__":
    unittest.main()
