# Intervocalic h-loss

## Historical discussion

When [SC085 OEHLoss](#rule-OEHLoss) removes intervocalic \emph{*h}, it creates
hiatus. [SC086 OEContraction](#rule-OEContraction) is the next operation in
the executable cascade, but loss and contraction are distinguishable
historical developments: the glossaries preserve forms still in hiatus.

Ringe and Taylor describe this late sequence of \emph{h}-loss and contraction
[@RingeTaylor2014, pp. 305--314, §§6.9.1--6.9.3]. Fulk places the contracted
verbs in a broader Germanic context [@Fulk2018, p. 270, §12.21], and Luick
describes the corresponding West Germanic contractions [@Luick1914, p. 165].

For clay, Épinal 3 has *thohae* 'clay' under Latin argillus (-a), while
Corpus 207 has *thoae* 'clay' under argilla [@Sweet1885, pp. 36, 41].
Ringe and Taylor read these as *thōhæ* 'clay' and *thōæ* 'clay', followed
by contracted *þō* 'clay' [@RingeTaylor2014, p. 314, §6.9.3].
On that reading a front ending was already present with the fricative;
loss then left the vowels in hiatus, before contraction.

Fringe supplies the contrasting environment. Épinal 1066 and the aligned
Erfurt parallel have *uulohum* 'fringe', whereas Corpus 2122 has *uuloum*
'fringe', all under Latin villis [@Sweet1885, pp. 104, 107].
The normalized dative plural *wlōhum* 'fringe' thus gives *wlōum* 'fringe':
both flanking vowels are back, and both the vowel and consonant of the
ending \emph{-um} survive loss. A front vowel was therefore unnecessary
for intervocalic loss [@RingeTaylor2014, p. 314, §6.9.3].

These related early Mercian glossary witnesses preserve different states
of the forms. Their textual relationship permits comparison without
assigning absolute dates to the changes from the dates of the surviving
copies. Nor does written \emph{h} by itself settle the fricative's phonetic
value: CAPR's assignment of [ç] before a following front vowel at
palatalization is a model analysis, not a transcription of that letter.

In the current stage trial for *þō* 'clay', the early final-vowel merger
and subsequent fronting supply \emph{ǣ} before palatalization, where
CAPR assigns [ç]. Shortening and merger then supply \emph{e}
while the fricative is still present; loss leaves
\emph{ō + e}, and contraction produces the contracted form. This verifies
the front-ending/fricative/hiatus sequence without equating the trial's
\emph{e} with the glossary spelling \emph{ae}. The historical interpretation
of that distinction is discussed with
[SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger).

## SC085. Loss of intervocalic \emph{*h} (`OEHLoss`) {#rule-OEHLoss}

```foma
define OEHLoss FootCtx([
    [{*x}|{*ç}] -> 0 || EnglishStarVocalic _ EnglishStarVocalic
]);
```

The rule removes singleton intervocalic \emph{*h} in either model
allophone. It must not depend on a front neighbour: *wlōhum* 'fringe'
loses the fricative between back vowels while retaining \emph{-um}.
Geminates do not meet the singleton environment. The existing foot
wrapper protects pretonic material: Campbell explicitly retains
intervocalic \emph{h} between an unaccented and an accented vowel in
*behindan* 'behind', *behealdan* 'hold', *gehelpan* 'help' and
*toheald* 'inclined' [@Campbell1959, pp. 186--187, §§461, 464--465].
Thus the prosodic guard has independent support; it is not a lexical
exception introduced to protect matching outputs.
Contraction can subsequently resolve the hiatus, but the hiatus is itself attested.

The [reviewed final-nasal candidate](https://github.com/nh36/caprWIP/commit/4b232d22ad3d55ecf0eb2111b736dcf4349a4bde)
reproduces the toe boundary in two separately executed trials. Moving
loss before [SC073 OEUnstressedAEMerger](#rule-OEUnstressedAEMerger), or
moving merger after loss, removes the palatal fricative while the ending
is still \emph{æ}. The resulting \emph{ā + æ} neither meets the merger's
consonantal context nor contracts, yielding [*tāæ*]{.pred} rather than
OE *tā* 'toe'. Unperturbed, merger first supplies \emph{e}; loss leaves
\emph{ā + e}, and contraction gives *tā* 'toe'.
The [earlier loss-displacement record](https://github.com/nh36/caprWIP/commit/196b8f6b73d825d86830bb8612834f50f865b9e4)
has the same final failure, but is a distinct, dated measurement, not the
source of these candidate intermediates. The result remains a computational
boundary observation, not independent historical proof that merger preceded
loss. If Corpus *thoae* 'clay' preserves distinct unstressed \emph{æ},
the clay witness instead puts loss before merger in that form. Whether this
spelling distinguishes \emph{æ} from \emph{e} remains open; a successful
contracted endpoint cannot decide it.

If loss is delayed until after [SC086 OEContraction](#rule-OEContraction), PGmc [fléuxaną]{.recon} ‘flee’ yields [*flēoan*]{.pred} rather than expected OE *flēon* ‘flee’, PGmc [sláxaną]{.recon} ‘slay’ yields [*sleaan*]{.pred} rather than expected *slēan* ‘slay’, PGmc [téxun]{.recon} ‘draw’ yields [*teoon*]{.pred} rather than expected *tēon* ‘draw’, and PGmc [táixōn]{.recon} ‘toe’ yields [*tāe*]{.pred} rather than expected *tā* ‘toe’. These outputs require loss before contraction in the current cascade. The four displacement witnesses agree with the glossary evidence for that sequence; neither their executable adjacency nor the copy dates establish an immediate historical succession.
