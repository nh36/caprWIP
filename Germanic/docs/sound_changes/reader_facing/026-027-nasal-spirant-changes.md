# Nasal spirant changes

## Historical discussion of nasal loss before spirants and compensatory lengthening

The two rules state successive phases of a single development. Campbell
describes nasal loss before voiceless spirants with compensatory lengthening and
nasalization of the preceding vowel. Ringe and Taylor assign the same outcomes
to inherited northern West Germanic, before late Old English
[@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

[SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) adjusts the vowel while the nasal-plus-spirant sequence remains present; [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) then removes the nasal. The first rule must therefore precede the second.

## SC026. Lengthening before nasal plus spirant (`NWGmcNasalSpirantLengthening`) {#rule-NWGmcNasalSpirantLengthening}

```foma
define NWGmcNasalSpirantLengthening [
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

All three witnesses require the vowel adjustment while the nasal is still present. If [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) follows [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss), PGmc \emph{*fúnxstiz} yields *fyst* rather than expected OE *fȳst* ‘fist’, PGmc \emph{*gánsz} yields *ġeas* rather than expected *gōs* ‘goose’, and PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. Earlier placement changes no checked output. The evidence requires lengthening to precede nasal loss without supplying a lower boundary, in agreement with the handbook treatment of the two as successive phases.

## SC027. Loss of the nasal before spirants (`NWGmcNasalSpirantLoss`) {#rule-NWGmcNasalSpirantLoss}

```foma
define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

The converse test fixes the same boundary: placing [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) before [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) produces the same errors in *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’. Later placement changes no checked output. These forms prove that the vowel was adjusted before the nasal disappeared; they provide no upper boundary for the loss.
