# Cluster adjudication queue (post-SC065)

Ranked agenda for the remaining syncope/cluster-corridor adjudications,
prepared at the close of the SC065 round (2026-10). Evidence counts are
from the live rule-coverage census
(`../../cascade_baseline/rule_coverage_census.tsv`); Barrack pages are
printed folios verified in `rule_census.tsv`. **Nothing below is
adjudicated; this file schedules work, it does not decide it.**

Ranking principle: adjudicate first where positive lexical witnesses and
interactions already exist (cheap, high-yield), and where a zero-firing
rule parallels the SC065 situation (either a coverage gap to fill or a
rule to retire); defer rules whose evidence requires new corpus classes.

## 1. SC066 + SC068 — l-adjacent syncope and preconsonantal degemination (joint round)

- Historical problem: l-adjacent syncope after light syllables (R/T
  §6.7.4) and the degemination of the clusters it creates; the two rules
  share the witness *spindle* (SC066 feeds SC068), so they should be
  adjudicated together.
- Census: SC066 fires on nettle, spindle, thistle; SC068 on bottom,
  spindle.
- Barrack: 388, 390 (p. 96, incl. *meolc*); 351 (p. 87); 481.7
  gemination (p. 125); 476 (p. 122, *sellic*, *wiersa*); 453
  (pp. 114–115); 286 (p. 71).
- Known tension to resolve: the germanic.txt SC066 comment calls the
  rule "lexically variable (cetel 'kettle' does NOT syncopate)", which
  conflicts with the project's exceptionless-law principle. The
  adjudication must either find the regular conditioning that separates
  *cetel* from *netle/þistel/spindel* (weight, cluster shape,
  left-vs-right adjacency to *l*) or restate the rule's domain; it must
  not keep "lexically variable" as a mechanism.
- Experiments: counterfactual broadenings/narrowings of the l-condition
  over the full corpus; SC066×SC068 order permutation (spindle is the
  discriminating witness); negative controls nettle (no degemination
  context) and bottom (degemination without l-syncope feeding).
- Readiness: READY — witnesses and harness pattern exist; main work is
  the cetel conditioning question in the handbooks (Campbell §§388–393,
  R/T §6.7.4, Hogg).

## 2. SC067 — dental assimilation (zero-firing)

- Historical problem: assimilation in dental clusters created by
  syncope (WS *fint* < *findiþ*, *cyst* < *cysseþ*-type, *cȳdde* <
  *cȳþde*). Currently fires on zero selected rows — the same situation
  SC065 was in before this round.
- Barrack anticipates the witness class exactly: 480.2 and 481.1
  (pp. 124–125) derive WS *fint* via 347 > 480.2 > 481.1 > 476; also
  480.1 (p. 124, *cyste*-type d > t), 481.2 (p. 125), 422 (p. 108).
- Lexical gap: the corpus contains no syncopated 2/3 sg. present verb
  forms or dental preterites. A SC065-style admission (one
  independently reconstructable witness, e.g. the 3 sg. of a Class 1
  weak verb with dental-final root, or a *cȳþde > cȳdde* preterite)
  is the obvious route, but verb inflection is a larger selected-cell
  policy question than the *-iþō nominals were.
- Experiments: retire-vs-retain counterfactual (expect zero corpus
  delta pre-admission); witness probes for fint/cȳdde/cyste families.
- Readiness: NEEDS SOURCE WORK first — establish the paradigm-cell
  policy for syncopated verb forms before admission; then READY.

## 3. SC080 — final geminate simplification (single witness)

- Historical problem: degemination in final position; census shows one
  firing (lung). One witness is thin for a confident retention.
- Barrack: 476 (p. 122, *cyng*), 457b (p. 115), 286 (p. 71).
- Work: out-of-sample probes (*mann/man*, *eall/eal*, *bedd/bed*
  families) and a near-miss census as in SC065; check interaction with
  SC068 (preconsonantal vs final domains disjoint?).
- Readiness: READY for a small round; likely RETAIN with witness
  documentation.

## 4. SC079 — j-loss after heavy syllables (healthy, low priority)

- Census: 29 firings (believe, hedge, net, set, sit, will, hue …) —
  well-witnessed and uncontroversial.
- Barrack: 266b (p. 69), 398.4b (pp. 99–100), 470 (p. 121).
- Work: routine adjudication (conditioning after light syllables,
  relation to gemination/palatalization) — no urgency; note the
  strength/length palatal-ġ issue from the SC065 round touches the
  palatalization complex that SC079 borders.
- Readiness: READY but low value relative to cost; schedule after 1–3.

## 5. Deferred: late cluster complex at large (SC087 follow-on)

- The broader late consonant-cluster investigation (Barrack 459.1/476
  interactions, *þridda/þirda*, cress residue from the SC087 round) is
  reserved for the separately announced, more capable round. Do not
  fold it into items 1–4.

## Cross-cutting observations

- Rhotacism (SC003) can create the *r* in late clusters; cluster-rule
  regression tests must census all rows, not rows whose protoform
  contains *r* (lesson applied in `test_sc065_adjudication.py`).
- The SC065 round's receipt shows the open-syllable weight law is only
  statable pre-apocope and then corrupts *sāwol*: any future corridor
  reformulation that revives the handbook law must solve the
  hēafudu-type medial-*u* problem first (Goering 2023).
