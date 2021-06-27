import math
from collections import deque


class Calculator:

    def __init__(self):
        self.state = 0
        self.display_q = deque(['dec', 'bin', 'oct', 'hex'])
        self.display_mode = self.display_q[0]
        self.memory = 0

    # ---------------------------------------------------
    # *************** CORE FEATURES *********************
    # ---------------------------------------------------
    def set_state(self, x):
        self.state = x

    def get_state(self):
        return self.state

    def clear(self):
        self.state = 0

    def set_error(self, err):
        self.state = f'Err: {err}'
        return self.state

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if x == 0 or y == 0:
            return self.set_error('cannot divide by zero')
        return x / y

    def square(self, x):
        return x * x

    def square_root(self, x):
        return math.sqrt(x)
    
    def inverse(self, x):
        return 1 / x

    def switch_sign(self, x):
        return -x

    # ---------------------------------------------------
    # *************** SCIENTIFIC FEATURES ***************
    # ---------------------------------------------------

    # ------------------- SWITCH DISPLAY METHODS -------------------
    def show_current_display_mode(self):
        return self.display_mode

    def switch_display_mode(self, mode: str=None):
        if not mode:  # If no mode given
            self.display_q.rotate()
            self.display_mode = self.display_q[0]
        else:
            self.__set_new_display_mode(mode)
    
    def __set_new_display_mode(self, mode):
        if mode not in ('bin', 'oct', 'hex', 'dec'):
            self.set_error('please enter valid display mode: bin | oct | hex | dec')
        else:
            while self.show_current_display_mode() != mode:
                self.display_q.rotate()
                self.display_mode = self.display_q[0]

    # ----------------- TRIG METHODS ------------------
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

    # ------------------ MEMORY METHODS -------------
    def add_to_memory(self, x):
        self.memory += x

    def get_memory(self):
        return self.memory

    def reset_memory(self):
        self.memory = 0

    # --------------- BONUS METHODS -----------------
    def factorial(self, x):
        if abs(x) > 0:
           return abs(x) * self.factorial(abs(x) - 1)
        else:
            return 1

    def natural_log(self, x):
        return math.log(x)

    def log(self, x, y):
        return math.log(x, y)
