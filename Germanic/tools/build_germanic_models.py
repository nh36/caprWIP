#!/usr/bin/env python3
"""Build and verify the selectable application binaries inside the backend."""
import argparse
import json
import os
import tempfile
from pathlib import Path

from sc047_models import MODELS, run, sha
from capr_runtime import layout

CONTROLS = ("sáiwalōi", "sáiwalôi", "bádjamiz", "fánją", "fánjai", "fánjas",
            "fánjō", "wígjaz", "wígją", "wígjai", "wígjas", "wígjô", "bázjas",
            "gakáwiθi", "gakáwid")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", choices=(*MODELS, "both"), default="both")
    args = parser.parse_args()
    models = tuple(MODELS) if args.model == "both" else (args.model,)
    output = layout().bin_dir / "germanic-model-bins"
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output) as temporary:
        directory = Path(temporary)
        result = run(models, CONTROLS, active=True, binaries=directory)
        for name in ("english.bin", "german.bin", "dutch.bin", "old_english.bin"):
            os.replace(directory / name, output / name)
        for model in models:
            binary = directory / f"old_english_{model}.bin"
            receipt = binary.with_suffix(".json")
            receipt.write_text(json.dumps({
                "fst_sha256": result["fst_sha256"],
                "runner_sha256": result["runner_sha256"],
                "bin_sha256": sha(binary),
            }) + "\n", encoding="utf-8")
            os.replace(binary, output / binary.name)
            os.replace(receipt, output / receipt.name)
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
