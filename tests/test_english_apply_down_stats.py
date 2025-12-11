import importlib.util
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / "server" / "tools" / "english_apply_down_stats.py"
spec = importlib.util.spec_from_file_location("english_apply_down_stats", MODULE_PATH)
ENGLISH_STATS = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ENGLISH_STATS)

FIXTURE_PATH = Path(__file__).resolve().parent / "fixtures" / "english_rows.tsv"

class NormalizeProtoTests(unittest.TestCase):
    def test_strips_markers(self) -> None:
        raw = "{*b} {*ă}-{*n}/*ą"
        self.assertEqual(ENGLISH_STATS.normalize_proto(raw), "băną")

class LoadRowsTests(unittest.TestCase):
    def test_filters_and_normalizes(self) -> None:
        rows = ENGLISH_STATS.load_rows(FIXTURE_PATH)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["concept"], "bake")
        self.assertEqual(rows[0]["proto"], "*b*a*k*ă*n*ą")
        self.assertEqual(rows[0]["norm"], "bakăną")
        self.assertEqual(rows[0]["ipa"], "beik")
        self.assertEqual(rows[1]["concept"], "ban")
        self.assertEqual(rows[1]["norm"], "bannăn")

class RunApplyDownTests(unittest.TestCase):
    def test_deduplicates_and_drops_placeholder_outputs(self) -> None:
        fake_stdout = "\n".join([
            "form\tfoo",
            "form\tfoo",
            "form\t+?",
            "form\tbar",
            "form\t",
        ]) + "\n"
        completed = mock.Mock(stdout=fake_stdout.encode("utf-8"), stderr=b"", returncode=0)
        with mock.patch.object(ENGLISH_STATS.subprocess, "run", return_value=completed) as mocked:
            outputs = ENGLISH_STATS.run_apply_down(Path("fake.bin"), "form")
        self.assertEqual(outputs, ["foo", "bar"])
        mocked.assert_called_once()
