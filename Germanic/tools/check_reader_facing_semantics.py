#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from check_predicted_forms import find_predicted_issues

ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"
VALIDATOR = TOOLS_DIR / "paragraph_gloss_validator.lua"
FORMS_TSV = ROOT / "docs" / "book" / "index_verborum_forms.tsv"
ALLOWLIST_TSV = ROOT / "docs" / "book" / "index_semantic_fingerprint_allowlist.tsv"
ASSEMBLED = ROOT / "docs" / "assembly" / "capr_book_draft_alpha_01.md"
MODEL_ENTRIES = ROOT / "docs" / "lexeme_reports" / "model_entries"
NIGHT_PATH = MODEL_ENTRIES / "2140-night-niht.model.md"
FOWL_PATH = MODEL_ENTRIES / "2030-fowl-fugol.model.md"
WATER_PATH = MODEL_ENTRIES / "2274-water-wæter.model.md"
NOSE_PATH = MODEL_ENTRIES / "2143-nose-nosu.model.md"
STEM_PATH = MODEL_ENTRIES / "2216-stem-stefn.model.md"
SLEEP_PATH = "Germanic/docs/lexeme_reports/model_entries/2196-sleep-slǣpan.model.md"
BASELINE_COMMIT = "0ecf63da65d82773e6d4f0bf77461c2d001337a0"

RECON_SPAN_RE = re.compile(r"\[(?P<content>[^\[\]\n]+)\]\{\.recon(?:[^}]*)\}")
RECON_BAD_LANG_RE = re.compile(r"\bOE\b|\bPGmc\b|\.{3}|>|<|~|,|/|\(|\)|`")
RECON_MULTI_WS_RE = re.compile(r"\s")
PRED_GLOSS_RE = re.compile(r"\[\*[^*\n]+\*\]\{[^}]*\bpred\b[^}]*\}\s*[,;]?\s*(?:'|‘|“)")
DUP_GLOSS_RE = re.compile(
    r"(?P<form>\[[^\]]+\]\{[^}]+\}|`[^`]+`|\*[^*]+\*|[A-Za-zÀ-ȳāēīōūȳǣæþðġċƀβ\-‑–]+)\s*"
    r"(?P<q1>'[^']+'|‘[^’]+’)\s*(?P<q2>'[^']+'|‘[^’]+’)"
)


@dataclass(frozen=True)
class ReconIssue:
    source: str
    span: str
    reason: str


def _inner_quote_text(q: str) -> str:
    return q.strip()[1:-1].strip().lower()


def find_recon_span_issues(text: str, source: str) -> list[ReconIssue]:
    issues: list[ReconIssue] = []
    for m in RECON_SPAN_RE.finditer(text):
        content = m.group("content").strip()
        span = m.group(0)
        if content.startswith("*"):
            issues.append(ReconIssue(source, span, "leading literal '*' inside .recon span"))
        if "'" in content or "‘" in content or "’" in content:
            issues.append(ReconIssue(source, span, "gloss text inside .recon span"))
        if RECON_BAD_LANG_RE.search(content):
            issues.append(ReconIssue(source, span, "multiple forms/chain/prose inside .recon span"))
        if RECON_MULTI_WS_RE.search(content):
            issues.append(ReconIssue(source, span, "whitespace indicates multiple lexical items or prose"))
    return issues


def find_duplicate_glosses(text: str, source: str) -> list[str]:
    out: list[str] = []
    for m in DUP_GLOSS_RE.finditer(text):
        q1 = _inner_quote_text(m.group("q1"))
        q2 = _inner_quote_text(m.group("q2"))
        if q1 == q2:
            line_no = text[: m.start()].count("\n") + 1
            out.append(f"{source}:{line_no}: adjacent duplicate glosses for {m.group('form')}")
    return out


def run_validator(markdown_text: str) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as tmp:
        md_path = Path(tmp) / "fixture.md"
        md_path.write_text(markdown_text, encoding="utf-8")
        proc = subprocess.run(
            ["pandoc", str(md_path), "--from=markdown+raw_tex", "--to=json", "--lua-filter", str(VALIDATOR)],
            text=True,
            capture_output=True,
            check=False,
        )
        return proc.returncode, proc.stderr


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def paragraph_fixture(section: str, body: str) -> str:
    """Build a minimal Part II fixture with the given prose section and body.

    The heading hierarchy matches the assembled book:
      # Word-by-word derivations  (switches to Part II)
      ### Fixture entry            (level-3 = p2_entry in validator)
      #### {section}               (level-4 = p2_section in validator)
    """
    return (
        "# Sound changes\n\n"
        "## Placeholder\n\n"
        "Non-lexical paragraph.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        f"#### {section}\n\n"
        f"{body}\n"
    )


def run_predicted_fixtures() -> None:
    tests = [
        ("yields *wrong* rather than expected *right*", True),
        ("yields *wrong* 'gloss' rather than expected *right*", True),
        ("yields [*wrong*]{.pred} rather than expected *right*", False),
        ("yields [*wrong*]{.pred} 'gloss' rather than expected *right*", True),
        ("historical input *form* is cited in evidence", False),
        ("yields *wrong+?* rather than expected *right*", False),
    ]
    for text, should_fail in tests:
        issues = find_predicted_issues(text)
        assert_true((len(issues) > 0) == should_fail, f"pred fixture failed: {text}")


def run_unicode_ascii_fixtures() -> None:
    # 1. cū then cȳ in same paragraph: second requires gloss.
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *cū* 'cow' appears first, but OE *cȳ* appears later without gloss.",
        )
    )
    assert_true(code == 2, "expected cȳ to fail after cū in same paragraph")

    # 2. nǣdl and nædl must remain distinct.
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *nǣdl* 'needle' is attested, and OE *nædl* appears again without gloss.",
        )
    )
    assert_true(code == 2, "expected nædl to fail as distinct form")

    # 3. exact same cū twice in same paragraph: pass.
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *cū* 'cow' appears here and OE *cū* appears later.",
        )
    )
    assert_true(code == 0, "same lexical form should not require a second gloss in paragraph")

    # 4. same cū in a new paragraph: fail.
    code, _ = run_validator(
        (
            "# Sound changes\n\nA stub.\n\n"
            "# Word-by-word derivations\n\n"
            "### Fixture entry\n\n"
            "#### Old English evidence\n\n"
            "OE *cū* 'cow' appears.\n\n"
            "OE *cū* appears again in a new paragraph.\n"
        )
    )
    assert_true(code == 2, "same form in new paragraph must be glossed again")

    # 5. .recon repeated in same paragraph: pass.
    code, _ = run_validator(
        paragraph_fixture(
            "Reconstruction and comparative evidence",
            "[júką]{.recon} 'yoke' is cited and [júką]{.recon} appears again.",
        )
    )
    assert_true(code == 0, ".recon repeated in same paragraph should not re-require gloss")

    # ASCII lexical coverage
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *faran* appears without gloss.")
    )
    assert_true(code == 2, "ASCII lexical form faran should be checked")

    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *faran* 'fare' appears with gloss.")
    )
    assert_true(code == 0, "ASCII lexical form with gloss should pass")

    code, _ = run_validator(
        paragraph_fixture("Reconstruction and comparative evidence", "German *fell* appears without gloss.")
    )
    assert_true(code == 2, "ASCII comparator form should be checked")

    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "This is *important* evidence for chronology.")
    )
    assert_true(code == 0, "ordinary English emphasis should not be lexical candidate")


def run_recon_duplicate_fixtures() -> None:
    bad_recon_cases = [
        "[nasō ... OE nasu]{.recon}",
        "[*júką]{.recon}",
        "[náxti > niht]{.recon}",
        "[júką 'yoke']{.recon}",
    ]
    for case in bad_recon_cases:
        assert_true(find_recon_span_issues(case, "fixture"), f"expected recon failure: {case}")

    good_recon_cases = [
        "[júką]{.recon} 'yoke'",
        "[wír-àldu]{.recon} 'world'",
    ]
    for case in good_recon_cases:
        assert_true(not find_recon_span_issues(case, "fixture"), f"expected recon pass: {case}")

    assert_true(find_duplicate_glosses("form 'night' ‘night’", "fixture"), "expected duplicate gloss failure")
    assert_true(find_duplicate_glosses("form ‘night’ 'night'", "fixture"), "expected duplicate gloss failure")
    assert_true(not find_duplicate_glosses("form 'night'", "fixture"), "single gloss should pass")
    assert_true(
        not find_duplicate_glosses("form 'night' and then explanation ‘by extension’", "fixture"),
        "distinct quoted prose should pass",
    )


def _load_forms_rows_from_text(text: str) -> list[dict[str, str]]:
    lines = [line for line in text.splitlines() if line.strip()]
    if not lines:
        return []
    return list(csv.DictReader(lines, delimiter="\t"))


def _read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _semantic_key(row: dict[str, str]) -> tuple[str, str, str, str, str]:
    source_path = (row.get("source_ref", "") or "").split(":", 1)[0]
    return (
        row.get("language", ""),
        row.get("form", ""),
        row.get("form_role", ""),
        row.get("source_scope", ""),
        source_path,
    )


def _load_allowlist() -> set[tuple[str, str, str, str, str]]:
    if not ALLOWLIST_TSV.exists():
        return set()
    return {_semantic_key(row) for row in _read_tsv(ALLOWLIST_TSV)}


def run_index_fingerprint_checks() -> None:
    current_rows = _read_tsv(FORMS_TSV)
    baseline_text = subprocess.check_output(
        ["git", "show", f"{BASELINE_COMMIT}:Germanic/docs/book/index_verborum_forms.tsv"],
        text=True,
    )
    baseline_rows = _load_forms_rows_from_text(baseline_text)
    current_fp = {_semantic_key(row) for row in current_rows}
    baseline_fp = {_semantic_key(row) for row in baseline_rows}

    allowlist = _load_allowlist()
    added = {row for row in (current_fp - baseline_fp) if row not in allowlist}
    removed = {row for row in (baseline_fp - current_fp) if row not in allowlist}
    assert_true(not added and not removed, f"unexpected semantic index fingerprint drift: +{len(added)} -{len(removed)}")

    # Line-number changes do not matter.
    a = {"language": "oe", "form": "slǣpan", "form_role": "target_form", "source_scope": "explicit_tag", "source_ref": "x.md:10"}
    b = {"language": "oe", "form": "slǣpan", "form_role": "target_form", "source_scope": "explicit_tag", "source_ref": "x.md:50"}
    assert_true(_semantic_key(a) == _semantic_key(b), "fingerprint must ignore source line numbers")

    # slǣpan must remain represented in sleep entry semantics.
    sleep_rows = [
        row
        for row in current_rows
        if (row.get("source_ref", "") or "").startswith(SLEEP_PATH)
        or row.get("source_ref", "") == "sleep — OE slǣpan"
    ]
    assert_true(
        any(row.get("form") in {"slǣpan", "slaepan"} for row in sleep_rows),
        "slǣpan missing from sleep entry index semantics",
    )

    # Adding .iv should change semantic index membership.
    base = {"language": "oe", "form": "faran", "form_role": "comparison_form", "source_scope": "broad_prose_decision", "source_ref": "a.md:1"}
    tagged = dict(base)
    tagged["source_scope"] = "explicit_tag"
    assert_true(_semantic_key(base) != _semantic_key(tagged), ".iv scope shift must change index semantics")


def run_stats_regression() -> None:
    md = (
        "# Sound changes\n\nA plain paragraph.\n\n"
        "# Word-by-word derivations\n\n"
        "### Stats test entry\n\n"
        "#### Transducer input and output\n\n"
        "[júką]{.recon} 'yoke' appears.\n\n"
        "#### Old English evidence\n\n"
        "OE *faran* 'fare' appears.\n"
    )
    code, stderr = run_validator(md)
    assert_true(code == 0, "stats fixture should pass validation")
    assert_true("top-level paragraphs visited" in stderr, "Part II top-level paragraph count missing")
    assert_true("prose paragraphs in ordinary-form scope" in stderr, "Part II prose scope count missing")
    assert_true(".recon-only paragraphs outside ordinary scope" in stderr, "Part II recon-only count missing")


def run_notation_fixtures() -> None:
    """Phonological notation sequences must never become lexical candidates."""
    # ēo, ēa, *ai must be ignored (notation, not words)
    for seq in ["ēo", "ēa", "*ai"]:
        code, _ = run_validator(
            paragraph_fixture("Old English evidence", f"The sequence *{seq}* is phonological notation.")
        )
        assert_true(code == 0, f"phonological sequence {seq!r} must not be treated as a lexical candidate")

    # A genuine two-character OE word must still be checked
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "OE *cū* appears without gloss.")
    )
    assert_true(code == 2, "genuine short OE word cū must require a gloss")

    # SC025 mōna regression: both alternant forms require their own gloss
    code, _ = run_validator(
        "# Sound changes\n\n"
        "The *mōnaþ* 'month' and *mōna* / *mōn* material.\n"
    )
    assert_true(code == 2, "SC025 regression: *mōna* must require a gloss when *mōn* carries the gloss")

    # SC025 fixed form: mōna has its own gloss
    code, _ = run_validator(
        "# Sound changes\n\n"
        "The *mōnaþ* 'month' and *mōna* 'moon' / *mōn* 'moon' material.\n"
    )
    assert_true(code == 0, "SC025 fixed: mōna 'moon' satisfies the gloss rule")


def run_lex_ex_fixtures() -> None:
    """.lex and .ex semantic markup fixtures."""
    # .lex without gloss fails
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} appears without gloss.")
    )
    assert_true(code == 2, ".lex without gloss should fail")

    # .lex with gloss passes
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} 'fare' appears.")
    )
    assert_true(code == 0, ".lex with gloss should pass")

    # .lex repeated same paragraph does not require re-gloss
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "[faran]{.lex lang=oe} 'fare' cited and [faran]{.lex lang=oe} again.")
    )
    assert_true(code == 0, ".lex repeated same paragraph should not re-require gloss")

    # .lex in new paragraph requires gloss again
    code, _ = run_validator(
        "# Sound changes\n\nA stub.\n\n"
        "# Word-by-word derivations\n\n"
        "### Fixture entry\n\n"
        "#### Old English evidence\n\n"
        "[faran]{.lex lang=oe} 'fare' first occurrence.\n\n"
        "[faran]{.lex lang=oe} second paragraph, no gloss.\n"
    )
    assert_true(code == 2, ".lex in new paragraph must be glossed again")

    # .ex (example phrase) always exempt
    code, _ = run_validator(
        paragraph_fixture("Old English evidence", "Cited as [tó ræste]{.ex} in Bosworth-Toller.")
    )
    assert_true(code == 0, ".ex example phrase must be exempt from gloss rule")

    # tó ræste regression: tó within .ex phrase must not require gloss
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "Oblique uses include [tó ræste]{.ex} 'to rest' and [on ræste]{.ex} 'at rest'.",
        )
    )
    assert_true(code == 0, "tó ræste regression: example phrases exempt from word-by-word gloss rule")


def run_case_normalization_fixtures() -> None:
    """Sentence-initial capitals must not create a new lexical identity."""
    # macaþ then Macaþ in same paragraph = one identity
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "The form *macaþ* 'makes' is the 3sg. *Macaþ* appears sentence-initially.",
        )
    )
    assert_true(code == 0, "Macaþ after macaþ 'makes' must not require a second gloss")

    # cū and cȳ remain distinct despite case-folding
    code, _ = run_validator(
        paragraph_fixture(
            "Old English evidence",
            "OE *cū* 'cow' appears first, but OE *cȳ* appears without gloss.",
        )
    )
    assert_true(code == 2, "cū and cȳ must remain distinct even after case folding")

    # Mönch regression: Brunner citation translation must not be a lexical candidate
    code, _ = run_validator(
        paragraph_fixture(
            "Development to Old English",
            "Campbell cites [`munuc`]{.iv lang=oe sort=munuc role=comparison_form} 'monk' "
            "and [`iuzuð`]{.iv lang=oe sort=iuzuth role=comparison_form} 'youth' in the "
            "same environment [@SieversBrunner1965, §150.3].",
        )
    )
    assert_true(code == 0, "Mönch regression: Brunner citation without German translations must pass")


def run_known_entry_checks() -> None:
    night = NIGHT_PATH.read_text(encoding="utf-8")
    fowl = FOWL_PATH.read_text(encoding="utf-8")
    water = WATER_PATH.read_text(encoding="utf-8")
    nose = NOSE_PATH.read_text(encoding="utf-8")
    stem = STEM_PATH.read_text(encoding="utf-8")

    assert_true("'night' 'night'" not in night and "\u2018night\u2019 \u2018night\u2019" not in night, "night still has duplicate glosses")
    assert_true("'fowl' 'fowl'" not in fowl and "\u2018fowl\u2019 \u2018fowl\u2019" not in fowl, "fowl still has duplicate glosses")
    assert_true("[nasō ... OE nasu]{.recon}" not in nose, "nose still has overbroad .recon span")
    assert_true("[*" not in water, "water still contains stray [* fragment")
    assert_true("]{.recon} 'water'weeter[*" not in water, "water retains malformed recon span fragment")
    assert_true("]{.recon} 'water'weter" not in water, "water retains malformed recon span fragment")
    assert_true("voice, sound" in stem or "stem, trunk" in stem or "prow" in stem, "stem entry missing expected stem/trunk/prow content")
    assert_true("*stébnō" not in stem or "wrong homonym" in stem, "stem entry still contains voice-word protoform without clear repudiation")

    # Residual v2 corruption guard: empty .recon spans must not exist in these entries
    for label, path in [("thousand", ROOT / "docs/lexeme_reports/model_entries/2252-thousand-þūsend.model.md"),
                         ("timber", ROOT / "docs/lexeme_reports/model_entries/2258-timber-timber.model.md"),
                         ("wake", ROOT / "docs/lexeme_reports/model_entries/2268-wake-wacan.model.md")]:
        text = path.read_text(encoding="utf-8")
        assert_true("[]{.recon}" not in text, f"{label} entry still contains empty []{{}}.recon span (v2 corruption)")

    # enforce corpus-wide .pred no-gloss policy
    pred_gloss_hits = []
    for path in (ROOT / "docs" / "sound_changes" / "reader_facing").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for m in PRED_GLOSS_RE.finditer(text):
            line_no = text[: m.start()].count("\n") + 1
            pred_gloss_hits.append(f"{path}:{line_no}")
    assert_true(not pred_gloss_hits, ".pred gloss policy violated:\n" + "\n".join(pred_gloss_hits[:20]))


def run_corpus_lints() -> None:
    recon_issues: list[ReconIssue] = []
    duplicate_issues: list[str] = []
    empty_recon_hits: list[str] = []

    for path in MODEL_ENTRIES.glob("*.model.md"):
        text = path.read_text(encoding="utf-8")
        recon_issues.extend(find_recon_span_issues(text, str(path)))
        duplicate_issues.extend(find_duplicate_glosses(text, str(path)))
        if "[]{.recon}" in text:
            line_no = text.find("[]{.recon}")
            lnum = text[:line_no].count("\n") + 1
            empty_recon_hits.append(f"{path}:{lnum}: empty []{{}}.recon span")

    assert_true(not recon_issues, "malformed .recon spans:\n" + "\n".join(f"{x.source}: {x.reason} :: {x.span}" for x in recon_issues[:40]))
    assert_true(not duplicate_issues, "adjacent duplicate glosses:\n" + "\n".join(duplicate_issues[:40]))
    assert_true(not empty_recon_hits, "empty .recon spans found:\n" + "\n".join(empty_recon_hits[:20]))


def main() -> int:
    if not VALIDATOR.exists():
        print(f"Missing validator: {VALIDATOR}", file=sys.stderr)
        return 2
    if not FORMS_TSV.exists():
        print(f"Missing index forms TSV: {FORMS_TSV}", file=sys.stderr)
        return 2
    if not ASSEMBLED.exists():
        print(f"Missing assembled markdown: {ASSEMBLED}", file=sys.stderr)
        return 2

    try:
        run_predicted_fixtures()
        run_notation_fixtures()
        run_unicode_ascii_fixtures()
        run_lex_ex_fixtures()
        run_case_normalization_fixtures()
        run_recon_duplicate_fixtures()
        run_stats_regression()
        run_known_entry_checks()
        run_corpus_lints()
        run_index_fingerprint_checks()
    except AssertionError as exc:
        print(f"Reader-facing semantic regression failure: {exc}", file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as exc:
        print(f"Reader-facing semantic regression command failed: {exc}", file=sys.stderr)
        return 2

    print("Reader-facing semantic regression suite passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
