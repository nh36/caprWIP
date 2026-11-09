# Stem-final n-loss after long i

## Historical discussion

The inherited
feminine \emph{in}-stem represented by Gothic \emph{faurhtei}, OE \emph{fyrhtu},
and oblique OE \emph{fyrhte} supplies the relevant evidence
[@Orel2003, p. 120; @RingeTaylor2014, pp. 380--381; @Campbell1959, p. 236, §589.7].
Final \emph{*n} after unstressed \emph{*ī} was lost after
Proto-West-Germanic differentiation; conservative southern Old High German
prevents treating it as an undifferentiated Northwest Germanic law
[@RingeTaylor2014, pp. 87--88; @Fulk2018, p. 173, §7.34].
This early loss must be distinguished from the later weak-syllable
developments described by Hogg, Ringe and Taylor, and Fulk
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--303, §§6.7.3--6.8.4;
@Fulk2018, p. 91, §5.6].

## SC064. Loss of stem-final \emph{*n} after long \emph{*ī} (`NWGmcInStemNLoss`) {#rule-NWGmcInStemNLoss}

```foma
define NWGmcInStemNLoss Ctx([{*n} -> 0 || {*ī} _ .#.]);
```

Only word-final \emph{*n} after unstressed long \emph{*ī} is at issue.
The conditioning is phonological, not membership in the feminine
\emph{īn}-stems. Besides their obliques, Campbell cites *strenge*
'strength', the loanword *pyle* 'pillow' and early past-subjunctive plural
endings [@Campbell1959, p. 189, §473; @SieversBrunner1965, pp. 225--226, §280].

CAPR models the oblique OE form through the Proto-Germanic genitive singular
\emph{*fúrxtīnaz} 'fright', following the project convention of using an appropriate
non-nominative paradigm cell when the nominative does not supply the required
derivation. Final ending loss exposes \emph{*fúrxtīn}; early loss of
\emph{*n}, mutation and later shortening yield *fyrhte* 'fright'.
This selected encoding imposes two implementation boundaries. Before
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), PGmc
\emph{*fúrxtīnaz} ‘fright’ yields [*fyrhten*]{.pred} rather than expected OE *fyrhte* ‘fright’.
After [SC072
OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), PGmc
\emph{*fúrxtīnaz} again yields [*fyrhten*]{.pred} rather than expected *fyrhte* 'fright'.
The former boundary exposes the segment; the latter keeps its long-vowel
environment visible. Neither dates the loss to a late post-apocope period.

Campbell attributes retained *n* in *nēten* 'livestock' to the inflected
forms [@Campbell1959, p. 189, §473]. Goering's later \emph{*nētīn}
therefore does not require immunity to the early law: a later paradigmatic
state and uninterrupted inherited retention are different claims.
An exposed early final \emph{*-īn} would regularly lose its consonant;
the later \emph{*nētīn} cannot be presented as an exemption or as
uninterrupted phonological survival. Its complete ancestral derivative
and intervening paradigmatic history are separate questions.
Final \emph{*ī} remains long until later shortening, while medial
\emph{*ī} has already shortened in the inflected forms
[@Goering2016, pp. 186--188; @Goering2023, pp. 67--68].
No word-specific protection or added accent is required. The exact date
of paradigmatic retention or restoration is not fixed by these comparisons.

The selected plural avoids that singular problem. Fulk prints
\emph{*nautīnō}, the ancestor of the Mercian plural, while the
Hatton *Pastoral Care* attests West Saxon *nietenu* 'animals, livestock'
[@Fulk2018, p. 92, §5.6; @Sweet1871, p. 109, lines 8--11;
@RingeTaylor2014, pp. 298--299]. Its medial nasal is followed by the
plural vowel throughout this early loss and therefore survives
regularly. The full plural reaches *nīetenu* 'animals' without either an
exception to this law or a transponent with restored final *n*.
