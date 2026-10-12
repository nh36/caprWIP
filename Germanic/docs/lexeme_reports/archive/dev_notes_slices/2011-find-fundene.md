---
row_id: 2011
concept: find
counterpart: fundene
proto: *fínθaną
protoform: *fúnðanǭ
derivation_class: late_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2011-find-fundene.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2011-find-fundene.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2011 find / fundene

## Current row state

- CONCEPT: `find`
- COUNTERPART: `fundene`
- PROTO: `*fínθaną`
- PROTOFORM: `*fúnðanǭ`
- DERIVATION_CLASS: `late_analogy`
- Live TSV note (abridged): row 2011 now treats the target as the attested strong past-participle **acc.sg.m.** cell `fundene`; the note cites Bosworth-Toller for the form itself, cites Hall's `tō-fundennes` as corroborative participial-stem evidence, states that regular Verner `*ð -> *d` and heterosyllabic `-an- -> -en-` are both present in this cell, and explicitly classifies bare nom.sg. `funden` as analogical after Campbell, Luick, and Brunner.
- `oe_known_problems.tsv`: no row-level entry for `*fínθaną`, `*fúnðanǭ`, `fundene`, or `funden`.
- `report_manifest.tsv`: no manifest entry for row 2011.
- Packet / memo state: both supporting files already point to the same three-level structure that the slice needs to preserve — cognate-set proto `*fínθaną`, row-level input `*fúnðanǭ`, and attested OE target `fundene`.
- Important metadata caution: one DEV_NOTES implementation table temporarily rewrote both `PROTOFORM` **and** `PROTO` to `*fúnðanǭ`, but the live TSV has since restored the necessary distinction. For current row policy, `PROTO = *fínθaną` remains the cognate-set headword, while `PROTOFORM = *fúnðanǭ` is the selected inflected input cell [DEV_NOTES:line-25754-25761].

## Development-note summary

The row's entire DEV_NOTES history is driven by one methodological demand: do **not** derive OE `findan` from the infinitive if the infinitive is already analogically levelled. The first major note established the consonantal side of the problem. Fulk is quoted for the standard expectation that Verner voicing belongs only in the **preterite plural** and **past participle** of strong verbs, not in the infinitive; Ringe-Taylor are quoted even more directly on this lexeme: `"PGmc *finþan 'to find' ... > *fīþan > OS fīðan (beside findan with voiced VL alternant levelled, cf. OE findan, OF finda)"` [DEV_NOTES:line-6992-7008; DEV_NOTES:line-7026-7030; @Fulk2018, §12.17; @RingeTaylor2014, §5.1.1]. That early note was right on the big point: OE lemma `findan` contains levelled `d`, whereas the regular voiced alternant belongs to participial or preterite-plural cells.

That same March note, however, stopped one step too early. It moved the row away from infinitive `*finþaną -> findan` and toward past participle `*funðanăz -> funden`, because that cell regularizes the **consonant**: no NSL before voiceless `*þ`, and regular Verner `*ð` hardening to `*d` after the nasal [DEV_NOTES:line-7101-7219; DEV_NOTES:line-7267-7337]. In that project state, `funden` was treated as the fully lautgesetzlich endpoint. Later row work shows that this was only half-correct. The participial strategy was sound, but the specific nominative singular chosen there was still morphologically levelled on the **vocalic** side.

The later April audit is therefore the controlling correction. DEV_NOTES re-opened the row after the `*ă/*a` migration exposed that the earlier `*funðanăz -> funden` success had depended on a load-bearing notation hack rather than on a defensible account of syllable structure. The note explicitly rejects restoring the breve just to keep the old outcome alive: `"We should *not* re-introduce the breve on row 2011. There is only one unaccented schwa-like low vowel at this stage, and we should spell it one way."` [DEV_NOTES:line-25144-25159]. That is an important current constraint: the row may use a different **paradigm cell**, but it should not smuggle syllabification into the spelling of unstressed vowels.

Once the source audit is sharpened, the handbook consensus becomes decisive and citation-dense enough to replace the older note. Campbell is quoted explicitly: `"This is the origin of OE -en when absence of umlaut shows it not to be from -in, and when it is not due to parasiting, e.g. strong pass. parts. in -en (still often -an in Ep.)"` [DEV_NOTES:line-25406-25421; @Campbell1959, §334]. Luick is equally explicit that the nominative is remodelled after inflected forms: `"*hebanæs, -æ ... und danach auch nom. hefæn ... und namentlich die starken part. prät."` [DEV_NOTES:line-25423-25438; @Luick1914, §301.3]. Brunner states the same point in even plainer morphological terms, saying OE `-en` from Germanic `-an` proceeds `"unter Verallgemeinerung der in flektierten Kasus eingetretenen Entwicklung"` [DEV_NOTES:line-25439-25464; @SieversBrunner1965, §366 Anm. 3]. The slice should preserve that consensus exactly, because it is the row's main authority: bare `funden` is not the regular sound-law continuation of nominative `*fúnðanaz`; it is an analogical nominative generalized from oblique cells.

Ringe-Taylor are not quoted as directly on this nominative issue, but DEV_NOTES still uses them as chronology control. Their account distinguishes unstressed `*a` before a nasal **in the syllable coda** from `*a` before an **intervocalic nasal**, and the note argues that their stated PWGmc loss chronology leaves nominative `*fundanaz` as `*fundan` before OE fronting can apply [DEV_NOTES:line-25217-25232; DEV_NOTES:line-25466-25498; @RingeTaylor2014, §5.1.2]. In other words, later DEV_NOTES does not merely prefer Campbell's analogical account; it concludes that no source in the local library supports forcing `funden` out of nominative `*fundanaz` by a new rule. That is why the row's present `late_analogy` label is substantive rather than decorative.

From that point on, the row's solution is a paradigm-cell solution in the strict sense. DEV_NOTES asks which inflected participial cell actually has the medial nasal in onset position and therefore fronts `-an-` regularly to `-en-`. The recommended answer is the strong participial/adjectival **acc.sg.m.** `*fúnðanǭ`, not because it is the dictionary headword, but because it is the cleanest cell where both key properties are inherited rather than levelled: the Verner consonant is regular and the medial vowel fronting is regular [DEV_NOTES:line-25289-25316; DEV_NOTES:line-25538-25571; @Campbell1959, §334]. The project briefly predicted that this path might surface as bare `funden`, but the implementation trace later showed that the actual regular reflex of this cell is `fundene`, with final `-e` from bimoric `*-ǭ` [DEV_NOTES:line-25356-25390; DEV_NOTES:line-25752-25790].

The attestation question matters because the row is not allowed to hide behind an unattested probe form. DEV_NOTES therefore asked whether the old regular comparator `fundan` was directly attested anywhere in the local reference library. The answer recorded there is negative: the library search produced only Old Saxon `fundan`, while Bosworth-Toller, Seebold's OE line, and the checked OE dictionary material gave `funden` rather than OE `fundan` [DEV_NOTES:line-25588-25646]. That closes off the tempting simplification `keep nominative protoform, just retarget to fundan`. For current workflow purposes, `fundan` remains a plausible relic-type comparator but **not** a supported row target.

The final implementation note supplies the row's present working endpoint. DEV_NOTES records the trace `fúnðanǭ -> fundene`, spelling out the crucial steps: West Germanic hardening `*ð -> *d`, early unstressed fronting of medial `*a` with heterosyllabic `n`, merger `*æ -> *e`, then bimoric `*ǭ -> *e` at the end [DEV_NOTES:line-25771-25790]. It also preserves the attestation case for the target itself: Bosworth-Toller quotes manuscript `fundene`, and Hall's `tō-fundennes` independently confirms an inflected participial stem `funden(n)-` [DEV_NOTES:line-25792-25816; @BosworthToller1898, s.v. "findan"; @ClarkHall1960, s.v. "tō-fundennes"]. For current row policy, that is the decisive closure: the row no longer targets infinitive `findan`, no longer treats nominative `funden` as regular, and no longer needs a rule tweak. It targets attested `fundene` from oblique participial `*fúnðanǭ`, while keeping `*fínθaną` as the comparative cognate-set proto and recognizing bare `funden` as the later analogical citation form.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6950-7568

Source heading: early `findan` note on Verner's Law, NSL, and the first paradigm-cell switch  
Source line or section hint: lines 6950-7568  
Fragment type: superseded_or_diagnostic_for_lexeme  
Status: superseded  
Issue tags: Verner_law;NSL;paradigm_cell;old_target;project_chronology  
Recommended use: use_to_explain_superseded_analysis  
Shared with row IDs:  
Text or paraphrase:
This long March note remains indispensable for the **reason the row left the infinitive**. It shows that infinitive `*finþaną` cannot be the row's direct FST input because NSL applies to `*-nþ-`, while OE `findan` has levelled `d`; it quotes Fulk on Verner voicing being expected in the preterite plural and passive participle, and it quotes Ringe-Taylor's exact `*finþan > *fīþan` statement for this verb [@Fulk2018, §12.17; @RingeTaylor2014, §5.1.1]. What is superseded inside the same fragment is the next move: it treated past-participle nominative `*funðanăz -> funden` as fully regular and therefore changed the row to `funden`. Later DEV_NOTES keeps the participial logic but rejects that nominative-cell endpoint as analogical on the vocalic side.

### DEV_NOTES:line-25144-25159

Source heading: withdrawal of the `*ă/*a` rescue for row 2011  
Source line or section hint: lines 25144-25159  
Fragment type: lexeme_specific  
Status: current  
Issue tags: notation_hack;row_hygiene;source_discipline  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This short fragment matters because it closes off the false repair path. DEV_NOTES explains that the earlier `*funðanăz -> funden` success depended on a hidden encoding distinction after the 2026-04-22 migration exposed the issue, then states plainly: `"We should *not* re-introduce the breve on row 2011. There is only one unaccented schwa-like low vowel at this stage, and we should spell it one way."` The row's eventual fix therefore has to be a genuine paradigm-cell or chronology decision, not a return to special spelling just for this participle [DEV_NOTES:line-25144-25159].

### DEV_NOTES:line-25406-25571

Source heading: sharpened source audit on strong past-participle `-en`  
Source line or section hint: lines 25406-25571  
Fragment type: bibliography_or_source_audit_for_lexeme  
Status: current  
Issue tags: source_audit;analogy;past_participle;oblique_cell;opinio_communis  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This is the controlling authority for the row's current analysis. Campbell, Luick, and Brunner are all quoted as treating strong past-participle nominative `-en` as analogical from inflected cases rather than as the regular reflex of nominative `*-anaz` [@Campbell1959, §334; @Luick1914, §301.3; @SieversBrunner1965, §366 Anm. 3]. DEV_NOTES then states the consequence explicitly: there is **no** source in the repo library that makes `funden` the lautgesetzlich nominative outcome of `*fundanaz`, so the only defensible row strategy is to encode an oblique participial cell such as `*fúnðanǭ` and stop trying to phonologize the analogical nominative.

### DEV_NOTES:line-25578-25750

Source heading: follow-up on `fundan` attestation and on why the row moved to the participle  
Source line or section hint: lines 25578-25750  
Fragment type: bibliography_or_source_audit_for_lexeme  
Status: current  
Issue tags: attestation_check;target_selection;project_history;paradigm_cell  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This fragment answers two practical questions later report writers would otherwise have to reopen. First, it records that direct OE attestation of `fundan` was **not demonstrated** from the local reference library, so the row cannot honestly simplify itself by retargeting to bare regular nominative `fundan` [DEV_NOTES:line-25588-25646]. Second, it reconstructs the project chronology: the row first moved away from infinitive `findan` because the infinitive's `d` is analogical and NSL destroys the regular `*nþ` path, then discovered that nominative participial `funden` is analogical on the vowel side, and finally concluded that an oblique participial cell is the cleanest cell in the whole paradigm [DEV_NOTES:line-25648-25737].

### DEV_NOTES:line-25752-25820

Source heading: Path α implementation result `*fúnðanǭ -> fundene`  
Source line or section hint: lines 25752-25820  
Fragment type: lexeme_specific  
Status: current  
Issue tags: row_policy;attested_form;proto_vs_protoform;accusative_singular;late_analogy  
Recommended use: cite_in_final_report  
Shared with row IDs:  
Text or paraphrase:
This fragment gives the row's present operational endpoint. It records the successful trace `fúnðanǭ -> fundene`, explains why medial `-an-` fronts regularly in this oblique cell, and states that the final `-e` is the regular reflex of bimoric `*-ǭ` [DEV_NOTES:line-25771-25790]. It also preserves the attestation basis for the target itself: Bosworth-Toller quotes `fundene`, while Hall's `tō-fundennes` confirms the inflected participial stem [@BosworthToller1898, s.v. "findan"; @ClarkHall1960, s.v. "tō-fundennes"]. The only part of this fragment that is now stale is its temporary implementation-table rewrite of `PROTO`; the live row has since restored `PROTO = *fínθaną` while keeping `PROTOFORM = *fúnðanǭ`.

## Superseded or diagnostic material

Two superseded phases must stay visible because they explain why the row looks unusual now. First, the March `*funðanăz -> funden` solution was a **real** advance over infinitive `*finþaną -> findan`: it correctly escaped the analogical infinitive consonant and the NSL trap. But later DEV_NOTES shows that it still encoded an analogical nominative participle and relied on an unstable `*ă/*a` distinction to keep the vowel fronting story alive [DEV_NOTES:line-7267-7337; DEV_NOTES:line-10115-10140; DEV_NOTES:line-10882-10895]. Use that phase only as project chronology.

Second, the intermediate Path-α decision note is not identical with the final row state. It was right to abandon rule tinkering and to prefer oblique `*fúnðanǭ`, but its verification plan still expected the surface result to collapse to bare `funden`, and its accompanying implementation stage temporarily rewrote `PROTO` as if the row no longer needed a cognate-set headword distinct from the inflected cell [DEV_NOTES:line-25356-25390; DEV_NOTES:line-25754-25761]. Later work corrected both points: the actual surface target is `fundene`, and the row once again distinguishes comparative `PROTO` from row-specific `PROTOFORM`.

The main diagnostic caution for future work is therefore editorial rather than phonological. Do not slide back into describing `fundene` as if it were merely a convenient probe for unattested `funden`, and do not describe `funden` as if it were the regular sound-law outcome of nominative `*fúnðanaz`. The current row only stays coherent if those two claims remain separate: `fundene` is the attested oblique participial cell the FST can derive regularly, while `funden` is the later analogical nominative that explains the familiar dictionary form.

## Open questions for later work

- If later report drafting wants a compact paradigm table, add an explicit row-local probe covering at least nom.sg. `*fúnðanaz`, acc.sg.m. `*fúnðanǭ`, nom.pl. `*fúnðanai`, and gen.sg. `*fúnðanas`, so the oblique-cell choice can be shown positively rather than only defended against the nominative.
- If additional primary-source access is added beyond the current local library, re-check whether any direct OE attestation of `fundan` exists. Until such evidence is in hand, the row should continue to treat `fundan` as an unsupported comparator rather than as an alternative target.
- If the live TSV note is ever tightened, keep the present three-level wording explicit: cognate-set `*fínθaną`, selected input cell `*fúnðanǭ`, attested OE target `fundene`, with `funden` mentioned only as the analogical nominative background.
