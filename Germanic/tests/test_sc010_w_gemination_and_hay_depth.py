#!/usr/bin/env python3
"""Regression for the SC010 *w-gemination repair and hay's reconstruction depth.

Governing memo:
Germanic/docs/sound_changes/audits/sc010-w-gemination-and-hay-depth-adjudication.md

Protected scientific conclusions:

  * CAPR implements the Ringe-Taylor/Campbell architecture, not Fulk's.
    PGmc singleton *wj geminates to *wwj by the ordinary West Germanic
    gemination law, and pre-OE then resolves *awwj to *auj.
    Campbell §407 p. 167: "every consonant except r being affected after
    short syllables... The forms in which w is doubled are dealt with in
    §120.2."  Ringe and Taylor p. 53: "it appears that that cluster too
    underwent gemination in PWGmc."
  * hay's selected Proto-Germanic input must carry a SINGLETON *w. The old
    *xáwwją encoded a West Germanic geminate in a Proto-Germanic slot, which
    no source reconstructs: R&T p. 53 give *hawja, Campbell §120.2 p. 46
    gives *hawja-, and Kroonen p. 215 gives *hauja-.
  * The general invariant: a selected Proto-Germanic input must not
    pre-encode a West Germanic change that the cascade itself models.
  * SC010 supplies the geminate, SC029 resolves it, SC030 fronts the result.
    The reconstructed intermediate is exposed, not telescoped away.
  * SC029's singleton branches were an artifact of hay's bad protoform and
    are gone. The surviving pair are stress-notation variants.
  * The *w branch is not a hay-specific exception: it uses the same
    environment as the other thirteen members, and genuine non-members must
    stay out of its domain.

Firing populations and absolute rule positions are deliberately NOT frozen
here; they come from the generated census. Only rule identity, the corpus
invariant, and the derivational chain are protected.

Run: cd Germanic/tests && python3 -m unittest test_sc010_w_gemination_and_hay_depth
"""
from __future__ import annotations

import csv
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GERMANIC = REPO_ROOT / "Germanic"
FST = GERMANIC / "fsts" / "germanic.txt"
CORPUS = GERMANIC / "data" / "germanic-aligned-final.tsv"
SC_DIR = GERMANIC / "docs" / "sound_changes"
REGISTRY = SC_DIR / "registry" / "sc_registry.tsv"
EDGES = SC_DIR / "registry" / "chronology_edges.tsv"
MEMO = SC_DIR / "audits" / "sc010-w-gemination-and-hay-depth-adjudication.md"
TRACE = GERMANIC / "docs" / "debug_snapshots" / "oe_full_trace_report.txt"

GEMINATION_ENV = "|| EnglishStarShortVowel _ {*j}"

# Words whose *au is created by the gemination-plus-resolution chain.
AWJ_WITNESSES = {"hay": "hīeġ", "strew": "strīeġan"}

# Protoforms containing w somewhere before a j that must NOT geminate: the
# w is not immediately before *j, or the preceding vowel is not short.
NEGATIVE_CONTROLS = (
    "*lḗwijaną",
    "*smérwijaną",
    "*skawōjaną",
    "*skáwōjaną",
    "*wainōjaną",
    "*wéljaną",
    "*weljô",
    "*wéljô",
)


def _tsv_rows(path: Path):
    lines = [line for line in path.read_text(encoding="utf-8").splitlines()
             if not line.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


class WGeminationRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = FST.read_text(encoding="utf-8")
        cls.uncommented = re.sub(r"(?m)^\s*#.*$", "", cls.text)
        cls.registry = {r["sc_id"]: r for r in _tsv_rows(REGISTRY)}
        cls.edges = _tsv_rows(EDGES)
        cls.corpus = _tsv_rows(CORPUS)
        cls.memo = MEMO.read_text(encoding="utf-8")
        flat = re.sub(r"(?m)^\s*>\s?", "", cls.memo.replace("`", ""))
        cls.memo_flat = " ".join(flat.split())
        cls.trace = TRACE.read_text(encoding="utf-8")

    def define_body(self, identifier: str) -> str:
        match = re.search(r"define\s+%s\s*\[(.*?)\];" % re.escape(identifier),
                          self.uncommented, re.DOTALL)
        self.assertIsNotNone(match, f"rule {identifier} not found in germanic.txt")
        return match.group(1)

    def protoforms(self, concept: str) -> set[str]:
        forms = {r["PROTOFORM"] for r in self.corpus if r["CONCEPT"] == concept}
        self.assertTrue(forms, f"concept {concept!r} missing from the corpus")
        return forms

    def derivation(self, protoform: str) -> str:
        """The trace block for one selected protoform."""
        start = self.trace.find(f"PROTO: {protoform}\n")
        self.assertNotEqual(start, -1,
                            f"no trace block for {protoform!r}; refresh the control plane")
        end = self.trace.find("\n--- ", start)
        return self.trace[start:end if end != -1 else len(self.trace)]

    # ------------------------------------------------------------------
    # Corpus reconstruction depth
    # ------------------------------------------------------------------

    def test_hay_enters_with_a_singleton_w(self):
        """hay's PGmc input must not pre-encode the West Germanic geminate.

        R&T p. 53 give PGmc *hawja, Campbell §120.2 p. 46 *hawja-, Kroonen
        p. 215 *hauja-. None reconstructs a Proto-Germanic *hawwja-.
        """
        for form in self.protoforms("hay"):
            self.assertNotIn("ww", form,
                             "hay must not carry a West Germanic geminate in a "
                             "Proto-Germanic slot; the cascade models that "
                             "gemination at SC010")
            self.assertIn("áwj", form,
                          "hay's PGmc input must show singleton *w before *j")

    def test_strew_keeps_its_source_correct_singleton_input(self):
        """strew was already right and must stay right (R&T p. 53 *strawjaną)."""
        for form in self.protoforms("strew"):
            self.assertIn("áwj", form)
            self.assertNotIn("ww", form)

    def test_no_selected_protoform_pre_encodes_wgmc_j_gemination(self):
        """The governing invariant, applied to the whole corpus.

        A selected Proto-Germanic input must not carry a geminate that the
        cascade itself creates before *j. This is what went wrong with hay.
        """
        offenders = sorted({
            (r["CONCEPT"], r["PROTOFORM"]) for r in self.corpus
            if re.search(r"(.)\1j", r["PROTOFORM"])
        })
        self.assertEqual(offenders, [],
                         "these protoforms pre-encode a pre-*j geminate that "
                         "SC010 should be producing")

    def test_corpus_has_no_iwj_lexeme(self):
        """Boundary condition on the *w branch (memo §5.2).

        SC029 requires a preceding *a, so an *iwj form would geminate at SC010
        with nothing to resolve it. R&T's *niwjaz, *siwjaną and *gliwjas need
        the separate *iuwj treatment of Campbell §120.2, which CAPR does not
        model. If this test ever fails, model that outcome first.
        """
        offenders = sorted({
            (r["CONCEPT"], r["PROTOFORM"]) for r in self.corpus
            if re.search(r"[iíīĭ]wj", r["PROTOFORM"])
        })
        self.assertEqual(offenders, [],
                         "an *iwj lexeme was added but its outcome is unmodelled")

    # ------------------------------------------------------------------
    # Rule identity
    # ------------------------------------------------------------------

    def test_sc010_geminates_w_before_j(self):
        """Campbell §407 p. 167 makes *w an ordinary member of the law."""
        body = self.define_body("PWGmcJGemination")
        self.assertIn("{*w} -> {*w} {*w} " + GEMINATION_ENV, body,
                      "SC010 must supply the *wwj geminate that SC029 resolves")

    def test_the_w_branch_is_not_a_special_case(self):
        """It must use the same environment as every other member."""
        body = self.define_body("PWGmcJGemination")
        clauses = [c.strip() for c in body.split(",") if c.strip()]
        self.assertGreater(len(clauses), 10)
        for clause in clauses:
            self.assertTrue(clause.endswith(GEMINATION_ENV),
                            f"clause {clause!r} does not use the shared "
                            "short-vowel-before-*j environment")

    def test_r_and_z_stay_out_of_the_gemination_law(self):
        """R&T p. 52: *r and *z are its only genuine exceptions."""
        body = self.define_body("PWGmcJGemination")
        for segment in ("{*r}", "{*z}"):
            self.assertNotIn(f"{segment} -> {segment} {segment}", body,
                             f"{segment} must not geminate before *j")

    def test_sc029_takes_only_the_geminate_input(self):
        """The singleton branches were an artifact of hay's bad protoform."""
        body = self.define_body("OEAwjGlideFormation")
        self.assertIn("{*á} {*w} {*w} {*j}", body)
        clauses = [c.strip() for c in body.split(",") if c.strip()]
        for clause in clauses:
            source = clause.split("->")[0]
            self.assertEqual(source.count("{*w}"), 2,
                             f"SC029 clause {clause!r} does not take a geminate "
                             "input; SC010 now supplies the geminate for every "
                             "witness, so singleton branches are unwitnessed")

    def test_sc029_is_not_telescoped_into_sc010(self):
        """Both changes must remain separately visible.

        The West Germanic geminate is a reconstructed intermediate attested in
        the continental cognates (OHG houwi, gistrouwen; OS hoi). A later
        reversal is no reason to delete the earlier change.
        """
        self.assertIn("define PWGmcJGemination", self.uncommented)
        self.assertIn("define OEAwjGlideFormation", self.uncommented)

    # ------------------------------------------------------------------
    # Derivational chain
    # ------------------------------------------------------------------

    def test_gemination_then_resolution_then_fronting(self):
        """The full reconstructed chain must be visible for both witnesses.

        This reproduces R&T p. 53 and Campbell §120.2 step for step:
        PGmc singleton -> WGmc geminate -> pre-OE diphthong -> fronted.
        """
        for concept in AWJ_WITNESSES:
            for form in self.protoforms(concept):
                block = self.derivation(form)
                gemination = re.search(r"PWGmcJGemination: (\S+)", block)
                self.assertIsNotNone(
                    gemination,
                    f"{concept}: SC010 must FIRE (not '[no-change]'), creating "
                    "the West Germanic geminate")
                self.assertIn("*w*w*j", gemination.group(1),
                              f"{concept}: SC010 must produce the *wwj geminate")
                resolved = re.search(r"OEAwjGlideFormation: (\S+)", block)
                self.assertIsNotNone(resolved, f"{concept}: SC029 must fire")
                self.assertIn("*áu*j", resolved.group(1),
                              f"{concept}: SC029 must yield *au with *j surviving")
                fronted = re.search(r"OEAuFronting: (\S+)", block)
                self.assertIsNotNone(fronted, f"{concept}: SC030 must fire")
                self.assertIn("*áeu", fronted.group(1),
                              f"{concept}: SC030 must front the new *au")

    def test_surface_outputs_are_unchanged_by_the_repair(self):
        """The repair corrects the history without moving any surface form."""
        for concept, expected in AWJ_WITNESSES.items():
            for form in self.protoforms(concept):
                block = self.derivation(form)
                self.assertIn(f"OUTPUTS: {expected}", block,
                              f"{concept} must still yield {expected}")

    def test_negative_controls_do_not_geminate(self):
        """A broad *w branch must not create accidental geminates."""
        for form in NEGATIVE_CONTROLS:
            if f"PROTO: {form}\n" not in self.trace:
                continue
            block = self.derivation(form)
            fired = re.search(r"PWGmcJGemination: (\S+)", block)
            if fired is not None:
                self.assertNotIn("*w*w", fired.group(1),
                                 f"{form} must not undergo *w-gemination")

    # ------------------------------------------------------------------
    # Registry and chronology
    # ------------------------------------------------------------------

    def test_sc010_keeps_confidence_a(self):
        """The general law stays secure; the dispute is confined to *w.

        Fulk §4.10 n. 1 p. 73 rejects only the *w member, so the confidence
        letter for the whole law must not be lowered mechanically.
        """
        self.assertEqual(self.registry["SC010"]["confidence"], "A")
        notes = self.registry["SC010"]["staging_notes"]
        self.assertIn("Fulk", notes,
                      "SC010 must record the dispute over its *w member")

    def test_sc029_keeps_confidence_b(self):
        """Discreteness still depends on the disputed gemination analysis."""
        self.assertEqual(self.registry["SC029"]["confidence"], "B")

    def test_sc010_feeds_sc029(self):
        """The feeding relation must be registered now that SC010 creates it."""
        matches = [e for e in self.edges
                   if e["source_change_id"] == "SC010"
                   and e["target_change_id"] == "SC029"]
        self.assertTrue(matches, "missing chronology edge SC010 -> SC029")
        for edge in matches:
            self.assertEqual(edge["witness_role"], "feeding")
            self.assertIn("hay", edge["representative_lexemes"])
            self.assertIn("strew", edge["representative_lexemes"])

    def test_sc029_still_feeds_sc030(self):
        """The repair must strengthen, not alter, the 11aa99e8 conclusion."""
        matches = [e for e in self.edges
                   if e["source_change_id"] == "SC029"
                   and e["target_change_id"] == "SC030"]
        self.assertTrue(matches, "SC029 -> SC030 feeding edge disappeared")
        for edge in matches:
            self.assertEqual(edge["witness_role"], "feeding")

    # ------------------------------------------------------------------
    # Memo
    # ------------------------------------------------------------------

    def test_memo_adopts_architecture_a_explicitly(self):
        self.assertIn("CAPR adopts **architecture A**", self.memo)
        for needle in (
            "every consonant except r being affected after short syllables",
            "it appears that that cluster too underwent gemination in PWGmc",
        ):
            self.assertIn(needle, self.memo_flat,
                          f"memo must quote the source directly: {needle!r}")

    def test_memo_records_fulks_dissent_without_adopting_it(self):
        self.assertIn("Fulk", self.memo)
        self.assertIn("straujaną", self.memo_flat,
                      "memo must state Fulk's actual alternative, that the "
                      "diphthong is original, not merely that he disagrees")

    def test_memo_records_the_rename_debt(self):
        self.assertIn("rename", self.memo_flat)


if __name__ == "__main__":
    unittest.main()
