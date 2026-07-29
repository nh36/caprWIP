#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
ASSEMBLED = ROOT / "docs" / "assembly" / "capr_book_draft_alpha_01.md"
SC057_PATH = ROOT / "docs" / "sound_changes" / "reader_facing" / "057-j-cluster-coalescence.md"

COUNTERFACTUAL_RE = re.compile(
    r"\byields?\s+"
    r"(?P<output>\[\*(?P<pred_form>[^*\n]+)\*\]\{[^}]*\bpred\b[^}]*\}|\*(?P<plain_form>[^*\n]+)\*)"
    r"(?P<gloss>\s*[,;]?\s*(?:'[^'\n]+'|‘[^’\n]+’))?"
    r"\s+(?P<contrast>rather than(?: the)? expected(?: OE)?|instead of(?: the)? expected(?: OE)?)\s+"
    r"(?P<expected>\*[^*\n]+\*)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class PredictedIssue:
    kind: str
    form: str
    line: int
    detail: str


def _is_uncertainty_notation(form: str) -> bool:
    token = form.strip()
    return "?" in token or "+?" in token or token.endswith("+")


def _line_no(text: str, index: int) -> int:
    return text[:index].count("\n") + 1


def find_predicted_issues(text: str) -> list[PredictedIssue]:
    issues: list[PredictedIssue] = []
    for m in COUNTERFACTUAL_RE.finditer(text):
        line = _line_no(text, m.start("output"))
        pred_form = (m.group("pred_form") or "").strip()
        plain_form = (m.group("plain_form") or "").strip()
        gloss = m.group("gloss") or ""

        if pred_form:
            if gloss.strip():
                issues.append(
                    PredictedIssue(
                        kind="glossed_pred",
                        form=pred_form,
                        line=line,
                        detail=".pred forms must not carry lexical glosses",
                    )
                )
            continue

        if plain_form and not _is_uncertainty_notation(plain_form):
            issues.append(
                PredictedIssue(
                    kind="unmarked_counterfactual",
                    form=plain_form,
                    line=line,
                    detail="Counterfactual yielded form is not marked with .pred",
                )
            )

    return issues


def check_sc057_policy() -> list[str]:
    text = SC057_PATH.read_text(encoding="utf-8")
    errors: list[str] = []
    if "[*bēaġan*]{.pred}" not in text:
        errors.append("SC057 missing .pred markup for counterfactual bēaġan")
    if "[*sōċan*]{.pred}" not in text:
        errors.append("SC057 missing .pred markup for counterfactual sōċan")
    if re.search(r"\[\*bēaġan\*\]\{\.pred[^}]*\}\s*['‘]", text):
        errors.append("SC057 has glossed .pred form bēaġan")
    if re.search(r"\[\*sōċan\*\]\{\.pred[^}]*\}\s*['‘]", text):
        errors.append("SC057 has glossed .pred form sōċan")
    return errors


def main() -> int:
    text = ASSEMBLED.read_text(encoding="utf-8")
    issues = find_predicted_issues(text)
    sc057_errors = check_sc057_policy()

    if issues or sc057_errors:
        print("Predicted-form policy violations detected:")
        for issue in issues:
            print(f"  Line {issue.line}: [{issue.kind}] {issue.form} — {issue.detail}")
        for error in sc057_errors:
            print(f"  {error}")
        print(
            "\nCounterfactual yielded outputs must be marked with `.pred` and must not be glossed."
        )
        return 2

    print("Predicted-form policy checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
