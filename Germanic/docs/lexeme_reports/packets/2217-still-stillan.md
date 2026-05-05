# Evidence packet — 2217 still / stillan

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2217 | still | stillan | *stéllijaną | *stéllijaną | regular | OE stillan wv. 'to still, calm' matches verb form of Du. stillen, G stillen; stille is adj. | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# still
PROTO: *stéllijaną
EXPECTED: stillan
OUTPUTS: stillan



### Proto-Germanic consonant inheritance

Proto Input: *stéllijaną

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>[no change] | **Old English**<br>OE Heavy Syllable Nasal Apocope: *stéllijan<br>OE Secondary Nasalization: *stéllijąn<br>Sievers Law Syncope: *stélljąn<br>OE I Umlaut: *stilljąn<br>OE Weak Tail Reduction: *stilljan<br>OE J Loss After Heavy: *stillan |



### Orthography & surface

Outcome: stillan

NOTE: OE stillan wv. 'to still, calm' matches verb form of Du. stillen, G stillen; stille is adj.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

_None_

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:8730 (exact COUNTERPART)

- Nearby heading: ### Empirical Confirmation from Our TSV

```text
8728: | `*sōkjăną` | CVVk (heavy) | `-jăną` | sēċan |
8729: | `*sandjăną` | CVCC (heavy) | `-jăną` | sendan |
8730: | `*stelljăną` | CVCC (heavy) | `-jăną` | stillan |
8731: | `*strakkjăną` | CVCC (heavy) | `-jăną` | streċċan |
8732: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| still | stille | inh | template:inh | still |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:106 (concept name)

- Nearby heading: ### Could we use paradigm forms? (Why we decided not to)

```text
104: - R/T explicitly calls leveling from these forms "implausible" because they are "relatively marginal in functional terms" (p.47). The instrumental singular was an infrequent case form, making it unlikely to be the analogical source for the entire paradigm's root vowel.
105: - If inst.sg. *-u could drive paradigmatic leveling for *wulf- and *full-, it should have done the same for *folc, *folm, *bolla, etc. — but those show regular lowering. The approach would explain some exceptions but cannot explain why the inst.sg. analogy worked here and not elsewhere.
106: - R/T's analysis orders u-lowering BEFORE the loss of final *a in PWGmc. At that early date, the relative paradigmatic weight of the inst.sg. would have been even smaller, since many more case-forms with non-high endings still survived.
107: 
108: **Approach C: Use the root-noun analysis (for words that could have been root nouns).**
```

#### Germanic/docs/DEV_NOTES.md:226 (concept name)

- Nearby heading: ### OE Medial unstressed `*u → *o`: Conditioning environment (2026-03-20)

```text
224: 
225: **Problem discovered:** After fixing NWGmcULowering to restrict to stressed vowels,
226: `*widuwōn` still produced `widowe` instead of `widuwe`. The culprit was a separate
227: rule `OEMedUnstressedULowering` that lowered ALL medial unstressed `*u` to `*o`.
228: 
```

#### Germanic/docs/DEV_NOTES.md:544 (concept name)

- Nearby heading: ### FST analysis: Why changing target to `wuduwe` won't suffice (2026-03-21)

```text
542: - Current output: `widowe`
543: - Expected: `wuduwe`
544: - Still a mismatch (different form, same count)
545: 
546: **Required fixes:**
```

#### Germanic/docs/DEV_NOTES.md:883 (concept name)

- Nearby heading: ### Current FST rule and needed changes

```text
881:    **Pipeline ordering note:** R/T mentions only `*i`, not `*e`. An earlier
882:    draft targeted `[{*i}|{*e}]` but this was unnecessary: the medial vowel
883:    is still `*i` at this point because `OEMedUnstressedILowering` (which
884:    lowers `*ĭ` → `*e`) fires AFTER syncope in the pipeline.
885: 
```

#### Germanic/docs/DEV_NOTES.md:934 (concept name)

- Nearby heading: ### Source analysis

```text
932: **R/T (vol.2, p.385) on OE u-stems:**
933: 
934: > "The u-stems remained a recognizable inflectional class, but its membership was reduced to a few very common and basic words. Still inflected as u-stems in early OE are masc. *sunu* 'son' and *wudu* 'wood' and fem. *hand* 'hand', *nosu* 'nose', and ***duru* 'door'** (the last **originally a root-noun that had shifted into the u-stems**)."
935: 
936: R/T also note (p.28) in discussing u-lowering:
```

#### Germanic/docs/DEV_NOTES.md:1149 (concept name)

- Nearby heading: ### The answer: Kroonen (2006), "Gemination and allomorphy in the Proto-Germanic mn-stems"

```text
1147: 
1148: Kroonen (2006:22):
1149: > "The fact that `*but(t)ma-` received its t analogically from `*buttaz` can nevertheless only be understood if the two root forms were still part of one and the same paradigm after Kluge's law. In other words, the roots `*bud-` and `*but(t)-` must have been two allomorphs at a certain stage."
1150: 
1151: And crucially (2006:22):
```

### Analysis and dossier hits

#### Germanic/docs/analysis/arestoration_r_l_research.md:696 (concept name)

- Nearby heading: ### 10.5 Predicted effects on neighbouring rule behaviour

```text
695: * `*hnappōjan → hnappian` (Campbell §158): intervening `*pp` — geminate in set — restoration applies. ✓
696: * `*flaskōn → flasce` (germanic.txt comment line 1798): intervening `*sk` — `sC` in set — restoration applies, then `SkPalatalization` runs after the *a*. ✓ (Still produces `flasce`, not `flæsce`.)
697: * `*næglaz` plural `*næglas` → `næglas` (Campbell §158): intervening `*gl` — `Cl` cluster, **not** in the new set — restoration does *not* apply. ✓ (consistent with Campbell's "always *næglas*").
```

#### Germanic/docs/analysis/arestoration_r_l_research.md:751 (concept name)

- Nearby heading: ## 11. Affected TSV rows

```text
750: 
751: **Row 2205 (`*spárēną → sparian`)**: Probed output under current FST is `spearen`. The proposed fix changes `OEARestorationIntervening` so that the *r* of `*spár-` is no longer excluded, but the trigger vowel of `*spárēną` is `*ē` (front), so A-restoration still does not fire. The path to `sparian` requires a class III → class II morphological remap (`*sparēn- → *sparōjan-`) which appears to be missing or out of order in the FST pipeline. **This is a separate, larger issue** beyond the scope of this report.
752: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:646 (concept name)

- Nearby heading: ### Option 5: Proto-form switch to hypothetical `*mezdō` (e-grade)

```text
645: **Test**:
646: - FST output would still be `meord`, not `mēd`
647: - This doesn't solve the mismatch
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:655 (concept name)

- Nearby heading: ### Option 5: Proto-form switch to hypothetical `*mezdō` (e-grade)

```text
654: 2. **Gothic refutes it**: Gothic *mizdō* has *i, not *e
655: 3. **Doesn't solve the problem**: FST would still produce `meord`, not `mēd`
656: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:657 (concept name)

- Nearby heading: ### Option 5: Proto-form switch to hypothetical `*mezdō` (e-grade)

```text
656: 
657: **Result**: ❌ **Rejected**. This would falsify the etymology and still leave the mismatch unresolved.
658: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:634 (concept name)

- Nearby heading: ### 6.3 Is *mēd* regular or analogical?

```text
633: 
634: **Possible resolution**: Kroonen may be treating *z as non-triggering for breaking (i.e., *izd does not undergo breaking because the *z is still present, and breaking only applies after rhotacism gives *ird).
635: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:735 (concept name)

- Nearby heading: ### 7.3 Recommended TSV/FST action

```text
734: 
735: **Option A** (Original dossier Option 1): **Status quo + NOTE** ⭐ **STILL RECOMMENDED**
736: 
```

#### Germanic/docs/analysis/notable_findings.md:460 (concept name)

- Nearby heading: ### Expert consultation (Stefan Schuhmacher, Vienna, 2026-03-20)

```text
459: **Assessment:** Kroonen's reconstruction is n-stem, not u-stem. However,
460: Schuhmacher's suggestion could still be valid if there was an earlier u-stem
461: stage (\*buku-?) before the n-stem formation, or if some dialects preserved a
```

#### Germanic/docs/analysis/notable_findings.md:645 (concept name)

- Nearby heading: ## 4. A-restoration trigger set: {*æ} is NOT a trigger

```text
644: reasoning that suffix *a (like gen.sg. *-as) had been fronted to *æ by AFB
645: but was "underlyingly back" and should still trigger restoration. This seemed
646: necessary to explain A-restoration in a-stem paradigms.
```

#### Germanic/docs/analysis/notable_findings.md:1114 (concept name)

- Nearby heading: ## 7. NWGmc *i > *e lowering: consonant-conditioned blocking and rule ordering

```text
1113:   phonologization, noting that Older Runic forms show the change with
1114:   conditioning factors still intact.
1115: 
```

#### Germanic/docs/dossiers/bugan-scufan-paradigm-cell-review.md:33 (concept name)

- Nearby heading: ## §1. Question

```text
32: This dossier asks whether — knowing now what we did not know in
33: checkpoint 065 — the **3 pl. pret. is still the right paradigm cell
34: to target**, and whether some other cell of the same paradigm would
```

#### Germanic/docs/dossiers/bugun-scufun-attestation.md:213 (concept name)

- Nearby heading: ### Verdict

```text
212: verify. The closest the record comes to a non-`-on` form is
213: Northumbrian `scyufon` in the Durham Ritual, which still has `-on`
214: (it differs from southern `scufon` only in the stem-vowel
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:448 (concept name)

- Nearby heading: ## 7. Regression watchlist for the cascade

```text
447: After applying the rule in § 6.1 (or 6.2), re-run the cascade and verify
448: these TSV rows still hit their expected English reflex:
449: 
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1168 (concept name)

- Nearby heading: ### B.8 Synthesis across the canvass: answers to questions A-G

```text
1167: - Within the cascade: the rule must precede OEMedUnstressedULowering
1168:   (so the *u trigger is still present when the rule fires), and
1169:   must precede whatever models Anglian smoothing if such forms
```

#### Germanic/docs/dossiers/widuwe-u-preservation.md:1299 (concept name)

- Nearby heading: ### B.9 RECOMMENDATIONS

```text
1298:    - The draft's pre-OEMedUnstressedULowering ordering is
1299:      correct: the *u trigger must still be present when the
1300:      rule fires, and the early date of the change (pre-700)
```

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

