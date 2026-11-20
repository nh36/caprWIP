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

## SC047 three-decision follow-up: unchanged SC112 before early loss

## Identity

19 November2026; control634a1335; PR #19 remains open.
## Question

Can the existing general stressed monosyllabic rule precede the proposed
early SC047 while preserving its applications? Earlier population and
score measurements above remain dated evidence.

## Current state (before any edits)

The394-row control has exactly two SC112 applications, there2333 and
where2334.

## Literature

Hill2017 pp.142–148 argues from monosyllabic local versus
directional forms, with additional levelling assumptions for the
Scandinavian comparison. Ringe–Taylor2014 p.65 allows deictic stress
or reanalysis involving here; Stiles2013 pp.15–16 lists the long
adverbs without independently proving the general law. The two
selected words alone therefore do not decide these interpretations.
Fulk2018 pp.56–57 compares short OE/OS dor and OHG tor: the selected
neuter a-stem is distinct from feminine duru.

## Diagnosis

Keep the rule's conditioning fixed and move only SC112 in the already
controlled SC017-before-pre-gemination-SC047 trial. It now sees *dórą,
does not apply, and subsequent apocope yields dor. Without the move
it sees *dór and incorrectly gives dōr. There/where still lengthen
*þár/*xwár to *þār/*xwār and front to þǣr/hwǣr. Secondary r from z
is not yet present. Disyllabic, unstressed, secondary-stress,
already-long, z-final and still-suffixed controls remain unchanged.

## Historical analysis

The generalization remains stressed short vowel before final r in a
monosyllable; no word or grammatical category conditions it.
The early working scope remains qualified West Germanic, without
a new absolute date. A placement before rhotacism excludes secondary r;
a placement before the experimental apocope excludes still-suffixed
dorą. Neither computational exclusion independently proves a calendar
date or a strict historical edge. Deictic stress and reanalysis are
published alternatives, not silently installed analogy operations.

## Verdict

Registry-verdict: SC112=RETAIN

The candidate returns to precisely the original two firing identities.
This permits SC112 before early SC047 and identifies an implementation
prerequisite, not a new strict historical edge. Production body/order
stay unchanged because production SC047 is retained.

## Propagation (only after verdict)

The reader, chronology card and current registry notes are updated.
The full seven-way corpus comparison and staged observations are in
[three-decision evidence](../literature_dossiers/sc047_three_decisions/README.md).
Reader/card/current notes distinguish evidence for the generalization
from evidence for its date. No SC015/SC024 relation is promoted.

## Residue

Exact date, scope, deictic versus phonological interpretation and the
pan-Germanic extension remain qualified. No new regression compiler,
fixture or routine sweep is added; the archived experiment records
the actual research cost.
