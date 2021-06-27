from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestCalcMemory(TestCase):

    def __run_add_to_memory_test(self, calc_obj, tests):
        for num_to_add, expected in tests:
            calc_obj.add_to_memory(num_to_add)
            actual = calc_obj.get_memory()
            error_message = self.__return_calc_error(num_to_add, expected, actual)
            self.assertEqual(expected, actual, error_message)
    
    def __run_clear_memory_test(self, calc_obj, tests):
        for num_to_add, expected in tests:
            calc_obj.add_to_memory(num_to_add)
            calc_obj.reset_memory()
            actual = calc_obj.get_memory()
            error_message = self.__return_calc_error(num_to_add, expected, actual)
            self.assertEqual(expected, actual, error_message)

    def __return_calc_error(self, num_to_add, exp, act):
        result = f"""
        {ErrorColors.GREEN}Expected: ({num_to_add}) -> {exp}
        {ErrorColors.RED}Actual:   ({num_to_add}) -> {act}{ErrorColors.RESET}
        """
        return result

    def test_add_to_memory(self):
        c = Calculator()
        self.__run_add_to_memory_test(c, [ # (val_to_add, expected)
            (2, 2), (3, 5), (-3, 2), (5, 7), (10, 17), (8, 25), (7, 32), (-6, 26)
        ])
    
    def test_clear_memory(self):
        c = Calculator()
        self.__run_clear_memory_test(c, [ # (val_to_add, expected)
            (2, 0), (3, 0), (-3, 0), (5, 0), (10, 0), (8, 0), (7, 0), (-6, 0)
        ])