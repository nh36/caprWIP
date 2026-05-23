#!/usr/bin/env python3
"""Manifest-driven batch runner for first-break order-sensitivity tests."""

from __future__ import annotations

import argparse
import csv
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

from sound_change_order_sensitivity import FIRST_BREAK_DONE_RESULTS, read_tsv_rows


TOOLS_DIR = Path(__file__).resolve().parent
GERMANIC_DIR = TOOLS_DIR.parent
RUNNER_PATH = TOOLS_DIR / "sound_change_order_sensitivity.py"
DEFAULT_MANIFEST = (
    GERMANIC_DIR
    / "docs"
    / "sound_changes"
    / "order_tests"
    / "summaries"
    / "order_sensitivity_first_break_batch_04_manifest.tsv"
)
DEFAULT_SUMMARY = (
    GERMANIC_DIR
    / "docs"
    / "sound_changes"
    / "order_tests"
    / "summaries"
    / "order_sensitivity_first_break_pilot_03.tsv"
)
DEFAULT_LOG_DIR = GERMANIC_DIR / "docs" / "sound_changes" / "order_tests" / "logs"

SKIP_STATUSES = {"done", "skipped"}
ACTIVE_STATUSES = {"pending", "queued", "partial", "error"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST))
    parser.add_argument("--summary-output", default=str(DEFAULT_SUMMARY))
    parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--change", help="Run only one change_id from the manifest")
    parser.add_argument("--only-status", help="Filter manifest rows by runner_status before execution")
    parser.add_argument("--direction", choices=("earlier", "later", "both"), default="both")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--sleep-seconds", type=float, default=0.5)
    parser.add_argument("--stop-on-error", action="store_true")
    return parser.parse_args()


def read_manifest(path: Path) -> Tuple[List[str], List[Dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise RuntimeError(f"Manifest {path} is missing a header row")
        return list(reader.fieldnames), list(reader)


def write_manifest(fieldnames: Sequence[str], rows: Sequence[Dict[str, str]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: str(row.get(field, "")) for field in fieldnames})


def requested_directions(direction: str) -> Tuple[str, ...]:
    return ("earlier", "later") if direction == "both" else (direction,)


def infer_runner_status(row: Dict[str, str]) -> str:
    earlier = row.get("earlier_status", "")
    later = row.get("later_status", "")
    statuses = [earlier, later]
    if all(status == "skipped" for status in statuses):
        return "skipped"
    if all(status in {"done", "skipped"} for status in statuses):
        return "done"
    if any(status == "running" for status in statuses):
        return "running"
    if any(status == "error" for status in statuses):
        return "error"
    if any(status == "done" for status in statuses):
        return "partial"
    if all(status == "pending" for status in statuses):
        return "pending"
    if any(status == "pending" for status in statuses):
        return "pending"
    if all(status == "queued" for status in statuses):
        return "queued"
    return row.get("runner_status", "queued")


def build_runner_command(change_id: str, direction: str, resume: bool) -> List[str]:
    command = [
        sys.executable,
        str(RUNNER_PATH),
        "--mode",
        "first-break",
        "--change",
        change_id,
        "--direction",
        direction,
    ]
    if resume:
        command.append("--resume")
    return command


def append_log(log_path: Path, command: Sequence[str], proc: subprocess.CompletedProcess[str]) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] COMMAND: {shlex.join(command)}\n")
        handle.write(f"[{timestamp}] EXIT_CODE: {proc.returncode}\n")
        if proc.stdout:
            handle.write("[stdout]\n")
            handle.write(proc.stdout)
            if not proc.stdout.endswith("\n"):
                handle.write("\n")
        if proc.stderr:
            handle.write("[stderr]\n")
            handle.write(proc.stderr)
            if not proc.stderr.endswith("\n"):
                handle.write("\n")
        handle.write("\n")


def find_terminal_summary(summary_path: Path, change_id: str, direction: str) -> Dict[str, str] | None:
    for row in read_tsv_rows(summary_path):
        if row.get("change_id") == change_id and row.get("direction") == direction:
            if row.get("result") in FIRST_BREAK_DONE_RESULTS:
                return row
    return None


def select_rows(rows: Sequence[Dict[str, str]], args: argparse.Namespace) -> List[Dict[str, str]]:
    selected: List[Dict[str, str]] = []
    for row in rows:
        if args.change and row.get("change_id") != args.change:
            continue
        if args.only_status and row.get("runner_status") != args.only_status:
            continue
        if args.resume and row.get("runner_status") in SKIP_STATUSES:
            continue
        selected.append(row)
        if args.limit is not None and len(selected) >= args.limit:
            break
    return selected


def relative_log_path(log_path: Path) -> str:
    try:
        return str(log_path.relative_to(GERMANIC_DIR))
    except ValueError:
        return str(log_path)


def main() -> None:
    args = parse_args()
    manifest_path = Path(args.manifest).expanduser().resolve()
    summary_path = Path(args.summary_output).expanduser().resolve()
    log_dir = Path(args.log_dir).expanduser().resolve()
    fieldnames, rows = read_manifest(manifest_path)
    target_rows = select_rows(rows, args)

    if args.change and not any(row.get("change_id") == args.change for row in rows):
        raise SystemExit(f"{args.change} not found in manifest {manifest_path}")

    if not target_rows:
        print("No manifest rows matched the requested filters.")
        return

    total_changes = 0
    for row in target_rows:
        change_id = row["change_id"]
        directions = requested_directions(args.direction)
        print(f"{change_id} runner_status={row.get('runner_status','-')} priority={row.get('priority','-')}")
        total_changes += 1

        for direction in directions:
            status_field = f"{direction}_status"
            current_status = row.get(status_field, "")
            if current_status == "skipped":
                print(f"  {direction}: skipped by manifest")
                continue
            if args.resume and current_status in SKIP_STATUSES:
                print(f"  {direction}: already {current_status}")
                continue

            command = build_runner_command(change_id, direction, args.resume)
            log_path = log_dir / f"{change_id}_{direction}.log"

            if args.dry_run:
                print(f"  DRY_RUN {shlex.join(command)}")
                continue

            row[status_field] = "running"
            row["runner_status"] = "running"
            row["notes"] = f"Running {direction}; log {relative_log_path(log_path)}"
            write_manifest(fieldnames, rows, manifest_path)

            proc = subprocess.run(
                command,
                cwd=GERMANIC_DIR,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            append_log(log_path, command, proc)

            summary_row = find_terminal_summary(summary_path, change_id, direction)
            if proc.returncode == 0 and summary_row is not None:
                row[status_field] = "done"
                row["notes"] = (
                    f"{direction} complete via {relative_log_path(log_path)}; "
                    f"summary result={summary_row['result']}"
                )
                print(f"  {direction}: done ({summary_row['result']})")
            else:
                row[status_field] = "error"
                row["notes"] = f"{direction} failed; inspect {relative_log_path(log_path)}"
                print(f"  {direction}: error")

            row["runner_status"] = infer_runner_status(row)
            write_manifest(fieldnames, rows, manifest_path)

            if proc.returncode != 0 and args.stop_on_error:
                raise SystemExit(proc.returncode)
            if proc.returncode != 0:
                break
            if args.sleep_seconds > 0:
                time.sleep(args.sleep_seconds)

    if args.dry_run:
        print(f"Dry run listed {len(target_rows)} change(s).")
    else:
        print(f"Processed {total_changes} change(s); manifest updated at {manifest_path}.")


if __name__ == "__main__":
    main()
