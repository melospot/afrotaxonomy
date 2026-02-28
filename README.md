# Afrotaxonomy

A structured, file-based taxonomy for African music genres and subgenres.

## Repository layout
- `schema/`
  - `genre.schema.json`
  - `tags.schema.json`
- `data/`
  - `genres/` (source of truth, organized by region/country)
  - `tags/` (controlled vocabularies)
  - `mappings/` (optional external platform mappings)
  - `relations.yaml` (cross-genre edges)
- `build/dist/` (compiled outputs)
- `tools/` (build/validate/lint scripts)
- `docs/` (editorial and taxonomy policy docs)
- `tests/` (schema + integrity tests)
- `.github/workflows/validate.yml` (CI checks)

## Genre file minimum
```yaml
id: example_genre
name: Example Genre
parents: [african_pop]
```

## Build and validation
```bash
python tools/lint.py
python tools/check_duplicates.py
python tools/validate.py
python tools/build.py
pytest -q
```

## Subgenre rule
- Every subgenre is its own file and points to its parent via `parents`.
