"""Replay immutable commit-pinned assays in a disposable runtime.

Compiled historical cascades are reused through the content-addressed
cache in ``Germanic/tools/compile_cache.py``; see that module and
``docs/HISTORICAL_REPLAY.md``. A cached build is verified against its
recorded digest before reuse; on any mismatch the cascade is recompiled.
"""
from contextlib import contextmanager
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "Germanic/tools"))
from compile_cache import (  # noqa: E402
    BUILD_ARTIFACT_GLOBS, cached_build, compile_cache_key, store_build)


@contextmanager
def historical_runtime(commit):
    image = subprocess.check_output(
        ["docker", "compose", "images", "-q", "backend"], cwd=ROOT, text=True).strip()
    if not image:
        raise RuntimeError("the backend image must exist for historical Foma replay")
    source = subprocess.check_output(
        ["git", "show", f"{commit}:Germanic/fsts/germanic.txt"], cwd=ROOT)
    corpus = subprocess.check_output(
        ["git", "show", f"{commit}:Germanic/data/germanic-aligned-final.tsv"], cwd=ROOT)
    mounts = [
        (ROOT / "Germanic/tools", "/usr/app/tools", True),
        (ROOT / "Germanic/data", "/usr/app/data_host", True),
        (ROOT / "Germanic/docs", "/usr/app/docs", True),
        (ROOT / "backend/oe_input_context.py", "/usr/app/oe_input_context.py", True),
        (ROOT / "backend/compare_fst.py", "/usr/app/compare_fst.py", True),
    ]
    # Keep all writable artifacts inside the disposable container. Nested
    # bind targets under a host temporary root can outlive `docker run --rm`
    # on Docker Desktop and make even user-owned directories undeletable.
    command = ["docker", "create", "--workdir", "/usr/app", "--entrypoint", "sleep"]
    for host, container, readonly in mounts:
        command += ["--volume", f"{host}:{container}" + (":ro" if readonly else "")]
    container_id = subprocess.check_output(
        command + [image, "infinity"], cwd=ROOT, text=True).strip()
    try:
        subprocess.run(["docker", "start", container_id], cwd=ROOT,
                       capture_output=True, check=True)
        subprocess.run(
            ["docker", "exec", "-i", container_id, "sh", "-c",
             "mkdir -p /usr/app/fsts && cat > /usr/app/fsts/germanic.txt"],
            input=source, cwd=ROOT, capture_output=True, check=True)
        # Pin the selected corpus to the replayed commit so later authorized
        # corpus admissions cannot perturb an immutable historical receipt.
        subprocess.run(
            ["docker", "exec", "-i", container_id, "sh", "-c",
             "cp -a /usr/app/data_host /usr/app/data && "
             "cat > /usr/app/data/germanic-aligned-final.tsv"],
            input=corpus, cwd=ROOT, capture_output=True, check=True)

        def execute(script, timeout=1800):
            return subprocess.run(["docker", "exec", container_id, "sh", "-c", script],
                                  cwd=ROOT, text=True,
                                  capture_output=True, check=True, timeout=timeout)

        key = compile_cache_key(image, source, corpus)
        cached = cached_build(key)
        if cached is not None:
            subprocess.run(
                ["docker", "exec", "-i", container_id, "sh", "-c",
                 "cd /usr/app && tar xf -"],
                input=cached, cwd=ROOT, capture_output=True, check=True)
        else:
            execute(
                "python3 tools/generate_oe_sandbox.py > /dev/null && "
                "foma -q -f fsts/old_english_sandbox.txt -e quit > /dev/null && "
                "PYTHONPATH=tools python3 -c "
                "'import oe_pipeline; from capr_runtime import write_build_manifest; "
                'write_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])'
                "'")
            exported = subprocess.run(
                ["docker", "exec", container_id, "sh", "-c",
                 f"cd /usr/app && tar cf - {BUILD_ARTIFACT_GLOBS}"],
                cwd=ROOT, capture_output=True, check=False)
            if exported.returncode == 0:
                store_build(key, exported.stdout, commit)
        yield execute
    finally:
        subprocess.run(["docker", "rm", "--force", container_id], cwd=ROOT,
                       capture_output=True, check=True)
