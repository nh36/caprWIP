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

This cache serves explicit historical-replay investigations only
(tests/historical_sc035.py). Ordinary incremental regression consumes the
Git-stored canonical full-trace reports and needs no evaluation cache.
"""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
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


def _log_event(kind: str, key: str, detail: str = "") -> None:
    """Append a cache event so hits/misses are visible in logs/receipts.

    Cached evidence must never be mistaken for a newly executed build;
    the events log makes every reuse auditable.
    """
    CACHE_DIR.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with (CACHE_DIR / "events.log").open("a", encoding="utf-8") as handle:
        handle.write(f"{stamp} {kind} {key}"
                     + (f" {detail}" if detail else "") + "\n")


def cached_build(key: str) -> bytes | None:
    """Return verified cached build bytes for *key*, or None."""
    archive, record = CACHE_DIR / f"{key}.tar", CACHE_DIR / f"{key}.json"
    if not (archive.is_file() and record.is_file()):
        _log_event("miss", key, "no entry")
        return None
    try:
        metadata = json.loads(record.read_text())
    except ValueError:
        _log_event("miss", key, "unreadable metadata")
        return None
    payload = archive.read_bytes()
    if (metadata.get("key") == key and metadata.get("archive_sha256")
            == hashlib.sha256(payload).hexdigest()):
        _log_event("hit", key)
        return payload
    # Corrupted or mismatched: fall back to a fresh compile.
    _log_event("miss", key, "digest mismatch (safe miss)")
    return None


def _atomic_write(path: Path, payload: bytes) -> None:
    """Write via a same-directory temp file and rename: a reader never
    observes a torn archive or metadata file, and an interrupted writer
    leaves no partial entry (only an unreferenced temp file)."""
    handle = tempfile.NamedTemporaryFile(
        dir=path.parent, prefix=path.name + ".", delete=False)
    try:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
        handle.close()
        os.replace(handle.name, path)
    except BaseException:
        handle.close()
        os.unlink(handle.name)
        raise


def store_build(key: str, payload: bytes, provenance: str) -> None:
    if not payload:
        return
    CACHE_DIR.mkdir(exist_ok=True)
    # Archive first, metadata last: an entry becomes eligible for reuse
    # only once its verifying record exists.
    _atomic_write(CACHE_DIR / f"{key}.tar", payload)
    _atomic_write(CACHE_DIR / f"{key}.json", (json.dumps({
        "key": key, "provenance": provenance,
        "archive_sha256": hashlib.sha256(payload).hexdigest(),
        "artifacts": BUILD_ARTIFACT_GLOBS,
    }, indent=1) + "\n").encode("utf-8"))
    _log_event("store", key, f"provenance={provenance}")
