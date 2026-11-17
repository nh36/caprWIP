# SC046 source-bound experiments

The [adjudication memorandum](../sc046-adjudication.md) defers executable
adoption. Production source, selected inputs and frozen baselines remain
those of starting `update` commit
`aea30b033f911d7417f8e38f87b02c9b35cbcda9`: 386/394, with the same eight
mismatches. No earlier archive is replaced.

## What is preserved

`manifest.json` hashes the actual initial and follow-up workers, their
unaltered JSON stdout and `provenance.json`. Provenance includes immutable
snapshot inputs/plans, command/completion receipts, source identity before
and after execution and empty successful stderr. Both successful receipts
record `source_changed=false`. The initial bootstrap's pre-Foma path error
and failed receipt are retained, not omitted. Private absolute receipt
paths describe the original execution machine; the public copies preserve
the recorded bytes and hashes without pretending those paths are portable.

The initial ten-network trial records all 394 rows under both restrictions,
each output set, rejection, ambiguity, target and change flag. The
stressed-target restriction changes only rainbow to *reġneafoga* (385/394).
The no-geminate restriction changes *lappa* to *læppa* and *tappa* to
*tæppa*, trading matches (386/394). Neither rejects or branches.
Independent *crabba/racca* component controls refute the blanket geminate
ban. The follow-up fixes SC047 before both competing operations and
locates the compound divergence specifically at SC059.

`proposed-stressed-target.patch` is an **unapplied** review diff for the
exact initial worker's `AF46S` definition, renamed `OEARestoration`.
It is not a production-ready correction: rainbow's exposed interaction
must be resolved on independent historical evidence first.

## Execution and regression ownership

Scientific predictions were written before execution in
[the source assessment](../../literature_dossiers/sc046-a-restoration/04-source-assessment.md);
the follow-up's distinct preregistration is also in its immutable plan.
The first order prediction was refuted, and remains in the record.
Exact tokenized intermediates are in `queries` in each observed JSON.

The experiment's cheap current-state mode reads two manifest-validated
cumulative snapshots and the manifest-validated final network:

```sh
docker compose exec -T backend python3 \
  docs/sound_changes/audits/sc046-restoration-evidence/experiment.py --production
cd Germanic/tests
python3 -m pytest -q test_sc046_adjudication.py test_sc041_adjudication.py \
  test_chronology_consistency.py
```

The SC046 module's two portable nodes authenticate the historical trials
and assert complete deltas plus decisive intermediates. They are not
represented as fresh counterfactual execution. Its sole runtime node
`test_current_production_restoration_positives_and_scoped_residue` adds
eleven selected rows in three batched lookups: no compiler, definition
preparation, rebuild, new corpus sweep or concurrency change. The existing
SC041 owner supplies its bleeding intervention; the existing strict corpus
owner supplies full current-production equivalence.

Optional scientific recapture from the repository root uses
`python3 Germanic/docs/sound_changes/audits/sc046-restoration-evidence/experiment.py
--capture-full` or `--capture-followup`. These create new isolated trials;
they do not overwrite these records. They are not routine test commands.

## Actual one-off cost

| Trial | Variants / emitted networks / Foma calls | Foma wall | Worker end-to-end | Peak actual Foma RSS |
|---|---|---|---|---|
| Initial | Two restrictions plus current/local/order controls; 10 / 1 | 300.260 s | 300.723 s | 2,790,788 KiB |
| Follow-up | Fixed-exposure order pair plus compound checkpoints; 6 / 1 | 438.400 s | 438.968 s | 2,790,396 KiB |

These are full-source standalone captures; no shared session image existed
for reuse. There was no separate image/fixture preparation process.
Common-definition evaluation is included in each Foma wall measurement,
not separately timed or claimed as free setup. Memory is the Linux Foma
child's `os.wait4(...).ru_maxrss`, not host Python or total-container RSS.
The trials answer different scientific questions and do not support a
performance comparison. Recurring compiler work is unchanged at zero
for the added SC046 owner.

Canonical `SC046 --evidence` regeneration was required and took 8m33s,
including the forced production/stage rebuild and full 394-row equivalence.
Its diagnostic receipt records source-card/bibliography edits during that
run; it is not an exact-final-candidate certificate. Final adjudication
validation uses the existing source-bound A/B/C receipts and JUnit reports,
not a second certification system.
