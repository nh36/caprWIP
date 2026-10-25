# Pretonic i-lowering

## Historical discussion

Late weak-tail reduction affects unstressed prefixes as well as inflectional
endings and medial vowels. Fulk's discussion of prefix vowels accounts for OE
\emph{*be-} and \emph{*ne-} [@Fulk2018, p. 97, §5.7]. Hogg explicitly includes *be-* and *ge-* in the lowering of unstressed
\emph{*i}, marginally later than the earlier front-vowel merger. Ringe and
Taylor supply early *gistīga* 'climb into/onto' beside later *gestīga*
'climb into/onto', and place *bi-* and *ni* alongside this development
[@HoggGrammar1992, §§6.50--6.54 (held 2011 reprint, pp. 237--239);
@RingeTaylor2014, pp. 334--335].

The manuscript evidence, rather than the older proxy's displacement
results, supports this limited relative chronology.

## SC076. Pretonic i-lowering (`OEPrefixIReduction`) {#rule-OEPrefixIReduction}

```foma
define OEPrefixIReduction SentenceCtx([
    [{*i} -> {*e} || .#. {*ᶠ} OEAnyConsonant* _]
    .o. [{*ᶠ} -> 0]
]);
```

The rule lowers short \emph{*i} in a positively identified weak pretonic
syllable, not specifically in morphemes beginning with a particular
consonant. Thus the same conditioning treats inherited weak \emph{*bi-}
and the raised vowel in \emph{*gi-}; stressed roots remain outside its
domain. The superscript `*ᶠ` is a nonsegmental prosodic annotation,
removed once it is no longer needed. The rule therefore produces
\emph{*e} directly, not a protected intermediate breve-e.

This bounded implementation requires a following headed syllable.
The separately unstressed negative particle *ni* 'not' > *ne* 'not'
supports the wider history of weak-vowel lowering, but is not made into
a newly encoded selected input or a claim that the present pretonic
condition covers every weak particle
[@RingeTaylor2014, p. 335].

The earlier displacement experiment found no final-output boundary for
the old consonant-identity proxy. That negative result is not a test of
the reformulated prosodic rule and does not date it. The relative placement
after the earlier merger follows the handbook account; its precise
interval remains approximate.
