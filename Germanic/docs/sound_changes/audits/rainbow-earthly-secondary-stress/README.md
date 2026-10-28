# Rainbow and earthly: isolated secondary-stress research

Branch: `research/compound-secondary-stress`.
Base: `3cb109c981c8868bf383172e2be06cdc88c00fb0`.
This is a research result, not a production implementation or publication.

The joint experiment derives selected *weorold* and *reġnboga*, and
predicted strong genitive *eorþcundes*, with one inherited-accent deletion.
All 389 selected outputs and both protected 380 populations remain unchanged.
The genitive is a reconstructed cell, not a recovered manuscript occurrence.
Read [adjudication.md](adjudication.md) for the qualified adoption-review
verdict and the failures that this result does not resolve.

## Reproduce

Run from this branch/worktree with the normal backend container already
running and its canonical scientific sources/runtime matching the base:

```sh
python3 Germanic/docs/sound_changes/audits/rainbow-earthly-secondary-stress/reproduce.py
python3 -m unittest discover \
  -s Germanic/docs/sound_changes/audits/rainbow-earthly-secondary-stress \
  -p test_experiment.py
```

The first command stages a `git archive` of the exact base and this research
directory inside a newly allocated private backend directory. It uses the
existing compiler, evaluator, pipeline and baseline helpers without editing
them. All Foma execution is inside the backend container. Compilations use
separate temporary directories, relative save paths, and no canonical
installation. The private snapshot is removed in `finally`; an interrupted
run may leave only its specifically named private directory for recovery.

Reproduction intentionally fails if the mounted scientific inputs have
drifted, canonical bins are stale, identity disagrees with any canonical
snapshot, the frozen baseline differs, a tested stage has multiple distinct
forward outputs, or protected files change during the assay. Do not repair
such failures by refreshing production as part of this research. The
receipt includes the container's existing runtime hashes, so reproduction
means equivalent observations, not identical host/runtime-dependent gzip
bytes.

The final archival run used `--container capr-secondary-stress-e8b280d3`,
an unmounted temporary container from the same `capr-backend` image.
Its `/usr/app` reference tree was copied read-only from the normal backend;
the wrapper still compiled elsewhere and verified reference identity at
every stage. This avoids another session rebuilding the shared bins during
the assay. The container was removed after the bounded command completed.
The default command above remains appropriate when the normal runtime is
not being rebuilt concurrently.

## Contents and receipt navigation

| File | Purpose |
|---|---|
| `literature.md` | Proposition-led review, page citations, direct/inferred evidence and access gaps |
| `lexical-evidence.md` | Documentary cells, reconstruction authority, missing attestations and controls |
| `experiment.py` | Definitions, 19 sequences, private compilation, full traces and preservation guards |
| `reproduce.py` | Host staging, invocation, receipt copying and targeted cleanup |
| `results.json.gz` | Complete matrix and before/after canonical hashes |
| `functionality.json.gz` | Whole-relation checks, ambiguous-domain extraction and inherited parser witness |
| `test_experiment.py` | Portable assertions over the actual receipts |
| `source-holdings.json` | Research-local source provenance; no full copyrighted works |
| `environment.md` | Shared-session interference and discarded development assays |
| `adjudication.md` | Scientific verdict, chronology classification and future-only change plan |

Load either compressed receipt with Python's `gzip.open(..., "rt")` and
`json.load`. In `results.json.gz`, `canonical_order` and
`canonical_definition_text` preserve the baseline. `definitions` and each
`models[NAME].order` specify the exact experiment. Every model contains
selected `final`, `counts`, `final_deltas`, full `transitions` (including
nonfirings and immutable380 original-input states), and candidate `steps`,
rejection and first aligned divergence.
`population_checks` includes active380 hashes and immutable380 original-input
outputs/deltas. `components` holds independent controls.

The main added sound operations pass Foma's forward functionality test.
This is not a claim that the entire inherited parser is functional:
both old and private-extended parsers map `biu` to two distinct starred
segmentations. Three internal annotation/sensitivity networks also produce
disagreement between Foma's functionality and empty-ambiguous-domain tests;
both results are preserved, not converted into a blanket success flag.
The main `RFoot` and `RLate` operations pass both tests. Reverse lookup is
not required to be unique.

## Scope and stopping point

Every tracked production file in this worktree remains byte-identical to
the base. Canonical FSTs, corpus, selections, registry, chronology, readers,
lexical reports, book manifests, baselines, old receipts and runtime were
not edited or installed. The accepted assay verifies canonical before/after
hash equality. External work in the original `update` worktree is disclosed
in `environment.md`, not misattributed to this branch.

No lexical admission, new stress law, registry verdict, production refresh,
publication build, merge or adoption PR is part of this assignment.
The stopping point is one research commit pushed to this branch.
