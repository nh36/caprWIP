---
row_id: 2267
concept: wain
counterpart: wæġn
proto: *wágnaz
protoform: *wágnaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2267 wain / wæġn

## Current row state

- The live OE row reads `CONCEPT = wain`, `COUNTERPART = wæġn`, `PROTO = *wágnaz`, `PROTOFORM = *wágnaz`, `DERIVATION_CLASS = regular`. Its source-note field is still just duplicated Wiktionary inheritance provenance rather than a lexeme-specific explanation [Germanic/data/germanic-aligned-final.tsv:1307-1307].
- `PROTO`, `PROTOFORM`, and `COUNTERPART` need to be kept distinct even though the first two currently coincide. In this row, `PROTO = *wágnaz` is the project's comparative PGmc label for the cognate set, `PROTOFORM = *wágnaz` is also the exact nominative-singular input presently fed into the OE derivation, and `COUNTERPART = wæġn` is the attested OE surface target. Dictionary-style stem citations such as Kroonen's `*wagna-` are therefore comparable evidence, but they are not the same field value as the row's nominative-singular `PROTOFORM` [Germanic/data/germanic-aligned-final.tsv:1307-1307; @Kroonen2013].
- The non-DEV_NOTES lexical support is straightforward. `old_english_wiktionary.tsv` gives `wain → wæġn`, Clark Hall glosses `wægn (wægen, wān) m. carriage, 'wain,' waggon, chariot, cart, vehicle`, and Kroonen reconstructs PGmc `*wagna- m. 'wagon'` with OE `wægn, wægen` among the reflexes [Germanic/data/old_english_wiktionary.tsv:326-326; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46543-46545; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28675-28679].
- The current derivational snapshot is also clean. The published OE trace report derives `*wágnaz` to `wæġn` via `PGmc Final Z Deletion: *wágna`, `PWGmc Final Bare A Loss: *wágn`, `Anglo Frisian Brightening: *wægn`, and `OE Velar Palatalization: *wæʤn`, then spells the output as `wæġn` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5519-5539].
- No row-specific packet, research memo, or pilot file was found during slice preparation, and no clearly row-specific analysis/dossier file outside DEV_NOTES was found either.

## Development-note summary

The live row presently looks **regular and stable**, but the surviving DEV_NOTES material is thin and mostly diagnostic rather than lexeme-dedicated. The clearest positive evidence for the row comes from the combination of the live TSV state, the generated derivation trace, and standard reference works: PGmc wagon `*wagna-` / row input `*wágnaz` yields OE `wæġn`, exactly the form listed in the lexical sources and exactly the output produced by the current pipeline [Germanic/data/germanic-aligned-final.tsv:1307-1307; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5519-5539; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46543-46545; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28675-28679].

The phonological path reflected in the trace is ordinary and should be stated explicitly. In the current model, final `-z` is lost first, then final bare `-a` is lost, so the form reaches OE pre-fronting as `*wágn` rather than as a stem still followed by a back-vowel ending [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5528-5533]. That matters because Anglo-Frisian fronting / brightening can then produce `*wægn`, while the later palatalization rule turns preconsonantal `g` after a front vowel into palatal `ġ`: Ringe-Taylor state that “preconsonantal and word-final *g were palatalized by any preceding front vowel,” and Campbell notes specifically that in the `ae` plus `ng` environment “the g and ċ were palatalized” [docs/references/ringe_taylor_linguistic_history_vol2.txt:11708-11730; @RingeTaylor2014, §§6.3.1, 6.4.1; docs/references/campbell_old_english_grammar.txt:2744-2747; @Campbell1959, §62]. The row's `COUNTERPART = wæġn` is therefore the expected OE outcome of a fronted and then palatalized nominative singular, not an exceptional spelling.

The distinction among the row fields is important because the reference literature and the project TSV encode slightly different kinds of proto labels. Kroonen's lemma is stem-level `*wagna- m. 'wagon'`, whereas the row uses accented nominative singular `*wágnaz` in both `PROTO` and `PROTOFORM` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28675-28679; Germanic/data/germanic-aligned-final.tsv:1307-1307]. That does **not** mean the row is internally confused. It means the project currently uses the same nominative-singular string both as comparative row label and as derivational input. `COUNTERPART`, by contrast, is not a reconstruction at all: it is the attested OE noun `wæġn` as reflected in the lexical sources [Germanic/data/old_english_wiktionary.tsv:326-326; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46543-46545]. Any later documentation should preserve that three-way distinction instead of flattening everything into a single “proto equals output” shorthand.

The genuinely row-specific DEV_NOTES evidence is almost entirely **negative history**. The only place the lexeme is named directly in current searches is the March regression block created when `{*ă}` was experimentally added to the A-restoration trigger environment. There DEV_NOTES records `wagnăz → wagn (should be wæġn) - REGRESSED`, and the summary line lists `wain` among the nine regressions caused by that change [Germanic/docs/DEV_NOTES.md:9524-9539]. This is useful evidence, but only as superseded diagnostics: it shows that broadening the trigger set incorrectly de-fronted nouns that should remain fronted. It is **not** evidence that the row itself is doubtful.

The current shared policy note in `§17.10.11` explains why that failed experiment matters beyond the individual row. DEV_NOTES explicitly says the assumption behind a bulk breve/plain migration was “wrong” because the distinction is doing “real phonological work,” and the decisive sentence for future reuse is that `OEARestorationTriggerVowel ... includes {*a} but not {*ă}` [Germanic/docs/DEV_NOTES.md:21731-21749]. That section is written around Class VI infinitives, not `wæġn`, so it should not be indexed as a lexeme-specific anchor by itself. But it does provide the current explanatory backdrop for why the regression line `wagnăz → wagn` was indeed a regression: once reduced weak-tail vowels are allowed to trigger restoration, nouns like `wæġn` lose the fronting they are supposed to preserve.

The older February A-restoration fix note is also shared rather than row-local, but it helps interpret the `wain` regression conservatively. That note records that `{*ă}` and `{*ą}` were removed from the back-vowel trigger set, and later notes continue to defend that restriction as current policy [Germanic/docs/DEV_NOTES.md:1658-1663,21731-21749]. For row 2267, the documentary takeaway is therefore narrow and stable: the live row is a regular fronted noun with correct current output; the DEV_NOTES trail is mostly a warning against overgeneralized A-restoration fixes, not a dedicated dossier arguing over the lexeme itself.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-9524-9539

- Source heading: `BUT: SIGNIFICANT REGRESSIONS OBSERVED!`
- Source line or section hint: `lines 9524-9539`
- Status: `superseded_but_row_specific`
- Issue tags: `a_restoration_overreach`; `fronting_regression`; `wagn_named`
- Recommended next use: `preserve_as_diagnostic_history`
- Shared with row IDs: `2055`; `2090`; `2118`; `2213`; `2256`; `2293`; other fronting-sensitive noun rows in the same regression list

This is the only clearly lexeme-addressable DEV_NOTES anchor now visible for row 2267. It names the failing probe directly: `wagnăz → wagn (should be wæġn) - REGRESSED`, then includes `wain` in the regression summary [Germanic/docs/DEV_NOTES.md:9531-9539]. The fragment is valuable because it captures the exact failure mode: adding `{*ă}` to the trigger set restores root `a` where the noun should have stayed fronted as `æ`. It should nevertheless be cited only as **superseded diagnostics**, because the experiment was explicitly judged worse overall and the live row no longer uses that setting.

### DEV_NOTES:line-21729-21755

- Source heading: `§17.10.11 — Phase 1d (Role 1) research findings: breve is NOT an engineering tag; rescope`
- Source line or section hint: `lines 21729-21755`
- Status: `current_but_shared`
- Issue tags: `current_trigger_policy`; `breve_vs_plain`; `a_restoration_scope`
- Recommended next use: `cite_as_shared_policy_background`
- Shared with row IDs: `1934`; `2046`; `2055`; `2266`; `2268`; `2272`; `2292`; many other A-restoration rows

This fragment is the clearest current-policy statement behind the regression history, even though it does not name `wæġn`. DEV_NOTES says the earlier assumption was “wrong” because breve versus plain vowel notation is doing “real phonological work,” and it states of the trigger set that it “includes `{*a}` but not `{*ă}`” [Germanic/docs/DEV_NOTES.md:21731-21749]. For row 2267, that shared statement explains why the experimental `wagnăz` output was false: a reduced weak-tail vowel must **not** count as the sort of back-vowel context that would undo fronting in this noun. This is strong technical background, but only weak lexeme-specific indexing evidence.

### DEV_NOTES:line-1649-1663

- Source heading: `A-Restoration Fix (2026-02-06)`
- Source line or section hint: `lines 1649-1663`
- Status: `current_but_shared`
- Issue tags: `trigger_set_restriction`; `chronology_fix`; `shared_background`
- Recommended next use: `cite_when_explaining_trigger_history`
- Shared with row IDs: many OE rows affected by A-restoration debugging

This earlier shared fragment records the technical repair that later underlies the `wain` regression discussion. DEV_NOTES says the fix removed `{*ă}` and `{*ą}` from the A-restoration back-vowel trigger set and moved apocope after restoration in the chronology [Germanic/docs/DEV_NOTES.md:1658-1663]. The note is not row-local and predates the later rescope, but it helps show that the project repeatedly learned the same lesson from different angles: reduced weak-tail vowels are dangerous triggers, and loosening that part of the system causes false restorations in nouns whose expected OE outputs remain fronted.

## Superseded or diagnostic material

- The main superseded material is the `wagnăz → wagn` regression produced by over-broad A-restoration triggering. It is important to preserve because it names the row directly, but it should be labeled as failed diagnostics rather than as support for changing the live row [Germanic/docs/DEV_NOTES.md:9531-9539].
- The shared trigger-policy notes are current, but they are not lexeme dossiers. For this row they explain the mechanics of the regression history; they do not independently argue for a different counterpart than `wæġn` [Germanic/docs/DEV_NOTES.md:1658-1663,21731-21749].
- The current debug snapshot is stronger than the direct DEV_NOTES evidence for positive support. It shows the live pipeline deriving `wæġn` correctly from `*wágnaz`, so later work should not let the superseded regression block overshadow the present-state derivation [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5519-5539].

## Open questions for later work

- If a later full report is written, it may be worth citing whether the final report should normalize the comparative label to Kroonen-style stem citation `*wagna-` while keeping the row's derivational `PROTOFORM = *wágnaz`. The present slice should keep both values distinct rather than silently harmonizing them [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28675-28679; Germanic/data/germanic-aligned-final.tsv:1307-1307].
- If `index.tsv` is revisited later, treat the row cautiously. The strongest lexeme-addressable DEV_NOTES line is the superseded regression block `9524-9539`; the strongest current-policy lines are shared A-restoration notes, especially `21729-21755`, not a dedicated `wain` memorandum.
- If future debugging ever reopens fronting versus restoration interactions for nouns in `-az`, the published derivation trace for `*wágnaz` should be reused as the baseline control case because it already shows the intended chronology in one compact line: final-vowel loss, brightening, then velar palatalization to `wæġn` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5528-5539].
