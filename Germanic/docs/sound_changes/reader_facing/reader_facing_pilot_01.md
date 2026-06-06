# Reader-facing sound-change pilot

_This assembled pilot PDF is for checking the first reader-facing rewrite layer of the sound-change half._

## Included sections

1. Velar palatalization before front vowels
2. The Old English i-umlaut and its West Saxon right edge
3. Nasal dissimilation

# Velar palatalization before front vowels

## Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440].

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and *sk had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1].

Taken together, these accounts show a gradual tightening of focus. Luick treats
palatalization as a broad early movement. Campbell distinguishes more sharply
between plain velars and the `sk` complex. Ringe and Taylor then place the plain
velar change in an explicit sequence that leads forward to later West-Saxon
diphthongization. The literature therefore supports two claims at once: the
change belongs to a larger palatalizing environment, and it must be kept
distinct from neighboring processes if the sequence of developments is to be
described accurately.

## Palatalization of k before front vowels and j (`OEVelarPalatalizationKFront`) {#rule-OEVelarPalatalizationKFront}

The first part of the implementation isolates the `k`-side environments of the
change.

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
```

In prose, the rule turns plain `k` into a palatal outcome before front vowels
and `j`, including the geminated environment before `j`.

Historically, this section corresponds to the core of the older discussion of
palatalized velars. It is the part of the process that prepares forms such as
those later assumed by [velar palatalization before front vowels
(`OEVelarPalatalization`)](#rule-OEVelarPalatalization) and, farther on, by
[fronting under i-umlaut (`OEIUmlautFronting`)](#rule-OEIUmlautFronting).

Within the present implementation, this helper rule is not ordered separately
from the broader velar-palatalization rule below. Its chronology is therefore
that of the larger rule it feeds.

## Velar palatalization before front vowels (`OEVelarPalatalization`) {#rule-OEVelarPalatalization}

The broader rule adds the `g` environments and composes them with the `k`
palatalization rule above.

```foma
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

In prose, the rule palatalizes plain `k` and `g` in front-vocalic and
`j`-adjacent environments. Writing it as a separate rule clarifies the relative
order of plain-velar palatalization, `sk`-palatalization, and umlautal
developments.

The rule belongs after the earlier syncope that prepares forms like _stretch_
and before the later umlautal rules that would otherwise over-palatalize forms
such as _cow_ and _lung_. See [fronting under i-umlaut
(`OEIUmlautFronting`)](#rule-OEIUmlautFronting) and [the composite i-umlaut rule
(`OEIUmlaut`)](#rule-OEIUmlaut) below.

If the rule is moved too early, before the syncope that prepares the consonant
cluster, it breaks the derivation of _stretch_. With PGmc *\*strákkijaną* in the
wrong order, the model produces *strecċan*; the expected Old English form is
*streċċan*.

If it is moved too late, after i-umlaut, it over-palatalizes forms such as
_cow_ and _lung_. PGmc *\*kūi* then yields *ċȳ*; the expected form is *cȳ*.
PGmc *\*lúnganjō* yields *lunġen*; the expected form is *lungen*.

Once the rule is in place, plain velars before front vowels and `j` no longer
remain plain. They become the palatal outcomes presupposed by later
developments, including the umlautal rules discussed in
[fronting under i-umlaut (`OEIUmlautFronting`)](#rule-OEIUmlautFronting).
That matters for dictionary-like forms such as *cild* or *dæg* and for the
broader relation between consonantal palatalization and later vowel-fronting
processes [@Luick1914, p. 157, §168; @Campbell1959, p. 278, §440;
@RingeTaylor2014, pp. 203--215, §§6.4.1, 6.5.1].

The evidence places the rule within a wider palatalizing environment, but it
does not require every neighboring palatal process to be merged with it. `sk`
belongs to a related but distinct development, and the later umlautal material
poses a different historical problem. The relation to the earlier syncope rule
is likewise specific and limited: the _stretch_ evidence shows a real dependency
without turning the feeder process into a coequal sound law of the same scope.

\newpage

# The Old English i-umlaut and West Saxon palatal diphthongization

## Historical discussion

Luick gives the change its traditional scale:

> Der wichtigste Fall von palataler Beeinflussung … war die Veränderung der
> urenglischen Vokale durch i oder j der Folgesilbe.
>
> [@Luick1914, pp. 166--167, §182]

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

The sequence of discussion is fairly clear. Luick, Campbell, and Hogg all give
i-umlaut primary importance. Ringe and Taylor and Fulk then help separate that
major change from the narrower West-Saxon diphthongization that stands beside
it. The literature therefore establishes a large, system-wide umlautal change
and a narrower adjoining process affecting words after initial palatals. That
distinction matters because the two processes act in different environments and
produce different lexical consequences.

## Fronting under i-umlaut (`OEIUmlautFronting`) {#rule-OEIUmlautFronting}

The first component of the implementation handles the broad fronting of vowels
under the influence of following `i` or `j`.

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
```

In prose, the rule fronts and raises the relevant simple vowels when a following
`i` or `j` provides the trigger.

Historically, this is the most central part of the umlautal development
described by Luick, Campbell, Hogg, Ringe and Taylor, and Fulk. Within the
present implementation it stands after [velar palatalization before front vowels
(`OEVelarPalatalization`)](#rule-OEVelarPalatalization) and before the narrower
West-Saxon palatal-diphthongization rule discussed below.

As a component rule, it shares the chronology of [the composite i-umlaut rule
(`OEIUmlaut`)](#rule-OEIUmlaut).

## Raising under i-umlaut (`OEIUmlautRaising`) {#rule-OEIUmlautRaising}

The second component handles the raising of umlauted `æ` to `e`.

```foma
define OEIUmlautRaising [
    {*æ} -> {*e} || _ EnglishIUmlautIntervening EnglishIUmlautTrigger
];
```

In plain language, this rule takes the fronted low vowel created by the earlier
fronting rule and raises it further where the same umlaut trigger still holds.

Historically, this belongs inside the same broad i-umlaut development. It is
part of the same chronological development and shares the evidence base of [the
composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut).

## Diphthongal outcomes under i-umlaut (`OEIUmlautDiphthong`) {#rule-OEIUmlautDiphthong}

The third component handles the diphthongal outcomes that also undergo
i-umlaut.

```foma
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
```

In prose, the rule states that diphthongal inputs are subject to umlaut as well:
the vowel change is not confined to simple vowels.

This matters historically because the handbooks describe i-umlaut as a
system-wide assimilatory development. The rule therefore stands inside the same
chronological bracket as [fronting under i-umlaut
(`OEIUmlautFronting`)](#rule-OEIUmlautFronting) and [raising under i-umlaut
(`OEIUmlautRaising`)](#rule-OEIUmlautRaising), even though its outputs are
shaped differently.

## The composite i-umlaut rule (`OEIUmlaut`) {#rule-OEIUmlaut}

The implementation also defines a composite rule that composes the three
preceding parts.

```foma
define OEIUmlaut OEIUmlautFronting
    .o. OEIUmlautRaising
    .o. OEIUmlautDiphthong;
```

In prose, this says that the implementation treats the umlaut as a sequence of
fronting, raising, and diphthongal adjustments composed in order.

Chronologically, the composite rule must follow [velar palatalization before
front vowels (`OEVelarPalatalization`)](#rule-OEVelarPalatalization). If it is
moved too early, forms such as _cow_ and _lung_ become over-palatalized. PGmc
*\*kūi* yields *ċȳ*; the expected form is *cȳ*. PGmc *\*lúnganjō* yields
*lunġen*; the expected form is *lungen*.

Those failures show that the broad umlautal rule needs an earlier terminus post
quem in the palatalization sequence, even though it remains the main vowel
change within the present chapter.

## West Saxon palatal diphthongization (`OEWsPalatalDiphthongization`) {#rule-OEWsPalatalDiphthongization}

The narrower West-Saxon rule is treated separately from the broader umlautal
complex.

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

In prose, this rule diphthongizes certain vowels after already palatal
consonants in West Saxon. It therefore has a narrower dialectal and
chronological scope than the broader umlaut rule.

Its place is later than [the composite i-umlaut rule (`OEIUmlaut`)](#rule-OEIUmlaut).
If this rule is moved too early, the later ordering is constrained by forms such
as _gift_ and _sheath_. PGmc *\*géftiz* then yields *ġieft*; the expected form
is *ġift*. PGmc *\*skáiθiz* yields *sċǣþ*; the expected form is *sċēaþ*.

No tested lexical item provides a comparably precise later terminus ante quem.
The available evidence therefore establishes the rule's relation to the earlier
umlautal process much more clearly than it fixes a later point by which it must
already have applied.

The two rules should accordingly be kept distinct. The broad umlautal rule
accounts for a system-wide assimilatory change; the West-Saxon rule accounts for
a narrower palatal-consonant-conditioned diphthongization whose chronological
and dialectal scope is more restricted.

\newpage

# Nasal dissimilation

## Historical discussion

Luick preserves individual outcomes such as “enitre ‘einjährig (aus *anwintri)”
without isolating a separate law around them [@Luick1914, p. 166]. Campbell
likewise reaches forms such as _heofon_ in a discussion of suffixal variation
and does not set them off in any special section on nasal dissimilation
[@Campbell1959, p. 155]. Hogg mentions _heofon_ in the course of his account of
back mutation, again without isolating a separate law [@Hogg1992, p. 112].

Fulk supplies the clearest general formulation: “In the cluster mn, the first
consonant tends to lose its nasality by dissimilation, though the results are
hardly regular” [@Fulk2018, p. 121, §6.11]. Ringe and Taylor stay close to the
lexical evidence and note that _enetre_ reflects “loss of the second *n by
dissimilation” [@RingeTaylor2014, p. 282].

The discussion therefore develops from scattered lexical observations to a more
explicit but still cautious generalization. Luick preserves the kind of form the
rule is meant to capture. Campbell and Hogg show that related outcomes enter the
handbooks, but only incidentally, as part of larger accounts of other changes.
Fulk makes the recurrent `mn` tendency explicit, while Ringe and Taylor provide
an exact lexical case in _enetre_. What emerges is a limited but recurring
dissimilatory pattern whose scope is far smaller than that of the major Old
English vowel laws.

## Nasal dissimilation in short-vowel environments (`OENasalDissimilation`) {#rule-OENasalDissimilation}

The implementation formalizes the change as a narrow rule applying in short
vowel environments before a following `n`.

```foma
define OENasalDissimilation [
    {*m} -> {*f} || EnglishStarShortVowel _ EnglishStarShortVowel {*n} [EnglishStarShortVowel | .#.]
];
```

In plain language, the rule turns medial `m` into `f` in a restricted
short-vowel environment before a following syllable containing `n`.

Historically, the rule captures the limited type of dissimilation reflected in
forms such as _heofon_, _fæstenn_, and _enetre_. It is much narrower than the
major vowel changes and is best understood as a recurring but partly lexicalized
pattern.

Chronologically, the available tests do not identify a sharper position within
the Old English sequence. When the rule is moved earlier, no lexical breakpoint
appears before the inherited West-Germanic material that precedes the tested Old
English changes. When it is moved later, the tests likewise fail to identify a
more precise later boundary within the remainder of the Old English sequence.

No comparable pair of lexical failures fixes a narrower slot here. The present
evidence therefore gives neither a precise terminus post quem nor a precise
terminus ante quem for the rule within the tested sequence.

Even so, the rule has real interpretative consequences. It provides a place in
the implementation for outcomes of the _heofon_, _fæstenn_, and _enetre_ type
discussed in the literature [@Fulk2018, p. 121, §6.11; @RingeTaylor2014,
p. 282; @Campbell1959, p. 155; @Luick1914, p. 166; @Hogg1992, p. 112]. Without
an explicit rule, those outcomes would be left to diffuse analogy or to
unexplained exception lists.

The evidence points to a narrow dissimilatory tendency, especially in
`mn`-type clusters and a small group of lexical outcomes. There is no support
for a regular change operating across a broad phonological field. The rule is
secure enough to model, but the available tests leave its position within the
Old English sequence underdetermined.

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
