# Anglo-Frisian ai-monophthongization

## Historical discussion

Inherited stressed \emph{*ái} monophthongized to \emph{*ā} across the North Sea Germanic area. Ringe and Taylor place the monophthongization of \emph{*ai} among the widespread early vowel developments of the English line [@RingeTaylor2014, pp. 40--41]. Versloot shows that the stressed development spread in successive waves through a dialect continuum, with Old English among the widest to carry it [@Versloot2017, pp. 281--324]. The Old English \emph{*ā} is later fronted to \emph{ǣ} in the relevant environments.

The change is areal in character. It is shared with Frisian, and its spread through the continuum gives it a range of dates and no single sharp moment.

All twenty-four corpus witnesses carry stressed \emph{*ái}; loam \emph{*láimą} 'loam' is one of them, stressed in its Old English protoform. The unstressed development \emph{*ai > *ē} is the separate earlier change [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).

## SC004. Anglo-Frisian ai-monophthongization (`EAFAiMonophthongization`) {#rule-EAFAiMonophthongization}

```foma
define EAFAiMonophthongization [
    {*ái} -> {*ā}
];
```

The soul form fixes the relation to interstress raising. If the monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} 'soul' yields [*sāwel*]{.pred} rather than expected OE *sāwol* 'soul'. An earlier placement changes no output. This shows that [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The unstressed development \emph{*ai > *ē} in final and nonfinal syllables is a separate and earlier change; see [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).
