---
row_id: 1936
concept: ban
counterpart: bannes
proto: *bánną
protoform: *bánnas
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1936-ban-bannes.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1936-ban-bannes.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1936 ban / bannes

## Current row state

- CONCEPT: `ban`
- COUNTERPART: `bannes`
- PROTO: `*bánną`
- PROTOFORM: `*bánnas`
- DERIVATION_CLASS: `late_analogy`
- NOTE: `Gen.sg. paradigm cell: *bannas → bannes. Word-final geminates are phonologically simplified; using gen.sg. preserves medial geminate. Note: a-stem neuter, gen.sg. same as masc.`
- HISTORY: `Original: *banną → bann (nom.sg.).`

## Development-note summary

The live row is a deliberate paradigm-cell split, not a silent re-etymologization of the lexeme. `PROTO` `*bánną` remains the cognate-set headword, while row-level `PROTOFORM` `*bánnas` is the selected gen.sg. comparator and `bannes` is the corresponding OE gen.sg. target. DEV_NOTES makes the reason explicit: word-final geminates were not kept phonologically in Old English, so nominative-style `*banną` gives regular `ban`, whereas an oblique form with medial `nn` can preserve the geminate and produce `bannes` regularly [DEV_NOTES:line-13645-13668; DEV_NOTES:line-13784-13799].

The key current DEV_NOTES argument is the project-wide geminate note that says word-final spellings such as `mann`, `bedd`, and `bann` are "orthographic conventions — analogical restorations from inflected forms — not phonological geminates," while the phonological outputs were single final consonants [DEV_NOTES:line-13649-13652]. For this row that means `*banną -> ban` is not a phonological failure; it is the expected nominative-style outcome once final geminates simplify. The row therefore does **not** claim that OE headword `bann` was impossible. It claims instead that the inherited paradigm contains an oblique cell whose regular development preserves the medial geminate and gives a more useful comparator for the project workflow [DEV_NOTES:line-13663-13720].

DEV_NOTES then chooses the **genitive singular** as the working cell for masculine/neuter a-stems. The note lays out the paradigm logic explicitly: nom.sg. `*-ăz` and acc.sg. `*-ą` leave the geminate word-final and therefore simplified, but gen.sg. `*-ăs/*-ĕsă` and dat.sg. `*-ai` keep the geminate medial, where preservation is regular [DEV_NOTES:line-13669-13677]. It still prefers the gen.sg. because the ending is "universally attested across all declension classes" and because gen.sg. forms are well documented in glossaries and texts [DEV_NOTES:line-13678-13683]. The same fragment also preserves the practical cost of the decision — row targets become `mannes`, `bannes`, etc. rather than citation-form headwords — which matters for later report prose because the row should be described as a selected inflectional cell, not as the ordinary dictionary lemma [DEV_NOTES:line-13700-13703].

The suffixal phonology is also part of the current row policy, not a minor implementation detail. DEV_NOTES stresses that the gen.sg. must be entered with full `*a`, not the weak-tail marker `*ă`, because only full `*a` undergoes the unstressed fronting chain `*a -> *æ -> *e`. The note spells this out with the exact contrast `*mannas -> *mannæs -> mannes` and warns that `*ă` would skip fronting and incorrectly stay `a` [DEV_NOTES:line-13730-13765]. For row 1936 the same reasoning is what licenses `*bannas -> bannes`: the medial geminate is preserved, the suffix vowel fronts as required, and the row remains a regular phonological derivation once the project deliberately compares the gen.sg. cell [DEV_NOTES:line-13730-13765].

Row 1936 also has a narrower row-specific authority that should stay visible in place of any high-level paraphrase. DEV_NOTES identifies `ban` among the geminate-stem mismatches, records the old state as `*banną -> ban` against target `bann`, then adds the row-specific correction: "Neuter a-stems: Gen.sg. uses the same `-es` ending as masculines (Brunner §237). Therefore `*banną` (neuter) can use gen.sg. `*bannas` -> `bannes`." The implementation checklist then records the concrete TSV change: "Updated row 1936 (ban): proto `*bannas`, target `bannes`" [DEV_NOTES:line-13784-13799]. That is the strongest row-attached DEV_NOTES authority and should anchor later descriptions of why this file exists.

A later audit confirms that the row survived subsequent grammar cleanup. When DEV_NOTES restricted compound-linking syncope so that it targeted only the breve-marked linking vowel `*ă`, it explicitly notes `*bannas -> bannes` as a control witness for the opposite point: ordinary inflectional `*a` must **not** be eaten by the compound cleanup, and the suffix vowel for this row was "correctly preserved" [DEV_NOTES:line-16905-16910]. This is not the source of the row decision, but it is useful current maintenance evidence that later report writers would otherwise have to rediscover.

The checked philological support is stronger for the noun lexeme than for the exact row target. Orel gives PGmc `*bannan sb.n.` with OE `ge-bann`; Kluge-Seebold likewise has Germanic `*banna-` with OE `geban(n)`; Clark Hall has `+bann n. proclamation, summons, command`; and Bosworth-Toller likewise records `ge-bann` with ordinary oblique usage such as `to cyniges gebanne` [@Orel2003, s.v. "*bannan"; @KlugeSeebold2011, s.v. "Bann"; @ClarkHall1960, s.v. "bann"; @BosworthToller1898, s.v. "ge-bann"]. None of the checked row materials supplies equally secure direct authority for exact unprefixed `bannes`. The slice therefore needs to say this plainly: current row policy securely supports a **regular inferred/selected gen.sg. cell** `*bánnas -> bannes`, but the checked repository evidence is clearer for lexeme/headword `bann` or `gebann` than for a directly cited standalone headword/form `bannes`.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-13645-13668

Source heading: geminate-stem paradigm-cell note on word-final versus medial geminates  
Source line or section hint: lines 13645-13668  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: final_geminate;orthography_vs_phonology;paradigm_cell;protoform_vs_proto  
Recommended next use: cite_in_final_report  
Shared with row IDs: 2119;2203;2300  
Text or paraphrase:
This is the project-level fragment that makes row 1936 intelligible. DEV_NOTES says the consensus is that word-final geminates were phonologically simplified in OE and that spellings such as `mann`, `bedd`, and `bann` are analogical orthographic restorations from inflected forms, not preserved final geminates. It then names `*banną -> ban` among the resulting mismatches and proposes the replacement method: instead of targeting the nominative singular, choose an oblique case where the geminate remains medial before a vowel-initial suffix. For `ban / bannes`, that is the point from which all later row policy follows.

### DEV_NOTES:line-13669-13720

Source heading: candidate paradigm cells and recommendation for geminate-stem nouns  
Source line or section hint: lines 13669-13720  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: genitive_singular;paradigm_cell;case_form;project_method  
Recommended next use: cite_in_final_report  
Shared with row IDs: 2119;2203;2300  
Text or paraphrase:
This fragment preserves the comparative argument for why the gen.sg. was chosen rather than some other oblique cell. DEV_NOTES tabulates nom.sg., gen.sg., dat.sg., and acc.sg. for masculine/neuter a-stems and marks only the oblique cells with medial geminate preservation. It then states that the genitive singular is the best choice because the geminate is medial before `-es`, the ending is broadly attested, and gen.sg. forms are well documented. Just as importantly, the fragment records the cost of the method — targets become `mannes`, `bannes`, etc. — so later report prose should treat `bannes` as a selected comparator, not as a disguised citation lemma.

### DEV_NOTES:line-13730-13765

Source heading: gen.sg. implementation note on full `*a` versus weak-tail `*ă`  
Source line or section hint: lines 13730-13765  
Fragment type: copied_shared_lexeme_fragment  
Status: current  
Issue tags: unstressed_fronting;suffix_vowel;protoform_spelling;genitive_singular  
Recommended next use: cite_in_final_report  
Shared with row IDs: 2119  
Text or paraphrase:
This is the detailed phonological fragment the slice has to preserve because it explains why row 1936 uses `*bánnas`, not some mechanically similar but wrong spelling with `*ă`. DEV_NOTES says, in capitals, that for gen.sg. `-es` "we need `a:{*a} s:{*s}` (NOT `ă:{*ă} s:{*s}`)," because the breve vowel skips unstressed fronting while full `*a` participates in `*a -> *æ -> *e`. The note illustrates the chain with `*mannas -> *mannæs -> mannes`; row 1936 depends on the same chain for `*bannas -> bannes`.

### DEV_NOTES:line-13784-13799

Source heading: geminate-stem mismatch table and row-1936 update  
Source line or section hint: lines 13784-13799  
Fragment type: lexeme_specific  
Status: current  
Issue tags: row_policy;project_history;neuter_a_stem;final_geminate  
Recommended next use: cite_in_final_report  
Shared with row IDs: 2119  
Text or paraphrase:
This is the strongest row-specific fragment and should remain the primary DEV_NOTES authority for the slice. It records the old state in the mismatch table (`1936 | ban | *banną | ban | bann | word-final degemination`), then immediately states the correction for this exact noun: neuter a-stems take the same gen.sg. `-es` ending as masculines, so `*banną` can use gen.sg. `*bannas -> bannes`. The checklist closes the loop by recording that row 1936 was updated to proto `*bannas` and target `bannes`.

### DEV_NOTES:line-16905-16910

Source heading: compound-linking syncope audit preserving ordinary inflectional `*a`  
Source line or section hint: lines 16905-16910  
Fragment type: phenomenon_context_for_lexeme  
Status: background  
Issue tags: regression_check;suffix_vowel;compound_syncope;project_maintenance  
Recommended next use: keep_as_general_background  
Shared with row IDs:  
Text or paraphrase:
This later audit is not the source of the row decision, but it is valuable maintenance evidence. DEV_NOTES reports that the restricted compound-linking syncope rule now targets only the linking-vowel marker `*ă`, and it cites `*bannas -> bannes` as a successful control case where the ordinary inflectional suffix vowel was "correctly preserved." That matters because it confirms that later cleanup did not accidentally destroy the very suffixal fronting behavior on which row 1936 depends.

## Superseded or diagnostic material

The superseded state is not the noun itself but the earlier way the row was framed. DEV_NOTES first preserved `ban` as a mismatch of the form `*banną -> ban` against orthographic target `bann`, i.e. as if the problem were simply that the transducer lost a consonant. The later geminate-stem note shows why that framing was too shallow: the real contrast is between a regular phonological nominative-style output with final simplification and a deliberately selected oblique cell where the geminate remains medial. That old mismatch entry is therefore worth keeping as project chronology, but it should no longer be cited as if it were the final account of the row.

A second point that must stay explicit is the philological limit of the current evidence. The checked dictionaries and etymological references securely support the noun lexeme (`bann`, `gebann`) and its PGmc bann-stem background, but they do not yet provide equally secure direct authority for exact standalone `bannes` in the repo materials reviewed here [@Orel2003, s.v. "*bannan"; @KlugeSeebold2011, s.v. "Bann"; @ClarkHall1960, s.v. "bann"; @BosworthToller1898, s.v. "ge-bann"]. So `bannes` should be carried forward as the project's selected regular gen.sg. comparator, not overstated as a lexicographic headword that the checked materials have already pinned down directly.

## Open questions for later work

- add a firmer philological citation for exact OE `bannes` if one turns up, since the checked repository evidence is clearer for lexeme/headword `bann` or `gebann` than for the exact selected gen.sg. target;
- if the final report keeps `bannes`, explain explicitly that `PROTO` `*bánną` is the cognate-set headword while row-level `PROTOFORM` `*bánnas` is a deliberate gen.sg. comparator chosen because final geminates simplify but medial ones survive;
- if row normalization is revisited later, keep the distinction between phonological output `ban` from nominative-style `*banną` and selected working-cell output `bannes` from gen.sg. `*bannas`, rather than collapsing the issue into a vague "analogy" label alone.
