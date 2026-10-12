---
row_id: 2109
concept: loam
counterpart: lām
proto: *laimōn
protoform: *láimą
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2109-loam-lām.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2109 loam / lām

## Current row state

- CONCEPT: `loam`
- COUNTERPART: `lām`
- PROTO: `*laimōn`
- PROTOFORM: `*láimą`
- DERIVATION_CLASS: `early_analogy`
- Live TSV row `2109` already encodes the row's governing distinction: comparative/cognate-set `PROTO` remains `*laimōn`, but the OE-facing `PROTOFORM` is `*láimą`, with the note that Orel/Kroonen reconstruct an n-stem masculine for the wider cognate set while OE has class-shifted to a neuter strong noun; the row therefore keeps the cognate-set headword unchanged and aligns only the per-row protoform to the OE class [Germanic/data/germanic-aligned-final.tsv:694-694].
- Packet state is regular at the current row setting: `PROTO: *láimą`, `EXPECTED: lām`, `OUTPUTS: lām`, with the compact trace `*láimą > *lāmą > lām`; the packet also records no manifest entry and no `oe_known_problems.tsv` hit for this row [Germanic/docs/lexeme_reports/packets/2109-loam-lām.md:11-13,17-44].
- `oe_known_problems.tsv` has no entry for `2109`, `*laimōn`, `*láimą`, or `lām`; the file currently contains only unrelated rows such as `*búkkaz`, `*fúglaz`, `*wúlfaz`, `*wúllō`, `*rústō`, `*fūri`, and `*táppô` [Germanic/data/oe_known_problems.tsv:1-8].
- Memo state: the row is treated as resolved at the lexical-policy level. The memo says the authoritative current bundle is TSV + packet + DEV_NOTES §17.39 source audit; it also states the three-way distinction explicitly—cognate-set `PROTO *laimōn`, OE-targeted `PROTOFORM *láimą`, and OE target `lām`—and warns that older `lāme` / `lāfe` traces are project diagnostics rather than current lexical evidence [Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:14-22,38-58].
- Current DEV_NOTES authority status: **current row-specific DEV_NOTES authority does exist**. The controlling note is §17.39, which diagnoses the inherited `*láimōn` mismatch, audits the sources, and states the row plan `PROTOFORM *láimōn → *láimą`, `COUNTERPART` unchanged `lām` [DEV_NOTES:line-38726-38835].

## Development-note summary

Current row-specific DEV_NOTES authority **does exist**, and it is strong enough that the slice can stand in for returning to `DEV_NOTES.md` for row 2109. The core current decision is not a change to the cognate-set reconstruction but a row-local OE modelling choice: keep `PROTO = *laimōn` for the wider Germanic cognate set, keep `COUNTERPART = lām` as the attested OE lemma, and set `PROTOFORM = *láimą` because the OE reflex behaves as a neuter strong noun while the inherited comparative headword is an n-stem masculine [Germanic/data/germanic-aligned-final.tsv:694-694; DEV_NOTES:line-38815-38835; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:40-47,56-58].

DEV_NOTES §17.39 makes the philological basis explicit and should be treated as the row's current source hierarchy. The note quotes Orel `*laimōn sb.m.: OE neut. lám`, Kroonen `*laiman- m. 'clay' — OE lām n.`, Clark Hall `lām n.`, and Bosworth-Toller `lám, es; n.`; the note then states the consensus plainly: printed etymological sources keep the cognate set as an n-stem masculine, while the OE reflex is neuter strong [DEV_NOTES:line-38776-38812]. That means the row is **not** claiming that Proto-Germanic itself was an a-stem. Instead, the row models an early OE-side class shift by changing only the per-row `PROTOFORM` to `*láimą` [DEV_NOTES:line-38807-38821; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:42-47].

The engineering side must stay separate from that philology. Feeding inherited `*láimōn` straight into the cascade is currently wrong for this row: the older project history preserved `*laimōn | lāme | ... | lām`, and the explicit §17.39 mismatch note later shows `*láimōn → lāfe` with spurious medial `/β/` and final `-e` [DEV_NOTES:line-3853-3853; DEV_NOTES:line-38733-38771]. The FST probe matrix is decisive here: `*láimą → lām` works, `*láimō → lām` also works, and `*láimaz → lām` works only as a comparator; DEV_NOTES itself says the Wiktionary-style masculine a-stem is an outlier against the printed-dictionary consensus and should not be mistaken for the row's adopted historical analysis [DEV_NOTES:line-38743-38752,38790-38805; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:18-22,46-47,62-64].

For later use, three levels must stay distinct. `PROTO` is the comparative PGmc headword `*laimōn`; `PROTOFORM` is the OE-directed modelling input `*láimą`; and the OE target is the attested neuter lemma `lām`, supported both by dictionary citations in DEV_NOTES and by the local lexical-table hit `loam -> lām` [Germanic/data/old_english_wiktionary.tsv:171-171; DEV_NOTES:line-38776-38812]. The row is therefore about stem-class realignment, not about choosing among rival attested OE spellings and not about selecting a different paradigm cell [Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:48-64].

The separate §17.39.1 `*aim:ōn → ā:β:e` artifact note must be preserved but kept subordinate. It is a current diagnostic follow-up explaining why inherited `*láimōn` can misfire as `lāfe`/`cāfe`; it is **not** a reason to undo the present row policy, because the row already avoids that shape through the OE-specific `PROTOFORM *láimą` [DEV_NOTES:line-38837-38861; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:56-58,77-78]. The memo is right to treat the row itself as resolved while leaving the artifact as a separate cascade investigation.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-38726-38835

- Source heading: `§17.39 *láimōn → lāfe (expected lām): TSV proto stem-class mismatch + cascade artifact note`
- Source line or section hint: `lines 38726-38835`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `stem_class`; `protoform_vs_proto`; `early_class_shift`; `row_policy`; `target_stability`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current row note. DEV_NOTES records the observed inherited-input failure `*láimōn → lāfe`, then states the diagnosis as a TSV alignment issue: the row is using the comparative n-stem headword even though OE has “class-shifted directly to neuter a-stem (`*laimą` → `lām`)” and the cascade has no class-shift rule [DEV_NOTES:line-38733-38733,38815-38821]. The plan that follows is explicit and should be treated as binding row policy: `TSV row 2109 ... PROTOFORM *láimōn → *láimą ... COUNTERPART unchanged (lām) ... Cognate-set ... stays *laimōn` [DEV_NOTES:line-38825-38835]. This matches the live TSV row exactly and matches the packet's successful compact derivation `*láimą -> lām`, so the fragment is not merely historical drafting; it is the current row-local authority [Germanic/data/germanic-aligned-final.tsv:694-694; Germanic/docs/lexeme_reports/packets/2109-loam-lām.md:17-40].

### DEV_NOTES:line-38774-38812

- Source heading: `Source audit` plus `Field consensus`
- Source line or section hint: `lines 38774-38812`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `source_audit`; `printed_dictionary_consensus`; `oe_neuter`; `wiktionary_outlier`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment supplies the philological justification for the row policy and preserves the direct quotations worth reusing. Orel is quoted as `*laimōn sb.m.: OE neut. lám`; Kroonen as `*laiman- m. 'clay' — OE lām n.`; Clark Hall as `lām n.`; and Bosworth-Toller as `lám, es; n.` [DEV_NOTES:line-38776-38788]. DEV_NOTES then contrasts that printed-dictionary consensus with the Wiktionary `*laimaz` page and calls the latter “an outlier,” concluding that reliable sources support an n-stem comparative proto while the OE reflex is neuter strong [DEV_NOTES:line-38790-38812]. For row 2109 this matters because it blocks two common mistakes at once: rewriting `PROTO` itself as an a-stem, and treating successful comparator probe `*láimaz → lām` as if it were the main historical solution [Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:16-22,42-47].

### DEV_NOTES:line-39962-39969

- Source heading: `Project precedent`
- Source line or section hint: `lines 39962-39969`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `protoform_vs_proto`; `project_precedent`; `cross_gmc_headword`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2013; 2053; 2152; 2183`

This late summary is shared rather than loam-specific, but it remains current and directly names loam as one of the precedent rows. DEV_NOTES says the same move was applied for “loam (§17.39)” and describes that move as switching “the per-row PROTOFORM to the paradigm cell that yields the attested OE form by regular sound change, leaving the cognate-set headword intact for cross-Gmc inheritance” [DEV_NOTES:line-39964-39969]. Row 2109 fits that formulation exactly, except that here the row-local change is a stem-class realignment rather than a different inflectional cell: comparative `PROTO *laimōn` stays in place, OE-facing `PROTOFORM *láimą` is adjusted, and the attested OE target `lām` stays fixed [Germanic/data/germanic-aligned-final.tsv:694-694; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:56-58].

### DEV_NOTES:line-38837-38861

- Source heading: `§17.39.1 follow-up: cascade artifact for *aim:ōn → ā:β:e`
- Source line or section hint: `lines 38837-38861`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `cascade_artifact`; `proto_to_oe_bug`; `aim_ōn_shape`; `non_blocking_follow_up`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This fragment is current but diagnostic-only. DEV_NOTES isolates a separate artifact whereby any `*Cáim:ōn`-type input can rewrite medial `/m/` to `/β/` and shrink `ōn` to `e`, producing examples such as `*káimōn → cāfe`; the note explicitly says the mechanism needs separate inspection and that it is “not in scope for the present TSV row fix” [DEV_NOTES:line-38837-38857]. For row 2109 the fragment matters only as a guardrail: it explains why inherited `*láimōn` can misbehave in the current cascade, but it does not compete with the row's adopted solution `*láimą -> lām` and should not be cited as if the loam row were still unresolved [Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:56-58,77-78].

### DEV_NOTES:line-3853

- Source heading: `Case 3: *flaskō → *flaskōn (OE flasce 'flask, bottle')`
- Source line or section hint: `line 3853`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `pre_fix_output`; `old_trace`; `project_chronology`; `stale_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This old table row should be retained only as pre-fix chronology. It records `*laimōn | lāme | lāme | lām`, i.e. an earlier stage where inherited `*laimōn` still produced `lāme` rather than the later explicitly diagnosed `lāfe` artifact or the current row-local fix `*láimą -> lām` [DEV_NOTES:line-3853-3853]. The memo is explicit that archival `lāme` traces are stale evidence, useful only for reconstructing project history and showing that the loam problem predates the more detailed §17.39 source audit [Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:18-20,56-58,78-78].

## Superseded or diagnostic material

- The successful probe `*láimaz → lām` is **misleading if uncontextualized** for this row. DEV_NOTES keeps it in the probe matrix, but the same source-audit note says the Wiktionary masculine a-stem is an outlier against Orel/Kroonen and should not be treated as the row's adopted historical reconstruction [DEV_NOTES:line-38744-38748,38790-38805; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:18-22,46-47,62-64].
- Older `*láimōn -> lāme` and newer inherited-input `*láimōn -> lāfe` outputs are both project diagnostics, not live row targets. They document what happens when the inherited n-stem is sent through a cascade that lacks the OE class-shift step; they do **not** undermine the present row policy `PROTO *laimōn`, `PROTOFORM *láimą`, `COUNTERPART lām` [DEV_NOTES:line-3853-3853,38733-38771; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:20-22,54-58].
- The absence of a manifest entry or `oe_known_problems.tsv` row should be preserved as current-state bookkeeping only. It means the row is not currently being tracked as an unresolved OE exception; it is not independent philological evidence [Germanic/docs/lexeme_reports/packets/2109-loam-lām.md:11-13,42-44; Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If `dev_notes_slices/index.tsv` is updated later, record row 2109 as having **current row-specific DEV_NOTES authority**, one current source-audit fragment, one shared project-precedent fragment, one current diagnostic artifact note, and one superseded pre-fix trace.
- If final report prose mentions Wiktionary at all, keep the hierarchy explicit: it is a cited outlier comparator behind the packet history, not the basis for replacing cognate-set `PROTO *laimōn` or for claiming that masculine a-stem `*láimaz` is the row's chosen solution [DEV_NOTES:line-38790-38805].
- If the `*aim:ōn → ā:β:e` artifact is investigated later, keep the row-local conclusion unchanged unless new evidence shows that OE `lām` should be modelled by something other than the already successful `PROTOFORM *láimą`; current repo evidence does not point that way [DEV_NOTES:line-38837-38861; Germanic/docs/lexeme_reports/research_memos/2109-loam-lām.md:56-58,72-78].
