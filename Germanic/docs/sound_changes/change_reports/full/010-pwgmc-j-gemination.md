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

No validated chronology card exists yet for SC010. The current runner can test it directly with `--order-profile expanded-pwgmc`, and dry-run order inspection in this pass confirmed that SC010 resolves as the seventh rule in the expanded PWGmc order.

What is still missing is real earlier/later first-break TSV output. Until those TSVs exist, no historical boundary should yet be claimed.

#### Interpretation

SC010 is a plausible singleton backend note and likely a stronger candidate than some of the immediately preceding rules. The source support is good, the trace presence is substantial, and the implementation captures a recognized West Germanic development. What it still lacks is validated chronology output.

#### Remaining cautions

The main cautions are internal and chronological. The rule is well supported historically, but the present pass does not yet establish its exact earlier/later first-break boundaries. Any later prose should also keep the relation to SC011 visible without implying that the two rules must become a single grouped unit.
