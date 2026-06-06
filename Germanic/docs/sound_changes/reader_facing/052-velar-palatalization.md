# Velar palatalization before front vowels

_Internal rule and chronology card: `OEVelarPalatalization` (`SC052`)._

## 1. Historical discussion

Older German scholarship places this change inside a broad early palatal phase.
Luick opens the relevant sequence with the heading **“Frühe Verschiebungen in
palataler Richtung”** and immediately treats English `k` and `g` before bright
vowels as part of that field [@Luick1914, §168]. The older tradition is not
wrong to frame the matter broadly: plain velars, `sk`, and later palatal
effects do belong to one neighborhood.

Newer English-language scholarship is more explicit about the sequencing inside
that neighborhood. Ringe and Taylor write that **“After initial velars and *sk
had been palatalized”** later West-Saxon diphthongization follows, which makes
plain velar palatalization a real earlier consonantal stage rather than a mere
side note [@RingeTaylor2014, §6.5.1]. Campbell likewise distinguishes plain
velars from the broader `sk` complex when he notes that **“[sk] is more prone to
palatalization and assibilation than [k]”** [@Campbell1959, §440].

The result is a familiar historical picture: the older tradition gives the
large palatal field, while the newer English handbooks make it easier to isolate
plain velar palatalization as a distinct step within that field.

## 2. Comparison of the traditions

The German and English traditions agree on the phenomenon but weight it
differently.

Luick's prose is large-scale and architectural. It describes an early movement
toward palatal articulation and then places later vowel changes to the right of
that region [@Luick1914, §§168--183]. Campbell, Hogg, and especially Ringe and
Taylor are more explicit about internal differentiation: plain velars, `sk`,
and later front-mutation material are related, but they are not identical
processes [@Campbell1959, §170; @Hogg1992, pp. 106--107, 111--114;
@RingeTaylor2014, §§6.4.1, 6.5.1, 6.6.1--6.6.4].

That comparison matters for the present chapter. The change is substantial
enough to deserve its own reader-facing section, but it should still be
explained as part of the larger palatalization-to-umlaut corridor rather than as
a self-contained sound law detached from its neighbors.

## 3. Formalization in the present project

The present implementation expresses the change with one helper definition for
plain `k` and a second block for plain `g`:

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

The order-sensitivity work gives this change a concrete local chronology.

Placed too early, before Sievers-law syncope, it breaks the derivation of
_stretch_. With PGmc *\*strákkijaną* in the wrong order, the model produces
*strecċan* instead of the expected Old English *streċċan* [Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md].

Placed too late, after i-umlaut, it over-palatalizes forms such as _cow_ and
_lung_. The chronology card records that PGmc *\*kūi* then yields *ċȳ* instead
of expected *cȳ*, and PGmc *\*lúnganjō* yields *lunġen* instead of expected
*lungen* [Germanic/docs/sound_changes/order_tests/chronology_cards/SC052-oe-velar-palatalization.md].

That is the reader-facing reason for the rule's present position: it must come
after the syncope that prepares forms like _stretch_, but before the umlautal
stage that would otherwise create the wrong palatalized outputs in _cow_ and
_lung_.

## 5. Consequences for reconstructed forms

Once the rule is in place, plain velars before front vowels and `j` no longer
remain plain. They become the palatal outcomes that later chapters presuppose.
That matters not only for dictionary-like forms such as *cild* or *dæg*, but
also for the broader relation between consonantal palatalization and later
vowel-fronting processes [@Campbell1959, §170; @RingeTaylor2014, §6.4.1].

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
