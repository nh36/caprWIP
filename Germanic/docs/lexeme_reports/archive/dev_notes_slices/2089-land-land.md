---
row_id: 2089
concept: land
counterpart: land
proto: *lándą
protoform: *lándą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
  - Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2089 land / land

## Current row state

- The live OE row is `2089`, with `CONCEPT = land`, `COUNTERPART = land`, `PROTO = *lándą`, `PROTOFORM = *lándą`, and `DERIVATION_CLASS = regular`; the row carries no row-local comment beyond duplicated imported provenance (`Source: Wiktionary etymology (template:inh)` twice) [Germanic/data/germanic-aligned-final.tsv:617-617].
- `old_english_wiktionary.tsv` independently maps `land` to OE `land` with the same inherited-source label, so the target is the ordinary attested OE noun rather than a repair surrogate or an analogical reporting form [Germanic/data/old_english_wiktionary.tsv:151-151].
- `oe_known_problems.tsv` has no entry for row `2089`, `land`, or `*lándą`; the row is not currently tracked as an OE exception, wontfix item, or unresolved mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage audit still lists row `2089` as uncovered, with no packet, memo, dossier, or requirement basis yet attached: `| 2089 | land | land | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:286-286].
- The current published derivation trace is fully successful: `PROTO: *lándą`, `EXPECTED: land`, `OUTPUTS: land`, with the only explicit OE-side step being `OE Heavy Syllable Nasal Apocope: *lánd`, followed by surface `Outcome: land` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2619-2638].
- Row-local project history is visible mainly through now-superseded diagnostics: the earlier apocope investigation still listed `*landą → lænda (exp. land)` among the heavy-stem `*-ą` failures, while the later experiment report lists `*landą → land ✓ (was: lænda)` as a successful repair after heavy-syllable `*-ą` apocope was added [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:148-150; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:289-289; Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md:24-33].

## Development-note summary

No dedicated `land / land` dossier survives in `DEV_NOTES.md`; there is no standalone row block explaining semantics, stem class, or a live mismatch. What survives is narrower and has to be classified carefully. One surviving DEV_NOTES thread is row-specific in content but shared in purpose: the 2026-03-11 audit of `*nd` rows explicitly includes `land | *landą | *lendh- "land" | original *dh | No`, i.e. this row was checked to confirm that its `d` is inherited and does **not** need a special `*ð` input or an `*nð` cluster analysis [Germanic/docs/DEV_NOTES.md:7538-7556].

The other surviving DEV_NOTES material is shared-background-only and mostly diagnostic. In the liquid/apocope investigation, `landu` appears not as a problem case but as a control proving that heavy short-vowel stems with two consonants were already apocopating correctly: `landu → land ✓ (heavy; correct apocope)` [Germanic/docs/DEV_NOTES.md:28953-28966]. The reasoning section then states the general conclusion in words that still apply directly to this row: “In environments with 2+ consonants, the apocope fires correctly regardless (word, land — short V + 2 C)” [Germanic/docs/DEV_NOTES.md:29143-29206]. A later probe table repeats the same control result, `*landu | land | land | HEAVY, no diphthong`, showing that `land` remained on the correct side of the fix rather than being one of the rows destabilized by it [Germanic/docs/DEV_NOTES.md:29459-29471].

Taken together, the surviving note stack supports a conservative reading of the live row. `PROTO` and `PROTOFORM` currently coincide as `*lándą`; the attested OE target is `land`; the live trace reaches that target directly; and DEV_NOTES uses the lexeme mainly to confirm two negative claims: no hidden Verner/`*ð` issue in the `nd` cluster, and no hidden apocope failure once heavy-syllable nasal apocope is in place [Germanic/data/germanic-aligned-final.tsv:617-617; Germanic/docs/DEV_NOTES.md:7538-7556; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2619-2638].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-7538-7556

- Source heading: `Systematic Check: TSV Forms with *nd Clusters (2026-03-11)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:7538-7556`
- Fragment type: `shared_audit_with_row_specific_entry`
- Status: `current`
- Issue tags: `nd_cluster`; `verner_check`; `consonant_etymology`; `proto_input_sanity`
- Recommended next use: `cite when explaining why this row keeps inherited d and does not need *ð or *nð rewriting`
- Shared-with rows if relevant: `bindan`, `windan`, `hund`, `hand`, `grund`, `sendan`, `funden`

This is the clearest surviving DEV_NOTES fragment that actually names the row. DEV_NOTES says the audit “Reviewed all TSV entries with `*nd` clusters to confirm none require `*nð`,” and the table entry for this lexeme is explicit: `| land | *landą | *lendh- "land" | original *dh | No |` [Germanic/docs/DEV_NOTES.md:7538-7550]. The point of the fragment is not to propose a new OE derivation, and not to argue for a row rewrite. Its job is narrower: it preserves that this row was checked against the project’s Verner/NSL concern and was found **not** to belong to the exceptional class.

That matters because the project does have at least one `*nd/*nð`-sensitive row (`funden`) in the same audit, so `land` is not just absent by accident; it was considered and ruled ordinary inside the exact diagnostic framework that was catching real exceptions elsewhere [Germanic/docs/DEV_NOTES.md:7538-7556]. The unaccented spelling `*landą` in the audit should be treated as shared-table notation rather than as a rival live-row reconstruction: the current aligned row still uses accented `PROTO/PROTOFORM *lándą`, and nothing in the audit suggests a different lexeme identity or a different OE target [Germanic/data/germanic-aligned-final.tsv:617-617; Germanic/docs/DEV_NOTES.md:7542-7550].

### DEV_NOTES:line-28953-28966-and-29143-29206

- Source heading: `§17.17 liquid-stem apocope investigation` / `§17.17.3 Phonological reasoning`
- Source line hint: `Germanic/docs/DEV_NOTES.md:28953-28966; 29143-29206`
- Fragment type: `shared_background_control`
- Status: `current_background_only`
- Issue tags: `high_vowel_apocope`; `stem_weight`; `heavy_syllable`; `control_case`
- Recommended next use: `cite when explaining that land is a positive control for heavy short-vowel + cluster apocope, not a problematic liquid-stem failure`
- Shared-with rows if relevant: `skipu/sċipu`, `gatu/ġetu`, `wordu/word`, plus the liquid-stem probe forms `speru`, `teru`, `smeru`, `faru`

This fragment is not a `land` dossier; it is a control setup inside a different bug investigation. DEV_NOTES first contrasts failing light liquid stems with a control table: `*skipu → sċipu`, `*gatu → ġetu`, `*wordu → word`, `*landu → land`, where `landu → land` is explicitly glossed “heavy; correct apocope” [Germanic/docs/DEV_NOTES.md:28953-28966]. The next paragraph sharpens the distinction: “The FST handles OE high-vowel apocope correctly for STOPS ... weight-conditioned as Campbell §345 prescribes. But after a /r/ (and by extension /l/, likely /n/, /m/), apocope fires even on light stems ...” [Germanic/docs/DEV_NOTES.md:28962-28966]. For row `2089`, the important point is negative but useful: `land` is cited on the **already-correct** side of the contrast.

The reasoning section then generalizes the same control result into a rule statement: heavy syllables are short vowel + `2+` consonants or any long nucleus, and therefore “In environments with 2+ consonants, the apocope fires correctly regardless (word, land — short V + 2 C)” [Germanic/docs/DEV_NOTES.md:29145-29206]. For this row, that sentence is the surviving DEV_NOTES explanation of why apocope is expected rather than surprising: `land` is a cluster-final heavy stem, so it is one of the rows that the weight rule already predicts correctly. This is shared-background-only support, but it is still the best surviving statement of the phonological rationale that fits the live trace’s `OE Heavy Syllable Nasal Apocope` step [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2626-2638].

### DEV_NOTES:line-29459-29471

- Source heading: post-fix probe table after the §17.17 apocope adjustment
- Source line hint: `Germanic/docs/DEV_NOTES.md:29459-29471`
- Fragment type: `shared_post_fix_verification`
- Status: `current`
- Issue tags: `regression_check`; `heavy_syllable`; `post_fix_probe`; `control_case`
- Recommended next use: `cite when documenting that land stayed correct after the apocope fix rather than being a collateral regression`
- Shared-with rows if relevant: `speoru`, `teoru`, `smeoru`, `heord`, `mearc`, `heall`, `heofon`, `feoh`, `sċipu`

This fragment is the late verification counterpart to the earlier control table. The probe results include `| *landu | land | land | HEAVY, no diphthong |` [Germanic/docs/DEV_NOTES.md:29459-29471]. In the same local context DEV_NOTES notes that several regressions “self-resolved,” but `land` is not listed among the regressions because it never moved off target in the post-fix probe set [Germanic/docs/DEV_NOTES.md:29473-29475].

For row `2089`, this fragment is useful as current verification, not as independent lexical analysis. It shows that after the project broadened the apocope handling to repair genuinely broken short-diphthong/light-stem cases, `land` still instantiated the expected heavy no-diphthong control outcome. That makes it a stability witness for the live row, not evidence of a surviving problem.

## Superseded or diagnostic material

- No row-specific `land / land` DEV_NOTES block survives beyond the shared audit/control material quoted above. If later indexing work looks for a standalone lexeme memo, it should say plainly that none survives rather than implying that the current slice was excerpted from a lost row dossier.
- The pre-fix apocope investigation outside DEV_NOTES is diagnostic history only: it listed `*landą → lænda (exp. land)` among the heavy-stem `*-ą` failures [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:289-289]. That is valuable for understanding why the row once needed infrastructure work, but it is superseded by the live trace and by the later experiment report.
- The experiment write-up is also diagnostic rather than controlling authority. It records `*landą → land ✓ (was: lænda)` and summarizes the broader infrastructure change as “All neuter *-ą cases with heavy stems now correctly lose the final vowel” [Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md:24-33]. Useful current-state confirmation, but not DEV_NOTES prose.
- The current debug trace is the best live derivational witness, but it should still be kept distinct from DEV_NOTES source material. Its role here is to confirm that the project now derives `land` directly by `OE Heavy Syllable Nasal Apocope`, not to replace the DEV_NOTES audit/control history [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2619-2638].

## Open questions for later work

- If this row is later indexed, decide whether the surviving material is sufficient for index inclusion. The row has real DEV_NOTES support, but it is shared audit/control support rather than a dedicated lexeme dossier.
- If later work revisits accent notation, keep the levels separate: live `PROTO` and `PROTOFORM` are both `*lándą` in the aligned TSV, while DEV_NOTES sometimes cites the same lexeme as unaccented `*landą` inside shared audit/control tables [Germanic/data/germanic-aligned-final.tsv:617-617; Germanic/docs/DEV_NOTES.md:7542-7550]. At present there is no evidence that these are competing reconstructions.
- If a future packet is created, it should preserve the older failed state (`*landą → lænda`) and the repaired state (`*landą → land`) together, because that pair explains why the row is now phonologically routine but still historically informative for the heavy-syllable `*-ą` apocope fix [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:289-289; Germanic/docs/germanic_notes/heavy_syllable_apocope_experiment_results.md:24-33].
