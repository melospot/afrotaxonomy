import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"
TAGS_DIR = ROOT / "data" / "tags"
SCHEMA_DIR = ROOT / "schema"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def test_genres_match_schema() -> None:
    validator = Draft202012Validator(_load_json(SCHEMA_DIR / "genre.schema.json"))
    for path in GENRES_DIR.rglob("*.yaml"):
        data = _load_yaml(path)
        errors = list(validator.iter_errors(data))
        assert not errors, f"{path.relative_to(ROOT)} failed schema: {errors[0].message}"


def test_tags_match_schema() -> None:
    validator = Draft202012Validator(_load_json(SCHEMA_DIR / "tags.schema.json"))
    for path in TAGS_DIR.glob("*.yaml"):
        data = _load_yaml(path)
        errors = list(validator.iter_errors(data))
        assert not errors, f"{path.relative_to(ROOT)} failed schema: {errors[0].message}"
