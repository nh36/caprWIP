# Research memo — 2179 sheep / sċēap

## Starting point

- **ID:** 2179
- **CONCEPT:** sheep
- **COUNTERPART:** sċēap
- **PROTO:** *skḗpą
- **PROTOFORM:** *skḗpą
- **DERIVATION_CLASS:** regular
- **NOTE:** `R/T vol.2 12522: PWGmc *skap > OE scéap (WS)`

This is a note-bearing `regular` row. The live derivation already outputs `sċēap`, so the memo question is chiefly whether the row is targeting the right Old English headword and whether the note states the dialectal issue clearly enough.

## Packet evidence assessment

**Authoritative/current:**
- The aligned TSV row is current project data: the row targets `sċēap` and classifies it as `regular`.
- The compact derivation trace is also current for modelling status: `PROTO *skḗpą`, expected `sċēap`, and actual output `sċēap` all match.

**Useful background:**
- The packet’s two `ws_vs_anglian_dialect_differences.md` excerpts are useful philological background. They support a West Saxon `scéap` versus Mercian/Kentish `scép` contrast, even though the packet downgrades them because they are concept-name hits rather than direct row-ID evidence.

**Stale or superseded:**
- No packet item looks genuinely superseded. The packet’s “possibly stale or diagnostic” label on the dialect table should be read as a confidence classification, not as evidence that the table is obsolete.

**Irrelevant or misleading:**
- The `old_english_wiktionary.tsv` hit (`sheep | persona | text | Old English link | sheep`) is not lexical evidence for this row and should be ignored.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md` (the fuller surrounding discussion, not just the packet excerpt)
- `docs/references/ringe_taylor_linguistic_history_vol2.txt` at lines 12522–12523 and nearby
- `docs/references/campbell_old_english_grammar.txt` at the palatal-diphthongization and later-spelling passages
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt`
- `Germanic/docs/lexeme_reports/coverage_audit.md`
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.md`

No full dossier file and no existing pilot/full lexeme report for this lexeme were found. The debug snapshot only preserves the current placeholder project note, so it is background on present output shape, not an authority on philology.

## Reconstruction and early-stage forms

The row’s **cognate-set proto** and **project input form** are both `*skḗpą`. That is the comparative form used across the aligned Germanic set, and the live OE trace derives the target from that input via intermediate stages including NWGmc lowering (`*skǣpą`) before the Old English developments.

The TSV note, by contrast, cites an **intermediate West Germanic stage** from Ringe & Taylor: `PWGmc *skap > *skep > *scep > WS OE scéap` [@RingeTaylor2014]. That does not force a change to TSV `PROTO` or `PROTOFORM`; it just means the note is citing a later stage in the chain than the row’s comparative proto. The memo should therefore keep three levels distinct: comparative `*skḗpą`, project input `*skḗpą`, and the Old English target `sċēap`.

## Old English philology

The row’s target is best understood as a **normalized West Saxon citation form** `sċēap` (= source spelling `scéap/scēap`). Ringe & Taylor explicitly give `WS OE scéap` and contrast `Merc., Kent. scép` [@RingeTaylor2014]. The analysis memo in `ws_vs_anglian_dialect_differences.md` is therefore current background, not a contradiction of the row.

Additional repo-local reference work sharpens the dialect picture:

- Campbell lists `sééap` among West Saxon palatal-diphthongization outcomes and also notes Northumbrian `scip`, apparently from `*sciep`, alongside undiphthongized `gér`, `géfon` forms in the same textual zone [@Campbell1959].
- Campbell also cites later spellings such as `séép/scép`, showing that contracted spellings can arise secondarily and should not automatically be treated as the headword target [@Campbell1959].
- Clark Hall’s dictionary headword is `scēap`, with spelling variation `(æ, ē, i)`, and it cross-references `scēp (VPs)=scēap` [@ClarkHall1960]. That supports `scēap` as the default headword while recognizing non-WS or reduced spellings as variants.

So the main philological point is not that the row is wrong, but that `sċēap` is a **WS-normalized choice among attested OE variants**, not the only form found across all dialects and manuscripts.

## Project problem and solution

This is not a modelling-failure row. The project problem is that a `regular` derivation still needs a short lexeme report because the note encodes a **dialect-selection issue**: the generator returns the WS form correctly, but the evidence base also contains non-WS `scép` and `scip` variants.

The solution is to keep the row as the WS target `sċēap`, keep `DERIVATION_CLASS = regular`, and make the final report explicitly state that the project is representing the West Saxon headword rather than a pan-OE abstraction.

## Paradigm probe

A paradigm probe is **not required**. The issue here is citation-form and dialect selection, not uncertainty about nominal inflectional cells or an FST mismatch within the paradigm.

## Recommended final report

Recommend a brief final `### Lexeme report` that says: comparative input `*skḗpą`; Ringe & Taylor’s West Germanic pathway to WS `scéap`; the row’s target is normalized WS `sċēap`; Mercian/Kentish `scép` and Northumbrian `scip` are variant non-target forms; and the live derivation already matches the intended WS output.

## Data-change recommendations

- **TSV `PROTO`:** no change recommended.
- **TSV `PROTOFORM`:** no change recommended.
- **TSV `COUNTERPART`:** no change recommended; `sċēap` is the right normalized WS target.
- **TSV `DERIVATION_CLASS`:** no change recommended; this remains a `regular` row.
- **TSV `NOTE`:** **change recommended.** The current note is serviceable but too compressed for the real issue. It should explicitly mark the row as a WS target and, ideally, mention the contrasting non-WS form, e.g. “R/T vol.2 12522–12523: WGmc *skap > WS OE scéap (project target sċēap); Merc., Kent. scép.”
- **`oe_known_problems.tsv`:** no change recommended; this is not a known-unmodelled or paradigm-failure case.
- **`DEV_NOTES` / dossier text:** no change recommended. No dedicated dossier exists for this lexeme, and the existing dialect-analysis file is already adequate background.

A packet-only cleanup point outside the requested change list is that the `old_english_wiktionary.tsv` `persona` hit is noise, not evidence.
