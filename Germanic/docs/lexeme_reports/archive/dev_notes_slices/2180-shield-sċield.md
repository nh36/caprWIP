---
row_id: 2180
concept: shield
counterpart: sċield
proto: *skélduz
protoform: *skélduz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2180 shield / sċield

## Current row state

- The live OE row currently reads `CONCEPT = shield`, `COUNTERPART = sċield`, `PROTO = *skélduz`, `PROTOFORM = *skélduz`, `DERIVATION_CLASS = regular`, with an empty `NOTE` field and only source-history boilerplate in `HISTORY` [Germanic/data/germanic-aligned-final.tsv:970-970].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not using a surrogate modelling stem, a paradigm-cell substitute, or a split between cognate-set label and OE-facing input. The same Proto-Germanic nominative singular form serves both as comparative headword and as derivational input [Germanic/data/germanic-aligned-final.tsv:970-970].
- `oe_known_problems.tsv` has no entry for row `2180`, for `shield`, for `sċield`, or for `*skélduz`, which is consistent with the row's current status as a solved regular derivation rather than a live exception bucket [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage tracking currently lists row `2180` as `regular`, with no packet, research memo, or manifest-backed report and requirement basis `none` [Germanic/docs/lexeme_reports/coverage_audit.md:347-347].
- The current published derivation trace is an exact match and gives the live stage sequence explicitly: `PROTO: *skélduz`, `EXPECTED: sċield`, `OUTPUTS: sċield`, with the derivational chain `PGmc Final Z Deletion: *skéldu`, `OE Sk Palatalization: *ʃéldu`, `OE Ws Palatal Diphthongization: *ʃíeldu`, `OE High Vowel Apocope: *ʃíeld`, then orthographic outcome `sċield` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4079-4099].
- The best row-specific comparative support now in the repo sits outside `DEV_NOTES` proper: the West-Saxon-vs.-Anglian analysis table lists `*skelduz` with West Saxon `scield` beside Mercian `sceld`, explicitly attributing the split to absence of palatal diphthongization outside West Saxon [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:453-460,701-703].

## Development-note summary

No dedicated `shield / sċield` lexeme section survives in `DEV_NOTES.md`. The replacement working note therefore has to be built from shared phonology notes plus the exact current derivation trace. That surviving evidence is still enough to state the live row conservatively. The row is currently regular and exact from `*skélduz`, but the support is mostly indirect: a stale project TODO naming `shield` among forms that need `*sk > ʃ` before front vowels, a reusable terminology note explaining that `sk > sc` is really the OE `/sk/ > /ʃ/` shift, and current chronology notes on West-Saxon palatal diphthongization showing that initial palatals convert surviving `e` to `ie` only when no earlier i-umlaut trigger removes the `e` first [Germanic/docs/DEV_NOTES.md:1795-1795,2991-2993,11309-11329; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4092-4099].

The distinction between `PROTO`, `PROTOFORM`, and the attested OE target is straightforward and should remain explicit. `PROTO = PROTOFORM = *skélduz` in the live TSV, so there is no row-policy split of the kind seen in analogy rows or paradigm-cell rescue rows [Germanic/data/germanic-aligned-final.tsv:970-970]. By contrast, the trace forms `*skéldu`, `*ʃéldu`, `*ʃíeldu`, and `*ʃíeld` are chronological derivational stages inside the current cascade, not rival stored protoforms [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4092-4099]. The unaccented `*skelduz` used in the dialect-analysis table is best treated as a notation variant of the same PGmc form, not as a different historical stage or a competing project policy; the accent in `*skélduz` is the project's stressed-vowel notation, while the analysis file uses plainer comparative spelling [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:453-460; Germanic/data/germanic-aligned-final.tsv:970-970].

The orthographic layer also needs to be kept separate from the phonological one. The current TSV and trace write the OE target as project-normalized `sċield`, but the dialect-analysis table writes manuscript-style `scield` and Mercian `sceld` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4096-4099; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:703-703]. `DEV_NOTES` explicitly warns in a neighboring `sk` note that "`sk -> sc` ... is not palatalization but a general OE shift of `/sk/ -> /ʃ/` spelled ⟨sc⟩" [Germanic/docs/DEV_NOTES.md:2991-2993]. For this row that means `sċ-` versus `sc-` is an editorial notation issue, while `/sk/ > /ʃ/` is the actual phonological stage.

The current live derivation also fits the surviving chronology notes cleanly. After final `*-z` deletion, the form reaches OE as `*skéldu`; initial `sk` then shifts to `ʃ`; because there is no i-umlaut trigger comparable to the `*-iz` tail in rows such as `ġift`, the front vowel `e` survives long enough for West-Saxon palatal diphthongization to convert it to `ie`; finally high-vowel apocope removes final `u`, leaving `sċield` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4092-4099; Germanic/docs/DEV_NOTES.md:11311-11329]. The dialect analysis gives the philological counterpart of that same chronology: West Saxon `scield` versus Mercian `sceld`, with the Anglian form reflecting absence of the West-Saxon diphthongization stage [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:701-703]. That matches the general `DEV_NOTES` quotation from Campbell §187 that “The diphthongization of front vowels after palatals is unknown to all Kt. and Merc. texts” [Germanic/docs/DEV_NOTES.md:6527-6529].

What does **not** survive is a row-specific DEV_NOTES quotation from a handbook or dictionary saying in so many words that OE `scield/sċield` continues `*skelduz/*skélduz`. The slice should therefore say plainly that the row is well supported as a live exact derivation, but the in-repo DEV_NOTES evidence is mostly shared-process and notation material rather than a dedicated shield dossier. That makes the row usable as a working note, but weaker as a candidate for central index extraction than rows with direct lexeme-specific DEV_NOTES sections.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1795-1795

- Source heading: `Project Status (as of 2026-03-10)`
- Source line or section hint: `line 1795`
- fragment_type: `stale_project_todo`
- current_status: `diagnostic_only`
- Issue tags: `sk_shift`; `front_vowel_context`; `historical_bug_state`
- recommended_next_use: `use_as_project_history_only`
- Shared with row IDs:

This one-line TODO is stale and comes from the English-sandbox side of the repo, but it is still the earliest explicit surviving place where `shield` is named as a form requiring a missing palatalisation pass: “Add the missing palatalisation pass ... `{*sk→ʃ}` before front vowels ... needed for `believe/beech/chew/shield/ship`” [Germanic/docs/DEV_NOTES.md:1795-1795]. For row `2180` that note does **not** function as current OE analysis, and it should not be mistaken for a shield-specific historical derivation. What it preserves is project history: `shield` was one of the lexemes that originally exposed the need for an initial `sk`-before-front-vowel treatment.

The fragment is therefore useful only as background on why shield-family rows show up in later exact-match traces. It should not be cited by itself as evidence that the current OE row needs repair, because the published OE derivation trace now already yields `sċield` exactly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4079-4099].

### DEV_NOTES:line-2991-2993

- Source heading: `Missing ēa diphthong + sk/sc issue (*skawô → sċawa vs scēawa)`
- Source line or section hint: `lines 2991-2993`
- fragment_type: `shared_terminology_and_notation`
- current_status: `diagnostic_but_reusable`
- Issue tags: `sk_shift`; `notation_layer`; `orthography`; `terminology`
- recommended_next_use: `cite_for_notation_clarity`
- Shared with row IDs: `2175`, `2181`

This short note is not about `shield`, but it is the most explicit in-repo warning against collapsing sound change and spelling convention. DEV_NOTES says that the `sk -> sc` change “is not palatalization but a general OE shift of `/sk/ -> /ʃ/` spelled ⟨sc⟩” [Germanic/docs/DEV_NOTES.md:2991-2993]. That sentence is directly reusable here because row `2180` is otherwise easy to misdescribe: the trace labels one stage `OE Sk Palatalization`, the TSV writes the output as `sċield`, and the dialect table writes `scield/sceld` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4092-4099; Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:703-703].

For this row, the reusable substance is narrow but important. The historical stage is `/sk/ > /ʃ/`; the spelling layer may be shown as project-normalized `sċ-` or manuscript-style `sc-`; and neither notation choice implies a different protoform or a different dialectal outcome. That distinction belongs in any future report prose on `sċield`.

### DEV_NOTES:line-6527-6529

- Source heading: `Campbell (1959) §187 via OE ġift 'gift'`
- Source line or section hint: `lines 6527-6529`
- fragment_type: `shared_scope_quote`
- current_status: `current`
- Issue tags: `ws_palatal_diphthongization`; `dialect_scope`; `west_saxon_only`
- recommended_next_use: `cite_with_dialect_scope_note`
- Shared with row IDs: `2040`, `2175`, `2178`

This Campbell quotation is not shield-specific, but it is the cleanest surviving DEV_NOTES statement about the dialect distribution that matters for row `2180`: “The diphthongization of front vowels after palatals is unknown to all Kt. and Merc. texts” [Germanic/docs/DEV_NOTES.md:6527-6529]. In isolation, that only states a general fact about palatal diphthongization. In combination with the local analysis table listing West-Saxon `scield` beside Mercian `sceld`, it becomes directly explanatory for the row's target selection [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:701-703].

For this slice, the quote should therefore be used with scope discipline. It does not attest `shield` by itself, but it does explain why the row's exact live output is a West-Saxon-looking `sċield` rather than an Anglian/Mercian `sceld`.

### DEV_NOTES:line-11309-11329

- Source heading: `Background: WS palatal diphthongization vs i-umlaut`
- Source line or section hint: `lines 11309-11329`
- fragment_type: `shared_chronology_rule`
- current_status: `current`
- Issue tags: `ws_palatal_diphthongization`; `i_umlaut`; `chronology`; `e_to_ie`
- recommended_next_use: `cite_as_shared_process_support`
- Shared with row IDs: `2041`, `2069`, `2178`

This is the most useful current DEV_NOTES fragment for the actual vowel history behind `sċield`. DEV_NOTES lays out two contrasting cases. Without an i-umlaut trigger, as in `*gebaną`, palatalization creates an initial palatal and West-Saxon palatal diphthongization then changes `*e` to `*ie`, yielding `giefan`; with an i-umlaut trigger, as in `*geftiz`, `*e` first becomes `*i`, and West-Saxon palatal diphthongization then has no `*e` left to target, yielding `ġift` [Germanic/docs/DEV_NOTES.md:11311-11329].

Row `2180` is not named in this section, but its live trace fits squarely on the first side of that contrast. After `*skélduz > *skéldu > *ʃéldu`, the row still has `e`, not umlauted `i`, so West-Saxon palatal diphthongization can apply and produce `*ʃíeldu`, after which high-vowel apocope gives `*ʃíeld` and surface `sċield` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4092-4099]. This fragment is therefore the best current DEV_NOTES support for the row's successful `e > ie` stage, even though the shield lexeme itself appears only in the trace and analysis materials.

## Superseded or diagnostic material

The main stale item is the old palatalisation TODO naming `shield` among unresolved forms [Germanic/docs/DEV_NOTES.md:1795-1795]. It is worth keeping only because it records that shield once functioned as a regression detector for missing `*sk > ʃ` support. It is not current row policy, and it should not be cited as if row `2180` were still broken.

The more durable caution is not a wrong analysis but an evidentiary gap. No dedicated `shield` packet, research memo, or lexeme-specific DEV_NOTES section survives, and the row's strongest direct statement (`*skelduz` → WS `scield`, Merc. `sceld`) currently lives in the separate dialect-analysis file rather than in `DEV_NOTES` itself [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:701-703]. The exact derivation trace is current and persuasive, but it is still a generated project artifact rather than a copied primary or secondary source statement [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4079-4099].

That combination makes the row a good candidate for a replacement working dossier but a cautious candidate for index integration. The live derivation is regular and exact, yet the surviving DEV_NOTES material is mostly shared-process support plus notation hygiene, not a row-local literature audit. If a future index row is desired, the safest upgrade path would be to anchor it with a direct shield-specific source quotation rather than relying only on indirect shared chronology plus the repo's analysis table.

## Open questions for later work

- If a future index entry is wanted, locate or quote the underlying Ringe-Taylor passage directly rather than relying only on the repo's extracted table `*skelduz > scield / sceld` [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:701-703].
- Decide whether future report prose should cite the target primarily as project-normalized `sċield` or as manuscript-style `scield`, while keeping clear that this is an orthographic/editorial choice rather than a different derivation [Germanic/docs/DEV_NOTES.md:2991-2993; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4096-4099].
- If a stronger row dossier is later assembled, add a shield-specific packet or memo so the row no longer depends mainly on shared DEV_NOTES process notes plus the generated derivation trace.
