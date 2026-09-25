import unittest

from calc import add, divide, multiply, power, subtract


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-4, 2.5), -10.0)
        self.assertEqual(multiply(7, 0), 0)
        self.assertEqual(multiply(1.5, 2.0), 3.0)

    def test_multiply_rejects_non_numeric(self):
        for bad in ("a", None, True, False, [1], 1j):
            with self.subTest(bad=bad, position="a"):
                with self.assertRaisesRegex(TypeError, "argument 'a' must be an int or float"):
                    multiply(bad, 3)
            with self.subTest(bad=bad, position="b"):
                with self.assertRaisesRegex(TypeError, "argument 'b' must be an int or float"):
                    multiply(3, bad)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(-3, 2), 9)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(9, 0.5), 3.0)

    def test_power_zero_negative_exponent(self):
        for exponent in (-1, -2, -0.5):
            with self.subTest(exponent=exponent):
                with self.assertRaisesRegex(ValueError, "Cannot raise zero to a negative power"):
                    power(0, exponent)


if __name__ == "__main__":
    unittest.main()
