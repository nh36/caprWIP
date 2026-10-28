#!/usr/bin/env python3
"""Stage this research and its clean base in a private backend directory."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import subprocess
from pathlib import Path

BASE = "3cb109c981c8868bf383172e2be06cdc88c00fb0"
RESEARCH = "Germanic/docs/sound_changes/audits/rainbow-earthly-secondary-stress"


def command(args, **kwargs):
    return subprocess.run(args, check=True, **kwargs)


def protected(root):
    files = subprocess.check_output(
        ["git", "-C", str(root), "ls-tree", "-r", "--name-only", BASE],
        text=True).splitlines()
    return {
        name: hashlib.sha256((root / name).read_bytes()).hexdigest()
        for name in files if (root / name).is_file()
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--container", default="capr-backend-1")
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("results.json.gz"))
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    root = Path(subprocess.check_output(
        ["git", "-C", str(here), "rev-parse", "--show-toplevel"],
        text=True).strip())
    command(["git", "-C", str(root), "diff", "--exit-code", BASE, "--", ".",
             f":(exclude){RESEARCH}"], stdout=subprocess.DEVNULL)
    if subprocess.check_output(
        ["docker", "inspect", "-f", "{{.State.Running}}", args.container],
        text=True).strip() != "true":
        raise RuntimeError("Backend container is not running.")
    before = protected(root)
    private = subprocess.check_output(
        ["docker", "exec", args.container, "mktemp", "-d",
         "/tmp/capr-secondary-repro-XXXXXXXX"], text=True).strip()
    if not private.startswith("/tmp/capr-secondary-repro-") or "/" in private[5:]:
        raise RuntimeError("Unexpected private directory: " + private)
    try:
        archive = subprocess.check_output([
            "git", "-C", str(root), "archive", BASE,
            "Germanic/tools", "Germanic/fsts", "Germanic/data",
            "Germanic/docs/sound_changes/registry",
            "Germanic/docs/sound_changes/cascade_baseline",
            "backend/oe_input_context.py", "backend/compare_fst.py",
        ])
        command(["docker", "exec", "-i", args.container,
                 "tar", "xf", "-", "-C", private], input=archive)
        command([
            "docker", "exec", args.container, "python3", "-c",
            "import pathlib,shutil,sys; p=pathlib.Path(sys.argv[1]); "
            "[(shutil.copy2(p/'backend'/n,p/'Germanic'/n)) "
            "for n in ('oe_input_context.py','compare_fst.py')]; "
            "(p/'Germanic/docs/sound_changes/audits').mkdir(exist_ok=True)",
            private,
        ])
        command([
            "docker", "cp", str(here),
            f"{args.container}:{private}/Germanic/docs/sound_changes/audits/",
        ])
        command([
            "docker", "exec", args.container, "python3",
            f"{private}/{RESEARCH}/experiment.py", "--output",
            f"{private}/results.json.gz",
        ])
        command([
            "docker", "exec", args.container, "python3",
            f"{private}/{RESEARCH}/experiment.py", "--functionality-only",
            "--output", f"{private}/functionality.json.gz",
        ])
        command(["docker", "cp", f"{args.container}:{private}/results.json.gz",
                 str(args.output.resolve())])
        command(["docker", "cp", f"{args.container}:{private}/functionality.json.gz",
                 str(args.output.with_name("functionality.json.gz").resolve())])
    finally:
        command([
            "docker", "exec", args.container, "python3", "-c",
            "import pathlib,shutil,sys; p=pathlib.Path(sys.argv[1]); "
            "assert p.parent==pathlib.Path('/tmp') "
            "and p.name.startswith('capr-secondary-repro-'); shutil.rmtree(p)",
            private,
        ])
        if before != protected(root):
            raise RuntimeError("Tracked production bytes changed in the research worktree.")
    with gzip.open(args.output, "rt") as handle:
        receipt = json.load(handle)
    print(json.dumps({
        "base_commit": receipt["base_commit"],
        "production_unchanged": receipt["production_unchanged"],
        "models": {
            name: dict(result["counts"], changed_ids=[
                delta["row_id"] for delta in result["final_deltas"]])
            for name, result in receipt["models"].items()},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
