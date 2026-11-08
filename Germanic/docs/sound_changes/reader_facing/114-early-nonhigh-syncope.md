# Ordinary nonhigh-vowel syncope

## Historical discussion

Old English nonhigh-vowel syncope must be distinguished from the later
high-vowel losses. Hogg describes loss of a short nonhigh vowel in an
open medial syllable, after both light and heavy roots, with restoration
and paradigm interactions considered separately. His account places
the process after umlaut and before unstressed \emph{i} lowers
[@HoggGrammar1992, pp. 220--222, §§6.14--6.18].
Luick's longer-word cases warn against reducing the domain to exactly
three syllables [@Luick1914, pp. 279--280, §303].
These are phonological and prosodic conditions, not permissions for
particular words or grammatical classes.

The implemented core deletes plain short \emph{a, æ, e} from an
open posttonic syllable. Primary-root weight and final-syllable weight
are not additional deletion conditions. A following singleton consonant
and vowel identify the bounded open-medial domain; this does not silently
claim complete syllabification of arbitrary consonant clusters.
A positively identified primary
root protects its own vowel, and the existing stress-domain machinery
admits the supported single pretonic syllable. Wider multiprefix
histories are not inferred from this restricted account.

### Selected applications and contrasting forms

The strong masculine nominative plural participle
\emph{*fúnðanai} gives *fundne* 'found', attested in *Juliana*335.
The inherited ending becomes long \emph{ē}; medial \emph{a}
then disappears before its still-heavy final syllable, and later
shortening gives final \emph{e}. The cell is supported independently
by the edition's syntax and glossary, while the reconstructed whole
word combines participial formation and adjectival inflection
[@Strunk1904, pp. 15, 82; @Fulk2018, p. 209, §9.2, p. 284, §12.30].
The genuine longer *fundene* 'found' and competing inherited
participial suffixes remain evidence for the wider paradigm, not
exceptions manufactured by changing the sound law.

The inherited accusative \emph{*sáiwalǭ} gives *sāwle* 'soul'.
After stressed-diphthong monophthongization, medial \emph{a}
is lost before the quantity-bearing inherited ending; its later
decoding and shortening supply final \emph{e}. The ending notation
does not imply unchanged late phonetic nasal rounding.
Luke12:20 establishes the accusative, distinct from the neighbouring
dative and vocative [@Skeat1874, p. 130].
No raising proxy or epenthesis is required in this selected span.
Fulk's competing metrical account and the syncope/apocope/epenthesis
history proposed for nominatives remain independent questions
[@Fulk2010, pp. 133--139; @RingeTaylor2014, pp. 265, 330].

Citation *hamer* 'hammer' is a nonapplication: earlier final-vowel
loss leaves the nonhigh vowel in the last syllable. By contrast, the
longer genitive input predicts *hamres*, not attested *hameres*
'of a hammer'; that wider history remains unresolved
[@WrightWuelcker1884, vol. 1, p. 272, line 36; @Toller1921, p. 505].
The inherited neuter base \emph{*wéstą} gives *west* 'westwards'
through existing nasal-vowel apocope, with no medial syncope target
[@Orel2003, p. 459; @Fulk2018, p. 146, §7.8].

### Relative chronology and limits

The executable position immediately before
[SC063 OEHighVowelApocope](#rule-OEHighVowelApocope) preserves
visibility of the inherited final quantity. That serialization is a
model-local representation choice, not a new independently demonstrated
historical ordering inferred from output success.
The source-supported chronology and the notation's lifetime must be
kept separate. The rules
[SC065 OEMedialSyncope](#rule-OEMedialSyncope) and
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) now distinguish
ordinary heavy/open high-vowel loss from later light pre-\emph{*l}
loss. *Weorold* 'world' retains its established selected history.
*Eorþcunde* 'earthly' and *reġnboga* 'rainbow' now lose the linking
\emph{*a} here rather than through the former early proxy.

## Compound formation and comparative linking-vowel evidence


Compound members with weakened force often lose or reshape their linking vowels, and Campbell treats that broad pattern through reduced second elements, connecting vowels, and obscured compounds [@Campbell1959, pp. 148--149, §§356--357; @Campbell1959, p. 153, §367; @Campbell1959, p. 159, §§386--387].

Those discussions concern several distinct developments: modification and
shortening within obscured second roots, connecting-vowel insertion, and
weak-vowel quality changes do not by themselves demonstrate deletion of a
linking vowel. For syncope, the relevant distinction is between short
nonhigh vowels, whose loss does not require a heavy first syllable, and
high linking *i/u*, whose regular heavy-root loss supplies the weight
condition modelled under [SC065 OEMedialSyncope](#rule-OEMedialSyncope). That condition is not an exhaustive account of
all historical compound losses. The handbooks compare retention in
light-root *Winifrið/Winefrið* and *duruweard* 'doorkeeper'
with loss in *dælnimend* 'partaker' and *handclāð* 'towel'
[@Campbell1959, p. 143, §341; @Campbell1959, pp. 145--146, §§348--353;
@HoggGrammar2011, pp. 220--223, §§6.14--6.19;
@RingeTaylor2014, pp. 266--267; @SieversBrunner1965, pp. 137--138, §§167--168].
These are comparison forms, not additional selected
derivations. Variant first stems and the *hild-/hilde-* material require
source-critical analysis rather than an automatic rule conditioned by the
identity or weight of the second member [@RingeTaylor2014, p. 303].

The handbook comparisons do not yet provide a selected complete history
testing the newly restricted high-vowel clause. In particular, Orel
reconstructs Proto-Germanic [đura-warđaz]{.recon .iv lang=pgmc sort=durawardaz role=source_protoform} 'doorkeeper', with an *a*-linker,
and compares Gothic [*daura-wards*]{.iv lang=goth sort=daurawards role=comparison_form} 'doorkeeper'; Kroonen derives the
Old English simplex [*duru*]{.iv lang=oe sort=duru role=comparison_form} 'door' from [durō-]{.recon .iv lang=pgmc sort=duro role=source_protoform}. Neither fact
establishes an inherited short linking *u* in [*duruweard*]{.iv lang=oe sort=duruweard role=comparison_form} 'doorkeeper', nor an
independently demonstrated change supplying it before syncope.
Its attested vowel cannot simply be substituted into the earlier
compound reconstruction. The retained name vowels also need their own
formation histories [@Orel2003, p. 79; @Kroonen2013, p. 110;
@SieversBrunner1965, pp. 137--138, §168].

The older names cannot simply be dismissed as exceptions to a universal
heavy-root requirement. Sievers and Brunner, Campbell, Luick and Hogg
explicitly recognize high-vowel loss after light first roots, including
[*Sigfrið*]{.iv lang=oe sort=sigfrith role=comparison_form} and
[*Hyglāc*]{.iv lang=oe sort=hyglac role=comparison_form}.
Luick distinguishes chronological layers and says that the circumstances
of the change are not yet understood. Hogg also discusses the second
member's weight. These observations require a bounded reconsideration
of an exhaustive weight-only account; they do not license lexical
optionality, a rule restricted to personal names, or an unsupported
appeal to analogy. Nor does the manuscript date of a name independently
date its formation or syncope [@SieversBrunner1965, pp. 137--138, §168;
@Campbell1959, pp. 145--146, §§348--349;
@Luick1914, pp. 283--284, §305; @HoggGrammar2011, pp. 224--225, §6.21].

[*seleweard*]{.iv lang=oe sort=seleweard role=comparison_form} 'hall-warden'
provides a stronger retained-vowel candidate. Orel prints
[sali-warđaz]{.recon .iv lang=pgmc sort=saliwardaz role=source_protoform}
and [sali-warđuz]{.recon .iv lang=pgmc sort=saliwarduz role=source_protoform},
with Old Norse [*sal-vǫrðr*]{.iv lang=on sort=salvordr role=comparison_form}
'hall-warden'. Both reconstructions have first-member *i*; their
alternatives concern the second member's inflection, not an *a/i*
linker choice. The first member's secondary i-stem history is independently
supported. Nevertheless, these transparent formations do not discriminate
inheritance of this particular compound from later independent formation:
Orel expressly reports Carr's parallel-formation assessment. Beowulf
attests the Old English accusative singular, but does not independently
place the compound before the relevant syncope. Neither an ending nor a
high linker has to be invented; the unresolved premise is formation
chronology [@Orel2003, pp. 315, 448; @Kroonen2013, p. 424;
@ClarkHall1960, p. 260, Beowulf 667].

The canonical grammar now recognizes inherited high-vowel first members
and the second member's dental cluster without sacrificing older accepted
analyses. Both printed hypotheses, and the ordinary a-stem accusative
\emph{*sáli-wàrðą}, regularly produce *seleweard*. Previously the
retained plain medial *i* incorrectly underwent breaking, producing
[seleoweard]{.pred}. Restoring the former early high-vowel deletion instead
produces [sealweard]{.pred}; removing the later weight condition produces
[selweard]{.pred}. These are three distinct wrong analyses, not three
attestations. Correct output establishes a conditional derivation, not the
date or inheritance of the compound.

No new lexical selection is made without that independent formation
premise. Complete selected weight controls and independently reconstructed
later-stage controls now test the high-vowel core described under
[SC065 OEMedialSyncope](#rule-OEMedialSyncope); they do not supply a
complete inherited-compound discriminator for the former early rule. [*reġnboga*]{.iv lang=oe sort=regnboga} 'rainbow' and [*eorþcunde*]{.iv lang=oe sort=eorthcunde} 'earthly'
remain genuine selected *a*-deletion witnesses, not evidence for the
new high-vowel restriction. The source-proposed *ūtumist* history supplies a
distinct transmitted-mutation and weak-vowel-loss control; its final root
alone does not independently order mutation against loss of *u*
[@RingeTaylor2014, p. 267].

Barrack's weak-vowel fronting and quality rules 333a/b and his rounding
rule 335 belong to this wider discussion, but are not equivalent
linking-vowel deletion laws. Their formal ordering is not independent
evidence for dating syncope or removal of secondary stress
[@Barrack1975, pp. 82--84].

The former [SC037 OECompoundLinkingSyncope](#rule-OECompoundLinkingSyncope)
proxy captured this pattern in *reġnboga* 'rainbow'. Its second-root vowel
has already lowered under subordinate stress:
\emph{*régna-bùgô > *régna-bògô}. The grave survives that early
change and formerly licensed early deletion of the linking vowel, giving
\emph{*régnbògô}; ordinary accent stripping formerly gave
\emph{*régnbogô}. The full account and its reconstruction qualifications
belong to [SC017 PNWGmcULowering](#rule-PNWGmcULowering), not to late
unstressed lowering. Its immediate annotation dependency does not date historical nonhigh
syncope. The handbooks place ordinary nonhigh syncope after breaking, and
high-vowel loss normally after mutation. The early *a* fragment is retained
as a selected-input holding proxy in the earlier model. It is now an
identity: ordinary nonhigh deletion applies here, independently of a
surviving grave, and inherited \emph{*b} receives positional realization
afterward under [SC049 PGmcBAllophony](#rule-PGmcBAllophony).
The high-vowel component follows mutation
[@SieversBrunner1965, pp. 137--138, §167 and notes;
@HoggGrammar2011, pp. 220--224, §§6.14--6.20;
@RingeTaylor2014, pp. 266--267].

The earlier proxy's apparent dependency on grave removal did not date a universal loss of compound secondary stress. The relevant junctures also relate to [SC035 OEPrefixAReduction](#rule-OEPrefixAReduction) and [SC036 OEInterStressRaising](#rule-OEInterStressRaising). Russom's metrical review challenges obligatory positional destressing; modern stress marks are annotations, not independent prosodic evidence for every historical name [@Russom2001, pp. 39--64].

## SC114. Ordinary nonhigh syncope (`OENonHighSyn`) {#rule-OENonHighSyn}

```foma
define OENonHighSyn FootCtx([
    [{*a}|{*æ}|{*e}] -> 0 ||
        .#. OEAnyConsonant* EnglishStarVocalic
        [OEAnyConsonant+ EnglishStarVocalic]* OEAnyConsonant+
        _ OEAnyConsonant EnglishStarVocalic
        [OEAnyConsonant|EnglishStarVocalic|{*ô}]* .#.
]);
```
