# SC016-SC020: Early vocalic/final corridor

## 1. Role in the book

This dossier is the first deliberately **multi-change corridor** in the sound-change half of the book. That is useful because the early corridor is not a sequence in which every rule has the same scholarly status.

1. SC016 is a real West Saxon phenomenon, but not a widely standardized handbook sound-law label.
2. SC017 is a classical comparative rule with stable literature support.
3. SC019 is historically real, but the literature usually treats it through final-vowel and ending structure rather than under a chapter-like rule name.
4. SC020 is historically real and important, but its sharp one-line CAPR implementation is more exact than the usual handbook wording.

That asymmetry is precisely why this chapter matters. It shows how the book can use three kinds of evidence together without collapsing them into one another:

1. **literature support**, which is strongest for SC017 and solid but more indirect for SC016, SC019, and SC020;
2. **formal implementation**, which gives each development a precise place in the cascade;
3. **order-testing evidence**, which identifies a local derivational spine that the handbooks usually imply only in broader terms.

## 2. Corridor overview

The active corridor is:

1. **SC016 OE Ws Palatal Glide** — glide-conditioned fronting entrance
2. **SC017 NWGmc U Lowering** — central standard rule
3. **SC019 NWGmc Final Long O Raising** — hinge into final-vowel structure
4. **SC020 PGmc Final Z Deletion** — bridge into later final-syllable chapters

This is a meaningful unit because the chronology cards recover one local spine all the way across it:

1. `SC016 < SC017` on `yoke`
2. `SC017 < SC019` on `nose`, `shovel`, `sorrow`
3. `SC019 < SC020` on `rest`

SC018 is **not** part of the active prose corridor despite its order number. In the cascade it sits between SC017 and SC019 as `NWGmcStressedMonosyllableORaising`, but its chronology card is a negative/boundary-limited card: no historical first-break boundary is currently identified on either side. It therefore matters to the implementation, but it does not define the local derivational spine that makes this chapter narratable.

## 3. Traditional description and literature synthesis

The literature does not present this corridor as a ready-made four-step chapter. It presents its pieces unevenly, and the book has to synthesize them carefully.

At the left edge, older grammars already treat the `geoc / geong / geoguþ` cluster as real West Saxon material. Kaluza lists `geoc`, `geong`, and `geogud` among the Old English reflexes of initial Germanic `j`; Bülbring discusses West Saxon `gio / geo`; and Campbell gives the clearest short statement, saying that the spellings in forms such as **`geoc`** reflect rising diphthongs "formed when palatal glides developed before back vowels." This is enough to ground SC016 historically, but it also shows why SC016 needs careful prose. The literature usually describes a **West Saxon palatal-glide / rising-diphthong phenomenon**, not a universally named sound law called *OE Ws Palatal Glide*.

The center of the corridor is stronger. For SC017, Kaluza, Campbell, and Fulk all state the familiar rule that stressed Germanic `u` lowers to `o` before a following non-high vowel, with standard examples such as `dohtor`, `gold`, `geoc`, `coren`, `boren`, and `holpen`. Campbell's compact formulation — **"`u > o before mid and low vowels`"** — is the clearest handbook wording; Fulk adds the most explicit modern conditioning, including blocking before tautosyllabic nasals and before `j` in the relevant environment. SC017 is therefore the most straightforwardly literature-defined member of the corridor.

The chapter then turns away from root vocalism toward ending structure. For SC019, the strongest witnesses are Luick, Ringe and Taylor, and Fulk. Ringe and Taylor state the core change most clearly: **"PGmc word-final bimoric non-nasalized long *-ō became short *-u in unstressed syllables in PNWGmc."** Fulk presents the same development through `ō`-stem and comparable endings, while Luick treats final `ō > u` as part of the wider problem of final-vowel shortening. This is strong evidence for the historical phenomenon, but it also explains why SC019 is less standard as a chapter label than SC017: the literature usually treats it as **final unstressed `*-ō > *-u`** or as an `ō`-stem/ending development rather than as a neat standalone rule called *NWGmc Final Long O Raising*.

SC020 continues that ending-centered turn. Campbell and Hogg give the concise handbook frame that Germanic `z` is later lost or rhotacized, while Crist 2001 and especially Crist 2002 sharpen the historical picture into a West Germanic loss of word-final `*z` in unstressed syllables before rhotacism. Kilday's modern summary is especially useful because it treats this as already established background: **"the well-known West Germanic loss of Proto-Germanic word-final *z in unstressed syllables."** Again, the phenomenon itself is not weak. What is less standard is CAPR's exact label and exact scope: the literature speaks most clearly of **word-final `*z` in unstressed syllables**, with major morphological consequences, rather than of an unconditional delete-any-final-`z` operation.

So the traditional picture is coherent, but uneven.

1. **SC017 is the clearest literature-defined sound change.**
2. **SC016 is real, but weakly named and often handled through spelling or palatal-glide description.**
3. **SC019 is historical, but mainly as an ending-development story.**
4. **SC020 is historical, but morphology-heavy and broader in the literature than CAPR's one-line rule.**

That is enough for book prose, so long as the chapter says so openly instead of pretending that all four subsections stand on identical historiographical footing.

## 4. Formal implementation

The CAPR model turns the corridor into four explicit stages. That precision is useful, but each stage needs its own caveat.

### SC016

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

Historical claim implemented: West Saxon `geoc / geong / geoguþ`-type fronting after an initial palatal onset before back-vocalic material.

Model-specific part: CAPR isolates this as a discrete insertion rule and extends it across a tightly defined initial palatal inventory.

Scope caveat: the literature supports the phenomenon, but usually not as a rule named *OE Ws Palatal Glide*. In prose, this should be presented as a formalized West Saxon palatal-glide development.

### SC017

```foma
define NWGmcULowering [
    {*u} -> {*o} || .#. EnglishStarConsonant* _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel,
    {*ú} -> {*ó} || .#. EnglishStarConsonant* _ [EnglishStarConsonantNoJ - EnglishStarNasal] EnglishStarConsonantNoJ* EnglishStarNonHighVowel
];
```

Historical claim implemented: stressed Germanic `u` lowers to `o` before a following non-high vowel.

Model-specific part: CAPR makes the initial-syllable restriction, the nasal blocking, and the `j`-blocking fully explicit in one rule.

Scope caveat: this is the rule closest to a standard handbook sound law. Even here, the exact CAPR conditioning is more exact than most short textbook summaries.

### SC019

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u} || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Historical claim implemented: unstressed final non-nasalized long `*-ō` becomes `*-u` in polysyllabic Northwest Germanic forms.

Model-specific part: CAPR gives the change a strict structural guard and separates out stressed monosyllables and other special endings into neighboring rules.

Scope caveat: this is best read as a formal stage for historical `final *-ō > *-u`, not as a handbook claim that always appears under the label *NWGmc Final Long O Raising*.

### SC020

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
define PGmcFinalZLoss PGmcFinalZDeletion;
```

Historical claim implemented: West Germanic loss of word-final `*z` before rhotacism.

Model-specific part: CAPR writes the change as an unconditional final deletion rule.

Scope caveat: the clearest literature statement is narrower — word-final `*z` in **unstressed syllables** — and is heavily tied to morphology. The book should therefore describe the historical phenomenon in literature terms and then explain that CAPR models it with a single deletion stage.

## 5. Place in the cascade

The relevant slice of `EnglishProtoToOE` is:

```foma
.o. NWGmcUnstressedAiMonophthongization
.o. NWGmcILowering
.o. OEWsPalatalGlide
.o. NWGmcULowering
.o. NWGmcStressedMonosyllableORaising
.o. NWGmcFinalLongORaising
.o. PGmcFinalZDeletion
```

This is why the book chapter should be a corridor rather than four unrelated notes.

1. SC016, SC017, SC019, and SC020 form the **interpretable derivational spine** recovered by the chronology cards.
2. SC018 sits inside the same local cascade but does **not** currently carry a positive chronology constraint on either side; it is important to the implementation, but not to the narrative spine.
3. SC020 points forward because once final `*z` is gone, the model begins feeding the broader final-syllable and weak-tail system that becomes more visible in later chapters.

So the prose architecture is selective rather than mechanical: it follows the meaningful historical-and-computational corridor, not every adjacent rule number.

## 6. Order-testing evidence

The chronology cards provide a narrow local spine, but that spine must be narrated as **CAPR order-testing evidence grounded in literature-compatible phonology**, not as direct handbook quotation.

### SC016 < SC017 on `yoke`

If SC016 is delayed across SC017, PGmc `*júką` yields `ġoc` instead of expected `ġeoc`.

1. what breaks: glide-conditioned fronting disappears from the `yoke` derivation
2. reciprocity: yes; SC016 later and SC017 earlier define the same boundary
3. independent literature support: partial only; the literature clearly supports the `geoc` phenomenon and the `u > o` rule, but does not explicitly state their local ordering in SC labels
4. what CAPR adds: a clean local claim that the West Saxon palatal-glide effect must be visible before the rule that lowers `u` to `o`

### SC017 < SC019 on `nose`, `shovel`, `sorrow`

If SC017 is moved later than SC019, PGmc `*núsō`, `*skúflō`, and `*súrgō` yield `nusu`, `sċufl`, and `surg` instead of expected `nosu`, `sċofl`, and `sorg`.

1. what breaks: the expected lowered root vowel fails to appear before final `*-ō` is turned into `*-u`
2. reciprocity: yes; SC017 later and SC019 earlier are reciprocal
3. independent literature support: partial but stronger than for SC016/SC017; Fulk supports the broader chronology that `u`-lowering is earlier than final `*-ō > *-u`, but the exact `nose / shovel / sorrow` boundary is CAPR's formulation
4. what CAPR adds: a concrete local corridor through lexemes that make the broader comparative chronology operational

`Nose` should also carry a caution in any polished chapter prose, because Kroonen's etymology preserves an ablaut alternative (`*nasō- ~ *nusō-`) rather than one uncontested preform.

### SC019 < SC020 on `rest`

If SC019 is moved later than SC020, PGmc `*rástōz` yields `rast` instead of expected `ræste`.

1. what breaks: final `*-ō` loses the chance to raise to `*-u` before final `*z` is removed
2. reciprocity: yes; SC019 later and SC020 earlier are reciprocal
3. independent literature support: indirect only; the literature strongly supports both historical ingredients, but does not itself formulate the `rest` boundary as a local chronology statement
4. what CAPR adds: the clearest local hinge showing why this corridor turns from vocalism into ending structure

### SC020 and the forward-looking side

SC020 has a later broad/far boundary with SC040. If SC020 is moved that far forward, derivations such as `beaver`, `bough`, `cud`, `field`, and `flood` begin to produce unwanted final `-o` outcomes.

That matters, but only as forward context.

1. it is not a tight local adjacency like the three boundaries above
2. it helps explain why SC020 is better treated as a bridge into later final-syllable chapters
3. it should not be narrated as if the handbooks independently state a direct SC020-before-SC040 law

## 7. Interpretation for the book

This corridor begins with a West Saxon palatal-glide phenomenon that is real but not usually named as a separate sound law; moves into a standard Northwest Germanic `u`-lowering rule; then turns into final-vowel and ending structure through final `*-ō > *-u`; and closes with West Germanic final `*z` loss, which explains why the same local derivational corridor also leads into later final-syllable chapters.

That should be the chapter's core narrative.

The point is not that four equally famous textbook rules happen to occur in sequence. The point is that a historically plausible derivational path becomes visible when the literature and the CAPR model are read together.

1. **SC016** supplies the local entrance through West Saxon `geoc`-type fronting.
2. **SC017** provides the strongest standard comparative rule in the group.
3. **SC019** shifts the chapter from root-vowel change into ending history.
4. **SC020** closes the local corridor and opens the door to the broader weak-tail/final-syllable story.

That is why this chapter belongs near the start of the sound-change half of the book. It demonstrates the method: literature first, implementation second, chronology evidence as controlled support, and explicit warnings when a clean local CAPR boundary goes beyond what the handbooks say in so many words.

## 8. Subsection treatment

| Subsection | Likely length | Main examples | Source anchors | CAPR evidence | Caveat |
| --- | --- | --- | --- | --- | --- |
| **1. Glide-conditioned fronting as the entrance: SC016** | short | `geoc`, `geong`, `geoguþ` | Campbell 1959; Kaluza 1900; Bülbring 1902 | reciprocal `SC016 < SC017` boundary on `yoke` | real phenomenon, but weakly named in the literature |
| **2. Northwest Germanic `u`-lowering as the central rule: SC017** | longest | `geoc`, `gold`, `dohtor`, `holpen`; corridor examples `nose`, `shovel`, `sorrow` | Campbell 1959; Fulk 2018; Kaluza 1900; Luick 1921 for doublets | reciprocal boundaries on both sides: `yoke`; `nose / shovel / sorrow` | strongest sound-law subsection, but local SC boundaries remain CAPR formulations |
| **3. Final `*-ō > *-u` as the hinge: SC019** | medium | `*gebō > *gebu`, `*feþrō > *feþru`, `hwatu`; corridor examples `nose`, `shovel`, `sorrow`, `rest` | Ringe and Taylor 2014; Fulk 2018; Luick 1921; Kroonen/Orel for lexical mapping | reciprocal `SC017 < SC019` and `SC019 < SC020` boundaries | historical change is clear, but CAPR's stage label should probably be softened in prose |
| **4. Final `*z` deletion as bridge/coda: SC020** | short-to-medium | `*dagaz`, `*gastiz`, `*sunuz`; corridor example `rest` | Crist 2002; Crist 2001; Hogg 1992; Campbell 1959; Kilday 2024 | reciprocal local boundary with SC019 on `rest`; later broad/far context toward SC040 | literature states a morphology-heavy WGmc final-unstressed loss, not CAPR's exact unconditional rule |

## 9. Relation to neighbouring changes

SC018 is the nearest non-member. It remains in the cascade slice because it is a genuine implemented rule, but it is a **negative / boundary-limited** card rather than a corridor-organizing node. It should therefore be acknowledged briefly and then set aside.

SC020's later relation to SC040 is real but broad/far. It belongs in this dossier only as a signpost that the corridor does not end the weak-tail story.

Three further later links have been checked and should be handled cautiously:

1. **SC041** is a contextual broad/far echo, not a local pair.
2. **SC042** has a checked local card-side link to SC020 through the `rest` derivation, but it belongs to a different later chapter problem.
3. **SC054** likewise has a checked local link through the `sea` derivation, but it is a later echo, not part of the present corridor spine.

These relations matter as orientation, not as chapter-expansion triggers. If they were allowed to dictate chapter scope, the corridor would expand into an undifferentiated graph-driven unit. The book should resist that. This chapter is about the early vocalic/final corridor proper; later chapters can pick up the downstream final-syllable consequences.

## 10. Remaining uncertainty

1. Should SC016 be called a **sound change**, or more cautiously a modeled West Saxon palatal-glide sub-rule?
2. Should SC019's CAPR label be softened in prose toward **final unstressed `*-ō > *-u`** or **final `ō`-stem raising/shortening** language?
3. How much of Crist's-law / final-`z` discussion belongs in the main SC020 text, and how much should be pushed into a note?
4. Should `nose` always carry an explicit ablaut caution because of Kroonen's `*nasō- ~ *nusō-` reconstruction?
5. Should the SC020 links to SC041/SC042/SC054 be mentioned in the main corridor chapter at all, or only in later neighboring chapters?

## 11. Proposed final book-section outline

1. **The early vocalic/final corridor**
2. **Why `geoc` is the chapter's entrance: West Saxon palatal-glide fronting**
3. **Northwest Germanic `u`-lowering as the corridor's central rule**
4. **From root vocalism to ending structure: final `*-ō > *-u`**
5. **Why `rest` closes the local corridor: final `*z` loss before the later weak-tail system**
6. **What the local chronology cards show**
7. **What the literature supports, and what CAPR adds**
8. **Why SC018 is adjacent but not chapter-forming**
9. **How this corridor hands off to later final-syllable chapters**
