---
row_id: 2271
concept: wart
counterpart: wearte
proto: "*wártōn"
protoform: "*wártōn"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2271 wart / wearte

## Current row state

- The live TSV row reads `CONCEPT = wart`, `COUNTERPART = wearte`, `PROTO = *wártōn`, `PROTOFORM = *wártōn`, `DERIVATION_CLASS = regular`, with only duplicated provenance in the source-note field: `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1323-1323].
- `PROTO` and `PROTOFORM` are string-identical in the current row, but they should still be kept conceptually separate from `COUNTERPART`. In this slice, both proto columns represent the comparative/project input `*wártōn`; `COUNTERPART` names the selected Old English output `wearte` [Germanic/data/germanic-aligned-final.tsv:1323-1323].
- The OE form chosen by the row is lexically well supported. Orel gives `*wartō(n) sb.f.: ON varta ‘wart', OE weart, wearte id.` [@Orel2003, p. 450; docs/references/orel_handbook_germanic_etymology.vision.txt:49631-49633], and Clark Hall likewise has `weart, wearte (a, e) f. ‘wart.` [@ClarkHall1960, s.v. "weart"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47442-47442]. That means the row's `COUNTERPART = wearte` is not an unsupported normalization; it is one of the attested dictionary variants.
- No row-specific packet, research memo, or pilot file was found for row `2271`. The only obvious row-local support files are the A-restoration analysis inventory, which lists `2271 | *wártōn | wearte | breaking`, and the published derivation trace, which reaches `wearte` directly [Germanic/docs/analysis/arestoration_r_l_research.md:743-749; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5580-5599].

## Detailed development-note summary

The surviving DEV_NOTES support for row `2271` is real but thin. There is no dedicated `wart / wearte` mini-essay in `Germanic/docs/DEV_NOTES.md`; instead, the row appears as a control item inside the February 2026 A-restoration fix for weak feminine `-ōn` stems. The only exact lexeme hit is the regression-table line `| *wartōn | wearte | wearte | wearte | unchanged (*r blocks) |` [Germanic/docs/DEV_NOTES.md:3844-3849]. That makes the row usable as project evidence, but it also means later writers should not pretend that DEV_NOTES contains a long row-specific rationale. It does not.

The crucial interpretive point is what `unchanged (*r blocks)` means in that note. In the immediately preceding explanation of the fix, DEV_NOTES says: `This change causes A-restoration to fire for root *a before consonant clusters (excluding *r, *l — which independently block A-restoration) followed by *ǭ` [Germanic/docs/DEV_NOTES.md:3830-3831]. For row `2271`, therefore, `*r blocks` refers to **A-restoration**, not to the development that produced `ea`. The row stays `wearte` because it belongs to the ordinary breaking class before `r + consonant`; it is not a special exception rescued by a blocker rule that suppresses breaking.

The published derivation trace confirms exactly that reading. It derives `*wártōn` through `NWGmc N Stem N Loss: *wártǭ`, then `Anglo Frisian Brightening: *wærtǭ`, then `OE Breaking: *weartǭ`, followed by unstressed-vowel adjustments to `*weartæ` and surface `wearte` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5587-5599]. This is the row's most concrete repo-local explanation of how the current `COUNTERPART` is obtained from the current `PROTOFORM`.

Campbell's grammar matches that derivation well. For the phonological step that matters most here, Campbell states that `æ was broken, and appears as ea with very great regularity, before r followed by a consonant`, giving examples such as `bearn`, `heard`, `hearg`, `mearh`, and `wearm` [@Campbell1959, §144; docs/references/campbell_old_english_grammar.txt:4469-4473]. That is the right comparative frame for `*wært- > *weart-`. On the restoration side, Campbell's §158 says restoration of `a` is common before single consonants and geminates, and also before `f` or `s` plus consonant, but `Before other groups, a is not restored except for a few instances before consonant plus liquid` [@Campbell1959, §158; docs/references/campbell_old_english_grammar.txt:4733-4744]. The cluster here is `rt`, not one of Campbell's ordinary restoration environments. So the grammar supports the same conservative reading as the DEV_NOTES regression table: this row should remain a breaking outcome, not an A-restoration case.

The in-repo A-restoration analysis makes that chronology explicit and ties it back to Ringe–Taylor. The analysis quotes Ringe–Taylor that retraction occurred `subsequently to fronting—and subsequently to breaking, because the diphthong of ‘slay’, etc. did not again become *a` [@RingeTaylor2014, §6.3.1; docs/references/ringe_taylor_linguistic_history_vol2.txt:11013-11015], then applies that logic to the affected rows and lists `2271 | *wártōn | wearte | breaking` among the unaffected items [Germanic/docs/analysis/arestoration_r_l_research.md:745-749]. That is useful because it shows that the row was not merely left untouched by accident: it was explicitly reviewed as part of the fix and retained in the breaking bucket.

Lexically, the row does not need a `PROTO`/`PROTOFORM` split to justify `COUNTERPART = wearte`. Orel and Clark Hall both give the OE lexeme as `weart, wearte` [@Orel2003, p. 450; @ClarkHall1960, s.v. "weart"]. The present dataset simply chooses the `wearte` member of that attested pair. So the distinction to preserve here is not between two different proto inputs, but between the row-level proto label/input (`*wártōn` in both proto columns) and the selected OE realization (`wearte`) [Germanic/data/germanic-aligned-final.tsv:1323-1323; docs/references/orel_handbook_germanic_etymology.vision.txt:49631-49633; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47442-47442].

The practical conclusion is conservative. Row `2271` looks stable and correctly classified as `regular`. The row's documentation base is not rich enough to support a dramatic narrative, but it is rich enough to support the current encoding: `*wártōn` is the proto/protoform input, `wearte` is an attested OE counterpart, and the relevant phonology is ordinary brightening plus breaking before `rC`, with A-restoration explicitly not taking over in this environment [Germanic/docs/DEV_NOTES.md:3830-3849; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5587-5599; @Campbell1959, §§144, 158].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3830-3835

- Source heading: `A-restoration interaction — a pipeline bug discovered`
- Source line or section hint: `lines 3830-3835`
- Fragment type: `shared_rule_context`
- Status: `current`
- Issue tags: `a_restoration_scope`; `r_blocks_restoration`; `weak_feminine_ōn_stems`; `interpretive_context`
- Recommended next use: `cite_with_row_specific_table_line`
- Shared with row IDs: `2016`; `2234`; `2271`

This is the most important interpretive fragment for row `2271`, even though it does not name `wearte` by itself. DEV_NOTES says that the A-restoration fix now fires `for root *a before consonant clusters (excluding *r, *l — which independently block A-restoration) followed by *ǭ` [Germanic/docs/DEV_NOTES.md:3830-3831]. That sentence explains how the row-specific table line should be read. For `*wártōn`, the relevant point is not that `r` somehow prevents the expected `ea`; rather, `r` prevents the later **restoration back to `a`**, leaving the earlier brightening-and-breaking path intact. This is why the row remains `wearte` rather than moving to an unbroken `warte`-type form.

### DEV_NOTES:line-3849-3849

- Source heading: `Regression check`
- Source line or section hint: `line 3849`
- Fragment type: `verification`
- Status: `current`
- Issue tags: `exact_match`; `wart_row`; `unaffected_by_fix`; `regular_breaking`
- Recommended next use: `weak_index_anchor_if_needed`
- Shared with row IDs: `2016`; `2168`; `2234`

This is the only exact DEV_NOTES line naming the row's lexeme: `| *wartōn | wearte | wearte | wearte | unchanged (*r blocks) |` [Germanic/docs/DEV_NOTES.md:3849-3849]. Its value is modest but real. It shows that after the `*ǭ` trigger was added for the `flasce`-type fix, `*wartōn` was deliberately checked and found already correct. The limitation is equally important: this is a regression-table sentinel, not a full lexeme note. It supports the current row as stable and regular, but it is not evidence for any more elaborate row-specific historical claim than that.

## Superseded or diagnostic material

- The duplicated live TSV source note should be treated as provenance only, not as the row's full evidentiary basis. The stronger support for the slice comes from the DEV_NOTES regression context, the derivation trace, Campbell's phonology, and the dictionary evidence for `weart, wearte` [Germanic/data/germanic-aligned-final.tsv:1323-1323; Germanic/docs/DEV_NOTES.md:3830-3849; docs/references/campbell_old_english_grammar.txt:4469-4473,4733-4744].
- The main diagnostic trap is to misread `unchanged (*r blocks)` as if `r` blocked breaking itself. That would invert the chronology. In the current project documentation, `r` blocks A-restoration, while the row still follows the ordinary `*æ > ea / _rC` breaking path to `wearte` [Germanic/docs/DEV_NOTES.md:3830-3849; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5593-5599].
- No superseded row-specific proto correction or counterpart replacement was located for row `2271`. The row appears in project history as a checked control item, not as a previously mis-set lexeme.

## Open questions for later work

- If a later full lexeme report is written, decide whether the report should quote both OE dictionary spellings explicitly as `weart, wearte`, while retaining `wearte` as the dataset's chosen `COUNTERPART` [@Orel2003, p. 450; @ClarkHall1960, s.v. "weart"].
- If `dev_notes_slices/index.tsv` is ever updated, the only plausible direct DEV_NOTES anchor is `DEV_NOTES:line-3849-3849`, probably cited together with `DEV_NOTES:line-3830-3835` so that `(*r blocks)` is not misinterpreted. The evidence is good enough for cautious indexing, but it remains a verification-table anchor rather than a dedicated row note.
- No current evidence suggests changing `PROTO`, `PROTOFORM`, `COUNTERPART`, or `DERIVATION_CLASS`. Later work here is more likely to involve source-hierarchy cleanup than lexical reanalysis.
