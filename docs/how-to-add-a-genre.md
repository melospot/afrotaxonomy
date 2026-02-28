# How To Add A Genre

## 1) Pick the right location
- Place the file under `data/genres/<region>/<country>/` where possible.
- Use `data/genres/foundations/` for broad umbrella genres.

## 2) Create the YAML file
Minimum required:
```yaml
id: example_genre
name: Example Genre
parents: [african_pop]
```

Recommended:
```yaml
aliases: [Example]
origin:
  countries: [ZA]
description: Short neutral description.
status: active
```

## 3) If adding a subgenre
- Add a separate file for it.
- Link to parent with `parents: [parent_id]`.
- Optionally add the child ID to the parent's `subgenres`.

## 4) Validate
- Run `python tools/lint.py`
- Run `python tools/check_duplicates.py`
- Run `python tools/validate.py`
