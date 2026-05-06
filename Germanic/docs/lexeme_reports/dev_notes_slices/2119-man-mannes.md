---
row_id: 2119
concept: man
counterpart: mannes
proto: *mánnaz
protoform: *mánnas
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2119-man-mannes.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2119 man / mannes

## Current row state

- CONCEPT: `man`
- COUNTERPART: `mannes`
- PROTO: `*mánnaz`
- PROTOFORM: `*mánnas`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note (quoted closely): `Gen.sg. paradigm cell: *mannas → mannes. Word-final geminates are phonologically simplified (Kurath 1956, Brunner §231); using gen.sg. preserves medial geminate orthographically.` [Germanic/data/germanic-aligned-final.tsv:733]
- Live TSV history field: `Original: *mannăz → mann (nom.sg.).` [Germanic/data/germanic-aligned-final.tsv:733]
- `oe_known_problems.tsv`: no entry was found for row `2119`, `man`, `mannes`, `*mánnaz`, `*mánnas`, or normalized `*mannas` during the required source check; the packet also records `_None_` for matching known-problem entries [Germanic/docs/lexeme_reports/packets/2119-man-mannes.md:44-46; Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:27-33].
- The packet's compact derivation trace already matches the live row exactly: `PROTO: *mánnas`, `EXPECTED: mannes`, `OUTPUTS: mannes`, with OE-side stages `*mánnæs` and `*mánnes` before surface `mannes` [Germanic/docs/lexeme_reports/packets/2119-man-mannes.md:17-42].
- Repo-local philological support keeps lemma and selected inflection distinct. Campbell's paradigm gives `mann, man / mannes / menn`, Brunner cites `man mannes Mensch` and then explains final simplification with forms like `man ... monnes`, Ringe-Taylor summarize `PGmc *mann- ... > OE mann ~ monn`, Orel gives `*mannz ... OE mann`, and Clark Hall indexes the headword as `mann` [docs/references/campbell_old_english_grammar.txt:16384-16388; docs/references/brunner_1965_altenglische_grammatik.txt:8898-8901, 9026-9030; docs/references/ringe_taylor_linguistic_history_vol2.txt:8474-8475; docs/references/orel_handbook_germanic_etymology.vision.txt:29463-29465; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27428-27429].
- Current DEV_NOTES authority status: securely attachable **current row-specific** DEV_NOTES authority does exist for this row. The strongest row-specific block is the 2026-04-05 geminate-mismatch note that records the old nominative mismatch and then explicitly says row 2119 was updated to proto `*mannas`, target `mannes`; shared current method fragments at 13645-13720, 13730-13765, and 25306-25310 explain why that update is principled rather than ad hoc [Germanic/docs/DEV_NOTES.md:13645-13720; Germanic/docs/DEV_NOTES.md:13730-13803; Germanic/docs/DEV_NOTES.md:25306-25310].

## Development-note summary

The live row is a deliberate paradigm-cell row, not a lemma-to-lemma replacement. `PROTO` `*mánnaz` remains the lexeme-level cognate-set label used by the TSV, while row-level `PROTOFORM` `*mánnas` is the selected PGmc **gen.sg.** cell and OE `mannes` is the corresponding **gen.sg.** target [Germanic/data/germanic-aligned-final.tsv:733; Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:43-51]. The packet confirms that this is not merely editorial prose: the current cascade derives `*mánnas` to `mannes` directly, with the expected OE intermediate stages `*mánnæs` and `*mánnes` [Germanic/docs/lexeme_reports/packets/2119-man-mannes.md:17-42].

This row has stronger current DEV_NOTES authority than many other slice candidates. DEV_NOTES first states the general phonological premise that word-final geminates were simplified and that spellings such as `mann` are analogical/orthographic restorations from inflected forms like `mannes` [Germanic/docs/DEV_NOTES.md:13649-13652]. It then works through the paradigm-cell solution, corrects the gen.sg. input spelling to full `*a` rather than breve `*ă`, and finally records the concrete row update: `✓ Updated row 2119 (man): proto *mannas, target mannes` [Germanic/docs/DEV_NOTES.md:13752-13764, 13796-13799]. That row-specific 2026-04-05 update should be treated as current authority, not merely as background precedent.

Philologically, the row should still be described with explicit form distinctions. Campbell's noun paradigm includes exact gen.sg. `mannes`, and Brunner both gives the geminate example `man mannes Mensch` and explains that in word-final position one ordinarily sees simplification in forms like `man`, with double spellings influenced by oblique forms such as `monnes` [docs/references/campbell_old_english_grammar.txt:16384-16388; docs/references/brunner_1965_altenglische_grammatik.txt:8898-8901, 9026-9030]. Ringe-Taylor, Orel, and Clark Hall all continue to index the lexeme under citation-form `mann`/`monn`, which is useful background but not current row authority for the selected target [docs/references/ringe_taylor_linguistic_history_vol2.txt:8474-8475; docs/references/orel_handbook_germanic_etymology.vision.txt:29463-29465; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27428-27429]. The safest formulation is therefore: citation lemma `mann` (also `monn` in some traditions), selected row target `mannes`, chosen because the gen.sg. keeps `nn` medial and therefore derivable by regular sound change.

The memo's probe logic should stay attached to the row because it explains why `mannes` is needed. The checked manual outputs were `*mannăz -> man`, `*manną -> man`, `*mannăi -> manne`, `*mannas -> mannes`, so the gen.sg. is the only singular cell in the memo's minimum probe set that yields the selected target [Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:29-39, 68-79]. That is why the row should be described as "the man lexeme represented by its gen.sg. cell," not as a claim that the ordinary dictionary headword is `mannes`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-13645-13668

- Source heading: `Paradigm-cell approach for geminate-stem words`
- Source line or section hint: `lines 13645-13668`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `final_geminate`; `orthography_vs_phonology`; `paradigm_cell`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1936; 2203; 2300`

This is the shared phonological premise behind row 2119. DEV_NOTES says the consensus of Kurath, Brunner, and Hogg is that word-final geminates were simplified in OE, and that spellings such as `mann`, `bedd`, and `bann` are "orthographic conventions — analogical restorations from inflected forms — not phonological geminates" [Germanic/docs/DEV_NOTES.md:13649-13652]. For this row that means nominative-style `*mannăz -> man` is not an error but the expected phonological outcome, exactly as the memo's manual probe also reports [Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:33-39, 62-66]. The fragment is current and should remain the basic explanation for why row 2119 cannot be read as a simple nominative headword row.

### DEV_NOTES:line-13669-13720

- Source heading: `Candidate paradigm cells for masc./neut. a-stems`
- Source line or section hint: `lines 13669-13720`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `genitive_singular`; `paradigm_cell`; `case_form`; `project_method`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1936; 2203; 2300`

This fragment preserves the actual comparative argument for choosing the gen.sg. cell. DEV_NOTES tabulates nom.sg., gen.sg., dat.sg., and acc.sg. for masc./neut. a-stems and marks only the oblique cases as positions where the geminate stays medial and is therefore preserved; it then says the **genitive singular** is the best choice because the geminate is medial before `-es`, the ending is "universally attested across all declension classes," and gen.sg. forms are well documented [Germanic/docs/DEV_NOTES.md:13669-13682]. For row 2119 this remains current methodology. The caveat that must be kept explicit is that the illustrative example in this block uses the older spelling `*mannăs -> mannes`; that exact protoform spelling is superseded by the later correction to full `*mannas`, even though the paradigm-cell reasoning itself remains current [Germanic/docs/DEV_NOTES.md:13682; Germanic/docs/DEV_NOTES.md:13752-13764].

### DEV_NOTES:line-13730-13765

- Source heading: `Implementing Option A: gen.sg. paradigm-cell approach`
- Source line or section hint: `lines 13730-13765`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `unstressed_fronting`; `suffix_vowel`; `protoform_spelling`; `genitive_singular`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1936`

This is the decisive phonological fragment for row 2119 because it corrects the protoform spelling and gives the exact derivation. DEV_NOTES says, in capitals, that for gen.sg. `-es` "we need `a:{*a} s:{*s}` (NOT `ă:{*ă} s:{*s}`)," because full `*a` participates in unstressed fronting while breve `*ă` skips it; the note then gives the exact chain `*mannas -> *mannæs -> mannes` [Germanic/docs/DEV_NOTES.md:13752-13764]. That is the row-specific explanation for why the live TSV now has `*mánnas` rather than an older mechanically similar but wrong `*mannăs` [Germanic/data/germanic-aligned-final.tsv:733]. It also matches the packet's compact derivation trace exactly [Germanic/docs/lexeme_reports/packets/2119-man-mannes.md:17-42].

### DEV_NOTES:line-13784-13803

- Source heading: `Geminate-related mismatches identified (2026-04-05)`
- Source line or section hint: `lines 13784-13803`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `row_policy`; `project_history`; `final_geminate`; `tsv_update`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1936`

This is the strongest row-specific DEV_NOTES authority and should anchor the slice. DEV_NOTES first records the earlier state in the mismatch table as row `2119 | man | *mannăz | man | mann | word-final degemination`, then immediately records the completed fix: `✓ Updated row 2119 (man): proto *mannas, target mannes` [Germanic/docs/DEV_NOTES.md:13786-13799]. For later work this fragment matters because it proves that current row 2119 is not an inferential cleanup invented by the packet or memo; DEV_NOTES itself explicitly documents both the superseded nominative state and the current gen.sg. replacement.

### DEV_NOTES:line-25306-25310

- Source heading: `Path α — paradigm-cell PROTOFORM (Lautgesetzlich via Campbell's own account)`
- Source line or section hint: `lines 25306-25310`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `project_precedent`; `paradigm_cell`; `analogical_transfer`; `protoform_vs_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1980; 2013; 2140; 2152`

This later summary keeps row 2119 current beyond its original 2026-04-05 fix. DEV_NOTES names `mannes` explicitly as one of the prior precedents and states the rule in general form: "when the attested OE form arose by morphological transfer in a specific cell, encode that cell — do not rig phonology to produce the analogical outcome from the nom.sg. protoform" [Germanic/docs/DEV_NOTES.md:25306-25310]. That statement matches row 2119 exactly: lexeme-level `PROTO` remains `*mánnaz`, but the row-level derivational input is the gen.sg. `*mánnas`, and the output compared by the TSV is the surface form of that chosen cell, `mannes` [Germanic/data/germanic-aligned-final.tsv:733; Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:45-51, 81-89].

## Superseded or diagnostic material

The first superseded state is the old nominative-style row itself. The TSV history field preserves `Original: *mannăz → mann (nom.sg.)`, and DEV_NOTES likewise preserves the old mismatch framing `*mannăz | man | mann` before the gen.sg. update was adopted [Germanic/data/germanic-aligned-final.tsv:733; Germanic/docs/DEV_NOTES.md:13786-13799]. That material is still worth keeping as project history because it shows why the row exists, but it is no longer current row authority.

The second superseded point is narrower but important: DEV_NOTES originally illustrated the gen.sg. solution as `*mannăs -> mannes` [Germanic/docs/DEV_NOTES.md:13682]. Later in the same development sequence it explicitly corrects this, saying gen.sg. must use full `*a`, not breve `*ă`, because only full `*a` undergoes the unstressed fronting chain that yields OE `-es` [Germanic/docs/DEV_NOTES.md:13752-13764]. Any future reuse of the older `*mannăs` example should therefore be tagged as superseded spelling, not cited as the current protoform.

Older control material that still reports nominative `mann` can also mislead if detached from the row update. For example, an earlier regression check records `mannăz    mann    ✓ (no regression)` before the later paradigm-cell retargeting [Germanic/docs/DEV_NOTES.md:12965-12970]. That is useful only as diagnostic confirmation that nominative `*mannăz` still derives the expected citation-style output; it should not be mistaken for evidence against the current `mannes` row.

Citation-form lexeme evidence likewise needs controlled handling. Ringe-Taylor `OE mann ~ monn`, Orel `OE mann`, and Clark Hall `mann` are all real and relevant, but they are comparator/background evidence for the lemma, not competing current row targets [docs/references/ringe_taylor_linguistic_history_vol2.txt:8474-8475; docs/references/orel_handbook_germanic_etymology.vision.txt:29463-29465; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:27428-27429]. The current row is intentionally not a dictionary-headword row.

## Open questions for later work

- Add a saved `oe_paradigm_probe.py` spec for this lexeme if probe coverage is expanded elsewhere; the memo already identifies the minimum useful cells as nom.sg. `*mannăz -> man`, acc.sg. `*manną -> man`, dat.sg. `*mannăi -> manne`, and gen.sg. `*mannas -> mannes` [Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:68-79].
- If later report prose or TSV-note cleanup revisits this row, state explicitly that **current row-specific DEV_NOTES authority does exist** and is the 2026-04-05 update at lines 13784-13799, rather than implying that the row rests only on diffuse shared precedent.
- If proto-label normalization is reconsidered in a broader audit, keep the levels separate: lexeme-level `PROTO` `*mánnaz` as the project headword, row-level `PROTOFORM` `*mánnas` as the selected gen.sg. input, and OE target `mannes` as the surface form of that chosen cell. Reference works differ on the lexeme-level reconstruction (`*mann-`, `*mannz`, `*mannan-`), but that does not unsettle the current row-level paradigm-cell solution [Germanic/docs/lexeme_reports/research_memos/2119-man-mannes.md:45-51, 81-89; docs/references/ringe_taylor_linguistic_history_vol2.txt:8474-8475; docs/references/orel_handbook_germanic_etymology.vision.txt:29463-29465].
