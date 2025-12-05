#!/usr/bin/env python3
"""Annotate english_sandbox_results entries with stage-by-stage info."""

import argparse
import importlib.util
import json
from pathlib import Path
from typing import List, Optional

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_BIN_DIR = SCRIPT_DIR.parent


def load_trace_helper():
    tracer_path = SCRIPT_DIR / "trace_english_sandbox.py"
    spec = importlib.util.spec_from_file_location("trace_english_sandbox", tracer_path)
    if not spec or not spec.loader:
        raise RuntimeError("Unable to load trace_english_sandbox module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


collect_stage_outputs = load_trace_helper().collect_stage_outputs


def resolve_bin_dir(arg: Optional[str]) -> Path:
    if arg:
        return Path(arg).expanduser().resolve()
    return DEFAULT_BIN_DIR.resolve()


def annotate(entries: List[dict], bin_dir: Path) -> List[dict]:
    for row in entries:
        proto = row.get("proto")
        if not proto:
            row["stage_outputs"] = []
            row["first_failing_stage"] = None
            continue
        stage_data = collect_stage_outputs(proto, bin_dir)
        row["stage_outputs"] = [
            {"stage": stage, "outputs": outputs} for stage, outputs in stage_data
        ]
        row["first_failing_stage"] = next(
            (stage for stage, outputs in stage_data if outputs == ["+?"]),
            None,
        )
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Attach tracer stage info to english_sandbox_results JSON",
    )
    parser.add_argument(
        "--input",
        default="tmp/english_sandbox_results_current.json",
        help="Path to the base sandbox results JSON (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default="tmp/english_sandbox_results_with_stages.json",
        help="Destination for annotated JSON (default: %(default)s)",
    )
    parser.add_argument(
        "--bin-dir",
        help="Directory containing english_sandbox_after_*.bin (defaults to repo/server)",
    )
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    bin_dir = resolve_bin_dir(args.bin_dir)

    data = json.loads(input_path.read_text(encoding="utf-8"))
    annotated = annotate(data, bin_dir)
    output_path.write_text(
        json.dumps(annotated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
