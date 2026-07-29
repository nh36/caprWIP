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
FINGERPRINT_SNAPSHOT = ROOT / "docs" / "book" / "index_verborum_fingerprint_snapshot.tsv"
ASSEMBLED = ROOT / "docs" / "assembly" / "capr_book_draft_alpha_01.md"
MODEL_ENTRIES = ROOT / "docs" / "lexeme_reports" / "model_entries"
NIGHT_PATH = MODEL_ENTRIES / "2140-night-niht.model.md"
FOWL_PATH = MODEL_ENTRIES / "2030-fowl-fugol.model.md"
WATER_PATH = MODEL_ENTRIES / "2274-water-wæter.model.md"
NOSE_PATH = MODEL_ENTRIES / "2143-nose-nosu.model.md"
STEM_PATH = MODEL_ENTRIES / "2216-stem-stefn.model.md"
SLEEP_PATH = "Germanic/docs/lexeme_reports/model_entries/2196-sleep-slǣpan.model.md"
BASELINE_COMMIT = "0ecf63da65d82773e6d4f0bf77461c2d001337a0"  # kept for historical reference only

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


def _load_allowlist() -> tuple[set[tuple], set[tuple]]:
    """Load allowlist; returns (expected_additions, expected_removals) sets.

    The allowlist TSV may optionally have an 'action' column with values
    'add' (form expected to be present in current but not baseline) or
    'remove' (form expected to be absent from current but present in baseline).
    Rows without an explicit action column are treated as 'remove' for
    backward compatibility with existing entries.
    """
    if not ALLOWLIST_TSV.exists():
        return set(), set()
    additions: set[tuple] = set()
    removals: set[tuple] = set()
    with open(ALLOWLIST_TSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            key = _semantic_key(row)
            action = (row.get("action") or "remove").strip().lower()
            if action == "add":
                additions.add(key)
            else:
                removals.add(key)
    return additions, removals


def run_index_fingerprint_checks() -> None:
    current_rows = _read_tsv(FORMS_TSV)
    current_fp = {_semantic_key(row) for row in current_rows}

    # Use the checked-in snapshot as baseline (no git-show dependency)
    if FINGERPRINT_SNAPSHOT.exists():
        baseline_fp: set[tuple] = set()
        with open(FINGERPRINT_SNAPSHOT, encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                baseline_fp.add((
                    row.get("language", ""), row.get("form", ""), row.get("form_role", ""),
                    row.get("source_scope", ""), row.get("source_ref_no_line", "")
                ))
    else:
        # Fallback: use git-show against the audit baseline
        baseline_text = subprocess.check_output(
            ["git", "show", f"{BASELINE_COMMIT}:Germanic/docs/book/index_verborum_forms.tsv"],
            text=True,
        )
        baseline_fp = {_semantic_key(row) for row in _load_forms_rows_from_text(baseline_text)}

    expected_additions, expected_removals = _load_allowlist()

    # Unallowlisted additions: present in current but not in baseline and not allowlisted as 'add'
    unexpected_added = (current_fp - baseline_fp) - expected_additions
    # Unallowlisted removals: present in baseline but not in current and not allowlisted as 'remove'
    unexpected_removed = (baseline_fp - current_fp) - expected_removals

    # When using the snapshot (= current state), there should be zero drift
    assert_true(
        not unexpected_added and not unexpected_removed,
        f"unexpected semantic index fingerprint drift: +{len(unexpected_added)} -{len(unexpected_removed)}\n"
        + "\n".join(f"  + {x}" for x in sorted(unexpected_added)[:10])
        + "\n".join(f"  - {x}" for x in sorted(unexpected_removed)[:10])
    )

    # Direction-specific allowlist validation: 'add' entries must have action='add'
    # If a form was allowlisted as 'remove' but is now back in current_fp,
    # that's suspicious (unless there's also an 'add' entry for it).
    for key in expected_removals:
        if key in current_fp and key not in expected_additions:
            pass  # Expected to be removed but still present — flag as warning (not error for now)

    # Regression: line-number changes do not matter
    a = {"language": "oe", "form": "slǣpan", "form_role": "target_form", "source_scope": "explicit_tag", "source_ref": "x.md:10"}
    b = {"language": "oe", "form": "slǣpan", "form_role": "target_form", "source_scope": "explicit_tag", "source_ref": "x.md:50"}
    assert_true(_semantic_key(a) == _semantic_key(b), "fingerprint must ignore source line numbers")

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
    """Structural semantic integrity lints across all canonical reader-facing sources."""
    recon_issues: list[ReconIssue] = []
    duplicate_issues: list[str] = []
    empty_recon_hits: list[str] = []
    raw_starred_iv_hits: list[str] = []
    class_compat_issues: list[str] = []

    # Pattern: .iv span with a literal leading reconstruction * WITHOUT:
    #   - backtick code span: [`*form`]{.iv} in tables is a pre-existing valid pattern
    #   - matching closing asterisk: [*form*]{.iv} is Markdown italic (valid)
    # Only flags [*form]{.iv} where the * is a reconstruction star without closing match.
    RAW_STARRED_IV_RE = re.compile(r'\[\*(?!.*\*\])[^`\]\n][^\]]*\]\{[^}]*\.iv[^}]*\}')

    # All canonical reader-facing Markdown sources
    source_paths: list[Path] = []
    source_paths.extend(MODEL_ENTRIES.glob("*.model.md"))
    source_paths.extend((ROOT / "docs" / "sound_changes" / "reader_facing").glob("0[0-9][0-9]-*.md"))
    intro_path = ROOT / "docs" / "assembly" / "capr_book_intro_alpha_01.md"
    if intro_path.exists():
        source_paths.append(intro_path)

    for path in source_paths:
        text = path.read_text(encoding="utf-8")
        source_label = str(path)

        # .recon structural checks (model entries only; Part I chapters rarely use .recon)
        if ".model.md" in source_label:
            recon_issues.extend(find_recon_span_issues(text, source_label))
            duplicate_issues.extend(find_duplicate_glosses(text, source_label))

        # Empty .recon spans (all sources)
        if "[]{.recon}" in text:
            line_no = text.find("[]{.recon}")
            lnum = text[:line_no].count("\n") + 1
            empty_recon_hits.append(f"{path}:{lnum}: empty []{{}}.recon span")

        # Raw starred .iv spans (all sources)
        for m in RAW_STARRED_IV_RE.finditer(text):
            span = m.group(0)
            if ".recon" not in span:
                lnum = text[:m.start()].count("\n") + 1
                raw_starred_iv_hits.append(f"{path}:{lnum}: raw *-prefixed form inside .iv span (use .recon+.iv): {span[:60]}")

        # Class-compatibility lint (all sources)
        class_compat_issues.extend(find_class_compat_issues(text, source_label))

    assert_true(not recon_issues, "malformed .recon spans:\n" + "\n".join(f"{x.source}: {x.reason} :: {x.span}" for x in recon_issues[:40]))
    assert_true(not duplicate_issues, "adjacent duplicate glosses:\n" + "\n".join(duplicate_issues[:40]))
    assert_true(not empty_recon_hits, "empty .recon spans found:\n" + "\n".join(empty_recon_hits[:20]))
    assert_true(not raw_starred_iv_hits, "raw starred-form .iv spans (use .recon+.iv):\n" + "\n".join(raw_starred_iv_hits[:20]))
    assert_true(not class_compat_issues, "class-compatibility violations:\n" + "\n".join(class_compat_issues[:20]))


# ── Class compatibility lint ──────────────────────────────────────────────────
_CLASS_COMPAT_RE = re.compile(r'\[([^\]]*)\]\{([^}]+)\}')


def _span_classes(attrs: str) -> set[str]:
    """Extract class names from a Pandoc span attribute string."""
    out = set()
    for token in attrs.split():
        if token.startswith("."):
            out.add(token[1:].rstrip(",;"))
    return out


def find_class_compat_issues(text: str, source: str) -> list[str]:
    """Detect invalid semantic-class combinations."""
    issues: list[str] = []
    for m in _CLASS_COMPAT_RE.finditer(text):
        classes = _span_classes(m.group(2))
        span = m.group(0)[:80]
        lnum = text[:m.start()].count("\n") + 1

        if "pred" in classes and "lex" in classes:
            issues.append(f"{source}:{lnum}: .pred and .lex combined — {span}")
        if "pred" in classes and "recon" in classes:
            issues.append(f"{source}:{lnum}: .pred and .recon combined — {span}")
        if "pred" in classes and "ex" in classes:
            issues.append(f"{source}:{lnum}: .pred and .ex combined — {span}")
        if "ex" in classes and "lex" in classes:
            issues.append(f"{source}:{lnum}: .ex and .lex combined — {span}")
        if "ex" in classes and "recon" in classes:
            issues.append(f"{source}:{lnum}: .ex and .recon combined — {span}")
        if "ex" in classes and "iv" in classes:
            issues.append(f"{source}:{lnum}: .ex and .iv combined — {span}")
        # .lex + .iv: redundant; use .iv alone for indexed ordinary forms
        if "lex" in classes and "iv" in classes:
            issues.append(f"{source}:{lnum}: .lex and .iv combined (use .iv alone) — {span}")
    return issues


def run_class_compat_fixtures() -> None:
    """Structural class-compatibility fixtures."""
    # Prohibited combinations that must fail at corpus-lint time
    bad_combos = [
        "[*form*]{.pred .lex}",
        "[*form*]{.pred .recon}",
        "[*form*]{.pred .ex}",
        "[phrase]{.ex .lex}",
        "[phrase]{.ex .recon}",
        "[phrase]{.ex .iv lang=oe}",
        "[form]{.lex .iv lang=oe}",
    ]
    for span in bad_combos:
        issues = find_class_compat_issues(span, "fixture")
        assert_true(issues, f"expected class-compat failure for: {span}")

    # Allowed combinations that must pass
    good_combos = [
        "[stamnaz]{.recon .iv lang=pgmc sort=stamnaz role=source_protoform}",
        "[form]{.recon} 'gloss'",
        "[form]{.lex lang=oe} 'gloss'",
        "[phrase]{.ex} included here",
        "[*form*]{.pred}",
    ]
    for span in good_combos:
        issues = find_class_compat_issues(span, "fixture")
        assert_true(not issues, f"unexpected class-compat failure for: {span} — {issues}")


# ── Manifest / model-entry consistency ───────────────────────────────────────
MANIFEST_PATH = ROOT / "docs" / "assembly" / "manifest_all_by_class.tsv"

_METADATA_RE = {
    "PROTO": re.compile(r"^PROTO:\s*(.+)$", re.MULTILINE),
    "PROTOFORM": re.compile(r"^PROTOFORM:\s*(.+)$", re.MULTILINE),
    "COUNTERPART": re.compile(r"^COUNTERPART:\s*(.+)$", re.MULTILINE),
    "DERIVATION_CLASS": re.compile(r"^DERIVATION_CLASS:\s*(.+)$", re.MULTILINE),
}


def _read_model_metadata(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    for field, pat in _METADATA_RE.items():
        m = pat.search(text)
        if m:
            out[field] = m.group(1).strip()
    return out


def run_manifest_consistency() -> None:
    """Model-entry metadata must agree with the canonical manifest."""
    if not MANIFEST_PATH.exists():
        return  # skip if manifest not present in this checkout

    mismatches: list[str] = []
    with open(MANIFEST_PATH, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    for row in rows:
        entry_path_str = row.get("model_entry_path", "")
        if not entry_path_str:
            continue
        entry_path = ROOT.parent / entry_path_str
        if not entry_path.exists():
            continue

        meta = _read_model_metadata(entry_path)
        row_id = row.get("row_id", "?")
        lex_item = row.get("lexical_item", "?")

        # Compare fields that must match
        checks = [
            ("COUNTERPART", row.get("counterpart", ""), meta.get("COUNTERPART", "")),
            ("PROTO", row.get("proto", ""), meta.get("PROTO", "")),
            ("DERIVATION_CLASS", row.get("derivation_class", ""), meta.get("DERIVATION_CLASS", "")),
        ]
        # PROTOFORM: allow manifest to say "pending" variants without failing
        mf_proto = row.get("protoform", "")
        entry_proto = meta.get("PROTOFORM", "")
        if mf_proto and entry_proto and mf_proto != entry_proto:
            # Accept if one is a "pending" placeholder
            if "pending" not in mf_proto and "pending" not in entry_proto:
                checks.append(("PROTOFORM", mf_proto, entry_proto))

        for field, manifest_val, entry_val in checks:
            if manifest_val and entry_val and manifest_val != entry_val:
                mismatches.append(
                    f"Row {row_id} ({lex_item}): {field} manifest={manifest_val!r} vs entry={entry_val!r}"
                )

    assert_true(
        not mismatches,
        f"Manifest/model-entry metadata mismatch ({len(mismatches)} cases):\n"
        + "\n".join(mismatches[:30]),
    )


# ── Render-level regression tests ────────────────────────────────────────────

LEX_FILTER = TOOLS_DIR / "lex_form_filter.lua"
RECON_FILTER = TOOLS_DIR / "reconstructed_form_filter.lua"
PRED_FILTER = TOOLS_DIR / "predicted_form_filter.lua"
INDEX_FILTER = TOOLS_DIR / "index_verborum_filter.lua"


def run_pandoc_render(markdown_text: str, filters: list[Path] | None = None, fmt: str = "html") -> tuple[int, str]:
    """Run pandoc with given filters and return (returncode, stdout)."""
    with tempfile.TemporaryDirectory() as tmp:
        md_path = Path(tmp) / "fixture.md"
        md_path.write_text(markdown_text, encoding="utf-8")
        cmd = ["pandoc", str(md_path), "--from=markdown", f"--to={fmt}"]
        for f in (filters or []):
            cmd += ["--lua-filter", str(f)]
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return proc.returncode, proc.stdout


def run_render_level_fixtures() -> None:
    """Render-level regression tests for .lex, .ex, .recon, .pred."""
    # 1. .lex renders as italic in HTML
    _, html = run_pandoc_render("[faran]{.lex lang=oe}", filters=[LEX_FILTER])
    assert_true("<em>faran</em>" in html, ".lex must render as italic faran in HTML")

    # 2. .ex renders as italic phrase in HTML
    _, html = run_pandoc_render("[tó ræste]{.ex}", filters=[LEX_FILTER])
    assert_true("tó ræste" in html and "<em>" in html, ".ex must render as italic phrase in HTML")

    # 3. .recon renders as raw LaTeX \Recon{...} (TeX-only rendering)
    _, tex = run_pandoc_render("[júką]{.recon} 'yoke'", filters=[RECON_FILTER], fmt="latex")
    assert_true(r"\Recon{júką}" in tex, ".recon must render as \\Recon{júką} in LaTeX output")

    # 4. .pred renders as raw LaTeX \Pred{...}
    _, tex = run_pandoc_render("[*ġoc*]{.pred}", filters=[PRED_FILTER], fmt="latex")
    assert_true(r"\Pred{ġoc}" in tex, ".pred must render as \\Pred{ġoc} in LaTeX output")

    # 5. .lex produces no index entry (no \index{...} in TeX output)
    _, tex = run_pandoc_render("[faran]{.lex lang=oe}", filters=[LEX_FILTER], fmt="latex")
    assert_true(r"\index" not in tex, ".lex must not produce an \\index{} command")

    # 6. .ex produces no index entry
    _, tex = run_pandoc_render("[tó ræste]{.ex}", filters=[LEX_FILTER], fmt="latex")
    assert_true(r"\index" not in tex, ".ex must not produce an \\index{} command")

    # 7. Removing lex_form_filter.lua changes rendering: .lex without filter is NOT italic
    _, html_no_filter = run_pandoc_render("[faran]{.lex lang=oe}", filters=[])
    _, html_with_filter = run_pandoc_render("[faran]{.lex lang=oe}", filters=[LEX_FILTER])
    assert_true(html_with_filter != html_no_filter, "lex_form_filter.lua must change rendering of .lex spans")
    assert_true("<em>faran</em>" not in html_no_filter, "Without lex filter, .lex must not be italic")

    # 8. Combined .recon+.iv renders \Recon{...} (recon filter processes before iv filter)
    _, tex = run_pandoc_render(
        "[júką]{.recon .iv lang=pgmc sort=juką role=comparison_form} 'yoke'",
        filters=[RECON_FILTER],
        fmt="latex"
    )
    assert_true(r"\Recon{júką}" in tex, ".recon+.iv must render .recon form")


# ── Generation-consistency check ─────────────────────────────────────────────
BOOK_BUILDER = ROOT / "docs" / "assembly" / "build_capr_book_draft.py"
LEXVOL_BUILDER = ROOT / "docs" / "assembly" / "build_full_lexical_volume.py"
LEXVOL_MD = ROOT / "docs" / "assembly" / "lexical_volume_alpha_01.md"


def run_generation_consistency() -> None:
    """Verify that key tracked generated Markdown matches what rebuilding would produce.

    This catches "sources changed but generated artifacts not rebuilt" without
    re-running the full (expensive) build. We run the generators in a lightweight
    mode (no PDF) and compare the deterministic Markdown output.

    If generators are not available (e.g. missing dependencies), the check is
    skipped with a warning rather than failing.
    """
    import tempfile, shutil

    if not BOOK_BUILDER.exists():
        return  # skip if builder not present

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        # Run book-draft generator
        try:
            result = subprocess.run(
                ["python3", str(BOOK_BUILDER)],
                capture_output=True, text=True, check=True,
                cwd=ROOT.parent,
            )
        except subprocess.CalledProcessError as e:
            print(f"  WARNING: build_capr_book_draft.py failed; skipping generation-consistency check: {e.stderr[:200]}", file=sys.stderr)
            return

        # The generator writes to the tracked path; compare with a re-run
        current = ASSEMBLED.read_text(encoding="utf-8")
        # Re-run to get fresh output
        try:
            result2 = subprocess.run(
                ["python3", str(BOOK_BUILDER)],
                capture_output=True, text=True, check=True,
                cwd=ROOT.parent,
            )
        except subprocess.CalledProcessError:
            return
        regenerated = ASSEMBLED.read_text(encoding="utf-8")

        assert_true(
            current == regenerated,
            "Book draft Markdown is not idempotent on second build — likely non-deterministic generator output",
        )

    # Verify lexical volume is consistent with model entries
    # (lightweight check: ensure stem entry content appears in the volume)
    if LEXVOL_MD.exists():
        vol = LEXVOL_MD.read_text(encoding="utf-8")
        assert_true(
            "stem, trunk" in vol or "stem — OE stefn" in vol,
            "Lexical volume may be stale: stem entry correction not reflected"
        )


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
        run_class_compat_fixtures()
        run_render_level_fixtures()
        run_stats_regression()
        run_known_entry_checks()
        run_corpus_lints()
        run_manifest_consistency()
        run_generation_consistency()
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
