#!/usr/bin/env python3
"""Content-addressed cache for compiled Foma cascade builds.

Cache identity is a digest over every compilation input: the Foma source,
the corpus, the live generator/pipeline tools, and the backend image id
(which pins the Foma build and execution environment). A Git commit id is
never used as a cache key: it does not uniquely describe the mounted tools
or the runtime image that participate in a build.

Entries live in ``.capr_compile_cache/`` at the repository root
(untracked): ``<key>.tar`` holds the build artifacts exactly as produced
inside the container working directory, and ``<key>.json`` records the key,
provenance label and archive digest. A cached archive is verified against
its recorded digest before reuse; any mismatch is treated as a miss.

Evaluation results (``<key>.eval.json``) may be cached under the same key
by the incremental regression tool, so unchanged executable inputs do not
trigger a fresh full-corpus Foma execution.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE_DIR = ROOT / ".capr_compile_cache"
# Container-relative artifacts produced by the cascade build and restored
# verbatim on a cache hit (tar preserves the manifest/bin mtime relation).
BUILD_ARTIFACT_GLOBS = "*.bin oe_build_manifest.json fsts/old_english_sandbox.txt"
# Live tools that participate in every cascade build.
BUILD_TOOLS = ("generate_oe_sandbox.py", "oe_pipeline.py", "capr_runtime.py")


def compile_cache_key(image: str, source: bytes, corpus: bytes,
                      extra: dict[str, bytes] | None = None) -> str:
    """Content digest over every input of a cascade build."""
    digest = hashlib.sha256()
    for label, payload in (
            ("image", image.encode()), ("source", source), ("corpus", corpus)):
        digest.update(f"{label}:{len(payload)}:".encode())
        digest.update(payload)
    for tool in BUILD_TOOLS:
        payload = (ROOT / "Germanic/tools" / tool).read_bytes()
        digest.update(f"tool:{tool}:{len(payload)}:".encode())
        digest.update(payload)
    for label in sorted(extra or {}):
        payload = (extra or {})[label]
        digest.update(f"extra:{label}:{len(payload)}:".encode())
        digest.update(payload)
    return digest.hexdigest()


def cached_build(key: str) -> bytes | None:
    """Return verified cached build bytes for *key*, or None."""
    archive, record = CACHE_DIR / f"{key}.tar", CACHE_DIR / f"{key}.json"
    if not (archive.is_file() and record.is_file()):
        return None
    try:
        metadata = json.loads(record.read_text())
    except ValueError:
        return None
    payload = archive.read_bytes()
    if (metadata.get("key") == key and metadata.get("archive_sha256")
            == hashlib.sha256(payload).hexdigest()):
        return payload
    return None  # corrupted or mismatched: fall back to a fresh compile


def store_build(key: str, payload: bytes, provenance: str) -> None:
    if not payload:
        return
    CACHE_DIR.mkdir(exist_ok=True)
    (CACHE_DIR / f"{key}.tar").write_bytes(payload)
    (CACHE_DIR / f"{key}.json").write_text(json.dumps({
        "key": key, "provenance": provenance,
        "archive_sha256": hashlib.sha256(payload).hexdigest(),
        "artifacts": BUILD_ARTIFACT_GLOBS,
    }, indent=1) + "\n")


def cached_evaluation(key: str) -> dict | None:
    path = CACHE_DIR / f"{key}.eval.json"
    if not path.is_file():
        return None
    try:
        record = json.loads(path.read_text())
    except ValueError:
        return None
    return record if record.get("cache_key") == key else None


def store_evaluation(key: str, record: dict) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    (CACHE_DIR / f"{key}.eval.json").write_text(
        json.dumps({**record, "cache_key": key}, ensure_ascii=False) + "\n")
