# Syllabic j after final-vowel loss

### Sound-change report

#### Historical formulation

SC011 `PWGmcSyllabicJ` isolates the development by which postconsonantal `*j` becomes syllabic `*i` after the loss of unstressed final `*a` and `*ą`. In the current inventory the trace occurrence count is `0`, which immediately marks this rule as backend-useful but observationally weak inside the present compact trace.

That does not make the rule unreal. It does mean the report should stay modest and should not pretend that the current lexical dataset exhibits a broad live witness set for the change.

#### Source tradition

Ringe and Taylor state directly that upon the loss of unstressed `*a` and `*ą`, preceding postconsonantal `*j` and `*w` became syllabic `*i` and `*u` respectively [@RingeTaylor2014, p. 46]. Their examples include PGmc `*harjaz` > PWGmc `*hari`, PGmc `*andijaz` > PWGmc `*andi`, and PGmc `*rikija` > PWGmc `*riki` [@RingeTaylor2014, p. 46].

That is good direct support for the historical phenomenon. The weakness lies not in the source tradition but in the trace layer: the current compact trace does not surface direct SC011 hits, so the report must keep the distinction between source-backed history and present trace visibility clear.

#### CAPR implementation

CAPR models the syllabic-j development as:

```foma
define PWGmcSyllabicJ [
    {*j} {*a} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.,
    {*j} {*ą} -> {*i} || EnglishStarShortVowel EnglishStarConsonant _ .#.
];
```

This is a deliberately tight formalization of the environment described by Ringe and Taylor. It keeps the focus on postconsonantal `*j` after final-vowel loss, rather than widening the rule into a generic fronting or vocalization note.

#### Place in the cascade

In the inventory ordering, SC011 follows SC010 `PWGmcJGemination` and precedes SC012 `EAFLThVoicing`. In the production cascade it remains inside bundled `EarlyEnglishLineChanges`, but the expanded-PWGmc first-break mode already exposes it directly for chronology testing.

Its most important local relation is to SC010. In CAPR, j-gemination must precede syllabic-j vocalization, because gemination creates heavy stems that no longer match the light-syllable environment for SC011. That is a modeled-cascade claim rather than a validated chronology card result at present.

#### Order evidence

Validated expanded-PWGmc first-break TSV output now exists for SC011, and the chronology card is complete. The earlier search finds an immediate real break at SC010 `PWGmcJGemination`: if SC011 is moved earlier to order `10`, PGmc `*nátją` yields `nete` instead of expected OE `nett`.

The later search then reaches order `86` with no real break before the current SC087 boundary, so the later side is boundary-only rather than a positive historical limit.

#### Interpretation

SC011 can now stand as a cautious singleton note. The handbook support is good and the validated order evidence recovers a real local seam with SC010, even though the current compact trace still gives the rule a zero direct occurrence count of its own.

#### Remaining cautions

The main caution is the mismatch between the validated boundary and the present trace layer. The historical phenomenon is real and the SC010/SC011 seam is now explicit, but the compact trace still yields no direct SC011 hits. Any later prose should keep that limitation visible and should not inflate the rule into a broader high-vowel chapter.
