# Dossier: row 2216 stem / stemn / stefn (2026 evidence gate)

## Source facts
- Orel 2003, p. 371 (`docs/references/orel_handbook_germanic_etymology.vision.txt:41236-41260`; page marker `:37025`) reconstructs `*stamnaz *stamniz` with ON `stafn`, OE `stefna`, OFris `stevene`, OS `stamn`, and OHG `stam`.
- Orel 2003, p. 373 (`...:41518-41526`; page marker `:37242`) separately reconstructs the voice-word `*stebnō ~ *stemnō`, with OE `stefn, stemn` 'voice'; this is the excluded homonym.
- Ringe–Taylor vol. 2, p. 346 (`docs/references/ringe_taylor_linguistic_history_vol2.txt:18934-18935`) give the voice chain `*stebno -> *stebnu -> OE stebn -> stefn -> stemn`, confirming that the earlier `*stébnō` solution belongs to the wrong lexeme.
- Clark Hall (`docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:38045-38052,38341-38343`) distinguishes `stefn` I 'voice, sound', `stefn` III 'stem, trunk ... prow or stern of a vessel', `stefna` 'prow or stern of a ship', `stemn = stefn`, and `stofn` 'trunk, stem, branch, shoot'.
- Luick (`docs/references/luick_historische_grammatik.txt:11324-11334,16992-17000`) gives stem-side `stemn Stamm` (perhaps from `*stofn`, with OS `stamn` and ME `stam`) and separately `stefn Stimme`.
- Brunner (`docs/references/brunner_1965_altenglische_grammatik.vision.txt:4016-4017,8040-8045`) records both `stefn, stemn Stamm` and the later southern/WS `fn > mn` doublets `stemn Stimme, stemn Stamm`.
- Bülbring (`docs/references/bulbring_altenglisches_elementarbuch.txt:9012-9015`) likewise has `stemn 'Stimme', stemn 'Steven'`.
- Kroonen (`docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:24696-24708,1738-1756`) is evidence for the voice/ablaut complex (`*stimno-`, `*stebnō`, `*stamnjō-`), not for the stem/trunk row as such.

## CAPR modelling choices
- CAPR stress-marking turns Orel's unaccented i-stem variant into `*stámniz`; that is a notation choice, not a source claim.
- The source layer secures the stem/trunk/prow family and an attested stem-side `stemn` doublet, while leaving the exact internal relation among `stefn`, `stefna`, `stofn`, and `stemn` partly open.

## Gate judgement
- Source-derived: the citation reconstruction should remain in the `*stamnaz/*stámnaz` family, not the voice-word `*stebnō/*stébnō` family.
- Source-derived: Orel attests an i-stem variant `*stamniz`; Clark Hall, Luick, Brunner, and Bülbring all support stem-side OE material that includes or cross-references `stemn`.
- CAPR probe result: the unchanged cascade derives `stámniz -> stemn` with multiplicity 1; no `mn -> fn` rule is needed for that target.
- Inference: the hypothesis is established strongly enough to justify a one-row TSV correction to `PROTOFORM = *stámniz` and `COUNTERPART = stemn`, while keeping `PROTO = *stámnaz`.
- Unresolved but non-blocking: whether `stemn` is best understood as a secondary doublet beside `stefn/stefna/stofn`, and how the stem-side variants should be narrated in later prose.

Recommendation: **PROCEED TO TSV CORRECTION**.

## Implementation update (2026-08-14): superseded target under the corrected cascade

The gate above was written against the **old** cascade, under which
`*stámniz -> stemn` (multiplicity 1) and the recommendation was
`COUNTERPART = stemn`. That recommendation is now **superseded** by the
implementation of the literal adjacent-`mn` SC022 (the same rule change that
retires the `mV…n` heaven proxy; see `dossier-heaven-paradigm-history-2026.md`
§15 and `audits/heaven-sc022-implementation-2026.md`).

Under the **corrected** cascade the i-stem input now derives the primary
stem/trunk form directly, multiplicity 1:

```text
*stámniz
  EAF Final Z Deletion:    *stámni
  PNWGmc Mn Dissimilation: *stáβni   ← adjacent mn > βn (SC022)
  EAF Brightening:         *stæβni
  OE i-Umlaut:             *steβni   ← æ > e (i-stem ending)
  OE High Vowel Apocope:   *steβn
  Orthography:             stefn
```

Implemented row 2216 fields:

```text
PROTO             *stámnaz     (a-stem citation, retained)
PROTOFORM         *stámniz     (Orel's attested i-stem variant, selected input)
COUNTERPART       stefn        (attested stem/trunk/prow form; Clark Hall stefn III)
DERIVATION_CLASS  early_analogy
```

Notes:

- `stefn` and `stemn` are both attested stem/trunk forms (Clark Hall; Luick §211;
  Brunner §205). The corrected cascade yields `stefn` (the primary form and the
  existing COUNTERPART), so the earlier `stemn` target is no longer needed.
- The homonym distinction is unchanged and must be preserved: this row is the
  stem/trunk/prow word (< `*stámnaz ~ *stámniz`, Orel 2003:371), **not** the
  voice/sound homonym (< `*stebnō ~ *stemnō`, Orel 2003:373; Ringe–Taylor vol. 2
  p. 346). The earlier `*stébnō` PROTOFORM belonged to the wrong homonym and is
  not used.
- Class is `early_analogy`: selecting the i-stem input over the a-stem citation
  is a pre-OE input selection; the Old English development is then regular.

Revised recommendation: **IMPLEMENTED** (PROTOFORM `*stámniz`, COUNTERPART
`stefn`, class `early_analogy`).
