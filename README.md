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
- `multiply(a, b)` — returns `a * b`; raises `TypeError` if either argument is not an `int` or `float` (`bool` is rejected).
- `divide(a, b)` — returns `a / b`; raises `ValueError` if `b` is zero.
- `power(base, exponent)` — returns `base ** exponent`.
