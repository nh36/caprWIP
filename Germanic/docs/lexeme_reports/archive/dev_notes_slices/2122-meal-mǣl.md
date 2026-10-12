---
row_id: 2122
concept: meal
counterpart: mǣl
proto: "*mḗlą"
protoform: "*mḗlą"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: no_row_specific_dev_notes_survive; current_derivation_matches
needs_literature_agent: no
---

# DEV_NOTES material — 2122 meal / mǣl

## Current row state

- The live Old English row is stable and internally simple: `ID 2122 | CONCEPT meal | COUNTERPART mǣl | PROTO *mḗlą | PROTOFORM *mḗlą | DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:743-745]. For this row, `PROTO` and `PROTOFORM` are identical project inputs; the attested/target OE form is the separate field `COUNTERPART` `mǣl` [Germanic/data/germanic-aligned-final.tsv:745-745].
- Coverage infrastructure treats the row as uncovered and non-report-bearing: `coverage_audit.md` lists `| 2122 | meal | mǣl | regular | no | - | - | - | none |`, and the research-memo index jumps from row `2120` to row `2126`, with no indexed packet or memo for `2122` [Germanic/docs/lexeme_reports/coverage_audit.md:303-309; Germanic/docs/lexeme_reports/research_memo_index.tsv:58-64].
- `oe_known_problems.tsv` contains only the current exception buckets for other protoforms; `*mḗlą` is absent, which is consistent with the row's present `regular` status [Germanic/data/oe_known_problems.tsv:1-8].
- The current OE derivation snapshot already lands exactly on the live target: `PROTO: *mḗlą`, `EXPECTED: mǣl`, `OUTPUTS: mǣl`, with the row-specific path `NWGmc Long E Lowering: *mǣlą` then `OE Heavy Syllable Nasal Apocope: *mǣl`, ending in `Outcome: mǣl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3164-3183].
- Repo-local lexical reference material supports the lexical identity of the row, though usually under comparative headword notation rather than the project's accented `*mḗlą`. Kroonen's entry `*mēla- 1 n. 'point in time'` includes `OE mal n. 'moment; meal'`, and Ringe-Taylor gives `PGmc *méla '(a) time' ... > WS OE mé@l`; Clark Hall likewise glosses `mæl ... time, point of time ... time for eating, 'meal,' meals` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19119; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26982-26985].
- The local OE lexeme lookup also aligns English `meal` with OE `mǣl`, not with a flour-word `melu`: `old_english_wiktionary.tsv` has `meal    mǣl    inh    template:inh    meal` [Germanic/data/old_english_wiktionary.tsv:180-184].

## Development-note summary

No row-specific DEV_NOTES block for `meal / mǣl / *mḗlą` appears to survive. The slice therefore has to say so plainly and build from two narrower supports: (1) the live row plus current successful derivation trace, which is row-specific and current, and (2) shared DEV_NOTES material on final-vowel loss after heavy syllables, which is relevant to the mechanics of `*mḗlą > mǣl` but not written as a dedicated `meal` note [Germanic/data/germanic-aligned-final.tsv:745-745; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3164-3183; Germanic/docs/DEV_NOTES.md:1591-1645,18624-18710].

The single most important project point to preserve is that the current pipeline now derives the row without repair by deleting final `*-ą` after a heavy stem. DEV_NOTES records that this was originally an empirical discovery rather than a directly inherited handbook rule: `"Neither source explicitly extends this pattern to *-ą"`, but `"The same heavy/light conditioning that applied to *-i/*-u also applied to *-ą"` in the model's successful generalization [Germanic/docs/DEV_NOTES.md:1604-1615]. For row `2122`, that is exactly the operative step seen in the live trace: `*mǣlą -> *mǣl` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3173-3183].

Support should therefore be classified conservatively. The lexical identification of `mǣl` as the OE target of the `*mēla-/*méla` family is row-specific current-state support from the TSV and repo reference corpus [Germanic/data/germanic-aligned-final.tsv:745-745; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19119; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861]. The heavy-syllable apocope discussion in DEV_NOTES is shared-background-only but still directly relevant to the rule application. Older mismatch lists that showed `*mēlą -> mēla (exp. mǣl)` are diagnostic, not current authority, because the present trace already resolves that older failure [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:271-302; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3164-3183].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-1591-1645
- Source heading: `Archived: Heavy Syllable Nasal Apocope (2026-02-06) — EMPIRICAL DISCOVERY`
- Source line hint: `Germanic/docs/DEV_NOTES.md:1591-1645`
- Fragment type: shared_background_rule_note_with_direct_row_consequence
- Status: current_for_rule; archived_as_discovery_note
- Issue tags: heavy_syllable_nasal_apocope; final_-ą_loss; regular_row; no_row_specific_block
- Recommended next use: cite_when_explaining_why_final_-ą_drops_in_*mḗlą
- Shared-with rows if relevant: broad heavy-stem `*-ą` rows; diagnostic list explicitly included the pre-fix meal case

This is the main surviving DEV_NOTES material that actually bears on row `2122`, even though it is not a `meal` dossier. DEV_NOTES records: `"Implemented experimental rule deleting proto *-ą after heavy syllables"`, calls the result an `"empirically-derived phonological finding"`, and states the key limitation honestly: `"Neither source explicitly extends this pattern to *-ą"` [Germanic/docs/DEV_NOTES.md:1595-1597,1604-1608]. The passage then gives the project's interpretive claim in exactly the form later workers need to preserve: `"The same heavy/light conditioning that applied to *-i/*-u also applied to *-ą"`, even though that extension had to be inferred from the mismatch inventory rather than copied straight from a handbook [Germanic/docs/DEV_NOTES.md:1609-1615].

For row `2122`, this fragment is not just general background; it is the specific rule family that turns project `PROTO/PROTOFORM` `*mḗlą` into target OE `mǣl`. The live derivation trace now shows precisely that: `NWGmc Long E Lowering: *mǣlą`, then `OE Heavy Syllable Nasal Apocope: *mǣl`, with no extra workaround [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3171-3183]. The older analysis file makes the before/after diagnostic explicit by listing `*mēlą → mēla (exp. mǣl)` among the former `final_vowel_extra` cases [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:275-302]. That older file is not DEV_NOTES authority, but it shows why this shared DEV_NOTES rule note matters so directly for `meal / mǣl`.

### DEV_NOTES:line-18624-18710
- Source heading: `§15.1: Two Distinct Stages of High Vowel Apocope` and `§15.3: Luick §304 — Later Pre-OE Apocope (Different Rule!)`
- Source line hint: `Germanic/docs/DEV_NOTES.md:18624-18710`
- Fragment type: shared_chronological_background
- Status: current_shared_background_only
- Issue tags: apocope_chronology; heavy_stressed_syllable; indirect_support_for_-ą_extension
- Recommended next use: cite_only_for_chronology_or_scope_control
- Shared-with rows if relevant: rows whose successful derivation depends on late apocope after heavy stressed syllables

This fragment does not mention `meal`, and it does **not** directly prove the loss of final `*-ą`; that distinction should stay explicit. What it does preserve is the project's chronology for the apocope environment into which row `2122` was later fitted. DEV_NOTES says there were `"two chronologically distinct apocope processes"`, then quotes Brunner on the later one: `"Nach betonten Silben ... i und u ... wurden dann im Ae. zum Teil apokopiert"`, translated in the note as original final `i` and `u` being partly lost in Pre-OE after stressed syllables [Germanic/docs/DEV_NOTES.md:18626-18631,18649-18657]. Luick's formulation is copied even more compactly: `"Im Auslaut schwanden i und u unmittelbar nach langer Tonsilbe"`, i.e. final `i/u` were lost immediately after a long stressed syllable [Germanic/docs/DEV_NOTES.md:18696-18710].

For `2122`, the right use of this fragment is background-only. It explains why the project was already thinking in terms of a late heavy-syllable apocope window, but DEV_NOTES itself distinguishes that inherited handbook evidence (about `i/u`) from the project's further empirical extension to `*-ą` in the archived heavy-syllable nasal-apocope note [Germanic/docs/DEV_NOTES.md:1604-1615,18624-18710]. In other words: useful chronology, but not a hidden row-specific proof text.

## Superseded or diagnostic material

- The older apocope investigation preserves the row in its pre-fix failure state as `*mēlą → mēla (exp. mǣl)` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:275-302]. That is diagnostically valuable because it shows why the final-vowel-loss rule mattered, but it is superseded by the current derivation snapshot, which now reaches `mǣl` directly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:3164-3183].
- No row-specific mismatch bucket, packet, memo, or manifest entry currently survives for `2122`; that absence is part of the present state, not an omission in this slice [Germanic/data/oe_known_problems.tsv:1-8; Germanic/docs/lexeme_reports/coverage_audit.md:303-309; Germanic/docs/lexeme_reports/research_memo_index.tsv:58-64; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- Comparative lexicographic support for the lexeme is solid, but it is not project-internal DEV_NOTES authority. Kroonen and Ringe-Taylor cite comparative headwords `*mēla-` / `*méla`, whereas the live row's project-facing `PROTO` and `PROTOFORM` are both `*mḗlą`; those sources support lexical identity and broad development, not the exact local notation choice [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19119; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861; Germanic/data/germanic-aligned-final.tsv:745-745].

## Open questions for later work

- If later lexeme-report curation wants fuller infrastructure for regular uncovered rows, decide whether `2122` needs a packet/memo at all; current evidence points to a stable control row rather than an unresolved problem case [Germanic/docs/lexeme_reports/coverage_audit.md:303-309; Germanic/data/oe_known_problems.tsv:1-8].
- If project documentation later standardizes how comparative headwords are quoted in slices, decide whether to normalize the reference-facing `*mēla-/*méla` citations more explicitly against the row's project `PROTO`/`PROTOFORM` `*mḗlą`, while keeping the distinction visible [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:19115-19119; docs/references/ringe_taylor_linguistic_history_vol2.txt:13859-13861].
- If the repository later retires legacy `meal/melu` bookkeeping elsewhere, ensure that flour-word material is not reattached to this row. The live `2122` evidence consistently points to OE `mǣl` as the target here [Germanic/data/germanic-aligned-final.tsv:745-745; Germanic/data/old_english_wiktionary.tsv:180-184; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26982-26985].
