# Reviewer checklist for Old English lexeme entries

Use this shared checklist before treating a draft as accepted. Do not copy it
into a per-entry pass table. Human judgement cannot be automated; record only
unique conclusions, unresolved premises and checked-source limits in the ledger
or existing memo.

Mechanical coverage is supplied by `test_repository_cleanup.py` (model metadata,
bibliography keys and historical migration), the citation/semantic/index checks,
and `validate_oe_lexeme_report_assembly.py` (certification and selected identities).
Run the canonical refresh and the validation commands in `docs/CI_VALIDATION.md`.
A passing check never certifies a scholarly claim or uninspected source image.

## Genre and scope

- [ ] Does the entry read like a **book entry about the word**?
- [ ] Does it avoid **project autobiography**?
- [ ] Is the prose about linguistic history rather than repository history?
- [ ] Is the entry as short as the case permits, rather than inflated to match a
      harder entry?

## Evidence and forms

- [ ] Does the entry give **actual source forms**?
- [ ] Does it avoid vague statements such as “the handbooks disagree” unless the
      forms are immediately named?
- [ ] Does it distinguish **attested**, **normalized**, **reconstructed**, and
      **project-selected** forms?
- [ ] Does it establish the **Old English evidence before the paradigm
      comparison**?
- [ ] If an OE target is reconstructed, is that stated explicitly?

## Citations

- [ ] Do all citations use bibliography keys present in `docs/refs.bib`?
- [ ] Are sources cited in prose rather than hidden behind local file names?
- [ ] If a cited source lacks a key, is that problem recorded in the ledger
      rather than silently patched over?

## Claims and certainty

- [ ] Does the entry distinguish **documented outputs** from
      **inferred/expected outputs**?
- [ ] If a comparison is manual, is it labeled as manual?
- [ ] Does the entry avoid overstating certainty?
- [ ] Does it avoid inventing unattested forms or automatic probe results?

## Style

- [ ] Does it avoid repetitive “not X but Y” rhetorical negation?
- [ ] Does it avoid generic summary endings?
- [ ] Does it avoid a conclusion unless there is a strong reason to include one?
- [ ] Does it avoid unnecessary project-facing terms after the brief metadata
      section?

## Forbidden project-facing content in the book-style prose

- [ ] Does it avoid mentioning packets, DEV_NOTES, backlog, manifest,
      implementation log, or project history in the final entry prose?
- [ ] Are local tools discussed only in the ledger or research memo?

## Evidence record

- [ ] Does the ledger retain the source pages, attribution and actual checks?
- [ ] Does it state what was **not** checked when relevant?
- [ ] Are scientific adoption and publication certification kept separate?
