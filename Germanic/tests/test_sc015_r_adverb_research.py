"""Text-only guards for the isolated SC015 research driver; never invoke Foma."""
import importlib.util
import csv
import json
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
DRIVER = ROOT / "docs/sound_changes/audits/sc015-r-adverb-lengthening-investigation/experiment.py"
SPEC = importlib.util.spec_from_file_location("sc015_r_research", DRIVER)
research = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(research)
BUILDER_SPEC = importlib.util.spec_from_file_location("sc015_r_recipe_builder", DRIVER.with_name("build_recipes.py"))
builder = importlib.util.module_from_spec(BUILDER_SPEC)
BUILDER_SPEC.loader.exec_module(builder)
SUMMARY_SPEC = importlib.util.spec_from_file_location("sc015_r_summary", DRIVER.with_name("summarize.py"))
summary = importlib.util.module_from_spec(SUMMARY_SPEC)
SUMMARY_SPEC.loader.exec_module(summary)


def specification():
    return {
        "schema_version": 1, "base_commit": "c" * 40, "witness_sha256": "d" * 64,
        "pins": {key: "a" * 64 for key in research.pin_paths(research.layout())},
        "recipes": [{
            "id": "no-op", "architecture": "A", "representation": "existing",
            "evidence": "test fixture, not a historical recipe", "assumptions": "none",
            "definitions": {}, "source_replacements": [], "symbols": [], "edits": [],
        }],
        "probes": [],
    }


class ResearchDriverTests(unittest.TestCase):
    def setUp(self):
        self.spec = specification()
        self.source = ROOT / "fsts/germanic.txt"

    def test_validation_never_runs_subprocess(self):
        with patch.object(research.subprocess, "run", side_effect=AssertionError("Foma prohibited")):
            order = research.validate(self.spec, self.source)
        self.assertEqual(len(order), 107)
        self.assertEqual(order[0], "EnglishProtoInput")
        self.assertEqual(order[-1], "OldEnglishSurface")

    def test_before_sc024_anchor_is_inside_expanded_bundle(self):
        recipe = self.spec["recipes"][0]
        recipe["definitions"] = {"XRNoop": "[?*]"}
        recipe["edits"] = [{"action": "insert", "rule": "XRNoop",
                            "target": "PNWGmcLongELowering", "side": "before"}]
        original = research.validate(self.spec, self.source)
        changed = research.edited_order(original, recipe)
        index = changed.index("PNWGmcLongELowering")
        self.assertEqual(changed[index - 1], "XRNoop")
        self.assertLess(index, changed.index("PNWGmcILowering"))

    def test_move_and_split_operations_have_no_duplicate_cascade(self):
        order = ["Input", "Early", "Lower", "Late", "Surface"]
        recipe = {"edits": [{"action": "move", "rule": "Lower", "target": "Early", "side": "before"}]}
        self.assertEqual(research.edited_order(order, recipe), ["Input", "Lower", "Early", "Late", "Surface"])
        recipe = {"edits": [{"action": "replace", "target": "Lower", "rule": "ZSt"},
                            {"action": "insert", "target": "Early", "rule": "R", "side": "before"}]}
        self.assertEqual(research.edited_order(order, recipe), ["Input", "R", "Early", "ZSt", "Late", "Surface"])

    def test_missing_and_duplicate_anchors_fail(self):
        recipe = {"edits": [{"action": "remove", "target": "R"}]}
        for order in (["Q"], ["R", "R"]):
            with self.assertRaisesRegex(ValueError, "exactly one"):
                research.edited_order(order, recipe)

    def test_source_replacement_exactly_once(self):
        recipe = {"source_replacements": [{"old": "ABC", "new": "DEF"}]}
        self.assertEqual(research.transformed_source("ABC", recipe), "DEF")
        for text in ("", "ABCABC"):
            with self.assertRaisesRegex(ValueError, "exactly once"):
                research.transformed_source(text, recipe)

    def test_bundle_replacement_cannot_silently_bypass_wrapper(self):
        self.spec["recipes"][0]["source_replacements"] = [{
            "old": ".o. PNWGmcLongELowering", "new": ".o. PNWGmcILowering",
            "reason": "test rejected composition edit", "consumers": ["EarlyEnglishLineChanges"],
        }]
        with self.assertRaisesRegex(ValueError, "composition changes"):
            research.validate(self.spec, self.source)

    def test_new_combining_long_vowel_is_rejected(self):
        recipe = self.spec["recipes"][0]
        recipe["definitions"] = {"XRLong": "[{*ẹ} -> {*ẹ̄}]"}
        recipe["symbols"] = [{"symbol": "ẹ", "role": "short", "consumers": ["XRLong"]}]
        with self.assertRaisesRegex(ValueError, "combining"):
            research.validate(self.spec, self.source)
        recipe["symbols"].append({"symbol": "ẹ̄", "role": "long", "consumers": ["XRLong"]})
        with self.assertRaisesRegex(ValueError, "single|one unique"):
            research.validate(self.spec, self.source)

    def test_single_codepoint_symbols_are_audited(self):
        recipe = self.spec["recipes"][0]
        recipe["definitions"] = {"XRLong": "[{*ẹ} -> {*ệ}]"}
        recipe["symbols"] = [
            {"symbol": s, "role": role, "consumers": ["XRLong"]}
            for s, role in (("ẹ", "short close-mid"), ("ệ", "long close-mid experimental label"))
        ]
        research.validate(self.spec, self.source)
        recipe["symbols"].pop()
        with self.assertRaisesRegex(ValueError, "declared"):
            research.validate(self.spec, self.source)

    def test_commands_and_nonlocal_source_io_are_rejected(self):
        for text in ("save stack ../old_english.bin", "source other.foma", "system echo unsafe"):
            with self.assertRaises(ValueError):
                research.safe_source(text)
        self.spec["recipes"][0]["definitions"] = {"XRBad": "[?*]; quit"}
        with self.assertRaisesRegex(ValueError, "not commands"):
            research.validate(self.spec, self.source)

    def test_contextual_and_stage_entry_probes_are_explicit(self):
        probe = {"id": "synthetic", "fst_input": "*x*í*r", "kind": "synthetic",
                 "historical_stage": "test", "reconstruction_level": "B",
                 "evidence": "test only", "entry_stage": "PNWGmcLongELowering", "side": "before"}
        self.spec["probes"] = [probe]
        original = research.validate(self.spec, self.source)
        self.assertEqual(research.entry_index(probe, original), original.index("PNWGmcLongELowering"))
        probe["context"] = {"word_stress": "stressed", "phonological_finality": "final"}
        with self.assertRaisesRegex(ValueError, "encode context explicitly"):
            research.validate(self.spec, self.source)

    def test_rejections_ambiguity_and_all_firings_are_preserved(self):
        with patch.object(research, "apply", side_effect=[
            [["*é"], ["*í"]], [["ē", "ǣ"], []],
        ]):
            history, census, finals = research.traces(
                [Path("a.bin"), Path("b.bin")], ["Lower", "Length"],
                ["*í", "*í"], ["one", "two"])
        self.assertEqual([f["id"] for f in census[0]["firings"]], ["one"])
        self.assertEqual(history["one"][-1]["status"], "ambiguous")
        self.assertEqual(history["two"][-1]["status"], "rejected")
        self.assertEqual(finals, [["ē", "ǣ"], []])

    def test_execution_on_host_fails_before_foma(self):
        with patch.object(research.subprocess, "run", side_effect=AssertionError("Foma prohibited")), \
                patch.object(research, "layout", return_value=SimpleNamespace(is_container=False)):
            with self.assertRaisesRegex(ValueError, "container"):
                research.execute(self.spec, Path("none"), Path("none"), Path("none"))

    def test_frozen_selected387_comparison_is_fail_closed(self):
        runtime = research.layout()
        rows = research.assay.corpus_rows(runtime.corpus_tsv)
        with (runtime.docs_dir / "sound_changes/cascade_baseline/cascade_baseline_outputs.tsv").open(
                encoding="utf-8", newline="") as handle:
            frozen = list(csv.DictReader(handle, delimiter="\t"))
        outputs = {row["row_id"]: [row["outputs"]] for row in frozen}
        research.verify_baseline(rows, outputs, runtime)
        outputs[rows[0]["id"]] = []
        with self.assertRaisesRegex(ValueError, "differs from frozen"):
            research.verify_baseline(rows, outputs, runtime)

    def test_lookup_failures_are_not_replaced_by_identity_outputs(self):
        with patch.object(research.assay, "batch_apply_down", side_effect=TimeoutError("bounded lookup")):
            with self.assertRaisesRegex(TimeoutError, "bounded lookup"):
                research.apply(Path("not-executed.bin"), ["xír"])


class RecipeBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = ROOT / "fsts/germanic.txt"
        cls.before = research.digest(cls.source)
        with patch.object(research.subprocess, "run", side_effect=AssertionError("Foma prohibited")):
            cls.plan = builder.build_spec("0" * 64, [])
        cls.recipes = {recipe["id"]: recipe for recipe in cls.plan["recipes"]}
        cls.order = research.source_order(cls.source)

    def test_builds_twenty_one_validated_hypotheses_without_witness_inputs(self):
        self.assertEqual(len(self.recipes), 21)
        self.assertEqual(self.plan["probes"], [])
        self.assertEqual({recipe["architecture"] for recipe in self.recipes.values()}, {"A", "B", "C", "D"})
        self.assertEqual(research.digest(self.source), self.before)

    def test_native_placements_and_reverse_control(self):
        before = research.edited_order(self.order, self.recipes["a-before-sc024-existing"])
        self.assertLess(before.index("XRLen"), before.index(builder.EARLY))
        after = research.edited_order(self.order, self.recipes["a-after-sc015-existing"])
        self.assertEqual(after.index("XRLen"), after.index(builder.LOWER) + 1)
        late = research.edited_order(self.order, self.recipes["d-before-fronting-existing"])
        self.assertEqual(late.index("XRLen"), late.index(builder.FRONT) - 1)
        reverse = research.edited_order(self.order, self.recipes["b-before-sc024-existing-reverse"])
        self.assertLess(reverse.index("XRLen"), reverse.index(builder.LOWER))
        self.assertLess(reverse.index(builder.LOWER), reverse.index(builder.EARLY))

    def test_late_assumptions_keep_stress_and_disclose_secondary_r(self):
        recipe = self.recipes["d-before-fronting-existing"]
        self.assertIn("cannot independently recover", recipe["assumptions"])
        self.assertNotIn("these proposed anchors precede it", recipe["assumptions"])
        self.assertIn("Late bare r is origin-insensitive", recipe["assumptions"])

    def test_correct_and_deliberately_colliding_long_outputs(self):
        correct = self.recipes["b-before-sc024-existing"]["definitions"]["XRLen"]
        collision = self.recipes["b-before-sc024-existing-collision"]["definitions"]["XRLen"]
        self.assertIn("{*é} -> {*ē}", correct)
        self.assertNotIn("{*é} -> {*ḗ}", correct)
        self.assertIn("{*é} -> {*ḗ}", collision)
        self.assertIn("{*í} -> {*ḯ}", correct)
        self.assertIn(".#. EnglishStarConsonant* _ {*r} .#.", correct)
        self.assertIn("[?* [{*ᵘ}|{*ᶜ}] ?*]", correct)

    def test_hill_lengthening_then_long_i_lowering_is_a_distinct_two_step_recipe(self):
        recipe = self.recipes["hill-lengthen-then-lower-long-i"]
        order = research.edited_order(self.order, recipe)
        self.assertEqual(recipe["architecture"], "A")
        self.assertLess(order.index("XRLen"), order.index("XRLongILower"))
        self.assertLess(order.index("XRLongILower"), order.index(builder.EARLY))
        self.assertLess(order.index(builder.EARLY), order.index(builder.LOWER))
        long_i_lowering = recipe["definitions"]["XRLongILower"]
        self.assertIn("{*ī} -> {*ē}", long_i_lowering)
        self.assertIn("{*ḯ} -> {*ē}", long_i_lowering)
        self.assertIn("Hill2017 p.148", recipe["evidence"])
        self.assertIn("not SC015's adopted short-i lowering", recipe["assumptions"])

    def test_source_derived_components_do_not_duplicate_unified_lowering(self):
        recipe = self.recipes["c-before-sc024-explicit-immediate"]
        definitions = recipe["definitions"]
        self.assertNotIn("{*z}", definitions["XRLowerR"])
        self.assertNotIn("| {*r}]", definitions["XRLowerZS"])
        self.assertIn("{*í} -> {*ḙ}", definitions["XRLowerR"])
        order = research.edited_order(self.order, recipe)
        self.assertNotIn(builder.LOWER, order)
        self.assertLess(order.index("XRLowerR"), order.index("XRLen"))
        self.assertLess(order.index("XRMerge"), order.index(builder.EARLY))
        self.assertEqual(order.index("XRLateMerge"), order.index("XRLowerZS") + 1)

    def test_explicit_classes_preserve_stress_and_quantity_not_palatal_membership(self):
        recipe = self.recipes["b-before-sc024-explicit-before-z-loss"]
        text = research.transformed_source(self.source.read_text(), recipe)
        bodies = research.oe_pipeline._define_bodies(research.oe_pipeline._strip_comments(text))
        for symbol in ("ẹ", "ḙ", "ệ"):
            self.assertIn("{*" + symbol + "}", bodies["PGmcStarVowel"])
            self.assertIn("{*" + symbol + "}", bodies["PGmcStarFrontVowel"])
            self.assertNotIn("{*" + symbol + "}", bodies["EnglishPalatalConsonant"])
            self.assertNotIn("{*" + symbol + "}", bodies["pgrmShortVowel"] + bodies["pgrmLongVowel"])
        self.assertIn("{*ḙ}", bodies["PGmcStarAcuteVowel"])
        self.assertNotIn("{*ẹ}", bodies["PGmcStarAcuteVowel"])
        self.assertNotIn("{*ệ}", bodies["PGmcStarAcuteVowel"])
        self.assertIn("{*ệ}", bodies["PGmcStarStressedVowel"])
        self.assertIn("{*ệ}", bodies["EnglishStarLongVowel"])
        self.assertNotIn("{*ệ}", bodies["EnglishStarShortVowel"])
        self.assertIn("PNWGmcULowering", recipe["representation_audit"]["direct_class_consumers"]["EnglishStarNonHighVowel"])

    def test_merger_duration_is_explicit_and_precedes_breaking(self):
        for architecture, placement in (("a", "after-sc015"), ("b", "before-sc024"), ("c", "before-sc024")):
            for representation in ("explicit", "origin"):
                immediate = self.recipes[f"{architecture}-{placement}-{representation}-immediate"]
                delayed = self.recipes[f"{architecture}-{placement}-{representation}-before-z-loss"]
                first = research.edited_order(self.order, immediate)
                second = research.edited_order(self.order, delayed)
                self.assertEqual(first.index("XRMerge"), first.index("XRLen") + 1)
                self.assertEqual(second.index("XRMerge"), second.index(builder.ZLOSS) - 1)
                self.assertLess(second.index("XRMerge"), second.index(builder.BREAKING))
                self.assertIn("duration", delayed["assumptions"])
                self.assertIn("{*é}", delayed["definitions"]["XRMerge"])

    def test_origin_symbols_do_not_add_a_long_phoneme(self):
        recipe = self.recipes["c-before-sc024-origin-before-z-loss"]
        self.assertEqual({symbol["symbol"] for symbol in recipe["symbols"]}, {"ị", "ỉ"})
        self.assertIn("{*ỉ} -> {*ē}", recipe["definitions"]["XRLen"])
        self.assertIn("{*ỉ} -> {*é}", recipe["definitions"]["XRMerge"])
        self.assertNotIn("new reconstructed phonemes", recipe["assumptions"])
        self.assertIn("not new reconstructed phonemes", recipe["representation"])

    def test_optional_breaking_anchor_explicitly_flags_final_z_representation_effect(self):
        plan = builder.build_spec("0" * 64, [], deferred_merge_before=builder.BREAKING,
                                  requested=["b-before-sc024-explicit-before-breaking"])
        recipe = plan["recipes"][0]
        self.assertIn("known representation effect", recipe["assumptions"])
        crossed = recipe["representation_audit"]["crossed_native_literal_events"]
        self.assertIn(builder.ZLOSS, [entry["event"] for entry in crossed])

    def test_bounded_recipe_selection_and_unknown_ids_fail(self):
        with patch.object(research.subprocess, "run", side_effect=AssertionError("Foma prohibited")):
            subset = builder.build_spec("0" * 64, [], requested=["b-before-sc024-existing"])
        self.assertEqual(len(subset["recipes"]), 1)
        with self.assertRaisesRegex(ValueError, "unknown requested"):
            builder.build_spec("0" * 64, [], requested=["not-a-model"])
        with self.assertRaisesRegex(ValueError, "unknown already-long"):
            builder.build_spec("0" * 64, [], already_long_probe_ids=["missing"])


class ReceiptSummaryTests(unittest.TestCase):
    def test_aligns_named_events_not_shifted_positions(self):
        left = [{"event": "Input", "index": 1, "after": ["i"]},
                {"event": "Lower", "index": 2, "after": ["e"]},
                {"event": "Surface", "index": 3, "after": ["ē"]}]
        right = [{"event": "Input", "index": 1, "after": ["i"]},
                 {"event": "Length", "index": 2, "after": ["ī"]},
                 {"event": "Lower", "index": 3, "after": ["ī"]},
                 {"event": "Surface", "index": 4, "after": ["ī"]}]
        self.assertEqual(summary.first_common_difference(left, right), {
            "event": "Lower", "left_index": 2, "right_index": 3,
            "left": ["e"], "right": ["ī"],
        })

    def test_intermediate_difference_survives_equal_finals(self):
        def model(name, intermediate):
            return {"recipe": {"id": name}, "order": ["Lower", "Surface"],
                    "outputs": {"one": ["ē"]}, "probes": [],
                    "traces": {"one": [
                        {"event": "Lower", "index": 1, "after": [intermediate]},
                        {"event": "Surface", "index": 2, "after": ["ē"]}]}}
        result = summary.compare(model("one", "e"), model("two", "ẹ"))
        self.assertEqual(result["selected_final_difference_count"], 0)
        self.assertEqual(len(result["selected_intermediate_or_final_differences"]), 1)

    def test_different_selected_populations_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "selected IDs"):
            summary.compare({"outputs": {"one": ["ē"]}}, {"outputs": {}})


class EvidencePackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = DRIVER.parent
        with (cls.directory / "probes.json").open(encoding="utf-8") as handle:
            cls.probes = json.load(handle)
        with (cls.directory / "WITNESSES.tsv").open(encoding="utf-8", newline="") as handle:
            cls.witnesses = list(csv.reader(handle, delimiter="\t"))

    def test_witness_rows_have_consistent_columns_and_unique_ids(self):
        self.assertTrue(self.witnesses)
        self.assertEqual({len(row) for row in self.witnesses}, {len(self.witnesses[0])})
        self.assertEqual(self.witnesses[0][0], "id")
        ids = [row[0] for row in self.witnesses[1:]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_cited_experimental_probe_exists(self):
        probes = {item["id"] for item in self.probes["probes"]}
        self.assertTrue(self.probes["already_long_probe_ids"])
        self.assertTrue(set(self.probes["already_long_probe_ids"]) <= probes)
        for row in self.witnesses[1:]:
            for probe_id in row[10].split("; "):
                if probe_id != "—":
                    self.assertIn(probe_id, probes, msg=row[0])


if __name__ == "__main__":
    unittest.main()
