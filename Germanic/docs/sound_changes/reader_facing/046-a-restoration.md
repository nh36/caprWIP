# A-restoration

## Historical discussion of A-restoration

Campbell's restoration of \emph{a} before following back vowels and Ringe and Taylor's later retraction describe the same post-brightening development in the adopted southern account [@Campbell1959, pp. 60--61, §§157--159; @RingeTaylor2014, pp. 189--190, §6.3.1; @Fulk2018, p. 74, §4.13]. Some outcomes of Anglo-Frisian fronting survive only in environments where restoration does not return them to back \emph{a}. This does not establish an identical history for every Old English dialect.

The familiar argument starts from West Saxon *slēan* 'slay'. If its diphthong arose by breaking of \emph{*æ}, fronting must have preceded breaking even before a velar fricative and a back vowel. Extending the same phonetic conditioning to *dagum* 'days' then motivates an earlier \emph{*dægum} and subsequent restoration. That is a regularity inference, not an attested intermediate. Versloot instead allows fronting followed by fricative loss and contraction in *slēan*, challenging the extrapolation from hiatus to other breaking environments. Northumbrian *slāa* 'slay' admits an earlier restoration under Hogg's interpretation, which Fulk explicitly treats conditionally; it does not reverse the adopted southern order [@Campbell1959, p. 60, §157; @HoggGrammar2011, pp. 96--97, §5.38; @RingeTaylor2014, pp. 189--190; @Versloot2021Review, pp. 93--95; @Fulk1998, pp. 150--151].

Dresher distinguishes restoration from retraction before back *l*. In his account of Mercian second fronting, loss of a synchronic restoration rule exposes front underlying vowels while independent consonantal retraction preserves forms such as *hwalas* 'whales' and *ald* 'old'. His representations of the nonalternating 'hawk', 'fork' and 'saddle' nouns, and the glossary distributions of *a*, *æ* and *ea*, are important evidence for the representation argument. His differing orders of restoration loss and back mutation in Épinal and Corpus are not direct records of every reconstructed phonetic stage; the glossaries also share a complicated transmission history [@Dresher1985, pp. 205--217, 229--250; @Seiler2019, pp. 527--528,536--538].

The early evidence does not uniformly decide between restoration and blocked fronting. Épinal *spadan* 'spades' is compatible with both; its weak-stem endings must also be assessed against independently documented paradigm remodelling. Épinal *-hebuc* 'hawk' is missed by both simplified accounts and must not be replaced with Erfurt's *-haebuc*. Épinal *fristmearc* 'interval' retains *ea* where an early breaking-plus-smoothing package predicts *æ*, but that contrast involves smoothing and dialect or transmission as well as fronting, not restoration alone. Versloot's quantitative comparison concerns early Anglian, expressly not a replacement West Saxon chronology [@Pheifer1974, pp. 27,29,57,134, nos. 497,547,1087; @RingeTaylor2014, pp. 153--154,376; @Versloot2025, pp. 107,122--129].

## SC046. Restoration of \emph{*a} before following back vowels (`OEARestoration`) {#rule-OEARestoration}

```foma
define OEARestoration FootCtx((
    {*æ} -> {*a} || _
        OEARestorationIntervening OEARestorationTriggerVowel
        - OEARestorationIntervening OEARestorationWeakTailVowel
));
```

The working account requires a stressed short front target and a historically back following vowel; stress on the target must not be confused with stress or subsequent changes in the following vowel. Singleton examples are strongest. Geminates include both *crabba* 'crab' and *racca* 'sailyard ring' as positives and *tæppa* 'tap' as a substantive negative. Neither a blanket geminate ban nor a special ban on *pp* is established. Evidence for *sk* and *st* does not equally license every *sC*, and the very limited *fC* evidence is specifically questioned by Hogg. A few consonant-plus-liquid forms do not establish an unrestricted extension to that class [@Campbell1959, p. 61, §§158--159; @HoggGrammar2011, pp. 93--96, §§5.35--37; @RingeTaylor2014, pp. 189--192].

The executable receives fronted \emph{*æ} from [SC043 EAFBrightening](#rule-EAFBrightening). Moving restoration before that stage makes PGmc \emph{*bákaną} 'bake' yield [bæcan]{.pred} rather than OE *bacan*, and PGmc \emph{*fáraną} 'fare' yield [færan]{.pred} rather than *faran*. This demonstrates feeding within the adopted reconstruction, not an independent refutation of blocked fronting. The later boundary with [SC048 OESecondaryNasalization](#rule-OESecondaryNasalization) also depends on exposure of the ending by [SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope). Holding that exposure constant, nasalization before restoration gives [bæcan]{.pred} and [wædan]{.pred} instead of *bacan* 'bake' and *wadan* 'wade'. Exchanging the outer operations while leaving apocope between them instead retains the back roots but yields [bacen]{.pred} and [waden]{.pred}. These are distinct computational interventions, not independent historical dating of all three processes.

The weak-noun plural must be distinguished from its nominative citation
form. A protected secondary nasal leaves \emph{*flæskōn} 'flasks'
with a back-vowel trigger, and restoration gives \emph{*flaskōn}.
The former predicted ending \emph{-en} concerned early shortening
and nasalization, not a failure of root restoration. The adopted
late shortening and lowering now give *flascan* through normal entry
from both the inherited nominative plural and dative singular. The
[weak-paradigm comparison](#weak-n-paradigms-after-apocope) separates
that ending dispute from Campbell's and Luick's analysis of singular
*flasce* 'flask' after inflected *flascan*
[@Campbell1959, p. 61, §158; @Luick1914, pp. 152--153, §161;
@RingeTaylor2014, pp. 163--164, 192].

The printed executable remains a broader proxy than the stressed-target
history. It also retracts unstressed linkers in *reġnboga* 'rainbow' and
*eorþcunde* 'earthly'. A stressed-target restriction removes both
applications: the latter still converges through ordinary syncope, but
the former develops a diphthong at [SC059 OEBackMutation](#rule-OEBackMutation)
which then escapes syncope, yielding [reġneafoga]{.pred}. This is a
disclosed interaction requiring further adjudication, not evidence that
the linker was stressed. The restriction is therefore not adopted here.
Ringe and Taylor's unstressed-vowel argument from *hegtis* 'witch'
remains relevant, with its explicitly qualified syncope history
[@RingeTaylor2014, p. 192].
