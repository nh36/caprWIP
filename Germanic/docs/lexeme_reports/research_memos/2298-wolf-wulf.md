# Research memo — 2298 wolf / wulf

## Starting point
- ID: 2298
- CONCEPT: wolf
- COUNTERPART: `wulf`
- TSV `PROTO`: `*wúlfaz`
- TSV `PROTOFORM`: `*wúlfaz`
- TSV `DERIVATION_CLASS`: `unexplained_unmodelled`
- TSV `NOTE`: the row already treats `wulf` as a documented exception to regular u-lowering, cites Campbell §115, and explains why a high-vowel escape hatch such as `*wulfi` would only trade a-umlaut for i-umlaut.

## Packet evidence assessment
- **Authoritative/current:** the TSV row; the current debug/compact derivation trace (`*wúlfaz -> wolf`, expected `wulf`); `oe_known_problems.tsv`; the project-status entry in `DEV_NOTES.md`; and especially `DEV_NOTES §17.10.34a`, which records the failed paradigm-cell experiment and the current conclusion.
- **Useful background:** the broader u-lowering-exception discussion in `DEV_NOTES` and `Germanic/docs/analysis/notable_findings.md`, because they show the comparative and literature context for the whole exception cluster.
- **Stale or superseded:** packet hits from `DEV_NOTES §17.10.34` proposing `*wúlfis -> wulfes` as a regular repair. `§17.10.34a` explicitly retracts that plan after rebuild and probe.
- **Irrelevant or misleading:** generic packet hits on unrelated dialect material. Under `packet_quality_notes.md`, the mere appearance of the protoform in old development notes is not enough to treat a superseded recommendation as current evidence.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at the early u-lowering overview, the project-status block, `§17.10.34`, and `§17.10.34a`
- `Germanic/data/oe_known_problems.tsv`
- `Germanic/docs/analysis/notable_findings.md`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.compact.md`
- `Germanic/data/old_english_wiktionary.tsv`

The packet did not name any separate full dossier file for this row.

## Reconstruction and early-stage forms
The cognate-set headword and row input remain masculine a-stem `*wúlfaz`. The regular chain reflected by the current FST is straightforward:

`*wúlfaz > *wólfaz > *wólfa > wolf`.

That is the regular comparator, and the OHG parallel `wolf` supports it. The crucial negative result from `DEV_NOTES §17.10.34a` is that a high-vowel paradigm cell does not rescue the row. Inputs such as reconstructed `*wulfi` / `*wúlfis` are not rival headwords; they are hypothetical oblique cells. They do block u-lowering, but the same high vowel then triggers i-umlaut, so their regular outcomes are `**wylf` / `**wylfe`, not bare `wulf`.

So the row’s reconstruction problem is not “find the right paradigm cell.” The repo’s current position is that no PGmc/NWGmc input form yields attested `wulf` by regular sound change alone.

## Old English philology
`wulf` is an attested OE citation form. `old_english_wiktionary.tsv` confirms the ordinary dictionary lemma, but the philological issue is not attestation; it is regularity. The repo evidence supports the following distinction:
- **Attested lemma:** `wulf`
- **Attested oblique form:** `wulfe`, but treated in `DEV_NOTES §17.10.34a` as analogically levelled, not as the straightforward regular outcome of `*wulfi`
- **Regularly expected outcomes from reconstructed preforms:** `wolf` from low-vowel cells, `**wylf/**wylfe` from high-vowel cells

The memo should therefore avoid implying a fully secure reconstructed “surface `wulf-` paradigm.” Repo-local evidence securely supports analogical reshaping of at least the attested forms, but the exact historical route is still a documented exception rather than a recoverable regular paradigm.

## Project problem and solution
The project problem was whether row 2298 could be repaired by switching away from nominative `*wúlfaz` to a supposedly regular oblique cell such as `*wúlfis`. `DEV_NOTES §17.10.34a` shows why that fails: if the high vowel is present early enough to block u-lowering, it is also early enough to trigger i-umlaut. The attempted repair was therefore both computationally and philologically wrong.

The current repo solution is the right one: keep `*wúlfaz`, keep the attested target `wulf`, classify the row as `unexplained_unmodelled`, and explain the row as a genuine documented exception rather than as a solvable phonological mismatch.

## Paradigm probe
No further paradigm probe is required. The crucial probe has already been done in `§17.10.34a`, and it produced the decisive negative result: high-vowel cells do not yield `wulf`; they yield i-umlauted forms instead. A final report may mention the oblique evidence, but it does not need a new probe cycle.

## Recommended final report
Recommend a final report that treats `wulf` as an attested Old English documented exception to regular u-lowering from `*wúlfaz`, uses FST `wolf` and OHG `wolf` as the regular comparator, and explicitly rejects `*wulfi/*wúlfis` as the row’s source because those would give i-umlauted outcomes.

## Data-change recommendations
- TSV `PROTO`: no change.
- TSV `PROTOFORM`: no change.
- TSV `COUNTERPART`: no change.
- TSV `DERIVATION_CLASS`: no change.
- TSV `NOTE`: yes, minor cleanup recommended. Cite `§17.10.34a` (or `§§17.10.34–34a`), not only `§17.10.34`, so the row points readers to the current conclusion rather than the withdrawn paradigm-cell proposal.
- `oe_known_problems.tsv`: no change.
- `DEV_NOTES` or dossier text: yes, editorial cleanup would help. `§17.10.34` should be marked more visibly as superseded by `§17.10.34a`, since packets still surface the obsolete `*wúlfis -> wulfes` plan.
