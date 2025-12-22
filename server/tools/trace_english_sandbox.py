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
    ("Palatalisation", "english_sandbox_after_palatalisation.bin"),
    ("ConsonantRules", "english_sandbox_after_consonant_rules.bin"),
    ("WestGermanic", "english_sandbox_after_west_germanic.bin"),
    ("OpenLengthening", "english_sandbox_after_open_lengthening.bin"),
    ("BreakingLengthening", "english_sandbox_after_breaking_lengthening.bin"),
    ("LiquidLowering", "english_sandbox_after_liquid_lowering.bin"),
    ("VelarShortening", "english_sandbox_after_velar_shortening.bin"),
    ("UrRounding", "english_sandbox_after_ur_rounding.bin"),
    ("WeakTailMarker", "english_sandbox_after_weak_tail_marker.bin"),
    ("ProtoToOE", "english_sandbox_after_proto_to_oe.bin"),
    ("WGlide", "english_sandbox_after_w_glide.bin"),
    ("GhMarker", "english_sandbox_after_gh_marker.bin"),
    ("GlideDeletion", "english_sandbox_after_glide_deletion.bin"),
    ("ShortAFronting", "english_sandbox_after_short_a_fronting.bin"),
    ("ProtoRhoticFronting", "english_sandbox_after_proto_rhotic_fronting.bin"),
    ("RhoticBreaking", "english_sandbox_after_rhotic_breaking.bin"),
    ("ShortBackLowering", "english_sandbox_after_short_back_lowering.bin"),
    ("ShortVowelSplit", "english_sandbox_after_short_vowel_split.bin"),
    ("RhoticColoring", "english_sandbox_after_rhotic_coloring.bin"),
    ("VowelRules", "english_sandbox_after_vowel_rules.bin"),
    ("PostVocalicRLoss", "english_sandbox_after_postvocalic_r_loss.bin"),
    ("WeakTailReductions", "english_sandbox_after_weak_tail.bin"),
    ("WeakTailCleanup", "english_sandbox_after_weak_tail_cleanup.bin"),
    ("SilentInitialCleanup", "english_sandbox_after_silent_cleanup.bin"),
    ("GhDeletion", "english_sandbox_after_gh_deletion.bin"),
    ("Orthography", "english_sandbox_after_orthography.bin"),
    ("Surface", "english_sandbox_after_surface.bin"),
]

DIPHTHONGS = ("ai", "au", "eu", "iu")


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


def maybe_brace_diphthongs(raw: str) -> str:
    wrapped = raw
    for diph in DIPHTHONGS:
        wrapped = wrapped.replace(diph, f"{{{diph}}}")
    return wrapped


PROTO_STRIP_RE = re.compile(r"[{}*\s\-/()]")


def normalize_proto_input(raw: str) -> str:
    """Collapse braces/stars plus proto punctuation before feeding flookup."""
    return PROTO_STRIP_RE.sub("", raw)


def iter_lexemes(args: argparse.Namespace) -> List[str]:
    entries: List[str] = []
    if args.lexeme:
        entries.extend(args.lexeme)
    if args.lexeme_file:
        path = Path(args.lexeme_file).expanduser()
        if not path.exists():
            raise FileNotFoundError(f"Lexeme file not found: {path}")
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            entries.append(line)
    if not entries:
        raise SystemExit("Provide at least one --lexeme or --lexeme-file entry")
    return entries


def collect_stage_outputs(lexeme: str, bin_dir: Path) -> List[Tuple[str, List[str]]]:
    plain = normalize_proto_input(lexeme)
    return [(label, run_stage(bin_dir, bin_name, plain)) for label, bin_name in STAGES]


def trace_lexeme(lexeme: str, bin_dir: Path, brace_diphthongs: bool) -> List[str]:
    header = maybe_brace_diphthongs(lexeme) if brace_diphthongs else lexeme
    lines = [f"=== {header} ==="]
    for label, outputs in collect_stage_outputs(lexeme, bin_dir):
        pretty = ", ".join(outputs)
        lines.append(f"{label}: {pretty}")
    lines.append("")
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Trace English sandbox stages for given lexemes.")
    parser.add_argument("--lexeme", action="append", help="Proto lexeme (brace or plain form)")
    parser.add_argument("--lexeme-file", help="Path to a file containing one proto lexeme per line")
    parser.add_argument(
        "--brace-diphthongs",
        action="store_true",
        help="Wrap ai/au/eu/iu sequences with braces in the log header for readability",
    )
    parser.add_argument(
        "--bin-dir",
        default=None,
        help="Directory containing english_sandbox_after_*.bin (defaults to <repo>/server)",
    )
    parser.add_argument(
        "--save-log",
        help="Write the tracer output to this file in addition to stdout",
    )
    args = parser.parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    if args.bin_dir:
        bin_dir = Path(args.bin_dir).expanduser().resolve()
    else:
        server_dir = repo_root / "server"
        bin_dir = server_dir.resolve() if server_dir.exists() else repo_root
    lexemes = iter_lexemes(args)
    all_lines: List[str] = []
    for lex in lexemes:
        section = trace_lexeme(lex, bin_dir, args.brace_diphthongs)
        all_lines.extend(section)
        print("\n".join(section))
    if args.save_log:
        Path(args.save_log).expanduser().write_text("\n".join(all_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
