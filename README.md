# gitweave-test

Sandbox repository for live GitWeave graph tests.

Run tests with:

```sh
python3 -m unittest discover -s tests
```

## Available functions

`calc.py` provides:

- `add(a, b)` — returns `a + b`.
- `subtract(a, b)` — returns `a - b`.
- `divide(a, b)` — returns `a / b`; raises `ValueError` if `b` is zero.
