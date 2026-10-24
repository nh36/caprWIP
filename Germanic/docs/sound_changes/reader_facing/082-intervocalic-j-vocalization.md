# Intervocalic j-vocalization

## SC082. Bounded inherited-j normalization (`OEIntervocalicJVocalization`) {#rule-OEIntervocalicJVocalization}

```foma
define OEIntervocalicJVocalization [
    {*j} -> {*i} ||
        [EnglishStarVocalic - [{*ǣ}|{*ē}|{*ḗ}]] _ EnglishStarVocalic
];
```

The former unrestricted VjV matcher wrongly gave model-only
[*cǣie*]{.pred} instead of *cǣġe* 'key'. Hogg's pre-OE
\emph{*kǣjæ} retains the glide [@Hogg1979, p. 105]. The bounded rule
therefore excludes preceding non-high long front monophthongs.

This is not a generic physical vocalization law. Hogg distinguishes
high-vowel coalescence from spellings that merely represent a consonantal
glide and from unstressed alternations
[@HoggGrammar2011, pp. 283--286, §§7.69--7.76].
The remaining weak-suffix e+j to e+i to i path telescopes later
raising/contraction, rather than asserting that its e+i intermediate is a
source reconstruction [@RingeTaylor2014, p. 228].
[SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction)
consumes that modeled sequence. The full residual proxy domain is not
claimed to be one independently established historical event.

The separately represented fricative ʝ passes through this zone without
being treated as inherited j. Its later merger belongs to
[SC109 OEPalatalFricativeMerger](#rule-OEPalatalFricativeMerger).

Moving the rule before [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) makes PGmc [stráwjaną]{.recon} ‘strew’ yield [*strīeian*]{.pred} rather than expected OE *strīeġan* ‘strew’. Delaying it until after [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction) makes PGmc [búrōjaną]{.recon} ‘bore’ yield [*boreian*]{.pred} rather than expected OE *borian* ‘bore’, PGmc [xándlōjaną]{.recon} ‘handle’ yield [*handleian*]{.pred} rather than expected *handlian* ‘handle’, and PGmc [mákōjaną]{.recon} ‘make’ yield [*maceian*]{.pred} rather than expected *macian* ‘make’. The witness forms require [SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) to follow [SC081 OEJStrengtheningAfterFrontDiphthong](#rule-OEJStrengtheningAfterFrontDiphthong) and precede [SC083 OEUnstressedEIContraction](#rule-OEUnstressedEIContraction).

[SC082 OEIntervocalicJVocalization](#rule-OEIntervocalicJVocalization) is
therefore ordered between strengthening and contraction.
