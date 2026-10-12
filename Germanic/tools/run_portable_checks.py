#!/usr/bin/env python3
"""Run explicitly portable checks; never certify unexecuted local capabilities."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / ".ci-results"


def main() -> int:
    OUTPUT.mkdir(exist_ok=True)
    scratch = OUTPUT / "scratch"
    scratch.mkdir(exist_ok=True)
    env = dict(os.environ, TMPDIR=str(scratch), TMP=str(scratch), TEMP=str(scratch))
    checks = [
        ("survey preflight", ["Germanic/tools/pgmc_reconstruction_survey.py", "--mode", "portable"]),
        ("bibliography", ["Germanic/tools/check_bibliography_sanity.py"]),
        ("regressions", ["-m", "pytest", "-q", "-ra", "--validation-mode=portable",
                         "Germanic/tests", f"--junitxml={OUTPUT / 'tests.xml'}"]),
        ("artifact graph", ["Germanic/tools/artifact_graph.py", "--check", "--mode", "portable"]),
        ("index", ["Germanic/tools/check_index_verborum.py"]),
    ]
    for path in [OUTPUT / "tests.xml", OUTPUT / "summary.md",
                 *[OUTPUT / (name.replace(" ", "-") + ".log") for name, _ in checks]]:
        path.unlink(missing_ok=True)
    results = []
    for name, arguments in checks:
        log = OUTPUT / (name.replace(" ", "-") + ".log")
        with log.open("w", encoding="utf-8") as stream:
            result = subprocess.run([sys.executable, *arguments], cwd=ROOT,
                                    env=env, stdout=stream, stderr=subprocess.STDOUT)
        results.append((name, result.returncode, log))
        print(f"{name}: {'PASS' if result.returncode == 0 else 'FAIL'} ({log.relative_to(ROOT)})",
              flush=True)
        if result.returncode:
            print(log.read_text(encoding="utf-8"), flush=True)
        if name == "survey preflight" and result.returncode:
            break
    failures = [name for name, code, _ in results if code]
    lines = [
        "## Germanic portable validation",
        f"**Portable: {'FAIL' if failures else 'PASS'}**",
        "",
        "| Check | Result | Complete log |", "| --- | --- | --- |",
        *[f"| {name} | {'FAIL' if code else 'PASS'} | `{log.relative_to(ROOT)}` |"
          for name, code, log in results],
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
    report = OUTPUT / "tests.xml"
    if report.exists():
        tree = ET.parse(report)
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
    if failures and not report.exists():
        lines.extend(["", "Preflight failed once; dependent checks were not executed. "
                      "See the complete preflight log for the exact file and cause."])
    summary = "\n".join(lines) + "\n"
    (OUTPUT / "summary.md").write_text(summary, encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(os.environ["GITHUB_STEP_SUMMARY"]).open("a", encoding="utf-8") as stream:
            stream.write(summary)
    print(summary)
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
