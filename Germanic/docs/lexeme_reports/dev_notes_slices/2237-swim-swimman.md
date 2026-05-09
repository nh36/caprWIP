---
row_id: 2237
concept: swim
counterpart: swimman
proto: "*swímmaną"
protoform: "*swímmaną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2237 swim / swimman

## Current row state

- The live OE row is `2237`, `CONCEPT swim`, `COUNTERPART swimman`, `PROTO *swímmaną`, `PROTOFORM *swímmaną`, `DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1190-1190].
- For this row, `PROTO` and `PROTOFORM` are the same inherited verbal form. The row is not currently using a substitute stage-form, a repaired preform, or a different paradigm cell; the OE target remains the infinitive `COUNTERPART = swimman` [Germanic/data/germanic-aligned-final.tsv:1190-1190].
- `oe_known_problems.tsv` has no entry for row `2237`, `*swímmaną`, or `swimman`, so the project is not presently tracking this item as an OE exception, mismatch, or unresolved analogical target [Germanic/data/oe_known_problems.tsv:1-8].
- No packet, research memo, or pre-existing lexeme report stem was found for this row, and `coverage_audit.md` still lists `| 2237 | swim | swimman | regular | no | - | - | - | none |`, so this slice uses the canonical row-based filename [Germanic/docs/lexeme_reports/coverage_audit.md:384-384].
- The published OE derivation trace is an exact match: `PROTO: *swímmaną`, `EXPECTED: swimman`, `OUTPUTS: swimman`, with only routine OE-side steps `OE Heavy Syllable Nasal Apocope`, `OE Secondary Nasalization`, and `OE Weak Tail Reduction` before surface `swimman` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5029-5041].

## Detailed development-note summary

The surviving DEV_NOTES support for row `2237` is real but narrow. It does not preserve a dedicated lexeme memo arguing over the OE target; instead it preserves three kinds of material that later work would otherwise have to rediscover separately: a handbook quotation explaining why the root vowel stays `i` before `-mm-`, a later implementation note showing that the nasal-dissimilation rule was explicitly prevented from breaking `swimman`, and a diagnostic quotation about final degemination that matters for bare written `swim` but does **not** retarget the row away from infinitive `swimman` [Germanic/docs/DEV_NOTES.md:10345-10357,12945-12973,13554-13571].

The most straightforward philological support is Campbell's statement that the redistribution of short vowels does not apply before a nasal consonant followed by another consonant. DEV_NOTES preserves the crucial wording: `"OE forms exemplifying this are ... the passive participles and infinitives of strong verbs of Class III like swummen, bunden, sprungen, swimman, bindan, springan"` [Germanic/docs/DEV_NOTES.md:10347-10357; @Campbell1959, §116]. For this row, that matters because the live target `swimman` is exactly such a Class III infinitive with root `i` before `mm`. The note is shared background rather than a row-local controversy, but it is still the clearest surviving source statement that the current row vowelism is regular rather than patched.

The most current project-specific fragment is the nasal-dissimilation implementation note written for `heofon`. There DEV_NOTES says the new `m → f` rule must **not** apply to geminates, listing as exclusions `*mannaz` and `*swimmanan`, then records the regression test `swimmăną    swimman    ✓  (no regression)` [Germanic/docs/DEV_NOTES.md:12945-12973]. The lexical importance for row `2237` is practical rather than historical: the project had to guard a shared sound-change rule so that a regular geminate-`mm` verb would keep surfacing as `swimman`. This fragment therefore does not propose a new `PROTOFORM`; instead it preserves the later correction that protects the existing row from an unrelated overapplication.

The third relevant DEV_NOTES passage is valuable mainly as a boundary marker. DEV_NOTES quotes Brunner's discussion of final degemination: `"Vereinfachung von Gemination tritt namentlich ... im Wortauslaut ein"`, with the example series `swim ... swimman`, and then translates the point as phonological simplification of word-final geminates, with occasional doubled spellings restored from inflected forms [Germanic/docs/DEV_NOTES.md:13554-13571; @SieversBrunner1965, §231]. For row `2237`, this does **not** mean the OE counterpart should be reduced to `swim`. It means that textual bare `swim` can coexist with inflected or infinitival `swimman` under final degemination, so later report work should not mistake simplex spellings for evidence that the live row target is wrong.

The replacement working conclusion is therefore conservative. Current row policy stays exactly where the live TSV already puts it: `PROTO = *swímmaną`, `PROTOFORM = *swímmaną`, `COUNTERPART = swimman`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1190-1190]. DEV_NOTES adds useful support and one important regression guard, but the support is still mostly shared or diagnostic rather than a dense row-local dossier. That is enough for a detailed replacement slice and not yet a strong case for indexing.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-10345-10357

- Source heading: `Campbell (1959) §116`
- Source line or section hint: `lines 10345-10357`
- Fragment type: `shared_handbook_support`
- Status: `current_but_shared`
- Issue tags: `class_iii_strong_verb`; `nasal_cluster`; `root_vowel_retention`
- Recommended next use: `use_as_background_support`

This fragment preserves the main handbook statement supporting the live row's regularity. DEV_NOTES quotes Campbell's observation that short-vowel redistribution does not apply before nasal-plus-consonant clusters and includes the exact Class III examples `swummen ... swimman` [Germanic/docs/DEV_NOTES.md:10347-10357; @Campbell1959, §116].

> `"OE forms exemplifying this are ... the passive participles and infinitives of strong verbs of Class III like swummen, bunden, sprungen, swimman, bindan, springan."` [Germanic/docs/DEV_NOTES.md:10349-10352; @Campbell1959, §116]

For row `2237`, the force of the fragment is simple: `swimman` is being treated as an ordinary Class III infinitive whose root vowel is expected before `-mm-`, not as an exceptional or analogically repaired form.

### DEV_NOTES:line-12945-12973

- Source heading: `nasal dissimilation conditioning and regression tests`
- Source line or section hint: `lines 12945-12973`
- Fragment type: `implementation_guard_with_row_relevance`
- Status: `current`
- Issue tags: `m_to_f_dissimilation`; `geminate_blocking`; `regression_test`
- Recommended next use: `cite_if_rule_interaction_matters`

This is the strongest current project fragment for the row because it records a rule interaction that could otherwise have damaged the output. DEV_NOTES states that the dissimilation rule must not apply to geminates, explicitly listing `*swimmanan` among the protected shapes, and then records the successful check `swimmăną    swimman    ✓  (no regression)` [Germanic/docs/DEV_NOTES.md:12948-12950,12972-12973].

> `This prevents the rule from applying to: ... Geminates like *swimmanan (first *m not in dissimilation context)` [Germanic/docs/DEV_NOTES.md:12948-12950]

> `$ echo 'swimmăną' | flookup -i backend/old_english.bin`
> `swimmăną    swimman    ✓  (no regression)` [Germanic/docs/DEV_NOTES.md:12972-12973]

The notation here is not identical to the live row's accented `PROTOFORM *swímmaną`, and that difference should not be flattened away. The live TSV remains authoritative for the row header [Germanic/data/germanic-aligned-final.tsv:1190-1190]. The DEV_NOTES value is the conditioning claim: geminate `mm` must survive this rule family intact.

### DEV_NOTES:line-13554-13571

- Source heading: `Kurath 1956 via Brunner §231 on final degemination`
- Source line or section hint: `lines 13554-13571`
- Fragment type: `diagnostic_philological_context`
- Status: `diagnostic_only`
- Issue tags: `final_degemination`; `simplex_swim`; `boundary_note`
- Recommended next use: `use_as_textual_diagnostic_only`

This fragment matters because it distinguishes row-target `swimman` from word-final spellings such as `swim`. DEV_NOTES quotes Brunner's summary of Kurath's argument that single final consonant spellings can reflect actual phonological simplification of geminates, not just spelling looseness [Germanic/docs/DEV_NOTES.md:13554-13571; @SieversBrunner1965, §231].

> `"Vereinfachung von Gemination tritt namentlich in folgenden Fällen ein: 1. Gewöhnlich im Wortauslaut, vgl. Formen wie ... swim ... mit ... swimman ..."` [Germanic/docs/DEV_NOTES.md:13560-13566; @SieversBrunner1965, §231]

For row `2237`, this is diagnostic rather than corrective. It helps explain why bare `swim` may appear in textual or lexical discussion, but it does not argue for changing `COUNTERPART = swimman`.

## Superseded or diagnostic material

- No dedicated superseded row-local target was found. Nothing in surviving DEV_NOTES argues that row `2237` once should have targeted some other OE infinitive, some analogical replacement, or a different derivation class [Germanic/docs/DEV_NOTES.md:10345-10357,12945-12973,13554-13571].
- The nasal-dissimilation fragment preserves notation drift (`*swimmanan`, `swimmăną`) rather than a competing live row state. Those spellings are useful because they show the rule environment and the regression test, but the live row's `PROTO = PROTOFORM = *swímmaną` remains the current repository authority [Germanic/docs/DEV_NOTES.md:12948-12950,12972-12973; Germanic/data/germanic-aligned-final.tsv:1190-1190].
- The Brunner/Kurath material is especially easy to overread. It is about phonological simplification in word-final position and therefore helps interpret simplex `swim`; it is not a proposal to rewrite the row from infinitive `swimman` to a degeminated lexical target [Germanic/docs/DEV_NOTES.md:13554-13571; @SieversBrunner1965, §231].
- Comparative reference works align with the live row without adding any sign of lexical instability: Kroonen lists Proto-Germanic `*swimman-` with OE `swimman`, and Clark Hall has `swimman³ ... to swim, float` [@Kroonen2013; @ClarkHall1960]. [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:25703-25708; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:39416-39416].

## Open questions for later work

- If later report work wants this row to become indexable, the missing piece is a denser row-local note or packet; the present DEV_NOTES evidence is accurate but mostly shared background plus one implementation guard.
- If a future final report needs fuller paradigm framing, add direct citations for the strong-verb paradigm (`swimman`, preterite, past plural, participle) so the row does not rely mainly on shared Campbell/Brunner discussion and trace output.
- If future searches turn up additional `swim` material, keep final-degeminated simplex `swim` evidence separate from the infinitive row target `swimman`; this row does not currently show a `PROTO`/`PROTOFORM` split or a lexical retargeting problem.
