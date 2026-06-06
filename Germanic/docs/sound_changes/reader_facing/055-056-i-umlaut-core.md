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
