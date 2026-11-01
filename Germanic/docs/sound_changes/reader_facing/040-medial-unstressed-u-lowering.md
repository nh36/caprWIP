# Medial unstressed-u lowering

## SC040. Lowering of medial unstressed \emph{*u} (`OEMedUnstressedULowering`) {#rule-OEMedUnstressedULowering}

```foma
define OEMedUnstressedULowering [MPFoot .o. MPULower .o. MPDecode];
```

Medial unstressed \emph{*u} lowers to \emph{*o} in the later Old
English period, while accented \emph{*u} preserves the following unstressed
vowel [@Campbell1959, pp. 155--156, §373]. This lowering follows the earlier shortening
and resolution of unstressed long vowels, rather than preceding that
history. The eighth-century unstressed back-vowel system and its later
development distinguish the two periods
[@StauslandJohnsen2015, pp. 21--22, 28--31].

The inherited ordering evidence from *wuduwe* 'widow' remains relevant:
delaying
[SC039 OEWICombinativeUUmlaut](#rule-OEWICombinativeUUmlaut) until after lowering yields
[*wudowe*]{.pred} rather than the expected form. In the adopted sequence,
*wuduwe* retains its medial vowel after accented \emph{*u}, whereas
*weorold* 'world' undergoes lowering.

### Medial prominence and the initial foot

The retained \emph{u} of *eorþcunde* 'earthly' is not an exemption
for a suffix or an inflection. Its heavy first syllable is followed
by a nonfinal heavy syllable which can head a medial foot. In contrast,
an initial light syllable is accommodated with a following syllable,
including a heavy one, in the initial foot. These distinct configurations
are supported by the quantity-sensitive analyses of
McCully and Hogg and Goering
[@McCullyHogg1990, pp. 323--333, especially pp. 330--333;
@Goering2023, pp. 79--84, §§4.5.1.1--4.5.2].

The relevant short diphthong \emph{*éo} counts as one short nucleus,
not as two separate vowels. In the inflected control
\emph{*wéoruldes}, syllabification gives light \emph{*weo}, heavy
\emph{*rul} and final \emph{*des}. The first two belong to the
initial light–heavy foot; the medial \emph{u} is not a separate
head and lowers. The shorter selected *weorold* has the same initial
accommodation. In *eorþ.cun.de*, the initial \emph{*eorþ} is heavy
and the subsequent nonfinal \emph{*cun} is independently heavy:
its \emph{u} is protected. The genitive control *eorþcundes* has
the same contrast. This explanation depends on the phonological
representation at lowering, not on the spelling of a comparative
citation form.

The independent comparisons *æþelingas* 'princes' versus *cyningas*
'kings', and *rīdende* 'riding' versus *wesende* 'being', test
initial-foot accommodation with different vowel classes. Inflected
*godcundne* 'divine' and *godcundre* 'divine' supply medial retention
comparisons, not permission to exempt the whole formation
[@McCullyHogg1990, pp. 330--333; @HoggGrammar2011, pp. 49--50,
§2.89]. Final uninflected *godcund* remains outside this nonfinal
medial-foot computation; the complete paradigm is not thereby derived.

### Temporary computation, not another inherited-accent loss

The implementation syllabifies the current string, accommodates the
initial foot and marks eligible later closed short-vowel heads.
It uses the existing short-vowel and short-diphthong inventories.
Temporary graves on \emph{a e i o u} distinguish computed prominence
from the inherited compound accent, already removed by
inherited secondary-accent deletion.
They are decoded immediately after this lowering. The existing
pretonic-prefix representation is accommodated without inserting a
new initial boundary or relocating inherited accent deletion.

Segmental conditioning is retained: the preceding \emph{u}-class
nuclei and following \emph{m} block lowering, with the same consonant
classes. A temporarily marked \emph{ù} also belongs to that preceding
exclusion; changing its technical marking must not make it license
lowering of a subsequent \emph{u}. This is preservation of the original
condition, not a new harmony law.

Hogg cautions against using “tertiary stress” merely to rename a desired
retention, and distinguishes labial-nasal preservation from ordinary
\emph{-un > -on} [@Hogg1996, pp. 8--11, especially p. 11 n. 7;
@HoggGrammar2011, pp. 239--241, §§6.55--6.58]. The computation consequently
uses weight and domain rather than lexical identity or a blanket
dental-nasal exception. Nor does metrical prominence by itself certify
speech-stress history [@MinkovaZhou2023, pp. 86--90]. This is a bounded
prosodic projection for the present sound law, not a complete cyclic
Old English stress grammar.

### Existing chronological distinctions

*Reġnboga* 'rainbow' is not a further live example: its second-root
\emph{o} arose while subordinate stress was still represented, under
[SC017 PNWGmcULowering](#rule-PNWGmcULowering).
Its linking-vowel history therefore does not require secondary-accent
loss before the present late lowering.

The reciprocal early-lowering experiment is no longer equivalent: the
intervening vowel-resolution history restores medial \emph{*u}, so that
movement does not now produce the same *widow* failure.

The formerly reported *ġeoguþ* 'youth' boundary does not establish that
lowering preceded
[SC072 OEUnstressedLongVowelShortening](#rule-OEUnstressedLongVowelShortening).
That experiment inserted a front glide vowel early in the derivation;
delayed lowering then encountered an altered preceding nucleus and
produced [ġeogoþ]{.pred}. With the adopted late
[SC016 OEWsPalatalGlide](#rule-OEWsPalatalGlide) spelling, the root retains
phonological \emph{*u} through lowering and preserves the medial vowel.
Moving lowering across shortening in this current architecture leaves
*ġeoguþ* unchanged. The spelling evidence is therefore not an independent
date for the lowering; the later placement rests on the historical
vowel chronology, not a reversal of that obsolete experiment.
