#!/usr/bin/env python3
"""Workflow control for CAPR adjudications: preflight, receipts, locking.

This module supplies the cheap, mandatory control checks that run BEFORE
any expensive regeneration, Foma compilation or container work:

``preflight(sc_id, operation)``
    Read-only prerequisite validation scoped to the requested operation
    (``investigate``, ``evidence`` or ``finalize``).  Reuses the existing
    validators (``adjudicate.check_memo``, the canonical registry readers,
    ``artifact_graph.ARCHIVE_PATHS``); it never implements weaker parallel
    versions of them and never performs a post-refresh freshness check —
    a generated artifact that will become fresh during finalisation is not
    a reason to block regeneration.

``run_logged(argv, ...)``
    Reliable subprocess execution: argument arrays only (no shell
    pipelines), full stdout/stderr captured to log files, the true exit
    code recorded in a machine-readable receipt.  Filtering a log can
    therefore never conceal a failing exit status.

``runtime_lock(operation)``
    Advisory lock around operations that mutate the shared runtime
    artifacts (container bins, build manifest, canonical trace), so two
    processes cannot interleave rebuilds of the same mutable state.

Operational metadata lives in the untracked ``.capr-work/`` directory at
the repository root.  Nothing here is a scientific authority: the
canonical registries, memoranda and the artifact graph continue to own
scholarly and generated facts.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
WORK_DIR = REPO_ROOT / ".capr-work"
LOCK_DIR = WORK_DIR / "locks"
RUNTIME_LOCK = LOCK_DIR / "runtime-runner.lock"

TEMPLATE = REPO_ROOT / "Germanic/docs/sound_changes/audits/ADJUDICATION_TEMPLATE.md"

# Operations and the checks they require.  ``investigate`` must not demand a
# completed verdict; ``finalize`` must.
OPERATIONS = ("investigate", "evidence", "finalize")

PASS = "PASS"
BLOCKED = "BLOCKED"
NOT_APPLICABLE = "NOT_APPLICABLE"
INFO = "INFO"


def _utcnow() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Source identity
# ---------------------------------------------------------------------------

def _git(*args: str) -> str:
    result = subprocess.run(["git", *args], cwd=REPO_ROOT,
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def worktree_changes() -> list[str]:
    """Repo-relative paths modified/added/removed vs HEAD (non-ignored)."""
    lines = _git("status", "--porcelain").splitlines()
    paths = []
    for line in lines:
        entry = line[3:]
        if " -> " in entry:
            entry = entry.split(" -> ", 1)[1]
        paths.append(entry.strip('"'))
    return paths


def source_identity() -> dict:
    """Exact identity of the source state an operation will run against.

    HEAD commit plus a digest over the content of every non-ignored
    worktree change.  An uncommitted state is captured reproducibly and
    hashed — it is never silently equated with the last commit.
    """
    head = _git("rev-parse", "HEAD").strip()
    changes = {}
    digest = hashlib.sha256(head.encode())
    for rel in sorted(worktree_changes()):
        path = REPO_ROOT / rel
        if path.is_file():
            payload = path.read_bytes()
            sha = hashlib.sha256(payload).hexdigest()
        else:
            sha = "absent"  # deleted or non-regular
        changes[rel] = sha
        digest.update(f"\n{rel}\0{sha}".encode())
    return {
        "head_commit": head,
        "worktree_changes": changes,
        "identity_sha256": digest.hexdigest(),
        "recorded_at": _utcnow(),
    }


# ---------------------------------------------------------------------------
# Reliable command execution with receipts
# ---------------------------------------------------------------------------

def run_logged(argv: list[str], *, label: str, log_dir: Path,
               cwd: Path | None = None, env: dict | None = None,
               timeout: float | None = None) -> dict:
    """Run *argv* (an argument array, never a shell string) with full logs.

    Returns a receipt recording the exact command, true exit code and the
    log paths.  Success is determined only by the recorded ``returncode``;
    downstream filtering of the logs cannot conceal a failure.
    """
    if isinstance(argv, str):
        raise TypeError("run_logged requires an argument array, not a shell string")
    log_dir.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9._-]+", "-", label)[:80]
    stdout_path = log_dir / f"{safe}.stdout.log"
    stderr_path = log_dir / f"{safe}.stderr.log"
    started = _utcnow()
    with stdout_path.open("wb") as out, stderr_path.open("wb") as err:
        try:
            completed = subprocess.run(
                argv, cwd=cwd or REPO_ROOT, env=env, stdout=out, stderr=err,
                timeout=timeout)
            returncode: int | None = completed.returncode
            timed_out = False
        except subprocess.TimeoutExpired:
            returncode = None
            timed_out = True
    receipt = {
        "label": label,
        "argv": list(argv),
        "cwd": str(cwd or REPO_ROOT),
        "started_at": started,
        "finished_at": _utcnow(),
        "returncode": returncode,
        "timed_out": timed_out,
        "ok": (returncode == 0),
        "stdout_log": str(stdout_path),
        "stderr_log": str(stderr_path),
    }
    receipt_path = log_dir / f"{safe}.receipt.json"
    _atomic_write_json(receipt_path, receipt)
    receipt["receipt_path"] = str(receipt_path)
    return receipt


def _atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=path.name, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=1, ensure_ascii=False)
            handle.write("\n")
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# Runtime lock (shared mutable container artifacts)
# ---------------------------------------------------------------------------

def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def runtime_lock_holder() -> dict | None:
    """Live holder of the runtime lock, or None (stale locks are ignored)."""
    if not RUNTIME_LOCK.is_file():
        return None
    try:
        record = json.loads(RUNTIME_LOCK.read_text(encoding="utf-8"))
    except ValueError:
        return None
    pid = record.get("pid")
    if isinstance(pid, int) and _pid_alive(pid) and pid != os.getpid():
        return record
    return None


class runtime_lock:
    """Advisory exclusive lock for operations that rebuild shared runtime
    artifacts (stage bins, build manifest, canonical trace)."""

    def __init__(self, operation: str):
        self.operation = operation

    def __enter__(self):
        holder = runtime_lock_holder()
        if holder is not None:
            raise RuntimeError(
                f"runtime artifacts are in use by pid {holder['pid']} "
                f"({holder.get('operation', '?')} since {holder.get('acquired_at', '?')}); "
                "wait for it to finish or remove the stale lock "
                f"{RUNTIME_LOCK} if that process is gone")
        _atomic_write_json(RUNTIME_LOCK, {
            "pid": os.getpid(),
            "operation": self.operation,
            "acquired_at": _utcnow(),
        })
        return self

    def __exit__(self, *exc):
        try:
            record = json.loads(RUNTIME_LOCK.read_text(encoding="utf-8"))
            if record.get("pid") == os.getpid():
                RUNTIME_LOCK.unlink()
        except (OSError, ValueError):
            pass
        return False


# ---------------------------------------------------------------------------
# Preflight
# ---------------------------------------------------------------------------

@dataclass
class PreflightReport:
    sc_id: str
    operation: str
    checks: list = field(default_factory=list)
    source: dict = field(default_factory=dict)

    def add(self, name: str, status: str, detail: str) -> None:
        self.checks.append({"name": name, "status": status, "detail": detail})

    @property
    def blocked(self) -> bool:
        return any(c["status"] == BLOCKED for c in self.checks)

    @property
    def status(self) -> str:
        return BLOCKED if self.blocked else PASS

    def to_json(self) -> dict:
        return {
            "sc_id": self.sc_id,
            "operation": self.operation,
            "status": self.status,
            "checks": self.checks,
            "source_identity": self.source,
        }

    def render(self) -> str:
        lines = [f"== preflight: {self.sc_id} ({self.operation}) =="]
        for c in self.checks:
            lines.append(f"{c['status']:>14}  {c['name']}: {c['detail']}")
        if self.source:
            lines.append(f"          INFO  source identity: "
                         f"{self.source['identity_sha256'][:16]} "
                         f"(HEAD {self.source['head_commit'][:12]}, "
                         f"{len(self.source['worktree_changes'])} worktree changes)")
        lines.append(f"PREFLIGHT {self.status}"
                     + ("" if not self.blocked else
                        f" ({sum(1 for c in self.checks if c['status'] == BLOCKED)}"
                        " blocking problems; nothing expensive was started)"))
        return "\n".join(lines)


def required_memo_sections() -> list[str]:
    """The H2 sections mandated by the canonical adjudication template."""
    headings = []
    for line in TEMPLATE.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            headings.append(line[3:].strip())
    return headings


_INDENTED_VERDICT_RE = re.compile(r"^[ \t]+Registry-verdict:", re.MULTILINE)


def preflight(sc_id: str, operation: str = "investigate",
              *, probe_runner: bool = True) -> PreflightReport:
    """Cheap read-only prerequisite validation; never compiles or rebuilds."""
    if operation not in OPERATIONS:
        raise ValueError(f"unknown preflight operation {operation!r}; "
                         f"expected one of {OPERATIONS}")
    # Late import: adjudicate imports this module.
    import adjudicate
    import artifact_graph

    report = PreflightReport(sc_id=sc_id, operation=operation)

    # 1. SC exists in the canonical registry.
    row = adjudicate.load_registry_row(sc_id)
    if row is None:
        report.add("registry_row", BLOCKED,
                   f"{sc_id} not found in the canonical registry "
                   "(Germanic/docs/sound_changes/registry/sc_registry.tsv)")
        report.source = source_identity()
        return report
    report.add("registry_row", PASS,
               f"{sc_id} registered (lifecycle: {row['lifecycle_status']}, "
               f"adjudication: {row['adjudication_status']})")

    # 2. Referenced registry documents resolve.
    unresolved = []
    for fld in ("adjudication_memo", "chronology_card",
                "source_reader_facing_file"):
        ref = row.get(fld, "")
        if ref and adjudicate.resolve_doc(ref) is None:
            unresolved.append(f"{fld}={ref!r}")
    for ref in adjudicate.split_refs(row.get("capr_evidence", "")):
        if adjudicate.resolve_doc(ref) is None:
            unresolved.append(f"capr_evidence={ref!r}")
    if unresolved:
        report.add("registry_documents", BLOCKED,
                   "unresolvable registry pointers: " + "; ".join(unresolved))
    else:
        report.add("registry_documents", PASS,
                   "all registry document pointers resolve")

    # 3. Verdict vocabulary (any recorded verdict must be well-formed even
    #    outside finalisation).
    verdict = row.get("verdict", "")
    bad_tokens = [t for t in verdict.split("/")
                  if t and t not in adjudicate.VERDICT_VOCABULARY]
    if bad_tokens:
        report.add("verdict_vocabulary", BLOCKED,
                   f"verdict tokens not in controlled vocabulary: {bad_tokens}")
    elif verdict:
        report.add("verdict_vocabulary", PASS, f"verdict {verdict!r} well-formed")
    else:
        report.add("verdict_vocabulary",
                   BLOCKED if operation == "finalize" else NOT_APPLICABLE,
                   "registry verdict is empty"
                   + ("" if operation != "finalize"
                      else " (finalisation requires a recorded verdict)"))

    # 4. Executable identifier, where the operation requires one.
    ident = row.get("fst_identifier", "")
    if operation == "evidence":
        if not ident:
            report.add("fst_identifier", BLOCKED,
                       f"{sc_id} has no executable fst_identifier; there is "
                       "no live rule to census")
        else:
            lineno, _ = adjudicate.find_rule(ident)
            if lineno:
                report.add("fst_identifier", PASS,
                           f"define {ident} at germanic.txt line {lineno}")
            else:
                report.add("fst_identifier", BLOCKED,
                           f"no live `define {ident}` in germanic.txt "
                           f"(lifecycle: {row['lifecycle_status']})")
    else:
        report.add("fst_identifier", NOT_APPLICABLE if not ident else PASS,
                   ident or "none recorded (not required for this operation)")

    # 5/6. Finalisation memo checks: exact Registry-verdict format accepted
    #      by the existing checker, plus the template-mandated sections.
    if operation == "finalize":
        memo_errors = adjudicate.check_memo(sc_id, row=row)
        memo_rel = row.get("adjudication_memo", "")
        memo_path = REPO_ROOT / memo_rel if memo_rel else None
        if memo_errors:
            detail = "; ".join(memo_errors)
            # Identify the exact defect for the common indentation mistake.
            if (memo_path is not None and memo_path.is_file()
                    and any("no 'Registry-verdict:' line" in e
                            for e in memo_errors)
                    and _INDENTED_VERDICT_RE.search(
                        memo_path.read_text(encoding="utf-8"))):
                detail += ("; a 'Registry-verdict:' line exists but is "
                           "indented — the checker only accepts it at the "
                           "start of a line (column 0)")
            report.add("memo_verdict", BLOCKED, detail)
        else:
            report.add("memo_verdict", PASS,
                       "memo Registry-verdict agrees with the registry")
        if memo_path is not None and memo_path.is_file():
            text = memo_path.read_text(encoding="utf-8")
            present = {line[3:].strip()
                       for line in text.splitlines() if line.startswith("## ")}
            missing = [h for h in required_memo_sections() if h not in present]
            if missing:
                report.add("memo_sections", BLOCKED,
                           f"memo {memo_rel} is missing required template "
                           f"sections: {missing}")
            else:
                report.add("memo_sections", PASS,
                           "all template-mandated sections present")
        else:
            report.add("memo_sections", BLOCKED,
                       f"memo missing: {memo_rel or '(registry field empty)'}")
    else:
        report.add("memo_verdict", NOT_APPLICABLE,
                   "verdict/memo agreement is checked at finalisation")

    # 7. ARCHIVE files are frozen: any worktree modification blocks.
    changes = set(worktree_changes())
    archive_rel = {str(p.relative_to(REPO_ROOT))
                   for p in artifact_graph.ARCHIVE_PATHS}
    touched_archive = sorted(changes & archive_rel)
    if touched_archive:
        report.add("archive_frozen", BLOCKED,
                   "ARCHIVE/FROZEN records are modified in the worktree "
                   f"(never rewritten by any operation): {touched_archive}")
    else:
        report.add("archive_frozen", PASS, "no frozen ARCHIVE record modified")

    # 8. Protected baseline summaries change only via the approved adoption
    #    mechanism (adjudicate --adopt-*-baseline with an approval receipt).
    baseline_rel = str(adjudicate.BASELINE_SUMMARY.relative_to(REPO_ROOT))
    baseline_dir = str(adjudicate.BASELINE_SUMMARY.parent.relative_to(REPO_ROOT))
    touched_baseline = sorted(
        c for c in changes
        if c == baseline_rel
        or (c.startswith(baseline_dir + "/")
            and "baseline" in Path(c).name and c not in archive_rel))
    approvals = sorted(c for c in changes
                       if Path(c).name.startswith("approved_")
                       and c.startswith(baseline_dir + "/"))
    if touched_baseline and not approvals:
        report.add("protected_baselines", BLOCKED,
                   "protected baseline files are modified without an "
                   f"approval receipt: {touched_baseline}; use the "
                   "--adopt-*-baseline mechanism")
    else:
        report.add("protected_baselines", PASS,
                   "no unapproved protected-baseline change")

    # 9. GENERATED files: informational only.  A stale/modified generated
    #    artifact is expected to become fresh during refresh/finalize and is
    #    not a reason to forbid regeneration; hand-edits are caught by the
    #    artifact graph's own freshness check afterwards.
    report.add("generated_ownership", INFO,
               "generated artifacts are owned by the artifact graph; "
               "freshness is checked after refresh, not here")

    # 10. Runner availability for operations that need the container. If an
    #     earlier check already blocked, nothing touches Docker at all.
    if operation in ("evidence", "finalize") and probe_runner and report.blocked:
        report.add("runtime_runner", NOT_APPLICABLE,
                   "probe skipped: earlier checks already block this operation")
    elif operation in ("evidence", "finalize") and probe_runner:
        from capr_runtime import run_in_runner
        try:
            probe = run_in_runner("true", capture_output=True, text=True,
                                  timeout=30)
            ok = probe.returncode == 0
        except (RuntimeError, OSError, subprocess.TimeoutExpired):
            ok = False
        if ok:
            report.add("runtime_runner", PASS, "backend runner reachable")
        else:
            report.add("runtime_runner", BLOCKED,
                       "backend runner unreachable; run `docker compose up -d` "
                       "and check `docker compose ps`")
    else:
        report.add("runtime_runner", NOT_APPLICABLE,
                   "no container work required for this operation"
                   if operation == "investigate" else "probe skipped")

    # 11. Working-directory permissions for receipts/journal.
    try:
        WORK_DIR.mkdir(exist_ok=True)
        probe_file = WORK_DIR / ".write-probe"
        probe_file.write_text("ok", encoding="utf-8")
        probe_file.unlink()
        report.add("work_dir", PASS, f"{WORK_DIR.name}/ writable")
    except OSError as exc:
        report.add("work_dir", BLOCKED, f"cannot write {WORK_DIR}: {exc}")

    # 12. No conflicting process holds the mutable runtime artifacts.
    if operation in ("evidence", "finalize"):
        holder = runtime_lock_holder()
        if holder is not None:
            report.add("runtime_conflict", BLOCKED,
                       f"runtime artifacts in use by pid {holder['pid']} "
                       f"({holder.get('operation', '?')})")
        else:
            report.add("runtime_conflict", PASS,
                       "no other process holds the runtime artifacts")
    else:
        report.add("runtime_conflict", NOT_APPLICABLE,
                   "operation does not mutate shared runtime artifacts")

    # 13. Record the intended source identity.
    report.source = source_identity()
    return report


def preflight_main(sc_id: str, operation: str, *, as_json: bool = False) -> int:
    report = preflight(sc_id, operation)
    if as_json:
        print(json.dumps(report.to_json(), indent=1, ensure_ascii=False))
    else:
        print(report.render())
    return 1 if report.blocked else 0
