---
row_id: 2195
concept: slay
counterpart: slēan
proto: *sláxaną
protoform: *sláxaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2195 slay / slēan

## Current row state

- The live aligned OE row reads `CONCEPT = slay`, `COUNTERPART = slēan`, `PROTO = *sláxaną`, `PROTOFORM = *sláxaną`, `DERIVATION_CLASS = regular`. The row carries no OE-facing project note beyond duplicated Wiktionary inheritance provenance [Germanic/data/germanic-aligned-final.tsv:1025-1028].
- `oe_known_problems.tsv` has no entry for row `2195`, `slēan`, or `*sláxaną`, so the row is not currently treated as an open OE exception [Germanic/data/oe_known_problems.tsv:1-8].
- Coverage infrastructure still marks the row as uncovered and unattached to any packet, memo, dossier, or report: `| 2195 | slay | slēan | regular | no | - | - | - | none |` [Germanic/docs/lexeme_reports/coverage_audit.md:357-357].
- The current published derivation already lands exactly on the target. The compact/published trace gives `PROTO: *sláxaną`, `EXPECTED: slēan`, `OUTPUTS: slēan`, and the OE-side path `Anglo Frisian Brightening: *slæxaną > OE Breaking: *sleaxaną > OE Heavy Syllable Nasal Apocope: *sleaxan > OE Secondary Nasalization: *sleaxąn > OE Weak Tail Reduction: *sleaxan > OE H Loss: *sleaan > OE Contraction: *slēan` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4326-4345].
- The full trace shows the same chronology in rule-by-rule form and confirms that nothing else interferes between breaking and contraction: after `AngloFrisianBrightening` and `OEBreaking`, the word passes unchanged through the umlaut/palatalization cluster, then `OEHLoss` gives `*sleaan` and `OEContraction` yields `*slēan`, followed by star removal only [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29352-29465].
- Comparative reference files support the lexeme family but preserve different citation conventions. Kroonen cites stem-level `*slahan- ... OE slēan`; Orel gives infinitival `*slaxanan ... OE sleán`; both are lexeme-level comparanda for the same verb, not rival OE targets [@kroonen2013, s.v. *slahan-; @orel2003, s.v. *slaxanan] [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23386-23389; docs/references/orel_handbook_germanic_etymology.vision.txt:38812-38815].

## Development-note summary

No dedicated `§17.xx` slay dossier survives in `DEV_NOTES.md`, and that absence should be stated plainly. What does survive is enough to reconstruct the row’s project history with some precision. Earlier January diagnostics still treated the verb as unresolved: the mismatch bucket listed `*slaxăną -> sleaan (expected slēan)` among the remaining “long-vowel missing” items, and a later rollback note still said that `slaxăną` remained in that bucket “for future work” [Germanic/docs/DEV_NOTES.md:1760-1774,2622-2624]. Current project state is different. By the later contraction audit, the same lexeme is no longer a live problem but a positive control: after dropping all nine obsolete breve-targeting `OEContraction` clauses, DEV_NOTES records `sláxăną -> slēan ✓` with “Zero regressions” [Germanic/docs/DEV_NOTES.md:21673-21686].

The row therefore needs three layers kept separate. The live **PROTO** and **PROTOFORM** are both the current project input string `*sláxaną`, while the OE target is the attested row headword `slēan` [Germanic/data/germanic-aligned-final.tsv:1027-1027]. The derivational stages `*slæxaną`, `*sleaxaną`, `*sleaxan`, `*sleaxąn`, `*sleaan`, and `*slēan` are chronological FST states inside the OE cascade, not competing row metadata [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:29410-29424,29445-29465]. The comparative dictionary forms `*slahan-` and `*slaxanan` are a third layer again: they are citation-form or notation-form variants for the same verb lexeme, not instructions to replace the row’s live OE-directed comparator [@kroonen2013, s.v. *slahan-; @orel2003, s.v. *slaxanan] [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23386-23389; docs/references/orel_handbook_germanic_etymology.vision.txt:38812-38815].

The notation differences inside project materials are also real, but they do not all mean the same thing. Earlier DEV_NOTES writes the input as `*slaxăną`; the live TSV writes `*sláxaną`. That difference is best read as **house-notation modernization**, not as a changed row policy: the later form adds the repo’s stress-marking acute and drops the older breve on the weak-tail vowel, while the lexical analysis remains the same [Germanic/docs/DEV_NOTES.md:1774-1774,21678-21678; Germanic/data/germanic-aligned-final.tsv:1027-1027]. By contrast, the difference between project `*sláxaną` and dictionary-style `*slahan-` / `*slaxanan` is partly notation and partly citation-form convention. DEV_NOTES explicitly notes elsewhere that some sources write the same inherited fricative as `h` where repo notation uses `x` [Germanic/docs/DEV_NOTES.md:42513-42515]. Kroonen’s trailing hyphen marks a stem citation; Orel writes the full infinitive; the repo uses the OE-directed comparator with final nasalized infinitive `-ą` and stress marking.

The most useful surviving explicit philological statement is preserved inside the later `tēon` dossier, where DEV_NOTES quotes Campbell on contraction after intervocalic `x/h` loss and gives the exact slay chain: `*slehan -> *sleahan -> *slean -> slēan` [@campbell1959, §238.2] [Germanic/docs/DEV_NOTES.md:42376-42379; docs/references/campbell_old_english_grammar.txt:7212-7218]. Brunner is even more explicit that Old English `slean` is “für *sleahan aus *slahan,” and he treats the broader contraction class with `feoh`, `sweor`, and `teoda/-teonti3` as regular products of the same process [@brunner1965, §§86, 129, 218.2] [docs/references/brunner_1965_altenglische_grammatik.txt:3010-3018,5484-5489]. DEV_NOTES then uses `sláxaną -> slēan` as the control case showing that the existing `*ea + *a -> *ēa` contraction clause already handles this lexeme correctly; the gap under discussion belongs to `*téxun -> tēon`, not to row `2195` [Germanic/docs/DEV_NOTES.md:42497-42500,42623-42629,42633-42638].

The conservative row-level conclusion is accordingly sharper than a generic “regular” label but still not a case for automatic index integration. Row `2195` is now a **solved regular derivation**. The older mismatch state is stale. The current row does **not** need a paradigm-cell replacement, does **not** belong in `oe_known_problems.tsv`, and does **not** require a different OE target than `slēan` [Germanic/docs/DEV_NOTES.md:21673-21686,42623-42629; Germanic/data/oe_known_problems.tsv:1-8]. What is missing is a dedicated slay-only DEV_NOTES argument block; the surviving evidence is a mix of one resolved old mismatch note, one current audit verification, and one later shared contraction discussion that uses `slēan` as an already-correct comparator. That makes the slice useful as a dossier, but still somewhat thin for indexing.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-21664-21686

- Source heading: `Audit of breve-targeting OEContraction clauses`
- Source line or section hint: `lines 21664-21686`
- Fragment type: `shared_row_verification`
- Status: `current`
- Issue tags: `contraction`; `resolved_mismatch`; `verification`; `breve_notation`
- Recommended next use: `cite_with_trace_if_reporting_current_status`
- Shared with row IDs: `2028`; `2058`; `2195`

This is the most important current fragment for the row because it records the post-fix state explicitly, not just inferentially. DEV_NOTES explains that all stressed cases already reach contraction as diphthong + weak-tail vowel before contraction, then reports the empirical test after deleting nine obsolete breve clauses. The row-specific verification line is unambiguous: `sláxăną  → slēan   ✓`, followed immediately by “Zero regressions” and the conclusion that “all 9 breve clauses are dead code at the current TSV state” [Germanic/docs/DEV_NOTES.md:21664-21686]. For row `2195`, this is the clearest statement that the live derivation now works for the right reason and does not depend on stale special-case contraction code.

### DEV_NOTES:line-42376-42429

- Source heading: `§17.48 — source audit for tēon`
- Source line or section hint: `lines 42376-42429`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `oe_contraction`; `campbell_quote`; `shared_source_authority`; `x_loss`
- Recommended next use: `cite_as_shared_phonology_background`
- Shared with row IDs: `1210`; `2058`; `2195`

This fragment is not a slay dossier, but it preserves the most explicit source-backed statement of the exact contraction pathway row `2195` uses. DEV_NOTES quotes Campbell §238.2 that contraction after intervocalic `x/h` loss yields long diphthongs and gives the slay example directly: `*slehan -> *sleahan -> *slean -> slēan` [@campbell1959, §238.2] [Germanic/docs/DEV_NOTES.md:42376-42379]. The same block then sets out the general problem in `*téxun`, showing that `*eo + *o` was missing from `OEContraction`, whereas `slēan` already belonged to the working `*ea + *a` type [Germanic/docs/DEV_NOTES.md:42398-42429]. For row `2195`, the fragment matters because it documents the phonological class and keeps the row out of the `tēon` repair scope.

### DEV_NOTES:line-42623-42638

- Source heading: `§17.48.1 C. The contraction rule itself / D. Risk audit`
- Source line or section hint: `lines 42623-42638`
- Fragment type: `shared_row_policy`
- Status: `current`
- Issue tags: `control_case`; `risk_audit`; `oe_contraction`; `not_a_live_problem`
- Recommended next use: `cite_if_asking_why_slēan_needs_no_fix`
- Shared with row IDs: `1210`; `2058`; `2195`

This later summary says in plain prose what the slay row now needs preserved. DEV_NOTES states that the contraction under discussion is “the same intervocalic *h-loss + contraction that the cascade already (correctly) handles for `*sláxaną -> slēan`, `*fehu -> fēo`, etc.” and then adds the lexicon audit result: among the relevant `*[ée]x` words, “`*sláxaną` uses the existing `*ea + a -> *ēa` rule” [Germanic/docs/DEV_NOTES.md:42623-42629,42633-42638]. That is not merely illustrative; it is the closest thing to a current row-policy sentence for `2195`. It confirms that the row is now an unaffected control case in the contraction system.

### DEV_NOTES:line-1760-1774 and DEV_NOTES:line-2622-2624

- Source heading: `Long-vowel-missing carryover diagnostics`
- Source line or section hint: `lines 1760-1774; 2622-2624`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `old_mismatch_bucket`; `notation_history`; `resolved_issue`
- Recommended next use: `preserve_as_project_history_only`
- Shared with row IDs:

These January notes are worth preserving precisely because they are no longer current. DEV_NOTES first says that after the 2026-01-10 rollback, diagnostics were back to baseline “with `slaxăną` still in the long-vowel bucket for future work,” and then lists the mismatch more explicitly as `*slaxăną -> sleaan (expected slēan)` [Germanic/docs/DEV_NOTES.md:1770-1774,2622-2624]. For row `2195`, the fragment documents the older failure mode and the older notation layer, but it should not be mistaken for live row policy now that later DEV_NOTES verification and current traces show exact output `slēan`.

## Superseded or diagnostic material

- The main stale material is the January mismatch state `*slaxăną -> sleaan (expected slēan)` [Germanic/docs/DEV_NOTES.md:2622-2624]. That note is historically useful because it records what used to be broken, but it is superseded by the later contraction audit and by the current published traces, both of which show exact output `slēan` [Germanic/docs/DEV_NOTES.md:21673-21686; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4326-4345].
- The older input spelling `*slaxăną` is best treated as a stale notation layer, not as a different lexical policy. Live row metadata uses `*sláxaną`; the later audit also uses stress-marked `*sláxăną`; and comparative dictionaries preserve still other citation styles such as `*slahan-` and `*slaxanan` [Germanic/data/germanic-aligned-final.tsv:1027-1027; Germanic/docs/DEV_NOTES.md:21678-21678,42513-42515; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23386-23389; docs/references/orel_handbook_germanic_etymology.vision.txt:38812-38815]. Those are notation/citation differences plus project chronology, not competing OE targets.
- The later `tēon` discussion should not be over-read as if row `2195` itself were under repair. Its value for this slice is that it preserves Campbell’s and Brunner’s contraction evidence and explicitly names `*sláxaną -> slēan` as an already-correct comparator [Germanic/docs/DEV_NOTES.md:42376-42379,42623-42638]. It is shared phonological background, not a slay-only design note.
- No row-local packet, memo, or problem-ticket exists at present [Germanic/docs/lexeme_reports/coverage_audit.md:357-357; Germanic/data/oe_known_problems.tsv:1-8]. That silence matters: the current need is accurate preservation of resolved project history and notation distinctions, not repair of an active derivational failure.

## Open questions for later work

- If `dev_notes_slices/index.tsv` is revisited, row `2195` should probably remain a no-index slice unless a dedicated slay-only memo or report is written. The present dossier is accurate and usable, but its DEV_NOTES authority is still mostly one current verification fragment plus shared contraction discussion rather than a row-specific analytical block.
- If later indexing standards do allow shared-current material, the safest anchors would be the current verification fragment (`21664-21686`) plus the shared contraction-policy lines (`42376-42429`, `42623-42638`), with the January mismatch notes kept explicitly diagnostic.
- If future reporting cites comparative reconstruction, keep the notation layers distinct: repo `*sláxaną` is the live OE-directed comparator; older internal `*slaxăną` is stale house notation; Kroonen’s `*slahan-` and Orel’s `*slaxanan` are dictionary citation forms for the same lexeme, not reasons to rewrite the OE target `slēan` [@kroonen2013, s.v. *slahan-; @orel2003, s.v. *slaxanan] [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:23386-23389; docs/references/orel_handbook_germanic_etymology.vision.txt:38812-38815].
