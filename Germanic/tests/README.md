# Germanic Pipeline Tests

Unit tests for the Germanic/OE FST tools.

## Running Tests

```bash
cd Germanic/tests
python -m pytest test_english_apply_down_stats.py
```

Or with unittest:
```bash
python -m unittest test_english_apply_down_stats
```

## Fixtures

Test data files are in `fixtures/`:
- `english_rows.tsv` — Sample English lexeme rows for testing
