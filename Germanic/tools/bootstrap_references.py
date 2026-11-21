#!/usr/bin/env python3
"""Provision checksum-pinned private references without changing Git or evidence."""

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[2]
REFERENCES = Path("docs/references")
SURVEY = Path("Germanic/docs/lexeme_reports/pgmc_reconstructions/survey_provenance.json")


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)


def registered(root, keys, survey):
    pins = {}

    def add(path, digest):
        relative = Path(path)
        if (not relative.is_relative_to(REFERENCES) or ".." in relative.parts
                or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ValueError(f"invalid holding path or SHA-256: {path}")
        if pins.setdefault(relative, digest) != digest:
            raise ValueError(f"conflicting registered SHA-256: {path}")

    found = set()
    if keys:
        for ledger in sorted((root / REFERENCES).glob("*/holdings.tsv")):
            with ledger.open(encoding="utf-8", newline="") as stream:
                for row in csv.DictReader(stream, delimiter="\t"):
                    key = row.get("citation_key")
                    if key in keys and row.get("pdf_path"):
                        add(row["pdf_path"], row.get("pdf_sha256") or "")
                        found.add(key)
        if missing := set(keys) - found:
            raise ValueError(f"no pinned PDF registration for {', '.join(sorted(missing))}")
    if survey:
        data = json.loads((root / SURVEY).read_text())
        for field in ("inputs", "historical_unavailable_inputs"):
            for path, digest in data.get(field, {}).items():
                if Path(path).is_relative_to(REFERENCES):
                    add(path, digest or "")
    return pins


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def provision(root, relative, expected, origins):
    target = root / relative
    if target.resolve() != target:
        raise ValueError(f"{relative}: destination must not traverse a symlink")
    if target.exists():
        if not target.is_file() or digest(target) != expected:
            raise ValueError(f"{relative}: destination is not the registered file (expected {expected})")
        return False
    if git(root, "check-ignore", "--", str(relative)).returncode:
        raise ValueError(f"{relative}: refusing to provision a path that is not Git-ignored")
    candidates = [origin / relative for origin in origins]
    if not (source := next((path for path in candidates if path.is_file()), None)):
        raise ValueError(f"{relative}: registered original missing; checked "
                         + ", ".join(map(str, candidates)))

    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".capr-reference-", dir=target.parent) as scratch:
        copy = Path(scratch) / "original"
        shutil.copyfile(source, copy)
        copy.chmod(0o600)
        if digest(copy) != expected:
            raise ValueError(f"{source}: SHA-256 mismatch (expected {expected})")
        os.link(copy, target)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("keys", nargs="*", help="citation keys in the holdings ledgers")
    parser.add_argument("--survey", action="store_true", help="include all pinned survey holdings")
    parser.add_argument("--checkout", type=Path, default=ROOT)
    parser.add_argument("--main-checkout", type=Path, help="override the main Git checkout")
    parser.add_argument("--cache", type=Path, default=Path.home() / ".cache/capr/references",
                        help="private cache mirroring repo-relative paths")
    args = parser.parse_args()
    if not (args.keys or args.survey):
        parser.error("specify at least one citation key or --survey")
    root = args.checkout.resolve()
    top = git(root, "rev-parse", "--show-toplevel")
    if top.returncode or Path(top.stdout.strip()) != root:
        parser.error("--checkout must name a Git worktree root")
    common = git(root, "rev-parse", "--git-common-dir").stdout.strip()
    main_checkout = (args.main_checkout or (root / common).resolve().parent).resolve()
    try:
        copied = 0
        failures = []
        pins = registered(root, args.keys, args.survey)
        for relative, expected in pins.items():
            try:
                copied += provision(root, relative, expected, (main_checkout, args.cache.resolve()))
            except (ValueError, OSError) as exc:
                failures.append(str(exc))
        if failures:
            parser.exit(1, "\n".join(failures) + "\n")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")
    print(f"Verified {len(pins)} registered holdings; copied {copied}. No source inspection performed.")


if __name__ == "__main__":
    main()
