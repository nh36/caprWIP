# SC036 isolated evidence

Current decision: [SC036 adjudication](../sc036-adjudication.md).
`evidence.json` is the pre-edit observation at the base commit recorded
inside it, not a replacement scientific baseline. `source-evidence.tsv`
records source claims and access qualifications; no original scholarly
PDF or page image is distributed here.

From the repository root:

```sh
python3 Germanic/tools/adjudicate.py SC036 --evidence
docker compose exec -T backend python3 \
  /usr/app/docs/sound_changes/audits/sc036-experiments/experiment.py \
  > /tmp/sc036-current-evidence.json
python3 -m pytest -q Germanic/tests/test_sc036_adjudication.py
```

The assay requires a fresh canonical build, compiles an isolated copy in
a container temporary directory using the existing shared compiler, and
cleans it up. It never replaces stage bins, production FSTs, corpus rows
or baseline files. It verifies identity against the production composition
and every cumulative named snapshot, runs the full 389 rows through each
counterfactual, and marks membership in the overlapping migration-aware
380 identities. No disjoint second population is invented.

The archived receipt records 17 complete-cascade model comparisons,
21 explicitly synthetic/component-level probes, formal shared-context
equivalence, technical marker interactions, complete changing traces of
the two positives and the real negative lung, and all private output
deltas. The current runner additionally tests source-motivated staged
alternatives; they are comparisons at the SC036 entry point, not
unlabelled Proto-Germanic attestations or new corpus selections.
`staged-evidence.json` preserves those later observations separately from
the pre-edit receipt. Rejected alternatives retain the exact rejecting
component, its input and the empty output set; they are not silently
discarded or reported as successful forms.

The “B-only” experiment deliberately compiles an isolated context-free
mapping. It must not be confused with extracting the grave target while
retaining the incumbent's shared context. Foma single-comma semantics is
checked against the explicitly conditioned union, not guessed from
indentation. The formal check uses `test equivalent` on the two private
component networks; the broader left-vowel-class candidate is explicitly
non-equivalent despite identical live finals.

Moving SC004 bodily earlier is also an experiment, not an adoption:
its thirteen other changed finals remain itemized. The three-component
controls separate class membership from final-u feeding without treating
those other effects as chronology evidence. Whole-cascade delay after
the current SC040 and the direct SC036/SC040 component comparison answer
different questions; the former crosses many intervening changes.

The frozen May/August chronology cards are not rewritten. Their old
coordinates and source revisions are discussed in the adjudication;
these modern experiments are not claimed as exact historical runtime
replays. Production definitions, selected outputs and protected baseline
digests remain unchanged by the adopted reformulation.
