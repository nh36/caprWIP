# Opening vowel prelude

### Sound-change report

> **Corrected PROTOFORM pass (supersedes the split note below).** SC014 is the
> unstressed monophthongization `*ai > *ē` (final AND nonfinal), live Foma rule
> `{*ai} -> {*ē}`. Under the production `PROTOFORM` it is **corpus-active**, with
> two dat.sg witnesses `span` (> spanne) and `meed` (> meorde) and a later
> first-break boundary at SC072 (order 69). **Read every "corpus-inert" /
> "chronology-negative" / "word-final only" below as superseded**: SC014 is
> corpus-active and covers final and nonfinal unstressed `*ai`. It executes at the
> head of the cascade (position 1), so it is no longer adjacent to SC015
> `PNWGmcILowering` (position 11). The separate stressed change is SC004
> `EAFAiMonophthongization` (`{*ái} -> {*ā}`; see
> `004-pwgmc-ai-monophthongization.md`). SC015's substantive text is unchanged.
> Implemented on branch `historical-cascade-order` (split `f59b758d`, PROTOFORM
> correction `9c71aed3`).

#### Historical formulation

`SC014-SC015` appears here as a **short, cautious opening bridge report**,
not as a claim that the traditional grammars present one robust textbook chapter
called "opening vowel prelude." The grouped report is useful for narrative shape because these are the earliest ordinary FST changes in the
volume, and the sound-change narrative reads more clearly if it begins
with an explicit opening prelude rather than jumping straight into the more
developed `SC016-SC020` corridor.

The internal hierarchy of the pair should stay explicit. SC014
**NWGmc Unstressed Ai Monophthongization** is the early opening member: it is the
word-final unstressed `*-ai > *-ē` change, historically plausible and
source-backed but **corpus-inert** (zero corpus applications), so it imposes no
chronology constraint. SC015 **NWGmc I Lowering** is the stronger member and carries
most of the report. It belongs to the broader history of early unstressed
front-vowel leveling and has one real, though broad/far, later chronology
relation through `world`.

#### Source tradition

The source tradition supports an early Northwest Germanic unstressed-vowel
prelude, but not a sharp two-step local corridor. Ringe and Taylor give the
clearest comparative statement for SC014: unstressed `*ai` was usually
monophthongized and merged with unstressed `*e` across much of the Northwest
Germanic area [@RingeTaylor2014, pp. 37--41]. Campbell independently treats
unaccented medial `ai` in West Germanic as monophthongized, though with sparse
direct evidence, which is exactly the kind of source profile that justifies
brief inclusion without overstating local chronology [@Campbell1959, §331.7].
Hogg adds the structural observation that diphthongs do not survive in Old
English unstressed syllables, reinforcing the broad historical type behind SC014
without turning it into a chapter center [@Hogg1992, p. 112].

SC015 is better anchored. Campbell states that unaccented front vowels fell
together in Old English [@Campbell1959, §369], and Hogg likewise argues that by
about 700 unstressed front vowels had broadly converged on `/e/`
[@Hogg1992, p. 117]. The `world` material then makes the rule more concrete.
Campbell records `weorold` / `weoruld` variation [@Campbell1959, §§338--339],
while Ringe and Taylor derive the word through `*weraldu > *weruld > weorold ~
worold` [@RingeTaylor2014, §6.3.3]. That does not create a tight local chapter,
but it does make SC015 a historically intelligible opening hinge rather than a
purely model-internal adjustment.

#### CAPR implementation

CAPR turns that broad unstressed-vowel background into two explicit opening
rules at the left edge of the ordinary cascade.

SC014 `PNWGmcUnstressedAiMonophthongization` removes the unstressed diphthongal
quality of `*ai`, formalizing a comparative development that the grammars
describe more diffusely. SC015 `PNWGmcILowering` then lowers or levels early
unstressed front-vowel quality farther. That sequence is more explicit than the
handbook prose, but it is still historically defensible so long as the report
states clearly that the two rules do not form a strong local reciprocal
corridor.

#### Place in the cascade

This report sits at the very opening of the volume and hands off
directly to the pilot `SC016-SC020` **Early vocalic/final corridor**.

```foma
.o. PNWGmcUnstressedAiMonophthongization
.o. PNWGmcILowering
.o. OEWsPalatalGlide
.o. PNWGmcULowering
.o. PNWGmcStressedMonosyllableORaising
.o. PNWGmcFinalLongORaising
.o. EAFFinalZDeletion
```

That immediate handoff is the main structural reason to keep the row here.
The report gives the volume an explicit opening without absorbing the `SC016-SC020` corridor to the right. Its outward links should remain restrained. Bundled
`EarlyEnglishLineChanges` bounds the earlier search space for both rules, but that is a
runner limitation rather than a positive left boundary. SC015 points forward
to SC036 through `world`, but that relation should remain a cross-reference
only, not a larger chapter claim.

#### Order evidence

The order evidence justifies the grouping only if the asymmetry remains explicit.

SC014 is source-backed but chronology-negative in current testing. The earlier
search runs safely down to bundled `EarlyEnglishLineChanges` with no real break, and the
later search finds no real break before the current search boundary at SC087.
Those results should not be rewritten into positive chronology claims. The card
supports SC014 as a brief opening note, not as a strongly bounded local law.

SC015 is the stronger member. Its earlier search is likewise runner-bounded at
bundled `EarlyEnglishLineChanges`, so that side is not a positive earlier boundary
either. The later side is real, but broad/far: SC015 must precede SC036
**OE Inter Stress Raising**. If SC015 is delayed later than SC036, the `world`
derivation yields `wuruld` rather than expected `weorold`. That is a genuine
historical ordering statement, but it is still a forward cross-reference rather
than a reason to build a non-contiguous `SC015-SC036` chapter.

Taken together, the cards support a short opening bridge with one weak
boundary-limited member and one stronger forward-looking member. They do **not**
support a local reciprocal corridor.

#### Interpretation

The value of this report is architectural as much as historical. It lets the
volume begin with explicit prose for the earliest ordinary Northwest
Germanic vowel adjustments instead of leaving the narrative to start abruptly at
the `SC016-SC020` corridor. That is enough to justify prose even though the
two members do not contribute equal weight.

SC014 should therefore stay brief: historically plausible, source-backed, and
useful as an opening note, but not a major chronology anchor. SC015 carries the
report because it belongs to the broader history of unstressed front-vowel
leveling and because its `world` relation gives the pair one real positive
ordering result. The grouped unit works best when it is described as a short
SC015-led prelude rather than as a symmetrical two-rule chapter.

#### Remaining cautions

The cautions here are straightforward but important. Do not treat bundled
`EarlyEnglishLineChanges` as a historical left boundary for either rule. Do not treat
SC014's no-break-before-boundary result as proof that it must precede the whole
rest of the half. Do not let the forward `SC015 < SC036` relation pull this
opening report into a non-contiguous chapter with the later
`SC035-SC037` bridge. And do not let the prelude duplicate the neighboring
`SC016-SC020` corridor. The report should remain exactly what it is: a
short cautious opening bridge with SC014 brief and SC015 carrying most of the
prose.
