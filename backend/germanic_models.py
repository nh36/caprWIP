"""Select the published Old English networks without changing other doculects."""
from pathlib import Path
import hashlib
import json
import sys

from foma import FST
from oe_input_context import CITATION_CONTEXT, lexical_apply_down, lexical_apply_up, lexical_fst

ROOT = Path(__file__).resolve().parent
MODEL_DIR = ROOT / "germanic-model-bins"
MODELS = ("A", "B2", "compatibility")
DEFAULT_MODEL = "A"


class UnknownModel(ValueError):
    pass


class ModelUnavailable(RuntimeError):
    pass


class PublishedGermanicFST:
    def __init__(self, fst, doculect):
        self.network = lexical_fst(fst, doculect)

    def apply_down(self, form, context=CITATION_CONTEXT):
        return lexical_apply_down(self.network, form, context)


def tool_path():
    tools = str(ROOT / "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)


def selected_inputs(rows):
    tool_path()
    from oe_pipeline import normalize_proto

    return {row["ID"]: normalize_proto(row.get("PROTOFORM", "")) for row in rows}


def board_apply_up(fst, ipa, context, selected=(None, None)):
    if isinstance(fst, PublishedGermanicFST):
        target, proto = selected
        # An unrestricted inverse can enumerate hundreds of thousands of forms per row.
        return (proto,) if target and proto and target in set(fst.apply_down(proto, context)) else ()
    return lexical_apply_up(fst, ipa, context)


def board_apply_down(fst, proto, context):
    if isinstance(fst, PublishedGermanicFST):
        return fst.apply_down(proto, context)
    return lexical_apply_down(fst, proto, context)


def model_name(value):
    if value is None:
        return DEFAULT_MODEL
    if value not in MODELS:
        raise UnknownModel("Germanic model must be A, B2, or compatibility")
    return value


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def model_bins(model, doculects):
    model = model_name(model)
    names = {"Old_English": "old_english", "English": "english",
             "German": "german", "Dutch": "dutch"}
    results = {}
    for doculect in doculects:
        if doculect not in names:
            continue
        path = MODEL_DIR / (names[doculect] + ".bin")
        if doculect == "Old_English" and model != "compatibility":
            path = MODEL_DIR / f"old_english_{model}.bin"
            try:
                receipt = json.loads(path.with_suffix(".json").read_text(encoding="utf-8"))
                if (receipt["fst_sha256"] != digest(ROOT / "fsts/germanic.txt")
                        or receipt["runner_sha256"] != digest(ROOT / "tools/sc047_models.py")
                        or receipt["bin_sha256"] != digest(path)):
                    raise ValueError("Stale binary")
            except (OSError, ValueError, KeyError) as exc:
                raise ModelUnavailable(
                    f"Model {model} binaries are missing or stale; run "
                    "docker compose exec -T backend python3 tools/build_germanic_models.py"
                ) from exc
        if path.is_file():
            results[doculect] = PublishedGermanicFST(FST.load(str(path)), doculect)
        elif doculect == "Old_English":
            raise ModelUnavailable("The compatibility Old English binary has not been built")
    return results
