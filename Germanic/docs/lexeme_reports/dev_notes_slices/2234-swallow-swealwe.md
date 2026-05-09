---
row_id: 2234
concept: swallow
counterpart: swealwe
proto: *swálwōn
protoform: *swálwōn
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2234-swallow-swealwe.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2234-swallow-swealwe.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/dossiers/widuwe-u-preservation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2234 swallow / swealwe

## Current row state

- CONCEPT: `swallow`
- COUNTERPART: `swealwe`
- PROTO: `*swálwōn`
- PROTOFORM: `*swálwōn`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *swalwōn- f. 'swallow (bird)' → OE swealwe f.; swelgan is the verb 'to swallow'` [Germanic/data/germanic-aligned-final.tsv:1180-1180].
- Live TSV history: `TSV fix: proto *swalgwōn → *swalwōn (Kroonen *swalwōn-, R/T *swalwa; no *g in this etymology, confused with *swelganą to swallow).` [Germanic/data/germanic-aligned-final.tsv:1180-1180].
- The live row keeps `PROTO` and `PROTOFORM` identical, so the project is not currently using a substitute stage-form or paradigm-cell surrogate here: the comparative headword family is represented in the row as `*swálwōn`, and the OE target to be explained is the citation-form noun `swealwe` [Germanic/data/germanic-aligned-final.tsv:1180-1180; @Kroonen2013, p. 495; @RingeTaylor2014, p. 185].
- Existing packet/memo infrastructure already uses the canonical row stem `2234-swallow-swealwe`, so the slice should reuse that stem rather than inventing a new filename [Germanic/docs/lexeme_reports/research_memo_index.tsv:106-106].

## Detailed development-note summary

The surviving DEV_NOTES support for row 2234 is narrow but genuinely usable. Its controlling row-specific statement is the March 2026 correction line: `"Swallow (*swalgwōn → *swalwōn): Kroonen (p.495, *swalwōn-) and R/T (p.185, PWGmc *swalwa) both reconstruct without *g. The TSV proto was confused with the verb *swelganą 'to swallow (food)' — the bird name has no etymological *g."` [DEV_NOTES:line-3096-3096]. That is the core point to preserve, because the row's real project problem was bad proto selection, not uncertainty about the OE noun.

For this row, `PROTO`, `PROTOFORM`, and `COUNTERPART` need to stay visibly distinct. The comparative etymological headword is Kroonen's Proto-Germanic `*swalwōn-` 'swallow' [@Kroonen2013, p. 495]. Ringe–Taylor give the West Germanic stage directly relevant to the OE vocalism and breaking environment: `PWGmc *swalwa ‘swallow’ (the bird; OHG swalewa) > *swelwe > WS OE swealwe, Merc. swalwe` [@RingeTaylor2014, p. 185]. The live row's `PROTOFORM` is the project input `*swálwōn`; the live row's `COUNTERPART` is the OE citation form `swealwe`, also supported by Clark Hall's `swealwe (a, o) f. 'swallow.'` [Germanic/data/germanic-aligned-final.tsv:1180-1180; @ClarkHall1960, s.v. "swealwe"]. Nothing in the surviving DEV_NOTES material suggests a `PROTO`/`PROTOFORM` split or any need to retarget the OE form.

The shared `*gw` discussion in DEV_NOTES matters here, but mainly as contrastive background. DEV_NOTES explains that Ringe–Taylor's discussion of loss of `*w` after non-initial velars yields different surface patterns depending on the phonetic value of `*g`, and for the liquid environment it summarizes the outcome as `After liquid (*lgw): same as post-vocalic → *lw (swealwe)` [DEV_NOTES:line-3104-3110; @RingeTaylor2014, §6.4.2]. For row 2234, however, that should not be misread as permission to keep an inherited `*lgw` in the row. The same DEV_NOTES cluster explicitly says that `snow` and `swallow` were fixed by correcting the TSV proto-forms to remove a spurious `*g`, whereas only `sing` needed a true OE-side `w`-loss rule [DEV_NOTES:line-3104-3111]. The row is regular because the comparative sources already lack that `*g`.

The implementation lines matter because they show that the correction was actually applied, not merely proposed. DEV_NOTES records `TSV changes: snow, swallow protos corrected` and `New weak tail: w:{*w} ō:{*ō} n:{*n} added for *swalwōn` [DEV_NOTES:line-3117-3118]. A later verification table then keeps `*swalwōn | swealwe | swealwe | swealwe | unchanged (*l blocks)` [DEV_NOTES:line-3850-3850]. So the note history for this row is short but coherent: old bad proto `*swalgwōn`, correction to `*swalwōn`, then stable exact-match behavior.

Later OE variant or oblique material does not overturn that conclusion. Campbell's discussion of parasitic-vowel and later lowering behavior cites `swaluwe swallow` and `swalewan` among forms showing unstressed `u/o/e` variation [@Campbell1959, §365]. That background is worth preserving for later report writers, and the widuwe dossier infrastructure already points to the same family of forms, but those are not the same thing as the row's nominative singular target `swealwe`. For the slice, the safe present decision is: keep the citation-form noun `swealwe` as current, keep `swelgan` strictly separate as the unrelated verb, and treat `swaluwe` / `swalewan` as later variant or inflectional background only [DEV_NOTES:line-3096-3096; @Campbell1959, §365].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3088-3088

- Source heading: `The problem`
- Source line or section hint: `line 3088`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_mismatch_snapshot`; `bad_proto_entry`; `spurious_g`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This line preserves the superseded mismatch state that later writers would otherwise have to reconstruct from git history: `*swalgwōn → swealgwe (expected swealwe): cons_mismatch__g_vs_w` [Germanic/docs/DEV_NOTES.md:3088-3088]. It should be kept only as diagnostic chronology. The row's present OE target was not wrong; the stored proto entry was.

### DEV_NOTES:line-3096-3096

- Source heading: `Research`
- Source line or section hint: `line 3096`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_correction`; `bird_vs_verb_disambiguation`; `comparative_support`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling lexeme-specific DEV_NOTES fragment and should be preserved almost verbatim: `"Swallow (*swalgwōn → *swalwōn): Kroonen (p.495, *swalwōn-) and R/T (p.185, PWGmc *swalwa) both reconstruct without *g. The TSV proto was confused with the verb *swelganą 'to swallow (food)' — the bird name has no etymological *g."` [Germanic/docs/DEV_NOTES.md:3096-3096]. It gives the comparative support, the exact correction, and the reason the correction was necessary.

### DEV_NOTES:line-3104-3110

- Source heading: `Analysis of *gw developments`
- Source line or section hint: `lines 3104-3110`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `shared_sound_change_context`; `contrast_with_genuine_gw_cases`; `after_liquid`; `spurious_g_removed`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2199`; `2190`

This shared fragment is useful because it explains why `swallow` was grouped with other `*gw` items but ultimately resolved differently from `sing`. DEV_NOTES states that R/T §6.4.2 covers `"Loss of *w after non-initial velars"` and then distinguishes `*ngw`, `*Vgw`, and `*lgw`, with the liquid environment summarized as `After liquid (*lgw): same as post-vocalic → *lw (swealwe)` [Germanic/docs/DEV_NOTES.md:3104-3110]. For row 2234 the important takeaway is the last line of the block: cases like `snow` and `swallow` were fixed by removing the false `*g` from the proto entry, not by installing a new row-specific OE repair rule [Germanic/docs/DEV_NOTES.md:3110-3111].

### DEV_NOTES:line-3117-3118

- Source heading: `Implementation`
- Source line or section hint: `lines 3117-3118`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `tsv_fix_applied`; `weak_tail_update`; `project_chronology`; `row_local_verification`
- Recommended next use: `cite_if_row_history_needed`
- Shared with row IDs: `2199`

These lines are terse but materially useful: `TSV changes: snow, swallow protos corrected` and `New weak tail: w:{*w} ō:{*ō} n:{*n} added for *swalwōn` [Germanic/docs/DEV_NOTES.md:3117-3118]. They confirm that the row's correction was pushed through into live data and that the corrected noun also received the tail material needed by the cascade.

### DEV_NOTES:line-3850-3850

- Source heading: `verification table`
- Source line or section hint: `line 3850`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `post_fix_stability`; `exact_match`; `l_blocks`; `sentinel_history`
- Recommended next use: `cite_if_stability_matters`
- Shared with row IDs:

This later table is brief but worth retaining because it shows that row 2234 stayed stable after the correction work: `| *swalwōn | swealwe | swealwe | swealwe | unchanged (*l blocks) |` [Germanic/docs/DEV_NOTES.md:3850-3850]. It is not a new argument, but it is a useful compact verification point for later report writing.

## Superseded or diagnostic material

- The only genuinely superseded lexical policy is the bad proto `*swalgwōn` and the false expected output `swealgwe`. That form should remain visible only as project history, because DEV_NOTES and the live TSV now agree that the bird-name etymology has no inherited `*g` [Germanic/docs/DEV_NOTES.md:3088-3096; Germanic/data/germanic-aligned-final.tsv:1180-1180].
- The verb `swelgan` is diagnostic-only background for this row. It explains how the contamination happened, but it is not a rival `COUNTERPART`, not a rival `PROTOFORM`, and not a reason to treat row 2234 as a verbal item [Germanic/docs/DEV_NOTES.md:3096-3096].
- Campbell's `swaluwe` / `swalewan` material and the widuwe dossier are useful philological background for later inflectional or variant discussion, but they are not evidence against the row's citation-form target `swealwe` [@Campbell1959, §365]. If a later full report uses them, it should label them explicitly as later variant or oblique material.

## Open questions for later work

- If `index.tsv` is updated later, the strongest standalone fragment to index is `DEV_NOTES:line-3096-3096`; the surrounding `3104-3110`, `3117-3118`, and `3850-3850` material is useful but increasingly shared or verification-oriented.
- Decide whether a later full lexeme report needs a short variant paragraph citing Campbell §365 and the widuwe dossier, while keeping those forms explicitly separate from the nominative citation form `swealwe` [@Campbell1959, §365].
- No current evidence suggests changing `PROTO`, `PROTOFORM`, `COUNTERPART`, or `DERIVATION_CLASS`. Later work here is more likely to be indexing/source-hierarchy cleanup than lexical reanalysis.
