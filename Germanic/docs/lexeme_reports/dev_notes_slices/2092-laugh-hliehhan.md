---
row_id: 2092
concept: laugh
counterpart: hliehhan
proto: *lákaną
protoform: *xláxjaną
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2092-laugh-hliehhan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/four_complex_tsv_items.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2092 laugh / hliehhan

## Current row state

- CONCEPT: `laugh`
- COUNTERPART: `hliehhan`
- PROTO: `*lákaną`
- PROTOFORM: `*xláxjaną`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note: `§17.40: target hlæhhan → hliehhan (WS form per Bright p.597, Brunner §392,4; Anglian hlæhhan attested as variant — cascade defaults to WS). Added *x to PWGmcJGemination per Fulk §6.15. | R/T: PGmc *hlahjanan > OE hlæhhan/hliehhan` [Germanic/data/germanic-aligned-final.tsv:628].
- `oe_known_problems.tsv`: no row-local entry survives. The packet records `Matching oe_known_problems.tsv entries` as `_None_`, and the memo repeats that no row-specific problem entry is present [Germanic/docs/lexeme_reports/packets/2092-laugh-hliehhan.md:45-47; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:28-33,103].
- Packet status: the packet's compact derivation trace is already aligned with the live row, with `PROTO: *xláxjaną`, `EXPECTED: hliehhan`, `OUTPUTS: hliehhan`, and orthographic `Outcome: hliehhan`; it therefore preserves current state as well as older mismatch history [Germanic/docs/lexeme_reports/packets/2092-laugh-hliehhan.md:17-42].
- Coverage status: `coverage_audit.md` still lists row `2092` as needing report coverage because it has both a non-empty `NOTE` and `DERIVATION_CLASS=early_analogy`, so this slice has to stand on its own even though no full lexeme report exists yet [Germanic/docs/lexeme_reports/coverage_audit.md:103].
- Current row-specific DEV_NOTES authority **does exist**. The securely current pieces are the row-local source audit backing WS `hliehhan` and the later implementation/verification block showing `*xláxjaną → hliehhan` after the *x-gemination/*x-loss repair; the earlier mismatch-stage dossier remains useful only as superseded or diagnostic history [Germanic/docs/DEV_NOTES.md:38901-38931,39348-39368; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:17-22,75-84,104-105].

## Development-note summary

Current DEV_NOTES authority for row 2092 is real, but it is split chronologically and has to be read that way. The early block at `38872 ff.` documents the old failure state `*xláxjaną -> hliehan`, while the later block at `39348-39368` is the actual current row policy: the project adopted the narrow `_ {*s} C` version of `NWGmcPreconsonantalXLoss`, preserved geminate `*xx`, and verified `*xláxjaną → hliehhan` with no regression for the only other active consumer row `2015` [Germanic/docs/DEV_NOTES.md:38872-38900,39294-39324,39348-39368]. The memo therefore correctly says that the bug trail is now historical and that the present row is no longer a live mismatch [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:17-22,73-84].

The three levels must remain explicit. `PROTO = *lákaną` is the aligned cognate-set label shared with the continental `laugh/lachen` set; `PROTOFORM = *xláxjaną` is the OE-directed j-present input; and the OE target is the lemma `hliehhan`, not the aligned proto label and not a paradigm-cell workaround [Germanic/data/germanic-aligned-final.tsv:628; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:52-60,77-82]. That is why `DERIVATION_CLASS = early_analogy` is still coherent: the special move is upstream branch or stem selection into the OE j-present, not a late rescue by substituting a different OE inflectional cell [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:58-60,82,98-102].

The row is an attested OE lemma-level case, but the slice has to keep WS target choice separate from variant background. DEV_NOTES' row-local source audit quotes Brunner, `Urspr. hj erscheint so als hh in ws. hliehhan ... angl. hlæhhan; ws. hliehhan`, and Bright's `hliehhan (<*hleahjan, 9 <*hlæhjan; Goth. hlahjan), to laugh`; Bosworth-Toller likewise lists `hlehhan, hlihhan, hlæhhan, hlyhhan` as variants while treating `hliehhan` as the WS lemma [Germanic/docs/DEV_NOTES.md:38910-38928]. The memo sharpens the policy consequence: `hliehhan` is the attested West Saxon target the default OE cascade should use, while `hlæhhan`, `hlehhan`, and similar spellings are real comparator/background variants, not rival current targets [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:64-71,77-84,94-102].

The sound-change side is likewise specific. DEV_NOTES first records the old failure as missing gemination plus target-choice confusion, but the source audit and later handbook dossier insist that geminate `hh` is regular here. Fulk is quoted for WGmc gemination before `*j` applying to any consonant except `*r`; Campbell is quoted that `The gemination of x remains (written hh) in OE whether due to doubling before j, e.g. hliehhan`; and the handbook derivation table then segments the row as `*hlahjanan/*xlaxjanan` > `*hlahhjan` > `*hlæhhjan` > `*hleahhjan` > `*hliehhjan` > `*hliehhan`, with Anglian `hlæhhan` explained as a variant line that still preserves `hh` [Germanic/docs/DEV_NOTES.md:38903-38908,39051-39056,39181-39196]. So the old single-`h` output was a project bug, not a philological alternative [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:45-48,66-69].

What remains special is not the existence of `hliehhan`, but the lexical history behind the broken vowel and the row's comparative labeling. The memo notes that Ringe-Taylor treat `laugh` as the unique case where breaking occurs before the palatalized geminate and suggest analogical support from the related noun `*hleahtr`, while Brunner likewise ties non-WS `hlæhhan` to noun influence [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:69-71,94]. That is compatible with keeping current row design intact: comparative `*lákaną`, OE-facing `*xláxjaną`, target `hliehhan`, and variant `hlæhhan/hlehhan` material retained only as background or superseded workflow history [Germanic/data/germanic-aligned-final.tsv:628; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:98-105].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39348-39368

- Source heading: `Iteration 2 — fix implemented`
- Source line or section hint: `lines 39348-39368`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `x_gemination`; `preconsonantal_x_loss`; `verification`; `row_resolution`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2015`

This is the main current row-specific DEV_NOTES authority. DEV_NOTES says the project adopted option `(a) in its tightest form`, narrowing `NWGmcPreconsonantalXLoss` to `_ {*s} C`, explicitly because that conditioning matches the handbook examples while leaving geminate `*xx` untouched; it then verifies `*xláxjaną` → `hliehhan` and simultaneously preserves row `2015` `*fúnxstiz` → `fȳst` as the only corpus row that still needs the loss rule to fire [Germanic/docs/DEV_NOTES.md:39348-39370]. For row 2092 this fragment is not mere implementation noise: it is the place where the row stops being an unresolved mismatch and becomes settled current project state, exactly as the packet's compact derivation trace and the memo's “bug trail is now historical” summary also indicate [Germanic/docs/lexeme_reports/packets/2092-laugh-hliehhan.md:17-42,111-121; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:17-22,73-76].

### DEV_NOTES:line-38901-38931

- Source heading: `Source audit`
- Source line or section hint: `lines 38901-38931`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `ws_target_choice`; `variant_management`; `handbook_quote`; `lemma_attestation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment is current because it preserves the exact source hierarchy behind the row's target choice. DEV_NOTES quotes Fulk that gemination before `*j` applies to any consonant except `*r`, quotes Brunner `Urspr. hj erscheint so als hh in ws. hliehhan lachen … angl. hlæhhan; ws. hliehhan`, and then adds Bright's explicit lemma citation `hliehhan (<*hleahjan, 9 <*hlæhjan; Goth. hlahjan), to laugh` plus Bosworth-Toller's variant list under the WS lemma [Germanic/docs/DEV_NOTES.md:38903-38928]. The packet preserves the same local evidence, and the memo draws the right conclusion from it: `hliehhan` is the WS form the project should target by default, while `hlæhhan` and related spellings remain attested variant background rather than the live row target [Germanic/docs/lexeme_reports/packets/2092-laugh-hliehhan.md:247-293,590-610; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:64-71,81,94-102].

### DEV_NOTES:line-39181-39196

- Source heading: `Derivation of *hliehhan* / *hlæhhan* in the handbooks`
- Source line or section hint: `lines 39181-39196`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `derivational_path`; `breaking`; `i_umlaut`; `hh_preservation`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This handbook-derivation table is background rather than row policy, but it is the clearest compact statement of the lawful path the row is supposed to follow. DEV_NOTES lays out the consensus sequence `*hlahjanan / *xlaxjanan` → WGmc gemination `*hlahhjan` → AFB `*hlæhhjan` → breaking `*hleahhjan` → i-umlaut `*hliehhjan` → j-loss/apocope `*hliehhan`, and then notes that Anglian `hlæhhan` represents a variant line that still preserves the geminate `hh` [Germanic/docs/DEV_NOTES.md:39183-39196]. The memo uses exactly this distinction to keep comparative `PROTO *lákaną`, OE derivational `PROTOFORM *xláxjaną`, and OE target `hliehhan` from collapsing into one another, while also identifying the broken vowel as the genuinely delicate part of the history [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:52-60,66-71,77-82].

## Superseded or diagnostic material

### DEV_NOTES:line-38872-38900

- Source heading: `Mismatch as observed`
- Source line or section hint: `lines 38872-38900`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `old_mismatch`; `missing_gemination`; `obsolete_target_state`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment has to be preserved, but only as superseded history. It records the old state exactly as `*xláxjaną -> hliehan (expected hlæhhan)`, then explains that the medial consonant was wrongly single rather than geminate and that the row was simultaneously entangled with a WS-versus-Anglian target-choice discussion [Germanic/docs/DEV_NOTES.md:38872-38900]. That diagnosis remains useful because it captures what actually went wrong before the fix, yet the memo is explicit that passages treating row 2092 as unresolved `hlæhhan`/`hliehan` work are now stale and must not be mistaken for current row state [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:17-22,75-84,104-105].

### DEV_NOTES:line-39260-39324

- Source heading: `Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39260-39324`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `diagnostic_only`
- Issue tags: `cross_row_diagnostic`; `x_loss_context`; `row_2015_control`; `xj_bug_case`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2015`

This fragment is diagnostic rather than current authority, but it is worth keeping because it shows why the eventual rule change was narrow instead of ad hoc. DEV_NOTES audits the OE corpus and finds exactly one row where preconsonantal `*x`-loss genuinely has to fire, row `2015` `*fúnxstiz → fȳst`, and exactly one row where the broad rule mis-fired after the new gemination clause, row `2092` `*xláxjaną → hliehhan` after intermediate `*xláxxjaną` [Germanic/docs/DEV_NOTES.md:39294-39324]. Once iteration 2 is implemented this becomes historical rather than operative, but it remains the clearest internal explanation of why row 2092 is a special diagnostic for `*xj` while not licensing a rollback of the gemination repair [Germanic/docs/DEV_NOTES.md:39348-39370].

### Packet/source-audit: supplementary OE table disagreement

- Source heading: `Local lexical-table hits`
- Source line or section hint: `packet lines 548-560`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `misleading_if_uncontextualized`
- Issue tags: `supplementary_tables`; `variant_background`; `source_ranking`; `false_rival_target`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This non-DEV_NOTES fragment should be retained because later writers are otherwise likely to rediscover the same apparent contradiction and over-weight it. The packet preserves a bare `old_english_wiktionary.tsv` hit `laugh | hlæhhan` alongside `old_english_swadesh.tsv` `to laugh | hliehhan`, and the memo explicitly classifies that disagreement as lightweight background that must not outrank the handbook and dictionary material favoring WS `hliehhan` [Germanic/docs/lexeme_reports/packets/2092-laugh-hliehhan.md:548-560; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:18-20,32-33,43-48]. It is therefore useful only as a checked source-audit note: `hlæhhan` is real variant evidence, but not current row policy.

## Open questions for later work

- If `index.tsv` is updated later, record explicitly that row 2092 has **current** row-specific DEV_NOTES authority at `39348-39368` and `38901-38931`, while `38872-38900` and the broader `39260-39324` audit are retained only as superseded or diagnostic history.
- If final report prose is written later, keep the three-way distinction explicit: comparative `PROTO *lákaną`, OE derivational `PROTOFORM *xláxjaną`, and OE target `hliehhan`; do not collapse the row into a statement that OE `hliehhan` directly continues the aligned cognate-set label [Germanic/data/germanic-aligned-final.tsv:628; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:52-60,77-82,98-102].
- If row-note cleanup is done elsewhere later, treat `hlæhhan`, `hlehhan`, `hlihhan`, and similar forms as comparator or variant background only unless a future source audit justifies a change in dialect policy; current repo authority still favors WS `hliehhan` as the default target [Germanic/docs/DEV_NOTES.md:38910-38928,39194-39196; Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:64-71,84,94-102].
- If packet extraction is refined later, mark `Germanic/docs/analysis/four_complex_tsv_items.md` more explicitly as mismatch-era history for this row so that its older `hlæhhan` framing is not promoted as live policy [Germanic/docs/lexeme_reports/research_memos/2092-laugh-hliehhan.md:19,29,104-105].
