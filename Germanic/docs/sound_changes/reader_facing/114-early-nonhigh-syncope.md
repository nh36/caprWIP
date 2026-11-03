# Early nonhigh-vowel syncope

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
open posttonic syllable before a final heavy syllable. Primary-root
weight is not an additional condition. The heavy-final restriction
delimits this supported core; it is not asserted as a universal theorem
about every Old English nonhigh loss. A positively identified primary
root protects its own vowel, and the existing stress-domain machinery
admits the supported single pretonic syllable. Wider multiprefix and
light-final histories are not inferred from this restricted account.

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
[SC066 OELAdjacentSyncope](#rule-OELAdjacentSyncope) retain their
distinct high-vowel decisions; this phase does not broaden them.
Likewise, *weorold* 'world', *eorþcunde* 'earthly' and
*reġnboga* 'rainbow' retain their established histories.

## SC114. Early nonhigh syncope (`OENonHighSyn`) {#rule-OENonHighSyn}

```foma
define OENonHighSyn FootCtx([
    [{*a}|{*æ}|{*e}] -> 0 ||
        .#. OEAnyConsonant* EnglishStarVocalic
        [OEAnyConsonant+ EnglishStarVocalic]* OEAnyConsonant+
        _ [OEAnyConsonant
           [EnglishStarLongVowel|EnglishStarLongDiphthong|{*ô}]
           OEAnyConsonant* |
           OEAnyConsonant EnglishStarVocalic OEAnyConsonant+] .#.
]);
```
