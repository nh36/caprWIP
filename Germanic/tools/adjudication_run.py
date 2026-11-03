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
import csv
import io
import json
import re
import shutil
import sys
import tempfile
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


def _command_executable(receipt: dict) -> Path | None:
    path = receipt.get("executable_path")
    return Path(path).resolve() if path and Path(path).is_file() else None


def _python_arguments(receipt: dict) -> list[str] | None:
    """Recognise installed Python invocations, not shell or -c wrappers."""
    argv = receipt["argv"]
    executable = _command_executable(receipt)
    interpreters = {Path(sys.executable).resolve()}
    interpreters.update(Path(p).resolve() for name in ("python", "python3")
                        if (p := shutil.which(name)))
    if executable not in interpreters:
        return None
    args = argv[1:]
    while args and args[0] in ("-B", "-u", "-E", "-s", "-I", "-P"):
        args = args[1:]
    return args


def _script_arguments(receipt: dict, relative: str) -> list[str] | None:
    entry = (REPO_ROOT / relative).resolve()
    if not entry.is_file():
        return None
    args = _python_arguments(receipt)
    if args and not args[0].startswith("-") and (Path(receipt["cwd"]) / args[0]).resolve() == entry:
        return args[1:]
    if _command_executable(receipt) == entry:
        return receipt["argv"][1:]
    return None


def _focused_tests(receipt: dict) -> bool:
    args = _python_arguments(receipt)
    if args and args[:2] == ["-m", "pytest"]:
        args = args[2:]
    else:
        pytest = shutil.which("pytest")
        if not pytest or _command_executable(receipt) != Path(pytest).resolve():
            return False
        args = receipt["argv"][1:]
    if {"--collect-only", "--collectonly", "--co", "--help", "-h", "--version", "-V"} & set(args):
        return False
    tests = (REPO_ROOT / "Germanic/tests").resolve()
    if Path(receipt["cwd"]).resolve().is_relative_to(tests) and any(
            arg in ("-k", "-m") and i + 1 < len(args) and args[i + 1].strip()
            for i, arg in enumerate(args)):
        return True
    for arg in args:
        path = (Path(receipt["cwd"]) / arg.split("::", 1)[0]).resolve()
        if (path.is_relative_to(tests) and path.is_file()
                and path.name.startswith("test_") and path.suffix == ".py"):
            return True
    return False


def _cell_transition_files(transition: dict, directory: Path) -> dict[Path, bytes]:
    """Derive exact protected effects by rehearsing the existing cell adopter."""
    import cascade_baseline as baseline

    required = {"approval_filename", "approval", "candidate", "migrations"}
    if not isinstance(transition, dict) or set(transition) != required:
        raise ValueError("invalid controlled cell-transition declaration")
    filename = transition["approval_filename"]
    if (not isinstance(filename, str)
            or not re.fullmatch(r"approved_[a-z0-9_]+_migration\.json", filename)
            or (directory / filename).exists()):
        raise ValueError("cell transition requires a new, explicitly named approval")
    approval, candidate = transition["approval"], transition["candidate"]
    previous = baseline.read_baseline(
        directory / "cascade_baseline_outputs.tsv",
        directory / "cascade_baseline_summary.json")
    baseline.validate_cell_transition(previous, candidate, approval)
    migration_path = directory / "approved_input_migrations.tsv"
    with migration_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields, existing = reader.fieldnames, list(reader)
    old_records = {r["row_id"]: r for r in previous["records"]}
    additions = [
        dict(row_id=c["row_id"], concept=old_records[c["row_id"]]["concept"],
             counterpart=c["before"]["counterpart"],
             new_counterpart=c["after"]["counterpart"],
             old_proto=c["before"]["proto"], new_proto=c["after"]["proto"],
             old_outputs=c["before"]["outputs"], new_outputs=c["after"]["outputs"],
             adjudication_memo=approval["adjudication_memo"])
        for c in approval["changes"]]
    if transition["migrations"] != existing + additions:
        raise ValueError("cell migration must preserve every earlier approval and append exactly its declared changes")
    original = migration_path.read_bytes()
    if not original.endswith(b"\n"):
        raise ValueError("existing migration ledger lacks its final newline")
    stream = io.StringIO(newline="")
    csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n").writerows(additions)
    migrations = original + stream.getvalue().encode("utf-8")
    suffix = approval["adjudication"].lower()
    if "transition_id" in approval:
        suffix += "_" + approval["transition_id"]
    archives = [f"cascade_baseline_{kind}_pre_{suffix}.{extension}"
                for kind, extension in (("outputs", "tsv"), ("summary", "json"))]
    if any((directory / name).exists() for name in archives):
        raise ValueError("cell transition cannot overwrite an existing pre-transition archive")
    with tempfile.TemporaryDirectory(prefix="capr_cell_plan_") as temporary:
        isolated = Path(temporary)
        for name in ("cascade_baseline_outputs.tsv", "cascade_baseline_summary.json",
                     "cascade_baseline_outputs_legacy380.tsv"):
            shutil.copyfile(directory / name, isolated / name)
        (isolated / migration_path.name).write_bytes(migrations)
        baseline.adopt_cell_baseline(candidate, isolated, approval)
        files = {directory / name: (isolated / name).read_bytes() for name in [
            "cascade_baseline_outputs.tsv", "cascade_baseline_summary.json", *archives]}
    files[migration_path] = migrations
    files[directory / filename] = (
        json.dumps(approval, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return files


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

    def _input_hashes(self, extra_paths=()) -> dict:
        paths = [Path(p) for p in extra_paths]
        paths.extend(p for domain in ("executable_model", "corpus", "registry", "memo")
                     for p in _domain_files(domain, self.sc_id))
        return {str(p.resolve()): hashlib.sha256(p.read_bytes()).hexdigest()
                if p.is_file() else "absent"
                for p in paths}

    def begin_propagation(self, modifications: dict[str, str]) -> None:
        """Before edits, pin the decision's exact SOURCE paths and target hashes."""
        self.refresh_validity()
        state = self.state()
        if self.frontier() != "PROPAGATE" or state.get("propagation"):
            raise WorkflowError("begin propagation requires a valid DECIDE and no existing propagation")
        decision = state["stages"]["DECIDE"]["evidence"]
        if modifications != decision["intended_source_modifications"]:
            raise WorkflowError("propagation modifications must agree with the recorded decision")
        before = self._input_hashes()
        executable = {str(p.resolve()) for domain in ("executable_model", "corpus")
                      for p in _domain_files(domain, self.sc_id)}
        import artifact_graph
        generated = {p.resolve() for node in artifact_graph.nodes() for p in node.outputs()}
        targets = {}
        for ref, sha in modifications.items():
            path = (REPO_ROOT / ref).resolve()
            if (artifact_graph.propagation_path_kind(path, generated=generated) != "SOURCE"
                    or not re.fullmatch(r"[0-9a-f]{64}", sha)):
                raise WorkflowError(f"not an authorised SOURCE path/hash: {ref}")
            if "DEFER" in decision["verdict"].split("/") and str(path) in executable:
                raise WorkflowError("DEFER permits documentation, not executable or selected-input propagation")
            targets[str(path)] = sha
        if transition := decision.get("cell_transition"):
            try:
                files = _cell_transition_files(transition, artifact_graph.BASELINE_DIR)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                raise WorkflowError(f"invalid approved cell transition: {exc}") from exc
            targets.update({str(p.resolve()): hashlib.sha256(data).hexdigest()
                            for p, data in files.items()})
            before.update(self._input_hashes(
                p for p in artifact_graph.BASELINE_DIR.iterdir()
                if p.is_file() and p.resolve() not in generated))
        before.update(self._input_hashes(targets))
        state["stages"]["PREFLIGHT"]["scope"] = "investigation"
        state["propagation"] = {"before": before, "targets": targets,
                                "pre_change_source": adjudication_control.source_identity(),
                                "generated_paths": [str(Path(p).relative_to(REPO_ROOT))
                                                    for p in generated
                                                    if Path(p).is_relative_to(REPO_ROOT)],
                                "started_at": adjudication_control._utcnow()}
        self._write_state(state)
        self._event("propagation_started", modifications=modifications)

    def _sanctioned_changes(self, state: dict) -> bool:
        propagation = state.get("propagation")
        if not propagation:
            return False
        current = self._input_hashes(propagation["before"])
        if propagation.get("completed_hashes"):
            experimental_paths = {str(p.resolve()) for domain in ("executable_model", "corpus")
                                  for p in _domain_files(domain, self.sc_id)}
            return all(current.get(p) == propagation["completed_hashes"].get(p)
                       for p in experimental_paths)
        before_source = propagation["pre_change_source"]
        current_source = adjudication_control.source_identity()
        if current_source.get("head_commit") != before_source.get("head_commit"):
            return False
        before_changes = before_source.get("worktree_changes", {})
        current_changes = current_source.get("worktree_changes", {})
        source_delta = {p for p in before_changes.keys() | current_changes.keys()
                        if before_changes.get(p) != current_changes.get(p)}
        allowed = set(propagation["generated_paths"])
        import artifact_graph
        allowed.update(str(p.relative_to(REPO_ROOT))
                       for node in artifact_graph.nodes() for p in node.outputs()
                       if p.is_relative_to(REPO_ROOT))
        allowed.update(str(Path(p).relative_to(REPO_ROOT))
                       for p in propagation["targets"] if Path(p).is_relative_to(REPO_ROOT))
        if source_delta - allowed:
            return False
        changed = {path for path in current.keys() | propagation["before"].keys()
                   if current.get(path) != propagation["before"].get(path)}
        return changed <= propagation["targets"].keys()

    def refresh_validity(self) -> list[str]:
        """Re-check every completed stage against current source identities.

        Invalidates exactly the stages whose own dependency domains changed
        (and records why); unrelated stages are untouched.  Returns the
        names of newly invalidated stages.
        """
        state = self.state()
        sanctioned = self._sanctioned_changes(state)
        invalidated = []
        for stage in STAGES:
            record = state["stages"].get(stage)
            if not record or record.get("status") != "complete":
                continue
            if stage in FROZEN_AFTER_PROPAGATE and sanctioned:
                continue  # the propagated edit was the sanctioned change
            if stage == "PREFLIGHT" and sanctioned:
                propagation = state["stages"].get("PROPAGATE", {})
                if (not state["propagation"].get("completed_hashes")
                        or (state["propagation"].get("finalization_preflight")
                            and propagation.get("domain_identities") == self._current_identities(
                                STAGE_DOMAINS["PROPAGATE"]))):
                    # This gate remains evidence of investigation prerequisites,
                    # not certification of the edited state. Finalisation has its
                    # own fresh, source-bound preflight below.
                    continue
            stale = []
            for domain, recorded in record.get("domain_identities",
                                               {}).items():
                current = domain_identity(domain, self.sc_id)
                if current != recorded:
                    stale.append(domain)
            if stage == "PROPAGATE":
                accepted = state["propagation"]["completed_hashes"]
                current = self._input_hashes(state["propagation"]["targets"])
                if any(current[p] != accepted.get(p) for p in state["propagation"]["targets"]):
                    stale.append("propagated_sources")
            if (stage == "VALIDATE"
                    and record["source_identity"]["identity_sha256"] !=
                    adjudication_control.source_identity()["identity_sha256"]):
                stale.append("validated_source_identity")
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
        summary = operations_summary(self)
        if summary:
            lines.append("operations:")
            for kind in sorted(summary):
                entry = summary[kind]
                extra = (f", {entry['redundant']} redundant"
                         if entry["redundant"] else "")
                lines.append(
                    f"  {kind}: {entry['count']} "
                    f"({entry['elapsed_seconds']:.0f}s{extra})")
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
        if stage == "SNAPSHOT":
            if evidence.get("no_executable_experiment"):
                if not isinstance(evidence["no_executable_experiment"], str):
                    raise WorkflowError("no-experiment exception requires a documented reason")
            else:
                import experiment_snapshot
                try:
                    snapshot = experiment_snapshot.Snapshot(Path(evidence["snapshot_root"]))
                    snapshot.verify()
                except (KeyError, OSError, ValueError, RuntimeError) as exc:
                    raise WorkflowError(f"SNAPSHOT requires a real verified snapshot: {exc}") from exc
        if stage == "INVESTIGATE" and evidence.get("experiments"):
            snapshot_record = state["stages"]["SNAPSHOT"]["evidence"]
            if snapshot_record.get("no_executable_experiment"):
                raise WorkflowError("executable experiments cannot use the no-experiment exception")
            for experiment in evidence["experiments"]:
                if Path(experiment.get("snapshot_root", "")).resolve() != Path(snapshot_record["snapshot_root"]).resolve():
                    raise WorkflowError("executable experiment was not compiled from the recorded snapshot")
                try:
                    adjudication_control.verify_receipt(experiment["receipt"], current=False)
                except (KeyError, OSError, ValueError) as exc:
                    raise WorkflowError(f"experiment execution receipt invalid: {exc}") from exc
        if stage == "DECIDE":
            self._check_decision(evidence)
        if stage == "VALIDATE":
            self._check_validation(evidence)
        if stage == "PROPAGATE":
            propagation = state.get("propagation")
            if not propagation or not self._sanctioned_changes(state):
                raise WorkflowError("PROPAGATE requires a controlled begin and no unexpected edits")
            current = self._input_hashes(propagation["before"])
            if any(current[path] != sha for path, sha in propagation["targets"].items()):
                raise WorkflowError("PROPAGATE target hashes do not match the authorised modifications")
            receipts = evidence.get("receipts", [])
            if not receipts:
                raise WorkflowError("PROPAGATE requires successful finalisation execution receipts")
            decision = state["stages"]["DECIDE"]["evidence"]
            transition = decision.get("cell_transition")
            adopter = ([transition["approval"]["adjudication"], "--adopt-cell-baseline",
                        "--approval", transition["approval_filename"]] if transition else None)
            for receipt in receipts:
                try:
                    is_adoption = adopter is not None and _script_arguments(
                        receipt, "Germanic/tools/adjudicate.py") == adopter
                    adjudication_control.verify_receipt(
                        receipt, allow_source_change=True, current=not is_adoption)
                except (ValueError, OSError, KeyError) as exc:
                    raise WorkflowError(f"PROPAGATE receipt invalid: {exc}") from exc
            commands = [_script_arguments(r, "Germanic/tools/adjudicate.py") for r in receipts]
            coordinated = decision.get("coordinated_adjudications", [self.sc_id])
            if any([sc, "--finalize"] not in commands for sc in coordinated):
                raise WorkflowError("PROPAGATE requires each SC-specific --finalize command")
            if adopter and adopter not in commands:
                raise WorkflowError("PROPAGATE requires the declared --adopt-cell-baseline receipt")
            preflights = [adjudication_control.preflight(sc, "finalize", probe_runner=False)
                          for sc in coordinated]
            for preflight in preflights:
                if preflight.blocked:
                    raise WorkflowError(f"finalisation preflight blocked: {preflight.render()}")
            final_preflight = preflights[0]
            certified_identity = receipts[-1]["source_identity_after"]["identity_sha256"]
            if (final_preflight.source.get("identity_sha256") != certified_identity
                    or adjudication_control.source_identity()["identity_sha256"] != certified_identity):
                raise WorkflowError("SOURCE changed after the finalisation receipt")
            propagation["finalization_preflight"] = final_preflight.to_json()
            propagation["coordinated_finalization_preflights"] = [
                preflight.to_json() for preflight in preflights]
            propagation["completed_hashes"] = current
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
        coordinated = evidence.get("coordinated_adjudications", [self.sc_id])
        if (not isinstance(coordinated, list) or self.sc_id not in coordinated
                or coordinated[0] != self.sc_id
                or any(not isinstance(sc, str) or not re.fullmatch(r"SC[0-9]{3}", sc)
                       for sc in coordinated) or len(set(coordinated)) != len(coordinated)):
            raise WorkflowError("coordinated adjudications must uniquely name the owning SCs, including this run")
        if transition := evidence.get("cell_transition"):
            if "DEFER" in tokens:
                raise WorkflowError("DEFER cannot authorise protected selected-cell adoption")
            try:
                if transition["approval"]["adjudication"] not in coordinated:
                    raise ValueError("cell approval is not owned by a declared coordinated adjudication")
                import artifact_graph
                _cell_transition_files(transition, artifact_graph.BASELINE_DIR)
            except (OSError, ValueError, KeyError, TypeError) as exc:
                raise WorkflowError(f"invalid approved cell transition: {exc}") from exc
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
        for receipt in receipts:
            try:
                adjudication_control.verify_receipt(receipt)
            except (ValueError, OSError, KeyError) as exc:
                raise WorkflowError(f"validation receipt invalid: {exc}") from exc
        levels = {r["level"] for r in receipts}
        if not {"A", "B", "C"} <= levels:
            raise WorkflowError("VALIDATE requires Level A, B and complete strict Level C evidence")
        integrated = set()
        for receipt in receipts:
            if receipt["level"] not in ("A", "B"):
                continue
            log = Path(receipt["stdout_log"]).read_text() + Path(receipt["stderr_log"]).read_text()
            if receipt["level"] == "A":
                semantics = _script_arguments(receipt, "Germanic/tools/check_reader_facing_semantics.py")
                if not ((_focused_tests(receipt) and re.search(r"\b[1-9]\d* passed\b", log))
                        or (semantics == [] and "Reader-facing semantic regression suite passed." in log)):
                    raise WorkflowError("Level A requires executed focused tests or the prescribed semantic regression suite")
            if receipt["level"] == "B":
                args = _script_arguments(receipt, "Germanic/tools/adjudicate.py")
                if args in (["--refresh"], ["--refresh", "--mode", "full"]) and re.search(
                        r"^CONTROL PLANE CLEAN$", log, re.MULTILINE):
                    integrated.add("refresh")
                elif args == ["--status"] and re.search(r"^STATUS OK\b", log, re.MULTILINE):
                    integrated.add("status")
                else:
                    raise WorkflowError("Level B requires the prescribed integrated --refresh/--status checks")
        if integrated != {"refresh", "status"}:
            raise WorkflowError("Level B requires both --refresh and --status execution receipts")
        strict = [r for r in receipts if r["level"] == "C"]
        lanes = {r["lane"] for r in strict}
        if not ({"serial", "exclusive"} <= lanes or
                {"independent", "runtime", "exclusive"} <= lanes):
            raise WorkflowError("incomplete strict-validation lanes (exclusive suite required)")
        for r in strict:
            argv = r["argv"]
            args = [arg for arg in argv[3:] if arg not in
                    ("-q", "--validation-mode=full", "--fresh-isolated-definitions")
                    and not arg.startswith("--junitxml=")]
            expected_args = {
                "serial": ["--ignore=test_evidence_interface.py"],
                "exclusive": ["test_evidence_interface.py"],
                "runtime": ["-m", "runtime", "--ignore=test_evidence_interface.py"],
                "independent": ["-m", "not runtime", "-n", "4", "--dist", "loadfile",
                                "--ignore=test_evidence_interface.py"],
            }
            if (argv[1:3] != ["-m", "pytest"] or args != expected_args.get(r["lane"])
                    or "--validation-mode=full" not in argv or r.get("pytest_addopts")):
                raise WorkflowError("strict-validation command does not match its lane")
            if r["lane"] == "serial" and r["test_counts"]["skipped"] < 5:
                raise WorkflowError("strict validation must preserve explicit historical-replay skips")
            log = Path(r["stdout_log"]).read_text() + Path(r["stderr_log"]).read_text()
            if not re.search(r"\b\d+ passed\b", log) or "failed" in log:
                raise WorkflowError("strict validation lacks executed passing test totals")


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


# ---------------------------------------------------------------------------
# resource budgets and failure controls
# ---------------------------------------------------------------------------

# Conservative defaults grounded in the measured pipeline (a full strict
# run uses one cascade build and ~20 min; adjudication experiments have
# needed at most a handful of variants). They are configurable per run via
# set_budget, and any excess requires an explicit, journaled override —
# never an arbitrary timeout that interrupts legitimate long computations.
DEFAULT_BUDGETS = {
    "experiment_variant": 12,
    "foma_compilation": 60,
    "cascade_evaluation": 20,
    "runtime_test": 60,
    "container_launch": 24,
    "definition_image_prep": 6,
    "full_suite": 3,
}
# Informational kinds: visibility only, never budgeted.
UNBUDGETED_KINDS = {"cache_hit", "cache_miss", "definition_image_reuse"}
OPERATION_KINDS = set(DEFAULT_BUDGETS) | UNBUDGETED_KINDS
# After this many failed repairs of the same underlying failure, the
# automatic repair loop must stop and report instead of retrying.
MAX_REPAIR_ATTEMPTS = 2


def _run_budget(state: dict, kind: str) -> int | None:
    if kind in UNBUDGETED_KINDS:
        return None
    return state.get("budgets", {}).get(kind, DEFAULT_BUDGETS[kind])


def set_budget(run: Run, kind: str, limit: int, reason: str) -> None:
    """Configure a per-run budget; the change and its reason are journaled."""
    if kind not in DEFAULT_BUDGETS:
        raise WorkflowError(
            f"no budget exists for {kind!r}; budgeted kinds: "
            f"{sorted(DEFAULT_BUDGETS)}")
    state = run.state()
    state.setdefault("budgets", {})[kind] = int(limit)
    run._write_state(state)
    run._event("budget_set", operation=kind, limit=int(limit), reason=reason)


def record_operation(run: Run, kind: str, *, identity: str | None = None,
                     elapsed_seconds: float | None = None,
                     ok: bool | None = None, label: str = "",
                     override_reason: str | None = None) -> dict:
    """Journal one expensive operation, enforcing budgets and flagging
    redundant repeats against unchanged inputs.

    ``identity`` should be a content identity of the operation's effective
    inputs (e.g. a compile-cache key or snapshot input hash).  If an
    earlier successful operation of the same kind recorded the same
    identity, the new record is flagged ``redundant`` and a warning event
    is journaled so the agent is informed before wasting the work again.

    Exceeding the kind's budget raises WorkflowError unless an explicit
    ``override_reason`` is supplied, in which case the override is
    journaled with its reason.
    """
    if kind not in OPERATION_KINDS:
        raise WorkflowError(
            f"unknown operation kind {kind!r}; kinds: "
            f"{sorted(OPERATION_KINDS)}")
    state = run.state()
    operations = state.setdefault("operations", [])
    previous = [op for op in operations if op["kind"] == kind]
    budget = _run_budget(state, kind)
    if budget is not None and len(previous) >= budget:
        if not override_reason:
            raise WorkflowError(
                f"budget exhausted for {kind}: {len(previous)} operations "
                f"recorded against a budget of {budget}. If more are "
                "genuinely required, pass an explicit override_reason "
                "(journaled) or raise the budget with set_budget")
        run._event("budget_override", operation=kind, budget=budget,
                   used=len(previous), reason=override_reason)
    redundant = bool(identity) and any(
        op.get("identity") == identity and op.get("ok") is not False
        for op in previous)
    record = {
        "kind": kind, "label": label, "identity": identity,
        "elapsed_seconds": elapsed_seconds, "ok": ok,
        "at": adjudication_control._utcnow(), "redundant": redundant,
    }
    operations.append(record)
    run._write_state(state)
    run._event("operation", operation=kind,
               **{k: v for k, v in record.items() if k != "kind"})
    if redundant:
        run._event(
            "redundant_operation_warning", operation=kind, identity=identity,
            advice="an equivalent operation already succeeded against the "
                   "same effective inputs; reuse its recorded result unless "
                   "fresh execution is scientifically required")
    return record


def record_repair_attempt(run: Run, failure_signature: str,
                          note: str = "") -> int:
    """Count repair attempts per underlying failure; stop the loop at the
    limit.  Returns the attempt number just recorded."""
    state = run.state()
    attempts = state.setdefault("repair_attempts", {})
    count = attempts.get(failure_signature, 0)
    if count >= MAX_REPAIR_ATTEMPTS:
        raise WorkflowError(
            f"{count} repair attempts have already failed for "
            f"{failure_signature!r}; stop the automatic repair loop and "
            "report the error, the evidence, the attempted repairs and the "
            "remaining uncertainty instead of retrying")
    attempts[failure_signature] = count + 1
    run._write_state(state)
    run._event("repair_attempt", failure=failure_signature,
               attempt=count + 1, note=note)
    return count + 1


def operations_summary(run: Run) -> dict:
    """Per-kind counts, elapsed time and redundancy, for status reports."""
    summary: dict = {}
    for op in run.state().get("operations", []):
        entry = summary.setdefault(
            op["kind"], {"count": 0, "elapsed_seconds": 0.0, "redundant": 0})
        entry["count"] += 1
        entry["elapsed_seconds"] += op.get("elapsed_seconds") or 0.0
        entry["redundant"] += 1 if op.get("redundant") else 0
    return summary


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
