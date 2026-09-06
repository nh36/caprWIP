# Hiatus-filling \emph{w} in the verba pura

## Historical discussion

The small class of Germanic strong verbs whose roots ended in a vowel — the *verba pura* — reached Northwest Germanic with a morphologically expected hiatus. Ringe and Taylor reconstruct Proto-Germanic \emph{*sēaną} 'to sow' (Gothic *saian*), which the Northwest Germanic lowering of \emph{*ē₁} carried to \emph{*sāaną}; the West Germanic languages then "exhibit innovative consonants that eliminated" the hiatus [@RingeTaylor2014, p. 12]. The repair differs by branch, and the difference dates and localizes the change: Old English and Old Frisian inserted \emph{w} — Old English *sāwan* 'to sow', Old Frisian *sāwinge* beside *grōwinge* 'growth' — while Old Saxon and Old High German used \emph{j} instead (*sāian*, *sāen*, *sājen*) [@RingeTaylor2014, pp. 12, 151]. The insertion of \emph{w} is therefore an Anglo-Frisian development, not a common West Germanic one, and the consonant of *sāwan* is not inherited: it must not be projected back into the protoform.

Ringe and Taylor locate the origin of the glide precisely: it arose first between the stem vowel and the \emph{*u}-initial endings — present indicative first singular \emph{*-u}, past indicative plural \emph{*-un} — and was generalized from there through the rest of the paradigm [@RingeTaylor2014, p. 151]. The rule below models the outcome of that generalization on citation forms; the layering of regular insertion and analogical spread belongs to the historical record rather than to the executable statement.

The chronology is fixed on both sides by Ringe and Taylor. The insertion must postdate the West Germanic loss of intervocalic \emph{*w}, or the new glide would itself have been swept away [@RingeTaylor2014, p. 151, n. 9]; and it "must have occurred early enough to prevent fronting of \emph{*ā}" in pre-Old English [@RingeTaylor2014, p. 151] — the whole reason *sāwan*, *cnāwan* 'to know', *blāwan* 'to blow', and *māwan* 'to mow' keep their back vowel is that the \emph{w} was already in place when the North Sea Germanic fronting applied. The insertion accordingly stands before the fronting in the cascade, even though, on the present corpus, the two orders happen to produce the same outputs: the fronting rule as implemented does not touch a prevocalic \emph{ā} in any case, so the ordering encodes the historical chronology rather than a corpus-internal contrast.

## SC102. Hiatus-filling \emph{w} after long \emph{ā} (`EAFHiatusWInsertion`) {#rule-EAFHiatusWInsertion}

```foma
define EAFHiatusWInsertion [
    [..] -> {*w} || {*ā} _ EnglishStarVocalic
];
```

The rule is fed by [SC024 PNWGmcLongELowering](#rule-PNWGmcLongELowering), which creates the \emph{ā}-initial hiatus it repairs: [sḗaną]{.recon} 'to sow' passes through \emph{*sāaną} to \emph{*sāwaną} on its way to *sāwan*. Displaced before the lowering, the rule can never apply — the root vowel is still \emph{*ē} and no hiatus after \emph{ā} exists — and the derivation loses its consonant altogether.

Its output in turn feeds the blocking environment of [SC101 EAFLongAFronting](#rule-EAFLongAFronting): the inserted \emph{w} is precisely what shields the \emph{ā} of *sāwan* from fronting, as treated in that chapter. The corpus carries *sāwan* as the diagnostic witness of the class; *cnāwan*, *blāwan*, *māwan*, *wāwan*, and *þrāwan* instantiate the same derivation [@RingeTaylor2014, p. 151].
