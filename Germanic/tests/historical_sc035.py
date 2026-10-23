"""Replay immutable SC035 assays in a disposable, commit-pinned runtime."""
from contextlib import contextmanager
from pathlib import Path
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[2]


@contextmanager
def historical_runtime(commit):
    image = subprocess.check_output(
        ["docker", "compose", "images", "-q", "backend"], cwd=ROOT, text=True).strip()
    if not image:
        raise RuntimeError("the backend image must exist for historical Foma replay")
    with tempfile.TemporaryDirectory(prefix="capr_sc035_history_") as temporary:
        runtime = Path(temporary)
        (runtime / "fsts").mkdir()
        source = subprocess.check_output(
            ["git", "show", f"{commit}:Germanic/fsts/germanic.txt"], cwd=ROOT)
        (runtime / "fsts/germanic.txt").write_bytes(source)
        mounts = [
            (runtime, "/usr/app", False),
            (ROOT / "Germanic/tools", "/usr/app/tools", True),
            (ROOT / "Germanic/data", "/usr/app/data", True),
            (ROOT / "Germanic/docs", "/usr/app/docs", True),
            (ROOT / "backend/oe_input_context.py", "/usr/app/oe_input_context.py", True),
            (ROOT / "backend/compare_fst.py", "/usr/app/compare_fst.py", True),
        ]
        command = ["docker", "run", "--rm", "-i", "--workdir", "/usr/app",
                   "--entrypoint", "sh"]
        for host, container, readonly in mounts:
            command += ["--volume", f"{host}:{container}" + (":ro" if readonly else "")]
        command += [image, "-c"]

        def execute(script, timeout=1800):
            return subprocess.run(command + [script], cwd=ROOT, text=True,
                                  capture_output=True, check=True, timeout=timeout)

        execute(
            "python3 tools/generate_oe_sandbox.py > /dev/null && "
            "foma -q -f fsts/old_english_sandbox.txt -e quit > /dev/null && "
            "PYTHONPATH=tools python3 -c "
            "'import oe_pipeline; from capr_runtime import write_build_manifest; "
            'write_build_manifest(oe_pipeline.expected_snapshot_bins() + ["old_english.bin"])'
            "'")
        yield execute
