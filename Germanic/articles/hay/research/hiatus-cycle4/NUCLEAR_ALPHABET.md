# I3a — Distinct nuclear structures and stage-local admission

## Question and baseline

The [cycle-three assay](../hiatus-cycle3/REPRESENTATION.md) assigned two different weight classes to **the same** pair of private nuclei in separate builds. This increment asks whether both classes, and the accented and unaccented members of each, can coexist in one compiled inventory without changing the existing behavior for syllabic hiatus, inherited *ei*, or a following palatal.

| Structure | Executable tokens | Final short *i* in the test frame *t–d–i* |
|---|---|---|
| Mid vowel followed by syllabic *i* | `*e*i` or `*é*i` | Retained for the unaccented probe: the adjacent vowels do not parse as a single heavy nucleus |
| Short complex front nucleus | `*ėi` or `*éi` | Retained with either accent value |
| Heavy complex front nucleus | `*ēi` or `*ḗi` | Deleted with either accent value |
| Inherited complex nucleus | `*ei` | Deleted under its unchanged frozen classification |
| Short *e* plus approximant or palatal fricative | `*e*j`, `*e*ʝ` | Deleted: the palatal plus following *d* supply two consonants in this frame |
| Long *ē* plus approximant | `*ē*j` | Deleted; distinct from both long complex nucleus and long syllabic sequence |

These are phonological alternatives encoded as different segments or syllable structures, not tags for the etymological origin of a segment. An identical input token receives identical conditioning. The light/heavy incorporation and dental-edge monophthongization are comparison operations, not claims that both weights occurred or that their historical domains were the same.

## Diagnosis and controls

- The gate at the research entry admits the four nuclear tokens but rejects an unlicensed control. The frozen HVD rejects all four private tokens; its empty output is **not** evidence of historical deletion. The frozen Proto-Germanic gate cannot construct these tokens: the unstarred strings with long *ē/ḗ* happen to be admitted as **two** vowel tokens, not as the research nucleus.
- Nonhigh syncope can remove an open linking vowel in a compound-shaped probe without deleting the first nucleus; the l-adjacent rule fires only with a light nucleus. These are structural examples, not new compound witnesses. The native palatal merger neutralizes the approximant–fricative contrast, which is still available at the earlier weight test.
- An acute survives incorporation and experimental monophthongization. The plain prefixed root is recognized through its existing foot marker; otherwise comparable posttonic material is not incorporated. The late print stage renders all four research nuclei alike without claiming that their quantity or syllabification was alike. Serializing is distinct from historical realization; inherited diphthong realization does not get recast as a rule for these new nuclei.

## Verdict and reproducibility

**RETAIN** the frozen historical rules and **DEFER** integration of the private inventory into general phonological domains until intervening and later components are audited. This demonstrates that the distinctions can coexist in the same relevant weight, syncope and output assays. It neither proposes a new sound law nor promotes a chronology edge. No registry or corpus state changes. The structural assessment follows the [earlier representation dossier](../hiatus-cycle3/REPRESENTATION.md) and its HVD literature basis (Fulk 2010: 129–134; Goering 2016: 186–188, 2023: 67–68); the new evidence is executable only.

```bash
set -o pipefail
c=Germanic/articles/hay/research/hiatus-cycle4
bash "$c/run-container.sh" nucleus_check --stage-cache /tmp/capr-hay-stress.lVemXDSn |
  gzip -n -9 > /tmp/capr-hay4-nucleus-replay.json.gz
```

The [receipt](nucleus-traces.json.gz) identifies the frozen source, ordered stages, isolated research exports and exact outputs. Recompilation may change binary hashes without changing traces. Validation cost: one private nine-export build and focused lookups, no default suite, corpus sweep or production rebuild.
