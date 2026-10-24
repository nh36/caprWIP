# West Saxon palatal diphthongization

## SC056. West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

```foma
define OEWsPalatalDiphthongization FootCtx([
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʝ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
]);
```

West Saxon *gieldan* ‘pay’, *scield* ‘shield’, and *scieppan* ‘create’ show diphthongization after an already palatal consonant [@RingeTaylor2014, pp. 215--216, §6.5.1]. Their dialectal and phonological restriction separates this development from system-wide i-umlaut.

Hogg's *giefan* ‘give’ and *sceap* ‘sheep’ belong to the same palatal-consonant environment [@HoggPhonology1992, p. 112]. Fulk likewise assigns this diphthongization a place before front mutation and distinguishes the two processes [@Fulk2018, p. 74, §4.13].

The relevant beginning is that of a headed stress foot, not necessarily
the word. Hogg's *sċeaft* 'shaft' and *ġesċeaft* 'creation' both have
diphthongization in the stressed root after the sh-sound. The weak first
vowel of *ġesċeaft* 'creation' does not diphthongize after the initial
j-sound. The context operation in the printed rule preserves an explicitly
identified pretonic syllable and applies the ordinary rule to the following
headed domain. It does not suppress diphthongization throughout a prefixed
word or infer weakness from a missing late accent
[@HoggGrammar1992, §5.48 n. 1 (held 2011 reprint, p. 104)].

This foot-based reformulation retains ordinary diphthongization before
mutation; it does not reopen the separate later treatment of mutation
products. Its complementary pretonic vocalism is discussed under
[SC035 OEPrefixAReduction](#rule-OEPrefixAReduction).

The ordinary live applications comprise *ġiefan* 'give', *ġiest* 'guest',
*sċeaft* 'shaft', *sċieran* 'shear', *sċēap* 'sheep',
*sċield* 'shield' and *ġēar* 'year'. Gift is unchanged at this rule because
its selected vowel already reflects earlier raising. Sheath changes from the mutation product
\emph{*ǣ} to \emph{*ēa}; it supplies evidence for the later *sċ* layer, not
the date of the ordinary treatment represented by the other examples.

The adopted ordinary process precedes mutation and preserves the split-
diphthong and high-i negative controls. The reported absence of a later
displacement failure supplies no positive historical terminus.
