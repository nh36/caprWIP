# Flask: attested cells and the late ending route

## Identity

2026-11-14, `research/flask-inherited-paradigm`, reference
`a829dfcb4a80eac9113ac473e06258edd7285002`.
Bounded research concerning SC023, SC069, SC071 and SC100;
SC051 and production lexical selection are held fixed.

## Question

Can any securely attested Flask cell be derived from its own defensible
full Proto-Germanic input without post-Proto-Germanic analogical
substitution? In particular, can a protected secondary final nasal
allow unstressed long o to reach the existing late shortening and
final-syllable lowering route? A spelling match establishes feasibility;
independent evidence for the conditioning is required for 1B.

## Current state (before any edits)

Production selects `*fláskōn : flasce`, output `flæsċe`.
The existing attestation ledger distinguishes nominative and accusative
plurals, singular obliques, and genitive plural. Previous production
gateway rejections and identical traces will be reused, not relabelled
as new execution. Earlier scratch gateway/secondary-n protection yields
`flascen`; early shortening or early final unrounding yields `flascan`.
Neither result itself establishes its historical chronology.

## Diagnosis

The production pipeline and source are byte-identical to `1181f623`,
so its unchanged input-specific traces are reused. The older `2805d98a`
and `77f314bf` sources differ from the current source only in the dated
restoration comment, not executable lines; their dative/genitive evidence
is reused with its original provenance. New production execution covers
the previously unrun inherited accusative plural.

### Condition and predictions fixed before execution

The smallest late-route hypothesis exempts **unstressed `ō` immediately
before word-final `n`** from the early `ō > a` rule. Early shortening
before m or before nonfinal n is otherwise unchanged. The condition is
segmental/prosodic, not “nominative plural” or a lexical whitelist; after
the old n-loss has ceased, the newly final n is an application witness.
Do not delete SC069 altogether or move SC051.

The experimental gateway retains its existing class-wide coverage and
adds Ringe's inherited accusative-plural tail `ōnunz`. All ordinary
experimental runs start from normalized raw input. The production
gateway is not extended. Predictions:

1. The protected-n control reproduces `flascen/tungen`.
2. With the exemption, restoration still gives `flaskōn`; if no other
   relation intervenes, late shortening gives `flaskon`, then final
   lowering gives `flaskan`, rendered `flascan`. Record any earlier
   blocker instead of supplying a desired intermediate.
3. `*túngōniz` is a parallel positive application control, but its
   inherited-vs-levelled ending has the same historical uncertainty.
   Independent `*búrōθi` 'bears' tests the existing late mechanism,
   not the pre-n condition: it should retain `boraþ`. No independent,
   demonstrably unlevelled noun with newly final `*-ōn` has yet been
   established as a decisive positive historical witness.
4. Nominative singular `*túngōn` escapes the exemption because the
   old loss has already removed its n; `tunge` must remain. Secondary
   n in `*dōną` survives, but its stressed vowel is outside shortening.
5. Inherited `*fláskōnunz` must be run independently of replacement
   by `*fláskōniz`. A successful replacement route would presuppose
   accusative/nominative syncretism, not establish inherited accusative
   regularity.
6. Earlier accusative raising changes the relevant vowel to ū, outside
   this ō-condition. Full `*fúldōnų/*érθōnų` tests retain any current
   missing-raising problem. Separate post-raising entries before
   `OEMedLongShort` test compatibility, not complete PGmc derivations:
   `*fóldūnų`, `*éorθūnų`. Late Northumbrian final-n loss is not added.
   Dative `*túngōmaz` remains a separate pre-m problem.

### Cell audit and results

“Reject” means no output from **production `EnglishProtoInput`**, not
a phonological output. `D:` is a separately labelled diagnostic after
that rejecting gateway, never successful normal admission. The late
column uses full raw input through the scratch gateway and protected-n
ordering, with only the stated early-shortening restriction.

| Cell and existing attestation | Reconstructed full input | Production gateway/output | Late scratch result | Historical assessment |
|---|---|---|---|---|
| Nom.sg. *flasce*, Wright–Wülcker 1884 col.240.3; *flaxe*, cols.109.5, 123.21 | `*fláskōn`, CAPR's pre-old-n-loss weak citation notation | `flæsċe` | `flæsċe` | Glossary nominative-equivalents, not a new contextual nominative. Wrong root vowel. Campbell/Luick's working root-levelling account is distinct from the ending question; the unadopted retention alternative remains historically open. |
| Nom.pl. *flascan*, Hecht C p.141.27; H p.141.26 and O apparatus *flaxan* | `*fláskōniz` | Reject; D: `flæsċe` | **`flascan`** | Secure cell; whole-input phonological feasibility, but regular northern `-an` versus ending redistribution remains unresolved. |
| Acc.sg. *flascan/flaxan*, Hecht C p.66.9/H p.66.10; C/H p.141.33 | `*fláskōnų` | Reject; D: `flasconu` | `flasconu` | Does not derive the attested ending. Raising and/or paradigm redistribution must be investigated independently; this failed implementation is not proof of analogy. |
| Dat.sg. *flascan/flaxan*, Hecht C/H p.142.3, *be þære ...* | `*fláskōni` | Reject; D: `flæsċe` | **`flascan`** | Second secure matching cell in the scratch route, with the same disputed newly final `-ōn` history; not an established 1A or historically demonstrated 1B. |
| Acc.pl. *flaxan*, Goodwin 1848 ch.XV p.64.15, 24; Wright–Wülcker col.97, shoemaker's answer | **`*fláskōnunz`**, inherited | Reject; D: **`flasconun`** | **`flasconun`** | Newly executed inherited route, not a successful regular plural. Extra syllable and ending remain; no inference to categorical analogy from this alone. |
| Same attested acc.pl., alternative syncretic history | `*fláskōniz`, replacing the inherited accusative | Reject; D: `flæsċe` (identical input to nom.pl.) | `flascan`, not literal *flaxan* | Presupposes accusative/nominative syncretism. Ringe–Taylor p.63 motivates its early possibility, not its date before Proto-Germanic or an inherited `*-ōniz` accusative. Cannot count as a no-substitution derivation. |
| Gen.pl. *flascena*, Hecht C p.141.28–29; O apparatus p.141.29 *flaxena* | `*fláskōnǭ̄` | Reject | Not retested | Earlier quantity-shadow `flascona` is not a full nasal-trimoric derivation. Masculine stem influence and later vowel restoration are explicit published hypotheses (Ringe–Taylor pp.153–154); no completed regular inherited route is available. |
| Gen.sg.: **unattested on present evidence** | `*fláskōniz` | Same rejection as nom.pl. | Same `flascan` | Shared reconstructed input is not a new attestation or a licence to select this cell. |
| Dat.pl.: **unattested on present evidence** | `*fláskōmaz` | Reject; D: `flascem` | `flascem` | Separate pre-m problem, with independent attested *tungum* control; cannot infer Flask's cell from it. |

No new token is claimed. Hecht's C/H/O parallels are recensions or
apparatus readings, not independent dates for a sound change. The
genitive input retains Ringe's nasal-trimoric distinction; no invented
multi-codepoint Foma symbol or oral quantity carrier is substituted for
it in a purported normal-entry success.

### Decisive traces and controls

Full component histories and provenance are in adjacent
[`observed.json`](flask-attested-cells-evidence/observed.json).
Compact notation below suppresses only token separators.

For the nominative plural, early i-loss and z-loss give
`fláskōniz → fláskōnz → fláskōn`; old n-loss has already run
while the nasal was nonfinal. The dative singular converges at
`fláskōni → fláskōn`. In both:

- **Root:** `fláskōn → flæskōn` at `EAFBrightening`,
  then **`flaskōn`** at `OEARestoration`. No root-retention rule.
- **Control ending:** `flaskōn → flaskan`
  (`OEEarlyOShortening`) `→ flaskæn`
  (`OEUnstressedFrontingEarly`) `→ flascen` (merger/orthography).
- **Late ending:** `FLEarly` leaves `flaskōn` unchanged, as does
  early unstressed fronting; **`OELateOShortening` gives `flaskon`**,
  **`OEFinalUnstressedOLowering` gives `flaskan`**, final output
  **`flascan`**. There is no intervening blocker of this late route.

Earlier successful routes are reused, not rerun or relabelled:
early shortening gives `flaskan → flaskąn → flascan`;
early final unrounding gives `fláskān → flæskān → flaskān
→ flaskan → flascan`. The new route differs by preserving ō through
fronting, without an extra early unrounding or moving shortening
before secondary nasalization.

The inherited accusative plural instead gives
`fláskōnunz → fláskōnun → flæskōnun → flaskōnun`.
`OEMedLongShort` gives `flaskonun` before SC069. The medial vowel
then raises to u and later lowers to o; final result **`flasconun`**.
Neither exemption of `ōn#` nor protection of a secondary nasal removes
the inherited accusative's extra syllable. Supplying `*-ōniz` would
change the historical cell, not repair this derivation.

All independent/parallel controls remain explicit:

- Parallel class: protected-n *tungen* becomes *tungan*. Its
  inherited-vs-levelled ending remains the same historical question.
- Normal *tunge*, *dōn* and independent late-mechanism *boraþ*
  remain unchanged. The last proves that the existing late route
  works elsewhere, not that feminine `ōn#` historically reached it.
- Full conditional accusatives `*fúldōnų/*érθōnų` remain
  `foldonu/eorþonu`. The independently labelled raised entries
  `*fóldūnų/*éorθūnų`, before `OEMedLongShort`, likewise yield
  `foldonu/eorþonu` in **both** variants: medial shortening gives u,
  but later medial u-lowering applies while final `ų` remains.
  The new ō-condition never rewrites ū, so it does not conflict
  locally with earlier raising; these outputs nevertheless do **not**
  complete the derivation of northern *foldu/eorðu*. No late northern
  final-n deletion is silently introduced.
- *Tungem* and Flask *flascem* are unchanged pre-m failures.
  The proposed condition does not repair or worsen them.

SC051 is identical in all runs. The successful cells contain root
`a` plus `sk` before a back vowel at palatalization, so the cluster
stays **sk**, rendered **sc**, not palatal **sċ**. This fits one
possible reading of *flascan*; plain sc alone does not prove that
reading. The x-witnesses independently support a hard/metathesized
cluster, but the present run does not perform `sk > ks` or literally
derive *flaxan*. A root/ending match must not be reported as a
resolution of that separate consonantal question.

## Literature

The requested passages were read before fixing the condition above,
including the original PDF pages for Ringe's paradigm, Ringe–Taylor,
Campbell and Hogg. Locators below are printed pages.

- Ringe 2017, pp.312–313: the inherited feminine forms are
  `*tungōniz` (nom.pl./gen.sg.), `*tungōnų` (acc.sg.),
  `*tungōni` (dat.sg.), **`*tungōnunz` (acc.pl.)**,
  `*tungōnǭ̄` (gen.pl.) and `*tungōmaz` (dat.pl.).
  Flask applies those endings to the independently identified weak
  stem. These complete Flask forms are reconstructions, not quotations
  of full forms in Ringe.
- Ringe–Taylor 2014, pp.62–63: reject general early `ōn > ūn`.
  Their proposed southern change affects **newly final** `*-ōn`
  after high-vowel loss; whether northern dialects shared it is left
  open. Raising before following u is phonetically plausible, but its
  paradigm-wide explanatory basis is questioned. The inherited
  accusative plural probably merged with the nominative very early;
  even Gothic's accusative reflects the old nominative. That is a
  syncretism hypothesis, not permission to call `*-ōniz` the inherited
  accusative ending.
- Ringe–Taylor 2014, pp.163–164: scenarios (1) and (2) obtain feminine
  `-an` through masculine redistribution, differing in earlier
  masculine genitive/dative history; scenario (3) explicitly permits
  regular northern final `*-ōn > -an`, with remodelling in the other
  direction. They identify no convincing unique solution. Scenario
  (3) supplies the regular historical hypothesis tested here, not its
  internal phonetic chronology or independent proof of unlevelled
  *tungan*.
- Campbell 1959, pp.147–148, §355: retained long vowels shorten in
  early OE; §355(4) includes syllables newly final after loss of an
  original final syllable. Late shortening of o gives a too late to
  front. This establishes a mechanism and relevant prosodic
  possibility, **not an explicit statement that weak `*-ōn`
  retained ō until that shortening**. The rule's comment citations
  to §§333/369 describe fronting/merger of short a, not independent
  proof of early shortening of every remaining pre-n ō.
- Hogg 2011 [1992], pp.64–65, §3.34: posits raising before following u
  and before m; under that account feminine accusatives have raised
  ū, ordinary *tungan* involves paradigm influence, and *foldu*
  preserves a relic. The pre-m route to *tungum* is separate.
  At pp.227–228, §§6.27(3), 6.28, long vowels survive before a final
  consonant or medially and subsequently shorten; ō gives a, with
  the shortening later than i-umlaut (6.28 n.2). The explicit
  examples establish late shortening elsewhere, including class-II
  verb forms, not an independently unlevelled weak-feminine `-ōn`
  example.
- Fulk 2018, p.172, §7.33: the common account raises ō before u,
  then before tautosyllabic n in the remaining relevant cases;
  OE feminine conformity to masculine endings is proposed, with
  northern accusatives as likely relics. He points to Ringe–Taylor
  for alternatives. This is a rival ending history, not evidence for
  a categorical late unraised ō in the northern nominative plural.

The existing SC021 adjudication additionally limits the warrant for the
implemented late o split: Stausland Johnsen 2015, pp.28–31, demonstrates
the shortening/medial–final mechanism in West Saxon class-II verbs;
extension beyond that domain is explicitly future research (p.36).
Neither that article nor its current CAPR implementation supplies the
missing noun-specific historical evidence by itself.

## Historical analysis

The old final-n loss, loss of i/z exposing a secondary nasal, vowel
shortening/fronting, and possible analogical redistribution are separate
events. A failed implementation or unattested cell cannot establish
analogy. The inherited accusative plural must not be silently replaced
by the nominative plural.

The present candidate does not need a new low-vowel retention law:
ordinary root fronting followed by restoration can give root a while
ō survives in the ending. It needs input coverage, protection of a
secondary nasal against the old-loss proxy, and restricted early
shortening. Those are implementation statements. The old-n/secondary-n distinction
has independent historical support; the last change's particular
pre-n history remains to be established against the competing
raising/redistribution accounts. No chronology edge follows simply
from success in this harness.

## Verdict

**DEFER historical selection / RETAIN production; unresolved between
1B and 2.** No 1A is demonstrated for any checked securely attested
cell: production either gives the wrong form or rejects the full input.
The strongest 1B candidate is now real computationally: the full
nominative plural and dative singular both derive *flascan*, by ordinary
root restoration and existing late vowel rules, after input coverage,
secondary-n protection and a phonological restriction of early
shortening. It is not blocked by an unavoidable later relation.

The specified literature supports that historical possibility, but does
not independently establish retained ō in this ending until late
shortening. The rival raised/redistributed history also remains
compatible. Therefore neither the hypothesis alone nor this fit meets
the stated **historical** 1B adoption standard, and 2 cannot be inferred
from the other failures. Published root levelling in the singular,
possible ending levelling in the plural/obliques, accusative syncretism,
and genitive restoration must remain separate claims.

Following CAPR's explanatory priority, prefer this regular route as the
working hypothesis for further nominative-plural/dative-singular
research: it uses the existing late mechanism rather than a new ending
law or obligatory redistribution. That preference is not a claim that
the missing pre-n evidence has been found, and does not relax the
historical adoption criterion.

The distinguishing observation must concern an **i-derived newly final
nasal cell**, not just the u-derived northern accusative relics: secure
evidence that its ō remained unraised and long past early fronting would
license the late route; evidence that the same cell had already raised
to ū would rule out that route and require a later source for its a.
An early, demonstrably pre-levelling northern paradigm contrasting
nom.pl./dat.sg. -an with u-raised accusative -u would be particularly
useful; late class-uniform *tungan* alone cannot supply that chronology.
Refuting this one route would still not prove analogy in every other
Flask cell.

No machine-readable per-SC registry verdict is added: this is a bounded
unadopted cross-rule experiment, not finalization of SC069/071/100.

## Propagation (only after verdict)

Research audit, reproducible evidence and a source-ledger follow-up
only. Retain the selected nominative `*fláskōn : flasce` and its
disclosed mismatch. There is no historically established candidate to
adopt yet, so the conditional 394-row comparison is not triggered and
no corpus-invariance claim is made for this new variant. The earlier
zero-delta early-shortening/unrounding measurements remain earlier
measurements, not a substitute. Production rules, lexical selection,
registries, SC051, baselines and generated publications are unchanged.
Publication rebuild and strict validation remain deferred.

### Execution and reproduction

```sh
docker compose ps
docker compose exec -T backend sh -c 'test -d /usr/app/fsts && command -v foma && command -v flookup'
python3 Germanic/docs/sound_changes/audits/flask-attested-cells-evidence/experiment.py \
  --snapshot-id flask-cells-a829dfcb-v2
```

Use a fresh ID rather than overwriting sealed `v1`. The snapshot retains
the preregistered condition/predictions, source, pipeline, old evidence,
recipe and driver. Source SHA256:
`21f86e76dd3d7f3f76633fabd679d3fab2d40548a5b8dc84596c6760d11b52d6`;
pipeline SHA256:
`742068d0091372e72865c235b4289c430f30fab83e2d1b4a6edb040a7570fcd6`.

The isolated backend compiled 115 components, 2026-11-14
15:27:28–15:32:00 UTC, exit 0. The worker ran
15:32:00–15:32:04, exit 0. It executed 30 full normal experimental
entries, three new production normal entries (two gateway rejections),
two separately labelled post-gateway diagnostics and four post-raising
stage entries. Twelve unchanged production records were reused with
their original provenance. Genitive-plural rejection is reused from its
separate original ledger. Component hashes and full measured histories
are exported in `observed.json`. Concurrent edits during compilation
were confined to this audit; compilation consumed immutable inputs,
and worker source identity was unchanged.

Focused result checks verify the two matching Flask cells, the separate
inherited accusative failure, root restoration, both late-rule firings,
the unchanged consonant stage, positive/negative controls and every
sealed result hash. Of the 15 normal inputs in each experimental
variant, exactly three finals differ: Flask nominative plural and
dative singular `flascen → flascan`, and tongue nominative plural
`tungen → tungan`. This is a focused matrix, not a 394-row census.
Driver syntax and `git diff --check` pass. Protected source/pipeline,
vocabulary, registry and baseline paths have no diff against the
reference.

## Residue

Unraised northern `ōn#` versus raised/redistributed endings remains the
decisive historical gap. Raised accusatives still require a complete
shortening/loss history, and the x variants require their own consonant
account. Genitive singular and dative plural are unattested in the
present ledger; the earlier DOE access limits remain, not a new exhaustive
negative corpus search.
