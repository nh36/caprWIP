# Final long-\emph{o} raising and final \emph{z}-deletion

## Historical discussion of final long-\emph{o} raising and final \emph{z}-deletion

These two rules belong together because the same final-syllable structure passes through both. Ringe and Taylor describe the change of unstressed final non-nasalized long \emph{*ō} to short \emph{*u}, while Hogg and Crist treat word-final \emph{*z} loss as a separate later step in West Germanic [@RingeTaylor2014, p. 30; @Hogg1992, p. 37; @Crist2002, p. 1].

That shared final-syllable history becomes especially visible in *ræste* ‘rest’: [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must still see final \emph{*ō}, and [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must remove final \emph{*z} only afterward.

## Historical discussion of final long-\emph{o} raising

The first change in the pair is the Northwest Germanic raising of unstressed final long \emph{*ō} to \emph{*u}. Ringe and Taylor state that development directly in comparative terms [@RingeTaylor2014, p. 30].

This is the stage that carries forms such as *nosu*, *sċofl*, and *sorg* into the later Old English sequence.

## SC019. Raising of final unstressed long \emph{*ō} (`NWGmcFinalLongORaising`) {#rule-NWGmcFinalLongORaising}

The implementation states the final-vowel raising directly.

```foma
define NWGmcFinalLongORaising [
    {*ō} -> {*u}
        || EnglishStarVocalic
           [EnglishStarConsonant | EnglishPalatalConsonant]+ _ .#.
];
```

In prose, the rule raises final unstressed long \emph{*ō} to \emph{*u}. This is the step behind forms such as *nosu* ‘nose’, *sċofl* ‘shovel’, and *sorg* ‘sorrow’.

Its chronology is explicit on both sides. If the rule is moved before [SC017 NWGmcULowering](#rule-NWGmcULowering), PGmc \emph{*núsō} yields *nusu* rather than expected OE *nosu* ‘nose’, PGmc \emph{*skúflō} yields *sċufl* rather than expected *sċofl* ‘shovel’, and PGmc \emph{*súrgō} yields *surg* rather than expected *sorg* ‘sorrow’. If it is delayed until after [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), PGmc \emph{*rástōz} yields *rast* rather than expected *ræste* ‘rest’. This shows that [SC017 NWGmcULowering](#rule-NWGmcULowering) must come before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), and that [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must come before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion).

## Historical discussion of final \emph{z}-deletion

The second change removes word-final \emph{*z}. Standard handbook tradition and Crist's West Germanic discussion both make that development clear, even though CAPR packages it more tightly than the morphology-heavy historical descriptions usually do [@Hogg1992, p. 37; @Crist2002, p. 1].

This is the step that closes the small final-syllable sequence and also opens the way to later final-vowel consequences farther to the right.

## SC020. Deletion of word-final \emph{*z} (`PGmcFinalZDeletion`) {#rule-PGmcFinalZDeletion}

The implementation keeps the deletion step short.

```foma
define PGmcFinalZDeletion [{*z} -> 0 || _ .#.];
```

In prose, the rule deletes word-final \emph{*z}. In the current sequence, this is the step that turns the protected final structure of *ræste* into its attested Old English shape after the raising rule has already applied.

Its chronology is explicit on both sides. If the rule is moved before [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising), PGmc \emph{*rástōz} yields *rast* rather than expected OE *ræste* ‘rest’. If it is delayed until after [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering), PGmc \emph{*bébruz} yields *befro* rather than expected *befer* ‘beaver’, PGmc \emph{*kwéðuz} yields *cwedo* rather than expected *cwedu* ‘cud’, and PGmc \emph{*félθuz} yields *feldo* rather than expected *feld* ‘field’, alongside eight other newly failing rows. This shows that [SC019 NWGmcFinalLongORaising](#rule-NWGmcFinalLongORaising) must come before [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion), and that [SC020 PGmcFinalZDeletion](#rule-PGmcFinalZDeletion) must come before [SC040 OEMedUnstressedULowering](#rule-OEMedUnstressedULowering).

The later boundary is historically real but broad and distant. It should be read as a forward link into the wider final-syllable sequence, not as a second tight pair beside *ræste*.
