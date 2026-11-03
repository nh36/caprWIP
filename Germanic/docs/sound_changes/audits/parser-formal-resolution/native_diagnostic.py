#!/usr/bin/env python3
"""Isolated source instrumentation, never an alternative production formal gate."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


PIN = "82f9acdef234eae8b7619ccc3a386cc0d7df62bc"
IMAGE = "sha256:91065f6b1fe4c180737956d44b5ce0158787d396cb9c1557a5f4d86023b12b13"


def worker():
    original = Path("/capr/source.c").read_text()
    installed = Path("/usr/app/foma-" + PIN + "/foma/structures.c")
    assert installed.read_text() == original
    with tempfile.TemporaryDirectory(prefix="capr_native_diagnostic_") as temporary:
        source = Path(temporary) / "foma"
        shutil.copytree(installed.parent, source)
        start = original.index("int fsm_isidentity(")
        end = original.index("\nstruct fsm *fsm_markallfinal", start)
        body = original[start:end]
        marker = "            free(newstring);"
        assert body.count(marker) == 1
        trace = (
            '            fprintf(stderr, "DEBT_RELEASE source=%d target=%d length=%d '
            'aliases_current=%d\\n", v, vp, currd->length, newstring == currd->string);\n')
        report = dict(pin=PIN, image=IMAGE, variants={})
        for variant in ("trace-original", "retain-borrowed-debts"):
            replacement = trace + (marker if variant == "trace-original" else
                                   "            /* Diagnostic only: retain borrowed debts. */")
            changed = original[:start] + body.replace(marker, replacement) + original[end:]
            (source / "structures.c").write_text(changed)
            (Path("/out") / (variant + "-structures.c")).write_text(changed)
            build = subprocess.run(
                ["make", "-s"], cwd=source, capture_output=True, text=True, timeout=180)
            (Path("/out") / (variant + "-build.log")).write_text(build.stdout + build.stderr)
            build.check_returncode()
            environment = dict(os.environ, LD_LIBRARY_PATH=str(source))
            results = {}
            for name in ("root", "plain", "delay", "native"):
                argv = [str(source / "foma"), "-q", "-e", "read att /capr/" + name + ".att",
                        "-e", "test functional", "-e", "test unambiguous", "-e", "quit"]
                result = subprocess.run(
                    argv, env=environment, capture_output=True, text=True, timeout=180)
                results[name] = dict(
                    argv=argv, returncode=result.returncode, stdout=result.stdout,
                    stderr=result.stderr)
                result.check_returncode()
            report["variants"][variant] = dict(
                source_sha256=hashlib.sha256(changed.encode()).hexdigest(), results=results)
        Path("/out/report.json").write_text(json.dumps(report, indent=2))


def host(identifier):
    import experiment
    from adjudication_control import run_logged
    from experiment_snapshot import create_snapshot

    evidence = experiment.ROOT / ".capr-work/experiments/parser-global-proof-01/results"
    snapshot = create_snapshot(
        identifier, "Pinned identity-checker lifetime diagnosis; not a production gate",
        inputs={
            "worker": Path(__file__),
            "source": experiment.ROOT / ".capr-work/pinned-foma/structures.c",
            "license": experiment.ROOT / ".capr-work/pinned-foma/COPYING",
            **{name: evidence / (component + ".att") for name, component in (
                ("root", "PGCellRoot"), ("plain", "PGCellPlain"),
                ("delay", "ProbeDelay"), ("native", "EnglishProtoNative"))}},
        variants={"instrumentation": "release trace", "diagnosis": "retain borrowed debts"},
        expected_outcomes={"installed_runtime_modified": False, "production_gate": False},
        environment={"image": IMAGE, "pin": PIN})
    result = run_logged(
        ["docker", "run", "--rm", "--entrypoint", "python3",
         "--mount", "type=bind,src=" + str(snapshot.root / "snapshot") + ",dst=/capr,readonly",
         "--mount", "type=bind,src=" + str(snapshot.staging_dir) + ",dst=/out",
         IMAGE, "/capr/worker.py", "--worker"],
        label="pinned-native-diagnostic", log_dir=snapshot.staging_dir, timeout=900)
    snapshot.complete("passed" if result["ok"] else "failed",
                      "Instrumented comparison only; unchanged native gate still required",
                      command_receipts=[result])
    snapshot.staging_dir.symlink_to("results", target_is_directory=True)
    print(snapshot.root)
    if not result["ok"]:
        print(Path(result["stderr_log"]).read_text())
        raise SystemExit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--id")
    parser.add_argument("--worker", action="store_true")
    args = parser.parse_args()
    worker() if args.worker else host(args.id)
