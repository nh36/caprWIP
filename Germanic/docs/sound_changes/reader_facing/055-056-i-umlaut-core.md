# The Old English i-umlaut and its West Saxon right edge

## 1. Historical discussion

For the older German tradition, the center of this chapter is unmistakable.
Luick puts the point strongly:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> In context, this means that i-umlaut is treated as the central case of
> palatal influence in early English.

[@Luick1914, pp. 166--167, §182]

That is a strong way of saying that i-umlaut is one of the major early English
vowel changes, not a marginal local effect.

Recent English-language scholarship says the same in a different register. Fulk
describes the process as “front mutation, more commonly referred to as front
umlaut or i/j-umlaut” and treats it as a large assimilatory change affecting
much of the vowel system [@Fulk2018, pp. 61--63, §4.7]. But Fulk also gives the
crucial complication for the second half of this chapter: “diphthongization by
initial palatal consonants (which precedes front umlaut but not breaking)”
[@Fulk2018, p. 74, §4.13].

The historical discussion therefore has two layers. The chapter center is the
Old English i-umlaut itself; the West-Saxon palatal diphthongization material is
real, but it stands on the edge of the chapter and has a more complicated
chronological profile in the handbooks.

## 2. Comparison of the traditions

The traditions agree strongly on the importance of i-umlaut and less strongly on
the place of the West-Saxon diphthongal material.

Campbell and Hogg both treat i-mutation as one of the central Old English vowel
developments. Campbell begins the main section by writing that “the process
known as i-umlaut or i-mutation operates on practically all the sounds which it
could theoretically affect in OE” [@Campbell1959, pp. 69--72, §190]. Hogg is
equally clear about scale: “we come now to a change which is almost as
uncontroversial as it is important” [@Hogg1992, p. 112]. Luick likewise gives
i-Umlaut primary weight, but treats palatal diphthongization as part of a
broader palatal field rather than as a second chapter of equal scale
[@Luick1914, pp. 166--167, §182].

Ringe and Taylor and Fulk sharpen the contrast. Both recognize the West-Saxon
diphthongization material, but both place it differently in the broader textbook
chronology from the local order found by the present implementation
[@RingeTaylor2014, pp. 215, 222, §§6.5.1, 6.6.1; @Fulk2018, pp. 61--63, 74,
§§4.7, 4.13]. That is why the present chapter is best read as a major umlaut
chapter with a narrower West-Saxon right-edge follower, not as a pair of fully
equal historical laws.

## 3. Formalization in the present project

The implementation keeps the broad umlaut rule and the narrower West-Saxon
diphthongization rule separate:

```foma
define OEIUmlautFronting [
    {*a} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ā} -> {*ǣ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*e} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*o} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ō} -> {*ē} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*u} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ū} -> {*ȳ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*á} -> {*æ} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*é} -> {*i} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ó} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ú} -> {*y} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];

define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];

define OEIUmlautDiphthong [
    {*ea} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēa} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*io} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*īo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*eo} -> {*ie} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ēo} -> {*īe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éa} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*éo} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger,
    {*ío} -> {*íe} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];

define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

```foma
define OEWsPalatalDiphthongization [
    {*æ} -> {*ea} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ǣ} -> {*ēa} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*e} -> {*ie} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ē} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*é} -> {*íe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.],
    {*ḗ} -> {*īe} || .#. [{*ʧ} | {*ʤ} | {*ʃ} | {*j}] _ [EnglishStarConsonant | EnglishPalatalConsonant | .#.]
];
```

In prose, the distinction is straightforward. `OEIUmlaut` performs the broad
fronting, raising, and diphthongal adjustments caused by following `i/j`.
`OEWsPalatalDiphthongization` is much narrower: it applies at the left edge of a
word after an already palatal consonant and creates specifically West-Saxon
diphthongal outputs.

## 4. Chronological placement

The present chronology is fixed by concrete lexical failures in both directions.

If i-umlaut is moved too early, before velar palatalization, the outputs of
_cow_ and _lung_ become over-palatalized. PGmc *\*kūi* yields *ċȳ* instead of
expected *cȳ*, and PGmc *\*lúnganjō* yields *lunġen* instead of expected
*lungen*.

If i-umlaut is moved too late, or if West-Saxon diphthongization is moved too
early, the local right edge breaks around _gift_ and _sheath_. PGmc
*\*géftiz* then yields *ġieft* instead of expected *ġift*, and PGmc
*\*skáiθiz* yields *sċǣþ* instead of expected *sċēaþ*.

The crucial limit is on the later side of the West-Saxon diphthongization rule.
No tested lexical item fixes a narrower later boundary. There is therefore no
warrant for turning that negative result into a historical claim that the rule
must stand before the final stages of the sequence.

## 5. Consequences for reconstructed forms

The chapter changes the shape of reconstructed forms on a large scale. In the
umlaut rule proper, back vowels front and high vowels raise under following
`i/j`; this is why forms such as *cȳ* and *lungen* belong to the same chapter as
more familiar textbook examples like _giest_ and _giefan_ [@Campbell1959,
pp. 69--72, §§190--191; @Fulk2018, pp. 61--63, §4.7].

The West-Saxon follower has a narrower consequence. It produces the diphthongal
surface forms expected in words such as _giefan_ and _sceap_, but it does so
only after the broader umlautal setting is already in place
[@RingeTaylor2014, p. 215, §6.5.1; @Hogg1992, p. 108]. That is why the
implementation treats it as a right-edge follower rather than as a second main
chapter of equal scale.

## 6. Remaining cautions

This chapter should not flatten two different historical scales into one.

The center is i-umlaut. The West-Saxon diphthongal material is genuine, but it
is narrower, more dialect-specific, and less stably placed in the broader
handbook chronology. For that reason the reader-facing chapter should keep the
asymmetry visible: one major sound law with one narrower right-edge follower.

It should also avoid turning the negative later result for the West-Saxon
follower into a positive historical boundary. The present evidence is strong
enough to fix the local relation to the left, but not to license a sweeping
claim about the far right of the whole Old English sequence.
