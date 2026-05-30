# SC016-SC020 early vocalic/final corridor architecture

## 1. Files created

This pass adds:

1. `Germanic/docs/sound_changes/literature_dossiers/020-pgmc-final-z-deletion.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/016-020-early-vocalic-final-corridor.architecture.md`

It builds directly on:

1. `Germanic/docs/sound_changes/literature_dossiers/016-oe-ws-palatal-glide.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/017-nwgmc-u-lowering.dossier.md`
3. `Germanic/docs/sound_changes/literature_dossiers/019-nwgmc-final-long-o-raising.dossier.md`
4. `Germanic/docs/sound_changes/literature_dossiers/016-017-palatal-glide-u-lowering.pair-report.md`
5. `Germanic/docs/sound_changes/literature_dossiers/016-019-early-vocalic-corridor.report.md`

## 2. Sources searched for SC020

The SC020 sweep covered the expected handbook and article layer plus Germanic-side internal notes:

- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/hogg_vol1.txt`
- `docs/references/crist_2001_conspiracy_in_historical_phonology.txt`
- `docs/references/crist_2002_z_loss_west_germanic.txt`
- `docs/references/kilday_2024_crists_law_smiths_law_wizen.txt`
- `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/luick_historische_grammatik.txt`
- `docs/references/brunner_1965_altenglische_grammatik.vision.txt`
- `docs/references/kaluza_historische_grammatik_englisch.txt`
- `docs/references/bulbring_altenglisches_elementarbuch.txt`
- `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt`
- `docs/references/orel_handbook_germanic_etymology.vision.txt`
- `Germanic/docs/analysis/meord_med_chronological_review.md`

## 3. Productive SC020 sources by date

| Year | Source | What it contributed |
| --- | --- | --- |
| 1959 | Campbell, *Old English Grammar* | standard handbook statement that Verner's-law `z` is later lost or rhotacized |
| 1992 | Hogg, *The Cambridge History of the English Language, Volume I* | compact OE-facing statement that final `z` is generally lost while intervocalic `z` rhotacizes |
| 2001 | Crist, *Conspiracy in Historical Phonology* | PWGmc `*-z` after unstressed vowel, explicit morphology consequences, and deletion-before-rhotacism chronology |
| 2002 | Crist, *An Analysis of \*z Loss in West Germanic* | clearest formulation of pan-WGmc word-final `*z` loss in unstressed syllables and strongest chronology with rhotacism |
| 2024 | Kilday, *Crist's Law, Smith's Law, and English wizen* | recent synthesis treating the basic WGmc final-unstressed loss as established background distinct from Crist's narrower Ingvaeonic deletions |

## 4. Sources checked but not useful

| Source file | Why it was checked | Why it was not used as a primary witness |
| --- | --- | --- |
| `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt` | expected comparative grammar witness | useful for medial `z` environments such as `mēd`, not for a clean direct SC020 statement |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | obvious comparative target | no clean direct SC020 passage was recovered from the local witness |
| `docs/references/luick_historische_grammatik.txt` | expected older German grammar witness | useful for neighboring `i/u`-before-`z/r` and final-vowel issues, not for a clear standalone SC020 statement |
| `docs/references/brunner_1965_altenglische_grammatik.vision.txt` | expected grammar witness | OCR too noisy for a safe final-`z` quotation |
| `docs/references/kaluza_historische_grammatik_englisch.txt` | early grammar check | no usable direct SC020 passage recovered |
| `docs/references/bulbring_altenglisches_elementarbuch.txt` | early grammar check | no usable direct SC020 passage recovered |
| `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | lexical control for `rest` and related forms | lexical mapping only, not historical rule discussion |
| `docs/references/orel_handbook_germanic_etymology.vision.txt` | lexical control for `rest`, `sea`, and later broad/far examples | lexical mapping only, not historical rule discussion |
| `Germanic/docs/analysis/meord_med_chronological_review.md` | internal note on `mizdō / meord / mēd` | useful only to keep medial `z` distinct from SC020 |

## 5. Strongest SC020 quotations

1. **Campbell 1959:** "the voiced spirant z ... is later lost or changed to r"
2. **Hogg 1992:** "Gmc /z/ yielded /r/ in intervocalic position ... but in final position it is generally lost."
3. **Crist 2001:** "This rule, which appears to have occurred at the PWGmc stage, had drastic consequences for noun morphology"
4. **Crist 2002:** "Throughout WGmc, PGmc *z deletes word-finally in unstressed syllables"
5. **Kilday 2024:** "the well-known West Germanic loss of Proto-Germanic word-final *z in unstressed syllables"

Together these make the core historical point clear: SC020 is not speculative. What remains model-specific is the exact one-line FOMA implementation and the detailed computational adjacency map around it.

## 6. Summary of each corridor member

### SC016

- literature status: partial
- CAPR status: real phenomenon but not a standard named sound law; local reciprocal boundary with SC017 on `yoke`
- book role: left-hand entrance to the corridor, introducing why glide-conditioned fronting must be stated cautiously

### SC017

- literature status: substantial
- CAPR status: strongest standard handbook change in the corridor; local reciprocal links on both sides
- book role: central explanatory anchor of the corridor

### SC019

- literature status: partial
- CAPR status: historically real final-`*-ō > *-u` development, but packaged in CAPR as a discrete stage; reciprocal local edge with SC017 and local edge with SC020
- book role: hinge from early vocalism into final-vowel / ending structure

### SC020

- literature status: partial
- CAPR status: strongly historical core, but CAPR implements it as an unconditioned final-`*z` deletion and then traces later computational effects outward to SC040/SC041/SC042/SC054
- book role: bridge section closing the early corridor and opening the later final-syllable system

## 7. Points of agreement across the corridor

1. The corridor is historically real as a chain of interactions, not just a string of arbitrary CAPR rules.
2. SC017 is the clearest standard sound change in the set.
3. SC019 and SC020 are both best understood through ending structure and final-syllable history rather than as isolated textbook chapter labels.
4. The core local CAPR boundaries (`SC016<SC017`, `SC017<SC019`, `SC019<SC020`) are all historically interpretable, even where the exact derivational examples are model-local.

## 8. Points of silence or disagreement

1. SC016 remains weakly named in the literature: the phenomenon is discussed, but the CAPR label is not standard.
2. SC019 is well supported as a historical development, but the literature rarely states it in the exact local form CAPR uses.
3. SC020 is standard as WGmc final-unstressed `*z` loss, but the literature does not itself stage the `rest` boundary or the later SC040/SC042/SC054 links in CAPR's exact way.
4. The corridor literature is therefore uneven: strong in the middle, thinner at the named-rule edges.

## 9. How the CAPR order-testing evidence fits the literature

The CAPR evidence should now be read as a structured supplement to the literature, not as a substitute for it.

1. **SC016/SC017:** the `yoke` boundary is primarily CAPR-local, but it is attached to a literature-backed West Saxon phenomenon and a literature-backed NWGmc lowering rule.
2. **SC017/SC019:** the `nose / shovel / sorrow` boundary is not quoted from the handbooks, but it aligns well with literature placing `u`-lowering before the final `*-ō > *-u` development.
3. **SC019/SC020:** the `rest` boundary is the key local bridge. The literature strongly supports both historical ingredients, but not their exact derivational packaging.
4. **SC020 onward:** the SC040 and SC041 relations are broad/far computational constraints; the SC042 and SC054 links are checked by actual chronology-card evidence but remain single-example later echoes, not reasons to dissolve the corridor into a giant undifferentiated chapter.

So the CAPR evidence now fits best as follows: it provides the local derivational spine of the corridor, while the literature tells us how confidently each node on that spine can be narrated.

## 10. Is the corridor now ready for a prose-ready book dossier?

Yes.

Not every member is equally strong as an independent named sound law, but the corridor no longer depends on unsupported computation alone. The dossier work has now established:

1. a documented SC016 phenomenon;
2. a strongly documented SC017;
3. a documented SC019 historical development;
4. a documented SC020 West Germanic final-`*z` loss.

That is enough to move from literature gathering to book-dossier drafting, provided the final prose architecture does not pretend that all four rules have the same status in the scholarship.

## 11. Recommended book architecture

**Recommendation: option 2. A three-part corridor plus SC020 bridge.**

In practice that means:

1. **main corridor core:** SC016, SC017, and SC019 as the three main subsections;
2. **bridge/coda:** SC020 as the section that closes the local `rest` problem and points forward into the later final-syllable system.

Why this is better than the alternatives:

1. **Better than four equal subsections.** SC020 is too strongly connected to the later final-syllable system to function as just another co-equal early vocalic subsection.
2. **Better than separate mini-chapters.** SC016 is too thinly named, and SC019/SC020 are too ending-oriented, for four fully separate mini-chapters to be the clearest architecture.
3. **Better than defer.** The missing SC020 literature work has now been done; continued deferral would no longer be solving the main bottleneck.

So the book unit should be conceived as an **early vocalic corridor chapter with a final-syllable bridge ending**:

1. SC016: glide-conditioned fronting entrance
2. SC017: Northwest Germanic `u`-lowering
3. SC019: final `*-ō > *-u` hinge
4. SC020: final `*z` deletion bridge into the later tail-reduction / final-syllable chapters

## 12. Recommended next task

Draft a **prose-ready early-corridor book dossier** using this architecture:

1. three main corridor subsections for SC016, SC017, and SC019;
2. one shorter SC020 bridge section;
3. explicit prose caution that SC019 and SC020 are historically real but more formally packaged in CAPR than SC017;
4. explicit distinction between literature-backed historical claims and CAPR-local order-testing evidence.
