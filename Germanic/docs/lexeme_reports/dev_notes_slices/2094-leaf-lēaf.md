---
row_id: 2094
concept: leaf
counterpart: lēaf
proto: *láubą
protoform: *láubą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/lexeme_reports/coverage_audit.md
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report.txt
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2094 leaf / lēaf

## Current row state

- CONCEPT: `leaf`
- COUNTERPART / target OE form: `lēaf`
- PROTO: `*láubą`
- PROTOFORM: `*láubą`
- DERIVATION_CLASS: `regular`
- Live TSV row 2094 currently keeps `PROTO = *láubą`, `PROTOFORM = *láubą`, and `COUNTERPART = lēaf`; the source fields are generic Wiktionary provenance lines, not a row-local explanatory note, so the row does not already carry embedded argumentation in the table itself [Germanic/data/germanic-aligned-final.tsv:636-636].
- `coverage_audit.md` marks row 2094 as uncovered infrastructure: `regular`, packet `no`, memo `-`, attached fragment `-`, overall `none` [Germanic/docs/lexeme_reports/coverage_audit.md:288-288].
- No row-specific `oe_known_problems.tsv` entry is present in the current ledger; the file only lists other exception buckets such as `*fūri` and `*táppô`, which is consistent with row 2094 remaining a regular success case rather than a known mismatch [Germanic/data/oe_known_problems.tsv:1-8].
- `report_manifest.tsv` likewise has no `2094 / leaf / lēaf` entry in the current pilot manifest; the manifest currently enumerates only a small pilot set and does not include this row [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- The published derivation snapshot already matches the live target without repair: `# leaf / PROTO: *láubą / EXPECTED: lēaf / OUTPUTS: lēaf`, with the compact OE-side sequence `OE Au Fronting: *láeubą`, `OE Diphthong Leveling: *lēabą`, `OE Heavy Syllable Nasal Apocope: *lēab`, `PGmc B Allophony: *lēaβ`, then surface `lēaf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2679-2698].
- The full trace confirms that nothing exotic is happening around this row: `NWGmcULowering`, `OEIUmlaut`, and the later cleanup rules are all `[no-change]` for `*láubą`; the successful derivation is the ordinary `*au > *aeu > ēa` path plus expected tail loss and `b > β > f` surface behavior [Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17867-17980].

## Development-note summary

No row-specific DEV_NOTES block for `leaf / lēaf / *láubą` survives in the live `DEV_NOTES.md`. The only direct `leaf` mentions recovered are (i) a **shared-background** example inside a different row's discussion of PGmc `*au`, and (ii) a **diagnostic** regression reminder about hypothetical `*laub-iz` under `i`-umlaut. That means this replacement slice must say plainly that there is no preserved lexeme-local controversy or repair history for row 2094 itself; the safe replacement note is built from shared sound-law material plus the current successful trace state, not from a lost row dossier [Germanic/docs/DEV_NOTES.md:34305-34318,34757-34760].

The durable phonological support is straightforward. DEV_NOTES explicitly uses `leaf` as an example of the regular OE treatment of PGmc `*au` before consonants: "`*laub-az → OE lēaf 'leaf' (WS, Anglian).`" In context, that sentence belongs to a general statement that PGmc `*au` undergoes fronting and leveling to OE `ēa` across OE dialects. That shared claim aligns exactly with the current row, where `PROTO` and `PROTOFORM` are both `*láubą` and the current derivation trace indeed shows `OEAuFronting` followed by `OEDiphthongLeveling` before the expected loss of final nasalized `*-ą` material and `b`-allophony [Germanic/docs/DEV_NOTES.md:34307-34318; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2688-2698; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17912-17932].

The same DEV_NOTES section also preserves `i`-umlaut material, but for this row that material is only **shared-background** or **diagnostic**, not direct row authority. The discussion says, for other lexemes with an `i/j` trigger, that West Saxon has "`The i-umlaut of ēa in West Saxon is īe`" and Anglian monophthongizes `ēa` to `ē` before `i/j` [Germanic/docs/DEV_NOTES.md:34322-34330]. That matters only if someone later investigates an inflected or derived `leaf`-family form such as the regression shorthand `*laub-iz`; it does **not** describe current row 2094, because row 2094's active `PROTOFORM` is bare `*láubą`, not an `*-i/-j` form, and the full trace explicitly shows `OEIUmlaut [no-change]` [Germanic/docs/DEV_NOTES.md:34757-34760; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17937-17939].

So the conservative working conclusion is simple: current support for row 2094 is real but thin and mostly shared. `PROTO` and `PROTOFORM` coincide as `*láubą`; the attested/target OE form is `lēaf`; the current FST path already derives that form regularly; and nothing in live DEV_NOTES promotes this row into an exception, alternate-protoform case, or unresolved methodological problem [Germanic/data/germanic-aligned-final.tsv:636-636; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2679-2698].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-34305-34318

- Source heading: `§17.22.3  Vowel discrepancy: īe (WS) vs. ē (Anglian) as i-umlaut of *au`; specifically `§17.22.3.1  The sound-change pathway: *au → ēa → īe (WS) or ē (Anglian)`
- Source line or section hint: `lines 34305-34318`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `shared_background_only`
- Issue tags: `inherited_au_to_ea`; `shared_sound_change`; `regular_reflex`; `no_row_specific_block`
- Recommended next use: `cite_as_shared_background_only`
- Shared with row IDs:

This is the strongest surviving DEV_NOTES support for row 2094 even though the section is not about `leaf` as its main subject. DEV_NOTES lays out the shared rule that PGmc `*au` in OE becomes fronted and then leveled to `ēa`, and it preserves `leaf` as one of the explicit examples: "`*haub-udą → OE hēafod 'head' (WS, Anglian)` ... `*raup-az → OE rēad 'red' (WS, Anglian)` ... `*laub-az → OE lēaf 'leaf' (WS, Anglian)`" [Germanic/docs/DEV_NOTES.md:34309-34318]. For row 2094, the usable substance is narrow but solid: the DEV_NOTES file itself treats `lēaf` as a regular OE reflex of inherited `*au`, not as a lexeme needing analogical rescue or a special counterexample. This fragment therefore supports only the vowel history and regular classification; it does not supply any row-specific morphology beyond that shared phonological point.

### DEV_NOTES:line-34322-34342

- Source heading: `§17.22.3.1  The sound-change pathway: *au → ēa → īe (WS) or ē (Anglian)`; `§17.22.3.2  Why does the FST produce WS īe instead of Anglian ē?`
- Source line or section hint: `lines 34322-34342`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `shared_background_only_or_diagnostic`
- Issue tags: `i_umlaut_of_ea`; `dialect_split`; `family_background`; `not_current_protoform`
- Recommended next use: `use_only_for_i_trigger_family_forms`
- Shared with row IDs:

This fragment is relevant only with a strict warning label. DEV_NOTES states: "`The i-umlaut of ēa in West Saxon is īe`" and, for Anglian, "`In Anglian the diphthong ēa is monophthongized to ē before i/j.`" It then works through a different lexeme where the trigger is present and explicitly distinguishes WS `īe` from Anglian `ē` [Germanic/docs/DEV_NOTES.md:34322-34342]. For row 2094, that is **not** direct evidence about the live row form `*láubą > lēaf`, because the current row has no following `i/j` trigger at all. Its only value here is to preserve the family-level distinction that a hypothetical `*laub-iz`-type form would belong to a different branch of the phonology than the current row's simple noun reflex.

### DEV_NOTES:line-34757-34760

- Source heading: `§17.22.9  Options for resolution`; `Option A: Target Anglian rēc, add Anglian i-umlaut rule to FST`
- Source line or section hint: `lines 34757-34760`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic`
- Issue tags: `regression_check`; `au_plus_i_umlaut`; `cross_row_warning`; `not_row_specific`
- Recommended next use: `use_only_when_touching_i_umlaut_rules`
- Shared with row IDs:

This fragment must be kept, but only as a diagnostic guardrail. DEV_NOTES warns: "`Regressions: Check ALL *au + i-umlaut lexemes (e.g., *haubi-dą → head, *laub-iz → leaf) to ensure Anglian rule applies consistently.`" [Germanic/docs/DEV_NOTES.md:34757-34760]. That wording does **not** convert current row 2094 into an `i`-umlaut case. Instead it shows that the project once used `leaf` as shorthand for a related family member with an `i`-trigger. For the present slice, the important substance is the distinction itself: current row `PROTOFORM = *láubą` remains the regular non-umlauted noun path to `lēaf`, while `*laub-iz` belongs to a separate, merely diagnostic branch that would matter only if the `ēa`-umlaut machinery were revised.

## Superseded or diagnostic material

- No surviving row-specific DEV_NOTES block for `2094 leaf / lēaf` was located. That absence should be stated explicitly rather than filled with invented project history: what survives is shared-background material plus a later regression warning, not a dedicated leaf note [Germanic/docs/DEV_NOTES.md:34305-34318,34757-34760].
- The `*laub-iz → leaf` regression shorthand is potentially misleading if detached from its context. It is **diagnostic family material**, not the live row's `PROTO` or `PROTOFORM`, and it should not be cited as though row 2094 itself had an `i`-umlaut trigger [Germanic/docs/DEV_NOTES.md:34757-34760].
- The trace reports are essential current diagnostics but they are not DEV_NOTES fragments. Their role here is to confirm that the row already succeeds regularly and that `OEIUmlaut` is inactive for the live form `*láubą` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2679-2698; Germanic/docs/debug_snapshots/oe_full_trace_report.txt:17897-17939].
- `coverage_audit.md`, `oe_known_problems.tsv`, and `report_manifest.tsv` are likewise status diagnostics, not philological argument. Taken together they confirm the row's present repo status: uncovered by packet/memo infrastructure, unlisted in the exception ledger, and absent from the pilot manifest because it has not needed special handling [Germanic/docs/lexeme_reports/coverage_audit.md:288-288; Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].

## Open questions for later work

- If later indexing work wants row 2094 represented beyond this slice, decide whether the surviving support is sufficient as-is: at present it is mostly shared `*au > ēa` material plus a clean successful trace, not a lexeme-local DEV_NOTES dossier.
- If future phonology changes touch `ēa` plus `i/j` behavior, keep `*láubą > lēaf` and any separate `*laub-iz`-type family probes sharply distinct; the current row is a non-umlauted noun reflex and should not inherit diagnostics from the `i`-umlaut branch by accident.
- If later bibliography work turns up a genuine lexeme-specific discussion of PGmc `*lauba-/*laubą` and OE `lēaf`, add it explicitly. Until then, the conservative row policy should remain: `PROTO = PROTOFORM = *láubą`, target `lēaf`, derivation class `regular`, no known problem entry.
