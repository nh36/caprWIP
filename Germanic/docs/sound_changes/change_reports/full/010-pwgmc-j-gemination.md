# West Germanic j-gemination

### Sound-change report

#### Historical formulation

SC010 `PWGmcJGemination` isolates West Germanic consonant gemination before `*j` after a short vowel. In the compact trace it appears across several familiar families such as `hedge`, `net`, `set`, `sit`, and `will`, and the trace occurrence count is therefore appreciably larger than for some of the surrounding early PWGmc rules.

This is historically recognizable and not merely a one-lexeme convenience. Even so, the report should keep its scope narrow: the rule concerns gemination before `*j` after a light syllable, not a general discussion of all consonant doubling in early West Germanic.

#### Source tradition

Fulk treats West Germanic consonant gemination before `*j` as regular after a short vowel and states that the change applies to any consonant other than `r` (including `r < z`) in that setting [@Fulk2018, §6.15]. He illustrates the rule with a wide set of examples including OE *scieppan*, *settan*, *lecgan*, *fremman*, *wennan*, and *sellan* [@Fulk2018, §6.15].

That is strong support for the historical phenomenon itself. It is less explicit about the exact interaction with the later CAPR rules that follow it, because those interactions belong to the modeled cascade rather than to the handbooks. The current source layer is therefore good for the existence and scope of the rule, but not yet for every internal chronology edge.

#### CAPR implementation

CAPR models the gemination as a large explicit set of consonants doubling before `*j` after a short vowel:

```foma
define PWGmcJGemination [
    {*p} -> {*p} {*p} || EnglishStarShortVowel _ {*j},
    {*b} -> {*b} {*b} || EnglishStarShortVowel _ {*j},
    {*t} -> {*t} {*t} || EnglishStarShortVowel _ {*j},
    {*d} -> {*d} {*d} || EnglishStarShortVowel _ {*j},
    {*k} -> {*k} {*k} || EnglishStarShortVowel _ {*j},
    {*g} -> {*g} {*g} || EnglishStarShortVowel _ {*j},
    {*f} -> {*f} {*f} || EnglishStarShortVowel _ {*j},
    {*s} -> {*s} {*s} || EnglishStarShortVowel _ {*j},
    {*m} -> {*m} {*m} || EnglishStarShortVowel _ {*j},
    {*n} -> {*n} {*n} || EnglishStarShortVowel _ {*j},
    {*l} -> {*l} {*l} || EnglishStarShortVowel _ {*j},
    {*ŋ} -> {*ŋ} {*ŋ} || EnglishStarShortVowel _ {*j},
    {*x} -> {*x} {*x} || EnglishStarShortVowel _ {*j}
];
```

This is broader and more explicit than any single handbook example, but it follows the general historical statement closely. The exact enumerated set belongs to the CAPR implementation layer rather than to the historical source tradition.

#### Place in the cascade

In the inventory ordering, SC010 follows SC009 `PWGmcIjContraction` and precedes SC011 `PWGmcSyllabicJ`. In the live production cascade it remains part of bundled `PWGmcChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

The local implementation logic also makes SC010 important for the next rule. In CAPR, j-gemination must precede SC011 so that newly heavy stems block later syllabic-j vocalization. That interaction is part of the modeled cascade and should stay explicit in backend documentation.

#### Order evidence

Validated expanded-PWGmc first-break TSV output now exists for SC010, and the chronology card is complete. The earlier search moved safely across SC009, SC008, SC007, SC006, SC005, and SC004 to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break, so the earlier side is boundary-only.

The later search finds an immediate real break at SC011 `PWGmcSyllabicJ`: if SC010 is delayed to order `11`, PGmc `*nátją` yields `nete` instead of expected OE `nett`. That is a tight local reciprocal boundary with SC011 rather than a broad/far rightward limit.

#### Interpretation

SC010 can now stand as a cautious singleton note. The source support is good, the trace presence is substantial, and the validated order evidence recovers a tight local seam with SC011 rather than only a distant broad/far boundary.

#### Remaining cautions

The main caution is scope. The rule is well supported historically, but the earlier side remains boundary-only at the left edge of the tested expanded-PWGmc chain. Any later prose should keep the relation to SC011 visible without turning the pair into a mandatory grouped chapter or enlarging SC010 into a general consonant-doubling chapter.
