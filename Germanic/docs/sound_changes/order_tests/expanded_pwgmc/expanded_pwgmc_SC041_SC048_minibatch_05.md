# Expanded PWGmc SC041-SC048 mini-batch 05

## Scope

Nathan manually ran the expanded-PWGmc **earlier-side** mini-batch for:

1. `SC041` earlier
2. `SC042` earlier
3. `SC043` earlier
4. `SC044` earlier
5. `SC045` earlier
6. `SC046` earlier
7. `SC047` earlier
8. `SC048` earlier

This note documents those rows as expanded-profile evidence only. It does not revise the default 70-card chronology-card corpus.

## Files used

This mini-batch is documented from the committed expanded-profile outputs only:

1. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01.tsv`
2. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_changes.tsv`
3. `Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_01_failures.tsv`

## Summary table

| change_id | direction | result | boundary / first break | variants tested | changed outputs | new failures | profile interpretation | note |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- |
| `SC041` | earlier | `first_break_found` | crossing `SC020` `PGmc Final Z Deletion` | 21 | 67 | 64 | `confirms_default_broad_far_break` | large broad/far break; representative failures: `beard`, `bosom`, `bottom`, `calf`, `coat` |
| `SC042` | earlier | `first_break_found` | crossing `SC020` `PGmc Final Z Deletion` | 22 | 1 | 1 | `confirms_default_broad_far_break` | broad/far rather than local; representative failure: `rest` |
| `SC043` | earlier | `first_break_found` | crossing `SC042` `PWGmc Surviving Bimoric O Unrounding` | 1 | 1 | 1 | `confirms_default_local_break` | representative failure: `rest` |
| `SC044` | earlier | `first_break_found` | crossing `SC043` `Anglo Frisian Brightening` | 1 | 29 | 1 | `confirms_default_local_break` | many changed outputs, but only one newly failing row: `slay` |
| `SC045` | earlier | `first_break_found` | crossing `SC044` `OE Breaking` | 1 | 12 | 12 | `confirms_default_local_break` | representative failures: `fee`, `fight`, `flax`, `knight`, `laugh` |
| `SC046` | earlier | `first_break_found` | crossing `SC043` `Anglo Frisian Brightening` | 3 | 20 | 19 | `confirms_default_broad_far_break` | broad/far or non-local rather than adjacent; representative failures: `bake`, `fare`, `flask`, `grave`, `haw` |
| `SC047` | earlier | `first_break_found` | crossing `SC034` `OE Aw Long Diphthong` | 13 | 1 | 1 | `confirms_default_broad_far_break` | broad/far rather than local; representative failure: `straw` |
| `SC048` | earlier | `first_break_found` | crossing `SC047` `OE Heavy Syllable Nasal Apocope` | 1 | 87 | 87 | `confirms_default_local_break` | large local break; representative failures: `bake`, `begin`, `believe`, `bind`, `bore` |

## Main interpretation

This batch differs from the earlier expanded-PWGmc mini-batches in one striking way: **all eight rows are positive first-break rows**.

### 1. Confirmed default-profile local breaks

Four rows still confirm default-profile local chronology relations:

1. `SC043` earlier across `SC042`, with `rest`
2. `SC044` earlier across `SC043`, with `slay`
3. `SC045` earlier across `SC044`, with `fee`, `fight`, `flax`, `knight`, and `laugh`
4. `SC048` earlier across `SC047`, with a large failure set including `bake`, `begin`, `believe`, `bind`, and `bore`

`SC044` is worth separating from the others: crossing `SC043` changes many outputs, but only one row becomes newly failing. So the effect is wide, but the actual new-failure signal remains narrow.

### 2. Confirmed default-profile broad/far or non-local breaks

Four rows should be treated as broad/far or otherwise non-local constraints, not as local adjacency evidence:

1. `SC041` earlier across `SC020`, producing a large broad/far break with `67` changed outputs and `64` new failures
2. `SC042` earlier across `SC020`, with `rest`
3. `SC046` earlier across `SC043`, with `bake`, `fare`, `flask`, `grave`, and `haw`
4. `SC047` earlier across `SC034`, with `straw`

So this batch adds more positive default-profile confirmations, but it does **not** add any new internal-PWGmc break of the `SC031` / `SC033` type.

### 3. No new negative or internal-PWGmc cases

Unlike the previous mini-batches:

1. no row in `SC041` through `SC048` is a new `strengthened_negative_evidence` case;
2. no row in this batch is a new `expanded_internal_pwgmc_break` case;
3. `SC041` and `SC048` are the two large-effect rows, but they still remain interpretable within the already known default-profile broad/far or local classes.

## Concrete examples from the committed failures TSV

All examples below are taken directly from the committed expanded-profile failures TSV.

1. `SC041` earlier across `SC020`
   - `beard`: PGmc `*bárdaz` > expected OE `beard`, variant `bearda`
   - `bosom`: PGmc `*bōsmaz` > expected OE `bōsm`, variant `bōsma`
   - `bottom`: PGmc `*búttmaz` > expected OE `botm`, variant `botma`
   - `calf`: PGmc `*kálbaz` > expected OE `ċealf`, variant `ċealfa`
   - `coat`: PGmc `*rúkkaz` > expected OE `rocc`, variant `rocca`
2. `SC042` earlier across `SC020`
   - `rest`: PGmc `*rástōz` > expected OE `ræste`, variant `rasta`
3. `SC043` earlier across `SC042`
   - `rest`: PGmc `*rástōz` > expected OE `ræste`, variant `rasta`
4. `SC044` earlier across `SC043`
   - `slay`: PGmc `*sláxaną` > expected OE `slēan`, variant `sleaan | slēaan`
5. `SC045` earlier across `SC044`
   - `fee`: PGmc `*féxu` > expected OE `feoh`, variant `fehu`
   - `fight`: PGmc `*féxtaną` > expected OE `feohtan`, variant `fehtan`
   - `flax`: PGmc `*fláxsą` > expected OE `fleax`, variant `flæhs`
   - `knight`: PGmc `*knéxtaz` > expected OE `cniht`, variant `cneht`
   - `laugh`: PGmc `*xláxjaną` > expected OE `hliehhan`, variant `hlehhan`
6. `SC046` earlier across `SC043`
   - `bake`: PGmc `*bákaną` > expected OE `bacan`, variant `bæcan`
   - `fare`: PGmc `*fáraną` > expected OE `faran`, variant `færan`
   - `flask`: PGmc `*fláskōn` > expected OE `flasce`, variant `flæsċe`
   - `grave`: PGmc `*grábaną` > expected OE `grafan`, variant `græfan`
   - `haw`: PGmc `*xágô` > expected OE `haga`, variant `hæga`
7. `SC047` earlier across `SC034`
   - `straw`: PGmc `*stráwą` > expected OE `strēaw`, variant `stræw`
8. `SC048` earlier across `SC047`
   - `bake`: PGmc `*bákaną` > expected OE `bacan`, variant `bacen`
   - `begin`: PGmc `*bigínnaną` > expected OE `beġinnan`, variant `beġinnen`
   - `believe`: PGmc `*galáubijaną` > expected OE `ġelīefan`, variant `ġelīefen`
   - `bind`: PGmc `*bíndaną` > expected OE `bindan`, variant `binden`
   - `bore`: PGmc `*búrōjaną` > expected OE `borian`, variant `borien`

## Profile warning

These rows remain **expanded-profile** results. They should not overwrite, silently revise, or be folded directly into the default chronology-card corpus, default first-break TSV corpus, or default graph export.

This batch also does not change the interpretation that expanded-profile evidence remains a separate review layer from the default 70-card corpus.

## Recommendation

Do **not** jump immediately to a much larger next batch.

The next manual expanded-profile step should be either:

1. a smaller `SC049` through `SC058` **earlier-only** mini-batch; or
2. another light audit of the expanded-profile index first, if the separate review layer is starting to feel unwieldy.

Do **not** move to later-direction expanded-profile tests yet.
