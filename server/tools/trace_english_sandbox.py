#!/usr/bin/env python3
"""Stage-by-stage tracer for the English sandbox cascade.

Usage:
    python3 server/tools/trace_english_sandbox.py --lexeme "*fiskaz" --lexeme "*gebaną"

Outputs the intermediate forms after each stage (ProtoInput through Surface) so we can see
where vowels/consonants change. Designed to help debug KIT/FOOT cases.
"""

import argparse
import subprocess
import sys
from pathlib import Path

STAGES = [
    "EnglishSandboxProtoInput",
    "EnglishSandboxInitialKnMarkers",
    "EnglishSandboxConsonantRules",
    "EnglishSandboxGhMarker",
    "EnglishSandboxGlideDeletion",
    "EnglishSandboxWestGermanic",
    "EnglishSandboxOpenSyllableLengthening",
    "EnglishSandboxBreakingLengthening",
    "EnglishSandboxVowelRules",
    "EnglishSandboxPostVocalicRLoss",
    "EnglishSandboxWeakTailReductions",
    "EnglishSandboxSilentInitialCleanup",
    "EnglishSandboxGhDeletion",
    "EnglishSandboxOrthography",
]


def run_foma(script: str, cwd: Path) -> str:
    proc = subprocess.run(
        ["foma", "-q"],
        input=script.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        check=True,
    )
    if proc.stderr:
        sys.stderr.buffer.write(proc.stderr)
    return proc.stdout.decode("utf-8").strip()


def trace_lexeme(lexeme: str, cwd: Path) -> None:
    print(f"=== {lexeme} ===")
    current = lexeme
    for stage in STAGES:
        script = f"source fsts/english_brace_sandbox.txt\nregex {stage};\napply down {current}\nquit\n"
        output = run_foma(script, cwd)
        lines = []
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith(("source", "Opening", "Writing", "regex", "apply", "quit", "clear", "save")):
                continue
            lines.append(line)
        surface = lines[-1] if lines else current
        print(f"{stage}: {surface}")
        current = surface
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Trace English sandbox stages for given lexemes.")
    parser.add_argument("--lexeme", action="append", required=True, help="Proto lexeme (brace form)")
    args = parser.parse_args()
    cwd = Path(__file__).resolve().parents[1]  # repo root
    for lex in args.lexeme:
        trace_lexeme(lex, cwd)


if __name__ == "__main__":
    main()
