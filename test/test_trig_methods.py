from unittest import TestCase
from test.error_colors import ErrorColors
from calculator import Calculator


class TestTrigMethods(TestCase):

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

    def test_sine(self):
        c = Calculator()
        self._test(c.sine, [
            (100,0.984807753012208),(45,0.7071067811865475),(151,0.48480962024633717),
            (34,0.5591929034707469),(265,-0.9961946980917455),(360,-2.4492935982947064e-16),
            (43,0.6819983600624985),(87,0.9986295347545738),(90,1.0)
        ])

    def test_cosine(self):
        c = Calculator()
        self._test(c.cosine, [
            (100,-0.1736481776669303),(45,0.7071067811865476),(151,-0.8746197071393957),
            (34,0.8290375725550416),(265,-0.08715574274765825),(360,1.0),(43,0.7313537016191705),
            (87,0.052335956242943966),(90,6.123233995736766e-17)
        ])

    def test_tangent(self):
        c = Calculator()
        self._test(c.tangent, [
            (100,-5.671281819617711),(45,0.9999999999999999),(151,-0.5543090514527691),
            (34,0.6745085168424267),(265,11.430052302761334),(360,-2.4492935982947064e-16),
            (43,0.9325150861376617),(87,19.08113668772816),(90,1.633123935319537e+16)
        ])

    def test_inverse_sine(self):
        c = Calculator()
        self._test(c.inverse_sine, [
            (12,0.21100172206374124),(25,0.45151844661923823),(23,0.4130729718520131),
            (34,0.6352912243478107),(34,0.6352912243478107)
        ])

    def test_inverse_cosine(self):
        c = Calculator()
        self._test(c.inverse_cosine, [
            (12,1.3597946047311553),(25,1.1192778801756584),(23,1.1577233549428836),
            (34,0.935505102447086),(34,0.935505102447086)
        ])

    def test_inverse_tangent(self):
        c = Calculator()
        self._test(c.inverse_tangent, [
            (12,0.20645531758085964),(25,0.4114299300931693),(23,0.3817348483668146),
            (34,0.5355612603445071),(34,0.5355612603445071)
        ])
