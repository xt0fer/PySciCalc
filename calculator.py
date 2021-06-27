import math

class Calculator:
    
    
    def __init__(self):
        self.current_state= None
        

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x*y

    def divide(self, x, y):
        if y == 0:
            return('err')
        else:
            return x / y


    def square(self, x):
        return x * x

    def square_root(self, x):
        return math.sqrt(x)

    

# add lots more methods to this calculator class.

    #trig functions

    def sin(self, radians):
        return math.sin(radians)
    
    def cos(self, radians):
        return math.cos(radians)
    
    def tan(self, radians):
        return math.tan(radians)

    def inverse_sin(self, radians):
        return math.asin(radians)

    def inverse_cos(self, radians):
        return math.acos(radians)
    
    def inverse_tan(self, radians):
        return math.atan(radians)

    #convert to radians or degrees on screen

    def switch_units_mode(self, radians):
        return math.degrees(radians)

    def switch_units_mode(self, degrees):
        return math.radians(degrees)    
