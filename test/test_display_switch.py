from logging import error
from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalcTwoArgs(TestCase):

    def __switch_test(self, calc_object, tests):  # This tests switch display WITH NO arguments
        for expected_mode in tests:
            current_mode = calc_object.show_current_display_mode()
            error_message = self.__return_calc_error(current_mode, expected_mode)
            calc_object.switch_display_mode()
            self.assertEqual(current_mode, expected_mode, error_message)

    def __set_test(self, calc_object, tests):  # This tests switch display mode WITH arguments
        for expected_mode in tests:
            calc_object.switch_display_mode(expected_mode)
            current_mode = calc_object.show_current_display_mode()
            error_message = self.__return_calc_error(current_mode, expected_mode)
            self.assertEqual(current_mode, expected_mode, error_message)
    
    def __return_calc_error(self, current_mode, expected):
        result = f"""
        {ErrorColors.GREEN}Expected: {expected}
        {ErrorColors.RED}Actual: {current_mode}{ErrorColors.RESET}
        """
        return result

    # TWO ARG TESTS
    def test_display_switch(self):
        c = Calculator() # these are the expected ouputs
        self.__switch_test(c, ['dec', 'hex', 'oct', 'bin', 'dec'])

    def test_display_set(self):
        c = Calculator()
        self.__set_test(c, ['dec', 'hex', 'oct', 'bin', 'oct', 'dec', 'dec', 'bin', 'oct'])