# Evidence packet — 2273 wasp / wæfs

> This packet is evidence for drafting. Do not treat all hits as equally authoritative; prefer high-confidence evidence.

## TSV row data

| ID | CONCEPT | COUNTERPART | PROTO | PROTOFORM | DERIVATION_CLASS | NOTE | HISTORY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2273 | wasp | wæfs | *wábsaz | *wábsaz | attested_variant | Retargeted from late-WS doublet 'wæsp' to the earliest attested OE form 'wæfs' (Épinal-Corpus glossary; Bülbring §484 Anm.3 'spät-ws. wasp aus wæps <waefs Corp.'; Fulk §6.5 lists wæfs first; Brunner §193,3 cites Ep.Corp. 'waefs'). Cascade: *wabsa- → *wæbs (a-fronting + final-V losses) → *wæβs (PGmcBAllophony) → wæfs (surface devoicing of *β before voiceless *s). The successive doublets wæfs > wæps (fs→ps, Brunner §193,3) > wasp (ps→sp, Brunner §204,3) are both lexically- and dialectally-restricted late-WS metatheses — implementing them would regress *drīfst-type forms (Brunner §193,3 Anm.2). Same playbook as §17.45 (spindle→spinl): target the lautgesetzlich early-OE form. See §17.47. | Source: Wiktionary etymology (template:inh) \| Source: Wiktionary etymology (template:inh) |

## Manifest status

_No manifest entry._

## High-confidence evidence

### Compact derivation trace entry

```md
# wasp
PROTO: *wábsaz
EXPECTED: wæfs
OUTPUTS: wæfs



### Proto-Germanic consonant inheritance

Proto Input: *wábsaz

| Earlier Germanic developments | Old English developments |
|:---|:---|
| **Proto-West Germanic**<br>[no change]<br><br>**Northwest Germanic**<br>PGmc Final Z Deletion: *wábsa | **Old English**<br>PWGmc Final Bare A Loss: *wábs<br>Anglo Frisian Brightening: *wæbs<br>PGmc B Allophony: *wæβs |



### Orthography & surface

Outcome: wæfs

NOTE: Retargeted from late-WS doublet 'wæsp' to the earliest attested OE form 'wæfs' (Épinal-Corpus glossary; Bülbring §484 Anm.3 'spät-ws. wasp aus wæps <waefs Corp.'; Fulk §6.5 lists wæfs first; Brunner §193,3 cites Ep.Corp. 'waefs'). Cascade: *wabsa- → *wæbs (a-fronting + final-V losses) → *wæβs (PGmcBAllophony) → wæfs (surface devoicing of *β before voiceless *s). The successive doublets wæfs > wæps (fs→ps, Brunner §193,3) > wasp (ps→sp, Brunner §204,3) are both lexically- and dialectally-restricted late-WS metatheses — implementing them would regress *drīfst-type forms (Brunner §193,3 Anm.2). Same playbook as §17.45 (spindle→spinl): target the lautgesetzlich early-OE form. See §17.47.
```

### Matching oe_known_problems.tsv entries

_None_

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:42199 (row ID)

- Nearby heading: ### The mismatch

```text
42197:   | *wábsaz  | wæfs    | wæsp       | cons_mismatch__f_vs_s__cluster |
42198: 
42199: Row 2273 in `germanic-aligned-final.tsv`. Cognate-set "wasp".
42200: 
42201: ### FST trace (excerpt)
```

#### Germanic/docs/DEV_NOTES.md:42346 (row ID)

- Nearby heading: ### Verification plan

```text
42344: ### Verification plan
42345: 
42346: 1. Edit row 2273: TOKENS `w æ f s`, COUNTERPART `wæfs`, append NOTE
42347:    citing Bülbring §484 Anm.3 + Brunner §193,3 + Fulk §6.5.
42348: 2. (No FST change needed.)
```

### Analysis and dossier hits

_None_

## Supporting/background evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:9533 (exact COUNTERPART)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9531: wagnăz → wagn (should be wæġn) - REGRESSED
9532: labbăz → labb (should be læppa) - REGRESSED (was læbb)
9533: wabsăz → wafs (should be wæsp) - REGRESSED (was wæfs)
9534: ```
9535: 
```

#### Germanic/docs/DEV_NOTES.md:42213 (exact COUNTERPART)

- Nearby heading: ### FST trace (excerpt)

```text
42211: ... PWGmcFinalBareALoss/…:     *w*æ*b*s
42212: PGmcBAllophony (proto_to_oe):  *w*æ*β*s
42213: Surface:                       wæfs
42214: ```
42215: 
```

#### Germanic/docs/DEV_NOTES.md:42220 (exact COUNTERPART)

- Nearby heading: ### FST trace (excerpt)

```text
42218: voiced segments, surfacing as f when later devoiced before a voiceless
42219: obstruent. Grimm's-law failure for *bs / *ps clusters (Fulk §6.5):
42220: "OE wæfs (also wæsp, wæps) 'wasp' (PIE *uobhs-; cf. Lith. vapsvà
42221: 'wasp', Avestan vawžaka- 'scorpion')."
42222: 
```

#### Germanic/docs/DEV_NOTES.md:42231 (exact COUNTERPART)

- Nearby heading: ### Source audit — what is the actual attested OE form?

```text
42229: > "Ebenso entsteht spät-ws. *wasp* aus *wæps* 'Wespe' (<*waefs* Corp.)."
42230: 
42231: — i.e. late-WS `wasp` ← `wæps` ← `wæfs`, with `wæfs` being the form
42232: attested in the Corpus glossary (the earliest direct attestation).
42233: 
```

### Analysis and dossier hits

_None_

### Local lexical-table hits

#### old_english_wiktionary.tsv

| ENGLISH | OE_FORM | SOURCE | DETAIL | PAGE |
| :--- | :--- | :--- | :--- | :--- |
| wasp | wæsp | inh | template:inh | wasp |

#### old_english_swadesh.tsv

_None_

## Possibly stale or diagnostic evidence

### DEV_NOTES hits

#### Germanic/docs/DEV_NOTES.md:9539 (concept name)

- Nearby heading: ### Empirical Validation (Dry Run 2026-03-13)

```text
9537: 
9538: - **Fixed: 6** (bake, grave, wade, wake, wash, will)
9539: - **Regressed: 9** (craft, day, mast, raven, staff, tap, wain, lap, wasp)
9540: 
9541: ### Analysis: Why the Fix Fails
```

#### Germanic/docs/DEV_NOTES.md:42191 (exact pair)

- Nearby heading: ## §17.47 *wábsaz → wæfs (expected wæsp): TSV target is the late-WS doublet, not the lautgesetzlich form

```text
42189: 
42190: 
42191: ## §17.47 *wábsaz → wæfs (expected wæsp): TSV target is the late-WS doublet, not the lautgesetzlich form
42192: 
42193: ### The mismatch
```

#### Germanic/docs/DEV_NOTES.md:42197 (exact pair)

- Nearby heading: ### The mismatch

```text
42195:   | PROTO    | FST out | TSV target | Sub-bucket               |
42196:   |----------|---------|------------|--------------------------|
42197:   | *wábsaz  | wæfs    | wæsp       | cons_mismatch__f_vs_s__cluster |
42198: 
42199: Row 2273 in `germanic-aligned-final.tsv`. Cognate-set "wasp".
```

#### Germanic/docs/DEV_NOTES.md:42221 (concept name)

- Nearby heading: ### FST trace (excerpt)

```text
42219: obstruent. Grimm's-law failure for *bs / *ps clusters (Fulk §6.5):
42220: "OE wæfs (also wæsp, wæps) 'wasp' (PIE *uobhs-; cf. Lith. vapsvà
42221: 'wasp', Avestan vawžaka- 'scorpion')."
42222: 
42223: ### Source audit — what is the actual attested OE form?
```

#### Germanic/docs/DEV_NOTES.md:42229 (concept name)

- Nearby heading: ### Source audit — what is the actual attested OE form?

```text
42227: **Bülbring §484 Anm.3** (Elementarbuch p.213):
42228: 
42229: > "Ebenso entsteht spät-ws. *wasp* aus *wæps* 'Wespe' (<*waefs* Corp.)."
42230: 
42231: — i.e. late-WS `wasp` ← `wæps` ← `wæfs`, with `wæfs` being the form
```

### Analysis and dossier hits

_None_

## Bibliography-key candidates

### Preferred candidates

| Key | Why it was selected |
| :--- | :--- |
| Fulk2018 | single available key for Fulk |

### Low-confidence candidates

_None_

## Paradigm probe

Paradigm probe required for this row, but no built-in `oe_paradigm_probe.py` specification exists yet. This packet should be used to draft the probe configuration before prose drafting.

