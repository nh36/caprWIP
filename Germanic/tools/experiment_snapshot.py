#!/usr/bin/env python3
"""Immutable source snapshots for CAPR adjudication experiments.

A small provenance wrapper around the EXISTING isolated experiment
machinery (``anglo_frisian_experiments.compile_isolated`` and friends).
It does not compile anything itself and introduces no new experimental
framework; it guarantees that:

* an experiment runs against an immutable, hashed copy of its inputs, so
  later production edits (for example to ``Germanic/fsts/germanic.txt``)
  cannot change a running or recorded experiment;
* an uncommitted source state is captured reproducibly and hashed —
  never silently replaced by the last committed version;
* outputs are staged and promoted atomically, so an interrupted run can
  never leave a valid-looking completion receipt;
* a failed experiment cannot be recorded as passed: completion with
  outcome ``passed`` is refused while any attached command receipt
  records a nonzero exit code.

Snapshots live under the untracked ``.capr-work/experiments/<id>/``:

    receipt.json       identity, purpose, input/variant hashes, source state
    snapshot/          read-only copies of every input
    staging/           work in progress (never authoritative)
    results/           atomically promoted outputs
    completion.json    outcome receipt, written only after promotion

For container execution the snapshot is staged into the backend
container's own ``/tmp`` (NOT a bind mount), so the production-editing
process on the host cannot write to it at all.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path

import adjudication_control

REPO_ROOT = Path(__file__).resolve().parents[2]
EXPERIMENTS_DIR = adjudication_control.WORK_DIR / "experiments"

OUTCOMES = ("passed", "failed", "inconclusive", "deferred")


def _identifier(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,79}", value):
        raise ValueError(f"invalid experiment identifier or service: {value!r}")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _make_read_only(path: Path) -> None:
    os.chmod(path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


@dataclass(frozen=True)
class Snapshot:
    root: Path

    @property
    def snapshot_dir(self) -> Path:
        return self.root / "snapshot"

    @property
    def staging_dir(self) -> Path:
        return self.root / "staging"

    @property
    def results_dir(self) -> Path:
        return self.root / "results"

    @property
    def receipt_path(self) -> Path:
        return self.root / "receipt.json"

    @property
    def completion_path(self) -> Path:
        return self.root / "completion.json"

    def receipt(self) -> dict:
        return json.loads(self.receipt_path.read_text(encoding="utf-8"))

    def input_path(self, label: str) -> Path:
        """The immutable snapshot copy for *label*; verified before use."""
        entry = self.receipt()["inputs"].get(label)
        if entry is None:
            raise KeyError(f"no snapshot input labelled {label!r}")
        path = self.snapshot_dir / entry["snapshot_name"]
        if path.resolve().parent != self.snapshot_dir.resolve():
            raise ValueError("snapshot input path escapes its source directory")
        actual = _sha256(path)
        if actual != entry["sha256"]:
            raise RuntimeError(
                f"snapshot input {label!r} no longer matches its recorded "
                f"hash ({actual} != {entry['sha256']}); the snapshot is "
                "corrupt and the experiment must not proceed")
        return path

    def verify(self) -> None:
        receipt = self.receipt()
        _identifier(receipt["experiment_id"])
        if not receipt.get("inputs"):
            raise ValueError("snapshot contains no inputs")
        for label in receipt["inputs"]:
            self.input_path(label)
        if receipt["variant_sha256"] != {
                name: hashlib.sha256(text.encode()).hexdigest()
                for name, text in receipt["variants"].items()}:
            raise ValueError("snapshot variant hashes do not match")

    def compile_isolated(self, source_label: str, recipe_label: str, *,
                         components_only: bool = False, service: str = "backend") -> dict:
        """Route pinned inputs to the existing compiler in container-private /tmp."""
        self.verify()
        source = self.input_path(source_label).name
        recipe = self.input_path(recipe_label).name
        container_dir = self.stage_in_container(service=service)
        output = f"/tmp/capr-build-{_identifier(self.receipt()['experiment_id'])}-{uuid.uuid4().hex}"
        code = (
            "import json,sys; from pathlib import Path; "
            "sys.path.insert(0,'/usr/app/tools'); "
            "from anglo_frisian_experiments import compile_isolated; "
            "root=Path(sys.argv[1]); out=Path(sys.argv[2]); out.mkdir(); "
            "recipe=json.loads((root/sys.argv[4]).read_text()); "
            "bins=compile_isolated(root/sys.argv[3],recipe,[],out,"
            "components_only=sys.argv[5]=='True'); "
            "print(json.dumps({k:str(v) for k,v in bins.items()}))")
        receipt = adjudication_control.run_logged(
            ["docker", "compose", "exec", "-T", service, "python3", "-c", code,
             container_dir, output, source, recipe, str(components_only)],
            label="isolated-compile", log_dir=self.staging_dir)
        if not receipt["ok"]:
            raise RuntimeError(f"isolated snapshot compile failed: {receipt['stderr_log']}")
        return {"receipt": receipt, "snapshot_identity": self.receipt()["source_identity"],
                "snapshot_root": str(self.root.resolve()),
                "container_source": container_dir, "container_output": output,
                "bins": json.loads(Path(receipt["stdout_log"]).read_text())}

    def is_complete(self) -> bool:
        return self.completion_path.is_file()

    def completion(self) -> dict:
        return json.loads(self.completion_path.read_text(encoding="utf-8"))

    # -- lifecycle ---------------------------------------------------------

    def complete(self, outcome: str, summary: str,
                 command_receipts: list[dict] | None = None,
                 evidence: dict | None = None) -> dict:
        """Promote staged outputs atomically and write the outcome receipt.

        ``passed`` is refused while any attached command receipt records a
        failure; an interrupted process that never reaches this call leaves
        no completion receipt at all.
        """
        if outcome not in OUTCOMES:
            raise ValueError(f"outcome {outcome!r} not in {OUTCOMES}")
        if self.is_complete():
            raise RuntimeError(
                f"experiment already completed: {self.completion_path}")
        receipts = command_receipts or []
        failed = [r.get("label", "?") for r in receipts if not r.get("ok")]
        if outcome == "passed" and failed:
            raise RuntimeError(
                "cannot record outcome 'passed': command receipts record "
                f"failures: {failed}")
        if outcome == "passed" and not receipts:
            raise RuntimeError(
                "cannot record outcome 'passed' without at least one "
                "command receipt attesting what actually ran")
        # Atomic promotion: staged outputs become results in one rename.
        if self.results_dir.exists():
            raise RuntimeError(f"results already promoted: {self.results_dir}")
        if self.staging_dir.exists():
            os.replace(self.staging_dir, self.results_dir)
        else:
            self.results_dir.mkdir(parents=True)
        outputs = {
            str(p.relative_to(self.results_dir)): _sha256(p)
            for p in sorted(self.results_dir.rglob("*")) if p.is_file()
        }
        payload = {
            "experiment_id": self.receipt()["experiment_id"],
            "outcome": outcome,
            "summary": summary,
            "completed_at": adjudication_control._utcnow(),
            "command_receipts": receipts,
            "evidence": evidence or {},
            "result_hashes": outputs,
            "source_identity_sha256":
                self.receipt()["source_identity"]["identity_sha256"],
        }
        adjudication_control._atomic_write_json(self.completion_path, payload)
        return payload

    # -- container isolation ----------------------------------------------

    def stage_in_container(self, *, service: str = "backend") -> str:
        """Copy the snapshot into the container's own /tmp (not a bind
        mount): the host production-editing process cannot write there.
        Returns the container-side snapshot directory."""
        self.verify()
        _identifier(service)
        container_dir = f"/tmp/capr-exp-{_identifier(self.receipt()['experiment_id'])}-{uuid.uuid4().hex}"
        checks = subprocess.run(
            ["docker", "compose", "exec", "-T", service, "sh", "-lc",
             f"mkdir {container_dir}"],
            cwd=REPO_ROOT, capture_output=True, text=True)
        if checks.returncode != 0:
            raise RuntimeError(
                f"cannot prepare container snapshot dir: {checks.stderr}")
        copy = subprocess.run(
            ["docker", "compose", "cp",
             str(self.snapshot_dir) + "/.", f"{service}:{container_dir}"],
            cwd=REPO_ROOT, capture_output=True, text=True)
        if copy.returncode != 0:
            raise RuntimeError(f"container snapshot copy failed: {copy.stderr}")
        # Verify hashes inside the container before anything consumes them.
        expected = {entry["snapshot_name"]: entry["sha256"]
                    for entry in self.receipt()["inputs"].values()}
        listing = subprocess.run(
            ["docker", "compose", "exec", "-T", service, "sh", "-lc",
             f"cd {container_dir} && chmod -R a-w . && sha256sum *"],
            cwd=REPO_ROOT, capture_output=True, text=True)
        if listing.returncode != 0:
            raise RuntimeError(
                f"container snapshot verification failed: {listing.stderr}")
        seen = {}
        for line in listing.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                seen[parts[-1]] = parts[0]
        if seen != expected:
            raise RuntimeError(
                "container snapshot does not match the recorded hashes; "
                f"expected {expected}, saw {seen}")
        return container_dir


def create_snapshot(experiment_id: str, purpose: str,
                    inputs: dict[str, Path], *,
                    variants: dict[str, str] | None = None,
                    probes: list | None = None,
                    expected_outcomes: dict | None = None,
                    negative_controls: list | None = None,
                    environment: dict | None = None,
                    work_root: Path | None = None) -> Snapshot:
    """Create an immutable, hashed snapshot of every experiment input.

    *inputs* maps a label (for example ``"germanic_fst"``) to the live
    path whose current content the experiment must be pinned to.
    *variants* maps variant names to their exact Foma definition text.
    *environment* records Foma/container identity when the caller has it;
    otherwise the receipt states explicitly that it was not recorded.
    """
    _identifier(experiment_id)
    root = (work_root or EXPERIMENTS_DIR) / experiment_id
    if root.exists():
        raise RuntimeError(
            f"experiment directory already exists: {root}; choose a new "
            "experiment id rather than silently reusing recorded evidence")
    snapshot_dir = root / "snapshot"
    snapshot_dir.mkdir(parents=True)
    recorded_inputs = {}
    for label, source in inputs.items():
        _identifier(label)
        source = Path(source)
        if not source.is_file():
            raise FileNotFoundError(f"experiment input {label!r}: {source}")
        name = f"{label}{''.join(source.suffixes) or '.txt'}"
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
            raise ValueError("unsafe snapshot filename")
        target = snapshot_dir / name
        shutil.copyfile(source, target)
        _make_read_only(target)
        sha = _sha256(target)
        if sha != _sha256(source):
            raise RuntimeError(
                f"input {label!r} changed while being snapshotted; retry "
                "once the source is quiescent")
        recorded_inputs[label] = {
            "original_path": str(source),
            "snapshot_name": name,
            "sha256": sha,
        }
    variant_hashes = {
        name: hashlib.sha256(text.encode("utf-8")).hexdigest()
        for name, text in (variants or {}).items()
    }
    receipt = {
        "experiment_id": experiment_id,
        "purpose": purpose,
        "created_at": adjudication_control._utcnow(),
        "source_identity": adjudication_control.source_identity(),
        "inputs": recorded_inputs,
        "variants": variants or {},
        "variant_sha256": variant_hashes,
        "probes": probes or [],
        "expected_outcomes": expected_outcomes or {},
        "negative_controls": negative_controls or [],
        "environment": environment or {
            "recorded": False,
            "reason": "caller did not supply Foma/container identity",
        },
        "staging_dir": "staging",
        "results_dir": "results",
    }
    adjudication_control._atomic_write_json(root / "receipt.json", receipt)
    (root / "staging").mkdir()
    return Snapshot(root=root)


def load_snapshot(experiment_id: str,
                  work_root: Path | None = None) -> Snapshot:
    _identifier(experiment_id)
    root = (work_root or EXPERIMENTS_DIR) / experiment_id
    if not (root / "receipt.json").is_file():
        raise FileNotFoundError(f"no experiment snapshot at {root}")
    return Snapshot(root=root)
