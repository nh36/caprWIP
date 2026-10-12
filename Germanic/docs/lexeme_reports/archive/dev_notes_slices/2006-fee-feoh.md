---
row_id: 2006
concept: fee
counterpart: feoh
proto: *féxu
protoform: *féxu
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2006 fee / feoh

## Current row state

- The live Old English row has `CONCEPT = fee`, `COUNTERPART = feoh`, `PROTO = *féxu`, `PROTOFORM = *féxu`, and `DERIVATION_CLASS = regular`; the row-level note is empty, and the only source metadata recorded in the TSV is duplicated Wiktionary inheritance tagging [Germanic/data/germanic-aligned-final.tsv:294-294].
- `coverage_audit.md` still classifies row 2006 as a regular row with empty `NOTE` and no report required, so this slice is replacing absent DEV_NOTES coverage rather than condensing an existing packet workflow [Germanic/docs/lexeme_reports/coverage_audit.md:233-236].
- No exact-row manifest entry exists, and `oe_known_problems.tsv` likewise does not list `*féxu`; for current project purposes, row 2006 is therefore being treated as a regular success case, not as an exception bucket item or open mismatch [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/data/oe_known_problems.tsv:1-8].
- No exact row-2006 packet or research memo was located during this pass. The replacement note therefore has to rely mainly on shared DEV_NOTES rule discussions that happen to preserve `*féxu -> feoh` as a control example.

## Development-note summary

No dedicated row-2006 subsection survives in `DEV_NOTES.md`. What survives instead is a small but internally consistent cluster of shared rule notes, and those notes are specific enough to support the live row if they are read carefully. The most important statement is the short-diphthong/apocope refactor note: `Added Campbell §§238/346 rule: final high vowels lost after /*x/ (h) regardless of weight, ordered before intervocalic h-loss. E.g. *féxu → *féoxu → feoh (not feou)` [Germanic/docs/DEV_NOTES.md:29441-29443]. For this row, that sentence is the closest thing to a current governing policy statement.

That line matters because it preserves the main phonological distinction that could otherwise get flattened. Row 2006 is **not** being justified as an ordinary contraction output like oblique `fēo`; rather, DEV_NOTES says the nominative-type outcome `feoh` depends on final high-vowel loss applying while `h/x` is still present, so the form reaches surface `feoh` before any hypothetical `feou` stage can survive as the row target [Germanic/docs/DEV_NOTES.md:29441-29443,29469-29475]. A later risk-audit note makes the same boundary condition explicit from the other side: among `*[eé]x` items with back vowels, only `*téxun` needed the new `*eo + *o` contraction clause, because ``*féxu* loses its *u to high-vowel apocope before h-loss`` [Germanic/docs/DEV_NOTES.md:42450-42455].

The surviving shared philology also helps keep nominative `feoh` distinct from related but non-identical forms. DEV_NOTES preserves Brunner's statement that the contraction class includes `feoh — Gen. feos`, and its summary table glosses `*fehu -> *feohu -> *feou -> *fēo* (gen)` as the oblique development for 'cattle' [Germanic/docs/DEV_NOTES.md:42551-42556; Germanic/docs/DEV_NOTES.md:42607-42619]. That is useful background, but it should not be mistaken for the row target: row 2006 still points to simplex `feoh`, while `fēo/feos` remain oblique or paradigm-comparison evidence.

Finally, the row is repeatedly used as a regression probe rather than an unresolved problem. DEV_NOTES reports `féxu -> feoh ✓` when testing whether certain contraction clauses were unnecessary, and later again includes `*féxu -> feoh` in a stable verification sample after the stressed-long-`ē` refactor [Germanic/docs/DEV_NOTES.md:21673-21681; Germanic/docs/DEV_NOTES.md:42735-42739]. That does not create new lexeme-specific evidence, but it does show that `feoh` is entrenched in project workflow as an already-working control output.

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:29441-29443, 29469-29475

- Source heading: `§17.17.8 Implementation results (short-diphthong weight refactor)`
- Source line or section hint: `lines 29441-29443 and verification table/regression note at 29469-29475`
- Fragment type: `shared_rule_with_exact_pair`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `h_loss_ordering`; `nominative_target`; `regular_outcome`
- Recommended next use: `primary_anchor_for_final_report`
- Shared with row IDs: `2068, 2120`

This is the strongest surviving DEV_NOTES material for row 2006 because it names the exact proto/Old English pair and explains why the row works. The note says that Campbell §§238/346 required a rule for final high vowels after `h/x`, ordered before intervocalic `h`-loss, and gives the row itself as the example: `*féxu → *féoxu → feoh (not feou)` [Germanic/docs/DEV_NOTES.md:29441-29443]. The verification table immediately below then repeats the exact pair `| *féxu | feoh | feoh | §238 -u after h loss |`, and the short regression note lists `feoh` among the forms restored by the round-3 fixes [Germanic/docs/DEV_NOTES.md:29469-29475].

For replacement-note purposes, this fragment should carry most of the argumentative weight. It says plainly that the live target is not a loose guess based on modern English `fee`, nor just a generic "breaking before h" outcome. The decisive point is rule ordering: `*u` disappears under the special final-high-vowel condition while the `h/x` environment is still present, and that ordering blocks the wrong output `feou` [Germanic/docs/DEV_NOTES.md:29441-29443].

### Germanic/docs/DEV_NOTES.md:42450-42455

- Source heading: `§17.48.1 Broader source survey / Risk audit`
- Source line or section hint: `lines 42450-42455`
- Fragment type: `diagnostic_scope_control`
- Status: `current`
- Issue tags: `overgeneration_audit`; `contraction_vs_apocope`; `shared_rule_boundary`
- Recommended next use: `cite_to_distinguish_feoh_from_tēon`
- Shared with row IDs: `2242, 2010, 2086`

This fragment survives inside the much later `tēon` dossier, but it is materially relevant to row 2006 because it explains why `feoh` was **not** endangered by the new `*eo + *o` contraction work. DEV_NOTES says the audit searched all relevant `*[eé]x` items and concluded: `Of these only *téxun has *x followed by a non-apocopating back vowel. (*féxu loses its *u to high-vowel apocope before h-loss; *séxs/*féxtaną/*wéxtiz/*knéxtaz have *x followed by a consonant.)` [Germanic/docs/DEV_NOTES.md:42450-42455].

The value of this passage is mostly negative but still important. It tells later writers not to explain `feoh` with the same mechanism used for `tēon`. For row 2006, the operative logic remains apocope-plus-h-loss ordering, not the special contraction clause added for `*téxun` [Germanic/docs/DEV_NOTES.md:42450-42455].

### Germanic/docs/DEV_NOTES.md:42551-42556, 42607-42619

- Source heading: `Brunner §129.2 quotation and contraction-rule summary table`
- Source line or section hint: `quoted source at 42551-42556; schematic table at 42607-42619`
- Fragment type: `secondary_source_quote_preserved_in_dev_notes`
- Status: `background_current`
- Issue tags: `brunner`; `oblique_forms`; `nominative_vs_genitive`; `contraction_class`
- Recommended next use: `use_for_morphological_caution`
- Shared with row IDs: `2195, 2242`

This material is not a row-2006 note in the narrow sense, but it preserves source-backed philological substance that should stay attached to `feoh`. DEV_NOTES quotes Brunner as follows: `gemeinws. zefēon ... plēon ... sēon aus *fehan usw. ... ferner die Subst. feoh — Gen. feos ...` [Germanic/docs/DEV_NOTES.md:42551-42556]. It then restates the same pattern in a table, where `*fehu` develops through `*feohu` and `*feou` to `*fēo* (gen)` [Germanic/docs/DEV_NOTES.md:42607-42619].

The conservative use of this fragment is to preserve a distinction, not to collapse it. Brunner's quotation and the table both support the broader historical class in which `feoh` belongs, but they point especially to the **oblique/genitival** side of the paradigm. That is useful because it shows that long-diphthong contraction with this lexeme is real in OE, yet it should not be turned into an argument that row 2006 itself ought to target `fēo`. The slice should keep nominative `feoh` and oblique `fēo/feos` separate unless later row-specific evidence says otherwise [Germanic/docs/DEV_NOTES.md:42551-42556; Germanic/docs/DEV_NOTES.md:42607-42619].

### Germanic/docs/DEV_NOTES.md:33889-33899

- Source heading: `§17.21.10.2 Does breaking apply across /st/ + r?`
- Source line or section hint: `lines 33889-33899`
- Fragment type: `shared_phonological_background`
- Status: `background`
- Issue tags: `breaking`; `eo_quality`; `h_environment`; `canonical_example`
- Recommended next use: `cite_if_feoh_vocalism_needs_justification`
- Shared with row IDs: `2002, 2270`

This is shared background rather than a dedicated fee note, but it is one of the clearest surviving places where DEV_NOTES preserves a scholarly quotation explicitly naming `feoh`. Summarizing Hogg, the note says: `Breaking is described as diphthongization of front vowels before back consonants ... The canonical examples are: *feoh 'cattle', *eo 'horse', *weorpan 'throw', *weorčan 'work', *eald 'old', *feoll 'fell'. Breaking applies before /h/, /x/, /r/ + C, /l/ + C` [Germanic/docs/DEV_NOTES.md:33889-33899].

For row 2006, this fragment is best used as phonological background for the `eo` of `feoh`. It does not solve the row by itself — the apocope/h-loss ordering note does that — but it does reinforce that `feoh` is a canonical, not marginal, illustration of OE breaking before `h/x` [Germanic/docs/DEV_NOTES.md:33889-33899].

### Germanic/docs/DEV_NOTES.md:21673-21681, 42735-42739

- Source heading: `contraction-clause audit` and `stressed long-ē verification sample`
- Source line or section hint: `lines 21673-21681 and 42735-42739`
- Fragment type: `verification_probe`
- Status: `current`
- Issue tags: `regression_probe`; `stable_output`; `shared_control_case`
- Recommended next use: `cite_as_verification_only`
- Shared with row IDs: `1987, 2195, 2242`

These two verification snippets are brief, but they matter because they show how the project has been using row 2006 operationally. In the contraction audit, DEV_NOTES says that removing nine breve clauses left total mismatches unchanged and lists `féxu     → feoh    ✓` among the retained successes [Germanic/docs/DEV_NOTES.md:21673-21681]. Much later, the stressed-long-`ē` refactor again cites `*féxu → feoh` in its sample of invariant probe outputs [Germanic/docs/DEV_NOTES.md:42735-42739].

That does not add new philology, and it should not be over-read as if DEV_NOTES once had a full fee dossier now lost. But it does show that `feoh` has repeatedly functioned as a trusted regression check. In practice, that makes the row better supported than a totally silent regular row, even though most of the support is shared and procedural rather than lexeme-exclusive [Germanic/docs/DEV_NOTES.md:21673-21681; Germanic/docs/DEV_NOTES.md:42735-42739].

## Superseded or diagnostic material

No dedicated row-2006 DEV_NOTES mismatch narrative survives for an earlier alternative target. The main superseded or diagnostic item is the rejected form `feou`, which the current note explicitly excludes by writing `feoh (not feou)` [Germanic/docs/DEV_NOTES.md:29441-29443]. That should be preserved as diagnostic history only: it is the wrong intermediate/result that the rule-ordering fix was designed to avoid.

Two related forms also need to stay fenced off from the live row target. First, Brunner's `feoh — Gen. feos` and the schematic `*fehu ... *fēo* (gen)` belong to the same historical paradigm, but DEV_NOTES preserves them precisely as oblique/genitive evidence, not as a reason to retarget row 2006 away from nominative `feoh` [Germanic/docs/DEV_NOTES.md:42551-42556; Germanic/docs/DEV_NOTES.md:42607-42619]. Second, the later smoothing discussion cites `feoh -> feh 'money'` only as an example showing that smoothing operates before velars; it is not presented there as the row's current lexical target [Germanic/docs/DEV_NOTES.md:33915-33915].

## Open questions for later work

- If row 2006 ever gets a full packet, add explicit lexical-source citations for the nominative/oblique split (`feoh` versus `fēo/feos`) so that the slice does not have to rely mainly on Brunner material preserved second-hand inside DEV_NOTES.
- Decide whether a future final report should say more directly that the modern English gloss `fee` is semantically narrower than OE `feoh` 'cattle, property, money'; DEV_NOTES material here is mostly phonological, not semantic.
- If proto notation is revisited, check whether later report prose should mention the ordinary comparative citation form `*fehu` alongside the project's stress-marked `*féxu`, without implying that the live row itself is unstable.
