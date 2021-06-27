from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalcTwoArgs(TestCase):

    def _test(self, method, tests):
        for num1, num2, expected in tests:
            actual = method(num1, num2)
            error_message = self.__return_calc_error(num1, num2, expected, actual)
            self.assertEqual(expected, actual, error_message)
    
    def __return_calc_error(self, n1, n2, exp, act):
        result = f"""
        {ErrorColors.GREEN}Expected: ({n1}, {n2}) -> {exp}
        {ErrorColors.RED}Actual:   ({n1}, {n2}) -> {act}{ErrorColors.RESET}
        """
        return result

    # TWO ARG TESTS
    def test_add(self):
        c = Calculator()
        self._test(c.add, [
            (1, 2, 3), (2, 3, 5), (6, 5, 11), (7, 10, 17), 
            (8, 9, 17), (31, 2, 33), (-13, 3, -10), (-5, -5, -10)
        ])

    def test_subtract(self):
        c = Calculator()
        self._test(c.subtract, [
            (1, 2, -1), (4, 3, 1), (10, 5, 5), (67, 10, 57),
            (-5, -10, 5), (31, 2, 29), (-13, 3, -16), (-6, 2, -8)
        ])

    def test_multiply(self):
        c = Calculator()
        self._test(c.multiply, [
            (1, 2, 2), (4, 3, 12), (10, 0, 0), (30, 3, 90),
            (-5, -10, 50), (31, 2, 62), (-11, 3, -33), (-6, 2, -12)
        ])

    def test_divide(self):
        c = Calculator()
        self._test(c.divide, [
            (1, 2, 0.5), (12, 3, 4), (9, 2, 4.5), (7, 7, 1), (4, 0, 'Err: cannot divide by zero'),
            (-10, 10, -1), (30, -3, -10), (-200, -2, 100), (-6, 2, -3)
        ])

    def test_log(self):
        c = Calculator()
        self._test(c.log, [
            (1,3,0.0),(2,2,1.0),(3,4,0.7924812503605781),(20,6,1.6719500161730103),(35,20,1.1868043392514251),
            (123,7,2.4729735634035324),(54,4,2.8774437510817346),(525,3,5.701190790597276),(262,5,3.4598069678497754),
            (100,89,1.0259619640926507)         
        ])
