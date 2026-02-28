# Contributing

## Workflow
1. Fork and create a branch.
2. Add or edit genre/tag data in YAML.
3. Run checks:
   - `python tools/lint.py`
   - `python tools/check_duplicates.py`
   - `python tools/validate.py`
4. Submit a pull request with references for factual claims.

## Contribution standards
- Keep descriptions neutral and concise.
- Use controlled tag values from `data/tags/*.yaml`.
- Add sources for contested or emergent genre labels.
