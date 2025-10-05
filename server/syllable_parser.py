"""Utilities for constructing syllable segment data used by CAPR."""
from __future__ import annotations

from typing import Iterable, List, Optional, Sequence, Tuple

from merge_phonemes import merge_phonemes

_DEFAULT_RULES = {"i": "im", "m": "m", "r": "mnNc", "t": "t"}
_MAX_SCHEMA = "i m r t"

# Mirrors the front-end vowel inventory; keeps detection logic consistent.
_VOWEL_CHARS = set(
    "aeiouyAEIOUYāēīōūáéíóúàèìòùâêîôûæœøəɘɜɛɞɐɑɒɔʌʉɯɪʊɨʏȳũẽĩõỹ"
)
_STRESS_MARKERS = {"ˈ", "ˌ", "'"}


def _split_onset_rime(syllable: str) -> Tuple[str, str]:
    text = syllable.strip()
    if not text:
        return "", ""

    prefix = []
    while text and text[0] in _STRESS_MARKERS:
        prefix.append(text[0])
        text = text[1:]

    onset = []
    rest = ""
    for idx, char in enumerate(text):
        if char in _VOWEL_CHARS:
            onset = list(text[:idx])
            rest = text[idx:]
            break
    else:
        onset = list(text)
        rest = ""

    if rest:
        rest = "".join(prefix) + rest
    else:
        onset = list(prefix) + onset

    onset_text = "".join(onset).strip()
    rest_text = rest.strip()
    return onset_text, rest_text


def _fallback_germanic(ipa_syllables: Sequence[str], ipa_text: str) -> List[Tuple[str, str]]:
    syllables: List[str] = [s.strip() for s in ipa_syllables if s.strip()]
    if not syllables and ipa_text:
        cleaned = ipa_text.strip()
        if cleaned:
            syllables = [cleaned]

    parsed: List[Tuple[str, str]] = []
    for syllable in syllables:
        onset, rime = _split_onset_rime(syllable)
        parts: List[Tuple[str, str]] = []
        if onset:
            parts.append(("i", onset))
        if rime:
            parts.append(("r", rime))
        if not parts:
            parts.append(("r", syllable))
        positions = " ".join(position for position, _ in parts)
        tokens = " ".join(token for _, token in parts)
        parsed.append((positions, tokens))
    return parsed


def build_syllable_parsed_entries(
    structure_field: str,
    tokens_field: str,
    ipa_text: str,
    ipa_syllables: Sequence[str],
    *,
    allow_fallback: bool = False,
) -> List[Tuple[str, str]]:
    structure_field = (structure_field or "").strip()
    tokens_field = (tokens_field or "").strip()
    schema_tokens = [part for part in structure_field.replace('+', ' ').split() if part]
    supports_merge = all(token.lower() in {'i', 'm', 'r', 't'} for token in schema_tokens)

    if structure_field and tokens_field and supports_merge:
        parsed: List[Tuple[str, str]] = []
        try:
            structures = structure_field.split(" + ")
            tokens = tokens_field.split(" + ")
            for sch, tk in zip(structures, tokens):
                sch = sch.strip()
                tk = tk.strip()
                if not sch or not tk:
                    continue
                parsed.append(
                    merge_phonemes(
                        str(sch),
                        str(tk),
                        _MAX_SCHEMA,
                        _DEFAULT_RULES,
                    )
                )
        except ValueError:
            if not allow_fallback:
                raise
            parsed = []
        if parsed:
            meaningful = [p for p in parsed if p[0] and p[1]]
            if meaningful:
                return parsed

    if allow_fallback:
        return _fallback_germanic(ipa_syllables, ipa_text)

    return []


def infer_syllable_strings(structure_field: str, tokens_field: str) -> Optional[Sequence[str]]:
    structures = [part for part in (structure_field or "").split() if part]
    tokens = [part for part in (tokens_field or "").split() if part]
    if not structures or len(structures) != len(tokens):
        return None

    syllables: List[List[str]] = []
    current: List[str] = []
    last_case = structures[0].isupper()

    for struct_symbol, token_symbol in zip(structures, tokens):
        current_case = struct_symbol.isupper()
        if current and current_case != last_case:
            syllables.append(current)
            current = []
        current.append(token_symbol)
        last_case = current_case

    if current:
        syllables.append(current)

    if len(syllables) <= 1:
        return None

    normalised = ["".join(parts).replace(" ", "") for parts in syllables if any(p.strip() for p in parts)]
    return [s for s in normalised if s]


__all__ = ["build_syllable_parsed_entries", "infer_syllable_strings"]
