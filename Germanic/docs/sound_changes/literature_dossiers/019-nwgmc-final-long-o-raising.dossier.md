# SC019 NWGmc Final Long O Raising — literature dossier

## Rule metadata

- change_id: SC019
- display_name: NWGmc Final Long O Raising
- FOMA rule: NWGmcFinalLongORaising
- current_order: 19
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC019-nwgmc-final-long-o-raising.md`
- example_lexemes: nose, shovel, sorrow, rest; standard comparative examples include `*gebō > *gebu`, `*feþrō > *feþru`, Runic `laþu`, and OE `hwatu`
- aliases searched: NWGmc Final Long O Raising; final long o raising; final ō raising; final -ō > -u; final o to u; final long o to u; unstressed ō to u; unstressed final ō; Proto-Germanic final ō; Northwest Germanic final ō; North-West Germanic final ō; final -o; final -u; ō-stem; ō-stems; feminine ō-stem; nominative singular ō-stem; nose; nosu; nusu; `*núsō`; shovel; sċofl; scufl; scofl; `*skūflō`; `*skúflō`; sorrow; sorg; surg; `*surgō`; `*súrgō`; rest; ræste; rast; `*rastōz`; final z deletion; final -z deletion; final ō raising before final z deletion; u lowering and final ō

## FOMA definition

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Immediate implementation context in `Germanic/fsts/germanic.txt` makes two important caveats explicit:

1. monosyllabic stressed final `*ō` is handled separately by `NWGmcStressedMonosyllableORaising`;
2. nasalized `*ǭ` and trimoric `*ô` are excluded by neighboring rules and comments rather than by the SC019 rewrite alone.

## Working description

SC019 is not best understood as a standard handbook change called **NWGmc Final Long O Raising**. The literature more often describes the underlying phenomenon as one of the following:

1. word-final unstressed `*-ō` becoming `*-u` in Proto-/Northwest Germanic;
2. the behavior of feminine `ō`-stem nominative singulars and comparable endings;
3. shortening or restructuring of unstressed final long vowels;
4. later West Germanic retention after light syllables and loss after heavy syllables.

So the historical phenomenon is real and well supported, but the CAPR label is a formal summary. It packages a broader comparative claim about final unstressed `*-ō > *-u` into one local stage that can then interact with SC017 and SC020.

## Search log

| Source file searched | Search terms used | Productive? | Evidence found | Notes |
| --- | --- | --- | --- | --- |
| `docs/references/luick_historische_grammatik.txt` | `auslautendes ō`, `zu u`, `gebō`, `Nominativen`, `nosu`, `sorg`, `räste` | yes | direct older discussion of word-final `ō` advancing to `u` before shortening | best early explicit witness recovered in this pass |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | `word-final bimoric non-nasalized long *-ō`, `short *-u`, `unstressed syllables`, `gebu`, `feþru` | yes | clean modern statement of the change in PNWGmc, plus standard ending examples | strongest concise rule statement |
| `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt` | `yielding NWGmc. *-u`, `PGmc. *-ō became *-u`, `laþu`, `hwatu` | yes | comparative statement for `ō`-stem endings and OE preservation/lowering after light stems | best modern bridge from comparative rule to OE outcomes |
| `docs/references/kroonen_etymological_dictionary_pgmc.vision.txt` | `*nasō`, `*nusō`, `*surgō`, `*rastō`, `nosu`, `sorg`, `ræst` | yes | lexical mapping for `nose`, `sorrow`, and `rest` to Proto-Germanic `ō`-stems | useful for CAPR example mapping, not chronology |
| `docs/references/orel_handbook_germanic_etymology.vision.txt` | `*skuflō`, `*rastō`, `scofl`, `rest` | yes | lexical mapping for `shovel` and `rest` | useful for CAPR example mapping, not chronology |
| `docs/references/campbell_old_english_grammar.txt` | `§ 331`, `331(5)`, `final unstressed long ō`, `hwatu`, `duru`, `nosu` | no | cross-references and obvious target sections surfaced, but no safely quotable direct SC019 passage was recovered from the local OCR witness | checked, but not used as a primary witness |
| `docs/references/hogg_vol1.txt` | `final -u`, `ō-stem`, `light stems`, `nom. sg. fem.` | no | later OE retention/loss material surfaced, but no compact SC019 rule statement | checked, but not used |
| `docs/references/kaluza_historische_grammatik_englisch.txt` | `nosu`, `ō-stems`, `Nom. Sg.`, `final u`, `duru`, `hond` | no | `nosu` surfaced only in stem-class paradigms; no direct earlier NWGmc `*-ō > *-u` statement recovered | checked, but not used as a primary witness |
| `docs/references/bulbring_altenglisches_elementarbuch.txt` | `nachtonigen Vokale`, `auslautende u`, `ō-stämme`, `Nominativ Singular` | no | useful on later OE retention/loss of final `i/u`, not a clean statement of SC019 itself | checked, but not used as a primary witness |
| `docs/references/brunner_1965_altenglische_grammatik.txt` | `ō-stämme`, `auslautendes ō`, `Nom. Sg.`, `hwatu` | no | likely relevant material exists, but OCR quality was too noisy for safe quotation | checked, but not used |
| `docs/references/crist_2002_z_loss_west_germanic.txt` | `final z`, `word-final z`, `unstressed syllables`, `West Germanic` | no | useful for SC020-side framing only; no direct discussion of final `*-ō > *-u` | checked for relation to other changes |
| `docs/references/bosworth_toller_anglo_saxon_dictionary.txt` | `nosu`, `scofl`, `sorg`, `ræst` | no | lexical confirmation only | dictionary evidence, not historical discussion |
| `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | `nosu`, `scofl`, `sorg`, `ræst` | no | lexical confirmation only | dictionary evidence, not historical discussion |

## Chronological source dossier

### Luick 1921

- source_key: Luick1921
- full source title: *Historische Grammatik der englischen Sprache*
- publication year: 1921
- locator: lines 16096-16106 in the local text witness
- terminology used by the source: `auslautendes ō`; `zu u vorgerückt`; `Verkürzung`
- exact quotation: "auch möglich, daß auslautendes ō schon vor der Verkürzung durch einen spontanen Lautwandel ... zu u vorgerückt war und daher die Verkürzung zu u führte."
- paraphrase of the source's claim: Luick treats final `ō > u` as a real historical development, though he frames it as a problem of how final long-vowel shortening interacted with an earlier spontaneous advance of `ō` to `u`.
- conditioning stated by the source: word-final `ō`, specifically in the context of final-vowel shortening
- examples used by the source: the surrounding discussion centers on final-vowel classes rather than on the CAPR lexeme quartet
- chronology stated or implied by the source: the `ō > u` advance may already have happened before the shortening process reached its endpoint
- relation to other changes: tied to the wider complex of final-vowel shortening and to the chronology of `a`-loss
- cautions or disagreements: Luick presents a theoretical explanation rather than a simple one-line rule; the source does not formulate SC019 as a named sound law
- usefulness for book prose: valuable as an early witness that the phenomenon was recognized historically, but too theory-heavy to serve as the main prose template

### Orel 2003

- source_key: Orel2003
- full source title: *A Handbook of Germanic Etymology*
- publication year: 2003
- locator: lines 33408-33411 and 38705-38706 in the local text witness
- terminology used by the source: etymological headwords `*rastō` and `*skuflō`
- exact quotation: "`*rastō sb.f.: ... OE rest 'rest, quiet' ...`"; "`*skuflō sb.f.: ... OE scofl id.`"
- paraphrase of the source's claim: Orel does not discuss SC019 as a sound law, but he maps two CAPR lexemes, `rest` and `shovel`, to Proto-Germanic feminine formations in `*-ō`.
- conditioning stated by the source: implied only through the reconstructed stem shape
- examples used by the source: `*rastō`, `*skuflō`, OE `rest`, OE `scofl`
- chronology stated or implied by the source: none explicit
- relation to other changes: useful only insofar as it anchors CAPR's examples in standard etymological headwords
- cautions or disagreements: this is lexical support, not chronology support
- usefulness for book prose: limited but useful for making the CAPR example set legible

### Kroonen 2013

- source_key: Kroonen2013
- full source title: *Etymological Dictionary of Proto-Germanic*
- publication year: 2013
- locator: lines 20131-20145, 21137-21138, and 25336-25337 in the local text witness
- terminology used by the source: etymological headwords `*nasō- ~ *nusō-`, `*rastō-`, `*surgō-`
- exact quotation: "`*nasō- ~ *nusō- f. 'nose' ... OE nosu f. 'id.'`"; "`*surgō- f. 'grief, sorrow, worry' ... OE sorg, sorh f. 'id.'`"; "`*rastō- f. 'interval' ... OE ræst f. 'rest, peace, grave'`"
- paraphrase of the source's claim: Kroonen confirms that `nose`, `sorrow`, and `rest` all belong to the same broad final-`ō` morphological zone CAPR is exploiting, while also showing that the `nose` etymon is itself reconstructively complicated (`*nasō- ~ *nusō-`).
- conditioning stated by the source: not given as a sound-law formula; the support is morphological-etymological
- examples used by the source: `nosu`, `sorg/sorh`, `ræst`
- chronology stated or implied by the source: none explicit
- relation to other changes: supports the lexical side of the SC017/SC019 and SC019/SC020 boundaries without itself asserting those boundaries
- cautions or disagreements: the `nose` entry itself preserves ablaut uncertainty, so it should not be overused as if the literature gave a single uncontested preform
- usefulness for book prose: useful for lexical grounding and for warning that not all CAPR preforms are equally straightforward

### Ringe and Taylor 2014

- source_key: RingeTaylor2014
- full source title: *The Development of Old English: A Linguistic History of English, Volume II*
- publication year: 2014
- locator: lines 1671-1679 in the local text witness
- terminology used by the source: `word-final bimoric non-nasalized long *-ō became short *-u in unstressed syllables in PNWGmc`
- exact quotation: "It is clear that PGmc word-final bimoric non-nasalized long *-ō became short *-u in unstressed syllables in PNWGmc."
- paraphrase of the source's claim: Ringe and Taylor give the cleanest direct statement of the change as a Proto-Northwest-Germanic development. They immediately connect it to common inflectional endings such as `*gebō > *gebu` and `*feþrō > *feþru`.
- conditioning stated by the source: word-final, bimoric, non-nasalized long `*-ō` in unstressed syllables
- examples used by the source: `*gebō > *gebu`, `*feþrō > *feþru`, `*grasō > *grasu`
- chronology stated or implied by the source: PNWGmc, before the later West Germanic heavy/light distribution of final `-u`
- relation to other changes: explicitly tied to later loss after heavy syllables and survival after light syllables
- cautions or disagreements: the source is about the general phenomenon, not about the exact CAPR label or the local SC017/SC019/SC020 corridor
- usefulness for book prose: strongest single concise rule statement recovered in this pass

### Fulk 2018

- source_key: Fulk2018
- full source title: *A Comparative Grammar of the Early Germanic Languages*
- publication year: 2018
- locator: lines 10024-10025 and 14500-14501 in the local text witness
- terminology used by the source: `yielding NWGmc. *-u`; `PGmc. *-ō became *-u in North and WGmc.`
- exact quotation: "`Nom. sg. PIE *-ā ... > PGmc. *-ō, yielding NWGmc. *-u, as in Runic laþu`"; "`PGmc. *-ō became *-u in North and WGmc., and this is preserved as such (or lowered to -o) in OE after light stems`"
- paraphrase of the source's claim: Fulk presents the change both as a comparative development of `ō`-stem endings and as a direct explanation of OE `-u/-o` after light stems. He is also the clearest source tying the rule to actual OE reflexes like `hwatu`.
- conditioning stated by the source: final `*-ō` in North/West Germanic, especially visible in `ō`-stem and comparable ending material; preserved in OE after light stems
- examples used by the source: Runic `laþu`, OE `hwatu`, and the broader `ō`-stem inflectional system
- chronology stated or implied by the source: Northwest Germanic / North-and-West-Germanic development prior to later OE heavy/light apocope behavior
- relation to other changes: directly related to later OE loss of final `-u` after heavy syllables; elsewhere in Fulk, NWGmc `u`-lowering is earlier than this development
- cautions or disagreements: Fulk's formulation is broader and more inflection-centered than the CAPR stage label
- usefulness for book prose: best modern source for translating the comparative rule into OE-facing prose

## Comparative synthesis

1. **Do the sources agree on the existence of the change?**  
   Yes, if the change is framed broadly as unstressed final `*-ō > *-u` in Northwest Germanic. The strongest direct witnesses are Luick, Ringe and Taylor, and Fulk. The etymological dictionaries presuppose the same development in the CAPR lexeme set.

2. **Do they use the same terminology?**  
   No. None of the productive sources uses the CAPR label **NWGmc Final Long O Raising**. They speak instead of `word-final ... *-ō became *-u`, of `ō`-stem nominatives, or of the behavior of light-stem final `-u/-o`.

3. **Do they describe the same conditioning environment?**  
   Broadly yes. The shared core is unstressed word-final non-nasalized long `*-ō` in polysyllables. CAPR sharpens that with a preceding-nucleus guard and by separating stressed monosyllables and nasalized/trimoric endings into other rules.

4. **Do they discuss final `*-ō > -u`, final long-vowel raising, `ō`-stem endings, or something else?**  
   Mostly final `*-ō > *-u` and `ō`-stem/ending behavior. The literature is more inflectional than chapter-like here. CAPR's label "raising" is a concise formalization of a broader ending-development story.

5. **Do they use examples comparable to `nose`, `shovel`, `sorrow`, or `rest`?**  
   Not as a standard quartet. The rule sources prefer inflectional examples such as `*gebō > *gebu`, `*feþrō > *feþru`, Runic `laþu`, and OE `hwatu`. The CAPR lexemes are recoverable mainly through etymological dictionaries: Kroonen maps `nose`, `sorrow`, and `rest`; Orel maps `shovel` and `rest`.

6. **Do they assign the same historical stage?**  
   Yes in broad terms. Ringe and Taylor place it in PNWGmc; Fulk frames it as North-and-West-Germanic; Luick treats it as an early final-vowel development preceding the endpoint of shortening. None of the productive sources makes it a specifically late Old English phenomenon.

7. **Do they give an explicit relative chronology with `u`-lowering or final `z` deletion?**  
   Only partially. Fulk's discussion of SC017 treats `u`-lowering as earlier than final `*-ō > *-u`, which supports the left-hand side of SC019's corridor. No productive SC019 source recovered here explicitly says that final `*-ō > *-u` precedes final `z` deletion in the `rest` derivation.

8. **Do they support, complicate, or fail to discuss the SC017/SC019 computational boundary?**  
   They support it only indirectly. The literature strongly supports SC019 as a real historical phenomenon and Fulk supports the relative order `u`-lowering before final `*-ō > *-u`. But the exact local boundary on `nose / shovel / sorrow` is a CAPR formulation rather than a quotation from the handbooks.

9. **Do they support, complicate, or fail to discuss the SC019/SC020 boundary?**  
   They mostly fail to discuss it directly. Kroonen and Orel confirm that `rest` belongs to a `*-ō` formation, and Crist confirms a separate West Germanic rule deleting final `*z` in unstressed syllables, but no productive source recovered here explicitly states the SC019-before-SC020 ordering that CAPR derives from `*rástōz`.

10. **Is SC019 a standard historical sound change, a CAPR-specific formalization, or a mixture?**  
    A mixture leaning historical. The underlying phenomenon is standard comparative phonology. The exact label, the exact FOMA guard conditions, and the tight local adjacency claims belong to CAPR's formalization.

11. **What can safely be said in book prose?**  
    It is safe to say that in Proto-/Northwest Germanic, unstressed final non-nasalized long `*-ō` became `*-u`, especially in common ending classes, and that West Germanic later treated this `-u` like inherited short `-u`, retaining it after light syllables and losing it after heavy ones. It is not safe to claim that the handbooks themselves formulate the exact SC017/SC019 or SC019/SC020 adjacency now seen in CAPR.

## Relation to CAPR implementation

The CAPR implementation is a disciplined local formalization of the broader literature:

1. **FOMA definition:** `NWGmcFinalLongORaising` rewrites final `*ō` to `*u` only when another vocalic nucleus precedes it and at least one consonant intervenes before word-end. That matches the literature's unstressed polysyllabic profile, but the exact structural guard is CAPR-specific.
2. **Current order:** SC019 stands at order 19, immediately after SC017 and immediately before SC020.
3. **Chronology card:** the card gives a reciprocal earlier boundary with SC017 on `nose; shovel; sorrow` and a reciprocal later boundary with SC020 on `rest`.
4. **Earlier CAPR boundary:** if SC019 is moved earlier than SC017, PGmc `*núsō`, `*skúflō`, and `*súrgō` yield `nusu`, `sċufl`, and `surg` rather than expected `nosu`, `sċofl`, and `sorg`.
5. **Later CAPR boundary:** if SC019 is moved later than SC020, PGmc `*rástōz` yields `rast` rather than expected `ræste`.

The literature supports the historical ingredients behind those failures, but not the exact card wording. Fulk's comparative account supports the broader order `u`-lowering before final `*-ō > *-u`. Kroonen and Orel support the lexical mapping of `nose`, `shovel`, `sorrow`, and `rest`. Crist's West Germanic `*z`-deletion paper supports treating final `*z` loss as a separate historical event. But the local SC017/SC019 and SC019/SC020 boundaries are still **CAPR order-testing results**, not statements automatically made by the handbooks.

This also clarifies what SC019 is doing in the model. CAPR is not inventing the historical phenomenon; it is turning a literature-backed ending development into one discrete stage with enough precision to interact with neighboring rules. That is especially reasonable on the SC017 side, where Fulk already points to the right comparative chronology, and more tentative on the SC020 side, where the local `rest` boundary remains much more model-local.

## Dossier status

- ready_for_book_dossier: partial
- remaining_gaps: recover a direct Campbell or Brunner quotation for the standard handbook framing; check whether any local source states the `rest`/final-`z` side more explicitly; review whether `nose` should be narrated with explicit ablaut caution each time because of Kroonen's `*nasō- ~ *nusō-` reconstruction
- recommended_next_step: create the SC020 literature dossier before drafting any book-level early-corridor prose
