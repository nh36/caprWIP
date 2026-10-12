---
row_id: 2017
concept: flax
counterpart: fleax
proto: *fláxsą
protoform: *fláxsą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md, Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md]
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2017 flax / fleax

## Current row state

- CONCEPT: `flax`
- COUNTERPART: `fleax`
- PROTO: `*fláxsą`
- PROTOFORM: `*fláxsą`
- DERIVATION_CLASS: `regular`
- The live TSV row is sparse but internally stable: row 2017 keeps `COUNTERPART = fleax`, `PROTO = PROTOFORM = *fláxsą`, and `DERIVATION_CLASS = regular`, with only duplicated inherited-source placeholders in the note/source field rather than a row-local explanation [Germanic/data/germanic-aligned-final.tsv:337-337].
- `coverage_audit.md` currently classifies row 2017 as a regular row with `NOTE? no`, no linked report path, and requirement basis `none`, so there is no pre-existing packet, memo, or pilot report to inherit from for this exact row [Germanic/docs/lexeme_reports/coverage_audit.md:240-240].
- The current derivation snapshot already reaches the target exactly and without repair branching: `Proto Input: *fláxsą`, then `Anglo Frisian Brightening: *flæxsą`, `OE Breaking: *fleaxsą`, `OE Heavy Syllable Nasal Apocope: *fleaxs`, `OE Xs Merge: *fleaXS`, and final `Outcome: fleax` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:1494-1504].

## Development-note summary

No extended row-specific DEV_NOTES dossier survives for `flax / fleax`. The only direct row mention in `DEV_NOTES.md` is brief but still important: row 2017 is listed under corpus items with medial `*xC`, specifically the `*xs` subgroup labelled “mostly preserved as `x` orthographically, no loss,” followed by the policy sentence “These do not require the loss rule. Per Campbell §416, *xs survives as `x` (= ks) when no further consonant follows” [Germanic/docs/DEV_NOTES.md:39260-39275]. For this row, that is the core current DEV_NOTES claim: `*fláxsą > fleax` is being treated as a regular `*xs` survivor, not as a consonant-loss exception and not as a row needing special repair.

The current trace matches that narrow claim cleanly. Nothing in the published derivation suggests a bespoke lexeme-level workaround: the vowel developments are ordinary for this environment, heavy-syllable nasal apocope removes the final nasalized vowel, and the surviving `*xs` cluster is then represented by OE `x`, giving `fleax` exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:1494-1504]. The row's present `regular` status is therefore well supported at the implementation level even though the prose discussion in DEV_NOTES is short [Germanic/data/germanic-aligned-final.tsv:337-337; Germanic/docs/DEV_NOTES.md:39260-39275].

The main older diagnostic material points in the opposite direction and should be kept only as superseded history. `final_vowel_apocope_investigation.md` once listed `*flaxsą → fleahsa (exp. fleax)` among the false outputs produced before the heavy-syllable apocope cleanup was settled [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:273-292]. That file is useful because it preserves the row's earlier failure mode, but it is not current authority; the later trace and DEV_NOTES inventory both show the row now resolving normally to `fleax` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:273-292; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:1494-1504; Germanic/docs/DEV_NOTES.md:39260-39275].

One further DEV_NOTES passage mentions the gloss `flax`, but not this row. In the discussion of over-broad `*īn`-loss, DEV_NOTES cites OE `līn` “flax” as a stressed monosyllable that preserves final `-n` [Germanic/docs/DEV_NOTES.md:41793-41824]. That material is philologically useful only as a gloss-collision warning: it concerns a different OE flax lexeme, not row 2017's `COUNTERPART = fleax` [Germanic/data/germanic-aligned-final.tsv:337-337; Germanic/docs/DEV_NOTES.md:41793-41824].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39260-39275

- Source heading: `#### 6. Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39260-39275`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `xs_preservation`; `no_loss_rule`; `regular_row`; `shared_rule_inventory`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2031, 2146, 2194, 2275, 2276`

This is the one clearly row-specific DEV_NOTES anchor that survives. DEV_NOTES names the row directly — `2017 *fláxsą → fleax` — inside the `*xs` subgroup and then gives the operative rule statement: “These do not require the loss rule. Per Campbell §416, *xs survives as `x` (= ks) when no further consonant follows” [Germanic/docs/DEV_NOTES.md:39265-39275]. For row 2017, that sentence does almost all the real explanatory work that DEV_NOTES now preserves.

The fragment is short, so it should not be overstated. It does not preserve a full lexeme dossier, an etymological debate, or a row-local literature review on `fleax`; instead it records the narrower implementation judgment that this row belongs with regular `*xs` survivors rather than with cases where preconsonantal `x` is lost [Germanic/docs/DEV_NOTES.md:39260-39275]. The present derivation trace agrees with that judgment exactly, because it reaches `fleax` without any `*xs > s` repair step [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:1494-1504].

### DEV_NOTES:line-41781-41824

- Source heading: `### B. Diagnosis: rule context too broad`
- Source line or section hint: `lines 41781-41824`
- Fragment type: `diagnostic_only`
- Status: `non_row_specific`
- Issue tags: `gloss_collision`; `different_oe_lexeme`; `stressed_in_preservation`; `do_not_conflate`
- Recommended next use: `use_only_as_lexeme_boundary_warning`
- Shared with row IDs: `2238 and other monosyllabic *-īn material`

This fragment is relevant only because it can mislead later row work if left uncited. DEV_NOTES warns that a proposed `*n`-loss rule was over-applying to stressed monosyllables and explicitly lists `*līn 'flax'` among the preserved forms: “Stressed monosyllabic *ī*n words preserve final *-n in OE without exception: … OE `līn` (n.) 'flax' — preserved” [Germanic/docs/DEV_NOTES.md:41818-41824]. That is accurate for the `līn` lexeme, but it is not evidence about row 2017.

The value of the fragment here is boundary-setting. Row 2017 targets `fleax`, not `līn`, so the passage should be retained only to make the lexical distinction explicit: the English gloss `flax` points to more than one OE form in repo-local materials, and this slice concerns the `*fláxsą > fleax` pathway only [Germanic/data/germanic-aligned-final.tsv:337-337; Germanic/docs/DEV_NOTES.md:41793-41824].

## Superseded or diagnostic material

- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` is preserved here only as project history. Its reference-data list still shows the older false output `*flaxsą → fleahsa (exp. fleax)`, which reflects a pre-fix diagnostic stage rather than the current analysis [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:273-292].
- The duplicated inherited-source placeholders in the TSV row are intake provenance, not substantive explanation. They should not be mistaken for a row-specific philological note or a replacement for the short but real DEV_NOTES `*xs`-preservation fragment [Germanic/data/germanic-aligned-final.tsv:337-337; Germanic/docs/DEV_NOTES.md:39265-39275].
- No row-specific packet or research memo was located for row 2017, and `coverage_audit.md` still treats it as a no-report-required regular row. Any later expansion therefore needs to start from the sparse shared-rule evidence gathered here, not from an omitted hidden dossier [Germanic/docs/lexeme_reports/coverage_audit.md:240-240].

## Open questions for later work

- If a later packet is ever written for row 2017, add explicit lexical-source handling for the distinction between OE `fleax` and OE `līn`, since DEV_NOTES already proves that the gloss `flax` is not lexeme-unique inside the project [Germanic/docs/DEV_NOTES.md:41793-41824; Germanic/data/germanic-aligned-final.tsv:337-337].
- If the project revisits `*x`-loss chronology, keep row 2017 grouped with `*xs` survivors unless new evidence shows that `fleax` should be treated differently from the other rows named in the same DEV_NOTES inventory [Germanic/docs/DEV_NOTES.md:39260-39275].
- If old apocope-era diagnostics are mined again, make sure `fleahsa` is treated as superseded false output history only, not as a live alternative OE target for this row [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:273-292; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.audit.md:1494-1504].
