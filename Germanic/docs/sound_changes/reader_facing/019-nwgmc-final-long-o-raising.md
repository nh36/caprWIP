# Raising of final unstressed long \emph{*ō}

## Historical discussion

Ringe and Taylor describe the change of unstressed final non-nasalized long
\emph{*ō} to short \emph{*u} as a Northwest Germanic development
[@RingeTaylor2014, p. 30]. It applies in the same final-syllable environment
as the subsequent loss of word-final \emph{*z}. The derivation of *ræste*
'rest' fixes their local order: [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising)
must still see final \emph{*ō}, and word-final \emph{*z}-deletion removes the following
\emph{*z} only afterward.

The change supplies the final vowel of forms such as *nosu* 'nose', *sċofl*
'shovel', and *sorg* 'sorrow'.

## SC019. Raising of final unstressed long \emph{*ō} (`NWGmcFinalLongORaising`) {#rule-NWGmcFinalLongORaising}

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Two groups of witnesses confine final unstressed long \emph{*ō} > \emph{*u}. The forms *nosu* 'nose', *sċofl* 'shovel', and *sorg* 'sorrow' fix its lower boundary.

Before [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc [núsō]{.recon} 'nose' yields [*nusu*]{.pred} rather than expected OE *nosu* 'nose', PGmc [skúflō]{.recon} 'shovel' yields [*sċufl*]{.pred} rather than expected *sċofl* 'shovel', and PGmc [súrgō]{.recon} 'sorrow' yields [*surg*]{.pred} rather than expected *sorg* 'sorrow'. After word-final \emph{*z}-deletion ([SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion)), PGmc [rástōz]{.recon} 'rest' yields [*rast*]{.pred} rather than expected *ræste* 'rest'. These failures place [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) after u-lowering and before final \emph{z}-loss.
