"""Tests for the historical compile cache's reuse, integrity and visibility.

Synthetic payloads only: no Docker or Foma. These pin the Milestone 4
guarantees for the existing content-addressed cache:

* unchanged inputs produce a stable key whose stored build is reused;
* any changed input (source, corpus, image, extra) forces a miss and
  therefore a fresh compile fallback;
* writes are atomic (no torn archive/metadata is ever observable) and a
  corrupted entry degrades to a safe miss, never a wrong hit;
* every hit, miss and store is visible in the cache events log, so
  cached evidence cannot masquerade as a newly executed build.
"""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

import compile_cache as cc  # noqa: E402


class CacheHarness(unittest.TestCase):

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="capr-cache-test-"))
        patcher = mock.patch.object(cc, "CACHE_DIR", self.tmp)
        patcher.start()
        self.addCleanup(patcher.stop)

    def events(self) -> list[str]:
        log = self.tmp / "events.log"
        return log.read_text(encoding="utf-8").splitlines() \
            if log.is_file() else []


class KeyIdentityTests(CacheHarness):

    def test_unchanged_inputs_yield_stable_key(self):
        a = cc.compile_cache_key("img:1", b"source", b"corpus")
        b = cc.compile_cache_key("img:1", b"source", b"corpus")
        self.assertEqual(a, b)

    def test_any_changed_input_changes_the_key(self):
        base = cc.compile_cache_key("img:1", b"source", b"corpus",
                                    {"x": b"1"})
        variants = [
            cc.compile_cache_key("img:2", b"source", b"corpus", {"x": b"1"}),
            cc.compile_cache_key("img:1", b"source2", b"corpus", {"x": b"1"}),
            cc.compile_cache_key("img:1", b"source", b"corpus2", {"x": b"1"}),
            cc.compile_cache_key("img:1", b"source", b"corpus", {"x": b"2"}),
        ]
        for variant in variants:
            self.assertNotEqual(base, variant)


class ReuseAndFallbackTests(CacheHarness):
    """Acceptance: unchanged experiment reuses valid compiled work, while a
    source or environment change forces the correct fallback (a miss)."""

    def test_round_trip_reuse(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        self.assertEqual(cc.cached_build(key), b"tar-bytes")

    def test_source_change_forces_fresh_compile(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        changed = cc.compile_cache_key("img:1", b"src EDITED", b"corpus")
        self.assertIsNone(cc.cached_build(changed))

    def test_environment_change_forces_fresh_compile(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        changed = cc.compile_cache_key("img:other-foma", b"src", b"corpus")
        self.assertIsNone(cc.cached_build(changed))

    def test_empty_payload_never_stored(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        cc.store_build(key, b"", provenance="deadbeef")
        self.assertFalse((self.tmp / f"{key}.tar").exists())


class IntegrityTests(CacheHarness):

    def _stored(self) -> str:
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        return key

    def test_corrupted_archive_is_a_safe_miss(self):
        key = self._stored()
        (self.tmp / f"{key}.tar").write_bytes(b"torn write")
        self.assertIsNone(cc.cached_build(key))

    def test_unreadable_metadata_is_a_safe_miss(self):
        key = self._stored()
        (self.tmp / f"{key}.json").write_text("{not json")
        self.assertIsNone(cc.cached_build(key))

    def test_metadata_for_wrong_key_is_a_safe_miss(self):
        key = self._stored()
        record = json.loads((self.tmp / f"{key}.json").read_text())
        record["key"] = "0" * 64
        (self.tmp / f"{key}.json").write_text(json.dumps(record))
        self.assertIsNone(cc.cached_build(key))

    def test_writes_are_atomic_and_leave_no_temp_files(self):
        key = self._stored()
        leftovers = [p.name for p in self.tmp.iterdir()
                     if p.suffix not in (".tar", ".json")
                     and p.name != "events.log"]
        self.assertEqual(leftovers, [])
        metadata = json.loads((self.tmp / f"{key}.json").read_text())
        self.assertEqual(metadata["archive_sha256"],
                         hashlib.sha256(b"tar-bytes").hexdigest())

    def test_interrupted_write_leaves_no_partial_entry(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        with mock.patch.object(cc.os, "replace",
                               side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        self.assertFalse((self.tmp / f"{key}.tar").exists())
        self.assertFalse((self.tmp / f"{key}.json").exists())


class VisibilityTests(CacheHarness):
    """Hits and misses must be visible; cached evidence must never be
    describable as a newly executed experiment."""

    def test_store_hit_and_miss_are_logged(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        self.assertIsNone(cc.cached_build(key))  # miss: no entry
        cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        self.assertEqual(cc.cached_build(key), b"tar-bytes")  # hit
        kinds = [line.split()[1] for line in self.events()]
        self.assertEqual(kinds, ["miss", "store", "hit"])
        self.assertIn("provenance=deadbeef", self.events()[1])

    def test_digest_mismatch_miss_is_distinguished(self):
        key = cc.compile_cache_key("img:1", b"src", b"corpus")
        cc.store_build(key, b"tar-bytes", provenance="deadbeef")
        (self.tmp / f"{key}.tar").write_bytes(b"corrupt")
        self.assertIsNone(cc.cached_build(key))
        self.assertIn("digest mismatch", self.events()[-1])


if __name__ == "__main__":
    unittest.main()
