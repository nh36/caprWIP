# Reader-facing sound-change pilot

_This assembled pilot PDF is for checking the first reader-facing rewrite layer of the sound-change half._

## Included sections

1. Velar palatalization before front vowels
2. The Old English i-umlaut and its West Saxon right edge
3. Nasal dissimilation

# Velar palatalization before front vowels

## 1. Historical discussion

Older German scholarship places this change inside a broad early palatal phase.
Luick introduces the whole region under the heading “Frühe Verschiebungen in
palataler Richtung” and immediately treats English `k` and `g` before bright
vowels as part of that field [@Luick1914, p. 157, §168]. The older tradition is
not wrong to frame the matter broadly: plain velars, `sk`, and later palatal
effects do belong to one neighborhood.

Newer English-language scholarship is more explicit about the sequencing inside
that neighborhood. Ringe and Taylor write that “after initial velars and *sk
had been palatalized” later West-Saxon diphthongization follows, which makes
plain velar palatalization a real earlier consonantal stage rather than a mere
side note [@RingeTaylor2014, p. 215, §6.5.1]. Campbell likewise distinguishes
plain velars from the broader `sk` complex when he notes that “[sk] is more
prone to palatalization and assibilation than [k]”
[@Campbell1959, p. 278, §440].

The result is a familiar historical picture: the older tradition gives the
large palatal field, while the newer English handbooks make it easier to isolate
plain velar palatalization as a distinct step within that field.

## 2. Comparison of the traditions

The German and English traditions agree on the phenomenon but weight it
differently.

Luick's prose is large-scale and architectural. It describes an early movement
toward palatal articulation and then places later vowel changes to the right of
that region [@Luick1914, pp. 157--167, §§168--182]. Campbell and Ringe and
Taylor are more explicit about internal differentiation: plain velars, `sk`,
and later front-mutation material are related, but they are not identical
processes [@Campbell1959, p. 278, §440; @RingeTaylor2014, pp. 203--215,
§§6.4.1, 6.5.1].

That comparison matters for the present chapter. The change is substantial
enough to deserve its own reader-facing section, but it should still be
explained as part of the larger palatalization-to-umlaut corridor rather than as
a self-contained sound law detached from its neighbors.

## 3. Formalization in the present project

The implementation formalizes the change with one helper definition for plain
`k` and a second block for plain `g`:

```foma
define OEVelarPalatalizationKFront [
    {*k} -> {*ʧ} || .#. _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || _ [{*i} | {*ī}],
    {*k} -> {*ʧ} || _ {*ḯ},
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || {*ḯ} _ EnglishStarFrontVowel,
    {*k} -> {*ʧ} || [{*i} | {*ī}] _ .#.,
    {*k} -> {*ʧ} || {*ḯ} _ .#.
] .o. [
    {*k} {*k} -> {*ʧ} {*ʧ} || _ {*j}
] .o. [
    {*k} -> {*ʧ} || _ {*j}
] ;

define OEVelarPalatalization [
    OEVelarPalatalizationKFront
] .o. [
    {*g} -> {*ʤ} || _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ .#.,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ EnglishStarFrontVowel,
    {*g} -> {*ʤ} || EnglishStarFrontVowel _ [EnglishStarConsonant - {*j}],
    {*g} {*g} -> {*ʤ} {*ʤ} || _ {*j}
] .o. [
    {*g} -> {*ʤ} || _ {*j}
];
```

In prose, the rule does exactly what the title suggests: it palatalizes plain
`k` and `g` in front-vocalic and `j`-adjacent environments. The point of
writing it as a separate rule is not to deny the larger palatal field, but to
make the relative order of plain-velar palatalization, `sk`-palatalization, and
umlautal developments testable.

## 4. Chronological placement

The chronology can be tested by moving the rule in either direction.

Placed too early, before the syncope that prepares the consonant cluster, it
breaks the derivation of _stretch_. With PGmc *\*strákkijaną* in the wrong
order, the model produces *strecċan* instead of the expected Old English
*streċċan*.

Placed too late, after i-umlaut, it over-palatalizes forms such as _cow_ and
_lung_. PGmc *\*kūi* then yields *ċȳ* instead of expected *cȳ*, and PGmc
*\*lúnganjō* yields *lunġen* instead of expected *lungen*.

That is the reader-facing reason for the rule's present position: it must come
after the syncope that prepares forms like _stretch_, but before the umlautal
stage that would otherwise create the wrong palatalized outputs in _cow_ and
_lung_.

## 5. Consequences for reconstructed forms

Once the rule is in place, plain velars before front vowels and `j` no longer
remain plain. They become the palatal outcomes that later chapters presuppose.
That matters not only for dictionary-like forms such as *cild* or *dæg*, but
also for the broader relation between consonantal palatalization and later
vowel-fronting processes [@Luick1914, p. 157, §168; @Campbell1959, p. 278,
§440; @RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1].

In other words, the rule is consequential because it creates the consonantal
environment inherited by the umlaut chapter. Without it, later reconstructed
forms are not merely shifted in date; they come out with the wrong consonant
quality.

## 6. Remaining cautions

This section should remain narrow.

It is not a chapter on every Old English palatal development. `sk` belongs to a
related but not identical part of the tradition, and the later umlaut chapter is
still a different historical problem. Nor should the left-hand relation to
Sievers-law syncope be inflated into a larger joint chapter: the _stretch_
evidence shows a real dependency, but it does not turn the feeder process into a
coequal historical unit.

\newpage

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

\newpage

# Nasal dissimilation

## 1. Historical discussion

This is not a chapter-sized textbook sound law. The strongest newer
English-language formulation recovered in the local sources is Fulk's cautious
statement: “In the cluster mn, the first consonant tends to lose its nasality
by dissimilation, though the results are hardly regular”
[@Fulk2018, p. 121, §6.11].
That is already a warning about scale: the phenomenon is real, but not neat or
uniform.

The older German material is thinner and more lexical. Luick preserves outcomes
such as “enitre ‘einjährig (aus *anwintri)” rather than building a separate
chapter around them [@Luick1914, p. 166]. Campbell and Hogg likewise reach
forms such as _heofon_ in other discussions without isolating a major Old
English “nasal-dissimilation” law [@Campbell1959, p. 155; @Hogg1992, p. 112].

The historical discussion must therefore begin by lowering expectations. The
change belongs in the book because the sources preserve scattered evidence for
the pattern, not because the handbooks present it as a major canonical law.

## 2. Comparison of the traditions

The contrast between traditions is instructive.

Newer English-language scholarship, especially Fulk, is willing to formulate a
general tendency in `mn` clusters, while immediately warning that the results
are irregular [@Fulk2018, p. 121, §6.11]. Ringe and Taylor are more lexical
still: their clearest direct statement is simply that *enetre* reflects “loss of
the second *n by dissimilation” [@RingeTaylor2014, p. 282]. The older German tradition,
represented here by Luick, preserves useful lexical traces but does not make
them into a chapter heading [@Luick1914, p. 166].

That comparison is the right historical scale for the present section. The rule
is not fictitious, but it is better treated as a residual pattern than as a
large named law comparable to i-umlaut or breaking.

## 3. Formalization in the present project

The implementation isolates the change very narrowly:

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

The code targets medial `m` in a short-vowel environment before a following
syllable containing `n`, and it rewrites that `m` as `f`. This is a stricter and
more explicit formulation than the handbooks usually give. That explicitness is
useful for the implementation, but it should not be mistaken for evidence that
the traditional scholarship isolates exactly the same rule in exactly the same
shape.

## 4. Chronological placement

The current chronology evidence is negative in both directions.

When the rule is moved earlier, the present tests find no lexical breakpoint
before the inherited West-Germanic material that lies to the left of the Old
English sequence. When it is moved later, they likewise fail to identify a
narrower lexical boundary before the far right edge of the tested Old English
sequence.

That means the chapter cannot be written like the stronger pilot cases. There is
no _stretch_, _cow_, or _gift_-style failure here to prove a narrow local slot.
The honest statement is simpler: the search found **no lexical evidence for a
narrower earlier or later boundary** within the tested window.

## 5. Consequences for reconstructed forms

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the _heofon_, _fæstenn_, and _enetre_ type
discussed in the literature [@Fulk2018, p. 121, §6.11; @RingeTaylor2014, p. 282;
@Campbell1959, p. 155; @Luick1914, p. 166; @Hogg1992, p. 112]. Without an
explicit rule, those outcomes would be left to diffuse analogy or to unexplained
exception lists.

The consequence is therefore modest but real. The rule marks a narrow, partly
lexicalized dissimilation tendency inside the larger Old English system. It does
not reorganize the whole chronology, but it keeps a historically attested type
of development visible in the model.

## 6. Remaining cautions

This section should stay short.

The literature does not justify treating nasal dissimilation as a chapter center
of the same rank as the major textbook sound laws. Nor do the present tests
justify a narrow slot fixed by lexical breakpoints on both sides. The right
reader-facing stance is therefore deliberately modest: the rule is explicit in
the present implementation, historically supported in scattered examples, and
chronologically underdetermined within the tested range.

\newpage

# Reader-facing pilot source note

## Style-model files consulted

- `Germanic/docs/lexeme_reports/writing_skill/README.md`
- `Germanic/docs/lexeme_reports/writing_skill/book_entry_template.md`
- `Germanic/docs/lexeme_reports/model_entries/2183-shoulder-sċuldrum.model.md`

## Pilot source files consulted

### General sound-change sources

- `Germanic/docs/sound_changes/change_reports/full/052-velar-palatalization-hinge.md`
- `Germanic/docs/sound_changes/change_reports/full/055-056-umlaut-core.md`
- `Germanic/docs/sound_changes/change_reports/full/058-oe-nasal-dissimilation-residual-note.md`
- `Germanic/docs/sound_changes/literature_dossiers/052-velar-palatalization-hinge.dossier.md`
- `Germanic/docs/sound_changes/literature_dossiers/055-056-umlaut-core.dossier.md`
- `Germanic/docs/sound_changes/literature_dossiers/058-oe-nasal-dissimilation-residual.dossier.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC055-oe-i-umlaut.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC056-oe-ws-palatal-diphthongization.md`
- `Germanic/docs/sound_changes/order_tests/chronology_cards/SC058-oe-nasal-dissimilation.md`
- `Germanic/fsts/germanic.txt`

### Reference texts checked directly

- `docs/references/campbell_old_english_grammar.txt`
- `docs/references/hogg_vol1.txt`
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`
- `docs/references/luick_historische_grammatik.txt`
- `docs/references/fulk_comparative_grammar_early_germanic.vision.txt`
- `docs/references/fulk_comparative_grammar_early_germanic.pdf`

## Citation verification note

For the revised pilot chapters, page citations were checked against the local
text witnesses and, where useful, against the repository PDF witness as well.

## Scope of the pilot

The pilot is intentionally small. It tests reader-facing section design,
quotation method, code presentation, and chronology explanation before any
full-volume rewrite is attempted.
