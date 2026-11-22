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
adds one selected-row lookup batch per stage, deduplicated with the
same diagnostics and controls; it does not increase the model
orders or compiled component count.
