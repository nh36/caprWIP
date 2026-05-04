# Research memo — 2300 wool / wull

## Starting point

- **ID / concept / counterpart:** 2300, **wool**, **wull**.
- **TSV values:** `PROTO *wúllō`, `PROTOFORM *wúllō`, `DERIVATION_CLASS unexplained_unmodelled`, note pointing to DEV_NOTES §17.10.34.
- **Immediate issue:** the current FST derives regular **woll**, while the row targets **wull**.
- **Workflow distinction:** for this row the cognate-set proto and the project input form happen to be the same (`*wúllō`), but they still need to be distinguished from the OE target. The OE-side philological question is further complicated by handbook and dictionary variation between **wull** and **wulle**.

## Packet evidence assessment

**Authoritative/current in the packet:**
- The live TSV row and the packet’s compact derivation trace are current for the project state: they correctly show `*wúllō -> woll` as the regular modeled output and `wull` as the target mismatch.
- The packet’s high-confidence DEV_NOTES excerpts from §17.10.34 / §17.10.34a are current and decisive: they state that `wull` is to be treated as a documented lexical exception, not as a rule bug and not as a paradigm-cell retargeting case.
- The `oe_known_problems.tsv` hit is current and confirms that the row is already tracked as a `u_lowering_near_labial` wontfix item.

**Useful background:**
- The packet’s older literature snippets (Bülbring, Luick, R/T, Brunner) are useful for framing the exception cluster and for showing that `wulle`/`wull` belongs to the same long-recognized retention group as `wulf`, `full`, `fugol`, and `bucca`.
- The packet’s `notable_findings.md` hit is useful background because it records the project’s broader reasoning about why a categorical labial-blocking rule is untenable.

**Stale or superseded:**
- The packet’s “possibly stale or diagnostic” DEV_NOTES hits are genuinely stale project history, especially the older `*wúllō -> woll (expected wull)` mismatch snapshots and the 2026-04-05 note treating row 2300 as a generic “degemination + vowel” problem. Those are superseded by §17.10.34 and especially §17.10.34a.
- The earlier §17.10.34 plan to solve four related rows by switching to high-vowel paradigm cells is also superseded for the cluster as a whole. For `wull`, even the original section already said the row had to be left alone; §17.10.34a strengthens that conclusion by rejecting the paradigm-cell escape more generally.

**Irrelevant or misleading for this memo:**
- Packet hits from `ws_vs_anglian_dialect_differences.md` and `widuwe-u-preservation.md` are not direct evidence for `wull`; they mainly guard against overgeneralizing other umlaut/lowering discussions into this lexeme.
- The packet’s “paradigm probe required” note is a workflow reminder, not evidential support by itself.

## Additional repo research

Beyond the packet I checked:
- `Germanic/docs/DEV_NOTES.md` at the early u-lowering-exception discussion (lines 63-140), the current implementation decision around §17.10.34 / §17.10.34a, and the older superseded 2026-04-05 mismatch note.
- `Germanic/docs/analysis/notable_findings.md` §2, including the follow-up discussion that mentions `OE wulle 'wool' could have levelled from *wullō` as a possibility discussed in the literature.
- `Germanic/docs/dossiers/widuwe-u-preservation.md`, which is not about `wull` directly but does explicitly warn against turning labial adjacency into a formal rule; that supports treating the wool case as lexical rather than rule-based.
- `Germanic/docs/analysis/ws_vs_anglian_dialect_differences.md`, whose packet hits proved irrelevant to this row.
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`, `ringe_vol1_pie_to_pgmc.txt`, `campbell_old_english_grammar.txt`, `brunner_1965_altenglische_grammatik.txt`, `bulbring_altenglisches_elementarbuch.txt`, `luick_historische_grammatik.txt`, and `clark_hall_concise_anglo_saxon_dictionary.vision.txt`.
- `Germanic/data/old_english_wiktionary.tsv` and `Germanic/data/oe_known_problems.tsv`.

Main results of that repo research:
- Current project authority is consistent: the row is meant to stay a documented exception.
- The handbooks often cite **wulle**, while Ringe vol. 1 and Clark Hall also support **wull** as an OE citation/headword form; this is a real philological normalization issue, not a reason by itself to rewrite the row.
- I found **no pilot lexeme report** for this lexeme; there is only the packet.

## Reconstruction and early-stage forms

- **Cognate-set proto:** `PROTO *wúllō` is the etymological headword used for the Germanic cognate set.
- **Project input form:** `PROTOFORM *wúllō` is the specific FST input for this row. Unlike the four masculine exception rows discussed in DEV_NOTES, there is no better cell-specific substitute here; the ō-stem paradigm offers no high-vowel cell that would block u-lowering without creating some other problem.
- **Regular modeled development:** the trace `*wúllō -> *wóllō -> *wóllu -> woll` is the project’s regular phonological outcome, and the packet/DEV_NOTES are explicit that this is the correct regular result.
- **OE target form:** the row’s target is **wull**, i.e. the project’s chosen OE counterpart for the lexeme.

So the crucial distinction is:
1. `PROTO` = cognate-set proto headword;
2. `PROTOFORM` = the FST input actually used for the OE row;
3. `COUNTERPART` = the OE target represented by the row.

For this lexeme, (1) and (2) coincide, but (3) does not follow by regular sound change.

## Old English philology

- The lexical exception itself is well supported. Bülbring, Luick, Brunner, and R/T all treat wool alongside other OE `u`-retention cases where regular lowering would predict `o`.
- The **headword/citation-form issue is mixed**:
  - Campbell and Brunner regularly cite **wulle** as the weak feminine noun.
  - Ringe vol. 1 explicitly gives **OE wull** as the OE outcome of PGmc `*wullō`, and his index separately lists **wulle** as an accusative form.
  - Clark Hall likewise has an entry `wull f. 'wool'` with `wulle` cross-referenced.
- That means the repo should not treat `wulle` as automatically the “real” form and `wull` as an error. Better: **wull** is a legitimate OE citation/headword normalization in repo-local sources, while **wulle** is also a real weak-noun form used heavily in handbook discussion.
- Philologically, then, the row is not primarily about whether the lexeme existed as `wull` versus `wulle`; it is about the root-vowel problem **u vs. expected o**. The memo for the eventual report should mention the weak-noun `wulle` tradition so that readers do not mistake the row’s bare `wull` target for a claim that only that surface form is attested.

## Project problem and solution

The project problem is not reconstruction of PGmc `*wullō`; that part is stable. The problem is that the project’s regular chronology correctly derives **woll**, while the OE lexeme is represented with **u**.

The current solution in the repo is the right one:
- keep the row as an explicit documented exception;
- do **not** alter the FST to add a labial/geminate blocker;
- do **not** invent a paradigm-cell retargeting workaround;
- explain in prose that `wull`/`wulle` belongs to the lexical cluster where OE preserves `u` against the regular outcome.

This is exactly the kind of row where the project should distinguish **regular model output** from **attested OE lexeme** rather than forcing them to match.

## Paradigm probe

A paradigm probe **is required**, but it is a negative-control probe, not a search for a rescuing cell.

Because the packet says no built-in spec exists yet, the missing probe should test the feminine ō-stem cells that matter for the “no escape hatch” claim:
- **nom.sg.** `*wúllō`
- **dat.sg.** `*wúllai`
- **acc.sg. / gen.pl.-type ǭ cell** `*wúllǭ`
- **gen.sg. / nom.-acc.pl.-type ōz cell** `*wúllōz`
- **dat.pl.** `*wúllōmaz`
- **instr.pl.** `*wúllōmiz`

If desired, duplicated syncretic cells can be folded together, but the probe should make explicit that every available ō-stem ending remains a back-vowel environment and therefore fails to supply the high-vowel blocker available in the four masculine comparison rows.

## Recommended final report

Recommend a short `### Lexeme report` that says: regular development of `*wúllō` gives modeled **woll**; OE **wull** (with handbook weak-noun form **wulle**) is a documented lexical exception in the NWGmc/OE u-lowering cluster; no paradigm-cell retargeting solution exists for this ō-stem, so the row should be documented rather than normalized away.

## Data-change recommendations

- **TSV `PROTO`:** **no change**. `*wúllō` remains the correct cognate-set proto headword in repo usage.
- **TSV `PROTOFORM`:** **no change**. There is no better cell-specific input that makes the row regular.
- **TSV `COUNTERPART`:** **no change recommended now**. Repo-local evidence supports `wull` as an acceptable OE citation/headword normalization, even though handbook discussion often uses `wulle`.
- **TSV `DERIVATION_CLASS`:** **change recommended** from `unexplained_unmodelled` to **`known_unmodelled`**. The row is not unexplained in project terms anymore: it is a documented, already-classified lexical exception with a known mismatch category and an `oe_known_problems.tsv` entry.
- **TSV `NOTE`:** **optional minor cleanup only**. The current note is substantively good; if touched, it should only add a brief philological clarification that handbook discussion often cites weak-noun `wulle` while the row keeps normalized `wull`.
- **`oe_known_problems.tsv`:** **no change**. The existing `*wúllō` `u_lowering_near_labial` entry is appropriate.
- **`DEV_NOTES` / dossier text:** **no substantive change**. Current DEV_NOTES already preserve both the current decision and the superseded history. No dossier cleanup is required for this memo, though a future editorial pass could label the old 2026-04-05 `wool` mismatch note more explicitly as superseded.
