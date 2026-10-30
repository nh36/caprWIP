# L-adjacent syncope

## Historical discussion

Vowel loss creates the clusters upon which later assimilation and degemination
operate. Hogg and Ringe and Taylor describe this dependence, while Brunner's
*netle* 'nettle' beside later *netele* 'nettle' supplies a concrete lexical type
[@HoggPhonology1992, p. 121; @RingeTaylor2014, pp. 264--296, §§6.7.3--6.8.2;
@SieversBrunner1965, pp. 144--145, §§158--159]. Fulk places this syncope after
i-umlaut [@Fulk2018, p. 91, §5.6].

The three relations are not equally secure. Lexical evidence orders syncope
and degemination; the intervening dental assimilation has no independent
ordering witness.

## SC066. L-adjacent syncope in medial syllables (`OELAdjacentSyncope`) {#rule-OELAdjacentSyncope}

```foma
define OELAdjacentSyncope Ctx([
    {*i} -> 0 || EnglishStarLongVowel OEAnyConsonant+ _ {*l},
    {*i} -> 0 || EnglishStarLongDiphthong OEAnyConsonant+ _ {*l},
    {*i} -> 0 || [EnglishStarShortVowel|EnglishStarShortDiphthong] OEAnyConsonant OEAnyConsonant+ _ {*l},
    {*i} -> 0 || [EnglishStarShortVowel|EnglishStarShortDiphthong] OEAnyConsonant _ {*l} EnglishStarVocalic
]);
```

The loss of medial \emph{*i} before \emph{*l} is late enough to preserve
earlier umlaut, as *netle* ‘nettle’ and *spinl* ‘spindle’ demonstrate.

Two historically distinct strata are stated here as one law. After a heavy
syllable the deletion continues the exceptionless prehistoric syncope of
unstressed high vowels in open medial syllables, the same law whose pre-dental
slice has already been treated: [spénnilō]{.recon} ‘spindle’ and the genitive
of [θístilas]{.recon} ‘thistle’ lose their \emph{*i} after the heavy sequences
\emph{-nn-} and \emph{-st-} [@RingeTaylor2014, pp. 270--272, §6.7.3;
@Campbell1959, p. 158, §392]. After a light syllable, however, the handbooks
describe a later and more particular development: unstressed \emph{*i} next to
\emph{l} is lost even where the preceding syllable is light, as in *netle*
‘nettle’ from the diminutive [nátilōn]{.recon} ‘nettle’ [@Kroonen2013, p. 384;
@RingeTaylor2014, p. 272, §6.7.4]. Luick, following Weyhe, restricts this
light-syllable deletion to trisyllabic forms whose middle syllable was open,
dating it before the literary period after dentals and to the eighth century
after gutturals [@Luick1914, §336]; Brunner likewise treats it as regular in
the oldest sources after light syllables [@SieversBrunner1965, pp. 132--133,
§159c]; Campbell describes medial vowels as dropped after short syllables when
a group of consonant plus \emph{l} or \emph{r} would result [@Campbell1959,
pp. 157--158, §§388--390].

The open-syllable condition carries the explanatory weight. *Cetel* ‘kettle’,
an early Latin loan ([katilaz]{.recon} ‘kettle’, from \emph{catillus}), famously fails
to syncopate [@Orel2003, p. 211; @RingeTaylor2014, p. 272]. It is not a
lexical exception. Its nominative \emph{*i} stands, after apocope, in a
word-final closed syllable — light and closed — a position that no published
formulation of the change reaches. The same structural point explains the
nominative--oblique split that Campbell records for the *netel*/*spinel*
class, where the nominative retains its vowel while the syllabically open
oblique cases syncopate [@Campbell1959, pp. 235--236, §589]. Within its properly
stated domain — after a heavy syllable, or after a light syllable in an open
medial syllable — the deletion is regular.

The sources disagree about the residue of variation. Weyhe, Luick, and
Brunner treat the law as categorical within its consonant-class and dialect
conditions, explaining late West Saxon *netele* as anaptyxis, a secondary
vowel reinserted in the cluster [@Luick1914, §336; @SieversBrunner1965,
p. 133, §159 Anm. 3]. Ringe and Taylor instead read pairs such as *crypel*
beside dative *cryple* as a change arrested before completion, leaving stable
variation [@RingeTaylor2014, p. 272]. The selected corpus cannot discriminate
between these readings, since its witnesses lie in the post-dental territory
that all parties treat as deleted; both accounts are therefore recorded
without a forced choice.

Barrack reaches the same material through his framework of progressive
environment simplification. His rule for medial high-vowel deletion in open
syllables after long accented syllables corresponds to the heavy-syllable
stratum, and in West Saxon he drops the length condition, generalizing the
deletion to light syllables [@Barrack1975, p. 87]. A separate rule deletes an
unstressed vowel before a liquid or nasal followed by a vowel, and he reports
that West Saxon simplified the environment further by dropping the
following-vowel condition entirely [@Barrack1975, p. 96]. The present law
retains the following-vowel condition for the light stratum: dropping it, as
Barrack's West Saxon formulation would, predicts syncope in the *cetel*
nominative. His neighbouring rule deleting a vowel after a liquid, which
derives *meolc* ‘milk’ from [meluk]{.recon} ‘milk’ [@Barrack1975, p. 96], is likewise
not adopted: West Saxon *meoloc* retains the vowel, and medial \emph{*u} next
to \emph{l} is in general kept far longer than \emph{*i} [@Luick1914, §336.2;
@RingeTaylor2014, p. 273].

Placed before i-umlaut, PGmc [nátilōn]{.recon} ‘nettle’ yields [*nætle*]{.pred} rather than
expected OE *netle* ‘nettle’, and PGmc [spénnilō]{.recon} ‘spindle’ yields [*spenl*]{.pred} rather
than expected *spinl* ‘spindle’. Placed after preconsonantal degemination, PGmc
[spénnilō]{.recon} yields [*spinnl*]{.pred} rather than expected *spinl*. The witnesses
therefore establish the sequence i-umlaut, l-adjacent syncope, preconsonantal
degemination. The first relation separates two historical phases; the second is
a direct feeding relation, since syncope creates the cluster that degemination
simplifies.
