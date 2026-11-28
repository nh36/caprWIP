# Unstressed ei-contraction

## SC083. Contraction of unstressed \emph{ei} (`OEUnstressedEIContraction`) {#rule-OEUnstressedEIContraction}

In the weak suffix of verbs such as *macian* ‘make’, earlier rounded
vocalism was shortened and unrounded. Unstressed \emph{*-ej-} >
\emph{-ij-}; further loss of the vowel was restricted to forms with a
following heavy syllable. Early spellings with \emph{i} or \emph{iġ}
reflect the distinction [@RingeTaylor2014, p. 228].

```foma
define OEUnstressedEIContraction FootCtx([
    {*e} -> 0 || EnglishStarVocalic [EnglishStarConsonant | EnglishPalatalConsonant]+ _ {*i}
]);
```

The preceding rule represents the weak sequence as \emph{e.i}. Removing
\emph{e} in that representation approximates the historical weak-vowel
development in *borian* ‘bore’ and *liccian* ‘lick’; the finite Vespasian
gloss *liciað* ‘lick’ independently attests the suffix
[@RingeTaylor2014, pp. 32, 35, 228; @Sweet1885, p. 286 (Ps. 71:9)].
The foot restriction keeps one annotated pretonic syllable outside the
context that licenses deletion. This prevents its vowel from licensing
loss of \emph{e} in the stressed root after earlier rules remove the
root's overt accent. In Mercian *ġeċēð* ‘calls’, the sequence arose
inside the stressed root after loss of \emph{w} and developed a long
vowel, not the weak outcome [@Campbell1959, §237.1b;
@RingeTaylor2014, pp. 260, 318]. The foot marker does not itself model
that contraction or diagnose stress after an unmarked longer prefix.

Moving this rule before [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization)
makes the reconstructed inputs [búrōjaną]{.recon} ‘bore’ and
[líkkōjaną]{.recon} ‘lick’
yield [*boreian*]{.pred} and [*licceian*]{.pred} instead of the attested
forms. This establishes that the two executable steps must be ordered in
that way for these weak forms, not that the consonant became a separate
vowel historically. No new failure was found towards
[SC087 OERMetathesis](#rule-OERMetathesis) within the tested range.
