# Quantitative high-vowel deletion

## Historical discussion

Final and medial short high vowels undergo one quantitative deletion.
Campbell, Hogg, Ringe and Taylor, and Fulk agree that the relevant loss
follows mutation, but disagree over trisyllables and surrounding syncope
[@Campbell1959, pp. 144--146, §§345--353; @HoggPhonology1992, p. 121;
@RingeTaylor2014, pp. 264--293, §§6.7.3, 6.8.1; @Fulk2018, p. 91, §5.6].
Barrack separately presents final deletion as rule 345 and medial
syncope as rule 351, with progressive simplification of the former
environment [@Barrack1975, pp. 23--25, 85--87].
Those descriptions remain comparative evidence, not proof of one
particular prehistoric serialization.

The adopted account follows Fulk's conservative Mercian evidence and
Goering's quantitative analysis. A heavy first syllable followed by two
light syllables preserves both high vowels: *hēafudu* 'heads', *lȳtelu*
'little' and *īdelu* 'idle'. A heavy following syllable instead licenses
medial loss, as in *nētna* 'of livestock'. The distinction is independently
motivated by quantity and metrical grouping, not inferred from the
selected corpus's match count [@Fulk2010, pp. 129--134, 140--142;
@Goering2016, pp. 186--188; @Goering2023, pp. 67--68].
Early medial shortening, realized in
[SC117 OEMedLongShort](#rule-OEMedLongShort), gives short medial
\emph{*i} in the inflected livestock forms while final \emph{*ī}
remains long in \emph{*nētīn}. Later shortening yields *nēten*
'livestock'; the earlier final-n law does not restart here.

The alternatives remain substantive. Conventional apocope followed by
syncope gives \emph{*hēafdu}, whereas Ringe and Taylor's
syncope-before-apocope account gives \emph{*hēafd}, with restored
attested plurals attributed to analogy. Hogg also discusses a tentative
one-syllable-reduction account [@HoggGrammar2011, pp. 225--227, §§6.22--6.25;
@RingeTaylor2014, pp. 289--293]. Output equivalence on selected words
does not erase these contrasting histories.

This loss is distinct from West Germanic weak-word deletion in
[SC098 PWGmcUnstressedWordFinalIApocope](#rule-PWGmcUnstressedWordFinalIApocope).
The separately selected sentence context remains effective; its boundary
annotation is not a segment of the reconstruction
[@RingeTaylor2014, pp. 57--58].
Later light-syllable pre-l loss in
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope), weak-vowel unrounding,
and technical stress decoding remain separate operations.

## SC063. Quantitative deletion of short unstressed high vowels (`OEHighVowelApocope`) {#rule-OEHighVowelApocope}

```foma
define OEHighVowelApocope FootCtx([
    [{*i}|{*u}|{*y}|{*ų}] -> 0 ||
        .#. OEAnyConsonant* HvI HvP* _
        [.#. | OEAnyConsonant [HvL | HvS OEAnyConsonant [.#.|OEAnyConsonant]]]
] .o. [{*ᶜ} -> 0]);
```

The auxiliary expressions distinguish short and long nuclei, heavy
syllables, the initial quantitative group and following permitted groups.
Deletion targets a short unstressed high vowel at a group boundary;
a medial target requires a following singleton onset and heavy syllable.
The first root and separately transmitted prominence remain protected.
The singleton-onset representation bounds this implementation; it is
not a general parser for arbitrary historical syllabification.

Mutation must precede loss: *cȳ* 'cow' and *brȳd* 'bride' require the
high vowel to perform its umlautal work. The selected *fȳlþe* 'filth'
and *spinle* 'spindle' retain their independently supported accusative
cells; their nonhigh final vowels produce the regular medial deletion.
The comparative nominatives \emph{*fȳleþu} and \emph{*spinnelu}
retain their light medial syllables in this account. Their attested
alternatives and the genuine comparative gemination problem remain
separate from the selected accusatives
[@Fulk2010, pp. 140--142; @Goering2016, pp. 186--188;
@RingeTaylor2014, pp. 289--293].

No special final-u loss after \emph{*h} is retained. *Feoh* 'cattle, wealth'
continues an independently supported, already-endingless a-stem
transponent \emph{*feh}, not an inherited u-stem forced through an
additional deletion [@RingeTaylor2014, p. 177, n. 4].
