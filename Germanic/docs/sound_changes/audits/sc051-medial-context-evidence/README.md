# SC051 medial-context experiment

Reference: `77f314bf85035c23706b6b09b3a1855aa23c0620`, the verified
PR10 candidate after PR9 integration. Production is unchanged.

`experiment.py` reproduces the seven immutable v2 variants in the
canonical backend. Run from the repository root with the reference
history available and the ordinary backend running:

```sh
python3 Germanic/docs/sound_changes/audits/sc051-medial-context-evidence/experiment.py
```

Completed snapshot IDs are immutable; a fresh replay needs a new
experiment ID. Every selected raw input traverses all compiled stage
relations. Identity is compared with the canonical whole-cascade bin.
The variant results are not claimed as separate whole-root compiles.

`matrix.tsv` gives counts; `corpus_outputs.tsv` gives all394 outputs
for every variant; `delta.json` lists every changed final.
`controls.tsv` separates atomic consonant results from artificial
suffix replays; `stage_traces.tsv` preserves the selected decisive
histories and explicitly labelled stage-entry probes.
`live_firings.tsv`, `orders.json`, `recipe.json` and `execution.json`
provide complete firing, order and execution provenance.
The superseded whole-root compile timeout remains recorded as failed.
