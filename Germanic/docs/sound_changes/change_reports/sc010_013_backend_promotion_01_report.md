# SC010-SC013 backend promotion 01 report

## Latest commit inspected

1. `93a8ee31 docs: add reader-facing SC007 and SC008`

## Files inspected

1. `Germanic/docs/sound_changes/reader_facing/reader_facing_local_section_17_report.md`
2. `Germanic/docs/sound_changes/reader_facing/reader_facing_manifest_coverage_05.md`
3. `Germanic/docs/sound_changes/change_reports/sc007_009_chronology_validation_01_report.md`
4. `Germanic/docs/sound_changes/change_reports/sc007_009_backend_promotion_01_report.md`
5. `Germanic/docs/sound_changes/order_tests/expanded_pwgmc_runner_mode.md`
6. `Germanic/docs/sound_changes/change_reports/STYLE_STANDARD.md`
7. `Germanic/docs/sound_changes/sound_change_inventory.tsv`
8. `Germanic/fsts/germanic.txt`
9. `docs/references/ringe_taylor_linguistic_history_vol2.txt`
10. `docs/references/legacy/fulk_comparative_grammar_early_germanic.txt`
11. `docs/references/campbell_old_english_grammar.txt`
12. `docs/refs.bib`

## Source evidence found for SC010

1. Fulk states that before `j` the change regularly applies to any consonant other than `r` after a short vowel [@Fulk2018, §6.15].
2. He gives a substantial lexical set including OE *scieppan*, *settan*, *lecgan*, *fremman*, *wennan*, and *sellan* [@Fulk2018, §6.15].
3. This is the strongest and clearest source base in the present SC010-SC013 batch.

## Source evidence found for SC011

1. Ringe and Taylor state directly that after the loss of unstressed `*a` and `*ą`, preceding postconsonantal `*j` became syllabic `*i` [@RingeTaylor2014, p. 46].
2. Their examples include `*harjaz > *hari`, `*andijaz > *andi`, and `*rikija > *riki` [@RingeTaylor2014, p. 46].
3. The main weakness is not the source layer but the current trace layer, which still shows zero compact-trace occurrences.

## Source evidence found for SC012

1. Ringe and Taylor say that word-internal `*lþ` became `*ld` by regular sound change in northern WGmc and illustrate the outcome with `fealdan`, `beald`, `wuldor`, and `gylden` [@RingeTaylor2014, pp. 170--171].
2. Campbell gives a compatible West-Germanic-facing formulation with examples such as `fealdan`, `wuldor`, `beald`, `gold`, and `feld` [@Campbell1959, §414].
3. The source support for the phenomenon is real, but the stage-label wording is narrower than the inventory's plain PWGmc label.

## Source evidence found for SC013

1. Ringe and Taylor state directly that in PWGmc the non-coronal voiced obstruents continued to exhibit allophony, but `*d` became a stop in all positions [@RingeTaylor2014, p. 43].
2. This is very strong systemic support, though the present lexical dossier is still comparatively compact.

## Dry-run order result for SC010

Command:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC010 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC010 target_rule=PWGmcJGemination`
2. `007    SC010    PWGmcJGemination    PWGmc J Gemination target`

## Dry-run order result for SC011

Command:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC011 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC011 target_rule=PWGmcSyllabicJ`
2. `008    SC011    PWGmcSyllabicJ    PWGmc Syllabic J target`

## Dry-run order result for SC012

Command:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC012 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC012 target_rule=PWGmcLThVoicing`
2. `009    SC012    PWGmcLThVoicing    PWGmc L Th Voicing target`

## Dry-run order result for SC013

Command:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC013 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed output:

1. `order_profile=expanded-pwgmc total_rules=83 target_change=SC013 target_rule=PWGmcDentalHardening`
2. `010    SC013    PWGmcDentalHardening    PWGmc Dental Hardening target`

## Whether a new harness was needed

1. No new harness was needed.
2. The ordinary runner already exposes SC010-SC013 cleanly through `--order-profile expanded-pwgmc`.

## Exact first-break commands for Nathan to run next

See:

`Germanic/docs/sound_changes/order_tests/run_sc010_013_first_breaks_README.md`

The heavy commands are:

```bash
cd /Users/nathanhill/Code/capr-v3-working

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC010 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC011 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC012 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC013 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc010_013_01_failures.tsv
```

## Reports created

1. `Germanic/docs/sound_changes/change_reports/full/010-pwgmc-j-gemination.md`
2. `Germanic/docs/sound_changes/change_reports/full/011-pwgmc-syllabic-j.md`
3. `Germanic/docs/sound_changes/change_reports/full/012-pwgmc-l-th-voicing.md`
4. `Germanic/docs/sound_changes/change_reports/full/013-pwgmc-dental-hardening.md`

## Literature dossiers created

1. `Germanic/docs/sound_changes/literature_dossiers/010-pwgmc-j-gemination.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/011-pwgmc-syllabic-j.dossier.md`
3. `Germanic/docs/sound_changes/literature_dossiers/012-pwgmc-l-th-voicing.dossier.md`
4. `Germanic/docs/sound_changes/literature_dossiers/013-pwgmc-dental-hardening.dossier.md`

## Book dossiers created

1. `Germanic/docs/sound_changes/book_dossiers/010-pwgmc-j-gemination.book-dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/011-pwgmc-syllabic-j.book-dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/012-pwgmc-l-th-voicing.book-dossier.md`
4. `Germanic/docs/sound_changes/book_dossiers/013-pwgmc-dental-hardening.book-dossier.md`

## Runbook created

1. `Germanic/docs/sound_changes/order_tests/run_sc010_013_first_breaks_README.md`

## Checks run and results

### Automated style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed for the current manifest-backed report set.
2. The new SC010-SC013 reports are not yet manifest-listed, so the audit does not cover them automatically.

### Manual heading-order check

Command:

```bash
grep -n "^#### " \
  Germanic/docs/sound_changes/change_reports/full/010-pwgmc-j-gemination.md \
  Germanic/docs/sound_changes/change_reports/full/011-pwgmc-syllabic-j.md \
  Germanic/docs/sound_changes/change_reports/full/012-pwgmc-l-th-voicing.md \
  Germanic/docs/sound_changes/change_reports/full/013-pwgmc-dental-hardening.md
```

Result:

1. All four reports contain the required seven subsection headings in the standard order.

### Manual style-tripwire grep

Command:

```bash
grep -n "reader-facing\|promot\|workflow\|project\|scaffold\|assembled\|book-facing" \
  Germanic/docs/sound_changes/change_reports/full/010-pwgmc-j-gemination.md \
  Germanic/docs/sound_changes/change_reports/full/011-pwgmc-syllabic-j.md \
  Germanic/docs/sound_changes/change_reports/full/012-pwgmc-l-th-voicing.md \
  Germanic/docs/sound_changes/change_reports/full/013-pwgmc-dental-hardening.md
```

Result:

1. no matches

## Scope confirmations

1. `report_manifest.tsv` was not updated.
2. No chronology cards were created.
3. No reader-facing chapters were created.
4. No local section 18 was created.
5. No FST rules were changed.
6. No lexical TSV data were changed.

## Sharp handoff for the next task

1. Once Nathan has run the heavy SC010-SC013 first-break commands, the next agent should validate the TSVs, create chronology cards only from real TSV evidence, decide whether any of SC010-SC013 are promotable, and only then update the manifest/scaffold/index files.
