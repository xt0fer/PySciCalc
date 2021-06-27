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
        {ErrorColors.GREEN}Expected: ({n1}, {n2}) -> {exp}
        {ErrorColors.RED}Actual:   ({n1}, {n2}) -> {act}{ErrorColors.RESET}
        """
        return result

    def _return_calc_error_one_arg(self, n1, exp, act):
        result = f"""
        {ErrorColors.GREEN}Expected: ({n1}) -> {exp}
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
            (2, 4), (3, 9), (-3, 9), (5, 25), (10, 100), (8, 64), (7, 49), (-6, 36)
        ])

    def test_square_root(self):
        c = Calculator()
        self._test_one_arg(c.square_root, [
            (2, 1.4142135623730951),(4, 2.0),(6, 2.449489742783178),(8, 2.8284271247461903),(10, 3.1622776601683795),
            (44, 6.6332495807108),(5, 2.23606797749979),(23, 4.795831523312719),(61, 7.810249675906654)
        ])

    def test_inverse(self):
        c = Calculator()
        self._test_one_arg(c.inverse, [
            (1, 1.0),(2, 0.5),(3, 0.3333333333333333),(20, 0.05), (30, 0.03333333333333333),
            (40, 0.025),(-50, -0.02), (-100, -0.01),(-45, -0.022222222222222223)
        ])

    def test_switch_sign(self):
        c = Calculator()
        self._test_one_arg(c.switch_sign, [
            (2, -2), (3, -3), (-3, 3), (5, -5), (10, -10), (-8, 8), (-7, 7), (-6, 6)
        ])

    def test_sine(self):
        c = Calculator()
        self._test_one_arg(c.sine, [
            (1, 0.8414709848078965),(2, 0.9092974268256817),(3, 0.1411200080598672), 
            (20, 0.9129452507276277), (30, -0.9880316240928618), (40, 0.7451131604793488), 
            (-50, 0.26237485370392877), (-100, 0.5063656411097588),(-45, -0.8509035245341184)
        ])

    def test_cosine(self):
        c = Calculator()
        self._test_one_arg(c.cosine, [
            (1, 0.5403023058681398),(2, -0.4161468365471424),(3, -0.9899924966004454),
            (20, 0.40808206181339196),(30, 0.15425144988758405),(40, -0.6669380616522619),
            (-50, 0.9649660284921133),(-100, 0.862318872287684),(-45, 0.5253219888177297)
        ])

    def test_tangent(self):
        c = Calculator()
        self._test_one_arg(c.tangent, [
            (1, 1.557407724654902),(2, -2.185039863261519),(3, -0.1425465430742778),
            (20, 2.2371609442247427),(30, -6.4053311966462765),(40, -1.117214930923896),
            (-50, 0.2719006119976307),(-100, 0.587213915156929),(-45, -1.6197751905438615)
        ])

    def test_inverse_sine(self):
        c = Calculator()
        self._test_one_arg(c.inverse_sine, [
            (0.55, 0.5823642378687435),(-0.55, -0.5823642378687435),(0, 0.0),
            (1, 1.5707963267948966),(-1, -1.5707963267948966),(0.22, 0.22181447049679442),
            (-0.22, -0.22181447049679442),(0.65, 0.7075844367253556),(-0.65, -0.7075844367253556)
        ])

    def test_inverse_cosine(self):
        c = Calculator()
        self._test_one_arg(c.inverse_cosine, [
            (0.55, 0.9884320889261531),(-0.55, 2.15316056466364),(0, 1.5707963267948966),(1, 0.0),
            (-1, 3.141592653589793),(0.22, 1.3489818562981022),(-0.22, 1.792610797291691), 
            (0.65, 0.863211890069541), (-0.65, 2.278380763520252)
        ])

    def test_inverse_tangent(self):
        c = Calculator()
        self._test_one_arg(c.inverse_tangent, [
            (0.55, 0.5028432109278609),(-0.55, -0.5028432109278609),(0, 0.0),(1, 0.7853981633974483),
            (-1, -0.7853981633974483),(0.22, 0.21655030497608926),(-0.22, -0.21655030497608926),
            (0.65, 0.5763752205911837),(-0.65, -0.5763752205911837)
        ])

    def test_factorial(self):
        c = Calculator()
        self._test_one_arg(c.factorial, [
            (-5, 120),(-1, 1),(1, 1),(2, 2),(0, 1),(6, 720),(4, 24),(9, 362880),(15, 1307674368000)
        ])

    def test_natural_log(self):
        c = Calculator()
        self._test_one_arg(c.natural_log, [
            (1, 0.0),(2, 0.6931471805599453),(3, 1.0986122886681098),(20, 2.995732273553991),(35, 3.5553480614894135),
            (123, 4.812184355372417),(54, 3.9889840465642745),(525, 6.263398262591624),(262, 5.568344503761097),
            (100, 4.605170185988092)
        ])

    def test_log(self):
        c = Calculator()
        self._test_two_args(c.log, [
            (1,3,0.0),(2,2,1.0),(3,4,0.7924812503605781),(20,6,1.6719500161730103),(35,20,1.1868043392514251),
            (123,7,2.4729735634035324),(54,4,2.8774437510817346),(525,3,5.701190790597276),(262,5,3.4598069678497754),
            (100,89,1.0259619640926507)         
        ])
