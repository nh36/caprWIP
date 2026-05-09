---
row_id: 2105
concept: line
counterpart: līne
proto: *lī́nōn
protoform: *lḯnōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current_shared_background_only
needs_literature_agent: no
---

# DEV_NOTES material — 2105 line / līne

## Current row state

- Live OE row `2105` currently has `CONCEPT = line`, `COUNTERPART = līne`, `PROTOFORM = *lḯnōn`, `DERIVATION_CLASS = regular`, and comparative `PROTO = *lī́nōn`; the row therefore already distinguishes the FST input form from the comparative-display proto label [Germanic/data/germanic-aligned-final.tsv:678-678].
- The row carries only inherited-etymology placeholders in the source/history fields, not a row-local explanatory note, so the live TSV itself does not preserve any lexeme-specific rationale beyond the migrated `PROTOFORM` and the regular classification [Germanic/data/germanic-aligned-final.tsv:678-678].
- `coverage_audit.md` still marks row `2105` as having no packet, no memo, no attached DEV_NOTES fragment, and no other report infrastructure. `report_manifest.tsv` likewise has no row `2105` entry in the currently tracked manifest rows [Germanic/docs/lexeme_reports/coverage_audit.md:295-295; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- `oe_known_problems.tsv` has no entry for `*lī́nōn` / `*lḯnōn`, so the row is not currently being managed as an exception bucket or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation is straightforward and succeeds without repair: `PROTO: *lḯnōn`, `EXPECTED: līne`, `OUTPUTS: līne`; the compact class trace reduces the row to `NWGmc N Stem N Loss: *lḯnǭ`, then `OE Unstressed Long Vowel Shortening: *lḯnæ`, then `OE Unstressed AE Merger: *lḯne`, with final surface `līne` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2903-2922].
- The full trace confirms that nothing row-specific or exceptional fires around the root vowel: `NWGmcInStemNLoss` is `[no-change]`, while the active steps are `NWGmcNStemNLoss`, `OEUnstressedLongVowelShortening`, `OEUnstressedAEMerger`, and final star removal [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19143-19257].

## Development-note summary

No analytical, row-specific DEV_NOTES block for `line / līne` survives in the live `DEV_NOTES.md`. The only surviving row-local DEV_NOTES mention is a **migration-table line** listing row `2105` among the OE rows whose stressed-root `*ī` was migrated to the dedicated `*ḯ` notation [Germanic/docs/DEV_NOTES.md:42006-42024]. Everything else that still matters for this row is **shared-background-only** material from §17.46 on the stressed long-`ī` tier.

That shared material is still important, because it explains the otherwise easy-to-misread split between `PROTO = *lī́nōn` and `PROTOFORM = *lḯnōn`. DEV_NOTES states: “The principled fix is to encode the stress-bearing property directly on the proto-vowel,” and then: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41919-41921,41938-41940]. For row 2105, this means the live `PROTOFORM` is not a new lexical hypothesis; it is the same root vowel, rewritten so the cascade can distinguish stressed root `ī` from the unstressed suffixal `*ī` targeted elsewhere by `NWGmcInStemNLoss`.

DEV_NOTES is equally explicit that this notation does **not** create a special OE surface vowel. “OE orthography does **not** distinguish stressed-root from unstressed-suffix long ī,” and the tier “exists only to gate one rule (`NWGmcInStemNLoss`); from the moment that rule fires (or doesn't), the two collapse for orthography” [Germanic/docs/DEV_NOTES.md:41954-41957]. That fits the live trace exactly: row 2105 keeps the stressed-root notation in the protoform, but surfaces as ordinary `līne`, with no special orthographic marking and no exceptional repair [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2903-2922].

So the replacement note for this row has to stay conservative. There is **no surviving lexeme-specific DEV_NOTES argument** about etymology, target choice, or attestation for `līne`; the usable project authority is narrower. It says that row 2105 is one of the stressed-root `*ī` rows migrated to `*ḯ`, that the migration is architectural rather than lexical, and that the row's actual OE derivation remains regular once that notation is in place [Germanic/docs/DEV_NOTES.md:41919-41957,42006-42024; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19168-19257].

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:41919-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line hint: `notation and pipeline-plumbing core`
- Fragment type: `shared-background-only`
- Status: `current`
- Issue tags: `stressed_long_i_tier`; `proto_vs_protoform`; `orthography`; `not_row_specific`
- Recommended next use: `cite when explaining why row 2105 uses *lḯnōn in PROTOFORM but still surfaces as līne`
- Shared-with rows if relevant: `1998, 2047, 2101, 2103, 2106, 2153, 2182, 2188, 2197, 2257, 2285, 2286, 2290, 2296; seed migration row 1194`

This is the main surviving DEV_NOTES authority for row 2105, but it is shared background rather than lexeme-specific discussion. The note says the “principled fix is to encode the stress-bearing property directly on the proto-vowel,” then explains the notation choice: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41919-41921,41938-41940]. For `line / līne`, that is the direct explanation of why the live row keeps comparative `PROTO = *lī́nōn` while using migrated FST `PROTOFORM = *lḯnōn` [Germanic/data/germanic-aligned-final.tsv:678-678].

The same fragment also gives the crucial orthographic caution that must be preserved in this slice: “OE orthography does **not** distinguish stressed-root from unstressed-suffix long ī,” and the tier exists only to gate `NWGmcInStemNLoss`, after which the two collapse again for spelling [Germanic/docs/DEV_NOTES.md:41954-41957]. That means row 2105 should not be read as claiming a special attested OE form `*lḯne`; the live target remains ordinary `līne`, and the `ḯ` belongs only to the internal protoform notation [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2903-2922].

### Germanic/docs/DEV_NOTES.md:41959-41982

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — rule audit`
- Source line hint: `rules updated vs. rules deliberately left *ī-only`
- Fragment type: `shared-background-only`
- Status: `current`
- Issue tags: `rule_audit`; `nwgmcinstemnloss_scope`; `safety_for_stressed_root_i`; `not_row_specific`
- Recommended next use: `cite when explaining why stressed-root rows like 2105 were migrated off plain *ī`
- Shared-with rows if relevant: `same stressed-root-*ī migration set as above`

This fragment matters because it states exactly how the new tier interacts with the rules. DEV_NOTES records that some rules were propagated to both `*ī` and `*ḯ`, but `NWGmcInStemNLoss` was “deliberately left as `*ī`-only,” “by design — *only* fires on unstressed suffix” [Germanic/docs/DEV_NOTES.md:41969-41982]. For row 2105 that is negative but essential evidence: the root vowel in `*lḯnōn` is not the suffixal `*ī` that this rule is meant to consume, so leaving the row as plain `*ī` would collapse a real structural distinction that DEV_NOTES now treats as mandatory.

The live full trace confirms the relevance of that distinction. On row 2105, `NWGmcInStemNLoss` is `[no-change]`; the row proceeds instead through `NWGmcNStemNLoss`, unstressed-vowel shortening, and unstressed `æ > e` merger to `līne` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19179-19257]. So this fragment is shared-background-only, but it is still the best surviving explanation of why the row's `PROTOFORM` was migrated while the row's ordinary regular derivation stayed otherwise unchanged.

### Germanic/docs/DEV_NOTES.md:42006-42024

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — TSV migration (Phase 4)`
- Source line hint: `inventory plus migrated-row table`
- Fragment type: `row-specific_batch_membership`
- Status: `current`
- Issue tags: `row_2105_explicit_mention`; `batch_2`; `protoform_migration`; `minimal_row_specific_support`
- Recommended next use: `cite when documenting the exact DEV_NOTES basis for row 2105's migrated protoform`
- Shared-with rows if relevant: `2103, 2106`

This is the only surviving DEV_NOTES fragment that names row 2105 directly. DEV_NOTES says that among OE rows with `*ī` in `PROTOFORM`, “**15** are stressed-root *ī (in the first syllable, no preceding vowel) — migrated to `*ḯ`,” while only the unstressed feminine in-stem suffix in `*fúrxtīn → fyrhte` was kept as plain `*ī` [Germanic/docs/DEV_NOTES.md:42010-42015]. The migration table then explicitly lists batch 2 as `2103, 2105, 2106 | līm, līne, līste` [Germanic/docs/DEV_NOTES.md:42017-42024].

The value of this fragment is narrow but real. It is **row-specific** only in the logistical sense that it records the row's inclusion in the migration batch; it does **not** preserve a separate lexical analysis of `line / līne`. Still, for this slice that narrow support is exactly what needs preserving: row 2105's current `PROTOFORM = *lḯnōn` is not arbitrary and not a one-off invention in the TSV; it is the documented outcome of the branch-wide stressed-root-`*ī` migration policy [Germanic/data/germanic-aligned-final.tsv:678-678; Germanic/docs/DEV_NOTES.md:42010-42024].

## Superseded or diagnostic material

- The immediately preceding regression note in §17.45.3g is still useful, but only as **diagnostic background**. There DEV_NOTES records the overbroad old rule `define NWGmcInStemNLoss [{*n} -> 0 || {*ī} _ .#.];`, warns that this matched both the intended unstressed suffix and unintended stressed-root environments, and quotes Brunner: “Der alte Ausgang -ī(n) zeigt sich in dem ständigen i-Umlaut der Wurzelsilbe” [Germanic/docs/DEV_NOTES.md:41783-41806]. For row 2105 this material is not row-specific evidence about `līne`; it is the superseded diagnostic that explains why stressed-root rows had to be migrated off plain `*ī` in the first place.
- That same diagnostic section is also where DEV_NOTES frames the underlying contrast most sharply: the change belongs to the **suffix**, “NOT on a stressed root vowel” [Germanic/docs/DEV_NOTES.md:41805-41806]. Row 2105 should therefore be read as a beneficiary of the later §17.46 cleanup, not as an in-stem-n-loss case of its own. The full live trace confirms that by showing `NWGmcInStemNLoss [no-change]` on this row [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:19222-19223].
- `coverage_audit.md`, `report_manifest.tsv`, and `oe_known_problems.tsv` are diagnostic-only for this row. They confirm the absence of prior packet/memo/manifest/problem infrastructure, but they do not preserve additional philological reasoning about `line / līne` beyond the fact that the row is currently regular and unflagged [Germanic/docs/lexeme_reports/coverage_audit.md:295-295; Germanic/docs/lexeme_reports/report_manifest.tsv:1-14; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If a packet or memo is ever created for row 2105, decide whether the row merits any lexeme-specific dossier at all, or whether it should remain documented only through shared stressed-root-`*ī` background plus the live trace.
- Keep the `PROTO` / `PROTOFORM` distinction explicit in later reporting. For this row, `*lī́nōn` and `*lḯnōn` are not competing lexical reconstructions; the latter is the branch's internal stressed-root notation for the same inherited long `ī` [Germanic/data/germanic-aligned-final.tsv:678-678; Germanic/docs/DEV_NOTES.md:41938-41940].
- Recheck row 2105 if a future build starts routing migrated `*ḯ` forms through one of the gate-input clauses that DEV_NOTES notes still lack full `ḯ:{*ḯ}` parallel arms. DEV_NOTES says “Today no migrated TSV form needs them,” but preserves that as a future audit point rather than a permanently closed question [Germanic/docs/DEV_NOTES.md:42060-42064].
