# Barrack 1975 and CAPR on vowel loss and the consonant-cluster system

Comparative historical research dossier for the late syncope and
consonant-cluster corridor (CAPR SC063–SC068, SC079–SC080; Barrack's
vowel-deletion rules 204, 345–359, 388–390 and cluster rules 476–484).
Prepared with the SC065 adjudication (2026-10; see
`../../audits/sc065-adjudication.md`). Pages are printed folios of
Barrack 1975, verified against the original in `rule_census.tsv`.

## 1. The two architectures

Barrack and CAPR agree on the gross historical shape: Old English
unstressed-vowel loss precedes and feeds the late consonant-cluster
developments. They differ on how that territory is carved into rules.

Barrack distributes vowel deletion across several ordered rules: an early
West-Saxon *i-syncope at 204 (p. 63); the main post-heavy-syllable
final high-vowel deletion at 345 (pp. 85–86); two further deletion rules
at 347 (pp. 86–87) and 351 (p. 87), the second with his prosodic "PES"
conditioning; syncope of originally long vowels at 358 (pp. 90–91) and a
general unstressed-vowel deletion at 359 (p. 91); and residual medial
losses at 388 and 390 (p. 96), the latter citing *meolc* 'milk'. His
deletions are conditioned prosodically and segmentally but are not
restricted to a pre-dental environment anywhere.

CAPR splits the same territory differently: final high-vowel apocope is
SC063 (`OEHighVowelApocope`); medial pre-dental syncope after heavy
syllables is SC065 (`OEMedialSyncope`); l-adjacent syncope is SC066
(`OELAdjacentSyncope`). SC065's pre-dental enumeration is an executable
proxy, adjudicated 2026-10 as RETAIN: at its post-apocope cascade site
the handbooks' open-syllable condition is unstatable, and the controlled
counterfactuals show every tested Barrack-style broadening corrupts a
selected output (u-extension: *hēafod* → hēafd; any-consonant: *hærfest*,
*sċilling* rejected; pre-apocope open-syllable law: *sāwol* → sāwl).

## 2. Barrack's explicit feeding claims

Barrack's ordering apparatus makes the syncope-feeds-cluster relationship
explicit, rule by rule (ordering claims verified in `rule_census.tsv`):

- 351 > 480.1 (p. 124): syncope feeds the devoicing of *d* to *t* after
  a voiceless consonant (the *cyste* type).
- 347 > 480.2 > 481.1 > 476: syncope feeds voicing assimilation, then
  devoicing/fortition (*findip* > WS *fint*, pp. 124–125), then cluster
  simplification (p. 122).
- 351 > 481.7 (p. 125): syncope feeds gemination.
- 459.1 > 476: r-metathesis precedes cluster simplification
  (*pridda/pirda*, p. 122).
- 476 after 481.2, 358, 351: cluster simplification is the terminal
  consumer of several deletion rules.

The historical content of these claims is the standard one: the clusters
that assimilate, devoice, degeminate and simplify in late Old English are
largely clusters that syncope created. CAPR encodes the same dependency
positionally: SC065 (order 74) and SC066 (75) immediately precede SC067
`OEDentalAssimilation` (76) and SC068 `OEPreconsonantalDegemination` (77),
and the corpus witnesses the feeding directly in *spindle*, where SC066's
syncope creates the cluster that SC068 degeminates.

## 3. Where the accounts genuinely differ

1. Conditioning of medial syncope. Barrack's deletions are broader;
   CAPR's SC065 is deliberately narrower. The SC065 counterfactuals show
   that at CAPR's cascade site the broader statements are not innocent:
   they corrupt independently selected outputs. This is an argument about
   executable architecture, not a refutation of Barrack's history: his
   broader rules live at different points of his own ordering, with his
   own prosodic conditions.
2. The dental-assimilation territory. Barrack derives WS *fint* through
   an explicit chain 347 > 480.2 > 481.1 (pp. 124–125). CAPR's SC067
   currently fires on zero selected rows because the corpus contains no
   syncopated verb inflection of this type; Barrack here anticipates
   exactly the witness class (2/3 sg. present forms) that SC067 needs.
3. Degemination and geminate simplification. Barrack handles these
   inside 476 (p. 122: *sellic*, *wiersa*, *cyng*) and 481.7 (p. 125),
   again fed by syncope; CAPR splits preconsonantal degemination (SC068)
   from final geminate simplification (SC080, witnessed by *lung*), with
   457b (p. 115) and 286 (p. 71) as further partial parallels.
4. Rhotacism-fed inputs. An *r* that conditions or participates in late
   clusters may arise by rhotacism (CAPR SC003); neither architecture
   restricts cluster rules to original *r*, and regression tests should
   not either.

## 4. Byforms and transmission

The corridor's attested byforms (e.g. *gærs* beside *græs* from the SC087
round; Barrack's own EWS *biernan–birnan* beside WS *byrnan* under 459.1,
pp. 115–117) are not evidence for optional rules. Within the project's
working principle — regular change is exceptionless within its properly
specified phonological, chronological and dialectal domain — they index
distinct dialect histories, interdialectal borrowing, or transmission of
chronologically distinct forms. The reader-facing chapters document such
byforms without modelling each one.

## 5. Comparative section for later book incorporation

> Barrack's 1975 cascade and the present one agree that the late Old
> English consonant-cluster developments are, to a first approximation,
> consumers of syncope. In his ordering, the vowel-deletion rules 345,
> 347 and 351 [@Barrack1975, pp. 85--87] feed voicing assimilation and
> fortition at 480.2 and 481.1, which derive West Saxon \emph{fint}
> 'finds' from \emph{*findip} [@Barrack1975, pp. 124--125], the coronal
> fricative-to-stop assimilation at
> 481.7 [@Barrack1975, p. 125], and the terminal cluster simplification
> at 476, which he also orders after r-metathesis on the strength of
> \emph{þridda} beside \emph{þirda} [@Barrack1975, p. 122]. The present
> cascade encodes the same dependency positionally: medial syncope
> (SC065, `OEMedialSyncope`) and l-adjacent syncope (SC066,
> `OELAdjacentSyncope`) immediately precede dental assimilation (SC067,
> `OEDentalAssimilation`) and preconsonantal degemination (SC068,
> `OEPreconsonantalDegemination`), and the corpus witnesses the feeding
> in \emph{spindel} 'spindle', where syncope creates the geminate-plus-
> consonant cluster that degemination then reduces. The substantive
> difference lies in the statement of syncope itself. Barrack's
> deletions are prosodically conditioned but segmentally broad; the
> present medial syncope is restricted to pre-dental position, a
> deliberately narrow executable statement whose counterfactual
> broadenings — toward Barrack's generality — demonstrably corrupt
> \emph{hēafod} 'head', \emph{hærfest} 'harvest' and \emph{sċilling}
> 'shilling' at this point in the cascade. Barrack's chain for
> \emph{fint} also identifies precisely the lexical class, syncopated
> verb inflection, that the present corpus still lacks and that any
> future adjudication of the dental-assimilation rule will need.

## 6. Status

Dispositions for every Barrack heading named above are recorded in
`barrack_to_capr.tsv`; the ranked adjudication agenda for the remaining
corridor rules is in `cluster_adjudication_queue.md`.

### SC066/SC068 adjudication outcome (2026-10-30)

The joint SC066–SC068 round is complete: SC066=REFORMULATE (weight and
open-syllable conditioning adopted; `{*ie}` reclassified as a short
diphthong; zero corpus delta), SC068=RETAIN. Print verification
corrected five census glosses (286 is vowel shortening before
geminates, not cluster simplification; 351 is MEDIAL deletion with a
WS generalization to light syllables; 453 is gemination before
liquids, not epenthesis; 481.7 is coronal fricative-to-stop
assimilation, not gemination; 388's WS variant drops the
following-vowel term). Barrack's West Saxon environment
simplifications under 351/388 and his post-liquid deletion 390 were
tested against the selected corpus and rejected: the first pair
predicts syncope in the *cetel*-type nominative, the last corrupts the
selected *meoloc* row. His 476 ordering of cluster simplification
after syncope independently corroborates CAPR's SC066 < SC068
relation. See `../../audits/sc066-adjudication.md` and
`../../audits/sc068-adjudication.md`.
