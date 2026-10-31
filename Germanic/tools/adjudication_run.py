#!/usr/bin/env python3
"""Durable workflow state machine for one CAPR adjudication.

Stages::

    INSPECT -> PREFLIGHT -> SNAPSHOT -> INVESTIGATE -> DECIDE
            -> PROPAGATE -> VALIDATE -> COMPLETE

One machine-readable journal per run lives in the untracked
``.capr-work/runs/<SCNNN>/``:

    state.json      current stage, per-stage records (atomic writes)
    events.ndjson   append-only history of significant events

The journal is operational metadata, NOT a scientific authority: the
canonical registries, research memoranda and the artifact graph
(``artifact_graph.py``) continue to own scholarly and generated facts.

A completed stage remains valid only while the source identities it
depends on remain unchanged.  Dependency domains are derived from the
EXISTING v2 full-trace provenance contract (``oe_trace_parse.SOURCE_PATHS``)
and the canonical registry files — there is no second, independently
maintained dependency table:

* ``executable_model``  compilation inputs + evaluation helpers
* ``corpus``            selected lexical inputs + context metadata
* ``registry``          canonical SC/chronology registries
* ``memo``              this SC's adjudication memorandum

Invalidation is selective: editing a memorandum invalidates only the
cheap PREFLIGHT record, never compiled Foma evidence; editing the FST
before propagation invalidates the experimental evidence and the
decision that rested on it; reader-facing prose invalidates nothing
scientific.  Once PROPAGATE has completed, the deliberate source change
it introduced no longer invalidates the pre-decision evidence record —
but VALIDATE is always checked against the exact current source
identity, so no earlier validation can certify a modified tree.

``DEFER`` is a legitimate scientific outcome.  A decision with a failing
required negative control or an unresolved counterexample cannot be
recorded as resolved merely because mechanical checks pass.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import adjudication_control
import oe_trace_parse

REPO_ROOT = Path(__file__).resolve().parents[2]
RUNS_DIR = adjudication_control.WORK_DIR / "runs"
REGISTRY_DIR = REPO_ROOT / "Germanic/docs/sound_changes/registry"

STAGES = ("INSPECT", "PREFLIGHT", "SNAPSHOT", "INVESTIGATE", "DECIDE",
          "PROPAGATE", "VALIDATE", "COMPLETE")

# Resolved verdict tokens; DEFER deliberately marks an open decision.
RESOLVED_VERDICTS = {"RETAIN", "REFORMULATE", "RESTRICT", "SPLIT", "RETIRE",
                     "REORDER"}

# What each stage is for, and the next permitted command once it is the
# frontier.  Reported verbatim so an agent never reconstructs the plan.
STAGE_GUIDE = {
    "INSPECT": "read the packet: python3 Germanic/tools/adjudicate.py {sc} --prepare",
    "PREFLIGHT": "cheap gate: python3 Germanic/tools/adjudicate.py {sc} --preflight",
    "SNAPSHOT": "pin experiment inputs: experiment_snapshot.create_snapshot(...) "
                "(record the snapshot id in the stage evidence)",
    "INVESTIGATE": "gather evidence: python3 Germanic/tools/adjudicate.py {sc} "
                   "--evidence, plus snapshot-pinned experiments",
    "DECIDE": "record the scientific decision: adjudicate.py {sc} --run decide "
              "<decision.json> (DEFER is legitimate)",
    "PROPAGATE": "edit SOURCE files, then python3 Germanic/tools/adjudicate.py "
                 "{sc} --finalize",
    "VALIDATE": "focused + integrated + full strict validation; attach "
                "run_logged receipts as stage evidence",
    "COMPLETE": "write the completion receipt: adjudicate.py {sc} --run "
                "advance COMPLETE",
}

# Dependency domains per stage.  INVESTIGATE/DECIDE identity checks stop
# applying once PROPAGATE has completed (the propagated edit is the
# sanctioned change the decision called for); VALIDATE is always checked.
STAGE_DOMAINS = {
    "INSPECT": (),
    "PREFLIGHT": ("registry", "memo"),
    "SNAPSHOT": (),  # immutable record; corruption is caught by its hashes
    "INVESTIGATE": ("executable_model", "corpus"),
    "DECIDE": ("executable_model", "corpus"),
    "PROPAGATE": ("registry", "memo"),
    "VALIDATE": ("executable_model", "corpus", "registry", "memo"),
    "COMPLETE": (),
}
FROZEN_AFTER_PROPAGATE = {"INVESTIGATE", "DECIDE"}


def _domain_files(domain: str, sc_id: str) -> list[Path]:
    src = oe_trace_parse.SOURCE_PATHS
    if domain == "executable_model":
        rels = [rel for label, rel in src.items()
                if label not in ("germanic-aligned-final.tsv",
                                 "entry_context_metadata.tsv")]
        return [REPO_ROOT / rel for rel in rels]
    if domain == "corpus":
        return [REPO_ROOT / src["germanic-aligned-final.tsv"],
                REPO_ROOT / src["entry_context_metadata.tsv"]]
    if domain == "registry":
        return [REGISTRY_DIR / name for name in
                ("sc_registry.tsv", "chronology_edges.tsv",
                 "sc_inventory_notes.tsv")]
    if domain == "memo":
        import adjudicate
        row = adjudicate.load_registry_row(sc_id)
        memo = (row or {}).get("adjudication_memo", "")
        return [REPO_ROOT / memo] if memo else []
    raise ValueError(f"unknown dependency domain {domain!r}")


def domain_identity(domain: str, sc_id: str) -> str:
    digest = hashlib.sha256(domain.encode())
    for path in _domain_files(domain, sc_id):
        digest.update(b"\0" + str(path).encode() + b"\0")
        digest.update(path.read_bytes() if path.is_file() else b"<absent>")
    return digest.hexdigest()


class WorkflowError(RuntimeError):
    """A stage transition violates its prerequisites; message is actionable."""


class Run:
    """One durable adjudication run (journal under .capr-work/runs/<sc>/)."""

    def __init__(self, sc_id: str, root: Path):
        self.sc_id = sc_id
        self.root = root
        self.state_path = root / "state.json"
        self.events_path = root / "events.ndjson"

    # -- persistence --------------------------------------------------------

    def state(self) -> dict:
        return json.loads(self.state_path.read_text(encoding="utf-8"))

    def _write_state(self, state: dict) -> None:
        adjudication_control._atomic_write_json(self.state_path, state)

    def _event(self, kind: str, **payload) -> None:
        record = {"at": adjudication_control._utcnow(), "kind": kind,
                  **payload}
        with self.events_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    def events(self) -> list[dict]:
        if not self.events_path.is_file():
            return []
        return [json.loads(line) for line in
                self.events_path.read_text(encoding="utf-8").splitlines()
                if line.strip()]

    # -- invalidation -------------------------------------------------------

    def _current_identities(self, domains) -> dict:
        return {d: domain_identity(d, self.sc_id) for d in domains}

    def refresh_validity(self) -> list[str]:
        """Re-check every completed stage against current source identities.

        Invalidates exactly the stages whose own dependency domains changed
        (and records why); unrelated stages are untouched.  Returns the
        names of newly invalidated stages.
        """
        state = self.state()
        propagated = (state["stages"].get("PROPAGATE", {}).get("status")
                      == "complete")
        invalidated = []
        for stage in STAGES:
            record = state["stages"].get(stage)
            if not record or record.get("status") != "complete":
                continue
            if stage in FROZEN_AFTER_PROPAGATE and propagated:
                continue  # the propagated edit was the sanctioned change
            stale = []
            for domain, recorded in record.get("domain_identities",
                                               {}).items():
                current = domain_identity(domain, self.sc_id)
                if current != recorded:
                    stale.append(domain)
            if stale:
                record["status"] = "invalidated"
                record["invalidated_because"] = (
                    f"dependency domains changed since completion: {stale}")
                invalidated.append(stage)
                self._event("stage_invalidated", stage=stage, domains=stale)
        if invalidated:
            self._write_state(state)
        return invalidated

    # -- queries ------------------------------------------------------------

    def frontier(self) -> str:
        """First stage that is not currently complete."""
        state = self.state()
        for stage in STAGES:
            record = state["stages"].get(stage)
            if not record or record.get("status") != "complete":
                return stage
        return "COMPLETE"

    def report(self) -> str:
        """Current stage, valid cached evidence, blockers, next operation."""
        self.refresh_validity()
        state = self.state()
        lines = [f"== adjudication run: {self.sc_id} =="]
        for stage in STAGES:
            record = state["stages"].get(stage)
            status = (record or {}).get("status", "pending")
            note = (record or {}).get("note", "")
            extra = ""
            if status == "invalidated":
                extra = f" — {record.get('invalidated_because', '')}"
            elif note:
                extra = f" — {note}"
            lines.append(f"  {stage:<12} {status}{extra}")
        frontier = self.frontier()
        blockers = [s for s in STAGES
                    if state["stages"].get(s, {}).get("status")
                    == "invalidated"]
        if blockers:
            lines.append(f"blockers: invalidated stages must be redone: "
                         f"{blockers}")
        next_stage = blockers[0] if blockers else frontier
        lines.append(f"current frontier: {frontier}")
        lines.append("next permitted operation: "
                     + STAGE_GUIDE[next_stage].format(sc=self.sc_id))
        return "\n".join(lines)

    # -- transitions --------------------------------------------------------

    def complete_stage(self, stage: str, *, note: str = "",
                       evidence: dict | None = None) -> dict:
        if stage not in STAGES:
            raise WorkflowError(f"unknown stage {stage!r}; stages: {STAGES}")
        self.refresh_validity()
        state = self.state()
        index = STAGES.index(stage)
        for prerequisite in STAGES[:index]:
            record = state["stages"].get(prerequisite, {})
            if record.get("status") != "complete":
                raise WorkflowError(
                    f"cannot complete {stage}: prerequisite {prerequisite} is "
                    f"{record.get('status', 'pending')}; next permitted "
                    "operation: "
                    + STAGE_GUIDE[prerequisite].format(sc=self.sc_id))
        existing = state["stages"].get(stage, {})
        if existing.get("status") == "complete":
            raise WorkflowError(
                f"{stage} is already complete; completed stages are redone "
                "only after invalidation (source change), never silently")
        evidence = evidence or {}
        if stage == "DECIDE":
            self._check_decision(evidence)
        if stage == "VALIDATE":
            self._check_validation(evidence)
        record = {
            "status": "complete",
            "completed_at": adjudication_control._utcnow(),
            "note": note,
            "evidence": evidence,
            "source_identity": adjudication_control.source_identity(),
            "domain_identities":
                self._current_identities(STAGE_DOMAINS[stage]),
        }
        state["stages"][stage] = record
        self._write_state(state)
        self._event("stage_complete", stage=stage, note=note)
        return record

    # -- stage-specific contracts -------------------------------------------

    _DECISION_FIELDS = (
        "historical_phenomenon", "conditioning", "executable_implementation",
        "selected_input_assumptions", "firing_census", "positive_witnesses",
        "negative_controls", "counterfactual_results", "literature_support",
        "historical_vs_modelling", "unresolved", "verdict",
        "intended_source_modifications",
    )

    def _check_decision(self, evidence: dict) -> None:
        missing = [f for f in self._DECISION_FIELDS if f not in evidence]
        if missing:
            raise WorkflowError(
                "DECIDE requires an explicit decision record; missing "
                f"fields: {missing}")
        verdict = evidence["verdict"]
        tokens = [t for t in str(verdict).split("/") if t]
        unknown = [t for t in tokens
                   if t not in RESOLVED_VERDICTS and t != "DEFER"]
        if not tokens or unknown:
            raise WorkflowError(
                f"verdict {verdict!r} is not in the controlled vocabulary "
                f"({sorted(RESOLVED_VERDICTS)} or DEFER)")
        resolved = any(t in RESOLVED_VERDICTS for t in tokens)
        failing_controls = [
            c for c in evidence.get("negative_controls", [])
            if isinstance(c, dict) and c.get("required", True)
            and c.get("passed") is not True]
        if resolved and failing_controls:
            raise WorkflowError(
                "a required negative control is not passing; the scientific "
                "decision must remain open (DEFER) regardless of unchanged "
                "corpus outputs: "
                + "; ".join(str(c.get("description", c))
                            for c in failing_controls))
        unresolved = evidence.get("unresolved") or []
        acknowledged = all(isinstance(u, dict) and u.get("acknowledged_in")
                           for u in unresolved)
        if resolved and unresolved and not acknowledged:
            raise WorkflowError(
                "unresolved counterexamples cannot be silently converted "
                "into a resolved verdict; either DEFER or acknowledge each "
                "item with an 'acknowledged_in' pointer to the memorandum "
                "section that documents it")

    def _check_validation(self, evidence: dict) -> None:
        receipts = evidence.get("receipts") or []
        if not receipts:
            raise WorkflowError(
                "VALIDATE requires run_logged command receipts attesting "
                "what actually ran (true exit codes and full logs)")
        failing = [r.get("label", "?") for r in receipts if not r.get("ok")]
        if failing:
            raise WorkflowError(
                f"validation receipts record failures: {failing}; a failed "
                "validation cannot be recorded as passed")
        current = adjudication_control.source_identity()["identity_sha256"]
        for receipt in receipts:
            attested = receipt.get("source_identity_sha256")
            if attested and attested != current:
                raise WorkflowError(
                    "a validation receipt attests a different source "
                    f"identity ({attested[:16]}…) than the current tree "
                    f"({current[:16]}…); an earlier pass cannot certify a "
                    "subsequently modified source tree")


# ---------------------------------------------------------------------------
# run management
# ---------------------------------------------------------------------------

def start(sc_id: str, *, runs_dir: Path | None = None) -> Run:
    root = (runs_dir or RUNS_DIR) / sc_id
    if (root / "state.json").is_file():
        run = Run(sc_id, root)
        if run.frontier() != "COMPLETE":
            raise WorkflowError(
                f"an active run for {sc_id} already exists; resume it "
                f"(adjudicate.py {sc_id} --run status) or archive "
                f"{root} explicitly before starting a new one")
        archive = root.parent / "archive"
        archive.mkdir(parents=True, exist_ok=True)
        stamp = adjudication_control._utcnow().replace(":", "")
        root.rename(archive / f"{sc_id}-{stamp}")
    root.mkdir(parents=True, exist_ok=True)
    run = Run(sc_id, root)
    state = {
        "sc_id": sc_id,
        "started_at": adjudication_control._utcnow(),
        "source_identity_at_start": adjudication_control.source_identity(),
        "scientific_reference_state": None,
        "stages": {},
        "operations": [],
    }
    run._write_state(state)
    run._event("run_started", sc_id=sc_id)
    return run


def load(sc_id: str, *, runs_dir: Path | None = None) -> Run:
    root = (runs_dir or RUNS_DIR) / sc_id
    if not (root / "state.json").is_file():
        raise WorkflowError(
            f"no run journal for {sc_id}; start one with: "
            f"python3 Germanic/tools/adjudicate.py {sc_id} --run start")
    return Run(sc_id, root)


def set_scientific_reference(run: Run, commit: str, reason: str) -> None:
    """Record the explicitly chosen scientific baseline commit for this run.

    Incremental regression keeps its default compared states; this record
    prevents an agent from mistaking HEAD's first parent for the last
    scientifically accepted baseline when intermediate commits intervene.
    """
    state = run.state()
    state["scientific_reference_state"] = {"commit": commit, "reason": reason}
    run._write_state(state)
    run._event("scientific_reference_set", commit=commit, reason=reason)


def record_comparison(run: Run, *, kind: str, compared: dict,
                      receipt: dict | None = None) -> None:
    """Journal which comparison was actually performed (current validation,
    incremental Git regression, or explicit historical replay)."""
    allowed = {"current_validation", "incremental_regression",
               "historical_replay"}
    if kind not in allowed:
        raise WorkflowError(f"comparison kind {kind!r} not in {allowed}")
    run._event("comparison_performed", comparison=kind, compared=compared,
               receipt=receipt or {})


def record_incremental_regression(run: Run, result: dict) -> None:
    """Journal an ``incremental_regression.run_comparison`` result.

    Records the exact Git states and basis the existing tool resolved
    (staged-vs-HEAD, HEAD-vs-first-parent including the explicit merge
    caveat, or --worktree), so an agent never mistakes HEAD's first
    parent for the last scientifically accepted baseline.  The default
    comparison behaviour of incremental_regression is unchanged.
    """
    states = result.get("states")
    if not states or "basis" not in states:
        raise WorkflowError(
            "record_incremental_regression expects the dict returned by "
            "incremental_regression.run_comparison (with resolved 'states')")
    record_comparison(run, kind="incremental_regression", compared=states,
                      receipt={
                          "identical": result.get("identical"),
                          "foma_invocations": result.get(
                              "foma_invocations"),
                          "limitations": result.get("limitations", []),
                      })


VALIDATION_LEVELS = {"A", "B", "C"}


def record_validation_level(run: Run, level: str, receipts: list,
                            reused_evidence: list | None = None) -> None:
    """Journal a validation pass, separating executed checks from evidence.

    ``receipts`` are run_logged receipts for checks actually executed now;
    ``reused_evidence`` lists checks satisfied by previously verified
    results, each of which must carry a ``basis`` describing where that
    verification is recorded.  Reused evidence is never counted as a
    fresh execution.
    """
    if level not in VALIDATION_LEVELS:
        raise WorkflowError(
            f"validation level {level!r} not in {sorted(VALIDATION_LEVELS)}")
    reused = reused_evidence or []
    missing = [item for item in reused
               if not (isinstance(item, dict) and item.get("basis"))]
    if missing:
        raise WorkflowError(
            "reused validation evidence must record the basis of its prior "
            f"verification; missing on: {missing}")
    run._event("validation_level", level=level,
               executed=[{"label": r.get("label", "?"),
                          "ok": bool(r.get("ok")),
                          "returncode": r.get("returncode")}
                         for r in receipts],
               reused=reused,
               source_identity=adjudication_control.source_identity())


def main() -> int:
    args = sys.argv[1:]
    if len(args) >= 2 and args[1] == "start":
        run = start(args[0])
        print(f"run started: {run.root}")
        print(run.report())
        return 0
    if len(args) >= 2 and args[1] == "status":
        run = load(args[0])
        print(run.report())
        return 0
    print("usage: adjudication_run.py SCNNN start|status "
          "(richer transitions go through adjudicate.py --run ...)",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.path.insert(0, str(REPO_ROOT / "Germanic/tools"))
    raise SystemExit(main())
