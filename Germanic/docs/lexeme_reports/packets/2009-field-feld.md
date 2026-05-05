# Evidence packet — 2009 field / feld

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2009 | field | feld | *félθuz | *félθuz | regular | R/T §5.1.3 p.171: *felθu-/*feldu- may reflect Verner's alternation or regular PWGmc *lθ→*ld; either gives OE feld | - |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# field
PROTO: *félθuz
EXPECTED: feld
OUTPUTS: feld



### Proto-Germanic consonant inheritance

Proto Input: *félθuz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>PWGmc L Th Voicing: *félduz<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *féldu | **Old English**<br>OE High Vowel Apocope: *féld |



### Orthography & surface

Outcome: feld

NOTE: R/T §5.1.3 p.171: *felθu-/feldu- may reflect Verner's alternation or regular PWGmc *lθ→ld; either gives OE feld
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:24457 (exact pair)

- Nearby heading: #### 1. Probe outcome (vs. post-§17.10.23 baseline of 38)

```text
24455: | \*bébruz   | befro   | befer    |
24456: | \*bōguz    | bōgo    | bōg      |
24457: | \*félθuz   | feldo   | feld     |
24458: | \*flōduz   | flōdo   | flōd     |
24459: | \*grúnduz  | grundo  | grund    |
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1338 (exact COUNTERPART)

- Nearby heading: ### Ambiguous examples (rule OR Verner's Law)

```text
1336: `*þ ~ *d` rather than (or in addition to) the `*lþ → *ld` rule:
1337: - `*gulþa- ~ *gulda-` → OE gold ('gold') — R/T §5.1.3 p.171
1338: - `*felþu- ~ *feldu-` → OE feld ('field') — R/T §5.1.3 p.171
1339: 
1340: For these, EITHER explanation yields the correct OE outcome. Our
```

#### Germanic/docs/DEV_NOTES.md:1354 (exact COUNTERPART)

- Nearby heading: ### Scope of Verner's Law in the project

```text
1352: mechanism. The current approach is case-by-case:
1353: - Where the regular sound change (`*lþ → ld`) gives the right answer, we
1354:   use it (gold, feld, fealdan, etc.)
1355: - Where only Verner's alternation explains the outcome (nǣdl), the item
1356:   remains a known mismatch until we decide on a systematic approach
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| field | feld | inh | template:inh | field |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:1875 (concept name)

- Nearby heading: #### CLI polish + harness hooks

```text
1873: - Added `--lexeme-file`, `--brace-diphthongs`, and `--save-log` switches so we can feed large TSV extracts straight into the tracer and drop the output into `docs/debug_snapshots/` without manual copy/paste. Example: `python3 tools/trace_english_sandbox.py --lexeme-file /usr/app/tmp/english_tracer_lexemes.txt --brace-diphthongs --save-log /usr/app/tmp/english_tracer_log.txt` (run inside Docker so `/usr/app/tmp` is writable).
1874: - Sample log (stored at `/usr/app/tmp/english_tracer_log.txt`) now drives the bucket review: `*fiskaz` reaches `Surface: fɪskæ`, `*braudą` reaches `Surface: brōdą`, while `*gebaną` and `*swestēr` still die at the surface filter—exact stage names are now captured in the log for regression diffs.
1875: - Added `tools/annotate_english_sandbox_results.py` to decorate the sandbox regression JSON with stage-by-stage outputs plus a `first_failing_stage` field. Usage (inside Docker so `flookup` is available):
1876:   ```bash
1877:   docker compose exec backend bash -lc \
```

#### Germanic/docs/DEV_NOTES.md:17679 (concept name)

- Nearby heading: #### 14.1 Tracing `*wir-uldu → weorold`: What Actually Happens (2026-04-12)

```text
17677: (b) An unhistorical shortcut that produces correct output accidentally?
17678: 
17679: **What the field seems to think:**
17680: 
17681: The consensus derivation for `weorold` assumes `*wer-` (with `*e`) as the input:
```

#### Germanic/docs/DEV_NOTES.md:18997 (concept name)

- Nearby heading: # Rule: medial u → o, except when preceded by u in prior syllable.

```text
18995: Row 1468 (youth): PROTOFORM changed from `*jugunθiz` to `*jugunθ`.
18996: 
18997: The NOTE field explains:
18998: > "PROTOFORM uses truncated form without -iz: R/T vol.2 p.141 notes early
18999: > apocope of -i in *-unþi- abstracts (before i-umlaut). Campbell §332:
```

#### Germanic/docs/DEV_NOTES.md:20970 (concept name)

- Nearby heading: ### §17.7 Success criterion

```text
20968:    Campbell §333.
20969: 5. §16 is rewritten to document a 2-way (not 3-way) convention that
20970:    aligns with field-standard notation.
20971: 
20972: At that point, every unstressed-a outcome in the FST is explained by
```

#### Germanic/docs/DEV_NOTES.md:22333 (concept name)

- Nearby heading: ### §17.10.14 — Phase 1d-β research: cross-source survey on A-restoration chronology and conditioning

```text
22331: Goal of this section: before redesigning `OEARestoration` to deal with
22332: the post-migration bare `{*a}` regression catalogued in §17.10.13,
22333: establish exactly what the field thinks the sound change is,
22334: chronologically and phonologically, so any new FST formulation is
22335: neogrammarian and historically defensible.
```

### Analysis and dossier hits

#### Germanic/docs/analysis/compound_archaism_inventory.md:53 (concept name)

- Nearby heading: ### Case 1: *mízdō (reward, wage) — meord (dialectal doublet, NOT compound)

```text
52: 
53: | Field | Value |
54: |-------|-------|
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:71 (concept name)

- Nearby heading: ### Case 2: *spéru (spear) — speoru

```text
70: 
71: | Field | Value |
72: |-------|-------|
```

#### Germanic/docs/analysis/compound_archaism_inventory.md:91 (concept name)

- Nearby heading: ### Case 3: *swéstēr (sister) — swester (lautgesetzlich) vs. swustor (late-WS innovation)

```text
90: 
91: | Field | Value |
92: |-------|-------|
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:29 (concept name)

- Nearby heading: ## 1. Mismatch Summary

```text
28: 
29: | Field | Value |
30: |-------|-------|
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:616 (concept name)

- Nearby heading: ### Option 3: Switch target to hypothetical compound form *meord-

```text
615: 1. **Weak attestation**: *meord-* in compounds is poorly attested; may not exist
616: 2. **Changes TSV semantics**: The COUNTERPART field is meant to be the **attested OE lemma**, not a reconstructed compound stem
617: 3. **User confusion**: Why are we targeting a compound when the simplex is well-attested?
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo.md:718 (concept name)

- Nearby heading: ### 8.4 How should we model analogical leveling in the FST?

```text
717: 
718: **Current practice** (per §17.16): Accept the mismatch, classify as analogical, document in NOTE field.
719: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:476 (concept name)

- Nearby heading: ### 4.2 The *spere parallel (Campbell §609)

```text
475: - Classifies the attested form as **analogical**
476: - Documents the mismatch in the NOTE field
477: 
```

#### Germanic/docs/analysis/mismatch_dossier_mizdo_supplement.md:804 (concept name)

- Nearby heading: ### 7.4 Final recommendation

```text
803: 
804: **Document thoroughly** in the NOTE field that:
805: 1. *meord* is not attested
```

#### Germanic/docs/analysis/notable_findings.md:1660 (concept name)

- Nearby heading: ### Contribution

```text
1659: 
1660: 3. **Honey/mead is a tangential homonym field worth flagging** but is not
1661:    relevant to the *mizdō-* problem itself. PIE *medʰu-* 'honey, mead' (OE
```

#### Germanic/docs/dossiers/g-palatalisation-conditioning.md:92 (concept name)

- Nearby heading: ### 2.1 Campbell, *Old English Grammar* (1959), §§ 426–430

```text
91: > sēċan seek, sicol sickle, þicgan to take, secgan say, hyġe mind), between
92: > a front vowel and a syllabic consonant (e.g. æcer field, nægl nail, fægr
93: > fair, wegn wain, regn rain, segl sail), and always after a vowel which has
```

## Bibliography-key candidates

### Preferred candidates

_None_

### Low-confidence candidates

_None_

