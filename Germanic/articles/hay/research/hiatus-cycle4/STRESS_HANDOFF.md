# I2a — Carrying the existing foot distinction across h-loss

## Question and baseline

Can the same S1 root/weak distinction be used immediately **after** h-loss, without a freely inserted marker or a different window for prefixed roots? This is a research-only representation check against canonical, A and B2, from the frozen source plus the S1 `FootCtx` repair to weak contraction. The existing pretonic marker derives from positively marked input stress; the experiment does not infer a stress contour from a modern prefix or pronounce every compound marker primary. Historical footing and its limits are assessed separately in the [original stress dossier](../hiatus-cycle2/STRESS.md); the prefix and weak-tail examples and source distinctions are in the [Q2 ledger](source-entry-audit.tsv).

## Diagnosis

The [new receipt](stress-handoff-traces.json.gz) reproduces the S2 ‘world’ failure in each order. The exact incoming string `*w*⌃*éo*r*⌄*u*l*d` leaves the lifted u-lowering rule as `**⌃w*éo**⌄r*o*l*d`: each tag has crossed a `*` delimiter rather than staying before a vowel token. Neither placement passes the archived alignment predicate. Without the free lift the same lowering maps ordinary `*w*éo*r*u*l*d` to `*w*éo*r*o*l*d` and ‘world’ surfaces as *weorold*. Thus the reported failure is in lifting a relation over serialized symbols, not in lowering or compound phonology.

The repaired probe factors frozen `OEHLoss` into the **same** `FootCtx`-wrapped deletion and the **same** marker removal. It moves only the removal across an optional strictly late test. With no intervening test, this is the original composition: no article, corpus form or production rule is edited. Unlike S2, this uses a domain marker already consumed and propagated by the frozen rules, not a symbol inserted indiscriminately into their input/output alphabets.

| Witness role | Experimental result |
|---|---|
| Eight independently selected weak firings across both archived and active panels | Before and after agree exactly with the S1 census, per order and per input. The experiment is focused on these firings, not a fresh 790-row census. |
| Full ‘world’, ‘believe’ and simplex ‘call’ | The handoff without a late overlay retains all S1 outputs; it adds no stress or quantity claim about them. |
| Plain prefixed root, otherwise similar later weak material | At the first stage after h-loss, contraction, gliding and atomic incorporation all see the head without an acute. None changes the explicitly later weak sequence. |
| H-loss positive ‘strike’ | The h-loss step converts `*s*l*e*ç*i*θ` to `*s*l*e*i*θ` under both versions. All three late diagnostics see this newly created sequence as well as the pre-existing ‘call’ sequence. |
| Prefixed ‘call’ present and participle | In A/B2 strictly late contraction gives *ġecēþ/ġecēd*. Gliding gives *ġeceġþ/ġeceġd*. For incorporation, the private atomic token is shown before a separately labelled print step, yielding *ġeceiþ/ġeceid*; the latter spellings do not imply syllabification. Canonical full entries have different upstream nuclei, so the short-input operation does not apply. |

## Verdict and limits

**RETAIN** S1 and the original phonological h-loss context; **REFORMULATE** the placement of marker removal for the immediate post-loss research comparison. The strictly late ‘call’ facts do not require a separate pre-loss resolution window merely to detect its head. This says nothing about whether *w*- and *h*-generated sequences actually resolved together, the placement relative to high-vowel loss, or the choice among mechanisms. The test stops marker propagation before the incumbent contraction/orthography stages. It does not yet implement independently valued secondary stress, all complex nuclear types, or a full late prosodic alphabet; those are separate requirements for a prospective stack.

```bash
set -o pipefail
c=Germanic/articles/hay/research/hiatus-cycle4
bash "$c/run-container.sh" stress_handoff --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 > /tmp/capr-hay4-stress-handoff-replay.json.gz
```

The trace binds to the pinned source, original panels and isolated exports. No production verdict or new chronology edge is registered.
