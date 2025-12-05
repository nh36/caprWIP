#!/usr/bin/env python3
"""Stage-by-stage tracer for the English sandbox cascade.

Run this inside the backend container (or any environment where the staged
`english_sandbox_after_*.bin` files exist under `server/`):

    docker compose exec backend bash -lc \
        "cd /usr/app && python3 server/tools/trace_english_sandbox.py --lexeme '{*fiskaz}'"

Use ``--bin-dir`` if the binaries live outside the repo root.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

STAGES: Sequence[Tuple[str, str]] = [
    ("ProtoInput", "english_sandbox_after_proto_input.bin"),
    ("InitialKn", "english_sandbox_after_initial_kn.bin"),
    ("ConsonantRules", "english_sandbox_after_consonant_rules.bin"),
    ("GhMarker", "english_sandbox_after_gh_marker.bin"),
    ("GlideDeletion", "english_sandbox_after_glide_deletion.bin"),
    ("WestGermanic", "english_sandbox_after_west_germanic.bin"),
    ("OpenLengthening", "english_sandbox_after_open_lengthening.bin"),
    ("BreakingLengthening", "english_sandbox_after_breaking_lengthening.bin"),
    ("VowelRules", "english_sandbox_after_vowel_rules.bin"),
    ("PostVocalicRLoss", "english_sandbox_after_postvocalic_r_loss.bin"),
    ("WeakTailReductions", "english_sandbox_after_weak_tail.bin"),
    ("SilentInitialCleanup", "english_sandbox_after_silent_cleanup.bin"),
    ("GhDeletion", "english_sandbox_after_gh_deletion.bin"),
    ("Orthography", "english_sandbox_after_orthography.bin"),
    ("Surface", "english_sandbox_after_surface.bin"),
]


def dedupe_preserve(seq: Iterable[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for item in seq:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def run_stage(bin_dir: Path, bin_name: str, form: str) -> List[str]:
    stage_path = (bin_dir / bin_name).resolve()
    if not stage_path.exists():
        raise FileNotFoundError(f"Missing stage binary: {stage_path}")
    proc = subprocess.run(
        ["flookup", "-i", str(stage_path)],
        input=f"{form}\n".encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    if proc.stderr:
        sys.stderr.buffer.write(proc.stderr)
    outputs: List[str] = []
    for raw in proc.stdout.decode("utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        if "\t" in raw:
            _, output = raw.split("\t", 1)
        else:
            output = raw
        outputs.append(output or "+?")
    if not outputs:
        outputs.append("+?")
    return dedupe_preserve(outputs)


def normalize_proto_input(raw: str) -> str:
    return re.sub(r"[{}*\s]", "", raw)


def trace_lexeme(lexeme: str, bin_dir: Path) -> None:
    print(f"=== {lexeme} ===")
    plain = normalize_proto_input(lexeme)
    for label, bin_name in STAGES:
        outputs = run_stage(bin_dir, bin_name, plain)
        pretty = ", ".join(outputs)
        print(f"{label}: {pretty}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Trace English sandbox stages for given lexemes.")
    parser.add_argument("--lexeme", action="append", required=True, help="Proto lexeme (brace form)")
    parser.add_argument(
        "--bin-dir",
        default=None,
        help="Directory containing english_sandbox_after_*.bin (defaults to <repo>/server)",
    )
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    if args.bin_dir:
        bin_dir = Path(args.bin_dir).expanduser().resolve()
    else:
        server_dir = repo_root / "server"
        bin_dir = server_dir.resolve() if server_dir.exists() else repo_root
    for lex in args.lexeme:
        trace_lexeme(lex, bin_dir)


if __name__ == "__main__":
    main()
