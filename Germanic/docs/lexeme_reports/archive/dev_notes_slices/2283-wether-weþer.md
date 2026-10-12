---
row_id: 2283
concept: wether
counterpart: weþer
proto: *wíθrą
protoform: *wíθrą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2283 wether / weþer

## Current row state

- The live TSV row reads `CONCEPT = wether`, `COUNTERPART = weþer`, `PROTO = *wíθrą`, `PROTOFORM = *wíθrą`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1371-1371].
- The source-note field still contains only the duplicated inherited placeholder `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`. That is not the actual documentary basis for the present row state [Germanic/data/germanic-aligned-final.tsv:1371-1371].
- No row-specific packet, research memo, pilot file, or other clearly row-addressed support file was found under `Germanic/docs/lexeme_reports/`; the coverage audit still records row 2283 as `none` [Germanic/docs/lexeme_reports/coverage_audit.md:409-409].
- The current published derivation snapshot already matches the live row exactly: `PROTO: *wíθrą`, `EXPECTED: weþer`, `OUTPUTS: weþer`, with the condensed development `NWGmc I Lowering: *wéθrą`, then `OE Heavy Syllable Nasal Apocope: *wéθr`, then `OE Epenthetic Vowel: *wéθer` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5781-5801].
- An older full-trace snapshot survives with the pre-correction proto input `*wiθră`; it still reaches `weþer`, but it is now diagnostic-only evidence for the superseded hacky input, not the current row definition [docs/debug_snapshots/oe_full_trace_report.txt:16063-16116].

## Detailed development-note summary

Unlike nearby `weather / weder`, this row **does** have a real DEV_NOTES dossier. The dossier is not mainly about whether Old English may show parasitic-vowel `-er` after a final `Cr` cluster; that shared chronology was already available. The row-specific problem was narrower and more important: what the OE-facing proto input must be if the project wants `weþer` to arise by regular rule order rather than by a legacy computational tag [Germanic/docs/DEV_NOTES.md:21434-21449,21563-21611].

The lexical identity itself is stable. Kroonen gives the Germanic item with `OE weder m. 'id.', E wether`; Orel likewise lists `OE weder id.`; Clark Hall has `weder I. m. wether sheep, ram` [@Kroonen2013; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29577-29581; @Orel2003; docs/references/orel_handbook_germanic_etymology.vision.txt:50629-50632; @ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48150-48152]. Those sources mostly print `weder` with `<d>`, while the row targets `weþer` with thorn. Nothing in the surviving DEV_NOTES dispute turns on that graphic difference; the project-local controversy is about the **proto-side input and chronology**, not about whether the OE lexeme is really 'wether' [Germanic/data/germanic-aligned-final.tsv:1371-1371; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5798-5801].

The row therefore needs the three labels stated plainly. `PROTO = *wíθrą` is the comparative headword now carried by the TSV for this cognate set. `PROTOFORM = *wíθrą` is also the actual derivational input now fed to the OE cascade. `COUNTERPART = weþer` is the selected OE reflex the row aims to derive [Germanic/data/germanic-aligned-final.tsv:1371-1371]. The fact that `PROTO` and `PROTOFORM` are identical strings is not trivial here. DEV_NOTES explicitly argues that the project should stop using the older artificial breve-tag form `*wíθră` and should instead use a reconstructable PGmc form with final `*ą`, because only that gives both the needed i-lowering environment and an etymologically interpretable input [Germanic/docs/DEV_NOTES.md:21563-21611].

The crucial DEV_NOTES sequence has two stages, and the first is superseded. In `§17.10.5–§17.10.6`, the notes first argued that the legacy form `*wíθră` should be replaced by bare `*wíθr`, because Ringe and Taylor place the loss of word-final short low vowels before later Anglo-Frisian developments. DEV_NOTES even called the trailing breve an “inert, deletion-bound marker” and concluded that “the `ă` in our TSV is a legacy computational artifact, not a historical reality” [Germanic/docs/DEV_NOTES.md:21429-21433,21463-21467]. In that phase, the note preserved the very useful shared chronology: “By the PWGmc loss of word-final short low vowels ... numerous word-final CR-clusters arose,” and those clusters later receive OE epenthesis [Germanic/docs/DEV_NOTES.md:21434-21449; @RingeTaylor2014, §§3.1.2, 6.9.5; docs/references/ringe_taylor_linguistic_history_vol2.txt:18711-18729].

But `§17.10.7` immediately corrects that plan and should control the current slice. DEV_NOTES says unambiguously: “**The §17.10.5 empirical claim was wrong.**” After recompilation, bare `*wíθr` yielded `wiþer`, not `weþer`, because `NWGmcILowering` requires a following non-high vowel and a bare final `-r` stem provides none [Germanic/docs/DEV_NOTES.md:21563-21585]. That row-specific point is the major difference from `weather / weder`: both words share the final-`Cr` epenthesis chronology, but only `wether` also needs a pre-apocope environment that lowers `*i > *e`. The row cannot simply inherit weather's easier `Cr > Cer` explanation and stop there.

DEV_NOTES then gives the current solution in exactly the form that should be preserved. Under the heading “**Why `*wíθrą` is the right target**,” the note says that PGmc reconstructs `*wéþruz / *wéþrą` for ‘wether’ and that the neuter/a-stem-like nominative singular input `*wíθrą` is “an actual reconstructable PGmc form, not an engineering tag” [Germanic/docs/DEV_NOTES.md:21587-21599]. The rule sequence is then explicit and row-addressed: `*ą` counts as a non-high vowel, so `NWGmcILowering` applies (`*wíθrą → *wéþrą`); later loss of final nasalized `*ą` creates final `-þr`; then `OEEpentheticInsertion` yields `*wéþer > weþer` [Germanic/docs/DEV_NOTES.md:21592-21607]. The current published trace agrees point for point with that summary [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5790-5801].

The shared OE epenthesis note remains necessary, but only as part of that fuller row-specific account. DEV_NOTES defines `OEEpentheticInsertion` as a “**real phonological rule**” for parasitic vowel insertion in final consonant clusters and states that after front vowels the inserted vowel surfaces as `e` [Germanic/docs/DEV_NOTES.md:16661-16691]. Ringe and Taylor describe the same class historically: “In word-final Cr-clusters a vowel was always inserted ... Normally the inserted vowel agreed in frontness with the vowel of the preceding syllable” [@RingeTaylor2014, §6.9.5; docs/references/ringe_taylor_linguistic_history_vol2.txt:18725-18729]. For row 2283, however, that shared note explains only the **last** step `*wéþr > *wéþer`; it does not by itself justify the `e` of the stressed syllable. The stressed-vowel lowering remains the row-specific issue.

Two additional DEV_NOTES passages are worth preserving as limited background. First, the March 2026 i-lowering refinement table already treated `wether` as a positive case with no onset-velar blocker and predicted “Lower | weþer ✓,” but it did so with the old form `*wiθră`; that passage helps explain why the project kept expecting lowering here, yet it is not a secure anchor for the current `*wíθrą` row state [Germanic/docs/DEV_NOTES.md:5621-5782]. Second, the later back-mutation canvass explicitly lists `*wíθrą` among rows where initial `w-` does **not** trigger the separate `*í > *ú` development, because the following material is `*θ + *r`, “not `*u/*o`” [Germanic/docs/DEV_NOTES.md:43585-43624]. That matters because it blocks a tempting but wrong alternative explanation for the row's vowel history.

Overall, row 2283 is better documented than many surrounding rows, but its documentation has to be handled carefully. The strongest current evidence is not the old placeholder note, and not the older `*wíθră` trace. It is the correction in `§17.10.7`: bare `*wíθr` was tested and rejected; `*wíθrą` was adopted because it preserves both historical interpretability and the regular derivation `*wíθrą > *wéθrą > *wéθr > *wéθer > weþer` [Germanic/docs/DEV_NOTES.md:21563-21611; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5790-5801].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-21563-21611

- Source heading: `§17.10.7 — Correction: *wíθr fails i-lowering; migrate to *wíθrą instead`
- Fragment type: `row_specific_resolution`
- Status: `current`
- Issue tags: `protoform_correction`; `i_lowering`; `final_cr_epenthesis`; `quotation_preserved`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs:

This is the row's main anchor. It says the earlier bare-stem proposal was wrong, explains exactly why `*wíθr` cannot trigger `NWGmcILowering`, and then gives the adopted solution: `*wíθrą` is retained because final `*ą` supplies the non-high-vowel environment before later loss and OE epenthesis [Germanic/docs/DEV_NOTES.md:21563-21611]. If a future index needs one line-range that actually captures the present row policy, this is it.

### DEV_NOTES:line-21434-21497

- Source heading: `§17.10.5 — Role 3 migration: *wíθră should become *wíθr, not *wíθra`
- Fragment type: `row_specific_superseded_analysis`
- Status: `superseded`
- Issue tags: `bare_stem_plan`; `final_vowel_loss`; `historical_chronology`; `diagnostic_quote`
- Recommended next use: `preserve_as_project_history`
- Shared with row IDs:

This fragment is superseded but still important. It preserves the project reasoning that exposed why the old breve form was unsatisfactory in the first place: final short low vowels should already be gone before later OE developments, and the older `*wíθră` was functioning as a computational convenience rather than as a clean historical input [Germanic/docs/DEV_NOTES.md:21434-21449,21463-21467]. The historical chronology argued here remains useful; the actual migration target proposed here does not.

### DEV_NOTES:line-16661-16691

- Source heading: `OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)`
- Fragment type: `shared_phonology_fragment`
- Status: `current`
- Issue tags: `epenthesis`; `final_cr_cluster`; `shared_rule`
- Recommended next use: `cite_with_row_specific_note`
- Shared with row IDs: `2160`, `2280`, `2283`, and other final-`Cr` rows

This is the best shared-rule support for the final step. DEV_NOTES defines epenthesis as a real phonological rule and states the front/back conditioning of the inserted vowel [Germanic/docs/DEV_NOTES.md:16661-16691]. For row 2283 it should be cited together with `§17.10.7`, not instead of it, because it explains `*wéþr > *wéþer` but not the earlier `*wí- > *wé-`.

### DEV_NOTES:line-5621-5782

- Source heading: `Refined analysis: onset velars also block i-lowering (2026-03-09 continued)` + implementation results
- Fragment type: `diagnostic_row_comparator`
- Status: `diagnostic_only`
- Issue tags: `i_lowering_environment`; `older_protoform`; `wether_test_case`
- Recommended next use: `background_only`
- Shared with row IDs: `nest`, `lid`, `fright`, `fish`, `liver`, `lick`

This passage is useful mainly because it shows that `wether` was one of the words pushing the i-lowering investigation: the table records `wether` as a case with no relevant blocker and expected lowering to `weþer` [Germanic/docs/DEV_NOTES.md:5621-5782]. But it still uses the older `*wiθră` representation and predates the more exact `*wíθr` versus `*wíθrą` correction. It should therefore stay diagnostic rather than serving as the row's main anchor.

### DEV_NOTES:line-43585-43624

- Source heading: `Conditioning — handbook canvass and final scope`
- Fragment type: `background_scope_note`
- Status: `current`
- Issue tags: `w_back_mutation_exclusion`; `conditioning_scope`; `negative_evidence`
- Recommended next use: `cite_only_if_w_mutation_is_raised`
- Shared with row IDs: several initial-`w-` rows

This fragment is narrow but helpful. It explicitly includes `*wíθrą` in a regression table and says the relevant following sequence is `*θ + *r (not *u/*o)`, so the separate initial-`w-` back-mutation rule does not apply [Germanic/docs/DEV_NOTES.md:43615-43624]. That keeps later report writing from confusing the row's `e` with a problem in the `wudu`/`wucu` type.

## Superseded or diagnostic material

- The pre-correction input `*wíθră` is superseded as row policy even though an older full trace still derives `weþer` from it. That trace documents project history, not the live protoform [docs/debug_snapshots/oe_full_trace_report.txt:16063-16116; Germanic/docs/DEV_NOTES.md:21463-21467,21609-21611].
- The bare-stem plan `*wíθră → *wíθr` is also superseded. DEV_NOTES preserves it because it clarified the chronology of final-vowel loss, but `§17.10.7` expressly withdraws its empirical conclusion [Germanic/docs/DEV_NOTES.md:21481-21497,21563-21585].
- Shared `weather / weder` material should be imported only partially. It is valid as comparator evidence for final `Cr > Cer` chronology, but it does not address the decisive row-local fact that `wether` needs a non-high-vowel trigger for i-lowering before the final vowel disappears [Germanic/docs/lexeme_reports/dev_notes_slices/2280-weather-weder.md:45-47; Germanic/docs/DEV_NOTES.md:21575-21596].

## Open questions for later work

- If `index.tsv` is revised later, the safest primary anchor is `DEV_NOTES:line-21563-21611`; `DEV_NOTES:line-21434-21497` is a valuable secondary anchor for superseded project history, not for current row policy.
- If later lexeme reporting wants to discuss the OE spelling more explicitly, it should note that the handbooks here cite `OE weder`, while the row and current trace normalize to `weþer`; the current dossier does not treat that graphic alternation as a separate lexical problem [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48150-48152; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5798-5801].
