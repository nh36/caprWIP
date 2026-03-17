#!/usr/bin/env python3
"""Check that OE FST bins are fresh and mutually in sync."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable, List, Tuple
import importlib.util


def _load_stage_bins(module_path: Path) -> List[str]:
    spec = importlib.util.spec_from_file_location("oe_full_trace_report", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load stages from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[call-arg]
    stages = getattr(module, "STAGES", [])
    return [bin_name for _label, bin_name in stages]


def _format_age(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.1f}s"
    if seconds < 3600:
        return f"{seconds / 60:.1f}m"
    if seconds < 86400:
        return f"{seconds / 3600:.1f}h"
    return f"{seconds / 86400:.1f}d"


def _collect_missing(paths: Iterable[Path]) -> List[Path]:
    return [path for path in paths if not path.exists()]


def _mtime(path: Path) -> float:
    return path.stat().st_mtime


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify OE bins exist, are fresh relative to FST sources, and are mutually synced."
    )
    parser.add_argument(
        "--repo-root",
        help="Override repo root (default: inferred from this script)",
    )
    parser.add_argument(
        "--bin-dir",
        help="Directory containing OE bins (default: <repo>/server)",
    )
    parser.add_argument(
        "--fsts-dir",
        help="Directory containing OE FST sources (default: <repo>/server/fsts)",
    )
    parser.add_argument(
        "--max-skew-seconds",
        type=int,
        default=3600,
        help="Max allowed mtime skew between main and sandbox bins (default: %(default)s)",
    )
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="Warn instead of failing when bins are missing or stale",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    if args.repo_root:
        candidate = Path(args.repo_root).expanduser().resolve()
        server_root = candidate / "server" if (candidate / "server").exists() else candidate
    else:
        server_root = script_dir.parent

    bin_dir = Path(args.bin_dir).expanduser().resolve() if args.bin_dir else server_root

    if args.fsts_dir:
        fsts_dir = Path(args.fsts_dir).expanduser().resolve()
    else:
        candidate = bin_dir / "fsts"
        fsts_dir = candidate if candidate.exists() else server_root / "fsts"

    germanic_txt = fsts_dir / "germanic.txt"
    sandbox_txt = fsts_dir / "old_english_sandbox.txt"
    oe_bin = bin_dir / "old_english.bin"

    stage_module = script_dir / "oe_full_trace_report.py"
    stage_bins = _load_stage_bins(stage_module)
    sandbox_bins = [bin_dir / name for name in stage_bins]

    issues: List[str] = []
    notes: List[str] = []

    missing = _collect_missing([germanic_txt, sandbox_txt])
    if missing:
        issues.append("Missing FST source files:")
        issues.extend(f"  - {path}" for path in missing)

    missing_bins = _collect_missing([oe_bin])
    missing_bins.extend(_collect_missing(sandbox_bins))
    if missing_bins:
        issues.append("Missing OE bin files:")
        issues.extend(f"  - {path}" for path in missing_bins)

    if not missing and not missing_bins:
        germanic_mtime = _mtime(germanic_txt)
        sandbox_mtime = _mtime(sandbox_txt)
        if _mtime(oe_bin) < germanic_mtime:
            issues.append(
                "old_english.bin is older than germanic.txt "
                f"({_format_age(germanic_mtime - _mtime(oe_bin))} behind)."
            )

        stale_sandbox = [
            path
            for path in sandbox_bins
            if _mtime(path) < sandbox_mtime
        ]
        if stale_sandbox:
            issues.append("Sandbox bins older than old_english_sandbox.txt:")
            issues.extend(f"  - {path.name}" for path in stale_sandbox)

        surface_bin = bin_dir / "old_english_sandbox_after_surface.bin"
        if surface_bin.exists():
            skew = abs(_mtime(surface_bin) - _mtime(oe_bin))
            if skew > args.max_skew_seconds:
                issues.append(
                    "old_english.bin and sandbox surface bin are out of sync "
                    f"(skew {_format_age(skew)} > {_format_age(args.max_skew_seconds)})."
                )
        else:
            notes.append("Surface bin missing; skipping cross-bin skew check.")

    if issues:
        print("OE bin sync check failed:")
        for line in issues:
            print(line)
        if notes:
            for line in notes:
                print(line)
        print("Next step: rebuild bins via: bash server/tools/rebuild_oe_bins.sh")
        if args.warn_only:
            print("Continuing because --warn-only was set.")
            return 0
        return 2

    print("OE bin sync check OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
