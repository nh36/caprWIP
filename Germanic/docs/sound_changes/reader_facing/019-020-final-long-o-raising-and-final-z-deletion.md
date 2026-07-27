# Final long-\emph{o} raising and final \emph{z}-deletion

## Historical discussion of final long-\emph{o} raising and final \emph{z}-deletion

The same final-syllable structure undergoes both changes. Ringe and Taylor describe the change of unstressed final non-nasalized long \emph{*ō} to short \emph{*u}, while Hogg and Crist treat word-final \emph{*z} loss as a separate later step in West Germanic [@RingeTaylor2014, p. 30; @Hogg1992, p. 37; @Crist2002, p. 1].

The derivation of *ræste* ‘rest’ fixes their order: [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must still see final \emph{*ō}, and [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) removes final \emph{*z} only afterward.

## Historical discussion of final long-\emph{o} raising

The first change in the pair is the Northwest Germanic raising of unstressed final long \emph{*ō} to \emph{*u}. Ringe and Taylor state that development directly in comparative terms [@RingeTaylor2014, p. 30].

The change supplies the final vowel of forms such as *nosu*, *sċofl*, and
*sorg*.

## SC019. Raising of final unstressed long \emph{*ō} (`NWGmcFinalLongORaising`) {#rule-NWGmcFinalLongORaising}

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

Two groups of witnesses confine final unstressed long \emph{*ō} > \emph{*u}. The forms *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’ fix its lower boundary.

Before [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*núsō} yields *nusu* rather than expected OE *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. After [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*rástōz} yields *rast* rather than expected *ræste* ‘rest’. These failures place [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) after u-lowering and before final \emph{z}-loss.

## Historical discussion of final \emph{z}-deletion

The second change is the loss of word-final \emph{*z}. Standard handbook tradition and Crist's West Germanic discussion establish the development within broader accounts of inflectional morphology [@Hogg1992, p. 37; @Crist2002, p. 1].

Final z-loss follows long-o raising and precedes the later changes in weak
syllables.

## SC020. Deletion of word-final \emph{*z} (`PGmcFinalZDeletion`) {#rule-PGmcFinalZDeletion}

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
```

The chronology of word-final \emph{*z}-loss is unusually well delimited: *ræste* supplies its early boundary, while later weak syllables supply its late boundary.

Before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*rástōz} yields *rast* rather than expected OE *ræste* ‘rest’. After [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*bébruz} yields *befro* rather than expected *befer* ‘beaver’, PGmc \emph{*kwéðuz} yields *cwedo* rather than expected *cwedu* ‘cud’, and PGmc \emph{*félθuz} yields *feldo* rather than expected *feld* ‘field’, alongside eight other newly failing rows. Final \emph{z}-loss therefore follows [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) and precedes [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The \emph{*rástōz} derivation fixes the local relation to [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising). The distant boundary at [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering) shows only that word-final \emph{*z}-loss precedes the later weak-syllable sequence; its placement within that wider interval follows the handbook chronology after final \emph{*ō}-raising.
