"""Tiny calculator used to exercise GitWeave graphs."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    for name, value in (("a", a), ("b", b)):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(
                f"multiply() argument '{name}' must be an int or float, "
                f"not {type(value).__name__}"
            )
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    return base ** exponent
