# SC004-SC006 backend promotion 01 report

## Reports created

1. `Germanic/docs/sound_changes/change_reports/full/004-pwgmc-ai-monophthongization.md`
2. `Germanic/docs/sound_changes/change_reports/full/005-nwgmc-a-to-u-before-m.md`
3. `Germanic/docs/sound_changes/change_reports/full/006-pwgmc-early-i-apocope.md`

## Literature dossiers created

1. `Germanic/docs/sound_changes/literature_dossiers/004-pwgmc-ai-monophthongization.dossier.md`
2. `Germanic/docs/sound_changes/literature_dossiers/005-nwgmc-a-to-u-before-m.dossier.md`
3. `Germanic/docs/sound_changes/literature_dossiers/006-pwgmc-early-i-apocope.dossier.md`

## Book dossiers created

1. `Germanic/docs/sound_changes/book_dossiers/004-pwgmc-ai-monophthongization.book-dossier.md`
2. `Germanic/docs/sound_changes/book_dossiers/005-nwgmc-a-to-u-before-m.book-dossier.md`
3. `Germanic/docs/sound_changes/book_dossiers/006-pwgmc-early-i-apocope.book-dossier.md`

## Source-support status

### SC004

1. The strongest recovered source support is for the **unstressed** `*ai` monophthongization, especially word-final and ending material [@RingeTaylor2014, pp. 40--41; @Fulk2018, §5.2].
2. The broader CAPR packaging of nonfinal `*ai > *ā` is historically plausible but less explicitly supported by the source passages gathered in this pass.
3. SC004 is therefore source-backed enough for a backend report and dossier, but not yet fully source-complete.

### SC005

1. Campbell, Sievers/Brunner, and Fulk all support the underlying pre-`m` raising in unstressed endings [@Campbell1959, §331(6); @SieversBrunner1965, §44; @Fulk2018, §5.2].
2. The retrieved source discussion is mostly morphological rather than centered on the single lexical witness `shoulder`.
3. The source base is usable for backend documentation but still leaves the exact historical stage label unresolved.

### SC006

1. Source support is comparatively good. Sievers/Brunner and Ringe/Taylor both support the early loss of final `*i` before later umlaut can act [@SieversBrunner1965, §§145--146; @RingeTaylor2014, p. 141].
2. Campbell's `dugup / geogup` discussion aligns with the same historical phenomenon [@Campbell1959, §332].
3. The present source pass is strongest for suffixal evidence and the `youth` family, not yet for every individual trace lexeme.

## SC005 stage-label / human-review status

1. SC005 still carries the inventory flag `needs_human_review=yes`.
2. The current sources fit at least a wider North/West-Germanic inflectional development and do not yet force a clean standalone `NWGmc` label.
3. That issue was preserved explicitly in the report and dossier layer and was **not** smoothed away.

## Chronology-harness decision

1. **No new harness script was needed.**
2. SC004-SC006 can be tested by the **ordinary existing first-break runner**:
   - `Germanic/tools/sound_change_order_sensitivity.py`
   - with `--mode first-break`
   - and `--order-profile expanded-pwgmc`
3. This is possible because the existing runner already supports an in-memory expansion of bundled `PWGmcChanges` into explicit SC004-SC013 component rules.

## Whether a harness was extended or created

1. No harness was extended.
2. No new wrapper script was created.
3. Instead, a run-book was added:
   - `Germanic/docs/sound_changes/order_tests/run_sc004_006_first_breaks_README.md`

## Dry-run result

Lightweight dry-run inspection was run through the ordinary runner:

```bash
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC004 --direction both --order-profile expanded-pwgmc --dry-run-order
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC005 --direction both --order-profile expanded-pwgmc --dry-run-order
python3 Germanic/tools/sound_change_order_sensitivity.py --mode first-break --change SC006 --direction both --order-profile expanded-pwgmc --dry-run-order
```

Observed result:

1. `SC004` resolves as position `1` in the expanded-PWGmc order profile.
2. `SC005` resolves as position `2`.
3. `SC006` resolves as position `3`.
4. Imports and order resolution succeeded.
5. No heavy crawl was run.

## Exact heavy commands for Nathan

See:

`Germanic/docs/sound_changes/order_tests/run_sc004_006_first_breaks_README.md`

The full commands are:

```bash
cd /Users/nathanhill/Code/capr-v3-working

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC004 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC005 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv

python3 Germanic/tools/sound_change_order_sensitivity.py \
  --mode first-break \
  --change SC006 \
  --direction both \
  --resume \
  --order-profile expanded-pwgmc \
  --first-break-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01.tsv \
  --first-break-changes-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_changes.tsv \
  --first-break-failures-output Germanic/docs/sound_changes/order_tests/summaries/order_sensitivity_first_break_expanded_pwgmc_sc004_006_01_failures.tsv
```

## Manifest update

1. `Germanic/docs/sound_changes/change_reports/report_manifest.tsv` was **not** updated.

### Exact blockers

#### SC004

1. No validated chronology card exists yet because no real first-break TSV output has been run.
2. The source layer for the broader nonfinal `*ai > *ā` side is still weaker than for the unstressed ending evidence.

#### SC005

1. No validated chronology card exists yet because no real first-break TSV output has been run.
2. The stage-label / `needs_human_review` issue remains unresolved.
3. The source discussion remains more morphological than lexical.

#### SC006

1. No validated chronology card exists yet because no real first-break TSV output has been run.
2. The source base is solid, but chronology still has to be computed from real TSV output before manifest promotion.

## Checks run and results

### Automated report-style audit

Command:

```bash
python3 Germanic/tools/audit_sound_change_report_style.py
```

Result:

1. Passed for the current manifest-backed report set.
2. As expected, the audit still scopes itself to manifest-listed rows and therefore does **not** automatically cover the new unmanifested SC004-SC006 reports.

### Manual style-standard check for SC004-SC006 reports

The three new reports were manually checked against `Germanic/docs/sound_changes/change_reports/STYLE_STANDARD.md`.

Result:

1. All three follow the required heading sequence:
   - `Historical formulation`
   - `Source tradition`
   - `CAPR implementation`
   - `Place in the cascade`
   - `Order evidence`
   - `Interpretation`
   - `Remaining cautions`
2. No manifest update or chronology-card creation was attempted without real first-break TSV output.

## Scope confirmations

1. No reader-facing chapters were created.
2. No production FST rules were changed.
3. No TSV lexical data were changed.
4. No files were added under `Germanic/docs/sound_changes/order_tests/chronology_cards/`.

## Next recommended step

1. Have Nathan run the heavy expanded-PWGmc first-break commands from `run_sc004_006_first_breaks_README.md`.
2. In the follow-up pass, convert those real TSV outputs into validated chronology cards for any of SC004-SC006 whose runs complete cleanly.
3. Revisit manifest promotion only after those validated chronology cards exist, with SC005's stage-label issue reviewed again in light of the chronology results.
