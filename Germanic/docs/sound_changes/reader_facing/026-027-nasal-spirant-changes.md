# Nasal spirant changes

## Historical discussion of nasal loss before spirants and compensatory lengthening

These two rules belong together because they are CAPR's formal articulation of one older development. Campbell describes the process as nasal loss before voiceless spirants with compensatory lengthening and nasalization of the preceding vowel, and Ringe and Taylor treat the same outcomes within inherited northern West Germanic development, not as an isolated late Old English innovation [@Campbell1959, p. 47, §121; @RingeTaylor2014, pp. 140--141].

That shared history also explains the local interaction. [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) adjusts the vowel while the nasal plus spirant sequence is still present, and [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) then removes the nasal. The pair is therefore more than a mere adjacency in the cascade: the first rule prepares the environment that the second rule closes.

## SC026. Lengthening before nasal plus spirant (`NWGmcNasalSpirantLengthening`) {#rule-NWGmcNasalSpirantLengthening}

The implementation keeps the vowel change explicit across the relevant nasal-spirant environments.

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

In prose, the rule lengthens and reshapes the vowel before nasal plus voiceless spirant sequences. This is the stage that helps produce OE *fȳst* ‘fist’, *gōs* ‘goose’, and *ġeoguþ* ‘youth’.

Its ordinary historical chronology is one-sided. If the rule is delayed until after [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss), PGmc \emph{*fúnxstiz} yields *fyst* rather than expected OE *fȳst* ‘fist’, PGmc \emph{*gánsz} yields *ġeas* rather than expected *gōs* ‘goose’, and PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. This shows that [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) must come before [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss). If the rule is moved earlier within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only that later relation. They do not identify a corresponding earlier constraint, and CAPR keeps the rule here because the sources treat vowel lengthening and nasal loss as two parts of the same inherited nasal-spirant development.

## SC027. Loss of the nasal before spirants (`NWGmcNasalSpirantLoss`) {#rule-NWGmcNasalSpirantLoss}

The implementation then removes the nasal from the same environment.

```foma
define NWGmcNasalSpirantLoss [
    EnglishStarNasal -> 0 || _ EnglishStarVoicelessFricative
];
```

In prose, the rule deletes the nasal before a voiceless spirant after the vowel has already been adjusted. This is the stage that completes the same inherited development behind *fȳst*, *gōs*, and *ġeoguþ*.

Its ordinary historical chronology is one-sided in the opposite direction. If the rule is moved before [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening), PGmc \emph{*fúnxstiz} yields *fyst* rather than expected OE *fȳst* ‘fist’, PGmc \emph{*gánsz} yields *ġeas* rather than expected *gōs* ‘goose’, and PGmc \emph{*júgunθ} yields *ġeogoþ* rather than expected *ġeoguþ* ‘youth’. This shows that [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening) must come before [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss). If the rule is moved later within the tested sequence, no checked form yields a form different from the expected one.

The checked forms therefore fix only the earlier relation: [SC027 NWGmcNasalSpirantLoss](#rule-NWGmcNasalSpirantLoss) must follow [SC026 NWGmcNasalSpirantLengthening](#rule-NWGmcNasalSpirantLengthening). They do not identify a corresponding later constraint, and CAPR keeps the rule here because the same inherited development requires the nasal to disappear only after the preceding vowel has already been adjusted.
