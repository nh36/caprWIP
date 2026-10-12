---
row_id: 2213
concept: start
counterpart: styrtan
proto: *stúrtijaną
protoform: *stúrtijaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2213 start / styrtan

## Current row state

- The live OE row reads `2213 | start | styrtan | *stúrtijaną | *stúrtijaną | regular`; the row carries no row-local explanatory NOTE, only duplicated Wiktionary inheritance provenance in the source fields [Germanic/data/germanic-aligned-final.tsv:1098-1098].
- For the live row, `PROTO` and `PROTOFORM` are the same quantity-marked form `*stúrtijaną`, while the OE `COUNTERPART` is `styrtan`. That current row state must be kept distinct from older DEV_NOTES spellings `*sturtijăną` and the superseded intermediate proposal `*sturtjăną` [Germanic/data/germanic-aligned-final.tsv:1098-1098; DEV_NOTES:line-8552-8555; DEV_NOTES:line-8934-8934].
- `oe_known_problems.tsv` has no row-local exception entry for `*stúrtijaną` / `styrtan`, so the row is not currently being tracked as a known OE exception bucket [Germanic/data/oe_known_problems.tsv:1-9].
- Coverage infrastructure still treats the row as ordinary uncovered regular material with no packet, memo, or report linkage yet attached: `| 2213 | start | styrtan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:368-368].

## Detailed development-note summary

The controlling DEV_NOTES story for row `2213` is a reversal. The earliest March 2026 pass treated `*sturtijăną` as a notation mistake and as a practical `no_output` bug: the grammar did not yet accept `ij`, the row produced `+?`, and the recommended repair was to rewrite the form to `*sturtjăną` [DEV_NOTES:line-8370-8375; DEV_NOTES:line-8478-8560]. That is no longer current row policy. The later decision update explicitly rejects the `TSV: *sturtjăną` solution and keeps the heavy-stem class-I form with `-ij-`; in present TSV notation, the live row's `*stúrtijaną` is the same policy outcome in newer accent/quantity spelling rather than a new lexical decision [Germanic/data/germanic-aligned-final.tsv:1098-1098; DEV_NOTES:line-8763-8899; DEV_NOTES:line-8903-9044].

The substantive linguistic point preserved by DEV_NOTES is Sievers' Law plus later PWGmc syncope, not a special lexical exception. DEV_NOTES quotes Ringe and Taylor's Cowgill-style formulation that heavy-root presents exhibited `*-ī- ~ *-ija-`, and it applies that directly to `*sturt-`, explicitly calling the stem shape CVCC and therefore heavy [@RingeTaylor2014, pp. 69-71; DEV_NOTES:line-8593-8619]. It also preserves Kluge-Seebold's wording `Aus wg. *sturt-ija- Vsw. "stürzen", auch in ae. sturtan, afr. sterta`, which is the row's clearest lexeme-specific handbook anchor for the `-ija-` analysis [@KlugeSeebold2011, s.v. "stürzen"; DEV_NOTES:line-8497-8505]. On this reading, the older Orel form `*startjanan` is not treated as disproof of `-ij-`; DEV_NOTES interprets it as normalized dictionary notation that abstracts away from the Sievers alternation rather than as a demand to change the row's project input [@Orel2003, p. 372; DEV_NOTES:line-8621-8626].

The current project solution is therefore chronological, not ad hoc. DEV_NOTES' decision update says the project is using **PGmc input notation**, so heavy-stem class-I weak verbs are entered with `*-ijăną`; the later West Germanic development is handled by a separate regular rule, quoted from Ringe and Taylor as `the sequence *-CijV- was syncopated to *-CjV-` [@RingeTaylor2014, p. 157; DEV_NOTES:line-8767-8799]. That keeps the row regular: `PROTO = PROTOFORM = *stúrtijaną` as the project input, `COUNTERPART = styrtan` as the OE target, and no need to demote the row to exception status. The implementation log and source-attestation note both reinforce that this was not a one-row patch: `*sturtjăną -> *sturtijăną` is listed among the systematic heavy-stem updates, and `*sturtijăną` appears again in the heavy-stem attestation table beside the explanation that all such forms were updated to `-ijăną` under PGmc notation [DEV_NOTES:line-8911-8935; DEV_NOTES:line-8991-9044].

What later report work still needs to remember is that DEV_NOTES preserves two different kinds of history at once. The useful current material is the heavy-stem/Sievers/syncope argument and the explicit decision to keep `-ij-`. The obsolete material is the earlier interpretation of `*sturtijăną` as a malformed Wiktionary normalization that should be repaired to `*sturtjăną`. Both need to stay visible in the slice, because otherwise a later reader could rediscover the old `no_output` lines and mistake them for present policy. The replacement note should therefore state the contrast bluntly: current regular project input `*stúrtijaną`; superseded proposal `*sturtjăną`; OE target `styrtan` throughout [Germanic/data/germanic-aligned-final.tsv:1098-1098; DEV_NOTES:line-8478-8560; DEV_NOTES:line-8763-9044].

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-8564-8645

- Source heading: `Sievers' Law and Class I Weak Verb Infinitives: The *sturtijăną Question`
- Source line or section hint: `lines 8564-8645`
- Fragment type: `row_specific_background`
- Status: `current`
- Issue tags: `sievers_law`; `heavy_stem_class_i`; `kluge_quote`; `normalized_orel_notation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best row-specific background fragment that remains current. It preserves the core heavy-stem argument, quotes Ringe and Taylor on the light/heavy `*-j- ~ *-ij-` alternation, and applies that directly to `*sturt-` as a CVCC heavy stem. It also carries the direct Kluge-Seebold quotation `Aus wg. *sturt-ija- ... auch in ae. sturtan`, which later work should preserve rather than paraphrase away [@KlugeSeebold2011, s.v. "stürzen"; @RingeTaylor2014, pp. 69-71; DEV_NOTES:line-8593-8645]. The fragment's current force is analytical rather than implementation-specific: it explains why the row can legitimately stand behind a live `PROTOFORM` with `-ij-`, even though later notation normalization has turned DEV_NOTES `*sturtijăną` into live TSV `*stúrtijaną` [Germanic/data/germanic-aligned-final.tsv:1098-1098].

### DEV_NOTES:line-8647-8747

- Source heading: `Sievers' Law and Class I Weak Verb Infinitives: The *sturtijăną Question`
- Source line or section hint: `lines 8647-8747`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `pwgmc_normalization`; `old_rewrite`; `row_chronology`; `no_output_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment is the indispensable record of the abandoned solution path. It is where DEV_NOTES argued that the project was really modeling PWGmc-style inputs, concluded that `*sturtijăną` was inconsistent with forms like `*libjăną`, and recommended `*sturtjăną`; the subsection even ends with the struck-through summary that the change to `*sturtjăną` was correct before immediately marking that conclusion `SUPERSEDED` [DEV_NOTES:line-8661-8747]. Its value now is historical and diagnostic only. It explains why row `2213` first appeared in the no-output inventory and why older project discussion may still talk as if `*sturtjăną` were the preferred repair, but it must not be cited as current row policy after the PGmc-notation decision [DEV_NOTES:line-8370-8375; DEV_NOTES:line-8763-8773].

### DEV_NOTES:line-8763-8899

- Source heading: `DECISION UPDATE (2026-03-13): Adopting PGmc Input Notation`
- Source line or section hint: `lines 8763-8899`
- Fragment type: `row_policy`
- Status: `current`
- Issue tags: `pgmc_input_notation`; `sievers_syncope`; `regular_derivation`; `notation_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling current-policy fragment. DEV_NOTES explicitly chooses PGmc input notation, states that heavy-stem class-I weak verbs "need `*-ijăną`", and separates that decision from the later regular PWGmc sound change quoted from Ringe and Taylor: `the sequence *-CijV- was syncopated to *-CjV-` [@RingeTaylor2014, p. 157; DEV_NOTES:line-8767-8799]. For row `2213`, this is the note that turns the old `ij-cluster` complaint into a regular derivational story: the project keeps a PGmc-style heavy-stem input and derives the OE target through ordinary chronology rather than by rewriting the row to a later normalized form. In live-row terms, this fragment underwrites `*stúrtijaną -> styrtan` as current policy, not `*sturtjăną -> styrtan` [Germanic/data/germanic-aligned-final.tsv:1098-1098].

### DEV_NOTES:line-8903-9044

- Source heading: `Sievers' Law Implementation Status` / `Source Attestation of *-ijăną Forms`
- Source line or section hint: `lines 8903-9044`
- Fragment type: `implementation_and_source_audit`
- Status: `current`
- Issue tags: `systematic_update`; `row_specific_old_new_pair`; `heavy_stem_attestation`; `project_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This combined fragment is current because it records both the implementation consequence and the wider evidence base. The implementation table explicitly lists `*sturtjăną | *sturtijăną | Kluge-Seebold (as *sturt-ija-)`, so row `2213` is not an isolated exception but part of a systematic heavy-stem update [DEV_NOTES:line-8917-8935]. The attestation section then repeats `*sturtijăną` in the heavy-stem table and concludes that all such forms were updated to `-ijăną` because that is "etymologically correct according to R/T, Fulk, and Sievers' Law" [@RingeTaylor2014, pp. 156-157; @Fulk2018, §5.8; DEV_NOTES:line-8991-9044]. For the slice, this fragment matters because it shows that the current row spelling policy is deliberate, implemented, and source-backed even if DEV_NOTES itself still uses the older unaccented `*sturtijăną` notation.

## Superseded or diagnostic material

- The earliest no-output table is still worth retaining as diagnostics, but only with an explicit superseded label. It lists `*sturtijăną | styrtan | Unknown`, then later narrows that to `ij cluster not in grammar | TSV: *sturtjăną`; both statements belong to the pre-decision stage and should not be mistaken for current linguistic policy [DEV_NOTES:line-8292-8297; DEV_NOTES:line-8341-8375].
- The standalone `TSV Analysis: *sturtijăną` note at `DEV_NOTES:line-8478-8560` is likewise superseded as row policy. Its direct Kluge and Orel quotations remain useful, but its operational recommendation `FROM *sturtijăną / TO *sturtjăną` no longer matches the live row after the PGmc-input decision [@KlugeSeebold2011, s.v. "stürzen"; @Orel2003, pp. 372, 384; DEV_NOTES:line-8478-8560].
- The live row's quantity-marked spelling `*stúrtijaną` is newer than the DEV_NOTES notation. Later report work should treat DEV_NOTES `*sturtijăną` as an older notation stage for the same kept heavy-stem analysis, not as evidence that the current TSV ought to revert to the superseded unaccented or `-j-` spellings [Germanic/data/germanic-aligned-final.tsv:1098-1098; DEV_NOTES:line-8763-9044].

## Open questions for later work

- If `index.tsv` is updated later, decide whether to index this row under the current fragments `DEV_NOTES:line-8564-8645`, `DEV_NOTES:line-8763-8899`, and `DEV_NOTES:line-8903-9044`, with the explicit note that DEV_NOTES uses older `*sturtijăną` spelling while the live TSV now has `*stúrtijaną`.
- If a later packet or research memo is created, add a brief source audit on whether the comparative headword should stay framed primarily through Kluge-Seebold `*sturt-ija-`, Orel `*startjanan`, or a broader cognate-set discussion; the present slice preserves the notation decision but not a full lexical-etymology dossier.
- If future cleanup revisits March 2026 no-output diagnostics, keep the chronology explicit: row `2213` was not solved by lexical retargeting or by downgrading to exception status, but by replacing the old `*sturtjăną` rewrite with a PGmc-input-plus-syncope account.
