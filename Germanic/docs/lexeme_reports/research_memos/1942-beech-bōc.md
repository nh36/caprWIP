# Research memo — 1942 beech / bōc

## Starting point
- ID: 1942.
- CONCEPT: beech.
- COUNTERPART: `bōc`.
- PROTO: `*bōkō`.
- PROTOFORM: `*bōkō`.
- DERIVATION_CLASS: `regular`.
- NOTE: “Kroonen *bōk(j)ō- f. > OE bōc (nom.sg.); bēċe is oblique form.”

## Packet evidence assessment
- **Authoritative/current:** the aligned TSV row; the packet’s compact current derivation (`*bōkō > bōc`); the current trace reports showing `EXPECTED: bōc`, `OUTPUTS: bōc`; and live `old_english.bin` probing (`bōkō -> bōc`).
- **Useful background:** older `DEV_NOTES` and full-trace snapshots where this item sat in `palatalization_missing`, because they explain why stale packet-era discussion still points toward `bēċe`; the lexical-table hit `beech -> bēċe`; and the nearby `book / bōc` row, which shows the homograph risk.
- **Stale or superseded:** February 2026 traces expecting `bēċe` directly from `*bōkō` and diagnosing `*bōkō -> bōcō/bucō` as the row’s live failure. Those are no longer current row-level evidence once the aligned TSV and current traces target nominative `bōc`.
- **Irrelevant or misleading:** treating the `book` row as if it proved the beech semantics, or treating the current FST’s `bōkjō`/`bōkjōz` probe outputs as direct attestation rather than project-internal paradigm diagnostics.

## Additional repo research
Checked beyond the packet:
- `Germanic/docs/DEV_NOTES.md` at the old mismatch discussion (`1715-1725`, `1760-1767`, `2478`, `2593-2605`).
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_short_o_fix.txt`.
- `Germanic/docs/debug_snapshots/oe_full_trace_report_2026-02-07_post_root_noun_fix.txt`.
- `Germanic/data/old_english_wiktionary.tsv`.
- `Germanic/data/germanic-aligned-final.tsv`, including row 1955 `book / bōc`.
- `Germanic/data/oe_known_problems.tsv` (checked; no row-specific entry).
- Live probe of `old_english.bin` with `bōkō`, `bōkjō`, `bōkjōz`, and `bōkjōn`.

## Reconstruction and early-stage forms
The row’s current derivational input is `*bōkō`, which the current OE transducer takes to `bōc` through NWGmc final long-`ō` raising and OE high-vowel apocope. The TSV note, however, preserves a broader etymological headword `*bōk(j)ō-`. That distinction matters:
- `*bōk(j)ō-` is etymological/headword material for the lexeme family;
- `*bōkō` is the current row’s modelling input for the nominative-singular target;
- `bōc` is the row’s OE output;
- `bēċe` belongs to different paradigm material and should not be treated as identical to the row target.

Live probing confirms the present grammar can separate these materials: `bōkō -> bōc`, while `bōkjō -> bēċ` and `bōkjōz` / `bōkjōn -> bēċe`. That is useful project evidence, but it is still modelling evidence, not direct textual attestation.

## Old English philology
For this row the safest philological claim is that the project now intends OE nominative singular `bōc`. The note itself says so, and the current trace reports agree. `old_english_wiktionary.tsv` instead lists `beech -> bēċe`, which is useful evidence that a different dictionary/headword or oblique form circulates in lexicographic material, but it does not by itself overturn the row’s current nominative target.

Two cautions should remain explicit:
- `bōc` for ‘beech’ must not be confused with row 1955 `bōc` ‘book’.
- The repo does not currently contain a dedicated beech dossier that securely maps every paradigm cell, so any stronger statement about exactly which oblique slot `bēċe` fills should be phrased cautiously.

## Project problem and solution
Historically the project treated row 1942 as a palatalization problem because older diagnostics expected `bēċe` directly from `*bōkō`. Current row data resolves that mismatch editorially as well as phonologically: the row is now aligned to nominative `bōc`, so the old `palatalization_missing` material is best read as evidence that an earlier target choice was stale or mixed with paradigm/headword material.

The project solution for this row is therefore to keep the lexical report narrowly tied to nominative `bōc`, while mentioning `*bōk(j)ō-` and `bēċe` only as background showing why earlier project history looked different.

## Paradigm probe
No probe is required for a narrowly row-specific final report. If the final report wants to discuss `bēċe`, a small probe is worth adding, but only to sort modelling inputs from row targets: nominative-style `*bōkō` versus `j`-bearing paradigm probes such as `*bōkjō`, `*bōkjōz`, and `*bōkjōn`. Any such probe should be presented as project-internal evidence, not as a substitute for attested paradigm documentation.

## Recommended final report
Recommend a concise lexeme report stating that row 1942 now targets OE nominative singular `bōc` from project input `*bōkō`, while noting briefly that Kroonen’s `*bōk(j)ō-` and the lexicographic form `bēċe` belong to related paradigm/headword material rather than to the row’s current target form.

## Data-change recommendations
- TSV `PROTO`: no change.
- TSV `PROTOFORM`: no change.
- TSV `COUNTERPART`: no change.
- TSV `DERIVATION_CLASS`: no change.
- TSV `NOTE`: no required change; it already captures the key distinction between nominative `bōc` and oblique `bēċe`.
- `oe_known_problems.tsv`: no change.
- `DEV_NOTES` / dossier text: `DEV_NOTES` should ideally mark the older `*bōkō -> bēċe` mismatch discussions as superseded for row 1942; no dossier change identified.
