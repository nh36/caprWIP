# Nasal spirant changes

## Historical discussion

The two rules state successive phases of a single development. Campbell
describes nasal loss before voiceless spirants with compensatory lengthening and
nasalization of the preceding vowel. Ringe and Taylor assign the same outcomes
to inherited northern West Germanic, before late Old English
[@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

[SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) adjusts the vowel while the nasal-plus-spirant sequence remains present; [SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss) then removes the nasal. The first rule must therefore precede the second.

## SC026. North Sea Germanic nasal-spirant lengthening (`EAFNasalSpirantLengthening`) {#rule-EAFNasalSpirantLengthening}

```foma
define EAFNasalSpirantLengthening [
    {*a} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*e} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*i} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*o} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*u} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*æ} -> {*ē} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*á} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*é} -> {*ḗ} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*í} -> {*ī} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ó} -> {*ō} || _ EnglishStarNasal EnglishStarVoicelessFricative,
    {*ú} -> {*ū} || _ EnglishStarNasal EnglishStarVoicelessFricative
];
```

All three witnesses require the vowel adjustment while the nasal is still present. If [SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) follows [SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss), PGmc [fúnxstiz]{.recon} ‘fist’ yields [*fyst*]{.pred} rather than expected OE *fȳst* ‘fist’, PGmc [gánsz]{.recon} ‘goose’ yields [*ġeas*]{.pred} rather than expected *gōs* ‘goose’, and PGmc [júgunθ]{.recon} ‘youth’ yields [*ġeogoþ*]{.pred} rather than expected *ġeoguþ* ‘youth’. Earlier placement changes no output. The evidence requires lengthening to precede nasal loss without supplying a lower boundary, in agreement with the handbook treatment of the two as successive phases.

## SC027. North Sea Germanic nasal-spirant loss (`EAFNasalSpirantLoss`) {#rule-EAFNasalSpirantLoss}

```foma
define EAFNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

The converse test fixes the same boundary: placing [SC027 EAFNasalSpirantLoss](#rule-EAFNasalSpirantLoss) before [SC026 EAFNasalSpirantLengthening](#rule-EAFNasalSpirantLengthening) produces the same errors in *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’. Later placement changes no output. These forms prove that the vowel was adjusted before the nasal disappeared; they provide no upper boundary for the loss.
