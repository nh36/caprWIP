---
row_id: 2015
concept: fist
counterpart: fȳst
proto: *fúnxstiz
protoform: *fúnxstiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2015 fist / fȳst

## Current row state

- The live OE TSV row now reads `2015 | fist | fȳst | *fúnxstiz | *fúnxstiz | regular`. In other words, both `PROTO` and `PROTOFORM` are now the same corrected project input, not the earlier erroneous `*funxwstiz` discussed in older DEV_NOTES history [Germanic/data/germanic-aligned-final.tsv:330].
- The current published derivation trace is an exact match: `PROTO: *fúnxstiz`, `EXPECTED: fȳst`, `OUTPUTS: fȳst`, with the internal path `*fúnxsti > *fūnxsti > *fūxsti > *fūsti > *fȳsti > *fȳst` before surface `fȳst` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1321-1340].
- `oe_known_problems.tsv` has no fist-specific entry. That matters because the row is no longer being carried as a known exception, unresolved mismatch, or accepted wontfix; current repo state treats `fȳst` as a regular successful derivation rather than an intentionally unmodelled survivor [Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv` contains no exact row-2015 pilot/full report entry; the manifest currently stops with row 2250 and has no `fist / fȳst` line. This slice therefore has to carry the row-specific working-note burden directly rather than pointing to an existing packet/memo pair [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Development-note summary

DEV_NOTES for row 2015 is unusually concrete and unusually chronological. The row-specific material is not a vague note about “some nasal-spirant issue”; it records three distinct states that should stay separate in later prose. First, the row originally carried a bad TSV protoform, `*funxwstiz`, whose spurious `*w` blocked parsing and had to be corrected from Kroonen's `*funhsti-` to project notation `*funxstiz` [Germanic/docs/DEV_NOTES.md:7897-7955]. Second, once that typo was fixed, the pipeline still misderived the row as `fyxt`, because nasal-spirant lengthening had been placed too late, after i-umlaut, so `*u` had already become `*y` when NSL tried to lengthen it [Germanic/docs/DEV_NOTES.md:7959-8124]. Third, after NSL was moved into the NWGmc layer and preconsonantal `*x`-loss was added, the row reached the intended OE outcome `fȳst`; later cross-row cleanup narrowed the `*x`-loss rule to the handbook-backed `*xs + C` environment without breaking row 2015, and DEV_NOTES explicitly says this row is the only current corpus item that depends on that rule firing [Germanic/docs/DEV_NOTES.md:8127-8279,39294-39370].

Philologically, the row is not being handled as an analogical rescue or as a shaky reconstructed OE target. DEV_NOTES preserves direct handbook support for the core derivation: Kroonen's reconstruction `*funhsti-` for 'fist'; Ringe-Taylor's statement that NSL is an early northern/NWGmc innovation; and Kaluza's explicit derivational shorthand `fȳst Faust (aus *fūsti- für *fuhsti-, *funhsti-)` [Germanic/docs/DEV_NOTES.md:7915-7919,8011-8037,8184-8188]. The live trace now matches that storyline exactly, so the row's present `regular` classification is defensible — but only under the corrected protoform and corrected chronology, not if one silently imports the superseded typo or the older `fyxt`/`fȳxt` intermediate bug states [Germanic/data/germanic-aligned-final.tsv:330; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1321-1340].

One caution should be preserved: DEV_NOTES usually discusses the input as unaccented `*funxstiz`, while the live TSV uses stressed project notation `*fúnxstiz`. That is a notation difference, not a different reconstruction. Later report prose should not manufacture a false PROTO-vs-PROTOFORM distinction here; the real historical distinctions are instead between the erroneous old TSV form `*funxwstiz`, the corrected PGmc/NWGmc input `*fúnxstiz`, the intermediate NWGmc `*fūsti-`, and the attested OE outcome `fȳst` [Germanic/docs/DEV_NOTES.md:7904-7919,8087-8093; Germanic/data/germanic-aligned-final.tsv:330].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7897-7955

- Source heading: `TSV Error: *funxwstiz → should be *funxstiz (cognate 501, fȳst)`
- Source line or section hint: `lines 7897-7955`
- Fragment type: `lexeme_specific`
- Status: `current_for_row_metadata; superseded_as_bug_state`
- Issue tags: `protoform_correction`; `tsv_history`; `scrape_error`; `kroonen_alignment`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the first indispensable row-specific fragment because it preserves the exact metadata repair that the live row still depends on. DEV_NOTES states flatly that row 2015 had `PROTOFORM: *funxwstiz` with `COUNTERPART: fȳst`, and that the grammar could not derive anything because `*nxwst` was not a licensed cluster [Germanic/docs/DEV_NOTES.md:7904-7912]. It then preserves the crucial corrective quotation from Kroonen: `*funhsti- f. 'fist' < IE *pn̥ksti- < *penkʷ- 'five'`, followed by the project-level conclusion, "This translates to our notation as `*funxstiz` ... There is NO labiovelar `*w` in Kroonen's reconstruction" [Germanic/docs/DEV_NOTES.md:7915-7919]. That substantive point remains current because the live TSV row now indeed carries `*fúnxstiz` in both proto fields [Germanic/data/germanic-aligned-final.tsv:330].

The rest of the fragment is diagnostic project history, but it is not disposable. DEV_NOTES says the old `*funxwstiz` seems to have come from early automated Wiktionary scraping and may reflect conflation of the true `*nx` cluster with an imagined reflex of PIE labiovelar `*kʷ` [Germanic/docs/DEV_NOTES.md:7921-7945]. Later notes should preserve that as the explanation for why older snapshots can show `+?` or impossible cluster behaviour for this row. The stable takeaway is narrow and important: if a future writer sees `*funxwstiz` in archival material, that is a row-specific data error, not a rival reconstruction.

### DEV_NOTES:line-7959-8124

- Source heading: `NSL Chronology Bug: *funxstiz → fyxt instead of fȳst`
- Source line or section hint: `lines 7959-8124`
- Fragment type: `lexeme_specific`
- Status: `current_substance_with_fixed_bug`
- Issue tags: `nsl`; `chronology`; `i_umlaut`; `long_vowel`; `row_resolution`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is still the core explanation of why OE `fȳst` is regular in the current system. DEV_NOTES records the old mismatch exactly as `*funxstiz → fyxt (actual)` versus `*funxstiz → fȳst (expected)`, then diagnoses the immediate failure: i-umlaut had already changed `*u` to `*y`, but the NSL rule only lengthened raw back vowels, so neither nasal loss nor compensatory lengthening applied when they were needed [Germanic/docs/DEV_NOTES.md:7966-8008]. The note then shifts to the deeper historical point, quoting Ringe-Taylor that "The most obvious phonological innovation of the northern dialects is the loss of nasals immediately preceding fricatives, with lengthening and nasalization of the preceding vowel" and concluding that NSL is a NWGmc innovation that must precede OE i-umlaut [Germanic/docs/DEV_NOTES.md:8011-8029].

The fragment also preserves the most useful compact handbook-style derivation. DEV_NOTES cites Ringe-Taylor's PWGmc `*fūsti` and summarizes the correct order as `*funxstiz` → NWGmc `*fūxstiz`/`*fūstiz` → OE `*fȳst`, while Kaluza is quoted with the even more direct outcome statement `fȳst Faust (aus *fūsti- für *fuhsti-, *funhsti-)` [Germanic/docs/DEV_NOTES.md:8030-8046,8085-8094,8117-8123]. That explanatory substance is live, not just historical, because the current FST comments still say the rule must precede i-umlaut so that `*funxstiz → *fūstiz (NSL) → *fȳst`, and the published trace now shows exactly that order [Germanic/fsts/germanic.txt:2708-2714,3126-3132; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1330-1340].

### DEV_NOTES:line-8127-8279

- Source heading: `Preconsonantal *x Loss: *xs > *s before Consonant Clusters`
- Source line or section hint: `lines 8127-8279`
- Fragment type: `lexeme_specific`
- Status: `mixed_current_and_superseded`
- Issue tags: `x_loss`; `cluster_conditioning`; `campbell`; `kaluza`; `implementation_history`
- Recommended next use: `cite_with_status_warning`
- Shared with row IDs: `2092`

This fragment preserves the phonological substance that lets the row finish as `fȳst` instead of lingering at `fȳxt`. DEV_NOTES states the problem after the NSL fix as `*funxstiz → fȳxt`, then quotes Campbell §417: `"When a consonant follows, xs > s in OE, e.g. *wastm* ... North. sesta ..."`, adds Ringe-Taylor's more cautious "possibly variably ... followed by two or more consonants", and cites Kaluza's direct derivation `fȳst Faust (aus *fūsti- für *fuhsti-, *funhsti-)` [Germanic/docs/DEV_NOTES.md:8132-8188]. The worked derivation at the end remains highly usable: `*funxstiz` → `*fū̃xstiz` → `*fūxstiz` → `*fūstiz` → `*fȳst` → `fȳst` [Germanic/docs/DEV_NOTES.md:8226-8235,8264-8270].

What is no longer current is the first implementation formula attached to that reasoning. DEV_NOTES originally records `NWGmcPreconsonantalXLoss` as the broad `_ EnglishPhoneme EnglishPhoneme` rule and marks row 2015 fixed under that wider schema [Germanic/docs/DEV_NOTES.md:8246-8262]. Later DEV_NOTES history narrowed that implementation to `_ {*s} EnglishStarConsonant` after the broad rule overgenerated for row 2092 `hliehhan` [Germanic/docs/DEV_NOTES.md:39348-39364]. So later prose should keep the handbook quotations and the `*fūsti- > fȳst` derivation from this fragment, but treat the broad `_CC` rule as superseded implementation history rather than current policy.

### DEV_NOTES:line-39294-39370

- Source heading: `Corpus rows that depend on the current loss rule` / `Iteration 2 — fix implemented`
- Source line or section hint: `lines 39294-39370`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `cross_row_diagnostic`; `x_loss_restriction`; `verification`; `row_2015_control`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2092`

This later shared fragment is the cleanest statement of present repo policy for row 2015. DEV_NOTES audits the entire OE corpus and says row 2015 `*fúnxstiz → fȳst` is "the canonical and only currently-active consumer" of `NWGmcPreconsonantalXLoss`, specifically in the `*nxst` > `*xst` > `*st` pathway after NSL [Germanic/docs/DEV_NOTES.md:39294-39300]. That matters because it explains why the row remains diagnostically important even though it is now regular: a future change to x-loss can still break this row even when no overt mismatch note survives.

The same fragment then records the current narrowed implementation: option `(a) in its tightest form`, with rule `*x -> 0 || _ {*s} EnglishStarConsonant`, and verifies both `*xláxjaną → hliehhan` and `*fúnxstiz → fȳst` under the narrowed rule [Germanic/docs/DEV_NOTES.md:39348-39370]. This is the fragment that turns the earlier March x-loss note from merely successful debugging into stable cross-row policy. It is also why the live FST comments now describe the rule specifically as `*x` loss in `*xs + C` and cite `*funxstiz → fūstiz → fȳst` as the canonical example [Germanic/fsts/germanic.txt:2736-2749].

## Superseded or diagnostic material

The main superseded material for this row falls into three layers, and later notes should keep them visibly separate rather than flattening them into one generic “old bug” story.

- The oldest layer is the TSV typo `*funxwstiz`, which produced no output at all because the row was malformed at input level [Germanic/docs/DEV_NOTES.md:7904-7912].
- The middle layer is the post-typo but pre-chronology-fix form `fyxt`, where i-umlaut had applied too early and NSL therefore failed to lengthen or delete as required [Germanic/docs/DEV_NOTES.md:7966-8029].
- The third layer is the interim `fȳxt` stage after NSL was moved earlier but before `*x`-loss was handled correctly [Germanic/docs/DEV_NOTES.md:8113-8115,8134-8144].

One further caution is easy to miss: the March 2026 x-loss note records a broad `_CC` implementation that did fix row 2015, but that exact implementation is not the live one anymore [Germanic/docs/DEV_NOTES.md:8246-8262]. The current rule is the narrower `_ {*s} C` version preserved in the later 2092/2015 shared audit [Germanic/docs/DEV_NOTES.md:39348-39364; Germanic/fsts/germanic.txt:2736-2749]. So if later prose quotes the older note, it should quote it for historical derivation logic and handbook support, not as the final statement of rule shape.

No exact row-specific packet or research memo currently stands behind this row in the manifest layer, so there is no later memo-level document silently superseding the DEV_NOTES trail. For row 2015, DEV_NOTES itself remains the main internal authority, with the live published trace serving as the best confirmation of present computational state [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1321-1340].

## Open questions for later work

- If a full packet/memo is generated later, keep the chronology explicit: corrected row input `*fúnxstiz`, NWGmc `*fūsti-`, and attested OE `fȳst` are the real stages; `*funxwstiz`, `fyxt`, and the broad `_CC` x-loss rule are superseded history.
- Decide whether future prose should explicitly mention that DEV_NOTES usually writes the form as unaccented `*funxstiz` while the live TSV uses stressed `*fúnxstiz`; it is probably worth one sentence so readers do not mistake notation variation for reconstruction variation [Germanic/docs/DEV_NOTES.md:7918-7919; Germanic/data/germanic-aligned-final.tsv:330].
- If row metadata is ever normalized further, consider whether `PROTO` and `PROTOFORM` should continue to be identical here or whether one field should carry a lexeme-style handbook headword corresponding to Kroonen's `*funhsti-`. Current repo state does not require that distinction, but the slice should not pretend the question was already settled.
- If later cross-row x-loss work is reopened, treat row 2015 as the control case. DEV_NOTES explicitly says it is the only current OE row that still depends on `NWGmcPreconsonantalXLoss` firing, so any further rule change should be checked against `*fúnxstiz → fȳst` first [Germanic/docs/DEV_NOTES.md:39294-39300,39367-39370].
