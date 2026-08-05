# Anglo-Frisian ai-monophthongization

## Historical discussion

Inherited \emph{*ai} monophthongized to \emph{*ā} across the North Sea Germanic area, in stressed root syllables and in unaccented nonfinal syllables alike. Ringe and Taylor place the monophthongization of \emph{*ai} among the widespread early vowel developments of the English line [@RingeTaylor2014, pp. 40--41]. Versloot shows that the stressed development spread in successive waves through a dialect continuum, with Old English among the widest to carry it [@Versloot2017, pp. 281--324]. The Old English \emph{*ā} is later fronted to \emph{ǣ} in the relevant environments.

The change is areal in character. It is shared with Frisian, and its spread through the continuum gives it a range of dates and no single sharp moment.

Two of the affected forms, \emph{*laimōn} 'loam' and \emph{*wainōjaną} 'whine', carry no accent in the reconstructed data, so their \emph{*ai} passes through the unaccented environment; the remaining witnesses show stressed \emph{*ái}.

## SC004. Anglo-Frisian ai-monophthongization (`EAFAiMonophthongization`) {#rule-EAFAiMonophthongization}

```foma
define EAFAiMonophthongization [
    [{*ai} -> {*ā} || _ ?]
    .o.
    [{*ái} -> {*ā}]
];
```

The soul form fixes the relation to interstress raising. If the monophthongization is delayed until after that change, PGmc [sáiwalō]{.recon} 'soul' yields [*sāwel*]{.pred} rather than expected OE *sāwol* 'soul'. An earlier placement changes no output. This shows that [SC004 EAFAiMonophthongization](#rule-EAFAiMonophthongization) must come before [SC036 OEInterStressRaising](#rule-OEInterStressRaising) in the modeled sequence.

The word-final unstressed development \emph{*-ai > *-ē} is a separate and earlier change; see [SC014 PNWGmcUnstressedAiMonophthongization](#rule-PNWGmcUnstressedAiMonophthongization).
