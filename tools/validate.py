#!/usr/bin/env python3
"""Validate taxonomy sources against JSON Schema."""

from __future__ import annotations

import json
from pathlib import Path
import sys

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: pyyaml. Install with `pip install pyyaml`.") from exc

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: jsonschema. Install with `pip install jsonschema`.") from exc


ROOT = Path(__file__).resolve().parents[1]
GENRES_DIR = ROOT / "data" / "genres"
TAGS_DIR = ROOT / "data" / "tags"
SCHEMA_DIR = ROOT / "schema"


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def collect_errors(validator: Draft202012Validator, instance: dict, path: Path) -> list[str]:
    return [f"{path}: {err.message}" for err in validator.iter_errors(instance)]


def main() -> int:
    genre_schema = load_json(SCHEMA_DIR / "genre.schema.json")
    tags_schema = load_json(SCHEMA_DIR / "tags.schema.json")
    genre_validator = Draft202012Validator(genre_schema)
    tags_validator = Draft202012Validator(tags_schema)

    errors: list[str] = []

    for path in sorted(GENRES_DIR.rglob("*.yaml")):
        errors.extend(collect_errors(genre_validator, load_yaml(path), path.relative_to(ROOT)))

    for path in sorted(TAGS_DIR.glob("*.yaml")):
        errors.extend(collect_errors(tags_validator, load_yaml(path), path.relative_to(ROOT)))

    if errors:
        for err in errors:
            print(err)
        return 1

    print("Schema validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
