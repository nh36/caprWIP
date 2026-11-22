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

Build the application binaries in the backend with
`docker compose exec -T backend python3 tools/build_germanic_models.py`.
It builds both models by default, verifies composed outputs against
ordered stage lookup, and writes distinct hash-bound Old English bins;
`--model A` or `--model B2` builds just one. Missing or stale model
bins fail rather than falling back to the historical cascade. The
Germanic board, internal refishing and FST editor source default to
A; select B2 in the UI or pass `"model": "B2"` to the corresponding
Flask endpoint. A is a documented interface default, not a decision
against B2. `/compare-fst` accepts `"internal"` for either
transducer with independent `oldModel` and `newModel` fields; custom
editor text is still supported. Explicit `compatibility` selects the
historical Old English network. Modern doculect networks are unchanged.
Internal Germanic board operations verify the TSV's selected input
against each matching network rather than enumerating unrestricted
inverse candidates. Old English uses the selected counterpart spelling;
the display and modern doculect targets retain their IPA. Custom editor
transducers retain the unrestricted comparison path.

The main book prints both active traces against the shared selections.
The companion reports preserve all changed checkpoints and the full
orders. The rule inventory, historical replay, standalone lexical
reference and canonical graph's legacy diagnostic suite retain their
compatibility ordering; they are not the default application model.

Validation cost: `test_adoption_capture_is_bound_to_active_source_and_preserves_historical_controls`
reuses the earlier capture checks, now bound to the verified production
capture. `test_application_flask_selects_provisioned_historical_models`
adds native endpoints, two board loads and one bounded comparison against
the provisioned binaries; this catches model-selection and lookup-form errors
that the existing stage assertions cannot see. The focused full-board test
took about 14 seconds and adds no compilation in pytest. The one-time
application build uses the same two compiler processes
as the earlier staged assay (definition image and isolated export), adds
two composed model networks and one lookup batch per model, and copies
the four existing doculect exports. Build time was about eight minutes;
the sampled Foma memory high-water mark was at least 2,245,632 KiB
(`VmHWM` in `/proc/<pid>/status` inside the backend).

## Measured model results

| Comparison | A | B2 |
|---|---:|---:|
| Immutable research inputs | 382/394 | 385/394 |
| Six common selected forms | 6/6 | 6/6 |
| Active catalogue (hay included) | 387/396 | 388/396 |
| Newly admitted bed and kin | 2/2 | 2/2 |

The unchanged compatibility cascade gives 388/396, compared with
386/394 in the archived pre-adoption compatibility baseline. Every
unmigrated row is identical and the same eight rows remain unmatched.
The active compatibility output fingerprint is
`51953ed3a411b10bfa551de996053bc805ba87525180c4bf13f9b1ba46d4ee0e`.

The [production capture](captures/sc047-production-v1.json.gz) has 97
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

The inherited direct controls remain distinct from the selected cells:

| Direct singular | A | B2 |
|---|---|---|
| Net | *nete* | *nett* |
| Bed | *bede* | *bedd* |
| Kin | *cyne* | *cyn* |
| Hay | *hei* | *hīeġ* |
| Hue | *hī* | *hīew* |

These diagnostics preserve the intermediate differences in doubling
and final simplification. The 97 paradigm traces and 13 supplementary
probes also preserve the protected donors, pledge and wicg, the later
rest dative, both genitive quantities, and the lowering controls.

Re-execute with the application build command above. Raw run SHA-256:
`1644926a17ff2658ad855695d1f8465124e5b89835e287daba16ea0ff0412c76`.
Compressed production capture SHA-256:
`ed3ed52377ad1ce61f1ecac8e36df2a804916f1c008ff2523d2d773a8ed80d31`.
Corpus SHA-256:
`29f11c10e7cf8756c2708334fbd6947a4629ddcb9e69ac28bfbf9a920c5f9cf7`.
Full executable-input hashes are embedded in the capture. The
model capture alone is not an exact-commit strict certificate.

The [A](A-volume.pdf) and [B2](B2-volume.pdf) companion volumes and
full alternative traces can be regenerated from that capture without
rerunning Foma (set `SC047_PREVIEW_MONOFONT` to a local font that
covers the transducer symbols if Noto Sans Mono is unavailable):

```sh
python3 Germanic/docs/models/sc047/publish.py \
  Germanic/docs/models/sc047/captures/sc047-production-v1.json.gz \
  .capr-work/adoption-models --pdf
```

## Shared publication audit

The ordinary indexed book contains 180 full dossiers, including bed,
kin and hay; its selected catalogue and compact derivation projection
cover all 396 active entries. The strict build passed the assembled
semantic, citation, bibliography, occurrence-parity and rendered-reference
checks. It found 1,561 printable and 83 excluded explicit occurrences,
with no omissions, duplicates or semantic discrepancies.

In the 344-page main PDF, all 1,377 Index Verborum page-number links
resolve to the matching printed page labels. Representative destinations
include *bedde*, *peti* and *bedi* on p. 145, *heig* and *hīeġ* on
p. 174, *hecg* and *heġġ* on p. 175, Cotton *hiewes* on p. 180,
*cyn* and *cynnes* on p. 181, *nátjai* and *nette* on p. 193,
and *rástǭ*, *rástē* and *ræste* on pp. 299–300. The entries for Old
Saxon *feni*, Old Frisian *fene*, *fenne* and *fennem*, and Old
English *wicg*, *wicge* and *wicga* resolve to their comparative
discussion on p. 5. Their role and language metadata are checked
separately from the page-link audit.

The comparative chapter begins on p. 137 and the shared references on
p. 327. The Index Verborum bookmark opens the section's title page
(p. 335); the contents lists the first index entries on p. 336.
The main PDF SHA-256 is
`b8a7c0a6c3a6d6c8b68ec532e4910f2bf2ea3a9178c993ee74d106a7b8c4281a`.
The nine-page companion PDF hashes are
`faa2299efbe27b4aa7deb4fc7976ebdf18a000ebc8f523cd87e15042d83f6bab` (A) and
`3af8982e6ab96b9367577609d96979685d3a016647705d8f596c0e52343cf7ec` (B2).
