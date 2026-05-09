---
row_id: 1997
concept: drink
counterpart: drincan
proto: "*drínkaną"
protoform: "*drínkaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1997 drink / drincan

## Current row state

- The live Old English row now reads `ID 1997 | CONCEPT drink | COUNTERPART drincan | PROTO *drínkaną | PROTOFORM *drínkaną | DERIVATION_CLASS regular`; the provenance columns are just duplicated inherited-etymology placeholders, not a row-local explanatory note [Germanic/data/germanic-aligned-final.tsv:258-258].
- Coverage infrastructure still treats this row as uncovered: `coverage_audit.md` lists `| 1997 | drink | drincan | regular | no | - | - | - | none |`, so there is no pre-existing packet, research memo, or manifest-backed report path to reuse for this exact row [Germanic/docs/lexeme_reports/coverage_audit.md:228-228].
- `oe_known_problems.tsv` currently contains other OE exception buckets but no entry for `*drínkaną`, which is consistent with the row's present `regular` status and with the lack of any preserved mismatch narrative for `drincan` [Germanic/data/oe_known_problems.tsv:1-8].
- The published OE derivation snapshot already lands on the live target without repair: `PROTO: *drínkaną`, `EXPECTED: drincan`, `OUTPUTS: drincan`, with OE-side stages `Heavy Syllable Nasal Apocope: *drínkan`, `Secondary Nasalization: *drínkąn`, and `Weak Tail Reduction: *drínkan` before orthographic `drincan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1017-1036].

## Development-note summary

No row-specific DEV_NOTES section for `drink / drincan / *drínkaną` appears to survive in the current repo, and that absence should be stated plainly rather than filled with invented drama. The only directly attachable DEV_NOTES material is a shared Class III strong-verb discussion in which Campbell's paradigm list includes `drincan drink` among ordinary Old English verbs of the class [Germanic/docs/DEV_NOTES.md:7072-7079].

That surviving material is still useful, but only in a narrow way. It supports the row's current interpretation as a straightforward Class III strong verb whose `COUNTERPART` is the ordinary OE infinitive `drincan`; it does **not** preserve a row-local dispute about target selection, attestation, or a special reconstructed OE substitute. In other words, `PROTO` and `PROTOFORM` are both the comparative input `*drínkaną`, and the current `COUNTERPART` is simply the normal OE infinitive reflex the project already derives successfully [Germanic/data/germanic-aligned-final.tsv:258-258; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1017-1036].

The strongest shared wording to preserve is Campbell's paradigm quotation as copied into DEV_NOTES: `"bindan, bind — band, bond — bundon — bunden / Similarly many verbs, e.g. drincan drink, gelimpan happen, grindan grind, / springan spring, climban climb..."` [Germanic/docs/DEV_NOTES.md:7074-7079]. That is not a bespoke `drincan` note, but it is real project evidence that `drincan` was being handled as an ordinary member of the OE Class III strong-verb family rather than as an exception row.

The rest of the nearby DEV_NOTES cluster is mainly scope control. Immediately after naming `drincan`, the note pivots to `findan` and its special West Saxon past singular `funde`, i.e. to a levelling problem that does **not** transfer to row `1997` just because both verbs appear in the same Campbell paragraph [Germanic/docs/DEV_NOTES.md:7078-7082]. For this slice, the conservative conclusion is therefore simple: current support is mostly shared classificatory material plus a clean successful derivation trace, not a row-local philological dossier.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7074-7079

- Source label line: `Germanic/docs/DEV_NOTES.md:7074-7079`
- Source heading: `The Levelling Chronology`
- Source line or section hint: `Campbell (1959) §741 quotation inside the Class III discussion`
- Fragment type: `shared_family_background_with_explicit_lexeme_hit`
- Status: `current`
- Issue tags: `class_iii_strong_verb`; `explicit_drincan_hit`; `shared_background_not_row_specific`
- Recommended next use: `cite_when_explaining_why_row_1997_stays_a_regular_class_iii_control`
- Shared with row IDs: `1977`; `2011`; other Class III strong-verb rows discussed through the same Campbell passage

This is the one clear DEV_NOTES fragment that names the lexeme directly, so it should be preserved with its substance intact. DEV_NOTES says `**Campbell (1959) §741** describes the OE Class III paradigm`, then quotes: `"bindan, bind — band, bond — bundon — bunden / Similarly many verbs, e.g. drincan drink, gelimpan happen, grindan grind, / springan spring, climban climb..."` [Germanic/docs/DEV_NOTES.md:7074-7079]. The underlying Campbell text in the repo reference file matches that wording closely enough to keep the quotation live for working-note purposes [docs/references/campbell_old_english_grammar.txt:20784-20788].

For row `1997`, the value of the fragment is classificatory, not problem-solving. It shows that when DEV_NOTES needed an OE Class III comparator list, `drincan` was unremarkable enough to appear in the ordinary paradigm inventory. That supports the current row state (`regular`, exact target match, no known-problem flag), but it does **not** amount to a hidden row-specific argument about alternate protoforms, analogical replacement, or uncertain attestation [Germanic/data/germanic-aligned-final.tsv:258-258; Germanic/data/oe_known_problems.tsv:1-8].

### DEV_NOTES:line-7081-7082

- Source label line: `Germanic/docs/DEV_NOTES.md:7081-7082`
- Source heading: `The Levelling Chronology`
- Source line or section hint: `Campbell follow-up immediately after the Class III list`
- Fragment type: `nearby_scope_limiting_context`
- Status: `current_but_not_row_specific`
- Issue tags: `neighboring_findan_problem`; `negative_scope`; `do_not_overread_shared_context`
- Recommended next use: `cite_if_later_work_needs_to_explain_why_the_surrounding_passage_does_not_create_a_drincan_issue`
- Shared with row IDs: `2011`; nearby Class III rows cited from the same passage

This second fragment matters because it marks where the useful `drincan` evidence stops. Right after the shared Class III quotation, DEV_NOTES says that Campbell notes OE `findan` has `d` throughout and even a West Saxon preterite singular `funde`, replacing expected `×fand` [Germanic/docs/DEV_NOTES.md:7081-7082]. The substance here is not a `drincan` claim; it is a warning against importing a neighboring `findan` levelling narrative into row `1997` merely because Campbell's verb list mentioned `drincan` first.

That negative scope is worth preserving in the slice because otherwise later reporting could misread the cluster as if every verb in the list shared the same problem profile. The present repo evidence does not do that. For `drincan`, the live derivation trace already succeeds exactly, and no surviving DEV_NOTES prose says that the row needed the kind of repair or paradigm-cell substitution discussed for `findan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1017-1036; Germanic/docs/DEV_NOTES.md:7099-7111].

## Superseded or diagnostic material

- No superseded row-specific DEV_NOTES note was located for `drincan`. The present replacement slice therefore has to be explicit that current project history preserves **shared** Class III background, not a lost lexeme dossier [Germanic/docs/lexeme_reports/coverage_audit.md:228-228; Germanic/docs/DEV_NOTES.md:7072-7082].
- The published derivation snapshot is diagnostic rather than DEV_NOTES authority, but it is materially useful because it shows that the current implementation already derives `drincan` directly from `*drínkaną` with no row-local workaround or alternate input [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:1017-1036].
- Additional handbook/reference material in the repo confirms that `drincan` is an ordinary strong verb with the familiar ablaut set `dranc, druncon, druncen`, but those are supporting comparanda rather than surviving DEV_NOTES content. Hogg's morphology discussion, for example, names `drincan 'drink'` with forms `dranc, druncon, gedruncen` and derivative family members; that is helpful confirmation, but it should not be mistaken for a row-local project memo [docs/references/hogg_vol1.txt:14193-14202].

## Open questions for later work

- If later lexeme-report curation decides that row `1997` needs index-level infrastructure, decide whether a single shared Campbell/Class III fragment is enough, or whether the row should remain a slice-only control item until more lexeme-specific material exists.
- If a future strong-verb family memo is written, attach `drincan` there alongside `climban`, `grindan`, and `springan`, since the surviving DEV_NOTES support is fundamentally family-level rather than row-level [Germanic/docs/DEV_NOTES.md:7074-7079].
- If later work revisits Class III paradigm reporting, it may be worth adding a clean attestation-facing note from the repo reference corpus for `drincan, dranc, druncon, druncen`; the current slice can already point to such material, but the present row does not yet need that heavier apparatus because the implementation and shared DEV_NOTES evidence are both stable [docs/references/bright_anglo_saxon_reader.txt:2445-2445; docs/references/hogg_vol1.txt:14193-14202].
