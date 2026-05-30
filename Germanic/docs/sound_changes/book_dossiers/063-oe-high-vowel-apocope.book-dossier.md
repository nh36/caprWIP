# SC063: OE High Vowel Apocope

## 1. Role in the book

SC063 is a strong second pilot because it represents a different kind of chapter from SC043. Where SC043 is a compact early vocalic pivot, SC063 is a late weak-tail reduction rule with richer conditioning, a longer FOMA definition, and a more obvious need to coordinate literature, implementation, and chronology carefully.

That makes it valuable for the sound-change half of the book. A workable mini-chapter must be able to handle not only elegant two-sided local dependencies, but also rules whose main historical reality is widely accepted while their exact formal scope is technically delicate. SC063 is ideal for that test: the literature strongly supports the rule, yet the repository implementation makes explicit several branches and caveats that need controlled exposition.

## 2. Name and basic formulation

- **change_id:** `SC063`
- **display_name:** `OE High Vowel Apocope`
- **rule_name:** `OEHighVowelApocope`
- **current_order:** `63`
- **card:** `Germanic/docs/sound_changes/order_tests/chronology_cards/SC063-oe-high-vowel-apocope.md`

Short formulation: SC063 deletes final high vowels `i/u/ų` after heavy syllables and in the key trisyllabic configurations that behave equivalently, with additional formal branches for final-vowel hiatus after long vowels and for final `x/h` environments. In the live cascade, it is one major component of late prehistoric weak-tail reduction rather than the whole weak-tail story by itself.

## 3. Traditional description and literature

The literature dossier shows that the rule is standard, but the label is less uniform than in SC043. Luick speaks of **`i-, u-Schwund`** and the older broader category of unstressed-vowel loss; Campbell embeds the process under early OE loss of unaccented vowels; Hogg, Ringe and Taylor, and Fulk all describe the same basic change in more modern prose.

Two direct quotations capture the core of the traditional picture especially well. Luick states: **"Im Auslaut schwanden i und u unmittelbar nach langer Tonsilbe, und auch nach kurzer, wenn darauf noch eine andere Silbe folgte (nicht aber unmittelbar nach kurzer)."** Ringe and Taylor then make the local chronology explicit: **"After general syncope had run its course, short *i and *u were lost word-finally after a heavy syllable and after an unstressed syllable preceded by a stressed light syllable."** Campbell is consistent with the same account, describing the loss of final unstressed high vowels after long accented syllables and in the relevant longer-word environments.

What is standard in the literature is therefore clear:

1. final high vowels are lost after heavy syllables;
2. they are also lost in the relevant trisyllabic environments;
3. the change is closely related to, but not identical with, medial syncope;
4. it belongs very late in prehistoric Old English.

What remains uncertain is not the existence of apocope itself but its **exact formal envelope**. The literature dossier flags:

1. the delicate trisyllabic branch;
2. the precise boundary between apocope and medial syncope;
3. inflectional exceptions such as Mercian `-u` retention;
4. the question of how much of the formal rule should appear in narrative prose and how much should be kept in a technical note.

What CAPR adds is a fully explicit decomposition of the rule into heavy disyllabic, trisyllabic, hiatus, and final-`x` branches, together with local chronology testing against OE i-umlaut and later unstressed-long-vowel shortening.

## 4. Formal implementation

The immediately preceding helper used by the rule is:

```foma
define OEAnyConsonant [EnglishStarConsonant | EnglishPalatalConsonant];
```

The rule itself is long, but it is useful to quote in full because the branching is exactly what later prose will need to simplify without distorting:

```foma
define OEHighVowelApocope [
    # Disyllabic: long syllable (long vowel + consonant(s)) + final vowel
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ .#.,
    # Disyllabic: diphthong + consonant(s) + final vowel
    # LONG diphthongs are heavy (any C count). SHORT diphthongs are heavy only
    # with 2+ consonants; a short diphthong + single C is a LIGHT syllable.
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ _ .#.,
    # Disyllabic: heavy closed syllable (short vowel + 2+ consonants) + final vowel
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ _ .#.,
    # Trisyllabic: long/diphthong + unstressed syllable + final vowel
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongVowel OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic with short-diphthong first syllable
    {*i} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortDiphthong OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic: short syllable + another syllable + final vowel
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Trisyllabic with heavy-by-position first syllable
    {*i} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*u} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    {*ų} -> 0 || EnglishStarShortVowel OEAnyConsonant OEAnyConsonant+ EnglishStarShortVowel OEAnyConsonant+ _ .#.,
    # Vowel-hiatus contraction: word-final *i after long vowel
    {*i} -> 0 || EnglishStarLongVowel _ .#.,
    # Final -u/-i loss after *x
    {*u} -> 0 || {*x} _ .#.,
    {*ų} -> 0 || {*x} _ .#.,
    {*i} -> 0 || {*x} _ .#.
];
```

The historical core of this implementation is straightforward: heavy-syllable and trisyllabic high-vowel loss. The more model-specific parts are the explicit **vowel-hiatus** and **final-`x`** subclauses, which are reasonable internal formalizations but more granular than the standard handbook presentation. For the eventual chapter, those should probably be presented as technical refinements of a classical rule rather than as the main historical claim.

## 5. Place in the cascade

The main cascade slice is:

```foma
.o. OEIUmlaut
.o. OEWsPalatalDiphthongization
.o. OEJClusterCoalescence
.o. OENasalDissimilation
.o. OEBackMutation
.o. OEWsPalatalUmlaut
.o. OEWeakTailNasalLoss
.o. OEWeightMarkers
.o. OEHighVowelApocope
.o. NWGmcInStemNLoss
```

The export layer and chronology cards then extend the local picture further right to SC072:

1. **core:** `SC054 < SC063`
2. **core:** `SC055 < SC063`
3. **core:** `SC063 < SC072`
4. **contextual:** none

This placement matters for different reasons on each side.

On the left, SC054 and SC055 show that high-vowel apocope belongs after earlier glide and umlaut-sensitive developments. The SC055 boundary is especially important because moving SC063 before i-umlaut destroys outcomes like `cȳ` and `brȳd`. SC054 contributes a narrower but still useful local anchor: `*sáiwiz` (`sea`) shows that OE W Loss Before I must already have happened before SC063.

On the right, SC072 shows that SC063 is still not the end of weak-tail history. The apocope rule must precede later unstressed long-vowel shortening; otherwise forms like `fyrhte` collapse to `fyrht`.

So SC063 is best described as a **late but not final** weak-tail rule: late enough to follow earlier umlaut and neighboring weak-tail preparations, but earlier than the last cleanup of unstressed long vowels.

## 6. Order-testing evidence

The chronology card gives a **safe computational window of `56-71`**.

- **earlier boundary:** `SC055` OE I Umlaut
- **representative failures:** `belly; birth; breeches; bride; cow`
- **later boundary:** `SC072` OE Unstressed Long Vowel Shortening
- **representative failure:** `fright`

The card's own evidence is **local historical evidence on both sides**, but the wider export network is not fully reciprocal. The graph layer records `SC054 < SC063`, `SC055 < SC063`, and `SC063 < SC072` as core edges, yet these are currently supported one-sidedly rather than as full reciprocal pairs. That does not make them weak; it just means the current testing corpus has supplied the strongest explicit support from one side of the relation.

What the testing **does** show is that SC063 is tightly integrated into a late cluster of weak-tail and umlaut-sensitive operations:

1. it must follow OE i-umlaut;
2. it must precede later unstressed-long-vowel shortening;
3. it already has a narrower left-side dependency involving OE W Loss Before I.

What it **does not** prove is every detail of the wider historical theory of unstressed-vowel loss. The computational evidence shows where the live transducer stops matching baseline outputs. The literature must still do the heavier interpretive work when distinguishing apocope from syncope, evaluating Mercian `-u` retentions, or deciding how prominently to treat the final-`x` and hiatus branches.

## 7. Interpretation for the book

For the book, SC063 should be treated as one of the decisive late weak-tail reductions of prehistoric Old English. It is not simply "final vowel deletion"; it is a weight-sensitive and structure-sensitive rule whose outputs make many familiar Old English forms look shorter and more morphologically compact than their earlier stages.

The chapter should emphasize two things at once. First, this is a very well-supported traditional rule: the literature is unusually consistent on its main conditioning. Second, the CAPR formalization shows that once one tries to implement the rule across a large derivational corpus, apparently simple apocope quickly ramifies into a cluster of heavy/light, trisyllabic, hiatus, and final-`x` decisions. That combination makes SC063 an excellent pilot for how the book should move between historical phonology and formal modeling.

## 8. Relation to neighbouring changes

1. **SC054 OE W Loss Before I:** local earlier anchor from the `sea` derivation; shows that the glide-loss window precedes apocope.
2. **SC055 OE I Umlaut:** strongest left-side historical boundary in the SC063 card; critical for `cȳ`, `brȳd`, and similar umlaut-triggered outputs.
3. **SC072 OE Unstressed Long Vowel Shortening:** later historical boundary; shows SC063 is not the end of the weak-tail story.
4. **Medial syncope rules nearby in the literature:** especially important interpretively even where they are not the immediate export neighbors.
5. **Weak-tail reduction more broadly:** SC063 should be narrated as one component in a larger late cluster, not as a self-sufficient final cleanup of unstressed vowels.

## 9. Remaining uncertainty

1. The boundary between **apocope** and **medial syncope** still needs careful narrative handling.
2. The **trisyllabic branch** is the most delicate part of the rule and is a likely place for later refinement.
3. The special **final-`x`** and **vowel-hiatus** clauses are plausible, but they are more model-specific than the core handbook rule and may deserve a separate technical note.
4. Luick and Fulk quotations are good enough for dossier work, but the dossier itself already recommends a later page-image check before final-volume quotation.
5. The local export edges are strong, but not all are reciprocal yet; later review may still sharpen the left and right network around SC063.

## 10. Proposed book-section outline

1. **OE High Vowel Apocope and the late weak-tail system**
2. **The basic rule: loss of final high vowels after heavy syllables**
3. **Why trisyllables matter**
4. **How the CAPR implementation expands the classical rule**
5. **Relation to OE I Umlaut**
6. **Relation to OE W Loss Before I**
7. **Relation to later unstressed-vowel shortening**
8. **What the order-testing evidence confirms**
9. **Where apocope shades into syncope and other weak-tail processes**
