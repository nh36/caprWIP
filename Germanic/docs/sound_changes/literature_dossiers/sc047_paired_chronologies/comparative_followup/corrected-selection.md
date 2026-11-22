# SC047 corrected-selection replay

**Question.** Do independently selected feminine hedge and accusative rest
remove two regressions without altering either historical model? Does the
archived geminate-only nuclearizer then affect only the expected scored
labial cells? An additional scored output difference, or a change in
singleton or protected controls, would refute the narrow interpretation.

**Execution.** `SC047-corrected-cells-v1` takes the canonical prefix and
the pinned A/B suffixes from the original paired assay. It compiles finite
domains for the two replacements and for 21 matched probe labels (20
distinct inputs), sharing one definition image. B2 is B with `FNG` in place
of `FNU` after nasal loss; shared post-oral-loss `FON` is unchanged.
This replay does not compile new orders or add routine validation cost.

```sh
docker compose exec -T backend sh -lc 'cd /usr/app && python3 docs/sound_changes/literature_dossiers/sc047_paired_chronologies/comparative_followup/replay_selected_cells.py'
```

The command uses the original-selection research checkout with fresh
canonical runtime bins. To verify the splice, compare the full normalized
rows of the combined proposal (`oe_pipeline.load_rows`) with the frozen
capture by row ID: all 394 identities, targets and prosodic contexts agree;
only `proto`, `proto_norm` and `fst_input` differ for 2069 and 2152. For
B2, the archived `split_geminate_only` endpoints have the same 394 row
IDs, inputs and targets; its identity, early and split columns agree
row-for-row with the frozen pair. It differs from plain B only at 2061
and 2332. The new capture splices only the two re-executed rows; it does
not claim a fresh full-corpus execution of the other 392 endpoints.

| Measure | Canonical | A | B | B2 |
|---|---:|---:|---:|---:|
| Frozen selections, matches / 394 | 386 | 381 | 382 | 384 |
| Corrected selections, matches / 394 | 386 | 383 | 384 | 386 |

| Row | Change of input | Canonical (both selections) | A, B and B2 (old → new) |
|---|---|---|---|
| 2069 hedge | `*xágjaz` → `*xágjō` | `heġġ` | `heġe` → `heġġ` |
| 2152 rest | `*rástōz` → `*rástǭ` | `ræste` | `rast` → `ræste` |

In production, old hedge uses `*xággjaz > *xággja > *xággj`;
the feminine route uses `*xággjō > *xággju` and only later loses `u`.
Both feed palatalization and mutation. Old rest uses `*rástōz >
*rástō > *rástā`; the accusative reaches `*rástā` from long nasal
`*rástǭ` without final-*z* deletion. Both continue through brightening
and shortening to `ræste`. Hedge remains regular; rest's classification
keeps the possible analogical history of the nominative alongside a
regularly derived accusative.

| Remaining difference from canonical | Canonical | A | B | B2 |
|---|---|---|---|---|
| 2061 hay | `hīeġ` | `hēa` | `hewe` | `hīeġ` |
| 2138 net | `nett` | `nete` | `nett` | `nett` |
| 2332 hue | `hīew` | `hii` | `hiewe` | `hīew` |

All 394 outputs are unambiguous in every arm. The inherited mismatch IDs
are `1973, 2013, 2030, 2162, 2224, 2240, 2298, 2300`; the above
differences are additional to those, not a new definition of a match.

## Labial and negative controls

Both split arms first double the labial before nasal loss. At the
nuclearizer, hay `*xáwwj` becomes `*xáwwi` in B and stays `*xáwwj` in
B2, reaching `*xáuj` at SC029. Hue `*xíwwj` becomes `*xíwwi` in B;
B2 retains `*xíwwj`, giving `*xíuwj` at SC033 and `*xīowj` at SC110
in the archived detailed trace. The first divergence is therefore the
representation after loss, not production of the geminate.

| Control | A | B | B2 | Interpretation |
|---|---|---|---|---|
| hay protected genitive / plural | `hīeġes` / `hīeġ` | same | same | Prevocalic *j* does not need the intervention. |
| hue protected genitive / plural | `hīewes` / `hīew` | same | same | Cotton *hiewes* verifies the genitive stem; the plural is a model prediction. |
| glee direct / protected genitive | `glii` / `glīewes` | `gliewe` / `glīewes` | `glīew` / `glīewes` | Direct unscored *iwj* probe responds like hue. The output does not establish the reconstructed cell as an attestation. |
| new masculine oral direct / protected genitive | `nii` / `nīewes` | same | same | The singleton was already stranded at oral loss; FNG does not preserve it. |
| sew / strew | `sīewan` / `strīeġan` | same | same | Prevocalic *j* remains; these forms do not distinguish the chronologies. |
| believe / straw / show | `ġelīefan` / `strēa` / `sċēawian` | same | same | These named interference controls do not change under exact FNG. In particular *strēa* remains an inherited corpus mismatch here. |
| dill / door / there / where | `dile` / `dor` / `þǣr` / `hwǣr` | same | same | Non-geminating and nonlabial controls are invariant. |
| net, direct | `nete` | `nett` | `nett` | A's regular prediction is unaffected by a labial intervention. |

The exact B2 intervention is not the broader delayed-singleton or
labial-rule relocation package. Its positive controls show a common
structural effect, not lexical exceptions. Its success does not prove
an independent surviving *j* phoneme or establish that the vowel
history of each attested direct cell was inherited. The scored *show*
control is `*skáwōjaną`, not proof about the separate historical
*awj* example discussed by Hogg. See the
[historical assessment](discrepancy-classification.md) for the different
singleton problems under A and the specific remaining source questions.

## Identities

| Input or receipt | SHA-256 |
|---|---|
| Frozen A/B capture, compressed | `f2962dde3a9f0e1771c6de1bab6cbd2b18f0f844bbddfcb6807b7dab81e43060` |
| Frozen labial endpoint TSV | `3f9c5f6fa0c9b65b44c263a004b6e3ebc994397f1127c3a2d5295a3f82470d27` |
| Frozen labial plan | `71b0bf5b33e9ee8196964245b6f0050ea3a200a71f7ba10065f3379f9ca155d5` |
| Production FST (unchanged) | `43188e9a8e5bcbd028043675586c6655f81394beba55f0a4bb4044792db4050f` |
| Corrected corpus TSV | `538b67e909f71ce0b620e54f34b059f993ac4608ecdd4cf846c49cd18764a6a3` |
| Context metadata (unchanged) | `6a69a8d450a0ad5898bed7150136dc70e5731422c29803608825cdefc6b0f914` |
| [Corrected replay capture](corrected-selection-observations.json.gz), compressed | `83ec684cbb7caa27cc9f11d065103824891c3a1624a6b24fe1ed288f522d1133` |
| Corrected capture JSON, uncompressed | `952e24106213c2ec84be68675e7c3eda21641dce005063adc3c9f9a1fcf67a24` |

**Verdict and propagation.** Retain the production cascade and both
frozen research orders. The two lexical corrections stand independently.
B2 remains a research variant; A's singleton outputs and independently
attested protected forms remain unscored philological evidence except
for the original selected direct cells. Defer the historical order;
do not reopen on match totals alone.
