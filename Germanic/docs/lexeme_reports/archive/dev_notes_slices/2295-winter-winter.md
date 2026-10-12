---
row_id: 2295
concept: winter
counterpart: winter
proto: *wíntruz
protoform: *wíntruz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2295 winter / winter

## Current row state

- The live TSV row reads `CONCEPT = winter`, `COUNTERPART = winter`, `PROTO = *wíntruz`, `PROTOFORM = *wíntruz`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1416-1416].
- The source-note field is still only the duplicated inherited placeholder `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)`. That placeholder is not the actual documentary basis for the row's present `regular` status [Germanic/data/germanic-aligned-final.tsv:1416-1416].
- No row-specific packet, research memo, pilot file, or other clearly row-addressed lexeme-report support file was found under `Germanic/docs/lexeme_reports/`; the coverage audit still records row 2295 as `none` [Germanic/docs/lexeme_reports/coverage_audit.md:417-417].
- The current published derivation snapshot already matches the live row exactly: `PROTO: *wíntruz`, `EXPECTED: winter`, `OUTPUTS: winter`, with the compact late path `PGmc Final Z Deletion: *wíntru`, `OE High Vowel Apocope: *wíntr`, `OE Epenthetic Vowel: *wínter`, then surface `winter` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5985-6004].
- `PROTO` and `PROTOFORM` are identical in the TSV for this row, but the labels should still be distinguished. `PROTO = *wíntruz` is the comparative Germanic headword the row publishes; `PROTOFORM = *wíntruz` is also the actual input fed to the OE derivation; `COUNTERPART = winter` is the selected Old English reflex the row aims to derive [Germanic/data/germanic-aligned-final.tsv:1416-1416].

## Detailed development-note summary

Row 2295 is thinly dossiered in `DEV_NOTES.md`. There is no winter-specific repair memo, target swap, or exception discussion comparable to `wether / weþer`. The useful material is instead a mixture of shared phonological notes, handbook quotations copied into other discussions, and later regression probes that keep `winter` as a stability check. That thinness needs to be stated explicitly: the row looks regular because the shared phonology is strong and the published trace already works, not because DEV_NOTES preserves a dedicated winter controversy [Germanic/docs/DEV_NOTES.md:16661-16710,22637-22643,40601-40605,41097-41103].

The lexical identity is secure even though the handbook headword formatting is not uniform. Kroonen gives `*wintru- m. 'winter; year' ... OE winter m. 'id.'`; Orel gives `*wentruz sb.m.` with `OE winter 'winter, year'`; Clark Hall lists `winter ... winter ... years` [@Kroonen2013; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29760-29764; @Orel2003; docs/references/orel_handbook_germanic_etymology.vision.txt:50199-50204; @ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48814-48817]. Those sources therefore support the lexeme pairing well, but they do **not** by themselves settle the exact project-normalized spelling of the proto headword. The live row uses `*wíntruz`; Kroonen prints a stem-form `*wintru-`; Orel prints `*wentruz`. This slice preserves the current row state rather than trying to resolve that broader reconstruction-format question [Germanic/data/germanic-aligned-final.tsv:1416-1416].

The strongest DEV_NOTES anchor is the shared epenthesis note, because it explicitly names `winter`. DEV_NOTES defines `OEEpentheticInsertion` as a rule inserting a vowel before final `*r` in consonant clusters and gives the exact winter pathway: `PGmc *wintruz → OE winter (via *wintr → *wintrEr → *winter)` [Germanic/docs/DEV_NOTES.md:16663-16675]. The same note insists that this is “a **real phonological rule**” rather than a hack, and concludes that the rule is “needed for words like `finger`, `timber`, `winter`” [Germanic/docs/DEV_NOTES.md:16677-16710]. For this row, that shared passage is more important than it was for `weather / weder`, because it is the only surviving DEV_NOTES passage that actually names the winter row and sketches its derivation rather than merely implying the class behavior.

Ringe and Taylor independently give essentially the same lexeme-specific development in handbook form. After explaining that apocope created many final `Cr` clusters, they write: “In word-final Cr-clusters a vowel was always inserted ... Normally the inserted vowel agreed in frontness with the vowel of the preceding syllable” [@RingeTaylor2014, §6.9.5; docs/references/ringe_taylor_linguistic_history_vol2.txt:18711-18729]. They then include winter itself among the examples created by apocope: `PGmce *wintruz ... > PWGmc *wintru ... > *wintr > OE winter` [@RingeTaylor2014, §6.9.5; docs/references/ringe_taylor_linguistic_history_vol2.txt:18804-18805]. That is especially useful here because it separates the steps that the compact project trace compresses: loss of final `-z`, loss of final high vowel after a heavy syllable, then final-`Cr` epenthesis.

Campbell supplies the other strong shared-class quotation preserved in DEV_NOTES. In the quotation copied at lines 22639-22643, `winter` appears among the “Normal OE forms”: “Normal OE forms are fugol, tungol, cumbol, **sāwol**, nagel, æppel, segel, þunor, wundor, winter, fæger, æcer ...” [Germanic/docs/DEV_NOTES.md:22639-22643; @Campbell1959, §362]. That passage is not a winter-specific note; it was copied into the `sāwol` discussion. But it matters because it treats `winter` as an ordinary member of the parasitic-vowel class, not as an exceptional spreadsheet row. Campbell's noun-morphology discussion is also worth preserving in the background: he cites `winter winter (also n. pl. winter or wintru)` and remarks that certain `u`-stem forms are due to the analogy of `winter` [@Campbell1959, §§614, 655; docs/references/campbell_old_english_grammar.txt:16068-16080]. That is morphological corroboration, not a derivational argument, but it confirms that the OE form `winter` is exactly the sort of output the row is supposed to target.

The row also intersects, negatively, with the separate initial-`w-` / back-mutation canvass. DEV_NOTES includes `*wíntruz` in the regression table for the narrowed `w`-conditioned rule and says the relevant sequence is `*n + *t (not *u/*o)`, so the rule does **not** fire; the note adds that `*wíntruz is excluded both because its *u sits behind a 3-C cluster (*ntr) and because the single-C scan stops at *n+*t` [Germanic/docs/DEV_NOTES.md:43615-43625]. This is not the row's main derivation, but it is valuable negative evidence. It makes explicit that `winter` should not be pulled into the `wudu`-type explanation merely because the protoform begins with `w-` and contains a later `u`.

Finally, the later OE-apocope troubleshooting notes use `winter` as a deliberate no-regression probe. Two separate verification blocks record `*wíntruz → winter` as a successful baseline check while the project adjusted other rows [Germanic/docs/DEV_NOTES.md:40601-40605,41097-41103]. Those probes do not explain the row; they only show that the implementation already handled it correctly and that subsequent edits were not supposed to disturb it. They should therefore be kept as diagnostic implementation history, not as the row's primary explanatory anchor.

Overall, the conservative replacement note is straightforward. `winter / winter` looks regular, but the evidence is mostly shared rather than row-local. The best current support is the shared epenthesis note that explicitly names `winter`, reinforced by Ringe and Taylor's direct `*wintruz > *wintru > *wintr > OE winter` example and Campbell's classification of `winter` among normal OE parasitic-vowel forms [Germanic/docs/DEV_NOTES.md:16661-16710,22639-22643; @RingeTaylor2014, §6.9.5; @Campbell1959, §362]. The back-mutation note and regression probes are useful only as secondary, limiting, or diagnostic evidence.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-16661-16710

- Source heading: `OEEpentheticInsertion: Parasitic Vowel in Final Consonant Clusters (2026-04-10)`
- Fragment type: `shared_phonology_fragment_with_explicit_lexeme_example`
- Status: `current`
- Issue tags: `epenthesis`; `final_cr_cluster`; `winter_example`; `quotation_preserved`
- Recommended next use: `best_available_index_anchor`
- Shared with row IDs: `2160`, `2255`, `2280`, `2283`, `2299`, and other final-`Cr` rows

This is the strongest surviving DEV_NOTES anchor for row 2295 because it actually names `winter` and gives the compressed derivational chain `*wintruz → *wintr → *wintrEr → *winter` [Germanic/docs/DEV_NOTES.md:16671-16675]. The fragment is still shared phonology rather than a row-specific dossier, but unlike many other shared notes it is lexeme-addressable enough to function as the row's best present anchor.

### DEV_NOTES:line-22637-22643

- Source heading: `Case 2 — *sáiwalō → sāwul (expected sāwol)`
- Fragment type: `shared_handbook_quote`
- Status: `current`
- Issue tags: `campbell_quote`; `normal_oe_forms`; `parasite_vowel_class`
- Recommended next use: `secondary_anchor`
- Shared with row IDs: `2201`, `2255`, `2299`, and other `-or/-er` parasite-vowel rows

This fragment is not winter-specific, but it preserves a useful direct quotation in which Campbell lists `winter` among the “Normal OE forms” [Germanic/docs/DEV_NOTES.md:22639-22643; @Campbell1959, §362]. It is best used as class evidence confirming that the target output is ordinary West Saxon, not as the main explanation of the row's derivation.

### DEV_NOTES:line-43615-43625

- Source heading: `Conditioning — handbook canvass and final scope`
- Fragment type: `background_scope_note`
- Status: `current`
- Issue tags: `w_back_mutation_exclusion`; `negative_evidence`; `initial_w`
- Recommended next use: `cite_only_if_w_conditioning_is_raised`
- Shared with row IDs: several initial-`w-` rows

This fragment matters because it names `*wíntruz` as a **non-trigger** for the separate `w`-conditioned mutation rule [Germanic/docs/DEV_NOTES.md:43615-43625]. It should not be mistaken for the main winter derivation, but it is valuable whenever later reporting needs to say explicitly why the row's vowel is **not** being explained through the `wudu`-type pathway.

### DEV_NOTES:line-40601-40605; DEV_NOTES:line-41097-41103

- Source heading: verification blocks in OE-apocope troubleshooting
- Fragment type: `diagnostic_row_probe`
- Status: `diagnostic_only`
- Issue tags: `no_regression_probe`; `implementation_history`
- Recommended next use: `background_only`
- Shared with row IDs: `spinl`, `fyrhte`, `botm`, and other probe rows from those checks

These fragments record `*wíntruz → winter` as a successful “no regression” or “baseline” probe during unrelated rule tuning [Germanic/docs/DEV_NOTES.md:40601-40605,41097-41103]. They confirm row stability, but they do not add new historical analysis and should not carry indexing weight on their own.

## Superseded or diagnostic material

- No winter-specific superseded migration note, repair memo, or contradiction was located in `DEV_NOTES.md`. The row's thinness is real: most support is shared-rule material rather than a row-local project history [Germanic/docs/DEV_NOTES.md:16661-16710,22639-22643].
- The duplicated Wiktionary placeholder in the TSV is inherited metadata, not the row's actual rationale [Germanic/data/germanic-aligned-final.tsv:1416-1416].
- The back-mutation note at `DEV_NOTES:line-43615-43625` is limiting evidence only. It explains what does **not** happen to `*wíntruz`; it does not replace the main apocope-plus-epenthesis derivation [Germanic/docs/DEV_NOTES.md:43615-43625].
- The regression probes at `DEV_NOTES:line-40601-40605` and `DEV_NOTES:line-41097-41103` are diagnostic implementation checks rather than lexeme analysis [Germanic/docs/DEV_NOTES.md:40601-40605,41097-41103].

## Open questions for later work

- If a later full lexeme report is written, it should decide whether to normalize discussion around the TSV's `*wíntruz`, Kroonen's stem-form `*wintru-`, or Orel's `*wentruz`; the present slice records the current row state but does not adjudicate that broader editorial choice [Germanic/data/germanic-aligned-final.tsv:1416-1416; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29760-29764; docs/references/orel_handbook_germanic_etymology.vision.txt:50199-50204].
- If `index.tsv` is revised later, the safest available anchor is `DEV_NOTES:line-16661-16710`. `DEV_NOTES:line-22637-22643` is a real secondary anchor, while `DEV_NOTES:line-43615-43625` is only a conditional background anchor.
