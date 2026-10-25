# Endingless \emph{aw} and the retained show proxy

## Historical discussion

The attested long nucleus does not establish one general law changing
singleton \emph{aw} to \emph{ēaw} before every following vowel.
For straw, the inherited nominative/accusative \emph{*stráwą} loses its
ending and vocalizes final \emph{w}, giving \emph{*strau}; the ordinary
English development then gives reconstructed \emph{*strēa}. Attested
*strēaw* 'straw' combines that long diphthong with \emph{w} restored
from inflected forms. Conversely, the long diphthong spreads into those
forms. The regular free simplex and short obliques are explicitly
unattested, although the endingless pattern survives in the compound
*strēaberige* 'strawberry'
[@Campbell1959, pp. 46--47, 232--233;
@SieversBrunner1965, pp. 49, 110, 204--205;
@RingeTaylor2014, pp. 172--173, 387].

The model retains attested *strēaw* 'straw' as its comparison target and produces
reconstructed \emph{*strēa} through the regular cascade. This is an
explicit mismatch, not an attested reconstructed endpoint or a sound law
for analogical restoration.
[SC111 PWGmcEndinglessAw](#rule-PWGmcEndinglessAw) supplies the narrow
endingless fragment; it does not imply that general final-vowel loss
was conditioned by an adjacent \emph{w}.

The inherited geminates of *dēaw* 'dew' and *hēawan* 'hew' instead undergo
early
[SC031 OEWWSimplification](#rule-OEWWSimplification), producing
\emph{*au} plus retained \emph{*w}, followed by English fronting and
[SC032 OEDiphthongLeveling](#rule-OEDiphthongLeveling).
Campbell distinguishes the glide histories; Ringe and Taylor distinguish
earlier reanalysis from later English realization
[@Campbell1959, pp. 45--47, 53--54; @RingeTaylor2014, pp. 65--66, 171--175].
These retained-glide histories differ from endingless straw.

For *sċēawian* 'show', Orel and Kroonen print singleton dictionary
inputs, while Campbell and Brunner include the verb among inherited
geminate examples. The class-II suffix places a vowel between root
\emph{w} and \emph{j}; this excludes direct root \emph{aw+j}
gemination but does not resolve the different root histories
[@Orel2003, p. 337; @Kroonen2013, p. 442;
@Campbell1959, p. 45; @SieversBrunner1965, p. 49].
[SC034 OEAwLongDiphthong](#rule-OEAwLongDiphthong) therefore remains
a disclosed support proxy for the three selected show cells, not an
established general singleton sound law or a newly dated West Saxon event.

## SC034. Retained show long-diphthong proxy (`OEAwLongDiphthong`) {#rule-OEAwLongDiphthong}

```foma
define OEAwLongDiphthong Ctx([
    {*a} {*w} -> {*ēa} {*w} || _ [EnglishStarVocalic | {*ô}],
    # Stressed variant (prosodic tier):
    {*á} {*w} -> {*ḗa} {*w} || _ [EnglishStarVocalic | {*ô}]
]);
```

The current operation changes the show infinitive, imperative singular
and present third singular. Straw already has its regular long nucleus
without \emph{w} and is unchanged here. Dew and
hew no longer demonstrate a local simplification-then-lengthening chain
here: their earlier reanalysis has already removed that input shape.
The older displacement results for those geminates describe the superseded
representation, not independent dates for the adopted early event.
The two proxy clauses remain unchanged; their successful show finals
do not decide the unresolved singleton-versus-geminate source premise.
The old straw displacement observation measured dependence on a
following vowel in the superseded proxy, not independent historical order
[@Campbell1959, pp. 45--47; @RingeTaylor2014, pp. 171--175].
