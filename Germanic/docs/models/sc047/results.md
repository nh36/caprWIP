# A and B2: corpus audit and open work

This page records the pre-adoption research comparisons. The
[integration candidate](adoption.md) uses common selected cells and
includes hay in both active denominators.

## What the comparison measures

Both models start from exactly the same frozen 394 inputs as the
canonical reference (386 matches). The frozen runs compare the
phonologies; the selections compare each model's derivation against
its own target. In A, hay remains an unresolved comparison, not
a selected protected form. It accounts for the difference between
393 selected cells and 394 diagnostic rows.

| Model | Frozen matches | Selected matches | Unresolved selection |
|---|---:|---:|---|
| A | 382/394 | 385/393 | Hay, row 2061 |
| B2 | 385/394 | 386/394 | None added |

The frozen B2 endpoints differ from canonical only for hedge. Frozen
A differs from canonical on hedge and the three rows below. Compared
with each other, A and B2 differ on only three frozen rows:

| Frozen input | Inherited A | Inherited B2 | Selected A | Selected B2 |
|---|---|---|---|---|
| *nátją* (2138, net) | *nete* | *nett* | *nátjai* → *nette*, dat.sg. | *nátją* → *nett*, acc.sg. |
| *xáwją* (2061, hay) | *hei* | *hīeġ* | Unresolved | *xáwją* → *hīeġ*, acc.sg. |
| *xíwją* (2332, hue) | *hī* | *hīew* | *xíwjas* → *hīewes*, gen.sg. | *xíwją* → *hīew*, nom.sg. |

The common lexical changes are *xágjō* → *heġġ* (feminine nominative,
2069) and *rástǭ* → *ræste* (accusative, 2152). The frozen *xágjaz*
regularly gives masculine *heġe* in both models; it is not the feminine
formation. *Rástōz* and *rástǭ* yield the same result in the active
models, but *þā ēcean ræste* is syntactically accusative. The inputs
and source justifications come from the unmerged hedge/rest proposal.
The other 389 rows retain the frozen selections in both editions;
381 of those match. This is a computational assessment of every
row, not 389 new manuscript or stem-class adjudications. The inventory
includes existing publication classifications and input decisions
where available, including inputs already chosen to reflect a later
stage or a different cell.

The A genitive is the Cotton reading *hwites hiewes* (Sweet,
pp. 86–87, l. 20); Hatton reads *hiwes*. B2's direct witness is
*þæt æðeleste hiew* in the question with resumptive subject *hit*
(Sweet p. 133, l. 11). No nominative *hīew* is derived by
selecting *hiewes*. For ‘net’, Lindisfarne *net* (Luke 5:6) and
*nett* (John 21:6) identify direct cases, not a surviving *nete*;
the Paris Psalter’s dative *nette* (89.10) is A's separate target.

## Shared phonology and controls

The split between the light neuters begins before gemination: A has
already lost final *ą* and vocalized singleton *j*, whereas B2
geminates with *ą* present. The models share the subsequent handling
of stranded geminated *wwj*. A's early ‘hay’ route reaches *hæwi*
before mutation and *w*-loss and ends at reconstructed *hei*, not
attested *heig*. A's early ‘hue’ reaches *hiwi* before *w*-loss,
then resolves final *i.i* to *hī*. B2 retains conditioning from *wwj*
for both *awj* and *iwj*. The protected cells agree, ‘new’ keeps its
oral singleton in both models, and consonantal *stráwjaną* and Fulk's
*stráujaną* both yield *strīeġan*, so this endpoint does not adjudicate
the inherited structure. Direct ‘glee’ gives *glī* in A and *glīew*
in B2, but its attested variants do not settle the donor or dialect.

Both models restore raising before final *z*-loss. Bimoric *rástōz*
retains *ō* through the raising slot, then loses *z* and undergoes
unrounding and fronting to give *ræste*. The genuine dative *rástōi*
instead reaches *rastē* through contraction. Independent controls:

| Noun | Bimoric genitive | Trimoric genitive alternative | Proto-Germanic dative |
|---|---|---|---|
| Rest | *ræste* | *rasta* | *ræste* |
| Gift (*gebō*) | *ġiefe* | *ġiefa* | *ġiefe* |
| Wool | *wolle* | *wolla* | *wolle* |
| Love | *lofe* | *lofa* | *lofe* |

The trimoric result also belongs to the homophonous inherited
nominative plural in Ringe–Taylor's reconstruction. This is a
phonological prediction, not evidence for applying the nominative
plural's reconstruction to the genitive. The gate parses *sáiwalōi*
as bimoric *ō* plus *i*, which contracts; *sáiwalôi* remains separately
parsed and does not undergo contraction.

Revision 2 admits independently reconstructed instrumental *-ōmiz*
(Ringe 2017, p. 312) through the same productive root grammar as
*-ōi*. Both plural routes converge at *-ōm*, but `OEEarlyOShortening`
gives *-am* and subsequent unstressed fronting and merger give *-em*.
Thus rest, gift, wool and love give *rastem, ġiefem, wollem, lofem*
in both plural probes. Ringe–Taylor (pp. 57–58, 115) support the
early loss of *i* after this sequence and the historical dative–
instrumental merger, but the merger need not have been purely
phonological. These model outputs do not account for the usual
Old English dative plural *-um*. Do not promote the outputs to attested
targets or add a special rule for ō-stems. Extension of *-um*
from other declensions is plausible but unproved. Conditional ‘youth’
nominative and dative probes are the only two remaining gate rejections
among 97 probes per model; the disputed inherited class (and lost
*Maldon* manuscript) prevents treating either as a negative sound-law
result.

All 40 canonical u-lowering firing identities are preserved. The
door probe enters SC112 as *dorą*, so that lengthening does not
apply and *dor* survives. There and where still fire at SC112 and
yield *þǣr* and *hwǣr*. Both models give heavy oral *ende*. Both
derive *saru* and *searwes*, isolating the proposed transfer of the
oblique vowel rather than a geminate. For ‘bed’, ‘pledge’ and ‘kin’,
A gives *bede*, *wede*, *cyne* and B2 gives *bedd*, *wedd*, *cyn*
(with final nasal simplification); both give protected *bedde*,
*wedde*, *cynne* and *beddes*, *weddes*, *cynnes*. These words are
probes, not additions to the 394. Bed and kin now have separate
proposed selections; pledge does not.

## Lexical expansion capture

[`sc047-lexical-expansion-v1.json.gz`](captures/sc047-lexical-expansion-v1.json.gz)
re-executes active runner `sc047-active-v2` with the following inputs
from the Germanic backend:

```sh
docker compose exec -T backend python3 /usr/app/tools/sc047_models.py \
  --form sáiwalōi --form sáiwalôi --form bádjamiz \
  --form fánją --form fánjai --form fánjas --form fánjō \
  --form wígjaz --form wígją --form wígjai --form wígjas --form wígjô \
  --form bázjas
```

The run began at source `2a14a1cfa8ab53004b0b5f9667ae8651575ec0a5`
and exited 0 in 5m58s. Publication-only commits and test/document
edits occurred during the run; the executable input hashes, both
orders, all 394 corpus records and all 97 paradigm traces per model
are identical to active v2. The 11 added queries are not scored.
Raw stdout SHA-256:
`9fe0dfc95d2e078f2921f50a101ed7c92ffe50daccdbb61d4415d4315eacef9c`;
gzip SHA-256:
`89a4fdd6459665212ffaa5669520d1d180a1214844745df358d777bdc051b2e4`.
The archive embeds the exact FST, runner, plan, inventory and corpus
hashes. This is fresh research execution, not a clean exact-commit
strict production certificate. Earlier captures are unchanged.

## Unmatched rows and next decisions

Both models inherit the following eight discrepancies unchanged.
These are diagnoses to investigate, not new source verdicts.

| Rows | Regular output versus target | Open issue |
|---|---|---|
| 1973 buck; 2030 fowl; 2162 rust; 2298 wolf; 2300 wool | *bocc* / *bucc*; *fogol* / *fugol*; *rost* / *rust*; *wolf* / *wulf*; *woll* / *wull* | Shared lowering domain and attested retention, not SC047 |
| 2013 fire | *fȳr* / *fȳre* | Proposed transfer of inflected *-e* |
| 2224 straw | *strēa* / *strēaw* | Proposed restoration of *w*; compare the SC034 analysis |
| 2240 tap | *tappa* / *tæppa* | Reconstructed n-stem levelling |
| 2061 hay, A only | *hei* / *hīeġ* | Regular inherited singleton versus attested stem; no verified protected target |

The next lexical dependency is a securely case-identified hay
witness with the predicted protected shape. An independently inherited
English singleton with a vowel, or a case-localized early double,
would have greater chronological force than a higher selected-form
score. The source and conditioning of the downstream labial reflexes
remain open. The shared unstressed plural endings and inherited
lowering problems are separate questions, not blockers for these
lexical proposals. Neither
the ordinary selected outputs nor the use of Cotton *hiewes* dates
paradigm transfer. Masculine ‘retainer’ and ‘hill’ retain the
unselected accusative contrasts; the source basis for the hypothetical
donor in ‘hill’ is weaker than the evidence for the doubled dative.

## Frozen run evidence

| Capture | Executed runner and cell source | Uncompressed output SHA-256 |
|---|---|---|
| [Revision 1](captures/sc047-active-v1.json.gz) | `4aa8becbe541366dd6c827651f2ddfda35383d4f` | `3486208f26770adeb847f28a4fdcc0e4a365c8ee67af72c242140b4ecd9b0bc7` |
| [Revision 2](captures/sc047-active-v2.json.gz) | `86b1a8b5f7338f0221160b9ec75651b2d631023b` | `8744e7ae1d9baa8d6a21a6ae0c401a32abf88842f27d3aaec3a11ec013dc962e` |

Both exited successfully in the backend with the two *sāwol* controls.
Their 394 row results, including every selected and diagnostic trace,
are identical. The captures bind the input, recipe and runner digests;
publication edits were made during the runs, so these are not
clean-worktree production strict-validation certificates.
