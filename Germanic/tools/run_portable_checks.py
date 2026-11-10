#!/usr/bin/env python3
"""Run explicitly portable checks; never certify unexecuted local capabilities."""
from __future__ import annotations

import argparse
import codecs
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / ".ci-results"


def run_check(argv: list[str], log: Path, env: dict[str, str]) -> int:
    decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
    with log.open("wb") as stream:
        try:
            process = subprocess.Popen(
                argv, cwd=ROOT, env=env, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, bufsize=0)
        except OSError as exc:
            message = f"Cannot start {argv[0]}: {exc}\n"
            stream.write(message.encode())
            print(message, end="", flush=True)
            return 127
        with process:
            while chunk := process.stdout.read(8192):
                stream.write(chunk)
                stream.flush()
                print(decoder.decode(chunk), end="", flush=True)
            print(decoder.decode(b"", final=True), end="", flush=True)
            return process.wait()


def publish(text: str) -> None:
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a", encoding="utf-8") as stream:
            stream.write(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, choices=(1, 2, 4), default=1,
                        help="portable pytest processes; 1 retains the serial reference")
    options = parser.parse_args(argv or [])
    if os.environ.get("PYTEST_ADDOPTS"):
        parser.error("portable runner requires empty PYTEST_ADDOPTS; use the recorded --workers option")
    started = time.monotonic()
    OUTPUT.mkdir(exist_ok=True)
    scratch = OUTPUT / "scratch"
    scratch.mkdir(exist_ok=True)
    env = dict(os.environ, TMPDIR=str(scratch), TMP=str(scratch), TEMP=str(scratch),
               PYTHONUNBUFFERED="1")
    parallel = ["-n", str(options.workers), "--dist", "loadfile"] if options.workers > 1 else []
    checks = [
        ("survey preflight", ["Germanic/tools/pgmc_reconstruction_survey.py", "--mode", "portable"]),
        ("bibliography", ["Germanic/tools/check_bibliography_sanity.py"]),
        ("regressions", ["-m", "pytest", "-v", "-ra", "--durations=40",
                         "--validation-mode=portable", *parallel,
                         "Germanic/tests", f"--junitxml={OUTPUT / 'tests.xml'}"]),
        ("artifact graph", ["Germanic/tools/artifact_graph.py", "--check", "--mode", "portable"]),
        ("index", ["Germanic/tools/check_index_verborum.py"]),
    ]
    for path in [OUTPUT / "tests.xml", OUTPUT / "summary.md", OUTPUT / "timings.json",
                 *[OUTPUT / (name.replace(" ", "-") + ".log") for name, _ in checks]]:
        path.unlink(missing_ok=True)
    results = []
    for name, arguments in checks:
        log = OUTPUT / (name.replace(" ", "-") + ".log")
        command = [sys.executable, *arguments]
        print(f"\nSTART {name} ({log.relative_to(ROOT)})", flush=True)
        if name == "regressions":
            print("Live pytest output follows. Silence means the current test/fixture "
                  "has not emitted progress; it is not proof of a hang.", flush=True)
        phase_started = time.monotonic()
        code = run_check(command, log, env)
        elapsed = time.monotonic() - phase_started
        results.append(dict(name=name, returncode=code, elapsed_seconds=elapsed,
                            argv=command, log=str(log.relative_to(ROOT))))
        print(f"\nEND {name}: {'PASS' if code == 0 else 'FAIL'} "
              f"(exit {code}; {elapsed:.2f}s)", flush=True)
        (OUTPUT / "timings.json").write_text(json.dumps({
            "workers": options.workers, "wall_seconds": time.monotonic() - started,
            "phases": results,
        }, indent=2) + "\n", encoding="utf-8")
        publish(f"- {name}: {'PASS' if code == 0 else 'FAIL'} "
                f"(exit {code}; {elapsed:.2f}s)\n")
        if name == "survey preflight" and code:
            break
    failures = [result["name"] for result in results if result["returncode"]]
    report = OUTPUT / "tests.xml"
    tree = None
    report_error = None
    counts = None
    if any(result["name"] == "regressions" for result in results):
        try:
            tree = ET.parse(report)
            counts = {key: sum(int(suite.get(key, "0")) for suite in tree.iter("testsuite"))
                      for key in ("tests", "failures", "errors", "skipped")}
            if not counts["tests"] or counts["failures"] or counts["errors"]:
                failures.append("JUnit regression results")
        except (OSError, ET.ParseError, ValueError) as exc:
            tree = None
            report_error = f"JUnit unavailable or invalid: {exc}. See regressions.log for original diagnostics."
            failures.append("JUnit report")
    lines = [
        "## Germanic portable validation",
        f"**Portable: {'FAIL' if failures else 'PASS'}**",
        "",
        f"Pytest workers: {options.workers}; no runtime execution or deselection.",
        "| Check | Result / original exit | Seconds | Complete log |",
        "| --- | --- | --- | --- |",
        *[f"| {result['name']} | {'FAIL' if result['returncode'] else 'PASS'} / "
          f"{result['returncode']} | {result['elapsed_seconds']:.2f} | `{result['log']}` |"
          for result in results],
        "",
        f"Total runner wall time: {time.monotonic() - started:.2f}s. "
        "Machine-readable commands, exit codes and timings: `.ci-results/timings.json`.",
        "",
        "**NOT RUN — local holding-dependent full validation:** all declared original "
        "PDFs and their complete provenance; original page-image verification was not repeated.",
        "**NOT RUN — provisioned runtime validation:** runtime_bins, full_trace, "
        "lexical_sources, interaction_matrix (requires an isolated Foma runner, "
        "compiled bins and build manifests). Tracked runtime receipts can still be checked "
        "by portable regression tests; that is not a new runtime execution.",
        "",
        "Full local commands: `python3 Germanic/tools/pgmc_reconstruction_survey.py` "
        "and `python3 -m pytest -q Germanic/tests` after provisioning holdings; "
        "`python3 Germanic/tools/artifact_graph.py --check` after provisioning runtime.",
        "Stale generated projections: `python3 Germanic/tools/adjudicate.py --refresh`. "
        "Portable-only refresh: `python3 Germanic/tools/adjudicate.py --refresh --mode portable` "
        "(never rewrites unavailable original hashes; cannot repair their provenance).",
    ]
    if tree is not None:
        lines.extend(["", f"JUnit test/subtest result counts: `{json.dumps(counts)}`. "
                      "These include subtests, not just collected node IDs."])
        skipped = list(tree.iter("skipped"))
        if skipped:
            reasons = sorted({item.get("message", "").replace("\n", " ")
                              for item in skipped})
            lines.extend(["", f"**Other test checks not executed: {len(skipped)} skipped.**",
                          *[f"- {reason}" for reason in reasons]])
        details = []
        for case in tree.iter("testcase"):
            for failure in [*case.findall("failure"), *case.findall("error")]:
                details.append(f"- `{case.get('classname')}.{case.get('name')}`: "
                               + failure.get("message", "").replace("\n", " ")[:700])
        if details:
            lines.extend(["", "### Genuine regression failures", *details])
        slowest = sorted(tree.iter("testcase"), key=lambda case: float(case.get("time", "0")),
                         reverse=True)[:8]
        lines.extend(["", "### Slowest test cases (JUnit, including setup/teardown)",
                      *[f"- {float(case.get('time', '0')):.2f}s "
                        f"`{case.get('classname')}.{case.get('name')}`" for case in slowest],
                      "", "Summed parallel test times are not runner wall time. "
                      "The complete pytest log also contains `--durations=40`."])
    if report_error:
        lines.extend(["", report_error])
    if results[0]["returncode"]:
        lines.extend(["", "Preflight failed once; dependent checks were not executed. "
                      "See the complete preflight log for the exact file and cause."])
    summary = "\n".join(lines) + "\n"
    (OUTPUT / "summary.md").write_text(summary, encoding="utf-8")
    publish(summary)
    print(summary, flush=True)
    return next((result["returncode"] for result in results if result["returncode"]),
                int(bool(failures)))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
