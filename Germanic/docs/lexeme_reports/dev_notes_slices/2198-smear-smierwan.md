---
row_id: 2198
concept: smear
counterpart: smierwan
proto: *smérwijaną
protoform: *smérwijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2198-smear-smierwan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2198-smear-smierwan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2198 smear / smierwan

## Current row state

- The live OE row is `CONCEPT = smear`, `COUNTERPART = smierwan`, `PROTO = *smérwijaną`, `PROTOFORM = *smérwijaną`, `DERIVATION_CLASS = regular`, with the TSV note `Source: Kroonen p.458 *smerwjan- > OE smierwan; R/T §6.7.1 p.289 WS smierwan (Merc. smirwan is Anglian)` [Germanic/data/germanic-aligned-final.tsv:1039-1039].
- The live published derivation trace already returns the target exactly. Its compact path is `*smérwijaną > *sméorwijaną > *sméorwjąn > *smíerwjąn > *smíerwan > smierwan`, with the named OE rules `OE Breaking`, `Sievers Law Syncope`, `OE I Umlaut`, `OE Weak Tail Reduction`, and `OE J Loss After Heavy` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4386-4405; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29700-29813].
- `oe_known_problems.tsv` has no entry for row `2198`, for `*smérwijaną`, or for `smierwan`; the row is therefore not currently being tracked as an exception or unresolved transducer failure [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage audit still lists the row among note-bearing regular OE items that need row-level documentation: `| 2198 | smear | smierwan | regular | yes | - | - | - | NOTE |` [Germanic/docs/lexeme_reports/coverage_audit.md:136-136].
- Existing packet and memo infrastructure already treat the row as a stable WS-target row and recommend keeping `PROTO`, `PROTOFORM`, `COUNTERPART`, and `DERIVATION_CLASS` unchanged, while clarifying the prose so Kroonen's comparative headword and Ringe-Taylor's later-stage reconstruction are not conflated [Germanic/docs/lexeme_reports/research_memo_index.tsv:95-95; Germanic/docs/lexeme_reports/research_memos/2198-smear-smierwan.md:19-21,58-61,105-111].

## Development-note summary

Current project evidence supports keeping row 2198 exactly where it already is: a **regular** OE row whose live target is West Saxon `smierwan`, with unchanged `PROTO = PROTOFORM = *smérwijaną` [Germanic/data/germanic-aligned-final.tsv:1039-1039; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4386-4405]. The slice has to keep three layers separate, because the surviving DEV_NOTES material and the cited scholarship do not all speak at the same chronological level.

The first layer is the comparative headword behind the current TSV fields. Kroonen's dictionary entry gives the etymon as `*smerwjan-`, citing OE `smierwan` among the reflexes [@Kroonen2013, p. 458; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23661-23662]. The live TSV's `*smérwijaną` is not a different etymological claim from Kroonen's `*smerwjan-`; it is the row-local infinitive-style expansion of that same comparative reconstruction in current house notation. DEV_NOTES' older spelling `*smerwijăną` is likewise the same Kroonen-aligned input written in an earlier notation layer with breve-marked unstressed `ă`, not a separate stage reconstruction [Germanic/docs/DEV_NOTES.md:15378-15397].

The second layer is Ringe-Taylor's later Northwest/Proto-West-Germanic-stage reconstruction. Ringe-Taylor explicitly gives `PNWGmc *smirwijana 'to smear, to anoint'` and derives `Merc. smirwan`, `North. smiriga`, and `WS smierwan` from that later stage [@RingeTaylor2014, §6.7.1, p. 183; @RingeTaylor2014, p. 248; docs/references/ringe_taylor_linguistic_history_vol2.txt:10656-10657,14371-14373]. That `*smirwijana` is a genuinely different chronological analysis from Kroonen's PGmc `*smerwjan-`; it is not just spelling variation. The DEV_NOTES disagreement block is valuable precisely because it preserves this distinction instead of collapsing the two authorities into one undifferentiated protoform [Germanic/docs/DEV_NOTES.md:15382-15395].

The third layer is the OE row target itself. The row does **not** target every member of the OE lexical family. It targets the West Saxon citation-form `smierwan`, which the live cascade already produces exactly [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29759-29813]. Ringe-Taylor's dialect note supports that choice by opposing WS `smierwan` to Mercian `smirwan` and Northumbrian `smiriga` [@RingeTaylor2014, §6.7.1, p. 183; docs/references/ringe_taylor_linguistic_history_vol2.txt:10656-10657]. Campbell independently supports the Anglian side of that contrast: in Anglian dialects, breaking of `i` before `r + consonant` regularly failed when `-i-` followed in the next syllable, and `smirwan` is one of his explicit examples [@Campbell1959, §154.3; docs/references/campbell_old_english_grammar.txt:4628-4638]. The local analysis file repeats the same point in project prose and correctly treats `smirwan` as the Anglian unbroken counterpart to WS `smierwan` [Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md:257-265].

The live derivation trace matters because it shows which analysis the current grammar is actually implementing. Starting from the Kroonen-aligned row input `*smérwijaną`, the trace applies OE breaking to stressed `e` before `r + C`, yielding `*sméorwijaną`; removes the heavy-syllable nasal ending and then the Sievers-law `i`, producing `*sméorwjąn`; then applies OE i-umlaut to produce `*smíerwjąn`; finally weak-tail reduction and post-heavy `j` loss produce `*smíerwan`, surfacing as `smierwan` [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29759-29813]. That derivation is specifically the Kroonen-style `e > eo > ie` pathway, not the Ringe-Taylor `i > io > ie` pathway. So the live row does not merely cite Kroonen in the note; it actually derives the OE form from a Kroonen-compatible input.

The lexicographic background is broader than the row target and should stay broader. Clark Hall heads the family under `smierwan`, explicitly notes spelling variation `(e, i, y)`, and cross-references `smirewan`, `smirian`, and `smirwan` back to that headword [@ClarkHall1960, s.v. smierwan; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:37047-37056]. Brunner shows the same family as philologically messy in historical OE, with West Saxon `smierwan`, Anglian forms with `i`, and early attraction into class-II forms such as `smirian`, `smyrian`, and preterite `smyrode` [@SieversBrunner1965, §§407--408; docs/references/brunner_1965_altenglische_grammatik.txt:16361-16405]. Bright likewise gives `smierwan ... smyrian; pret. smyrode` as a later pedagogical lexical-family presentation [@BrightCassidyRingler1971, §97; docs/references/bright_anglo_saxon_reader.vision.txt:3832-3836]. None of that overturns the row target; it means only that `smierwan` is the chosen inherited WS citation form, while `smirwan`, `smiriga`, `smirian`, `smyrian`, `smyrode`, and dictionary simplifications like `smerian` are comparators, variants, or later reshaped family members rather than silent replacements for the row's `COUNTERPART` [Germanic/data/old_english_wiktionary.tsv:259-259].

What survives in DEV_NOTES is therefore enough to explain the row, but not enough to make the row a clean index candidate. One fragment is genuinely current and useful: the Campbell-based explanation that Anglian `smirwan` is unbroken whereas WS `smierwan` shows breaking plus i-umlaut [Germanic/docs/DEV_NOTES.md:15270-15299]. The other substantial fragment is mixed in status: its quotations from Kroonen and Ringe-Taylor are still useful and accurate, but its closing editorial sentence that the TSV “may need updating if we prefer R/T's reconstruction” is project-history rather than current row policy [Germanic/docs/DEV_NOTES.md:15382-15397]. The memo and live trace now point the other way: keep the row, but explain its source layering more carefully [Germanic/docs/lexeme_reports/research_memos/2198-smear-smierwan.md:83-91,105-111].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-15270-15299

- Source heading: `The Anglian Exception (Campbell §154.3)`
- Source line or section hint: `lines 15270-15299`
- Fragment type: `shared_dialect_background_with_row_specific_application`
- Status: `current`
- Issue tags: `anglian_failure_of_breaking`; `ws_vs_anglian`; `i_plus_rC`; `dialect_distribution`
- Recommended next use: `cite_in_row_dossier_not_as_full_index_anchor`
- Shared with row IDs: `2057; 2095`

DEV_NOTES quotes Campbell's statement that in Anglian dialects “the breaking of i regularly failed before r followed by a consonant if -i- stood in the next syllable,” and the examples explicitly include “forms and derivatives of **smirwan** smear” [@Campbell1959, §154.3; Germanic/docs/DEV_NOTES.md:15290-15297; docs/references/campbell_old_english_grammar.txt:4628-4638]. DEV_NOTES then draws the row-level conclusion in its own words: “This is why Anglian has `smirwan` (unbroken) while WS has `smierwan` (broken + i-umlaut)” [Germanic/docs/DEV_NOTES.md:15298-15299]. For row 2198 this fragment is real current authority. It does not choose the comparative protoform, but it does justify the OE dialect contrast encoded in the TSV note and in the research memo.

### DEV_NOTES:line-15378-15395

- Source heading: `Source Disagreement: *smerwijăną vs *smirwijăną`
- Source line or section hint: `lines 15378-15395`
- Fragment type: `source_audit_with_live_row_relevance`
- Status: `mixed_current`
- Issue tags: `proto_vs_protoform`; `chronological_stage_distinction`; `kroonen_vs_ringe_taylor`; `derivational_pathways`
- Recommended next use: `cite_for_source_layering_with_explicit_status_note`
- Shared with row IDs:

This fragment preserves the most important source-classification fact about the row. DEV_NOTES quotes Kroonen's `*smerwjan-` with reflexes including OE `smierwan`, then quotes Ringe-Taylor's `PNWGmc *smirwijana ... > *smiorwjan ... > WS *smierwjan ... > smierwan`, and explicitly states that both analyses reach the same OE outcome through different pathways [Germanic/docs/DEV_NOTES.md:15382-15395; @Kroonen2013, p. 458; @RingeTaylor2014, §6.7.1, p. 183; @RingeTaylor2014, p. 248]. For row 2198 this is the essential dossier fragment because it keeps distinct what later prose must also keep distinct: Kroonen's PGmc headword, Ringe-Taylor's later-stage Northwest/Proto-West-Germanic reconstruction, and the attested/project-target OE form `smierwan`. The fragment is usable, but only if the notation layers are explained: DEV_NOTES `*smerwijăną` corresponds to the live row's `*smérwijaną` as house-notation variants of the same Kroonen-aligned input, whereas Ringe-Taylor's `*smirwijana` is a different chronological reconstruction.

### DEV_NOTES:line-15395-15397

- Source heading: `Source Disagreement: *smerwijăną vs *smirwijăną`
- Source line or section hint: `lines 15395-15397`
- Fragment type: `diagnostic_project_history`
- Status: `stale`
- Issue tags: `editorial_revision_history`; `possible_protoform_rewrite`; `not_current_policy`
- Recommended next use: `retain_only_as_history`
- Shared with row IDs:

The final sentence of the disagreement block says: “Our TSV follows Kroonen (`*smerwijăną`), which is defensible but may need updating if we prefer R/T's reconstruction” [Germanic/docs/DEV_NOTES.md:15395-15397]. That sentence is no longer current row policy. The live memo's explicit recommendation is **not** to change `PROTO` or `PROTOFORM`, but to improve the explanatory prose so the two source layers are not blurred [Germanic/docs/lexeme_reports/research_memos/2198-smear-smierwan.md:105-111]. This fragment should therefore be preserved only as evidence of an earlier editorial uncertainty, not as a standing instruction to rewrite the data row.

## Superseded or diagnostic material

- `old_english_wiktionary.tsv` gives `smear -> smerian`, which is useful as a reminder that compact lexical tables often collapse this family under a later or simplified lemma, but it is not good authority for retargeting row 2198 away from `smierwan` [Germanic/data/old_english_wiktionary.tsv:259-259].
- Clark Hall's cross-references and Brunner's discussion show that the family contains `smirewan`, `smirwan`, `smirian`, and `smyrian`; Bright adds `smyrode` as a later class-II-family form [@ClarkHall1960, s.v. smierwan; @SieversBrunner1965, §§407--408; @BrightCassidyRingler1971, §97; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:37047-37056; docs/references/brunner_1965_altenglische_grammatik.txt:16390-16405; docs/references/bright_anglo_saxon_reader.vision.txt:3832-3836]. Those forms are philologically relevant but diagnostically dangerous if treated as rival row targets. The row is an infinitive/citation-form dossier for inherited WS `smierwan`, not a whole-family inventory row.
- The packet's statement that DEV_NOTES had “_None_” under high-confidence hits is only a packet-matching artifact; the real DEV_NOTES material is present but sits in shared background sections rather than in a row-dedicated repair note [Germanic/docs/lexeme_reports/packets/2198-smear-smierwan.md:44-60,132-178].
- The row does not currently need paradigm probing or FST repair. The live trace already derives the target exactly, and the remaining issue is documentary clarity about source layers and dialect comparators, not missing morphology or a broken cascade [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4386-4405; Germanic/docs/lexeme_reports/research_memos/2198-smear-smierwan.md:83-97].

## Open questions for later work

- If row 2198 is ever indexed, decide whether an index row should cite only the current Campbell-based dialect fragment, or whether the source-disagreement block can be indexed as well despite its stale final sentence. At present the DEV_NOTES evidence is probably too mixed to serve as a clean index anchor without this slice's explanatory mediation.
- If the live TSV note is later rewritten outside this slice, the safest wording will distinguish source layers explicitly: Kroonen for the comparative PGmc headword `*smerwjan-`; Ringe-Taylor for later-stage `*smirwijana` and the dialect distribution `WS smierwan` vs. `Merc./Anglian smirwan`; and the live transducer for the current Kroonen-aligned derivation from `*smérwijaną` to `smierwan`.
- If a later report needs fuller lexicographic discussion, keep citation-form `smierwan` separate from secondary family material such as `smiriga`, `smirian/smyrian`, and `smyrode`; otherwise the row will start to look like a dispute over lemma choice when the real issue is only how broadly to describe the OE family.
