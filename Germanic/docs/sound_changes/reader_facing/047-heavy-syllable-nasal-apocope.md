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
@HoggGrammar2011, pp. 62--64, §§3.27--3.32].
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
\emph{*rīkiją > *rīkī}, continued by *searu* 'device' and *rīce*
'kingdom'. Their *mettas* 'foods' beside *mete* 'food' and OHG
*beti* 'bed' support low-vowel loss and glide vocalization before
j-gemination; the familiar geminate citation forms often reflect
extension from other paradigm cells
[@RingeTaylor2014, pp. 46--47].

The long final vowel in \emph{*rīkī} matters: the source derives it
from \emph{ij}, not from a single stranded \emph{j}. Staged
nuclearization recovers this form and subsequently *rīċe*, while a
surviving medial j still conditions gemination. It does not complete
every derivation. Early \emph{*sarwą > *saru} loses the consonantal
environment for breaking; the present restoration then gives
\emph{*saru}, not *searu*. An oral-ending parallel likewise recovers
\emph{*gelu} but not the complete history of *ġeolu* 'yellow'.
These are wider-cascade limitations, not evidence against the
comparative vocalization or grounds for silently changing its quantity
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

Prior lowering is independently compatible with early loss:
Ringe and Taylor contrast the lowering environments of a-stems and
root nouns, and explicitly accommodate lowering before low-vowel
apocope. Fulk's lowering discussion is §4.3; his preceding §4.2
concerns closed-syllable shortening, not this ordering
[@RingeTaylor2014, pp. 27--29, 44--47, §§2.3.1(i), 3.1.2--3.1.3;
@Fulk2018, pp. 55--57, §§4.2--4.3, especially p. 57 n. 1].
Moving [SC017 PNWGmcULowering](#rule-PNWGmcULowering) before the
experimental early loss preserves all forty lowering applications and
recovers the twelve changed root-vowel outputs. Three other endpoint
differences remain: *dēor* 'deer' loses z instead of rhotacizing it,
*dor* 'door' acquires length when final r is exposed too soon, and
straw loses its endingless-diphthong input. Loss after ordinary final-z
deletion still gives predicted \emph{*dōr}; that is a separate
lengthening dependency, not a failure to restore lowering.
A thirteenth lost lowering, in *ġeoc* 'yoke', is hidden at the endpoint
by the later palatal-glide treatment. Endpoint agreement alone therefore
does not establish an unchanged derivation.

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
