# The Old English i-umlaut and its West Saxon right edge

## 1. Historical discussion

Luick gives the change its traditional scale:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> In context, this means that i-umlaut is treated as the central case of
> palatal influence in early English.

[@Luick1914, pp. 166--167, §182]

Campbell gives the most compact classical formulation in English when he writes
that “the process known as i-umlaut or i-mutation operates on practically all
the sounds which it could theoretically affect in OE”
[@Campbell1959, p. 69, §190]. Hogg continues in the same vein: “we come now to
a change which is almost as uncontroversial as it is important”
[@Hogg1992, p. 112]. Taken together, these statements leave little doubt that
i-umlaut is one of the central Old English vowel changes.

The narrower palatal-diphthongal material is described differently. Ringe and
Taylor treat West-Saxon diphthongization after initial palatals as a distinct
process [@RingeTaylor2014, p. 215, §6.5.1], and Fulk is even more explicit about
its chronological delicacy when he calls it “diphthongization by initial
palatal consonants (which precedes front umlaut but not breaking)”
[@Fulk2018, p. 74, §4.13].

## 2. Development of the discussion

The sequence of discussion is fairly clear. Luick, Campbell, and Hogg all give
i-umlaut primary importance. Ringe and Taylor and Fulk then help separate that
major change from the narrower West-Saxon diphthongization that stands beside
it. The literature therefore establishes a large, system-wide umlautal change and a
narrower adjoining process affecting words after initial palatals. That
distinction matters because the two processes act in different environments and
produce different lexical consequences.

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
_cow_ and _lung_ become over-palatalized. PGmc *\*kūi* yields *ċȳ*; the
expected form is *cȳ*. PGmc *\*lúnganjō* yields *lunġen*; the expected form is
*lungen*.

If i-umlaut is moved too late, or if West-Saxon diphthongization is moved too
early, the local right edge breaks around _gift_ and _sheath_. PGmc
*\*géftiz* then yields *ġieft*; the expected form is *ġift*. PGmc
*\*skáiθiz* yields *sċǣþ*; the expected form is *sċēaþ*.

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
[@RingeTaylor2014, p. 215, §6.5.1; @Hogg1992, p. 108]. That is why the implementation treats it as a narrower follow-on process and not
as a second main change of equal scale.

## 6. Remaining cautions

The West-Saxon diphthongal material is genuine, but it is narrower, more
dialect-specific, and less stably placed in the broader chronology than the
umlautal change itself. The evidence is therefore strongest when it is used to
distinguish the two processes and keep them from collapsing into one
undifferentiated chapter. The available tests fix the left edge well, but they
do not license a sweeping claim about the far right of the whole Old English
sequence.
