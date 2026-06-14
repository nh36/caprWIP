# SC007-SC009 backend promotion 01 report

## Files inspected

1. `.github/copilot-instructions.md`
2. `docs/AGENTS.md`
3. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc_runner_mode.md`
4. `Germanic/fsts/germanic.txt` (the SC007-SC009 region inside `PWGmcChanges`)
5. `Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_04.md`
6. `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_16_report.md`
7. `Germanic/docs/sound_changes/change_reports/sound_change_half_scaffold.tsv`
8. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv`
9. `Germanic/docs/sound_changes/sound_change_inventory.tsv`
10. `docs/references/ringe_taylor_linguistic_history_vol2.txt`
11. `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt`
12. `docs/references/campbell_old_english_grammar.txt`
13. `docs/refs.bib`

## Current-state confirmations

1. Local section 16 is the current reader-facing build target.
2. SC004 and SC006 are now reader-facing.
3. SC005 remains deliberately outside the manifest.
4. SC007-SC013 remain the next internal PWGmc rules to prepare.
5. This pass is backend preparation only.

## Source evidence found for SC007

1. Ringe and Taylor state that surviving bimoric long `ō` became PWGmc `a` word-finally and before word-final `r` [@RingeTaylor2014, pp. 58--59].
2. Their key examples are `four` and `water` [@RingeTaylor2014, pp. 58--59].
3. Fulk gives the same broad historical framing for `ō` before final `r` in West Germanic [@Fulk2018, §5.3].
4. The evidence is good but narrow, so the report keeps the environment-specific caution explicit.

## Source evidence found for SC008

1. Ringe and Taylor describe the assimilation of `*zw` and `*dw` to `*ww` as a Proto-West-Germanic innovation [@RingeTaylor2014, pp. 56--57].
2. Their historical examples are `four`, `you (dat.pl.)`, and `your (pl.)` [@RingeTaylor2014, pp. 56--57].
3. They also note that there is essentially one clear lexical example of each input cluster, even though the change itself is historically secure [@RingeTaylor2014, pp. 56--57].

## Source evidence found for SC009

1. Ringe and Taylor describe a change of `*ijo` to `*iu` in the `friend` family [@RingeTaylor2014, p. 62].
2. The same passage warns that the `*ijo` sequence is unique enough that broader generalization is inadvisable [@RingeTaylor2014, p. 62].
3. This makes SC009 source-backed but unusually narrow.

## Dry-run order result for SC007

Command run:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC007 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC007 target_rule=PWGmcFinalOrLowering`
2. `004    SC007    PWGmcFinalOrLowering    PWGmc Final Or Lowering target`

## Dry-run order result for SC008

Command run:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC008 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC008 target_rule=PWGmcCoronalWAssimilation`
2. `005    SC008    PWGmcCoronalWAssimilation    PWGmc Coronal W Assimilation target`

## Dry-run order result for SC009

Command run:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC009 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC009 target_rule=PWGmcIjContraction`
2. `006    SC009    PWGmcIjContraction    PWGmc Ij Contraction target`

## Whether a new harness was needed

1. No new harness was needed.
2. The ordinary runner already exposes SC007-SC009 cleanly through `--order-profile expanded-pwgmc`.

## Exact first-break commands for Nathan to run next

See:

`Germanic/docs/sound_changes/order_tests/run_sc007_009_first_breaks_README.md`

The heavy commands are:

```bash
cd /Users/nathanhill/Code/capr-v3-working

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC007 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC008 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC009 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc007_009_01_failures.tsv
```

## Reports created

1. `Germanic/docs/sound_changes/change_reports/full/007-pwgmc-final-or-lowering.md`
2. `Germanic/docs/sound_changes/change_reports/full/008-pwgmc-coronal-w-assimilation.md`
3. `Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md`

## Literature dossiers created

1. `Germanic/docs/sound_changes/literature_dossiers/007-pwgmc-final-or-lowering.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/008-pwgmc-coronal-w-assimilation.dossier.md`
3. `Germanic/docs/sound_changes/literature_dossiers/009-pwgmc-ij-contraction.dossier.md`

## Book dossiers created

1. `Germanic/docs/sound_changes/book_dossiers/007-pwgmc-final-or-lowering.book-dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/008-pwgmc-coronal-w-assimilation.book-dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/009-pwgmc-ij-contraction.book-dossier.md`

## Runbook created

1. `Germanic/docs/sound_changes/order_tests/run_sc007_009_first_breaks_README.md`

## Checks run and results

### Automated style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed for the current manifest-backed report set.
2. The new SC007-SC009 reports are not yet manifest-listed, so the audit does not cover them automatically.

### Manual style-tripwire grep

Command:

```bash
grep -n "reader-facing\\|promot\\|workflow\\|project\\|scaffold\\|assembled\\|book-facing" \
  Germanic/docs/sound_changes/change_reports/full/007-pwgmc-final-or-lowering.md \
  Germanic/docs/sound_changes/change_reports/full/008-pwgmc-coronal-w-assimilation.md \
  Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md
```

Result:

1. no matches

### Manual heading-order check

Command:

```bash
grep -n "^#### " \
  Germanic/docs/sound_changes/change_reports/full/007-pwgmc-final-or-lowering.md \
  Germanic/docs/sound_changes/change_reports/full/008-pwgmc-coronal-w-assimilation.md \
  Germanic/docs/sound_changes/change_reports/full/009-pwgmc-ij-contraction.md
```

Result:

1. All three reports contain the required seven subsection headings in the standard order.

## Manifest and chronology-card status

1. `report_manifest.tsv` was **not** updated.
2. No chronology cards were created.

## Scope confirmations

1. No reader-facing chapters were created.
2. No production FST rules were changed.
3. No lexical TSV data were changed.

## Sharp handoff for the next task

Once Nathan has run the heavy `SC007`–`SC009` first-break commands from `run_sc007_009_first_breaks_README.md`, the next pass should:

1. validate the resulting TSVs;
2. create chronology cards **only from real TSV evidence**;
3. decide whether any of SC007, SC008, or SC009 are promotable;
4. and only then update `report_manifest.tsv`, `sound_change_half_scaffold.tsv`, `chronology_card_index.tsv`, `sound_change_order_sensitivity.tsv`, and `sound_change_book_dossier_inventory.tsv` as needed.
