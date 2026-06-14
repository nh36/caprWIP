# Early i-apocope

### Sound-change report

#### Historical formulation

SC006 `PWGmcEarlyIApocope` isolates the early loss of final `*i` after unstressed syllables in forms far enough from the main stress that later i-umlaut no longer sees the trigger. In the trace output it appears in forms such as `thousand`, `bore (3sg)`, `have`, `learn (3sg)`, and `lick (3sg)`.

That is historically recognizable and more strongly sourced than SC005. The main historical value of the rule is not the individual lexemes alone, but the broader argument that early final `*i` loss must precede later umlaut and related vocalic developments.

#### Source tradition

Sievers/Brunner treats the early Common-Germanic loss of final `-i` after unstressed syllables as established by the fact that these endings no longer triggered i-umlaut in Old English [@SieversBrunner1965, §§145--146]. Ringe and Taylor give the classic `youth` example directly: PWGmc `*jugunþi > *juguþ > OE geoguþ ~ iuguþ` [@RingeTaylor2014, p. 141]. Campbell likewise cites `dugup` and `geogup` among the relevant outcomes of early final high-vowel loss [@Campbell1959, §332].

That is good support for the historical phenomenon itself. The present source pass is less complete for the full spread of CAPR's inventory examples, since the retrieved prose is strongest on endings and on the `youth` family rather than on every trace witness such as `have` or `lick (3sg)`. The source layer is therefore solid but not yet exhaustive.

#### CAPR implementation

CAPR models the early apocope as a targeted deletion of final `*i` in sufficiently remote unstressed syllables:

```foma
define PWGmcEarlyIApocope [
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ .#.,
    {*i} -> 0 || PGmcStarStressedVowel PGmcStarConsonant+ PGmcStarVocalic PGmcStarConsonant+ _ {*z} .#.
];
```

The implementation makes explicit what the historical discussion implies: the decisive issue is relative stress and syllable count, not just absolute word-final position. This is why the rule is modeled separately from later syncope and apocope.

#### Place in the cascade

In the inventory ordering, SC006 follows SC005 `NWGmcAToUBeforeM` and precedes SC007 `PWGmcFinalOrLowering`. Like SC004 and SC005, it is still live inside bundled `PWGmcChanges`, but the current runner can now expose it directly through the `expanded-pwgmc` first-break profile.

That means the main backend blocker is no longer runner visibility. It is simply the absence of actual first-break TSV output for this specific change.

#### Order evidence

Validated order evidence now exists through the expanded-PWGmc first-break output family:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv`

The earlier search moved SC006 safely across SC005 and SC004 down to order `4` and then reached the left edge of the tested expanded-PWGmc chain with no real break. That side is therefore boundary-only rather than a positive chronology constraint.

The later search does find a real historical break at order `34` across `SC034` OE Aw Long Diphthong. If PWGmc Early I Apocope is delayed that far, PGmc `*skáwōθi` yields `sċēaweþ` rather than expected OE `sċēawaþ`.

That later boundary is historically interpretable, but it is broad/far rather than a tight local adjacency claim.

#### Interpretation

SC006 works well as a short singleton note. The historical phenomenon is well supported, and the chronology layer now supplies a usable one-sided later boundary. The report's center of gravity should remain the anti-umlaut and suffixal evidence rather than an attempt to distribute equal weight across every current trace witness.

#### Remaining cautions

The major caution is not the existence of the rule but its scale. The retrieved source discussion is strongest for suffixal evidence and `geoguþ` rather than for every inventory witness, and the later `SC034` relation is broad/far rather than local. Those limits should remain visible even in a cautious singleton note.
