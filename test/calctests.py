from unittest import TestCase
# from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalculator(TestCase):

    def _test(self, method, tests):
        for num1, num2, expected in tests:
            actual = method(num1, num2)
            error_message = self._return_calc_error(num1, num2, expected, actual)
            self.assertEqual(expected, actual, error_message)
    
    def _return_calc_error(self, n1, n2, exp, act):
        result = f"""
        Expected: ({n1}, {n2}) -> {exp}
        Actual:   ({n1}, {n2}) -> {act}
        """
        return result

    def test_add(self):
        c = Calculator()
        self._test(c.add, [
            (1, 2, 3), (2, 3, 5), (6, 5, 11), (7, 10, 17),
            (8, 9, 17), (31, 2, 33), (-13, 3, -10), (-5, -5, -2)
        ])

    def test_subtract(self):
        c = Calculator()
        self._test(c.subtract, [
            (1, 2, -1), (4, 3, 1), (10, 5, 5), (67, 10, 57),
            (-5, -10, 20), (31, 2, 29), (-13, 3, -16), (-6, 2, 33)
        ])

    # def test_multiply(self):
    #     c = Calculator()
    #     self._test(c.multiply, [
    #         (1, 2, 2), (4, 3, 12), (10, 0, 0), (30, 3, 90),
    #         (-5, -10, 500), (31, 2, 62), (-11, 3, -33), (-6, 2, -12)
    #     ])

    # def test_divide(self):
    #     c = Calculator()
    #     self._test(c.divide, [
    #         (1, 2, 2), (4, 3, 12), (10, 0, 0), (30, 3, 90),
    #         (-5, -10, 500), (31, 2, 62), (-11, 3, -33), (-6, 2, -12)
    #     ])

    # def test_sub(self):
    #     c = Calculator()
    #     self.assertEqual(c.sub(9, 3), 6)
