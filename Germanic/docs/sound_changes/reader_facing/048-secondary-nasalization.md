# Coda nasalization and the final-n proxy

## Historical conditioning and paradigms

Unstressed short \emph{a} remained back before a nasal in the same
syllable, while a nasal belonging to the next syllable did not prevent
fronting. Ringe and Taylor give
\emph{*bindaną > *bindan > *bindąn} for *bindan* 'bind', but also
\emph{*bindandī > *bindąndī > *bindændi} for *bindende* 'binding'.
The latter contains an internal coda: subsequent i-mutation changes
its nasal low vowel. Final n alone is therefore too narrow as a statement
of the historical phenomenon
[@RingeTaylor2014, pp. 152--154, §5.1.2;
@HoggGrammar2011, pp. 214--217, §§6.1--6.6;
@Campbell1959, pp. 140--141, §§333--334].

The paradigm of *guma* 'man' supplies independent evidence, but not
uniformly inherited \emph{-an} in every cell. Ringe and Taylor take
accusative singular and nominative plural as regular donors for extension
to other cases. Fulk instead reconstructs an older accusative with
\emph{-un}, citing Northumbrian *galgu* 'gallows' on the Ruthwell Cross,
and derives the general \emph{-an} from other cells. The genitive and
dative singulars and the complex history of *gumena* 'of men' must
therefore be kept distinct from regular nasalization
[@RingeTaylor2014, pp. 153--154; @Fulk2018, pp. 168--171, §§7.30--7.31].
Likewise, inflected participial forms supply the proposed source of
\emph{-en} in endingless participles; this is a paradigmatic argument,
not grammatical conditioning of fronting
[@RingeTaylor2014, p. 152; @Campbell1959, pp. 140--141, §§333--334].

## SC048. Unstressed nasalization before final n (`OESecondaryNasalization`) {#rule-OESecondaryNasalization}

```foma
define OESecondaryNasalization [Ctx([
    {*a} -> {*ą} || _ {*n} .#.
])] .o. [Ctx([
    {*à} -> {*ą} || _ {*n} .#.
])];
```

The retained relation is an explicit final-n proxy. Its selected
applications affect short unaccented a exposed by
[SC047 OEHeavySyllableNasalApocope](#rule-OEHeavySyllableNasalApocope);
the secondary-stress companion is separately represented. Long \emph{ā}
and accented \emph{á} are not targets; decoded unmarked vowels still
require an independently justified stress history. The spelling evidence
alone does not prove a nasal intermediate: Faulkner's 19,315 infinitives
are written with \emph{-an} 96.1% of the time, including manuscripts
whose conservative spellings cannot directly date the phonetic reduction
[@Faulkner2020, pp. 3--7].

The broad predicted \emph{-en} failure set when this proxy precedes
apocope establishes a computational exposure dependency. The position
of [SC046 OEARestoration](#rule-OEARestoration) matters separately:
when apocope precedes both operations, premature nasalization can remove
the encoded restoration trigger and give predicted \emph{*bæcan}.
Neither comparison independently dates all historical coda nasalization.

Back mutation requires a dialect-specific qualification. West Saxon
\emph{e} is regularly mutated by following \emph{u}, not by the
\emph{a} of the infinitive; Mercian *weofan* 'weave' is not the West
Saxon *wefan*. The previous parallel clauses of
[SC059 OEBackMutation](#rule-OEBackMutation) nevertheless admitted an
a-trigger for e, so delaying nasalization yielded predicted
\emph{*steolan} and \emph{*weofan} computationally. The adopted,
separately composed clauses enforce the stated West Saxon trigger and
remove both differences. The old examples remain observations about
that previous implementation, not independent
historical proof of nasalization before West Saxon back mutation
[@RingeTaylor2014, pp. 319--327, especially p. 325;
@HoggGrammar2011, pp. 149--157, §§5.103--5.106;
@Campbell1959, pp. 85--86, §§205--206].

The [weak-paradigm comparison](#weak-n-paradigms-after-apocope) exposes
the distinction between the adopted and earlier experimental histories.
Long \emph{*ō} in a protected plural \emph{*flaskōn} 'flasks' is not
a target of this short-a rule. In the former unrestricted sequence,
shortening created a too late for nasalization, so unstressed fronting
yielded predicted \emph{*flascen}. Experimental shortening after
restoration but before nasalization instead gives \emph{*flaskąn} and
*flascan*. Neither that experiment nor its output establishes an
independent historical edge. In the adopted history long ō survives
both nasalization and unstressed fronting; later shortening and lowering
give *flascan* without changing this rule
[@RingeTaylor2014, pp. 163--164;
@Fulk2018, pp. 90, 171--172, §§5.6, 7.32--7.33].

Wider early coda nasalization can preserve the selected endpoints when
its i-mutation consumer and nasal restoration trigger are also represented.
Directly blocking fronting before coda nasals can preserve them without
a nasal intermediate under the corrected West Saxon back-mutation condition.
The retained final-n proxy does not choose between otherwise equivalent
observations or claim to implement every reconstructed paradigm cell.

Staged \emph{*bindandī} makes the missing domain visible without
treating a West Germanic participle as a Proto-Germanic input. The
final-n proxy leaves its internal vowel oral, yet ordinary i-mutation
still gives *bindende*. Wider early nasalization instead gives
\emph{*bindąndī}; without a corresponding nasal-vowel i-mutation
consumer it incorrectly preserves \emph{*bindande}. Adding that
consumer recovers the front vowel and *bindende*. The intermediate
nasality is thus a prediction of the wider account, not something
proved by their common spelling. An onset-nasal negative and paired
short/long and accented controls keep these mechanisms separate
[@RingeTaylor2014, p. 153].

The weak-noun tests remain incomplete. Ringe and Taylor's reconstructed
accusative \emph{*gumanų} needs early loss of its final high vowel;
leaving it until quantitative high-vowel deletion lets intervening
syncope give predicted \emph{*gumn}. The alternative accusative based
on Fulk's \emph{-on-um} reaches *guman* in the present cascade, but
without his preceding \emph{-un-} stage: late o-lowering supplies the
same spelling by a different route. The regular nominative plural
supplies *guman*, whereas unrelevelled genitive and dative inputs give
predicted \emph{*gymen}. Those recipient cells require the source's
independently argued paradigm extension, not a grammatical condition
on the sound law
[@RingeTaylor2014, pp. 153--154; @Fulk2018, pp. 169--171, §7.31].

The wider and direct accounts agree on the selected corpus, these
accusative and recipient-cell endpoints, and ordinary-vowel onset
endpoints, but are not identical transducers. A constructed
protected-tail carrier distinguishes their encoded vowel classes.
It is not a literal reconstruction of the genitive-plural ending.
With ordinary long-vowel genitive-plural stages both give predicted
\emph{*gumne}, not *gumena*: syncope and the source's subsequent
paradigm restoration and dissimilation have not all been modelled.
Neither that artificial carrier nor a correct aggregate score settles
the historical nasal intermediate
[@RingeTaylor2014, pp. 153--154].
