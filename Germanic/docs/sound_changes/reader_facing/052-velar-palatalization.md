# Velar palatalization before front vowels

## Historical discussion

Luick places the change inside a broad early palatalizing movement. Under the
heading “Frühe Verschiebungen in palataler Richtung,” he treats English `k` and
`g` before bright vowels together with the larger field of palatal effects
[@Luick1914, p. 157, §168]. His emphasis falls on the environment first: velars
before bright vowels and in the vicinity of the palatal glide belong to one
early phonological corridor. The examples associated with that corridor, such as
`ceaster`, `geaf`, `giefan`, and `giest`, already show that consonantal
palatalization and later vowel effects stand close together historically, even
when they must be distinguished analytically [@Luick1914, pp. 157--167,
§§168--182].

Campbell narrows the picture by distinguishing plain velars from the especially
palatal-prone `sk` cluster. His remark that “[sk] is more prone to
palatalization and assibilation than [k]” is brief, but it makes clear that
different members of the larger palatal field need not behave identically
[@Campbell1959, p. 278, §440]. Elsewhere in the same part of the grammar he uses
forms such as `cild`, `dæg`, `giefan`, and `giest`, which show how palatalized
velars, palatal influence, and later umlautal outcomes meet in the same region
of the lexicon without collapsing into one process [@Campbell1959, pp. 69--72,
89, §§170, 190--191].

Hogg makes the conditioning sharper still. He states that the change takes place
when the velar consonant is adjacent to and in the same syllable as a front
vowel or the palatal consonant `j` [@Hogg1992, pp. 103--104]. This formulation
is important because it moves the discussion from a broad list of palatal
outcomes to a more precise phonological environment involving adjacency and
syllable structure.

Ringe and Taylor make the chronological relation still clearer. When they write
that “after initial velars and *sk had been palatalized” West-Saxon
diphthongization follows, plain velar palatalization becomes an earlier
consonantal stage presupposed by later vowel developments
[@RingeTaylor2014, p. 215, §6.5.1]. Their own examples of the plain-velar rule,
such as `weccan`, `licgan`, `lecgan`, `secg`, `ecg`, `wicg`, and `brycg`,
illustrate the same point in lexical detail: front vowels and `j` create the
palatal environment in which plain `k` and `g` cease to behave as plain velars
[@RingeTaylor2014, pp. 213--214, §6.4.1].

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
palatalized velars. It captures the environments behind forms such as `weccan`,
`licgan`, and `lecgan`, where front vowels or `j` trigger the palatal outcome in
the first place [@RingeTaylor2014, pp. 213--214, §6.4.1]. It is also the part
of the process that prepares forms later assumed by [velar palatalization before
front vowels
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
