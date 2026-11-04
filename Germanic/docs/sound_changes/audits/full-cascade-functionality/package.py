#!/usr/bin/env python3
"""Freeze essential formal evidence; retain hashes of every private export."""
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    if target.exists():
        raise SystemExit("Never overwrite an existing evidence capsule")
    here = Path(__file__).resolve().parent
    files = {}
    retained = []
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        retained.append(dict(path=str(relative), bytes=path.stat().st_size, sha256=sha(path)))
        if path.suffix == ".bin":
            continue
        if path.name.startswith("prefix-") and path.suffix == ".att":
            if int(path.stem.split("-")[1]) > 61:
                continue
        files["networks/" + str(relative)] = path
    for path in sorted(here.glob("*.py")):
        files["scripts/" + path.name] = path
    helper = here.parent / "parser-formal-resolution/functionality.py"
    files["accepted-proof/functionality.py"] = helper
    private = source.parent
    for path in sorted(private.glob("*cascade*.log")):
        files["logs/" + path.name] = path
    for name in ("cascade-witness-lookups-01.json", "cascade-stressed-probes.json",
                 "cascade-followup-worker.py"):
        if (private / name).is_file():
            files["operational/" + name] = private / name
    manifest = dict(
        scope="all first-62-prefix certificates and ATTs, actual full ATT, "
              "all native receipts, diagnostic restrictions, traces and paths",
        private_exports_retained_not_all_embedded=retained,
        members={name: dict(bytes=path.stat().st_size, sha256=sha(path))
                 for name, path in files.items()})
    raw = (json.dumps(manifest, indent=2) + "\n").encode()
    with tarfile.open(target, "w:gz") as archive:
        for name, path in files.items():
            archive.add(path, arcname=name)
        info = tarfile.TarInfo("manifest.json")
        info.size = len(raw)
        archive.addfile(info, io.BytesIO(raw))
    with tarfile.open(target) as archive:
        for name, record in manifest["members"].items():
            assert hashlib.sha256(archive.extractfile(name).read()).hexdigest() == record["sha256"]
    receipt = dict(archive=target.name, bytes=target.stat().st_size, sha256=sha(target),
                   embedded_members=len(files), retained_exports=len(retained))
    target.with_name("evidence-manifest.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))
