# A and B2 integration candidate

## Source disposition

Based on `update` at `545ba40ab3fa363249562bc032f7df1c3923dc47`.
Open PR #20 (`1468c4ac0a6b4d4ca4997a28f82e88353f33c7a0`) is not
merged: its independent deer genitive plural enters as a source
migration; its paired experiments remain evidence. The combined
hedge/rest proposal (`399c50ad1dd339df4d235dda53334b39fb5fec14`)
supplies the two lexical source changes, not its generated book,
indexes, traces, or baseline fingerprints. The research head
`f95a8c13306bf74b520f7f029047380a5e78b8cc` supplies the two-model
runner, comparative evidence and historical captures. No new
historical edge is asserted.

| Identity | Previous `update` input → comparison | Active shared input → comparison | Cell / witness |
|---|---|---|---|
| 1988 deer | *déuzą → dēor* | *déuzô → dēora* | Genitive plural; Ohthere, *Orosius* I.1 §15, Bosworth p. 20 |
| 2069 hedge | *xágjaz → heġġ* | *xágjō → heġġ* | Feminine nominative singular, not masculine *hege* |
| 2138 net | *nátją → nett* | *nátjai → nette* | Dative singular, Paris Psalter 89.10 |
| 2152 rest | *rástōz → ræste* | *rástǭ → ræste* | Accusative singular, *Blickling Homilies*, Morris 101.26 |
| 2332 hue | *xíwją → hīew* | *xíwjas → hīewes* | Genitive singular, Cotton *hiewes*, Zupitza p. 30 l. 11 |
| 2340 bed | — | *bádjai → bedde* | Dative singular, Paris Psalter 40.3 |
| 2341 kin | — | *kúnjas → cynnes* | Genitive singular, West Saxon Mark 7:26 |

Deer was already migrated in the immutable research benchmark, which
is not identical to the pre-integration compatibility corpus. Hay
2061 retains the direct attested comparison in both denominators;
A has no verified protected selection and is expected to miss.
Pledge, fen and wicg stay unscored. The eight inherited discrepancies
and the explanation of ō-stem plural *-um* are not adjudicated here.

## Execution and publication

The active catalogue is the ordinary Old English selection in
`Germanic/data/germanic-aligned-final.tsv`, with common headwords and
witnesses in the normal lexical dossiers. The operation
`sc047_models.py --active --model both` runs shared definitions once
against both orders, and includes the separate hash-pinned historical
inputs. Choose `--model A` or `--model B2` to execute a single
configuration. Without `--active`, the runner reads only the
immutable 394-row archive for comparison; neither mode silently
switches downstream callers to the other chronology.

The Flask application, default bins, canonical graph, ordinary
compatibility CI and ordinary book trace generation still use the
compatibility cascade. The book describes A/B2 and indexes the
shared lexical and comparative prose. The separately generated model
reports give alternative derivations without repeating that prose.
There is no default choice of A or B2 for existing runtime consumers.

The model acceptance assertions reuse a capture instead of adding a
Foma call or live corpus sweep to pytest. The explicit active run
adds the selected inputs to the existing lookup batch at each stage,
deduplicated with diagnostics and controls. The number of compiled
components and calls is unchanged.

## Measured model results

| Comparison | A | B2 |
|---|---:|---:|
| Immutable research inputs | 382/394 | 385/394 |
| Six common selected forms | 6/6 | 6/6 |
| Active catalogue (hay included) | 387/396 | 388/396 |
| Newly admitted bed and kin | 2/2 | 2/2 |

The [full capture](captures/sc047-adoption-v1.json.gz) has 97
registered paradigm traces and 13 supplementary probes per model.
Their full results are identical to the supplemental research
capture; unscored forms have no match denominator. The original
frozen outputs are unchanged, including earlier comparisons for
hedge (both models *heġe*) and A net (*nete*), A hue (*hī*) and
A hay (*hei*). The only changed active selections relative to
the frozen research inputs are 2069, 2138, 2152 and 2332; the two
new rows are 2340 and 2341. See the migration table for the
additional deer transition relative to `update`.

| Identity | Active output → target | Scope |
|---|---|---|
| 1973 buck | *bocc → bucc* | Shared lowering |
| 2013 fire | *fȳr → fȳre* | Proposed inflected vowel transfer |
| 2030 fowl | *fogol → fugol* | Shared lowering |
| 2061 hay | *hei → hīeġ* | A only; unverified protected target |
| 2162 rust | *rost → rust* | Shared lowering |
| 2224 straw | *strēa → strēaw* | Proposed glide restoration |
| 2240 tap | *tappa → tæppa* | Proposed n-stem levelling |
| 2298 wolf | *wolf → wulf* | Shared lowering |
| 2300 wool | *woll → wull* | Shared lowering |

Re-execute with the command in [results](results.md#lexical-expansion-capture)
and add `--active`. Raw run SHA-256:
`e7dd900f8ea01e10d2d5a5d4cf03541868926754ca0f5a6939928af525badbb1`.
Corpus SHA-256:
`29f11c10e7cf8756c2708334fbd6947a4629ddcb9e69ac28bfbf9a920c5f9cf7`.
Full executable-input hashes are embedded in the capture. The
model capture alone is not an exact-commit strict certificate.
