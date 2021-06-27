from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalcStateChange(TestCase):

    def _test(self, calc_object, method, tests):
        for num, expected_state in tests:
            starting_state = calc_object.get_state()  # store the starting state
            result = method(starting_state, num)      # stort the result of the operation using starting state
            calc_object.set_state(result)             # set the new state of the object
            error_message = self.__return_calc_error(starting_state, num, calc_object.get_state(), expected_state)
            self.assertEqual(calc_object.get_state(), expected_state, error_message)
    
    def __return_calc_error(self, starting_state, num, actual_state, expected_state):
        result = f"""
        {ErrorColors.GREEN}Expected: ({starting_state}, {num}) -> {expected_state}
        {ErrorColors.RED}Actual:   ({actual_state}, {num}) -> {actual_state}{ErrorColors.RESET}
        """
        return result

    # The test results are cummulative
    def test_add_state(self):
        c = Calculator()
        self._test(c, c.add, [  # (num_to_add, expected_state)
            (1,1),(2,3),(5,8),(16,24),(-4,20),(-77,-57),(23,-34),(56,22)
        ])

    def test_subtract_state(self):
        c = Calculator()
        self._test(c, c.subtract, [ # (num_to_subtract, expected_state)
            (1,-1),(2,-3),(5,-8),(16,-24),(-4,-20),(-77,57),(23,34),(56,-22)
        ])

    def test_multiply_state(self):
        c = Calculator()
        c.set_state(1)
        self._test(c, c.multiply, [ # (num_to_multiply, expected_state)
            (1,1),(2,2),(5,10),(16,160),(-4,-640),(-77,49280),(23,1133440),(56,63472640)
        ])

    def test_divide_state(self):
        c = Calculator()
        c.set_state(50000)
        self._test(c, c.divide, [ # (divisor, expected_state)
            (3,16666.666666666668),(2,8333.333333333334),(5,1666.6666666666667),
            (2,833.3333333333334),(10,83.33333333333334),(10,8.333333333333334)
        ])
