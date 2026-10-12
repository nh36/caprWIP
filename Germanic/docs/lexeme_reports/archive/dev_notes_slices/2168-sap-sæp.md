---
row_id: 2168
concept: sap
counterpart: sæp
proto: *sapōn
protoform: *sápą
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2168-sap-sæp.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2168-sap-sæp.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2168 sap / sæp

## Current row state

- CONCEPT: `sap`; COUNTERPART: `sæp`; PROTO: `*sapōn`; PROTOFORM: `*sápą`; DERIVATION_CLASS: `early_analogy` [Germanic/data/germanic-aligned-final.tsv:923-923].
- The live row note already encodes the present project reading: `OE neut. a-stem (Hall, K-S); Kroonen: n-stem *safō dissolved dialectally` [Germanic/data/germanic-aligned-final.tsv:923-923].
- `oe_known_problems.tsv` has no entry for row `2168`, `sap`, `sæp`, `*sapōn`, or `*sápą`; the row is therefore not being tracked as a live unresolved OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- Repo-local OE lexical confirmation exists independently of DEV_NOTES: `old_english_wiktionary.tsv` has `sap\tsæp\tinh\ttemplate:inh\tsap` [Germanic/data/old_english_wiktionary.tsv:229-229].

## Development-note summary

The current row already reflects the main substantive conclusion of the later `DEV_NOTES.md` work, but the file history has to be read carefully. The live TSV now keeps `PROTO = *sapōn` while using `PROTOFORM = *sápą` for the actual OE-directed derivation [Germanic/data/germanic-aligned-final.tsv:923-923]. That split is the heart of the row. The comparative headword `*sapōn` is still retained for the broader cognate set, but DEV_NOTES' later row discussion argues that this inherited stem shape is not the right direct input for deriving OE `sæp`; the live `PROTOFORM` has already been adjusted to the strong-neuter a-stem solution that gives the attested OE outcome [Germanic/docs/DEV_NOTES.md:11912-12052; Germanic/data/germanic-aligned-final.tsv:923-923].

The dedicated current DEV_NOTES section is `### The Etymology of OE sæp 'sap'` [Germanic/docs/DEV_NOTES.md:11910-12060]. Its starting point is the mismatch `*sapōn -> sape` against target `sæp`, diagnosed as a stem-class problem: DEV_NOTES says that the then-current proto input `*sapōn` was a weak/n-stem style form, while OE `sæp` is a neuter noun and therefore should not be modelled as the direct continuation of that weak stem shape [Germanic/docs/DEV_NOTES.md:11912-11918]. The section then collects the comparative source base in a way that still matters for row 2168. Kroonen is quoted for the broader inherited history and, crucially, for the sentence that the coexistence of several Germanic stem types points to `dialectal dissolution of a primary n-stem *safō, gen. *sappaz` [Germanic/docs/DEV_NOTES.md:11924-11937]. Kluge-Seebold is quoted as reconstructing WGmc `*sapi-` while still explicitly calling OE `sæp` neuter (`ae. sæp n.`) [Germanic/docs/DEV_NOTES.md:11939-11947]. Orel is cited for the broader `*sapōn ~ *sapan` comparative set [Germanic/docs/DEV_NOTES.md:11949-11953]. Hall gives the most direct OE lexical authority in the section: `sæp (e) n. 'sap,' juice` [Germanic/docs/DEV_NOTES.md:11955-11959]. Read together, those citations support a conservative current statement: the inherited comparative history is mixed, but the OE target to be modelled is neuter `sæp`.

The phonological argument in the same DEV_NOTES section is the decisive reason the live row now uses `PROTOFORM = *sápą`. DEV_NOTES tests two rival direct inputs. First, inherited `*sapōn` yields `sape`, so it fails to produce both the apocopated shape and the fronted root vowel required by `sæp` [Germanic/docs/DEV_NOTES.md:12018-12022]. Second, the tempting i-stem comparator `*sapiz` fails even more instructively: DEV_NOTES shows `*sapiz -> *sæpiz -> *sepiz -> sepe`, and explains that Campbell §193 makes that result expected because i-mutation of `æ` gives `e` [Germanic/docs/DEV_NOTES.md:11991-12008]. The section's key inference is therefore sound and should be preserved explicitly in this slice: if the OE target is `sæp` rather than `sep`, the direct OE-facing proto input must not contain an i-umlaut trigger. That is why DEV_NOTES recommends neuter a-stem `*sapą`, and why the live row now encodes that solution as accented `*sápą` in `PROTOFORM` while leaving the comparative `PROTO` untouched [Germanic/docs/DEV_NOTES.md:11988-12008,12026-12052; Germanic/data/germanic-aligned-final.tsv:923-923].

Earlier DEV_NOTES prose must not be mistaken for current row authority. An older bucket note near line 3856 says the expected form `sæp` is itself problematic and instead points to OE `*sāpe` as the correct outcome of `*sapōn` [Germanic/docs/DEV_NOTES.md:3851-3860]. That is now stale project history, not the live row policy. Likewise, the closing `TSV Change (pending approval)` lines in the later sap section still speak as if the row were moving from `PROTOFORM = *sapiz` to `*sapą` [Germanic/docs/DEV_NOTES.md:12056-12060]. The live TSV shows that this change has already effectively been absorbed in a slightly different final form: `PROTO` remains `*sapōn`, while `PROTOFORM` is now `*sápą` [Germanic/data/germanic-aligned-final.tsv:923-923]. For replacement-note purposes, that means the row should be read as solved by a `PROTO`/`PROTOFORM` split, not as still awaiting a one-column replacement.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-11924-11979

- Source heading: `The Etymology of OE sæp 'sap'` / `Scholarly Sources on the Etymology` / `Analysis of the Stem Classes`
- Source line or section hint: `lines 11924-11979`
- fragment_type: `bibliography_or_source_audit_for_lexeme`
- current_status: `current`
- Issue tags: `source_audit`; `oe_neuter`; `reconstruction_disagreement`; `stem_class`; `comparative_background`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the current source-audit fragment that should anchor any final report prose. It preserves the quotations that matter most for row 2168: Kroonen's broader comparative entry and his statement about `dialectal dissolution of a primary n-stem *safō`; Kluge-Seebold's `*sapi-` reconstruction alongside `ae. sæp n.`; Orel's broader `*sapōn ~ *sapan`; and Hall's direct OE dictionary entry `sæp (e) n. 'sap,' juice` [Germanic/docs/DEV_NOTES.md:11924-11959]. The fragment does not dissolve source disagreement, and the slice should not pretend that it does. What it securely establishes is narrower and more useful: OE `sæp` is being treated here as a neuter noun, while comparative dictionaries preserve evidence for multiple earlier stem formations behind the Germanic set [Germanic/docs/DEV_NOTES.md:11968-11979].

### DEV_NOTES:line-11983-12052

- Source heading: `The Etymology of OE sæp 'sap'` / `Phonological Development` / `Scholarly Support for the Neuter a-stem *sapą`
- Source line or section hint: `lines 11983-12052`
- fragment_type: `lexeme_specific`
- current_status: `current`
- Issue tags: `protoform_vs_proto`; `i_umlaut`; `AFB`; `stem_class`; `early_analogy`; `row_policy`
- recommended_next_use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling derivational fragment. DEV_NOTES lays out the two main comparator paths explicitly: `*sapą -> sæp` works through Anglo-Frisian Brightening plus apocope, while `*sapiz` fails because the fronted vowel is then raised by i-umlaut to `e` [Germanic/docs/DEV_NOTES.md:11985-12008]. The FST summary table makes the row policy concrete: `*sapōn | sape | sæp | ✗ wrong stem class`; `*sapiz | sepe | sæp | ✗ i-umlaut raises æ→e`; `*sapą | sæp | sæp | ✓` [Germanic/docs/DEV_NOTES.md:12018-12022]. For row 2168 this fragment establishes the exact reason the project now needs two proto levels: comparative `PROTO *sapōn` can remain as background, but the OE-facing `PROTOFORM` must be the non-i-triggering a-stem input represented in the live row as `*sápą` [Germanic/data/germanic-aligned-final.tsv:923-923; Germanic/docs/DEV_NOTES.md:12026-12052].

### DEV_NOTES:line-3851-3860

- Source heading: `Case 3: *flaskō → *flaskōn (OE flasce 'flask, bottle')`
- Source line or section hint: `lines 3851-3860`
- fragment_type: `superseded_or_diagnostic_for_lexeme`
- current_status: `superseded`
- Issue tags: `project_history`; `old_target_superseded`; `vowel_length`; `weak_stem_misread`
- recommended_next_use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This older bucket note is important only because later readers are likely to encounter it and over-trust it. The table row records the mismatch `*sapōn | sæpe | sape | sæp`, and the prose then says that expected `sæp` is itself problematic because the correct OE form would supposedly be weak feminine `*sāpe` [Germanic/docs/DEV_NOTES.md:3851-3860]. That is no longer the row's governing analysis. Its value now is diagnostic: it shows an earlier stage when the project had not yet separated comparative inherited background from the OE-facing modelling input and had not yet stabilized the current neuter-`sæp` solution.

### DEV_NOTES:line-12056-12060

- Source heading: `The Etymology of OE sæp 'sap'` / `TSV Change (pending approval)`
- Source line or section hint: `lines 12056-12060`
- fragment_type: `superseded_or_diagnostic_for_lexeme`
- current_status: `superseded`
- Issue tags: `project_history`; `pending_change_resolved`; `protoform_vs_proto`; `row_state_stale`
- recommended_next_use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

These lines preserve the transition state between the dedicated sap note and the live TSV. The recommendation itself still points in the right direction—use a neuter a-stem input rather than an i-stem—but the bookkeeping is stale because it says `Current: PROTOFORM = *sapiz` and `Proposed: PROTOFORM = *sapą` [Germanic/docs/DEV_NOTES.md:12056-12060]. The live row is no longer in that state: it keeps `PROTO *sapōn` as comparative background and encodes `PROTOFORM *sápą` as the actual derivational input [Germanic/data/germanic-aligned-final.tsv:923-923]. This fragment should therefore be used only to explain the chronology of the fix, not to describe current data columns.

## Superseded or diagnostic material

- The main stale danger is the old `*sāpe` claim. It belongs to earlier mismatch-bucket history and should not be reused as if it overruled the later row-specific sap section or the live TSV [Germanic/docs/DEV_NOTES.md:3856-3860; Germanic/data/germanic-aligned-final.tsv:923-923].
- A second, subtler danger is flattening the current row into a one-column story. The live row does **not** simply replace inherited `*sapōn` with `*sápą`; it now distinguishes `PROTO` from `PROTOFORM`, keeping the former as comparative background and the latter as the OE-facing input [Germanic/data/germanic-aligned-final.tsv:923-923]. Any future prose that says only “the protoform is `*sapą`” without saying which column is meant will be incomplete for this row.
- Kluge-Seebold's `*sapi-` remains useful comparative evidence, but DEV_NOTES itself explains why it is not a viable direct derivational input here: once `*-i-` is present, the expected phonology leads to `sep/sepe`, not `sæp` [Germanic/docs/DEV_NOTES.md:11939-11947,11991-12008]. It should therefore be kept as background on stem-history disagreement, not as current row policy.

## Open questions for later work

- If a central report is drafted, keep the conclusion conservative: OE `sæp` is the secure neuter target, but the comparative prehistory remains mixed across Kroonen, Orel, and Kluge-Seebold; the live project solution is specifically an OE-facing `PROTOFORM` choice, not a claim that all comparative sources should be rewritten to `*sapą` [Germanic/docs/DEV_NOTES.md:11924-12052; Germanic/data/germanic-aligned-final.tsv:923-923].
- If `DEV_NOTES.md` is ever cleaned up, mark both the `*sāpe` passage at `3856-3860` and the stale `Current: PROTOFORM = *sapiz` bookkeeping at `12058-12060` more explicitly as historical, since both are now easy to misread against the live row [Germanic/docs/DEV_NOTES.md:3856-3860,12056-12060].
- If `Germanic/docs/lexeme_reports/dev_notes_slices/index.tsv` is updated later, index the row under the current source-audit fragment (`11924-11979`) and the current phonological/row-policy fragment (`11983-12052`), with the two shorter superseded fragments retained only for project-history lookup.
