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
