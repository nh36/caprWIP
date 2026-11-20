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
The isolated direct branches are incomplete, but the history of *searu*
is not unexplained: *searwes* 'of a device' preserves the environment for breaking,
and Campbell, Hogg, and Hogg and Fulk explicitly extend its diphthong
into the direct cases. This is positive evidence for analogy, not a
repair inferred merely from a failed output. Ball and Stiles likewise
derive the broken root of *ġeolu* from w-bearing forms; the direct
\emph{*gelu} branch instead has a different regular continuation.
The model has no paradigm-transfer operation
[@Campbell1959, pp. 230--232, §§579--582;
@HoggGrammar2011, p. 92, §5.32(4);
@HoggFulk2011, pp. 22--26, §§2.27--2.33;
@BallStiles1983, pp. 15--18, §4].

The chronology itself has a published alternative. Hogg and Fulk
prefer oral nominative loss before gemination but nasal accusative
loss afterwards; their alternative, following Campbell and Dal,
loses both early and extends geminates from other cells. Boutkan also
prefers gemination before low apocope. These accounts must be compared
as histories of paradigms, not chosen by the fit of citation forms
[@HoggFulk2011, pp. 20--21, §2.23;
@Boutkan1995, pp. 209--213, 435--436].

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
Moving unchanged [SC112 PNWGmcMonosyllabicFinalRLengthening](#rule-PNWGmcMonosyllabicFinalRLengthening)
before the experimental loss restores short *dor*, preserving exactly
the two original lengthening applications. This is an executable
prerequisite of that candidate, not an independent historical date.
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

The direct-case *r* of *dēor* 'deer' is likewise not independently established
by the late executable derivation. Under the early-loss account it
comes from inflected cells with internal z. The supplied dictionary
dative resolves to Northumbrian *deare* 'animal' (dative singular), not
a diplomatic West Saxon *dēore* 'animal' token; West Saxon *deora*
'animals', the genitive plural in
Ohthere's account, provides a secure independent oblique. Its
reconstruction \emph{*deuzôⁿ} regularly retains internal z, whereas
the direct cell exposes it to northern final-z loss. The genitive
plural is a proposed scoring alternative, not a silently changed
selection [@KembleHardwick1858, p. 19, capitulum LXXIX;
@Bosworth1859, p. 20, lines 25--27;
@RingeTaylor2014, pp. 86--87, 174; @Fulk2018, pp. 148--149, §7.8].

The current apocope position is retained. The position beside oral
loss remains endpoint-equivalent; the pre-gemination package makes
real progress on the stranded-glide intermediates, but still changes
hay, net and hue and needs explicit paradigm histories. The
same-site endingless-aw companion to
[SC111 PWGmcEndinglessAw](#rule-PWGmcEndinglessAw) separately restores
regular reconstructed \emph{*strēa}; it does not derive attested
*strēaw* 'straw'. These are tested alternatives, not adopted reorderings.
