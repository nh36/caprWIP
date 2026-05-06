---
row_id: 2003
concept: fare
counterpart: faran
proto: *fáraną
protoform: *fáraną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2003-fare-faran.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2003-fare-faran.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2003 fare / faran

## Current row state

- CONCEPT: `fare`
- COUNTERPART: `faran`
- PROTO: `*fáraną`
- PROTOFORM: `*fáraną`
- DERIVATION_CLASS: `regular`
- Live TSV note: OE target `faran` (infinitive of the strong class-VI verb 'to fare, go'). The older target `færan` is now treated as a project mistake caused by conflation with umlauted present-tense forms such as `fær(e)þ` and with the separate weak causative `færan` 'to frighten', plus likely alignment to the pre-fix buggy FST output rather than to the attested infinitive.
- `oe_known_problems.tsv`: no row-local entry for `2003`, `*fáraną`, or `faran`.
- `report_manifest.tsv`: no manifest entry for this lexeme.

## Development-note summary

This row has securely attachable row-specific DEV_NOTES authority, and that authority is still current enough to replace repeated return visits to `DEV_NOTES.md`. The decisive material is the cluster at `DEV_NOTES:line-36757-36923`: first the A-restoration repair exposes row 2003 as a newly visible target-side mismatch, then the dedicated row note explains why the old target `færan` was wrong and why the live TSV correction to `faran` is the right one. The later generic chronology note at `DEV_NOTES:line-10668-10684` is useful supporting background, but it is not the source of the row correction itself.

The core philological point is simple and should stay explicit in later work: the row targets the **citation infinitive** of the strong class-VI verb, and that infinitive is `faran`, not `færan`. DEV_NOTES says the old note was internally inconsistent because it named the class-VI verb 'to fare, go' while giving the wrong infinitive. The only plausible OE forms with `æ` in this lexical neighborhood are either umlauted present-tense cells such as `fær(e)þ` / `færest` or the different weak verb `færan` 'to frighten'; neither can justify normalized row target `faran > færan` for the infinitive [DEV_NOTES:line-36856-36910; @SieversBrunner1965, §392; @ClarkHall1960, s.vv. "faran", "færan"; @BosworthToller1898, s.vv. "faran", "færan"].

The sound-change background also stays regular. DEV_NOTES' later chronology discussion preserves Fulk's wording that unstressed Anglo-Frisian `a` was nasalized only before a **tautosyllabic** nasal, "otherwise fronted to æ ... as in OE faran ... but with fronting ... in ... OE ... pp. faren- 'gone' < *faræn- < *faran-." That quotation is valuable because it explains why the infinitive can stay `faran` while participial or inflected material shows fronting: the infinitive's `n` is syllable-final in the relevant stage, but participial `n` is heterosyllabic [DEV_NOTES:line-10668-10684; @Fulk2018, §5.6, p. 92]. Campbell's A-restoration rule and the comparative handbooks cited in DEV_NOTES all point the same way: `*fáraną` is a regular inherited input and `faran` is the expected OE infinitive [DEV_NOTES:line-36880-36900; @Campbell1959, §158; @RingeTaylor2014, pp. 142, 153; @Kroonen2013; @Orel2003].

The project-history point that must not be lost is that the old target was probably **tuned to a buggy FST state**. Before the A-restoration conditioning fix, the grammar wrongly blocked restoration across single `*r`, so `*fáraną` surfaced as `færan`; once that rule was corrected, the FST moved to `faran` and the row became mismatched against its already-wrong target. DEV_NOTES treats that exact agreement between the buggy output and the old TSV target as the "smoking gun" for a target-tuned-to-buggy-FST anti-pattern, not as evidence that `færan` was ever a soundly supported infinitive [DEV_NOTES:line-36808-36854]. For normal workflow, row 2003 should therefore be treated as a **corrected regular row**, not as a known exception, paradigm-cell workaround, or unresolved literature dispute.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-36757-36804

- Source heading: `Post-fix verification after A-restoration repair exposed row 2003`
- Source line or section hint: `lines 36757-36804`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `a_restoration_fix`; `mismatch_exposure`; `target_side_issue`; `project_chronology`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2141, 2240`

This fragment is the best compact record of **how** row 2003 reappeared. DEV_NOTES logs the repaired outputs and explicitly lists ``*fáraną → faran`` as "etymologically correct" while the TSV still had `færan`, then explains that the apparent regression in mismatch count came from target-side problems newly exposed by the fix rather than from broken phonology. For this slice the fragment matters as chronology, not as live policy: it shows that row 2003 only became visible once A-restoration before single `*r` was repaired, and it ties the row to the same exposure pattern as `mare` and `tæppa`.

### DEV_NOTES:line-36808-36854

- Source heading: `Why the old target probably copied the buggy FST output`
- Source line or section hint: `lines 36808-36854`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `target_tuned_to_bug`; `old_target`; `methodological_warning`; `project_chronology`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2141, 2240`

This methodological note should be preserved because it explains the row's most important superseded detour. DEV_NOTES reconstructs the old buggy derivation step by step — A-fronting applied, A-restoration was wrongly blocked across single `*r`, and the resulting surface form was `færan` — then argues that the prior TSV target was likely set to that buggy output rather than to dictionary-backed OE evidence. The note's larger warning also survives: after every rule repair, newly exposed matches and mismatches should be checked for rows whose target may have been silently tuned to an earlier incorrect cascade state. Later writers should cite this fragment only when explaining project chronology or workflow risk, not when justifying the present row target.

### DEV_NOTES:line-36856-36910

- Source heading: `Row diagnosis: infinitive faran, not umlauted present forms or weak causative færan`
- Source line or section hint: `lines 36856-36910`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `target_correction`; `class_vi_infinitive`; `paradigm_cell_conflation`; `weak_causative_confusion`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the controlling row-policy fragment. It states plainly that the repaired FST now gives `*fáraną → faran`, that the old note was internally inconsistent, and that the likely visible conflations are with present-tense `fær(e)þ / færest` or with the separate weak verb `færan` 'to frighten'. It then sets out the handbook consensus in reusable form: Orel's cognate set, Kroonen's inherited strong-VI comparison, Campbell's use of `faran` as a textbook A-restoration example, Brunner's use of `faran` as the model class-VI verb, and the statement that there is no regular historical path to infinitival `færan` here [@Orel2003; @Kroonen2013; @Campbell1959, §158; @SieversBrunner1965, §§368, 392]. If a later lexeme report needs one DEV_NOTES fragment to justify the live row, it should start here.

### DEV_NOTES:line-36912-36923

- Source heading: `Exact TSV correction for row 2003`
- Source line or section hint: `lines 36912-36923`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `implemented_change`; `note_rewrite`; `row_edit_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This short implementation table is no longer needed to decide the row, because the live TSV already embodies the correction. It still deserves preservation as working-note history because it shows exactly what was changed together: `TOKENS` and `COUNTERPART` were rewritten from `færan` to `faran`, the note was rewritten to name the conflations explicitly, and `PROTO` / `PROTOFORM` were left unchanged. That last point is important: this row was fixed by **target correction**, not by inventing a new protoform or derivation class.

### DEV_NOTES:line-10668-10684

- Source heading: `Chronology note using faran and faren- to distinguish nasalization and fronting`
- Source line or section hint: `lines 10668-10684`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `tautosyllabic_vs_heterosyllabic_n`; `infinitive_vs_participle`; `literature_quote`; `chronology_background`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is useful supporting background rather than row-local correction history. It preserves the Fulk quotation in full: unstressed Anglo-Frisian `a` was nasalized before a nasal "but only a tautosyllabic one if the vowel was unstressed", "otherwise fronted to æ ... as in OE faran ... but with fronting ... in ... pp. faren- 'gone' < *faræn- < *faran-'." That wording is worth carrying over because it gives later writers a compact explanation for why `faran` is the right infinitive while `faren-` and umlauted present forms remain genuine comparators [@Fulk2018, §5.6, p. 92]. Use it as background if a final report needs to explain the paradigm contrast more fully.

## Superseded or diagnostic material

The superseded material here is not a competing philological analysis of the infinitive. What is superseded is the **old project state** in which `færan` appeared to be acceptable because the buggy cascade also returned `færan`. DEV_NOTES does preserve real nearby comparators with `æ` — present `fær(e)þ / færest`, participial `faren- < *faræn-`, and the separate weak causative `færan` — but those are diagnostic comparators, not surviving support for the row target. Later work should therefore resist any formulation like "DEV_NOTES once argued for `færan`." It did not preserve a durable row-local case for that infinitive; it preserved a record of a project mistake and its correction.

## Open questions for later work

- Decide whether the final lexeme report should quote a dictionary entry directly, alongside DEV_NOTES, when distinguishing strong `faran` from weak `færan`.
- If the final report wants a compact paradigm contrast table, the most useful cells are infinitive `faran`, 2sg/3sg present `færest / fær(e)þ`, and participial `faren-`; keep those explicitly labelled as different cells or lexemes, not as alternative infinitives.
- If later workflow audits the target-tuned-to-buggy-FST anti-pattern more broadly, row 2003 should be cited as the cleanest example of a row where the phonology was right and only the TSV target had drifted.
- When a manifest entry or full lexeme report is eventually created, preserve the distinction between comparative proto headword evidence and the unchanged row input `*fáraną`; this row does **not** need a protoform rethink.
