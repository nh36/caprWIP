# Reader-facing sound-change pilot

_This assembled pilot PDF is for checking the first reader-facing rewrite layer of the sound-change half._

## Included sections

1. Velar palatalization before front vowels
2. The Old English i-umlaut and its West Saxon right edge
3. Nasal dissimilation

# Velar palatalization before front vowels

## 1. Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to palatalization
and assibilation than [k]” is brief, but it makes clear that different members
of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440].

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and *sk had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1].

## 2. Development of the discussion

Taken together, these accounts show a gradual tightening of focus. Luick treats
palatalization as a broad early movement. Campbell distinguishes more sharply
between plain velars and the `sk` complex. Ringe and Taylor then place the plain
velar change in an explicit sequence that leads forward to later West-Saxon
diphthongization. The literature therefore supports two claims at once: the
change belongs to a larger palatalizing environment, but it also needs to be
kept distinct from neighboring processes if the sequence of developments is to
be described accurately.

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
`k` and `g` in front-vocalic and `j`-adjacent environments. Writing it as a
separate rule clarifies the relative order of plain-velar palatalization,
`sk`-palatalization, and umlautal developments.

## 4. Chronological placement

The chronology can be tested by moving the rule in either direction.

Placed too early, before the syncope that prepares the consonant cluster, it
breaks the derivation of _stretch_. With PGmc *\*strákkijaną* in the wrong
order, the model produces *strecċan*; the expected Old English form is
*streċċan*.

Placed too late, after i-umlaut, it over-palatalizes forms such as _cow_ and
_lung_. PGmc *\*kūi* then yields *ċȳ*; the expected form is *cȳ*. PGmc
*\*lúnganjō* yields *lunġen*; the expected form is *lungen*.

That is the reason for the rule's present position. It must come
after the syncope that prepares forms like _stretch_, but before the umlautal
stage that would otherwise create the wrong palatalized outputs in _cow_ and
_lung_.

## 5. Consequences for reconstructed forms

Once the rule is in place, plain velars before front vowels and `j` no longer
remain plain. They become the palatal outcomes that later chapters presuppose.
That matters for dictionary-like forms such as *cild* or *dæg* and for the
broader relation between consonantal palatalization and later
vowel-fronting processes [@Luick1914, p. 157, §168; @Campbell1959, p. 278,
§440; @RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1].

In other words, the rule is consequential because it creates the consonantal
environment inherited by the umlaut chapter. Without it, later reconstructed
forms come out with the wrong consonant quality.

## 6. Remaining cautions

This change belongs to a wider palatalizing environment, but the evidence does
not require every neighboring palatal process to be merged with it. `sk`
belongs to a related but distinct development, and the later umlautal
material poses a different historical problem. The left-hand relation to
Sievers-law syncope is likewise specific and limited. The _stretch_
evidence shows a real dependency without turning the feeder process into a
coequal sound law of the same scope.

\newpage

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

\newpage

# Nasal dissimilation

## 1. Historical discussion

Luick preserves individual outcomes such as “enitre ‘einjährig (aus *anwintri)”
without isolating a separate law around them [@Luick1914, p. 166]. Campbell
likewise reaches forms such as _heofon_ in a discussion of suffixal variation
and does not set them off in any special section on nasal dissimilation [@Campbell1959,
p. 155]. Hogg mentions _heofon_ in the course of his account of back mutation,
again without isolating a separate law [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that _enetre_ reflects “loss of the second *n by
dissimilation” [@RingeTaylor2014, p. 282].

## 2. Development of the discussion

The discussion therefore develops from scattered lexical observations to a more
explicit but still cautious generalization. Luick preserves the kind of form the
rule is meant to capture. Campbell and Hogg show that related outcomes enter the
handbooks, but only incidentally, as part of larger accounts of other changes.
Fulk makes the recurrent `mn` tendency explicit, while Ringe and Taylor provide
an exact lexical case in _enetre_. What emerges is a limited but recurring dissimilatory pattern whose scope is far
smaller than that of the major Old English vowel laws.

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

No comparable pair of lexical failures fixes a narrower slot here. The present
tests do not identify sharper evidence for an earlier or later position within
the Old English sequence.

## 5. Consequences for reconstructed forms

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the _heofon_, _fæstenn_, and _enetre_ type
discussed in the literature [@Fulk2018, p. 121, §6.11; @RingeTaylor2014, p. 282;
@Campbell1959, p. 155; @Luick1914, p. 166; @Hogg1992, p. 112]. Without an
explicit rule, those outcomes would be left to diffuse analogy or to unexplained
exception lists.

The consequence is therefore modest but real. The rule marks a narrow, partly
lexicalized dissimilation tendency inside the larger Old English system. It
leaves the larger chronology largely unchanged and keeps a historically
attested type of development visible in the model.

## 6. Remaining cautions

The evidence points to a narrow dissimilatory tendency, especially in
`mn`-type clusters and a small group of lexical outcomes. There is no support
for a regular change operating across a broad phonological field. The rule is secure
enough to model, but the available tests leave its position within the Old
English sequence underdetermined.

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
