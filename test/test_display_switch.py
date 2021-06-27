from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalcTwoArgs(TestCase):

    def _test(self, calc_object, tests):
        for expected_mode in tests:
            current_mode = calc_object.show_current_display_mode()
            error_message = self.__return_calc_error(current_mode, expected_mode)
            calc_object.switch_display_mode()
            self.assertEqual(current_mode, expected_mode, error_message)
    
    def __return_calc_error(self, current_mode, expected):
        result = f"""
        {ErrorColors.GREEN}Expected: {expected}
        {ErrorColors.RED}Actual: {current_mode}{ErrorColors.RESET}
        """
        return result

    # TWO ARG TESTS
    def test_display_switch(self):
        c = Calculator()
        self._test(c, ['dec', 'hex', 'oct', 'bin', 'dec'])