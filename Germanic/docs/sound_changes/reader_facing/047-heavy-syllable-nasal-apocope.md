# Final short nasal low-vowel apocope

## Early low-vowel loss and its nasal fragment

The nasal deletion represented here belongs with
[SC041 PWGmcFinalBareALoss](#rule-PWGmcFinalBareALoss), not with a
separately established heavy-syllable Old English apocope. Ringe and
Taylor treat oral and nasal short-final low-vowel loss together as a
West Germanic development. Their comparative evidence includes *horn*
'horn' and the vocalization of glides stranded by vowel loss. Fulk
explicitly distinguishes this weight-independent loss from later,
quantitatively conditioned high-vowel loss
[@RingeTaylor2014, pp. 44--47, §§3.1.2--3.1.3;
@Fulk2018, pp. 79--81, 91--92, §§5.2, 5.6].

Campbell's discussion of protected endings and Hogg's account of earlier
final-consonant and vowel losses provide the surrounding history
[@Campbell1959, pp. 137--140, §331;
@HoggPhonology1992, pp. 62--64, §§3.27--3.32].
Campbell's separate discussion of nasal loss before fricatives does not
date this apocope or secondary vowel nasalization
[@Campbell1959, p. 166, §403].
The later back-mutation discussion concerns a different interaction
[@Campbell1959, pp. 85--86, §§205--206;
@RingeTaylor2014, pp. 319--327, §6.9.4].

## SC047. Final short nasal low-vowel apocope (`OEHeavySyllableNasalApocope`) {#rule-OEHeavySyllableNasalApocope}

```foma
define OEHeavySyllableNasalApocope Ctx([
    {*ą} -> 0 || OEAnyConsonant _ .#.
]);
```

The retained identifier contains an obsolete heavy-syllable description.
The operation has no weight restriction: both the light stem of *þæc*
'roof' and the heavy stem of *horn* undergo loss. Its consonant class
also includes the glides. That does not reconstruct their entire history:
Ringe and Taylor derive \emph{*sarwą > *saru} and
\emph{*rīkiją > *rīki}, continued by *searu* 'device' and *rīce*
'kingdom'. Their *mettas* 'foods' beside *mete* 'food' and OHG
*beti* 'bed' support low-vowel loss and glide vocalization before
j-gemination; the familiar geminate citation forms often reflect
extension from other paradigm cells
[@RingeTaylor2014, pp. 46--47].

The executable position is later than that historical argument would
suggest. Moving this fragment beside the oral loss changes no selected
endpoint; its present position after restoration is not necessary.
Moving it before gemination alone, however, removes vowel triggers
still needed by the serialized u-lowering and changes the treatment
of final consonants. Those dependencies explain limitations of the
implementation, not a historically late date for apocope. The secondary
final n of *dōn* 'do' must likewise be exposed only after
[SC023 PNWGmcNStemNLoss](#rule-PNWGmcNStemNLoss) has ceased to operate.

The old lower-bound test depended on the superseded straw proxy:
moving apocope before [SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong)
gave predicted \emph{*stræw} rather than attested OE *strēaw* 'straw'.
The adopted regular endingless branch now reaches reconstructed
\emph{*strēa} through
[SC111 PWGmcEndinglessAw](#rule-PWGmcEndinglessAw), before this apocope.
The attested target retains analogically restored \emph{w} and explicitly
mismatches the regular output. That older failure does not independently
place nasal apocope after a universal singleton long-diphthong law
[@Campbell1959, pp. 46--47, 232--233;
@RingeTaylor2014, pp. 172--173, 387].

For the retained final-n implementation,
[SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) must see
the n exposed by loss. Inverting the two operations gives predicted
\emph{*bacen} for *bacan* 'bake' and \emph{*binden} for *bindan* 'bind'.
This demonstrates a feeding relation between the two representations;
the same reversal recorded from both directions is not two independent
historical dates.
