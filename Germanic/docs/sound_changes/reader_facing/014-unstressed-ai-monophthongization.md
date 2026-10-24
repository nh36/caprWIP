# Unstressed ai monophthongization

## Historical discussion of unstressed \emph{*ai} monophthongization

Ringe and Taylor describe the widespread monophthongization of unstressed
\emph{*ai} to a long mid vowel, largely merging with inherited unstressed
\emph{*ē}. Their examples include final dative-singular and nonfinal
inflectional syllables. They nevertheless question a single completed
Proto-Northwest Germanic merger: Runic evidence suggests that some
unstressed diphthongs survived later than others
[@RingeTaylor2014, pp. 25--26]. The stressed development of \emph{*ái}
to \emph{*ā} is treated separately as
[SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization).

## SC014. Monophthongization of unstressed \emph{*ai} (`PNWGmcUnstressedAiMonophthongization`) {#rule-PNWGmcUnstressedAiMonophthongization}

```foma
define PNWGmcUnstressedAiMonophthongization Ctx([
    {*ai} -> {*ē}
]);
```

The dative-singular endings span [spánnai]{.recon} 'span' and meed [mízdai]{.recon} 'meed' carry this change; both give a final \emph{*ē}. If [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) is delayed until after [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening), the \emph{*ē} is no longer present for shortening, so PGmc [spánnai]{.recon} 'span' yields [*spannē*]{.pred} rather than expected OE *spanne* 'span'. This shows that [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization) must come before [SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening) in the modeled sequence.
