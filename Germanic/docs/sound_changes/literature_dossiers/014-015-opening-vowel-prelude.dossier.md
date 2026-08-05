# SC014-SC015 Opening Vowel Prelude -- literature dossier

> **Split note (SC004 Outcome-C).** SC014 is now a standalone early
> Proto-Northwest Germanic change — word-final unstressed `*-ai > *-ē` — split
> out of the former bundled SC004 `PWGmcAiMonophthongization`. Its live Foma rule
> is `{*ai} -> {*ē} || _ .#.` (the obsolete `{*ăi} -> {*ē}` no-op is gone), and
> it is **corpus-inert**: zero corpus applications, because no OE corpus lexeme
> carries word-final unstressed `*-ai`; its witnesses are inflectional endings.
> The general `*ai/*ái > *ā` development is now the separate SC004
> `EAFAiMonophthongization` (Chapter 3; see
> `004-pwgmc-ai-monophthongization.dossier.md`). Where the analysis below calls
> SC014 "runner-limited by bundled `PWGmcChanges`," read that as **corpus-inert**:
> the earlier limitation was an artefact of SC014 sharing a rule with the general
> change, which the split removes. SC015's substantive text is unchanged.
> Implemented on branch `historical-cascade-order` (FST split commit `f59b758d`).

## Rule metadata

- **change_ids:** SC014; SC015
- **display_names:** NWGmc Unstressed Ai Monophthongization; NWGmc I Lowering
- **FOMA rule names:** `PNWGmcUnstressedAiMonophthongization`; `PNWGmcILowering`
- **current_orders:** SC014 now executes at the head of `EarlyEnglishLineChanges` (executable position 1, the former SC004 slot); SC015 immediately precedes the pilot `SC016-SC020` early vocalic/final corridor
- **chronology card paths:**
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC014-nwgmc-unstressed-ai-monophthongization.md`
  - `Germanic/docs/sound_changes/order_tests/chronology_cards/SC015-nwgmc-i-lowering.md`
- **representative failures / witnesses:**
  - SC014: none — corpus-inert (zero corpus applications; witnesses are inflectional endings, not standalone lexemes)
  - SC015: `world`
- **local chronology summary:**
  - SC014 has no positive chronology boundary of any kind: it is corpus-inert, so no witness can be crossed in either direction.
  - SC015 has no positive earlier historical boundary: the earlier search stops at bundled `EarlyEnglishLineChanges`.
  - SC015 must precede SC036, with `world`.
  - The row is adjacent and useful as an opening prelude, but the available chronology is highly asymmetric: SC014 is corpus-inert (unconstrained), while SC015 has one real broad/far later boundary.

## Historical problem

`SC014-SC015` is the earliest compact ordinary row still left in scaffold form.
It sits immediately before the better-documented `SC016-SC020` pilot corridor,
so the book needs some way to mention both changes without pretending that the
opening pair is already a classical textbook chapter.

The asymmetry inside the row is the main editorial problem. SC014 is
historically plausible as part of early Northwest Germanic unstressed-vowel
simplification, but its current order evidence is purely boundary-limited: the
earlier side stops at bundled `PWGmcChanges`, and the later side finds no real
break before the current search limit. SC015 is stronger. Its earlier side is
still runner-limited, but its later boundary is historically interpretable:
`SC015 < SC036` through `world`, where delaying the rule yields `wuruld`
instead of expected `weorold`. The question is therefore not whether the row
matters, but whether it should eventually become a short cautious opening
bridge, or a more obviously asymmetric unit with SC014 reduced to a brief
boundary-limited note while SC015 carries most of the prose.

## Source dossier

### Ringe and Taylor 2014

- **source_key:** `RingeTaylor2014`
- **locator:** pp. 37--41; §6.3.3
- **terminology:** monophthongization of unstressed `*ai`; merger of unstressed `*ai` with `*e`; `*weraldu > *weruld > weorold`
- **short quotation:** "`unstressed *ai was usually monophthongized to *e throughout the NWGmc area`"; "`*weraldu > *weruld > WS OE weorold ~ worold`"
- **paraphrase:** Ringe and Taylor provide the clearest comparative support for both members of the row. In their early Northwest Germanic discussion they state directly that unstressed `*ai` was usually monophthongized and merged with unstressed `*e` across most of the Northwest Germanic area, illustrating the change through endings such as subjunctive `*-ai`, weak-past endings, and the dative singular of a-stems [@RingeTaylor2014, pp. 37--41]. That gives SC014 real historical substance even though the chronology card remains negative. Later, in the Old English sound-change discussion, they derive `world` through `*weraldu > *weruld > weorold ~ worold`, which gives SC015 a clear historical home inside early unstressed-medial vocalism and explains why the later `SC015 < SC036` card boundary is historically legible rather than merely computational [@RingeTaylor2014, §6.3.3].
- **conditioning:** unstressed syllables, especially endings and medial weak-vowel positions; later medial-vowel development in forms like `world`
- **chronology:** This source strongly supports the type of both changes, but it does not yield a local SC014 or SC015 chapter by itself. SC014 remains weak in chronology despite strong comparative support; SC015 gains a stronger forward-looking historical anchor.
- **examples:** `bere`; `beren`; `dege`; `hatte`; `world`
- **cautions:** The source supports a broad Northwest Germanic vocalic prelude, not a ready-made two-change chapter. It especially does not license turning the runner-bounded left edge or the broad/far SC036 relation into local chapter architecture.

### Campbell 1959

- **source_key:** `Campbell1959`
- **locator:** §331.7; §§338--339; §369
- **terminology:** unaccented medial `ai`; unaccented front-vowel merger; `weorold` / `weoruld`
- **short quotation:** "`The history of ai and au in unaccented medial syllables is difficult to determine`"; "`x, e, and i fell together in a sound written e in unaccented syllables`"; "`weorold ... weoruld`"
- **paraphrase:** Campbell is useful because he treats both the early comparative side and the specifically Old English side of the problem. In §331.7 he says that medial unaccented `ai` in West Germanic did monophthongize, even if the evidence is not abundant; that makes SC014 source-legible, but also explains why it may remain a short note rather than a chapter center [@Campbell1959, §331.7]. In §369 he states the stronger generalization that unaccented front vowels fell together as `e`, which gives SC015 a straightforward historical analogue as part of early unstressed-vowel leveling [@Campbell1959, §369]. And in §§338--339 he records forms such as `weorold` and `weoruld`, showing that the medial-vowel instability seen in the `world` derivation is not an invention of CAPR but part of the handbook record [@Campbell1959, §§338--339].
- **conditioning:** unaccented medial syllables; general unaccented front-vowel merger; later low-stress medial vocalism in words like `world`
- **chronology:** Campbell gives better historical shape to SC015 than to SC014. SC014 remains real but thinly exemplified; SC015 belongs to a broader and better documented history of unstressed front-vowel leveling and medial-vowel variation.
- **examples:** `lufen`; `weorold`; `weoruld`
- **cautions:** Campbell still does not produce a discrete SC014-SC015 chapter. SC014 remains broad background rather than a strongly bounded rule, and SC015's clearest book value is as an opening prelude to later unstressed-vocalic material.

### Hogg 1992

- **source_key:** `Hogg1992`
- **locator:** pp. 101, 112, 117
- **terminology:** monophthongization of `/ai/`; absence of unstressed diphthongs; merger of unstressed front vowels to `/e/`
- **short quotation:** "`because of the monophthongisation of /ai/`"; "`diphthongs did not occur in Old English unstressed syllables`"; "`by about 700 all unstressed front vowels had become /e/`"
- **paraphrase:** Hogg gives the most compact structural explanation for why SC014 and SC015 belong together at all. He treats the monophthongization of `/ai/` as one of the developments that reshaped the early vowel system [@Hogg1992, p. 101], states plainly that diphthongs do not occur in Old English unstressed syllables [@Hogg1992, p. 112], and argues that by about 700 all unstressed front vowels had merged as `/e/` except in a few protected environments [@Hogg1992, p. 117]. That combination makes the opening pair historically coherent as a short unstressed-vocalic prelude even if only SC015 currently yields a positive chronology constraint.
- **conditioning:** weak-stress syllables; unstressed front-vowel reduction; loss of unstressed diphthong contrasts
- **chronology:** Hogg supports the row as an early opening zone of unstressed-vowel simplification, but not as a precise two-step local chronology. His value here is structural and typological rather than boundary-specific.
- **examples:** general unstressed front-vowel merger; absence of unstressed diphthongs
- **cautions:** This is background support rather than a witness-driven chronology argument. It helps justify the row as a plausible opening bridge, but it does not by itself decide whether SC014 deserves more than a very short subsection.

## CAPR formulation versus literature

CAPR turns that early unstressed-vowel background into two explicit adjacent
rules at the very start of the ordinary cascade.

SC014 `PNWGmcUnstressedAiMonophthongization` is historically plausible and
comparatively well supported as a type. Ringe and Taylor give the clearest
statement that unstressed `*ai` merged with unstressed `*e` across much of the
Northwest Germanic area, and Campbell supplies older West Germanic support for
the same general move [@RingeTaylor2014, pp. 37--41; @Campbell1959, §331.7].
Post-split, SC014 is the word-final `*-ai > *-ē` change only; it is corpus-inert
(zero corpus applications), so CAPR gives it no positive chronology on either
side. It is therefore best understood as a real early historical prelude whose
placement rests on comparative evidence rather than on any CAPR derivation.

SC015 `NWGmcILowering` is stronger. Campbell's unaccented-vowel merger and
Hogg's claim that unstressed front vowels converged on `/e/` give it a clear
historical analogue [@Campbell1959, §369; @Hogg1992, p. 117]. Its later
boundary at SC036 is also interpretable because the `world` derivation belongs
to the same documented space of unstable medial vowels seen in Campbell and
Ringe and Taylor [@Campbell1959, §§338--339; @RingeTaylor2014, §6.3.3]. The
rule is still only one-sided in chronology, but it has a more obvious prose
center than SC014.

The practical result is an opening pair whose internal hierarchy is already
clear. SC014 is a boundary-limited left flank. SC015 is the stronger right-hand
member and the only one that currently points forward into a later ordinary
chronology relation.

## Chronology implications

- SC014 has no positive historical first-break boundary in either direction because it is **corpus-inert**: no OE corpus lexeme carries word-final unstressed `*-ai`, so no witness can be crossed.
- SC014's cascade placement is therefore computationally free; its early Proto-Northwest Germanic stage rests on comparative evidence (inflectional endings `*-ai`), not CAPR derivation.
- The former "runner-limited at bundled `PWGmcChanges`" reading is superseded by the SC004 split, which removed the shared rule that caused it.
- SC015 has one current historical boundary, and it is rightward: `SC015 < SC036`, with `world`.
- SC015's earlier side is also runner-limited at bundled `PWGmcChanges` and must not be rewritten as a positive left boundary.
- The `SC015 < SC036` relation is broad/far and should remain a cross-reference only. It does not justify a non-contiguous SC015-SC036 chapter.
- The opening pair therefore has one real future-facing hinge but no local reciprocal corridor of the kind seen in the `SC016-SC020` pilot.

## Chapter-shape options

### Option 1: keep SC014-SC015 as one short cautious opening bridge

This is the least disruptive option and remains fully viable.

- **Why it works:** the rules are adjacent, both are ordinary FST changes, and together they form a real prelude to the `SC016-SC020` pilot corridor.
- **How it should be narrated:** SC014 as a short boundary-limited opening note, SC015 as the stronger subsection that carries most of the historical prose.
- **Main caution:** the report would need to say openly that SC014 is source-backed but chronology-negative in current testing.

### Option 2: keep the grouped row, but make SC014 explicitly very short and let SC015 carry the chapter

This is probably the best reading if the row is ever promoted unchanged.

- **Why it works:** it matches the evidence already in hand. SC014 has real comparative support but no usable positive chronology, while SC015 has both source support and one interpretable order relation.
- **How it should look:** a brief opening paragraph on unstressed `*ai` monophthongization, followed by a longer SC015 subsection focused on early unstressed front-vowel leveling and the `world` cross-reference.
- **Main caution:** the prose should remain a genuine two-change report rather than quietly collapsing into an SC015 singleton with SC014 omitted.

### Option 3: let SC015 function as a prelude to later unstressed-vocalic material by cross-reference only

This is the main alternative, but it is weaker as current book architecture.

- **Why it works:** SC015's only current positive chronology points forward to SC036, so the row naturally gestures toward the later interstress material.
- **Why it should stay cross-reference only:** SC036 is non-contiguous and already belongs to a different promoted region. Turning that relation into chapter architecture would break the strict chronological policy.
- **Main caution:** if SC014-SC015 is not eventually promoted in some local form, the opening ordinary pair risks remaining under-described next to the already mature `SC016-SC020` corridor.

## Cross-region links that should stay as cross-references only

1. **Bundled `PWGmcChanges`** bounds the earlier searches for both SC014 and SC015, but it is a runner limitation rather than a historical opening boundary.
2. **The pilot `SC016-SC020` corridor** is the immediate right-hand neighbor and the reason this row matters as an opening prelude, but it should not absorb SC014-SC015 by default.
3. **SC036** is the one real positive later relation for SC015 through `world`, but it is too far right to justify a non-contiguous chapter.

These links are editorially useful, but none of them licenses a claim stronger
than "opening prelude with a forward cross-reference."

## Working recommendation

The source pass does **not** point to immediate promotion, but it does make the
next human decision much clearer.

1. `SC014-SC015` can remain scaffolded for now.
2. If the row is eventually promoted unchanged, it should be a short cautious opening bridge with SC014 explicitly brief and SC015 carrying most of the prose.
3. SC014 is likely to remain a boundary-limited implementation-context note even inside a grouped report.
4. SC015 can and should cross-reference the later SC036 / `world` material, but only as cross-reference.
5. Further source work is optional rather than mandatory; the main unresolved question is chapter shape, not missing basic evidence.

## Open questions

- Should the eventual production prose be a genuinely short two-change opening bridge, or an even more asymmetric SC014-note plus SC015-led treatment?
- How explicitly should the finished book mention the bundled `PWGmcChanges` limitation without making it sound like a historical left boundary?
- How much of the `world` derivation should appear in the SC015 subsection, given that SC036 later revisits the same witness from a different angle?
- Should the handoff to the `SC016-SC020` pilot corridor be framed as "opening prelude" or as "pre-pilot unstressed-vowel setup"?
- Is there any editorial benefit in splitting the row later, or does a deliberately asymmetrical grouped note already solve the book problem?

## Dossier status

draft_complete
