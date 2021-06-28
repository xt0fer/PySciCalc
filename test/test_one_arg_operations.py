from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestOneArgOps(TestCase):

    def _test(self, method, tests):
        for num, expected in tests:
            actual = method(num)
            error_message = self.__return_calc_error(num, expected, actual)
            self.assertEqual(expected, actual, error_message)

    def __return_calc_error(self, n1, exp, act):
        result = f"""
        {ErrorColors.GREEN}Expected: ({n1}) -> {exp}
        {ErrorColors.RED}Actual:   ({n1}) -> {act}{ErrorColors.RESET}
        """
        return result

    def test_square(self):
        c = Calculator()
        self._test(c.square, [
            (2, 4), (3, 9), (-3, 9), (5, 25), (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_square_root(self):
        c = Calculator()
        self._test(c.square_root, [
            (2, 1.4142135623730951),(4, 2.0),(6, 2.449489742783178),(8, 2.8284271247461903),(10, 3.1622776601683795),
            (44, 6.6332495807108),(5, 2.23606797749979),(23, 4.795831523312719),(61, 7.810249675906654)
        ])

    def test_inverse(self):
        c = Calculator()
        self._test(c.inverse, [
            (1, 1.0),(2, 0.5),(3, 0.3333333333333333),(20, 0.05), (30, 0.03333333333333333),
            (40, 0.025),(-50, -0.02), (-100, -0.01),(-45, -0.022222222222222223)
        ])

    def test_switch_sign(self):
        c = Calculator()
        self._test(c.switch_sign, [
            (2, -2), (3, -3), (-3, 3), (5, -5), (10, -10), (-8, 8), (-7, 7), (-6, 6)
        ])

    def test_factorial(self):
        c = Calculator()
        self._test(c.factorial, [
            (-5, 120),(-1, 1),(1, 1),(2, 2),(0, 1),(6, 720),(4, 24),(9, 362880),(15, 1307674368000)
        ])

    def test_natural_log(self):
        c = Calculator()
        self._test(c.natural_log, [
            (1, 0.0),(2, 0.6931471805599453),(3, 1.0986122886681098),(20, 2.995732273553991),(35, 3.5553480614894135),
            (123, 4.812184355372417),(54, 3.9889840465642745),(525, 6.263398262591624),(262, 5.568344503761097),
            (100, 4.605170185988092)
        ])
