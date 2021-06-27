from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestTrigUnitSwitch(TestCase):

    def __switch_test(self, calc_object, tests):  # This tests switch display WITH NO arguments
        for expected_mode in tests:
            current_mode = calc_object.get_current_trig_unit()
            error_message = self.__return_calc_error(current_mode, expected_mode)
            calc_object.switch_units()
            self.assertEqual(current_mode, expected_mode, error_message)

    def __set_test(self, calc_object, tests):  # This tests switch display mode WITH arguments
        for input, expected in tests:
            actual = calc_object.switch_units(input)
            error_message = self.__return_calc_error(actual, expected)
            self.assertEqual(actual, expected, error_message)
    
    def __return_calc_error(self, current_mode, expected):
        result = f"""
        {ErrorColors.GREEN}Expected: {expected}
        {ErrorColors.RED}Actual: {current_mode}{ErrorColors.RESET}
        """
        return result

    # TWO ARG TESTS
    def test_trig_unit_switch(self):
        c = Calculator() # these are the expected ouputs
        self.__switch_test(c, ['deg', 'rad', 'deg', 'rad', 'deg', 'rad'])

    def test_trig_unit_set(self):
        c = Calculator()
        self.__set_test(c, [
            ('rad','rad'), ('deg','deg'),
            (1, 'Err: please enter a valid unit: deg | rad'),
            ('n', 'Err: please enter a valid unit: deg | rad'),
            ('ser', 'Err: please enter a valid unit: deg | rad'),
            ({}, 'Err: please enter a valid unit: deg | rad'),
            ([], 'Err: please enter a valid unit: deg | rad')
        ])