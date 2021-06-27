import math


class Calculator:

    def __init__(self):
        self.__state = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    # MY METHODS
    def set_state(self, x):
        self.__state = x

    def get_state(self):
        return self.__state

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def square(self, x):
        return x * x

    def square_root(self, x):
        return math.sqrt(x)
    
    def inverse(self, x):
        return 1 / x

    def sine(self, x):
        return math.sin(x)

    def cosine(self, x):
        return math.cos(x)

    def tangent(self, x):
        return math.tan(x)

    def inverse_sine(self, x):
        return math.asin(x)

    def inverse_cosine(self, x):
        return math.acos(x)

    def inverse_tangent(self, x):
        return math.atan(x)

    def factorial(self, x):
        if abs(x) > 0:
           return abs(x) * self.factorial(abs(x) - 1)
        else:
            return 1

    def switch_sign(self, x):
        return -x
    
    def natural_log(self, x):
        return math.log(x)

    def log(self, x, y):
        return math.log(x, y)


# add lots more methods to this calculator class.
