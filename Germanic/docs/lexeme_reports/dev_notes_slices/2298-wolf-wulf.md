---
row_id: 2298
concept: wolf
counterpart: wulf
proto: *wúlfaz
protoform: *wúlfaz
derivation_class: unexplained_unmodelled
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2298-wolf-wulf.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2298-wolf-wulf.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2298 wolf / wulf

## Current row state

- CONCEPT: `wolf`
- COUNTERPART: `wulf`
- PROTO: `*wúlfaz`
- PROTOFORM: `*wúlfaz`
- DERIVATION_CLASS: `unexplained_unmodelled`
- Live TSV note (abridged): Campbell §115 names `wulf` as an exception to regular lowering (`**wolf` is the regular outcome, cf. OHG `wolf`); no lautgesetzlich `PROTOFORM` is available because low-vowel cells yield `wolf` while high-vowel cells yield umlauted forms such as `**wylfe`.

## Development-note summary

`wulf` is now a row where the project deliberately accepts mismatch rather than inventing a recoverable FST input. The broad early survey in `DEV_NOTES` treats OE `wulf` as part of the classic *u*-retention cluster beside `full`, `fugol`, `wull`, `bucca`, and `rust`, and it repeatedly stresses that the regular NWGmc/OE lowering rule is still right: `*wúlfaz` should give `wolf`, exactly as the FST and the OHG comparator do [@RingeTaylor2014, §2.3.1; @Campbell1959, §115]. The scholarly problem is not whether lowering existed, but why a small set of lexemes kept `u` anyway.

The early literature survey preserves the main handbook positions in usable form. Bülbring describes OE `u` appearing where `o` is expected, especially “namentlich zwischen Labial und langem oder gedecktem l”, explicitly including `wulf`, but he also concedes that “meist steht jedoch der Hauptregel gemäß o”; the same environment still yields regular lowered forms such as `folc` and `bolt` [@Bulbring1902, §116]. Luick therefore rejects a categorical phonological blocker and instead points to analogical or doublet-driven reshaping, while Ringe-Taylor call the relevant a-stem high-vowel cells too marginal to make paradigmatic levelling an attractive general solution [@Luick1914, §78 Anm. 3; @RingeTaylor2014, pp. 32-33]. Brunner likewise keeps `wulf` in the exception list near labials, not as the output of a clean sound law [@SieversBrunner1965, §68].

A later project phase tried to save strict Lautgesetzlichkeit by switching row 2298 away from nominative `*wúlfaz → wulf` and toward a high-vowel oblique cell such as gen.sg. `*wúlfis → wulfes`. That move is now explicitly superseded. The same high vowel that blocks *u*-lowering also triggers i-umlaut, so a form like `*wulfi` probes as `wylf`, not `wulf`; low-vowel cells still give `wolf`, high-vowel cells give `wylf/wylfe`, and no known paradigm cell yields attested bare `wulf` by regular sound change. The later rollback note treats the earlier retargeting as a regression, rereads Brunner’s `wulfi` discussion as analogical rather than generative, and restores row 2298 to documented-exception status [@SieversBrunner1965, §230 Anm.].

For this slice, the important distinction is therefore three-way. The live row state is current and should be cited as current policy. The broad exception survey is current contextual support for keeping `wulf` exceptional. The `*wúlfis → wulfes` plan is useful only as superseded project history showing a serious but rejected attempt to separate cognate-set headword from cell-specific FST input.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-63-166

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `lines 63-166`
- Status: `current`
- Issue tags: `u_lowering`; `known_exception`; `reconstruction_disagreement`; `literature_survey`
- Recommended use: `cite_in_final_report`
- Shared with row IDs: `2030`, `2162`, `2300`

This opening survey is still the best compact statement of the general exception problem surrounding `wulf`. It begins from the regular rule, not from the exception: stressed NWGmc/early-OE `*u` lowers to `o` before a following non-high vowel, so `*wulfăz` should develop to `wolf` [@RingeTaylor2014, §2.3.1]. The note then lists the stubborn OE counterexamples, including `*wulfăz → wulf (not ×wolf; OHG wolf)`, and makes clear that the project is not dealing with an isolated row-local oddity but with a broader lexical cluster.

The preserved literature detail matters for the final report. Bülbring’s formulation is carried over with its internal tension intact: OE `u` appears “namentlich zwischen Labial und langem oder gedecktem l”, including `wulf`, yet “meist steht jedoch der Hauptregel gemäß o”, so the same environments also produce lowered forms [@Bulbring1902, §116]. Luick’s response is equally important because it rules out turning the labial environment into a neat FST condition; he prefers paradigmatic or lexical explanations precisely because forms like `folc`, `folde`, and `bolt` show that labial/velar proximity does not reliably block lowering [@Luick1914, §78 Anm. 3]. Ringe-Taylor then press the same point from the opposite side: the exceptional forms are genuine, but the available a-stem high-vowel cells are too functionally marginal to explain everything, so “We do not really know why *u failed to lower in these forms” [@RingeTaylor2014, pp. 32-33].

The end of the survey supplies the current project decision: accept the regular rule, accept `wulf` as a lexical exception, and do not formalize a labial blocker merely because the exceptions cluster near labials. Brunner’s added formulation — “In einigen Wörtern steht, zumal in der Nachbarschaft von Labialen, statt des zu erwartenden o ein u” — is useful as corroboration, but the note explicitly treats it as observational support rather than a new categorical mechanism [@SieversBrunner1965, §68].

### DEV_NOTES:line-205-212

- Source heading: `NWGmc u-lowering Exceptions Near Labials`
- Source line or section hint: `lines 205-212`
- Status: `diagnostic_only`
- Issue tags: `u_lowering`; `transducer_limitation`; `worked_example`
- Recommended use: `use_as_project_history_only`
- Shared with row IDs:

The worked example for `*wulfaz` is short but still worth preserving because it shows the regular derivational path in the barest possible form. The note parses `*w*u*l*f*a*z`, observes that the following `*l*f*a` environment matches the lowering rule, and states the result plainly: `*u → *o → wolf`.

For row 2298 this is not a competing analysis, only a diagnostic reminder of what the current FST already gets right. The fragment is useful when explaining why the row remains `unexplained_unmodelled`: the system’s failure is not inability to model the regular law, but inability to derive the attested exception without contradicting the law.

### DEV_NOTES:line-25940-26067

- Source heading: `attempted paradigm-cell rescue for the u-lowering exception cluster`
- Source line or section hint: `lines 25940-26067`
- Status: `superseded`
- Issue tags: `paradigm_cell`; `protoform_vs_proto`; `source_conflict`; `project_history`
- Recommended use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2030`, `2162`

This section matters because it records the strongest abandoned attempt to repair `wulf` without changing the sound laws. Its source audit is partly still useful. Stiles is quoted for the basic environment split, Campbell §115 is quoted for the explicit exception status of `wulf`, and Brunner is quoted for the fact that oblique cells with following high vowel preserve `u`; the note even preserves the crucial Brunner wording on instrumental `wulfe aus wulfi`, with the warning that “der i-Umlaut ist in der Regel nach den anderen Kasus aufgegeben” [@Campbell1959, §§115-116; @SieversBrunner1965, §§68, 239]. Those citations remain relevant background.

What is superseded is the decision drawn from them. After correctly observing that low-vowel cells give `wolf` and that high-vowel cells preserve `u`, the section proposed shifting row 2298 from nom.sg. `*wúlfaz → wulf` to gen.sg. `*wúlfis → wulfes` as the regular, row-level target. That move no longer represents current policy. In retrospect the section underweighted Brunner’s own caveat that the attested `wulfe` cell is itself analogically levelled and therefore cannot simply be used as a clean generative source for the whole paradigm.

Use this fragment only when explaining project chronology: it shows why the team briefly considered separating `PROTO` and `PROTOFORM`, but it should not be cited as the present solution for row 2298.

### DEV_NOTES:line-26126-26197

- Source heading: `rollback of the paradigm-cell switch; documented-exception status restored`
- Source line or section hint: `lines 26126-26197`
- Status: `current`
- Issue tags: `paradigm_cell`; `i_umlaut`; `u_lowering`; `row_policy`
- Recommended use: `cite_in_final_report`
- Shared with row IDs:

This revision is the decisive current fragment for `wulf`. It records the failed implementation of the `*-is` retargeting plan, then gives the probe that broke it: `echo wúlfi | flookup -i old_english.bin` returns `wylf`, not `wulf`. The note interprets that result correctly. A following high vowel can block *u*-lowering, but the same high vowel then triggers i-umlaut before heavy-syllable i-apocope removes it, so the chain is still fully regular — just regular toward the wrong answer.

The section then states the row-level conclusion in exactly the form needed for this slice. Every possible paradigm cell falls into one of two bad buckets: low-vowel cells yield `wolf`; high-vowel cells yield `wylf`, `wylfe`, or comparable fronted outcomes. “There is no PGmc/NWGmc paradigm cell from which attested `wulf` ... can be derived by regular sound change.” That conclusion is then aligned with Brunner’s own statement that the i-umlaut in `wulfi`-type forms “ist in der Regel nach den anderen Kasus aufgegeben”, i.e. the attested oblique forms are already analogical and cannot rescue the nominative [@SieversBrunner1965, §230 Anm.].

For current work, this is the fragment that supersedes the earlier genitive-retargeting plan. It also sharpens the project claim from “lexical exception” to something more specific: `wulf` is not merely irregular because nominative `*wúlfaz` lowers to `wolf`; it is doubly resistant because the obvious high-vowel escape cells overshoot into i-umlaut as well. That is why the live TSV note now says that no lautgesetzlich `PROTOFORM` is available.

## Superseded or diagnostic material

The old `*wúlfis → wulfes` proposal should stay visible in this slice because packet-style evidence gathering can still surface it, and because it records a real methodological experiment with paradigm-cell retargeting. But the later correction is the controlling note: once `wúlfi → wylf` was actually probed, the earlier plan ceased to be a live option.

The short worked example is also worth keeping, but only as a diagnostic anchor for the regular comparator `wolf`. It should not be mistaken for a recommendation to change the row.

## Open questions for later work

- Decide whether the final lexeme report should quote Brunner’s `wulfe aus wulfi` line directly when explaining why attested oblique `wulfe` does not validate a regular `*wulfi` source.
- Decide whether the final report should foreground the handbook consensus (`Campbell`, `Luick`, `Ringe-Taylor`, `Brunner`) or the repo-specific `wúlfi → wylf` probe first.
- Check whether the final report should cite the live TSV note’s “doubly irregular” formulation verbatim.
