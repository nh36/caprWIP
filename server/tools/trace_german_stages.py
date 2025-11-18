#!/usr/bin/env python3
"""Stage-by-stage tracer for the Germanic transducer cascade.

Run inside the backend container (or any environment where ``foma`` is
available) to compile the German stage automata and stream a set of lexemes
through each stage.  This is meant to make debugging the ever-growing German
stack tractable.

Examples
--------

Trace the default probes (``laukaz``/``milkiz``) through every stage::

    python3 server/tools/trace_german_stages.py

Trace a custom list and capture the output as Markdown::

    python3 server/tools/trace_german_stages.py \
        --lexeme laukaz --lexeme kni\u02d0 --lexeme bro\u02d0t > /tmp/trace.md

The tool preserves the lexeme exactly as provided.  If your proto lexeme uses
the Burmish-style brace notation (e.g. ``l{au}kaz``), pass it verbatim.  If you
want the helper to wrap the core diphthongs automatically, add
``--brace-diphthongs``.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


DEFAULT_STAGES: List[str] = [
    "GermanProtoInput",
    "GermanAfterEw",
    "GermanAfterLongV",
    "GermanAfterAu",
    "GermanAfterNasal",
    "GermanAfterConsonant",
    "GermanAfterStopShift",
    "GermanAfterPalatal",
    "GermanAfterAzLoss",
    "GermanAfterApocope",
    "GermanAfterVowelAdj",
    "GermanAfterFinalDevoice",
    "GermanAfterCleanup",
    "GermanAfterOrthography",
    "GermanAfterStarDrop",
    "GermanPreSurface",
    "GermanReflexes",
    "German",
]


DEFAULT_LEXEMES: List[str] = ["laukaz", "milkiz"]


DIPHTHONGS = ("ai", "au", "eu", "iu")
PROTO_SOURCE_CANDIDATES = ("fsts/germanic.txt", "server/fsts/germanic.txt")
TOKEN_PATTERN = re.compile(r"(?P<src>\{[^}]+\}|[^{}\s|]+):\{\*(?P<dst>[^}]+)\}")


def run_foma(script: str, *, cwd: Path) -> subprocess.CompletedProcess:
    """Execute a small Foma program."""

    return subprocess.run(
        ["foma", "-q"],
        input=script.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        check=True,
    )


def compile_stage_binaries(stages: Iterable[str], tmpdir: Path, *, cwd: Path) -> None:
    lines = ["set verbose-type none;", "source fsts/germanic.txt"]
    for stage in stages:
        target = tmpdir / f"{stage.lower()}.bin"
        lines.append(f"regex {stage};")
        lines.append(f"save stack {target}")
    lines.append("quit")
    script = "\n".join(lines)
    result = run_foma(script, cwd=cwd)
    if result.stderr:
        sys.stderr.buffer.write(result.stderr)


def flookup(stage_bin: Path, lexemes: Iterable[str], *, cwd: Path) -> List[str]:
    proc = subprocess.run(
        ["flookup", str(stage_bin)],
        input="\n".join(lexemes).encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd,
        check=True,
    )
    if proc.stderr:
        sys.stderr.buffer.write(proc.stderr)
    # ``flookup`` echoes "<input>\t<output>" per line, blank line between items.
    return proc.stdout.decode("utf-8").strip().splitlines()


def foma_apply_down(stage: str, lexemes: Iterable[str], *, cwd: Path) -> List[str]:
    lines: List[str] = [
        "set verbose-type none;",
        "source fsts/germanic.txt",
        f"regex {stage};",
    ]
    for lexeme in lexemes:
        lines.append(f"apply down {lexeme}")
    lines.append("quit")
    result = run_foma("\n".join(lines), cwd=cwd)
    outputs = []
    for raw in result.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        if raw.startswith("Foma,") or raw.startswith("Copyright"):
            continue
        if raw.startswith("This is free") or raw.startswith("Type \"help"):
            continue
        if raw.startswith("foma[") or raw.startswith("regex"):
            continue
        outputs.append(raw)
    return outputs


def maybe_brace(lexeme: str) -> str:
    # Minimal helper: wrap core proto diphthongs so callers can trace plain
    # ``laukaz`` as ``l{au}kaz`` when requested.
    out = lexeme
    for diph in DIPHTHONGS:
        out = out.replace(diph, f"{{{diph}}}")
    return out


def _strip_braces(token: str) -> str:
    if token.startswith("{") and token.endswith("}"):
        return token[1:-1]
    return token


def _find_proto_source(workdir: Path) -> Path:
    for candidate in PROTO_SOURCE_CANDIDATES:
        path = workdir / candidate
        if path.exists():
            return path
    raise FileNotFoundError(
        f"Unable to locate germanic.txt relative to {workdir}; tried {', '.join(PROTO_SOURCE_CANDIDATES)}"
    )


@lru_cache(maxsize=None)
def load_proto_inventory(workdir: Path) -> Tuple[Dict[str, str], List[str]]:
    source = _find_proto_source(workdir)
    text = source.read_text(encoding="utf-8")
    mapping: Dict[str, str] = {}
    for match in TOKEN_PATTERN.finditer(text):
        src = _strip_braces(match.group("src"))
        dst = match.group("dst")
        if not src or src == "0":
            continue
        mapping.setdefault(src, f"{{*{dst}}}")
    # Sort keys longest-first so diphthongs win before single vowels.
    key_order = sorted(mapping.keys(), key=len, reverse=True)
    return mapping, key_order


def _map_locked_segment(segment: str, mapping: Dict[str, str]) -> str:
    if not segment:
        return ""
    if segment.startswith("*"):
        return f"{{{segment}}}"
    if segment in mapping:
        return mapping[segment]
    raise ValueError(f"Unknown proto segment '{segment}' in brace block")


def normalize_plain_lexeme(lexeme: str, mapping: Dict[str, str], key_order: List[str]) -> str:
    if "{*" in lexeme:
        return lexeme
    tokens: List[str] = []
    i = 0
    while i < len(lexeme):
        if lexeme[i] == "{":
            end = lexeme.find("}", i + 1)
            if end == -1:
                segment = lexeme[i]
                i += 1
            else:
                segment = lexeme[i + 1 : end]
                i = end + 1
            tokens.append(_map_locked_segment(segment, mapping))
            continue

        matched = None
        for key in key_order:
            if lexeme.startswith(key, i):
                matched = key
                break
        if matched is None:
            raise ValueError(f"No proto mapping for segment starting at '{lexeme[i:]}'")
        tokens.append(mapping[matched])
        i += len(matched)
    return "".join(tokens)


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lexeme",
        action="append",
        dest="lexemes",
        help="Lexeme to trace (may be repeated).",
    )
    parser.add_argument(
        "--file",
        type=Path,
        help="Read additional lexemes from a newline-delimited file.",
    )
    parser.add_argument(
        "--stage",
        action="append",
        dest="stages",
        help="Stage to include (may be repeated). Defaults to the full cascade.",
    )
    parser.add_argument(
        "--apply-down",
        action="store_true",
        help="Use foma apply down instead of flookup so we see stage outputs even when the transducer rejects.",
    )
    parser.add_argument(
        "--brace-diphthongs",
        action="store_true",
        help="Wrap ai/au/eu/iu in braces before tracing (useful for plain inputs).",
    )
    parser.add_argument(
        "--normalize-plain",
        action="store_true",
        help="Map plain proto strings into the brace/star alphabet using pgrmWord.",
    )
    parser.add_argument(
        "--workdir",
        type=Path,
        default=Path("."),
        help="Working directory containing fsts/germanic.txt (default: repo root).",
    )
    return parser.parse_args(list(argv))


def collect_lexemes(args: argparse.Namespace, *, workdir: Path) -> List[str]:
    lexemes: List[str] = []
    if args.lexemes:
        lexemes.extend(args.lexemes)
    if args.file:
        lexemes.extend(
            line.strip() for line in args.file.read_text(encoding="utf-8").splitlines() if line.strip()
        )
    if not lexemes:
        lexemes.extend(DEFAULT_LEXEMES)
    if args.brace_diphthongs:
        lexemes = [maybe_brace(lex) for lex in lexemes]
    if args.normalize_plain:
        mapping, key_order = load_proto_inventory(workdir)
        lexemes = [normalize_plain_lexeme(lex, mapping, key_order) for lex in lexemes]
    return lexemes


def main(argv: Iterable[str]) -> int:
    args = parse_args(argv)
    stages = args.stages if args.stages else DEFAULT_STAGES
    workdir = args.workdir.resolve()
    lexemes = collect_lexemes(args, workdir=workdir)
    if not lexemes:
        print("No lexemes provided.", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="german_stages_") as tmp:
        tmp_path = Path(tmp)
        compile_stage_binaries(stages, tmp_path, cwd=workdir)
        for stage in stages:
            bin_path = tmp_path / f"{stage.lower()}.bin"
            if not bin_path.exists():
                print(f"[warn] stage {stage} missing binary", file=sys.stderr)
                continue
            print(f"== {stage} ==")
            if args.apply_down:
                outputs = foma_apply_down(stage, lexemes, cwd=workdir)
            else:
                outputs = flookup(bin_path, lexemes, cwd=workdir)
            if not outputs:
                print("  (no output)\n")
                continue
            for line in outputs:
                if not line:
                    continue
                print(f"  {line}")
            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
