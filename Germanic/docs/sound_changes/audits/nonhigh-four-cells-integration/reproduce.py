#!/usr/bin/env python3
"""Replay a pinned blocked integration diagnosis inside the backend container."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "Germanic/tools").is_dir())
sys.path.insert(0, str(ROOT / "Germanic/tools"))

BOOTSTRAP = """
import json,shutil,sys,tempfile,subprocess
from pathlib import Path
src=Path(sys.argv[1]);mapping=json.loads((src/'layout.json').read_text())
root=Path(tempfile.mkdtemp(prefix='capr_parser_replay_source_'))
try:
 for label,relative in mapping.items():
  files=list(src.glob(label+'.*'))
  if len(files)!=1:raise RuntimeError('invalid pinned input: '+label)
  dest=root/relative;dest.parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(files[0],dest)
 for name in ('compare_fst.py','oe_input_context.py'):
  shutil.copyfile(root/'backend'/name,root/'Germanic'/name)
 subprocess.run(['python3',str(root/'.capr-work/parser_diagnostic.py'),
                 '--worker',sys.argv[2]],check=True)
finally:
 shutil.rmtree(root)
"""


def main():
    from adjudication_control import run_logged
    from experiment_snapshot import Snapshot

    manifest = json.loads((HERE / "evidence-manifest.json").read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--experiment", default="nonhigh-parser-root-repair-02",
        choices=[n for n in manifest["experiments"] if n != "nonhigh-four-cells-01"])
    args = parser.parse_args()
    archive_path = HERE / "evidence.tar.gz"
    if hashlib.sha256(archive_path.read_bytes()).hexdigest() != manifest["archive_sha256"]:
        raise RuntimeError("Evidence archive hash mismatch")
    work = ROOT / ".capr-work"
    work.mkdir(exist_ok=True)
    workspace = Path(tempfile.mkdtemp(prefix="nonhigh-gate-replay-", dir=work))
    with tarfile.open(archive_path) as archive:
        members = archive.getmembers()
        if len(members) != len(manifest["files"]):
            raise RuntimeError("Evidence member count mismatch")
        for member in members:
            relative = Path(member.name)
            if (not member.isfile() or relative.is_absolute() or ".." in relative.parts
                    or member.name not in manifest["files"]):
                raise RuntimeError("Unexpected evidence member: " + member.name)
            with archive.extractfile(member) as handle:
                digest = hashlib.sha256(handle.read()).hexdigest()
            if digest != manifest["files"][member.name]:
                raise RuntimeError("Evidence member hash mismatch: " + member.name)
        archive.extractall(workspace, filter="data")
    snapshot = Snapshot(workspace / "experiments" / args.experiment)
    snapshot.verify()
    completion = json.loads(snapshot.completion_path.read_text())
    for name, digest in completion["result_hashes"].items():
        if hashlib.sha256((snapshot.results_dir / name).read_bytes()).hexdigest() != digest:
            raise RuntimeError("Pinned result hash mismatch: " + name)
    container = snapshot.stage_in_container()
    destination = container + "/../parser-replay.json"
    receipt = run_logged(
        ["docker", "compose", "exec", "-T", "backend", "python3", "-c",
         BOOTSTRAP, container, destination],
        cwd=ROOT, label="nonhigh-gate-replay", log_dir=workspace / "replay")
    if not receipt["ok"]:
        print("Replay execution failed; receipt: " + receipt["receipt_path"])
        return 1
    result_path = workspace / "replay/diagnostic.json"
    subprocess.run(
        ["docker", "compose", "cp", "backend:" + destination, str(result_path)],
        cwd=ROOT, check=True)
    result = json.loads(result_path.read_text())
    for name in ("PGCellInput", "PGNew", "OENonHighSyn"):
        print(name + ": " + result["formal"][name]["stdout"].strip())
    print("Replay evidence: " + str(workspace / "replay"))
    if any(not result["formal"][name]["stdout"].startswith("1 ")
           for name in ("PGCellInput", "PGNew", "OENonHighSyn")):
        print("STOP: productive parser native functionality gate remains failed.")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
