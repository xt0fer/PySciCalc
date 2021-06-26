from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalculator(TestCase):

    def _test_two_args(self, method, tests):
        for num1, num2, expected in tests:
            actual = method(num1, num2)
            error_message = self._return_calc_error_two_args(num1, num2, expected, actual)
            self.assertEqual(expected, actual, error_message)

    def _test_one_arg(self, method, tests):
        for num, expected in tests:
            actual = method(num)
            error_message = self._return_calc_error_one_arg(num, expected, actual)
            self.assertEqual(expected, actual, error_message)
    
    def _return_calc_error_two_args(self, n1, n2, exp, act):
        result = f"""
        {ErrorColors.GREEN}Expected: ({n1}, {n2}) -> {exp}{ErrorColors.RESET}
        {ErrorColors.RED}Actual:   ({n1}, {n2}) -> {act}{ErrorColors.RESET}
        """
        return result

    def _return_calc_error_one_arg(self, n1, exp, act):
        result = f"""
        {ErrorColors.GREEN}Expected: ({n1}) -> {exp}{ErrorColors.RESET}
        {ErrorColors.RED}Actual:   ({n1}) -> {act}{ErrorColors.RESET}
        """
        return result

    # TWO ARG TESTS
    def test_add(self):
        c = Calculator()
        self._test_two_args(c.add, [
            (1, 2, 3), (2, 3, 5), (6, 5, 11), (7, 10, 17),
            (8, 9, 17), (31, 2, 33), (-13, 3, -10), (-5, -5, -10)
        ])

    def test_subtract(self):
        c = Calculator()
        self._test_two_args(c.subtract, [
            (1, 2, -1), (4, 3, 1), (10, 5, 5), (67, 10, 57),
            (-5, -10, 5), (31, 2, 29), (-13, 3, -16), (-6, 2, -8)
        ])

    def test_multiply(self):
        c = Calculator()
        self._test_two_args(c.multiply, [
            (1, 2, 2), (4, 3, 12), (10, 0, 0), (30, 3, 90),
            (-5, -10, 50), (31, 2, 62), (-11, 3, -33), (-6, 2, -12)
        ])

    def test_divide(self):
        c = Calculator()
        self._test_two_args(c.divide, [
            (1, 2, 0.5), (12, 3, 4), (9, 2, 4.5), (7, 7, 1),
            (-10, 10, -1), (30, -3, -10), (-200, -2, 100), (-6, 2, -3)
        ])

    # ONE ARG TESTS
    def test_square(self):
        c = Calculator()
        self._test_one_arg(c.square, [
            (2, 4), (3, 9), (-3, 9), (5, 25),
            (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_square_root(self):
        c = Calculator()
        self._test_one_arg(c.square_root, [
            (2, 4), (3, 9), (-3, 9), (5, 25),
            (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_inverse(self):
        c = Calculator()
        self._test_one_arg(c.inverse, [
            (2, 4), (3, 9), (-3, 9), (5, 25),
            (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_switch_sign(self):
        c = Calculator()
        self._test_one_arg(c.switch_sign, [
            (2, -2), (3, -3), (-3, 3), (5, -5),
            (10, -10), (-8, 8), (-7, 7), (-6, 6)
        ])

    def test_sine(self):
        c = Calculator()
        self._test_one_arg(c.sine, [
            (2, 4), (3, 9), (-3, 9), (5, 25),
            (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_cosine(self):
        c = Calculator()
        self._test_one_arg(c.cosine, [
            (2, 4), (3, 9), (-3, 9), (5, 25),
            (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_tangent(self):
        c = Calculator()
        self._test_one_arg(c.tangent, [
            (2, 4), (3, 9), (-3, 9), (5, 25),
            (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    # def test_inverse_sine(self):
    #     c = Calculator()
    #     self._test_one_arg(c.inverse_sine, [
    #         (2, 4), (3, 9), (-3, 9), (5, 25),
    #         (10, 100), (8, 64), (7, 49), (-6, 36)
    #     ])

    # def test_inverse_cosine(self):
    #     c = Calculator()
    #     self._test_one_arg(c.inverse_cosine, [
    #         (2, 4), (3, 9), (-3, 9), (5, 25),
    #         (10, 100), (8, 64), (7, 49), (-6, 36)
    #     ])

    # def test_inverse_tangent(self):
    #     c = Calculator()
    #     self._test_one_arg(c.inverse_tangent, [
    #         (2, 4), (3, 9), (-3, 9), (5, 25),
    #         (10, 100), (8, 64), (7, 49), (-6, 36)
    #     ])
