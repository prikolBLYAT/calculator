import unittest
from main import calculate, format_result

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(2, '+', 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(10, '-', 4), 6)

    def test_multiplication(self):
        self.assertEqual(calculate(3, '*', 7), 21)

    def test_division(self):
        self.assertEqual(calculate(8, '/', 2), 4)

    def test_division_by_zero(self):
        self.assertEqual(calculate(5, '/', 0), "Ошибка: деление на ноль")

    def test_invalid_operation(self):
        self.assertEqual(calculate(2, '^', 3), "Неизвестная операция")

    def test_non_number_inputs(self):
        self.assertEqual(calculate("a", '+', 3), "Ошибка: аргументы должны быть числами")

    def test_format_normal(self):
        self.assertEqual(format_result(2, '+', 3, 5), "2 + 3 = 5")

    def test_format_error(self):
        self.assertEqual(format_result(2, '/', 0, "Ошибка: деление на ноль"), "Ошибка: деление на ноль")

    def test_addition_negative(self):
        self.assertEqual(calculate(-2, '+', -3), -5)

    def test_subtraction_negative(self):
        self.assertEqual(calculate(-2, '-', -3), 1)

    def test_subtraction_negative(self):
        self.assertEqual(calculate(-2, '-', 3), -5)

    def test_multiplication_negative(self):
        self.assertEqual(calculate(-2, '*', 3), -6)

    def test_multiplication_negative(self):
        self.assertEqual(calculate(-2, '*', -3), 6)

    def test_division_negative(self):
        self.assertEqual(calculate(-4, '/', -2), 2)

    def test_division_negative(self):
        self.assertEqual(calculate(-4, '/', 2), -2)


if __name__ == '__main__':
    unittest.main()
