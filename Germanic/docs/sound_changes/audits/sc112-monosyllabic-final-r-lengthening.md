# SC112: stressed monosyllabic lengthening before inherited final *r

Registry-verdict: SC112=RETAIN

## Adjudication

Old English *þǣr* ‘there’ and *hwǣr* ‘where’ are admitted as two
source-backed short-*a* witnesses. Their experimental antecedents are
`*θár` and `*xwár`; the source package records the attested forms and the
remaining disagreement about whether the quantity is inherited from an
earlier stage or reflects later lengthening. The corpus therefore records a
qualified input and does not claim a Proto-Germanic date.

The smallest general formalization is stressed monosyllabic vowel
lengthening before inherited final *r*. It is placed in the early working
corridor immediately before rhotacism so that secondary *r* < *z* cannot
feed it. The preceding-vocalic guard excludes disyllabic forms. This
position is an executable modeling choice, not a demonstrated strict
chronology edge against SC015 or SC024.

The bounded comparison rejected the later alternatives as less explanatory:
the intermediate placement produces *þār* and *hwār*, while the late
placement requires post-brightening *æ* handling and additionally changes
the existing *door* output. The early placement produces both admitted
targets and leaves all 387 prior selected outputs unchanged.

## Rule

```foma
define PNWGmcMonosyllabicFinalRLengthening [
    [
        {*á} -> {*ā},
        {*é} -> {*ē},
        {*í} -> {*ī},
        {*ó} -> {*ō},
        {*ú} -> {*ū}
        || .#. EnglishStarConsonant* _ {*r} .#.
    ]
];
```

The rule is general, not lexical. It does not establish that SC015
preceded lengthening: neither admitted witness contains *i*. The source
ledger and machine-readable three-placement receipt remain the evidence
record for this adoption.
