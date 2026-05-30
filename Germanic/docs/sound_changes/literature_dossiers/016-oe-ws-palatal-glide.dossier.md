# SC016 OE Ws Palatal Glide — literature dossier

## Rule metadata

- change_id: SC016
- display_name: OE Ws Palatal Glide
- FOMA rule: OEWsPalatalGlide
- current_order: 16
- chronology_card: `Germanic/docs/sound_changes/order_tests/chronology_cards/SC016-oe-ws-palatal-glide.md`
- example_lexemes: yoke, young, youth
- aliases searched: OE Ws Palatal Glide; palatal glide; West Saxon palatal glide; glide-conditioned fronting; glide fronting; fronting before j; fronting before i/j; palatal diphthongization; ġeoc; geoc; yoke; *júką; juk; i-umlaut; palatal influence; breaking and palatal glide; West Saxon fronting

## FOMA definition

```foma
define OEWsPalatalGlide [
    {*j} {*u} -> {*j} {*e} {*u} || .#. _,
    {*j} {*ú} -> {*j} {*é} {*u} || .#. _
] .o. [
    {*ʤ} {*u} -> {*ʤ} {*e} {*u} || .#. _,
    {*ʤ} {*ú} -> {*ʤ} {*é} {*u} || .#. _
] .o. [
    {*ʧ} {*u} -> {*ʧ} {*e} {*u} || .#. _,
    {*ʧ} {*ú} -> {*ʧ} {*é} {*u} || .#. _
] .o. [
    {*ʃ} {*u} -> {*ʃ} {*e} {*u} || .#. _,
    {*ʃ} {*ú} -> {*ʃ} {*é} {*u} || .#. _
];
```

## Working description

The CAPR rule inserts a front glide element before initial `u` after word-initial palatals, yielding West Saxon spellings and outputs of the `geoc / geong / geoguþ` type. The literature does discuss this phenomenon, but usually not under the exact rule name **OE Ws Palatal Glide**. Older grammars more often describe:

1. rising diphthongs or glide spellings before back vowels in West Saxon;
2. `geoc / geong / geoguþ` as the core example set;
3. dialectal and orthographic variation among `iu / io / eo` or undiphthongized forms.

That matters for book use. The historical phenomenon is real and well attested, but the CAPR rule is a narrow formalization of it rather than a standard named sound law in the way that Anglo-Frisian Brightening or i-umlaut are.

## Search log

| Source file searched | Search terms used | Productive? | Evidence found | Notes |
| --- | --- | --- | --- | --- |
| `docs/references/kaluza_historische_grammatik_englisch.txt` | `geoc`, `gioc`, `geong`, `iung`, `Joch`, `yoke`, `palatal` | yes | early grammar statement of OE reflexes of initial Germanic `j`; `geoc / geong / geogud` example cluster | good dated witness; terminology is descriptive rather than rule-name based |
| `docs/references/bulbring_altenglisches_elementarbuch.txt` | `iuc`, `jeoc`, `geoc`, `geong`, `gio`, `geo`, `Joch` | yes | detailed West Saxon `gio/geo` discussion with `Joch`, `jung`, `Jugend` examples | especially useful for spelling variation |
| `docs/references/luick_historische_grammatik.txt` | `geoc`, `jung`, `young`, `Joch`, `zio`, `zeo` | yes | discussion of West Saxon doublets and later generalization of `geo-` spellings | useful caution about variation and chronology of spellings |
| `docs/references/campbell_old_english_grammar.txt` | `palatal glide`, `rising diphthongs`, `geoc`, `geong`, `§ 172`, `young` | yes | clearest English-language description of rising diphthongs formed by palatal glides before back vowels | best source for book-safe wording |
| `docs/references/ringe_taylor_linguistic_history_vol2.txt` | `geoc`, `/jok/`, `word-initial /j/`, `back vowel`, `West Saxon diphthongization` | yes | modern witness that `geoc` represents /jok/ after initial /j/ before back vowel | useful, but more phonological/orthographic than chronological |
| `docs/references/hogg_vol1.txt` | `geoc`, `palatal diphthongization`, `rising diphthongs`, `geong` | no | mostly etymological or lexical mentions | no short dossier-ready discussion of this specific phenomenon recovered in this pass |
| `docs/references/brunner_1965_altenglische_grammatik.txt` | `geoc`, `geong`, `§ 92`, `Joch` | no | relevant section found, but OCR was too noisy for a clean short quotation | checked, but not used as a primary witness |
| `docs/references/bosworth_toller_anglo_saxon_dictionary.txt` | `geoc`, `geong`, `geoguþ` | no | lexical confirmation only | dictionary evidence, not historiographic discussion |
| `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` | `geoc`, `geong`, `geoguþ` | no | lexical confirmation only | dictionary evidence, not historiographic discussion |

## Chronological source dossier

### Kaluza 1900

- source_key: Kaluza1900
- full source title: *Historische Grammatik der englischen Sprache. Erster Teil: Geschichte der englischen Sprache, Grundzüge der Phonetik, Laut- und Formenlehre des Altenglischen*
- publication year: 1900
- locator: § 90, lines 7280-7283 in the local text witness
- terminology used by the source: reflexes of initial Germanic `j` in Old English
- exact quotation: "Beispiele: a) Urg. j im Anlaut = ae. g, ge, gi, i [g, j]: ... geoc, gioc Joch (lat. jugum), geómor Jammer, geong, giung, iung jung, geogud Jugend"
- paraphrase of the source's claim: Kaluza treats `geoc / geong / geogud` as regular Old English reflexes of initial Germanic `j` in this environment. The presentation is descriptive and orthographic-phonological rather than a named sound-change chapter.
- conditioning stated by the source: initial Germanic `j` in Old English; the quoted examples show the West Saxon `ge-/gio-/gi-` spellings before back-vocalic material
- examples used by the source: `geoc`, `gioc`, `geómor`, `geong`, `giung`, `iung`, `geogud`
- chronology stated or implied by the source: implied Old English development; no explicit relative chronology against another named sound change
- relation to other changes: the passage is about reflexes of initial `j`, not about u-lowering or i-umlaut directly
- cautions, uncertainties, or disagreements: the source does not isolate a separate sound law called "palatal glide"; it groups these forms under the wider treatment of initial `j`
- assessment of usefulness for the book: useful as an early witness that the `geoc / geong / geogud` set is real and traditional, but not enough by itself to justify the exact CAPR rule name

### Bülbring 1902

- source_key: Bulbring1902
- full source title: *Altenglisches Elementarbuch. I. Teil: Lautlehre*
- publication year: 1902
- locator: §§ 298-299, lines 5970-5985 in the local text witness
- terminology used by the source: West Saxon `gio / geo` development; `io`/`eo` spellings after palatal environments
- exact quotation: "iuc, jeoc 'Joch' (< wg. *juk, niederl. juk) ... jo ist im Ws. zu gio geo geworden ... gioc geoc 'Joch' (aus wg. *jok, neben *juk § 298), giōmrian geōmrian"
- paraphrase of the source's claim: Bülbring explicitly treats West Saxon `gio / geo` as the relevant development and uses `Joch`, `jung`, and `Jugend` as the standard examples. He also preserves the coexistence of forms from both `*juk` and `*jok` type reconstructions in the explanatory tradition.
- conditioning stated by the source: West Saxon development after palatal onset; `jo` and related sequences yield `gio / geo`
- examples used by the source: `iuc / jeoc`, `gioc / geoc`, `giōmrian / geōmrian`, `iúng / gióng / geing`
- chronology stated or implied by the source: the source implies a West Saxon development and later orthographic regularization, but gives no explicit chronology against u-lowering
- relation to other changes: relation is primarily to dialectal spelling development rather than to a separate chain of vowel changes
- cautions, uncertainties, or disagreements: the reconstruction alternates between `*juk` and `*jok`, showing that the older tradition did not always isolate the exact stage CAPR now targets
- assessment of usefulness for the book: very useful for demonstrating that the `geoc / geong / geoguþ` cluster was long recognized, but also that the older literature often handled it as spelling/diphthongization rather than as a sharply bounded sound change

### Luick 1921

- source_key: Luick1921
- full source title: *Historische Grammatik der englischen Sprache*
- publication year: 1921
- locator: lines 10447-10458 in the local text witness
- terminology used by the source: West Saxon doublets; later generalization of `zeo-/geo-` spellings
- exact quotation: "Alfred zeigt jung ... daneben aber ... zēomor Jammer', geoc 'Joch'. Später wurden diese letzteren Formen ... in der Schreibung verallgemeinert"
- paraphrase of the source's claim: Luick emphasizes that West Saxon preserved competing spellings and that later `geo-` forms became generalized in writing. The phenomenon is thus treated as a real development, but one entangled with orthographic regularization and dialectal variation.
- conditioning stated by the source: West Saxon environment with the `jung / geoc / geōmor` type forms
- examples used by the source: `jung`, `zēomor`, `geoc`, `zeonz`, `zeozoo`
- chronology stated or implied by the source: later written generalization follows earlier variation; explicit ordering against u-lowering is absent
- relation to other changes: relation is to dialect and spelling history, not to an independently named chronology slot
- cautions, uncertainties, or disagreements: Luick's emphasis on doublets is a warning against treating the phenomenon as a perfectly clean single-step law
- assessment of usefulness for the book: useful mainly as a cautionary source; it helps prevent overclaiming about uniformity

### Campbell 1959

- source_key: Campbell1959
- full source title: *Old English Grammar*
- publication year: 1959
- locator: § 44, lines 2192-2199 in the local text witness
- terminology used by the source: rising diphthongs formed when palatal glides developed before back vowels
- exact quotation: "the graphs ea, eo, io are used not for the usual OE falling diphthongs, but for rising diphthongs, which were formed when palatal glides developed before back vowels, as in ... geoc yoke ... A palatal glide + u is written eo, io or iu in W-S and Kt."
- paraphrase of the source's claim: Campbell gives the clearest compact description of the phenomenon. The central claim is that West Saxon spellings like `geoc` and `geong` reflect rising diphthongs formed by palatal glides before back vowels.
- conditioning stated by the source: palatal glide before back vowel; especially palatal glide plus `u` in West Saxon and Kentish
- examples used by the source: `geoc`, `geong`, other `ea / eo / io` rising-diphthong examples
- chronology stated or implied by the source: Old English dialect development; no explicit order against u-lowering, but the description presupposes the palatal-glide outcome as a phonological fact
- relation to other changes: related to the treatment of initial palatal consonants and later dialect spelling conventions
- cautions, uncertainties, or disagreements: Campbell still describes a phonological/spelling phenomenon, not a standard separate sound law with a fixed historical label
- assessment of usefulness for the book: the best single source for book prose on the historical phenomenon behind SC016

### Ringe and Taylor 2014

- source_key: RingeTaylor2014
- full source title: *The Development of Old English*
- publication year: 2014
- locator: p. 5 in the local text witness, lines 1169-1173
- terminology used by the source: orthographic practice after word-initial `/j/` followed by a back vowel
- exact quotation: "After word-initial /j/ followed by a back vowel that practice was universal. Thus ... geoc 'yoke' is /jok/; exceptionally, geong ~ iung 'young' is /jung/."
- paraphrase of the source's claim: Ringe and Taylor explicitly treat `geoc` as an orthographic representation of /jok/ and note `geong ~ iung` as a marked variation point. This is a modern confirmation that the `geoc` type is real, but it is not presented as a standalone named sound change.
- conditioning stated by the source: word-initial `/j/` before back vowel
- examples used by the source: `geoc`, `geong ~ iung`, `geara`, `geomor`
- chronology stated or implied by the source: none explicit for the change itself; the emphasis is phonological interpretation of spellings
- relation to other changes: indirectly related to West Saxon diphthongization and to the treatment of initial palatals
- cautions, uncertainties, or disagreements: modern source still stops short of treating this as an independently named chronology anchor
- assessment of usefulness for the book: useful as a modern control on what the spellings represent, but not enough to turn SC016 into a standard literature-defined sound law

## Comparative synthesis

1. **Do the sources agree on the existence of the change?**  
   Yes, in the limited sense that they agree on a real West Saxon phenomenon behind `geoc / geong / geogud` type forms. What they do **not** agree on is framing it as a standalone named sound change.

2. **Do they use the same terminology?**  
   No. Kaluza, Bülbring, and Luick describe the reflexes of initial `j` or the `gio/geo` spellings; Campbell speaks of rising diphthongs formed by palatal glides before back vowels; Ringe and Taylor frame the issue as orthographic/phonological interpretation. The exact CAPR label **OE Ws Palatal Glide** is model terminology, not a standard literature label.

3. **Do they define the same conditioning environment?**  
   Broadly yes: initial palatal onset before back-vocalic material, especially `u`. But the sources vary in how narrow they are. Campbell is closest to the CAPR environment; older grammars often speak more broadly about spelling classes and West Saxon forms.

4. **Do they use the same examples?**  
   Yes, strongly. The recurring core examples are `geoc` 'yoke', `geong` 'young', and `geogud / geoguþ` 'youth', with `geōmor` often nearby.

5. **Do they assign the same historical stage?**  
   They all place it in Old English, especially West Saxon. None of the productive sources turns it into an earlier Northwest Germanic change.

6. **Do they give an explicit relative chronology?**  
   No clear literature source recovered here explicitly says "palatal glide before u-lowering." The sources describe the phenomenon, but the exact SC016/SC017 ordering is mostly a CAPR articulation drawn from the `yoke` derivation.

7. **Do they conflict with the current CAPR implementation?**  
   Not directly, but they are broader and less formalized. The literature supports the `geoc / geong / geoguþ` outcomes, while CAPR operationalizes that support as a discrete insertion rule before SC017. The main risk is over-reading literature description as if it already supplied CAPR's exact rule boundaries.

8. **Do they support, complicate, or fail to discuss the SC016/SC017 computational boundary?**  
   They partly support it and partly fail to discuss it. They support it because `geoc` is the standard test item and because the palatal/glide outcome is real. They fail to discuss it because no productive source recovered here explicitly states the relative chronology with NWGmc u-lowering.

9. **Is the change a standard historical sound change, a model-internal formalization, or a mixture?**  
   A mixture. The historical phenomenon is standard enough, but the exact CAPR rule name and discrete stage are model-internal formalization of material the literature usually treats under orthography, diphthongization, or palatal-glide description.

10. **What can safely be said in book prose?**  
   It is safe to say that West Saxon developed `geoc / geong / geoguþ` type outcomes through palatal-glide/rising-diphthong behavior before back vowels. It is **not** yet safe to present SC016 as a universally recognized named sound law with an independently literature-established chronology against SC017.

## Relation to CAPR implementation

The CAPR rule turns the literature's descriptive phenomenon into a sharply bounded formal stage:

1. **FOMA definition:** `OEWsPalatalGlide` inserts `e` after initial palatals before `u/ú`, yielding the `geoc`-type outputs.
2. **Current order:** SC016 sits immediately before SC017 in the cascade.
3. **Chronology card:** the card is one-sided. Its earlier side is runner-limited by bundled `PWGmcChanges`, but its later boundary is tight and reciprocal against SC017.
4. **Representative failure:** if SC016 is delayed across SC017, PGmc `*júką` yields `ġoc` instead of expected `ġeoc`.
5. **Graph/export layer:** the core edge `SC016 < SC017` is already deduplicated as reciprocal support (`support_count=2`, representative failure `yoke`).

The literature does not contradict this. But it also does not independently establish the exact SC016/SC017 order. What CAPR has done is to isolate a local computational dependency that fits the traditional `geoc / geong / geoguþ` evidence, while giving it a cleaner stage identity than the scholarship usually does.

## Dossier status

ready_for_book_dossier: partial
