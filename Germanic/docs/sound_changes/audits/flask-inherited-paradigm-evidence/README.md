# Flask research evidence

Reference: `2805d98ae5ecf7df33c65dc0caf7d9df2ed22077`.
These observations were frozen before the research branch's prose/comment
changes. They are not a claim that later commits have already passed CI.

`matrix.tsv` and `corpus_outputs.tsv` give all ten variants and every
accepted row. `probes.tsv` distinguishes normal-entry rejections from
named-boundary diagnostics. `stage_traces.tsv` retains all changing and
critical unchanged stages for the principal witnesses and every class
probe. `live_firings.tsv` is the complete current394 census at the
recorded affected/diagnostic stages, including zero-final-delta trials.
Empty fields in raw traces mean rejection, not an empty-word success.
`attestations.tsv` distinguishes manuscript readings, editorial/Latin
lookalikes and secondary compound corroboration.

`orders.json`, the two recipes and the five drivers preserve the exact
scientific definitions, input construction, compiler and execution.
`executions.json` records original immutable receipt/completion digests,
input/driver digests, actual command statuses and log digests. Original
full receipts and unabridged stage outputs remain in the named
`.capr-work/experiments/` snapshots; this export avoids duplicating every
large intermediate JSON and local absolute path.

## Reproduction

Use a separate clean checkout at the exact reference SHA and a healthy
canonical Docker backend. Never use host Foma. Copy the five `.py` files
from this evidence directory into that checkout's
`.capr-work/flask-research/` directory, then run from that checkout's root:

```sh
docker compose ps
docker compose exec -T backend sh -c 'test -d /usr/app/fsts && command -v foma && command -v flookup'
python3 .capr-work/flask-research/raw_experiment.py
python3 .capr-work/flask-research/secondary_experiment.py --secondary-n
python3 .capr-work/flask-research/front_controls.py
python3 .capr-work/flask-research/shortening_order.py
python3 .capr-work/flask-research/following_high.py --following-high
```

The raw experiment compiles independent full roots and all components.
The secondary-n driver separately compiles its three roots and checks
full/composed equality. The last three assays reuse the first experiment's
hash-pinned stage bins; they do not compile new whole-root networks.
Run in this order in a fresh experiment namespace: completed snapshot
IDs deliberately cannot be reused or silently overwritten.

The two root drivers' exported versions differ from their recorded
original driver digests only by reading the terminal stdout log before
snapshot promotion. The Foma worker and recipe are unchanged. The
original scientific receipts passed; the old host print attempted a
now-relocated staging path and returned1 after successful sealing.
The initial raw empty-batch attempt and the two failed front-control
setup attempts produced no accepted results and are not represented
as scientific passes.

`source_images.tsv` fingerprints the inspected original-page images
without copying source scans into the repository. The source ledger
supplies edition identities and printed locators; local images are
provenance records, not newly claimed publicly distributed holdings.

Structural wasċe/þersċe/disċes/discas controls are not newly authenticated
full PGmc reconstructions. The inherited accusative-plural route was not
run; contextual OE accusative-plural attestations must not be confused
with a completed reconstruction.
