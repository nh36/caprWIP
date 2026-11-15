# Flask nominative plural: admission and ending chronology

## Identity

2026-11-14, `research/flask-inherited-paradigm`; exact reference
`1181f62303972f9538a3a4d8d18dd63ab2f35c70`.
Bounded SC023/SC048/SC069 ending research and SC043 reader clarification,
not production adoption or a new SC051 assignment.

## Question

Can inherited `*fláskōniz` reach attested nominative plural *flascan*
through ordinary entry in a general experimental cascade? Does either
existing ending experiment explain independent cells better?

## Current state (before any edits)

The existing audit records two successful post-gateway plural routes:
shortening after restoration but before secondary nasalization, or
earlier polysyllabic final `*-ōn > *-ān`. Both move old final-n loss
before early i-apocope, so it cannot consume a secondary nasal.
The production selection remains `*fláskōn : flasce`, output *flæsċe*.

### Predictions recorded before execution

1. Admission is input coverage: native input tails omit `ōniz`; the
   fallback stem template excludes medial `ō`, and its final inventory
   cannot supply the missing whole tail. Adding the independently
   reconstructed `ōniz, ōni, ōnų, ōmaz` to an experimental input-only
   relation should admit the whole class, without selecting root vowels
   or injecting an intermediate.
2. Admission alone should still lose the plural's secondary nasal;
   moving old n-loss alone should preserve it but give *flascen/tungen*.
   The two ending experiments should instead give *flascan/tungan*,
   while nominative singular *tunge* and secondary *n* in *dōn* survive.
3. The successful plural routes should differ internally: early
   shortening feeds short-vowel nasalization; earlier unrounding carries
   long *ā* past the early short-vowel fronting. Before another vowel,
   their domains differ: shortening can affect `*-ōnų`, while the
   unrounding experiment requires final `*-ōn#`.
4. Northern accusative *foldu/eorðu* require comparison with a raising
   history, not automatic reinterpretation as nominative plurals.
   Neither experiment introduces that raising. Dative plural *tungum*
   tests a separate pre-*m* raising problem and must not be counted as
   repaired just because the nominative plural succeeds.
5. *Ascan* is a secondary class comparison, not a newly verified
   contextual nominative-plural token: the existing ashes ledger's
   clear obliques are singular. The `*áskōniz` run is conditional.

## Diagnosis

`normalize_proto("*fláskōniz")` gives `fláskōniz`; the literal
citation star is not the problem. Measured component lookups reject
`fláskōniz` and `túngōniz` in both `EnglishProtoNative` and
`PGCellRaw`. `pgrmInputTailVowel` accepts `ōn` but rejects `ōniz`;
`PGCellStem` accepts `an` but rejects `ōn`.

The scratch `FPGateway` preserves the native-first/fallback policy,
adding only the four independently reconstructed ending shapes to the
existing root templates. It is not a Flask whitelist and does not
supply a post-apocope intermediate. Every successful normal run starts
with normalized raw input and checks the gateway's tokenization.
Production admission is unchanged.

## Measured results

All columns except “production diagnostic” use full normal entry.
The production column starts **after the rejecting gateway** where
marked †; it is not normal admission. “N only” protects the secondary
nasal without changing either vowel history.

| Input / cell | Production diagnostic | Admission only | N only | Early shortening | Final unrounding |
|---|---|---|---|---|---|
| `*fláskōniz`, nom.pl. | flæsċe† | flæsċe | flascen | flascan | flascan |
| `*túngōniz`, nom.pl. | tunge† | tunge | tungen | tungan | tungan |
| `*túngōn`, nom.sg. | tunge | tunge | tunge | tunge | tunge |
| `*fláskōn`, nom.sg. | flæsċe | flæsċe | flæsċe | flæsċe | flæsċe |
| `*áskōniz`, conditional nom.pl. | æsċe† | æsċe | ascen | ascan | ascan |
| `*túngōnų`, acc.sg. | tungunu† | tungunu | tungunu | tungn | tungunu |
| `*fláskōnų`, acc.sg. | flasconu† | flasconu | flasconu | flascn | flasconu |
| `*fúldōnų`, conditional acc.sg. | foldonu† | foldonu | foldonu | foldn | foldonu |
| `*érθōnų`, conditional acc.sg. | eorþonu† | eorþonu | eorþonu | eorþn | eorþonu |
| `*túngōmaz`, dat.pl. | tungem† | tungem | tungem | tungem | tungem |
| `*dōną`, secondary-n control | dōn | dōn | dōn | dōn | dōn |

### Decisive traces

The evidence JSON retains token boundaries, unchanged named
checkpoints and every changed stage. Compact forms below omit only the
token separators, not a historical stage.

- Common plural route: `fláskōniz → fláskōnz`
  (`PWGmcEarlyIApocope`) `→ fláskōn` (`EAFFinalZDeletion`).
  Earlier `PNWGmcNStemNLoss` leaves the original full input unchanged;
  it cannot consume the later-exposed nasal.
- Shortening route: `fláskōn → flæskōn` (`EAFBrightening`)
  `→ flaskōn` (`OEARestoration`) `→ flaskan`
  (`OEEarlyOShortening`) `→ flaskąn`
  (`OESecondaryNasalization`). `OEUnstressedFrontingEarly` leaves
  `flaskąn` unchanged; `OEWeakTailReduction` gives `flaskan`;
  final rendered output is `flascan`.
- Unrounding route: `fláskōn → fláskān` (`FPUnround`)
  `→ flæskān → flaskān` (fronting, restoration).
  Both secondary nasalization and early unstressed fronting leave
  `flaskān` unchanged. `OEUnstressedLongVowelShortening` gives
  `flaskan`; final output is `flascan`.
- Accusative difference: shortening gives
  `túngōnų → túnganų → túngnų → tungn` through early shortening,
  nonhigh syncope and high-vowel apocope. Final-only unrounding does
  not apply; the unchanged downstream history gives
  `túngōnų → túngonų → túngunų → tungunu`.
- Dative in both: `túngōmaz → túngōma → túngōm → túngam
  → túngæm → tungem`. Final bare-a loss exposes `ōm`; the missing
  pre-m raising allows shortening/fronting instead of attested
  `tungum`. This is independent of secondary-n protection.
- Singular control: `túngōn → túngǭ → túngā → túngǣ
  → túngæ → tunge`. Secondary-n control:
  `dōną → dōn` at `OEHeavySyllableNasalApocope`, retained to the end.

## Literature

Ringe 2017, pp.312–313 supplies the feminine paradigm, including
`*tungōniz, *tungōnų, *tungōni, *tungōmaz`. Full Flask forms apply
that paradigm to its independently attested weak stem; they are not
quoted complete forms in Ringe. Hecht 1900, C p.141.27, predicate of
*twā ... fatu*, securely establishes nominative plural *flascan*;
C pp.66.9 and 142.3 instead establish accusative and dative singular;
C p.141.28–29 establishes genitive plural *flascena*.

Ringe–Taylor 2014, pp.163–164 contrasts *tunge : tungan : tungum*
and explicitly leaves competing raising/redistribution and regular
northern *-an* histories open. Fulk 2018, pp.88–90, §§5.5–5.6,
and p.172, §7.33, discusses raising and masculine conformity;
Hogg 2011 [1992], pp.64–65, §§3.32–3.34 and pp.298–299, §§7.98–7.100,
distinguishes the northern accusative relics and conditioned raising.
Kroonen 2013, p.159, supplies the *fuldō-* family; applying a weak
accusative ending to it is an explicit reconstruction assumption.
The *earth* stem uses the selected `*érθōn` convention, with the
same independently reconstructed weak accusative ending.

## Historical analysis

Old final-n loss predates the apocope which exposes the secondary
plural nasal; its executable identifier does not date it. The two
proposed vowel histories concern unstressed quantity, rounding and
nasal context, never grammatical membership. Neither a shared final
*-an* nor a diagnostic fit by itself establishes their ordering.
No new chronology edge is promoted.

There is a real differing prediction: the unqualified early-shortening
move feeds accusative syncope, whereas final `*-ōn#` unrounding does
not. That favours the latter as the less disruptive experiment, not as
a proven sound law. Independent evidence requires an earlier raising
route in the accusative: Hogg §3.34 gives
`*tungōnu > *tungūnu > *tungu(n)`; Fulk §7.33 connects the raised
feminine endings with following u and discusses northern conformity
to the masculine. Raising before shortening could change the test,
so `tungn` does not disprove every possible early-shortening chronology.
Neither current experiment implements that independent raising.

The Northumbrian accusative relics *foldu* (CædH9) and *eorðu*
(LRid11) belong to Hogg's separate, late Northumbrian final-n loss.
They constrain raising before that loss, not the relative order of
plural shortening and secondary nasalization. The same texts retain n
elsewhere, and Hogg notes possible nasalization/orthographic ambiguity.
The scratch non-Northumbrian cascade must not acquire a final-n deletion
just to reproduce those surface spellings. Its conditional full inputs
give `foldn/eorþn` under shortening and `foldonu/eorþonu` under
unrounding; the latter also expose later u-lowering, not a completed
northern raising history.

Ringe–Taylor p.164 expressly permits either raising plus masculine
redistribution, or regular northern `-an` plus feminine redistribution.
Hogg's ordinary *tungan* likewise invokes paradigm influence.
These are attributed morphological explanations, not new grammatical
conditions in the experiment. *Tungum* independently requires pre-m
raising; neither candidate accounts for it. No inspected source
independently dates the two competing plural vowel mechanisms against
each other.

## Verdict

Normal admission is resolved **experimentally**: both whole inherited
plural inputs now succeed, without a transponent. Historical selection
is not resolved. Retain `*fláskōn : flasce` and its disclosed
`flæsċe` mismatch; do not switch to the plural yet. Final unrounding
is a better-contained candidate for further ending research, but neither
route meets the requirement of an independently supported complete
history. CAPR declines to adopt root retention while leaving the
historical possibility open. SC051 is unchanged.

## Propagation (only after verdict)

The supplied discussion follows the first-fronting→restoration link
in SC043. Chapter 3 and the Flask entry cross-reference that decision
and distinguish experimental admission from historical validation.
The *ræste* counterexample is qualified by its selected reconstruction
and Wright §56's i-umlaut treatment. The supplied Hogg reference is
corrected to `HoggGrammar2011`, pp.93–96, §§5.35–5.38: those are
the monograph's sections, not the differently numbered
`HoggPhonology1992` Cambridge History chapter. Existing discussion and
dated earlier experiment measurements are preserved.

### Reproduction and execution identity

From the repository root, with the existing backend healthy:

```sh
python3 Germanic/docs/sound_changes/audits/flask-nominative-plural-evidence/experiment.py \
  --snapshot-id flask-nompl-1181f623-v2
```

Use a fresh snapshot ID; do not overwrite sealed `v1`. The recipe fixes
production source and pipeline to the exact reference SHA above,
asserts equality to the checkout, and changes only experimental
admission and the stated component orders. Source, recipe, driver,
pipeline, preregistered predictions, receipts and full traces are sealed
under `.capr-work/experiments/flask-nompl-1181f623-v1/`.
Portable evidence is adjacent
[`observed.json`](flask-nominative-plural-evidence/observed.json);
it includes all orders and the 120 component binary hashes.

Backend compile: 2026-11-14 14:46:59–14:52:38 UTC, exit 0.
Probe worker: 14:52:38–14:52:44 UTC, exit 0.
There are 55 normal-entry attempts: 47 accepted, eight production
gateway rejections; the eight separately labelled post-gateway
diagnostics also complete uniquely. The compiler receipt notices
concurrent reader-prose edits; its source and recipe were immutable
snapshot inputs, not those documents. The worker identity is unchanged.
The original wrapper failed only when printing a log after sealing had
moved it from staging to results; computation, sealing and evidence
export had already succeeded. The reporter now reads the sealed path;
no second runtime build was needed.

Focused source checks:

```sh
python3 -m pytest -q Germanic/tests/test_reader_architecture.py \
  -k 'each_source_has_only_its_registered_identity_and_one_primary_heading or rule_links_in_both_entries_and_shared_context_reach_unique_destinations or individual_sources_are_nested_below_real_chapters_without_changing_code'
```

Three passed, 30 deselected. In-memory reader rendering confirms the
requested insertion point and unique rule/Chapter 3 destinations.
Existing reconstruction-span, duplicate-gloss and predicted-form helpers,
Pandoc parsing and bibliography-key checks pass on the three edited
reader/model sources. The paragraph-gloss validator passes both reader
sources. In the proper Part II lexical fixture it reports six findings
identical to `1181f623` (*hæfdon, behydde, flaxan, flascones, flasċe,
flaxe*); no new lexical finding is introduced. Those existing findings
are not repaired by rewording mature prose. Driver and worker syntax,
sealed log relocation and the exported admission/control results were
also checked. No new 394-row comparison, full suite or publication
rebuild is claimed.

## Residue

Independent dating of the secondary-nasal plural vowel, the conditioned
raising routes, and their interaction with syncope remain open.
Production rules, selected vocabulary, frozen baselines and generated
publication files are unchanged.
