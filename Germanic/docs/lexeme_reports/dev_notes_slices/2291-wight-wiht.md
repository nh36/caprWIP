---
row_id: 2291
concept: wight
counterpart: wiht
proto: *wéxtiz
protoform: *wéxtiz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2291 wight / wiht

## Current row state

- The live OE row is a regular exact-match row: `CONCEPT = wight`, `COUNTERPART = wiht`, `PROTO = *wéxtiz`, `PROTOFORM = *wéxtiz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1400-1400].
- `old_english_wiktionary.tsv` independently gives the same pair `wight | wiht`, so the row's basic lexeme identity is secure even though no row-specific packet, research memo, pilot file, or clearly row-specific analysis file was found during this pass [Germanic/data/old_english_wiktionary.tsv:348-348].
- `coverage_audit.md` classifies row `2291` as a regular row with no pre-existing report requirement (`Requirement basis = none`), which means this slice is replacement working documentation rather than continuation of an older required-report chain [Germanic/docs/lexeme_reports/coverage_audit.md:415-415].
- The published derivation trace is currently exact and gives the project's working stage sequence explicitly: `Proto Input: *wéxtiz`, `OE Breaking: *wéoxti`, `OE I Umlaut: *wíexti`, `OE Ws Palatal Umlaut: *wixti`, `OE High Vowel Apocope: *wixt`, `Old English Orthography: *wiht`, `Outcome: wiht` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5904-5924].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so this row is **not** presently using a substitute paradigm cell or analogical rescue input. `PROTO = *wéxtiz` is the comparative/project label, `PROTOFORM = *wéxtiz` is the actual FST input in current practice, and the OE-side target is normalized `wiht` [Germanic/data/germanic-aligned-final.tsv:1400-1400; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5904-5924].
- Comparative references make the lexical distinction that later work must keep explicit. Orel splits `*wextiz I` “thing” from `*wextiz II` “weight,” and Kroonen likewise distinguishes `*wehti- 1` “thing” from `*wehti- 2` “weight”; the current row's `CONCEPT = wight` therefore belongs with the “being / thing” lexeme, not with the separate weight noun, even though OE `wiht` can surface in both semantic areas [docs/references/orel_handbook_germanic_etymology.vision.txt:49880-49907; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29281-29292; @Orel2003; @Kroonen2013].
- OE reference works point the same way. Clark Hall glosses `wiht I` as “'wight,' person, creature, being ... thing” and separately lists `wiht III` as “'weight,'” while Sweet likewise gives `wiht, sf. wight, creature, thing` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48468-48472; docs/references/sweet_anglo_saxon_primer.txt:6892-6894; @ClarkHall1960; @Sweet1953].

## Development-note summary

No dedicated row-2291 dossier currently survives in `DEV_NOTES.md`. The attachable DEV_NOTES evidence is thin, shared, and mostly diagnostic in purpose: a later `*x`-loss audit explicitly lists `2291 *wéxtiz -> wiht` among the preserved `*xt` rows, Campbell's quoted §464 statement explains why inherited `*xt` remains in Old English, and a still later contraction-risk audit records that `*wéxtiz` was checked and found outside the new `*x + vowel` environment [Germanic/docs/DEV_NOTES.md:39045-39056,39278-39288,42450-42455,42633-42638]. This slice therefore replaces missing row-local notes with the strongest current shared material rather than pretending that a bespoke `wiht` analysis still exists.

The row nevertheless has a clear present interpretation. `PROTO = *wéxtiz` and `PROTOFORM = *wéxtiz` coincide, so the project is not distinguishing a lexeme-level headword from a special OE-facing inflectional input here [Germanic/data/germanic-aligned-final.tsv:1400-1400]. `COUNTERPART = wiht` is the selected Old English outcome, and the live derivation trace shows that the current cascade reaches that form by ordinary breaking, i-umlaut, West-Saxon palatal umlaut, high-vowel apocope, and final orthographic `xt > ht` spelling [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5911-5924]. In other words, the row is currently a stable regular control case, not a repair row.

Primary-source support helps keep the summary from becoming too schematic. Campbell's palatal-umlaut discussion states: “In eW-S we already find `cniht ... Wikt Wight, wiht creature`” [docs/references/campbell_old_english_grammar.txt:8763-8765; @Campbell1959, §305]. That matters because DEV_NOTES itself does **not** preserve a row-specific `wiht` quotation, yet Campbell confirms that `wiht` belongs in the same early West-Saxon `eo/io > i` before `ht` cohort as other familiar `-iht` words. The live project trace `*wéoxti -> *wíexti -> *wixti -> wiht` is therefore not only internally exact but also directionally consistent with handbook phonology [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5917-5924; docs/references/campbell_old_english_grammar.txt:8763-8780].

The main caution is lexical ambiguity, not sound-law instability. OE `wiht` can denote both “wight / creature / thing” and “weight,” and Campbell's Kentish note includes `wiht weight`, not the animate or indefinite-pronominal lexeme [docs/references/campbell_old_english_grammar.txt:8779-8780; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48468-48472]. For row 2291, the concept label, OE Wiktionary row, and comparative dictionaries all favor the “thing / being” branch [Germanic/data/germanic-aligned-final.tsv:1400-1400; Germanic/data/old_english_wiktionary.tsv:348-348; docs/references/orel_handbook_germanic_etymology.vision.txt:49880-49907; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29281-29292]. Later reporting should therefore resist citing generic `wiht` hits as if they automatically belonged to this row; some belong to the distinct weight noun, and some belong to compounds such as `nāwiht` rather than the simplex lexeme [docs/references/fulk_comparative_grammar_early_germanic.vision.txt:12826-12829; @Fulk2018].

The safest replacement note is accordingly conservative. Current DEV_NOTES authority does support the row's **regular** status and does give one usable row-explicit anchor, but it does **not** preserve a rich row-local narrative. The slice should therefore be read as a control-case note: `*wéxtiz -> wiht` is one of the live preserved-`*xt` witnesses, its OE target is consistent with handbook `wiht creature`, and later audit prose mainly records that subsequent `*x`-rule work was designed not to break it [Germanic/docs/DEV_NOTES.md:39278-39288,42450-42455,42633-42638; docs/references/campbell_old_english_grammar.txt:8763-8765,12049-12061; @Campbell1959, §§305, 464].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39278-39288

- Source heading: `Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39278-39288`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `xt_cluster`; `preconsonantal_x_loss`; `control_case`; `preserved_ht`
- Recommended next use: `cite_if_explaining_why_row_stays_regular`
- Shared with row IDs: `2010`, `2086`, `2102`, `2125`, `2140`

This is the strongest surviving row-explicit DEV_NOTES attachment. DEV_NOTES lists `2291 *wéxtiz -> wiht` inside the preserved `*xt` cohort and immediately states the conditioning: “These have *x followed by a single *t plus a vowel — the rule's two-consonant right context is not satisfied, so loss does not fire (correctly)” [Germanic/docs/DEV_NOTES.md:39278-39288]. For row 2291 that is the current project-policy sentence to quote. It shows that `wiht` is not merely tolerated by the present cascade; it is one of the rows actively used to verify that preconsonantal `*x`-loss has **not** been overgeneralized.

### DEV_NOTES:line-39045-39056

- Source heading: `Campbell §464` quoted inside the later `*x`-loss audit
- Source line or section hint: `lines 39045-39056`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `campbell`; `xt_preservation`; `shared_rule_scope`; `h_group_history`
- Recommended next use: `cite_as_shared_rule_authority`
- Shared with row IDs: `2010`, `2086`, `2102`, `2125`, `2140`

This fragment does not name `wiht`, so it should not be oversold as a dedicated row note. It is still the main DEV_NOTES source audit behind the preserved-`*xt` bucket. DEV_NOTES quotes Campbell: “the only group in which x was followed by a voiceless consonant in Prim. OE was `xt`, and this group remained, e.g. ... `miht` ... `niht` ...” [Germanic/docs/DEV_NOTES.md:39045-39056; docs/references/campbell_old_english_grammar.txt:12049-12061; @Campbell1959, §464]. For row 2291 the value is methodological: the row-specific list at lines `39278-39288` is grounded in a handbook rule that inherited `*xt` survives. This fragment should therefore be cited as shared rule authority, not as direct lexical attestation of `wiht`.

### DEV_NOTES:line-42450-42455 and line-42633-42638

- Source heading: `Risk audit` / `Lexicon audit`
- Source line or section hint: `lines 42450-42455; 42633-42638`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `contraction_guardrail`; `collateral_check`; `x_plus_c`; `unaffected_row`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `2010`, `2086`, `2194`

These later notes come from the `ten / tīen` contraction repair, not from a `wiht` investigation. Even so, they name the row's lexical environment in current form. DEV_NOTES says the audit searched all `*[eé]x` rows with back-vowel continuations and concluded that `*wéxtiz`, like `*séxs`, `*féxtaną`, and `*knéxtaz`, has `*x + C`, not `*x + V`, and is therefore unaffected by the new contraction clauses [Germanic/docs/DEV_NOTES.md:42450-42455,42633-42638]. This is useful as project history because it shows that later rule work explicitly checked row 2291 for collateral damage. It is not central philological evidence for why `*wéxtiz` yields `wiht`.

## Superseded or diagnostic material

- No row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file was found for row `2291`; the blank linkage fields above are therefore a real evidence-state report, not an omission in this slice [Germanic/data/germanic-aligned-final.tsv:1400-1400; Germanic/docs/lexeme_reports/coverage_audit.md:415-415].
- The chief interpretive hazard is semantic collapse of two different lexical families. Clark Hall, Orel, and Kroonen all distinguish the `wiht` “thing / creature” lexeme from the separate `wiht` “weight” noun, so later reuse of generic `wiht` citations must be filtered carefully [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48468-48472; docs/references/orel_handbook_germanic_etymology.vision.txt:49880-49907; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29281-29292; @ClarkHall1960; @Orel2003; @Kroonen2013].
- Compounds such as `nāwiht`, `nāuht`, and `nāht` are relevant for the broader history of the lexeme family, but they are not direct authority that the simplex row should be reinterpreted or re-glossed. Fulk's discussion is useful background on the family, not a row-local replacement for the live `wight / wiht` entry [docs/references/fulk_comparative_grammar_early_germanic.vision.txt:12826-12829; @Fulk2018].
- The later contraction-risk audit is diagnostic-only. Preserve it as proof that row `2291` was checked against overgeneration, not as the main reason to trust the row [Germanic/docs/DEV_NOTES.md:42450-42455,42633-42638].

## Open questions for later work

- If a final report is ever written, decide whether to normalize the proto citation explicitly as project `*wéxtiz` versus handbook `*wextiz` / `*wehti- 1`, since the lexical equation is plausible but the notation difference is easy to misread as a stage difference [Germanic/data/germanic-aligned-final.tsv:1400-1400; docs/references/orel_handbook_germanic_etymology.vision.txt:49880-49907; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29281-29292; @Orel2003; @Kroonen2013].
- If later reporting needs richer OE philology, add a short note distinguishing simplex `wiht` from compounds such as `nāwiht`, and from the separate weight noun, so the row's concept label `wight` is not blurred by dictionary homography [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48468-48472; docs/references/fulk_comparative_grammar_early_germanic.vision.txt:12826-12829; @ClarkHall1960; @Fulk2018].
- If `index.tsv` is revisited later, decide whether a shared control fragment such as `DEV_NOTES:line-39278-39288` is strong enough to index. It is row-explicit and current, but it is still a verification list rather than a rich row-specific dossier [Germanic/docs/DEV_NOTES.md:39278-39288].
