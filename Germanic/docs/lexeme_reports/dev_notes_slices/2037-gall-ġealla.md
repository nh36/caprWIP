---
row_id: 2037
concept: gall
counterpart: ġealla
proto: *gállą
protoform: *gállô
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2037-gall-ġealla.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2037 gall / ġealla

## Current row state

- CONCEPT: `gall`
- COUNTERPART: `ġealla`
- PROTO: `*gállą`
- PROTOFORM: `*gállô`
- DERIVATION_CLASS: `early_analogy`
- Live TSV row policy: the cognate-set headword stays `*gállą`, but the OE derivational input is the weak masculine `*gállô`; the row history already says the older strong-neuter setup was replaced because OE `ġealla` is weak masculine and because the strong input had yielded the wrong bare form [Germanic/data/germanic-aligned-final.tsv:415].
- `oe_known_problems.tsv`: no entry for row 2037, `*gállô`, `*gállą`, or `ġealla`, which matches the row's present status as solved rather than still open-ended [Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv`: no manifest row for 2037 is currently present; the file still lists only the earlier pilot set, so this slice has to function as the row's detailed replacement working note rather than as a pointer to some completed report [Germanic/docs/lexeme_reports/report_manifest.tsv:1-14].
- Packet and memo state agree on the essential live split: the packet's compact trace shows `*gállô -> ġealla`, while the memo explicitly warns that the live evidence does **not** justify collapsing `PROTO` and `PROTOFORM` into the same weak-noun form [Germanic/docs/lexeme_reports/packets/2037-gall-ġealla.md:17-41; Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md:13-22,51-60].

## Development-note summary

The row-specific DEV_NOTES authority for 2037 is concentrated and unusually clean. The note begins with the exact modelling failure that mattered for Old English: the earlier TSV entry used `*gallą` as a strong neuter a-stem, and the pipeline therefore produced bare `ġeall` after heavy-syllable apocope, even though the expected OE lexeme is `ġealla` [DEV_NOTES:line-3700-3703]. For later workflow, that matters more than the generic mismatch label: the problem was not breaking, palatalization, or some hidden OE surface repair, but the wrong inherited stem class being fed into the transducer.

DEV_NOTES then preserves the correction that still governs the row. It cites Kroonen's weak-noun reconstruction `*gallōn-`, using nominative singular `*gallô`, and pairs that with the lexicographic statement `"ġealla, an; m."` to make the philological point explicit: OE `ġealla` is a weak masculine noun, not a strong neuter reflex of `*gállą` [DEV_NOTES:line-3705-3706]. That direct quotation should be kept in any later report or note refresh, because it is the compact source-backed reason the row switched away from the old a-stem input.

The same fragment also explains why the corrected row is now straightforward rather than precarious. Once the OE-facing input is weak `*gállô`, DEV_NOTES says the derivation runs normally: `*gallô -> ġealla`, with the weak suffix passing through `NWGmcNStemNLoss`, then unstressed long-vowel shortening, and surfacing as final `-a`; the packet's trace reproduces the same successful result and the memo's comparator probe confirms the practical contrast `*gállą -> ġeall` versus `*gállô -> ġealla` [DEV_NOTES:line-3708-3709; Germanic/docs/lexeme_reports/packets/2037-gall-ġealla.md:17-41; Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md:43-49,72-83]. In other words, row 2037 is an `early_analogy` / stem-selection case upstream of OE sound change, not an unresolved surface exception.

What later writers most need from this slice is the three-level distinction that DEV_NOTES itself only partly preserves and the live TSV now preserves better. The cognate-set label remains `PROTO = *gállą`, shared with the non-OE rows in set 205; the actual OE derivational input is `PROTOFORM = *gállô`; and the target is the attested weak noun `ġealla` / dictionary `gealla` [Germanic/data/germanic-aligned-final.tsv:413-416; Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md:51-60]. That split is not optional explanatory garnish. It is the whole reason the current row can both remain aligned with the wider cognate set and still derive the OE form correctly.

The remaining caution is that DEV_NOTES closes the row with one sentence that no longer matches live policy. Its final cognate-set note correctly says that German `Galle` has a different gender and declension class and that the other cognate-set rows retain `*gallą`, but it then adds that the OE row now has `*gallô` in both `PROTOFORM` and `PROTO` columns [DEV_NOTES:line-3711-3713]. The live TSV contradicts only that last clause, not the broader warning about mixed declensional behavior inside cognate set 205 [Germanic/data/germanic-aligned-final.tsv:413-416]. For replacement-note purposes, the durable conclusion is therefore: keep the strong-vs-weak correction, keep the cognate-set caution, and treat the claim about both columns changing as stale project history rather than current row authority.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3700-3709

- Source heading: `Case 1: *gallą -> *gallô (OE ġealla 'gall, bile')`
- Source line or section hint: `lines 3700-3709`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `stem_class`; `protoform_vs_proto`; `early_analogy`; `weak_noun_correction`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core row-specific authority and should do most of the replacement-note work by itself. DEV_NOTES states the exact failure mode first: older TSV `*gallą` behaved like a strong neuter a-stem and yielded bare `ġeall` after heavy-syllable apocope, but OE needs `ġealla` [DEV_NOTES:line-3702-3703]. It then records the philological correction, citing Kroonen's `*gallōn-` and the nominative singular `*gallô`, and preserving the Bosworth-Toller-style gloss `"ġealla, an; m."` as evidence that the OE noun is weak masculine [DEV_NOTES:line-3705-3706]. The closing lines are equally important because they show that no special downstream rescue is needed once the stem class is fixed: `*gallô -> ġealla` works regularly via weak-noun `*-ô`, `NWGmcNStemNLoss`, and unstressed-vowel shortening [DEV_NOTES:line-3708-3709].

### DEV_NOTES:line-3711-3713

- Source heading: `same ġealla note: cognate-set warning and stale column claim`
- Source line or section hint: `lines 3711-3713`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `protoform_vs_proto`; `cognate_set_scope`; `project_history`; `stale_row_policy`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This short coda needs to stay visible because it mixes one still-useful warning with one no-longer-current row statement. The useful part is its reminder that German `Galle` is feminine and that the other rows in cognate set 205 continue to reflect `*gallą`, so the OE weak noun should not automatically force the whole set into the same declension class [DEV_NOTES:line-3711-3712]. The stale part is the final clause claiming that the OE row now has `*gallô` in both `PROTOFORM` and `PROTO` columns [DEV_NOTES:line-3712-3713]. The live TSV now keeps the more informative split `PROTO = *gállą`, `PROTOFORM = *gállô`, so this fragment should be cited only as project chronology and as a warning against collapsing cognate-set headword and row-specific derivational input [Germanic/data/germanic-aligned-final.tsv:415; Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md:17-22,53-60].

## Superseded or diagnostic material

No additional securely attachable row-specific DEV_NOTES authority survives beyond the `ġealla` note itself. The packet's high-confidence area says `_None_` for DEV_NOTES hits even though its supporting/background section does preserve the relevant line cluster, so later workflow should rely on the explicit line-based fragment refs above rather than on the packet's summary label [Germanic/docs/lexeme_reports/packets/2037-gall-ġealla.md:43-49,55-117].

The packet's only non-DEV_NOTES background item is a table line from `analysis/arestoration_r_l_research.md` saying merely `| 2037 | *gállô | ġealla | geminate *ll* + breaking |` [Germanic/docs/lexeme_reports/packets/2037-gall-ġealla.md:141-150]. That is useful as phonological context, but it is not evidence for the crucial stem-class correction and should not be allowed to outrank the dedicated DEV_NOTES note or the live TSV row.

The memo's most useful diagnostic warning is likewise about project hygiene, not new row substance: it explicitly marks DEV_NOTES `line-3711-3713` as stale where it claims both columns changed, and it also warns that older diagnostic shorthand elsewhere in the repo can still say `*gallą -> ġealla` even though the live comparator cleanly distinguishes the incorrect strong input from the correct weak one [Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md:17-22,43-49,83-104]. Later report writers should preserve that warning so the row does not get flattened back into a one-column proto label.

## Open questions for later work

- Decide whether the eventual final report should quote Kroonen directly alongside the carried-over DEV_NOTES quotation `"ġealla, an; m."`, so the weak-masculine correction is documented from both the etymological and the OE lexical side.
- Decide whether the row's live `NOTE` field should eventually state the same three-way distinction now made explicit here: cognate-set `PROTO = *gállą`, OE-facing `PROTOFORM = *gállô`, target `ġealla`.
- If the final report mentions dialect background, decide how much memo-only evidence about Anglian `galla` belongs in the row narrative without blurring the fact that the current counterpart remains West-Saxon-style `ġealla` [Germanic/docs/lexeme_reports/research_memos/2037-gall-ġealla.md:47-49,65-69].
