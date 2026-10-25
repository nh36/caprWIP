# Heavy-syllable nasal apocope

## Historical discussion of heavy-syllable nasal loss and secondary nasalization

Heavy-syllable nasal apocope removes the final nasalized vowel; secondary
nasalization then marks the preceding \emph{a} before final \emph{n}. The
handbooks do not isolate both developments under equally prominent labels.
Campbell describes later nasal loss and the back-mutation environment; Ringe
and Taylor provide the later relation to back mutation
[@Campbell1959, pp. 86, 166, §§205--206, 403;
@RingeTaylor2014, p. 319, §6.9.4].

The reciprocal failure set fixes the order: apocope removes the ending before
secondary nasalization acts on the remaining structure. Restoration receives
the fuller historical treatment in the handbooks.

## SC047. Heavy-syllable nasal apocope of final \emph{*ą} (`OEHeavySyllableNasalApocope`) {#rule-OEHeavySyllableNasalApocope}

```foma
define OEHeavySyllableNasalApocope Ctx([
    {*ą} -> 0 || OEAnyConsonant _ .#.
]);
```

The old lower-bound test depended on the superseded straw proxy:
moving apocope before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong)
made PGmc [stráwą]{.recon} ‘straw’ yield [*stræw*]{.pred} rather than
attested OE *strēaw* 'straw'. The adopted regular endingless branch now reaches
reconstructed \emph{*strēa} through
[SC111 PWGmcEndinglessAw](#rule-PWGmcEndinglessAw), before this
apocope. The attested target retains analogically restored \emph{w}
and explicitly mismatches the regular output. The old failure therefore
does not independently place nasal apocope after a universal singleton
long-diphthong law
[@Campbell1959, pp. 46--47, 232--233;
@RingeTaylor2014, pp. 172--173, 387].

The separate recorded upper-bound test is unchanged: after
[SC048 OESecondaryNasalization](#rule-OESecondaryNasalization), PGmc
[bákaną]{.recon} ‘bake’ yields [*bacen*]{.pred} rather than expected OE
*bacan*, and PGmc [bíndaną]{.recon} ‘bind’ yields [*binden*]{.pred}
rather than expected *bindan*, alongside a broad \emph{-en} failure set.
That secondary-nasalization dependency is not newly adjudicated here.
