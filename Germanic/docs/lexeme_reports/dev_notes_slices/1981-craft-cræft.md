---
row_id: 1981
concept: craft
counterpart: cræft
proto: *kráftiz
protoform: *kráftaz
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1981-craft-cræft.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1981-craft-cræft.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1981 craft / cræft

## Current row state

- CONCEPT: `craft`
- COUNTERPART: `cræft`
- PROTO: `*kráftiz`
- PROTOFORM: `*kráftaz`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note (abridged): Kroonen gives `*kraftu-` as a u-stem and Orel gives `*kraftiz ~ *kraftuz`; OE `cræft` has `æ`, not `e`, so the row rejects a direct i-stem input and uses a-stem `*kraftăz` as the modelling form.
- `oe_known_problems.tsv`: no row-specific entry.
- `report_manifest.tsv`: `pilot/craft.md` is already tracked as `pilot`.

## Development-note summary

The durable row-level point in DEV_NOTES is not “Proto-Germanic was certainly an a-stem,” but the narrower modelling claim that the pre-OE input used in the English cascade cannot be the old citation-style i-stem. DEV_NOTES opens the case by pairing `cræft` with `stæf` and showing the concrete mismatch: `*kraftiz` yields predicted OE `creft`, while the attested target is `cræft` [DEV_NOTES:line-4689-4703]. The phonological reason is explicit and still current: a following `*-iz` would trigger i-umlaut and raise fronted `æ` to `e`, so any row that keeps `cræft` as the OE target has to avoid feeding the FST an i-stem input for the actual derivation [DEV_NOTES:line-4738-4758; @Orel2003, p. 220].

DEV_NOTES is also valuable because it preserves the comparative disagreement instead of hiding it. The note surveys Kroonen's u-stem `*kraftu-`, Orel's split `*kraftiz ~ *kraftuz`, and Kluge-Seebold's i-stem analysis with acknowledgement of parallel u-stem evidence, then adds Fulk's MHG `kraft beside krefte` as evidence that the paradigm was morphologically unstable rather than trivially uniform [DEV_NOTES:line-4705-4723; @Kroonen2013, p. 307; @Fulk2018, §4.7 n. 12]. That comparative uncertainty remains relevant, but the slice should not reuse DEV_NOTES' table as exact philological authority for which modern dictionary prints `craft` versus `cræft`: the packet and research memo treat that orthographic column as noisy. The secure takeaway is the stem-class disagreement itself, not the table's source-to-spelling assignment.

What survives as current policy is the three-way phonological comparison. DEV_NOTES argues that an i-stem `*kraftiz` predicts `creft`, a u-stem `*kraftuz` predicts `craft`, and only an a-stem-style modelling input `*kraftăz` predicts `cræft`, because Anglo-Frisian fronting gives root `æ`, while the fronted suffix vowel does not create either i-umlaut or a-restoration [DEV_NOTES:line-4734-4758]. The live row keeps that phonological lesson but expresses it more conservatively than the original DEV_NOTES update. DEV_NOTES wanted both `PROTOFORM` and `PROTO` rewritten to `*kraftăz`; the live TSV instead keeps `PROTO` `*kráftiz` as cognate-set shorthand while using `PROTOFORM` `*kráftaz` as the row-specific input. That separation is the current project decision and is exactly what the research memo recommends preserving.

The OE side is much firmer than the PGmc morphology. DEV_NOTES explicitly cites Campbell's `cræft` under OE `æ` from PGmc `*a`, Campbell's plural `cræftas`, and Luick's paired `stæf ... cræft` examples, all of which confirm that `cræft` with `æ` is real OE evidence rather than a normalization choice [DEV_NOTES:line-4785-4795; @Campbell1959, §§133, 160; @Luick1914, p. 176]. The same fragment also warns against back-projecting later English `craft` with `a` onto the OE row: DEV_NOTES treats the later `a` vocalism as subsequent English history, not as evidence against OE `cræft` [DEV_NOTES:line-4792-4795].

Later debugging chronology is worth preserving because it clarifies what kind of early-analogy case this is. An earlier OE diagnostic snapshot still had stale high-vowel outputs such as `crafti`, showing that the row once sat inside the broad “final `-i/-u` cleanup” problem when the old input still behaved like a high-vowel stem [DEV_NOTES:line-2426-2484]. After the row was rewritten to a-stem modelling input, a different regression briefly appeared: `kraftăz → craft (should be cræft)`. DEV_NOTES then rejected an overbroad A-restoration fix and recorded the reusable principle that `*kraft.ăz` fronts to `cræft` precisely because there is no coda nasal and no legitimate back-vowel trigger in the following syllable [DEV_NOTES:line-9525-9568; @RingeTaylor2014, p. 153]. That later debugging note is not lexical authority by itself, but it does preserve the best in-repo statement of why row 1981 belongs under `early_analogy` rather than under an OE-rule exception bucket.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-4689-4783

- Source heading: `stem-class disagreement and modelling choice for cræft / stæf`
- Source line or section hint: `lines 4689-4783`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `stem_class`; `protoform_vs_proto`; `early_analogy`; `i_umlaut`; `a_restoration`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2212`

This is the main surviving authority for row 1981. DEV_NOTES first states the mismatch plainly: old TSV `*kraftiz` produced `creft`, but the expected OE form is `cræft` [DEV_NOTES:line-4696-4703]. It then lays out the source disagreement — Kroonen u-stem, Orel i-stem or u-stem, Kluge-Seebold i-stem with parallel u-stem evidence, plus Fulk's `kraft / krefte` alternation — to show that the project is responding to a real comparative problem rather than a typo [DEV_NOTES:line-4705-4723; @Kroonen2013, p. 307; @Orel2003, p. 220; @Fulk2018, §4.7 n. 12]. The crucial phonological comparison follows immediately: `*kraftiz -> creft`, `*kraftuz -> craft`, `*kraftăz -> cræft` [DEV_NOTES:line-4738-4758]. What should be carried forward is the modelling consequence, not every detail of the original rewrite proposal: the row needs an a-stem-style pre-OE input to reach OE `cræft`, but the live TSV now preserves that as `PROTOFORM` while leaving `PROTO` as the comparative headword.

### DEV_NOTES:line-4785-4795

- Source heading: `OE attestation for cræft and warning against later English back-projection`
- Source line or section hint: `lines 4785-4795`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `oe_attestation`; `handbook_quote`; `oe_vowel`; `later_english_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2212`

This short attestation fragment should remain explicit in the slice because it is the cleanest DEV_NOTES witness that the OE target itself is not in doubt. Campbell is cited for `cræft` under OE `æ` from PGmc `*a` and for plural `cræftas`; Luick is cited for `stæf 'Stab', cræft 'Kraft'` as `æ` examples [DEV_NOTES:line-4789-4791; @Campbell1959, §§133, 160; @Luick1914, p. 176]. DEV_NOTES also notes Bülbring's `craft 'Kraft'`, but specifically labels that as later ME/ModE `a`, not as counterevidence to OE `cræft` [DEV_NOTES:line-4792-4795]. Later report writing should therefore keep the chronological contrast overt: OE `cræft` is the row target; later `craft` belongs to later English history.

### DEV_NOTES:line-4797-4804

- Source heading: `original row-1981 TSV rewrite instruction`
- Source line or section hint: `lines 4797-4804`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `row_update`; `protoform_vs_proto`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment matters because it records the original project action taken after the stem-class review. DEV_NOTES instructed the team to change both `PROTOFORM` and `PROTO` from `*kraftiz` to `*kraftăz` and rewrote the row note accordingly [DEV_NOTES:line-4799-4804]. That is no longer the exact live policy. The current row keeps the same phonological conclusion — use `*kráftaz` as the modelling input — but no longer lets that modelling input erase the comparative headword in `PROTO`. The fragment should therefore be retained as project chronology explaining where the current row note came from, while being labelled superseded for row-state purposes.

### DEV_NOTES:line-9525-9568

- Source heading: `rejected A-restoration broadening and the craft regression`
- Source line or section hint: `lines 9525-9568`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `debug_history`; `a_restoration`; `fronting`; `regression`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2212`

This later debugging fragment is not the source of the row's lexical decision, but it is still worth preserving because it records exactly what went wrong once the a-stem comparator was in play. DEV_NOTES logs the regression `kraftăz -> craft (should be cræft)` and then rejects the attempted global fix that would make all following `*ă` trigger A-restoration [DEV_NOTES:line-9525-9551]. The note quotes Ringe-Taylor's conditioning — unstressed `*a` is nasalized, and therefore not fronted, only when followed by a nasal in syllable coda — and uses `*kraft.ăz` as the noun counterexample: “no nasal → `a` NOT nasalized → fronts → `cræft`” [DEV_NOTES:line-9557-9568; @RingeTaylor2014, p. 153]. For row 1981 this fragment should be cited only as diagnostic history, but it preserves the best repo-local explanation of why the a-stem modelling input should front to `æ` rather than restoring to `a`.

## Superseded or diagnostic material

Two older project states need to stay visible but subordinate. First, the old high-vowel output `crafti` belongs to the pre-resolution stage where the row still behaved like a high-vowel stem and was caught in general final `-i/-u` cleanup work rather than in a settled lexical note [DEV_NOTES:line-2426-2484]. Second, the March 2026 DEV_NOTES rewrite correctly identified the need for an a-stem-style modelling input, but it overshot by recommending that `PROTO` itself be rewritten to `*kraftăz` [DEV_NOTES:line-4797-4804]. The current slice should preserve both pieces of chronology while keeping the live distinction firm: `PROTO` remains comparative `*kráftiz`; `PROTOFORM` is modelling `*kráftaz`.

The other caution is source hygiene. DEV_NOTES is dependable on the main phonological contrast i-stem `e` / u-stem `a` / a-stem `æ`, but its literature table should not be recycled as if it were a perfect witness to which dictionary prints `craft` and which prints `cræft`. The packet and research memo already flag that orthographic column as noisy. Later report writing should therefore cite the dictionaries themselves for exact spellings and use DEV_NOTES mainly for the comparative disagreement and project chronology.

## Open questions for later work

- In the final lexeme report, decide how explicitly to explain that live `PROTO` and live `PROTOFORM` now deliberately diverge: comparative headword `*kráftiz` versus modelling input `*kráftaz`.
- Check whether the final report should quote Campbell's `cræft` / `cræftas` pair directly, since that is the cleanest handbook confirmation that OE `æ` is the relevant stage.
- If the final report discusses comparative morphology, keep the claim narrow: the row does not prove PGmc was “really” an a-stem, only that pre-OE modelling must avoid both i-stem umlaut and u-stem a-restoration.
- If exact source spellings from Kroonen, Orel, or Kluge-Seebold become central to the final report, verify them directly from the reference extracts rather than reusing the DEV_NOTES table uncorrected.
