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

No validated chronology card exists yet for SC006. The older batch-04 manifest lists it as skipped only because the bundled `PWGmcChanges` stage had not yet been made reorderable in first-break mode.

The current runner can now test SC006 directly with `--order-profile expanded-pwgmc`, and the dry-run order inspection in this pass confirmed that SC006 resolves as the third rule in that expanded profile. No real first-break TSV output was produced here, so its earlier/later boundaries remain unvalidated and should not yet be narrated as historical constraints.

#### Interpretation

SC006 is a good backend singleton candidate. The historical phenomenon is well enough supported to justify a production-style report and dossiers, and the trace occurrence count is substantial enough to make later chronology work worthwhile. What it still lacks is the validated first-break TSV layer.

#### Remaining cautions

The major caution is not the existence of the rule but its current documentation boundary. Real first-break TSV output is still missing, and the retrieved source discussion is strongest for suffixal evidence and `geoguþ` rather than for every inventory witness. Until the chronology layer is computed from the expanded-PWGmc runner, SC006 should remain out of `report_manifest.tsv`.
