"""Fail-closed historical replay and stable-ID baseline comparisons (no Foma)."""

import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


GERMANIC = Path(__file__).resolve().parents[1]
DRIVER = GERMANIC / (
    "docs/sound_changes/audits/sc015-r-adverb-lengthening-investigation/"
    "followup_experiment.py"
)
SPEC = importlib.util.spec_from_file_location("sc112_followup_replay", DRIVER)
replay = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(replay)


class HistoricalDeltaTests(unittest.TestCase):
    def setUp(self):
        self.rows = [{"id": "one", "concept": "first"}, {"id": "two", "concept": "second"}]
        self.baseline = {"two": ["b"], "one": ["a"]}

    def test_every_model_uses_the_same_historical_mapping(self):
        models = [
            {"two": ["b"], "one": ["changed"]},
            {"one": ["a"], "two": ["b"]},
            {"one": ["changed"], "two": ["b"]},
        ]
        comparisons = [
            replay.historical_deltas(self.rows, self.baseline, model) for model in models
        ]
        self.assertEqual([len(result) for result in comparisons], [1, 0, 1])
        self.assertEqual(comparisons[0], comparisons[2])
        self.assertEqual(comparisons[0][0]["baseline"], ["a"])

    def test_reordering_rows_or_output_keys_does_not_change_deltas(self):
        outputs = {"one": ["changed"], "two": ["b"]}
        self.assertEqual(
            replay.historical_deltas(self.rows, self.baseline, outputs),
            replay.historical_deltas(
                list(reversed(self.rows)), dict(reversed(list(self.baseline.items()))),
                dict(reversed(list(outputs.items()))),
            ),
        )

    def test_model_difference_is_not_a_historical_baseline_difference(self):
        model_a = {"one": ["different"], "two": ["b"]}
        model_b = {"one": ["a"], "two": ["b"]}
        self.assertNotEqual(model_a, model_b)
        self.assertEqual(replay.historical_deltas(self.rows, self.baseline, model_b), [])

    def test_genuine_baseline_difference_is_detected_even_when_models_agree(self):
        outputs = {"one": ["a"], "two": ["different"]}
        self.assertEqual(replay.historical_deltas(self.rows, self.baseline, outputs), [
            {"id": "two", "concept": "second", "baseline": ["b"], "variant": ["different"]},
        ])

    def test_missing_or_duplicate_id_fails_closed(self):
        for rows, baseline, outputs in (
            (self.rows * 2, self.baseline, self.baseline),
            (self.rows, {"one": ["a"]}, self.baseline),
            (self.rows, self.baseline, {"one": ["a"]}),
        ):
            with self.subTest(rows=rows, baseline=baseline), self.assertRaises(ValueError):
                replay.historical_deltas(rows, baseline, outputs)


class HistoricalReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = replay.load_receipt(DRIVER.with_name("followup-receipt.json.gz"))
        cls.files = replay.historical_bundle(replay.layout())

    def materialize(self, directory):
        for name, text in self.files.items():
            (directory / name).write_text(text, encoding="utf-8")

    def test_pinned_sources_context_and_parsed_orders_match_receipt(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.materialize(directory)
            original, candidates, order = replay.validate_inputs(directory, self.receipt)
        self.assertEqual(len(original), 387)
        self.assertEqual({row["id"] for row in candidates}, {"2333", "2334"})
        self.assertNotIn("XRAdverbLen", order)
        self.assertNotIn("PNWGmcMonosyllabicFinalRLengthening", order)
        you = next(row for row in original if row["id"] == "2326")
        self.assertEqual(you["fst_input"], "ᵘízwiz")

    def test_mismatched_source_corpus_context_helper_or_candidate_is_rejected(self):
        for name in (
            "germanic.txt", "germanic-aligned-final.tsv", "entry_context_metadata.tsv",
            "oe_input_context.py", "candidate_expansion.tsv", "oe_pipeline.py",
            "anglo_frisian_experiments.py",
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary)
                self.materialize(directory)
                with (directory / name).open("a", encoding="utf-8") as handle:
                    handle.write("\n")
                with self.assertRaisesRegex(ValueError, "pin changed|helper differs"):
                    replay.validate_inputs(directory, self.receipt)

    def test_mismatched_receipt_identity_is_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "receipt.gz"
            path.write_bytes(DRIVER.with_name("followup-receipt.json.gz").read_bytes() + b"\n")
            with self.assertRaisesRegex(ValueError, "receipt identity changed"):
                replay.load_receipt(path)

    def test_receipt_order_and_context_are_not_accepted_as_source_authority(self):
        for field in ("order", "rows"):
            receipt = copy.deepcopy(self.receipt)
            if field == "order":
                receipt["models"][0]["order"][1:3] = reversed(
                    receipt["models"][0]["order"][1:3]
                )
            else:
                receipt["rows"][0]["fst_input"] = "unapproved"
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary)
                self.materialize(directory)
                with self.assertRaisesRegex(ValueError, "order differs|identities or context"):
                    replay.validate_inputs(directory, receipt)

    def test_equivalence_checks_all_scientific_fields_not_only_final_outputs(self):
        historical = self.receipt["models"][0]
        for field in replay.SCIENTIFIC_FIELDS:
            model = copy.deepcopy(historical)
            model[field] = None
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, field):
                replay.verify_model(model, historical)
        model = copy.deepcopy(historical)
        model["compiler"] = {"compile_log": "different path or runtime diagnostic"}
        model["original_deltas"] = ["legacy derived comparison is not authoritative"]
        self.assertEqual(len(replay.verify_model(model, historical)), 64)

    def test_temporary_workspace_is_removed_on_success_and_error(self):
        from types import SimpleNamespace

        for fail in (False, True):
            visited = []

            def execute(directory, receipt):
                visited.append(directory)
                (directory / "temporary.bin").write_bytes(b"test")
                if fail:
                    raise RuntimeError("bounded test failure")
                return {"status": "equivalent"}

            with self.subTest(fail=fail), \
                    patch.object(replay, "layout", return_value=SimpleNamespace(is_container=True)), \
                    patch.object(replay.base, "protected_hashes", return_value={}), \
                    patch.object(replay, "replay", side_effect=execute):
                if fail:
                    with self.assertRaisesRegex(RuntimeError, "bounded test failure"):
                        replay.execute_bundle(self.files, self.receipt)
                else:
                    report = replay.execute_bundle(self.files, self.receipt)
                    self.assertTrue(report["temporary_workspace_cleaned"])
            self.assertEqual(len(visited), 1)
            self.assertFalse(visited[0].exists())


if __name__ == "__main__":
    unittest.main()
