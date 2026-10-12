---
row_id: 2238
concept: swine
counterpart: swīn
proto: "*swī́ną"
protoform: "*swḯną"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2238-swine-swīn.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2238-swine-swīn.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2238 swine / swīn

## Current row state

- The live OE row gives `CONCEPT = swine`, `COUNTERPART = swīn`, `PROTO = *swī́ną`, `PROTOFORM = *swḯną`, and `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1194-1194].
- The live TSV note is already unusually explicit and should control the slice: `Proto: oblique *swīnăn→*swīną (n. a-stem nom.sg.; Kroonen) §17.46 Phase 2: PROTOFORM accented (ḯ = stressed long *ī, U+1E2F) so NWGmcInStemNLoss does not fire on the root *ī.` [Germanic/data/germanic-aligned-final.tsv:1194-1194].
- For this row the three-way distinction matters. `PROTO = *swī́ną` is the row's comparative/project headword spelling; `PROTOFORM = *swḯną` is the OE-facing derivational input rewritten with the single-codepoint stressed-long-`ī` notation; `COUNTERPART = swīn` is the OE target form to be explained [Germanic/data/germanic-aligned-final.tsv:1194-1194].
- Existing packet/memo infrastructure already uses the stem `2238-swine-swīn`, so this slice reuses that stem rather than inventing a new row filename [Germanic/docs/lexeme_reports/research_memo_index.tsv:108-108; Germanic/docs/lexeme_reports/coverage_audit.md:148-148].
- `oe_known_problems.tsv` has no row-local entry for `2238`, `swīn`, `*swī́ną`, or `*swḯną`, so the item is not currently being tracked as an OE exception or wontfix case [Germanic/data/oe_known_problems.tsv:1-8].

## Detailed development-note summary

The surviving DEV_NOTES material for row 2238 is not a debate about whether OE `swīn` is real or whether the row should be exceptional. The real project problem was narrower and more technical: once `NWGmcInStemNLoss` was broadened so that it could delete final `-n` in the unstressed feminine in-stem suffix `*-īn`, it briefly over-applied to the stressed root vowel of `*swīną` and produced the false derivation `*swīną → swī` [Germanic/docs/DEV_NOTES.md:41751-41818]. The slice therefore needs to preserve both the bad intermediate project state and the later correction, because otherwise the current row note looks arbitrary.

The philological core is straightforward. OE `swīn` is the ordinary inherited noun, and Kroonen's comparative lemma is `*swina- n. 'pig'`, with OE `swin` among the reflexes [@Kroonen2013, p. 502]. Clark Hall likewise has `swin (y) n. wild boar, pig, hog, pl. "swine"` [@ClarkHall1960, s.v. "swin"]. Nothing in the surviving DEV_NOTES material suggests that the OE target should be anything other than `swīn`; the only instability lay in how the pre-OE input should be encoded so that the transducer would not confuse a stressed root `*ī` with the unstressed suffixal `*-īn` that really does undergo `n`-loss.

That distinction is why the row's `PROTO` and `PROTOFORM` must not be collapsed. The current project headword is `*swī́ną`, with acute accent marking the stressed long vowel in the human-readable comparative layer. The current row-specific FST input is `*swḯną`, where `ḯ` is not a new historical stage but a notation-layer repair introduced because foma would not reliably accept combining-acute `ī́` under `apply down`; DEV_NOTES is explicit that "`*ḯ` = stressed long *ī" and that the diaeresis is "purely notational" [Germanic/docs/DEV_NOTES.md:41923-41939]. `COUNTERPART = swīn` then remains the ordinary OE surface outcome because `OldEnglishRemoveStars` maps `{*ḯ} -> ī`; the special tier exists only so `NWGmcInStemNLoss` can remain restricted to unstressed long `*ī` [Germanic/docs/DEV_NOTES.md:41944-41957].

The earlier regression note is still useful because it states exactly what went wrong. DEV_NOTES records the probe result `*swīną → swī (expected swīn)` and then explains the bad derivational path: `OEHeavySyllableNasalApocope` first yields `*swīn`, after which the broadened `NWGmcInStemNLoss` wrongly deletes the final `n` from the monosyllabic root form [Germanic/docs/DEV_NOTES.md:41767-41779]. The diagnosis is also worth preserving nearly verbatim: the live sources restrict the change to **unstressed** suffixal `*-īn`, not to any word-final `īn` sequence, and Brunner's formulation is quoted directly in DEV_NOTES as `"Der alte Ausgang -ī(n) zeigt sich in dem ständigen i-Umlaut der Wurzelsilbe"`—that is, the old ending `-ī(n)` is visible through consistent i-umlaut of the **root syllable**, so the change belongs to the suffix, not the stressed root [Germanic/docs/DEV_NOTES.md:41797-41806; @SieversBrunner1965, §280; @Campbell1959, §473; @RingeTaylor2014, pp. 71-72; @Fulk2018, §7.34].

The current project decision is the later `*ḯ` solution in §17.46, not the interim context-restriction workaround from §17.45.3g. DEV_NOTES says the context restriction "worked for the small TSV but is not principled" because the change is conditioned by stress rather than syllable count [Germanic/docs/DEV_NOTES.md:41900-41922]. The permanent repair is therefore to encode stressed long root `*ī` separately and leave plain `*ī` available for the genuinely unstressed in-stem suffix. DEV_NOTES then records the exact verification pair that matters for this row: `swīną → swī (unstressed-suffix *ī, NWGmcInStemNLoss FIRES ✓)` versus `swḯną → swīn (stressed-root *ḯ, rule BLEEDS ✓)` [Germanic/docs/DEV_NOTES.md:42031-42040]. For row 2238, that is the real replacement working note: keep the lexeme regular, keep `swīn` as the OE target, keep `*swī́ną` as the comparative/project headword, and keep `*swḯną` as the row-specific derivational encoding that prevents the old false output.

One older DEV_NOTES line should survive only with a warning label. Before the regression was discovered, a scope-check note said that `*swīną` was an `acc.sg. neut. n-stem 'swine'` and therefore unaffected because it contained `-n-ą`, not `-īn` [Germanic/docs/DEV_NOTES.md:41250-41258]. That line is valuable as project chronology, but it is no longer safe as current row guidance: the later regression note and the stressed-`ḯ` fix show that the row absolutely did need explicit handling, and the live TSV note now frames the background differently, from oblique `*swīnăn` to nominative `*swīną` with Kroonen-style a-stem citation-form orientation [Germanic/data/germanic-aligned-final.tsv:1194-1194; @Kroonen2013, p. 502].

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-41250-41258

- Source heading: `§17.45.3f ... F. Scope check on the proto-gate`
- Source line or section hint: `lines 41250-41258`
- Fragment type: `superseded_project_history`
- Status: `superseded`
- Issue tags: `early_scope_check`; `stale_morphology_label`; `pre_regression_confidence`
- Recommended next use: `keep_only_as_chronology`
- Shared with row IDs:

This fragment preserves the early, now-insufficient project confidence statement: `Search confirms *swīną (acc.sg. neut. n-stem 'swine') has *-n-ą (with short *a) not *-īn, so is unaffected` [Germanic/docs/DEV_NOTES.md:41257-41258]. It should not be treated as current row policy. Its value is diagnostic: it shows the project initially believed the new rule could not touch `swine`, before the later probe proved otherwise.

### DEV_NOTES:line-41751-41823

- Source heading: `§17.45.3g — Regression on *swīną and rule-context restriction`
- Source line or section hint: `lines 41751-41823`
- Fragment type: `row_specific_regression_and_diagnosis`
- Status: `diagnostic_but_still_important`
- Issue tags: `regression`; `false_output_swī`; `root_vs_suffix`; `shared_sound_change_logic`
- Recommended next use: `cite_when_explaining_why_the_row_note_exists`
- Shared with row IDs:

This is the key diagnostic fragment and it should be preserved in substance. DEV_NOTES records the exact failure state, `*swīną → swī (expected swīn)`, then explains that the word first becomes `*swīn` after heavy-syllable nasal apocope and only afterward loses `-n` incorrectly because the rule is matching any word-final `īn` string rather than just the unstressed suffixal one [Germanic/docs/DEV_NOTES.md:41767-41779]. The same block then states the principle that remains current even though its immediate fix was later replaced: all cited handbooks restrict the change to **unstressed** `*ī`, and stem-internal stressed `*īn` in monosyllables such as `swīn`, `līn`, and `wīn` keeps final `-n` in OE [Germanic/docs/DEV_NOTES.md:41789-41823; @RingeTaylor2014, pp. 71-72; @Campbell1959, §473; @SieversBrunner1965, §280; @Fulk2018, §7.34].

### DEV_NOTES:line-41893-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line or section hint: `lines 41893-41957`
- Fragment type: `current_shared_policy`
- Status: `current`
- Issue tags: `stressed_long_i`; `notation_migration`; `proto_vs_protoform`; `rule_gating`
- Recommended next use: `cite_as_current_authority`
- Shared with row IDs: all OE rows migrated to stressed `*ḯ`

This is the controlling current fragment. DEV_NOTES explicitly rejects the earlier context-restriction solution as unprincipled and says the real conditioning factor is stress: a monosyllabic root such as `*swīn` keeps its `-n` because the `*ī` is the stressed root vowel, not because the word is short [Germanic/docs/DEV_NOTES.md:41900-41922]. The notation note is equally important for later writers: combining-acute `ī́` failed under foma input, so single-codepoint `ḯ` was adopted; "`The diaeresis is purely notational. Semantically *ḯ = stressed long *ī`" [Germanic/docs/DEV_NOTES.md:41925-41939]. The same block then says that `{*ḯ} -> ī` at surface level, because OE spelling does not mark the distinction [Germanic/docs/DEV_NOTES.md:41944-41957].

### DEV_NOTES:line-42006-42040

- Source heading: `§17.46 ... E. TSV migration (Phase 4)` plus `F. Verification`
- Source line or section hint: `lines 42006-42040`
- Fragment type: `current_row_verification`
- Status: `current`
- Issue tags: `seed_migration`; `verification_probe`; `regression_cleared`; `swḯną`
- Recommended next use: `cite_for_live_row_behavior`
- Shared with row IDs: all migrated `*ḯ` rows plus row `2034` as the retained unstressed-`*ī` control

This fragment gives the current operational proof for row 2238. DEV_NOTES records the seed migration `*swīną → *swḯną` in Phase 2, then verifies the contrastive probes `swīną → swī` and `swḯną → swīn` [Germanic/docs/DEV_NOTES.md:42028-42040]. For this slice, that pair is the shortest accurate statement of why the row now has split notation. Plain `*ī` remains available for the unstressed suffix that `NWGmcInStemNLoss` must consume elsewhere; stressed root `*ī` is rewritten as `*ḯ`, which bleeds the rule and preserves OE `swīn`.

## Superseded or diagnostic material

- The old `acc.sg. neut. n-stem` scope-check note is not current row policy anymore. It is useful only because it shows the project once thought `swine` lay outside the risk zone for `NWGmcInStemNLoss`, before the explicit regression probe disproved that confidence [Germanic/docs/DEV_NOTES.md:41250-41258].
- The context-restriction proposal in §17.45.3g is also no longer the live solution. It correctly diagnosed the difference between stressed root `*ī` and unstressed suffixal `*-īn`, but DEV_NOTES itself later replaced that workaround with the more principled stressed-`*ḯ` tier [Germanic/docs/DEV_NOTES.md:41827-41891; Germanic/docs/DEV_NOTES.md:41893-41922].
- Earlier project forms such as `*swīnăn` and unaccented `*swīną` should be kept only with labels. `*swīnăn` remains useful background for the stem/paradigm history alluded to in the live note, but it is not the current OE-facing `PROTOFORM`; unmarked `*swīną` is the exact spelling whose ambiguity caused the regression, so it should not silently replace current `*swḯną` in row-level prose [Germanic/data/germanic-aligned-final.tsv:1194-1194; Germanic/docs/DEV_NOTES.md:42028-42040].
- The row is not a known-problems item. Any future prose that treats `swīn` as an exception, analogical rescue, or unresolved philological problem would overstate the evidence; the surviving material supports a regular row with a resolved notation/rule-gating history [Germanic/data/oe_known_problems.tsv:1-8].

## Open questions for later work

- If this row is ever indexed, decide whether the index should point only to the current authorities `DEV_NOTES:line-41893-41957` and `DEV_NOTES:line-42006-42040`, while keeping `41250-41258` and the context-restriction material explicitly marked as superseded chronology.
- If later report writing revises the row note, make the notation bridge fully explicit in one sentence: `project headword *swī́ną` versus `OE-facing input *swḯną`, with `ḯ` used only because combining-acute `ī́` was not reliable in foma input [Germanic/docs/DEV_NOTES.md:41925-41939].
- If a future lexeme report wants fuller philological prose, it may be worth adding a short source note on Kroonen's lemma format `*swina-` versus the row's nominative-singular/project headword `*swī́ną`, but nothing in the current slice requires changing the row data [@Kroonen2013, p. 502].
