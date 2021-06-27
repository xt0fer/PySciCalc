
import math 


class Calculator:

    def __init__(self):
        self.display = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if x == 0 or y == 0:
            return "cannot divide by 0"
        return x / y

    def square(self, x):
        return x ** 2  

    def square_root(self, x,):
        return math.sqrt (x) 

    def exponentiate(self, x, y):
        return x ** y
    
    def inverse(self, x):
        return 1/x 

    def invert_sign(self, x):
        return -x 

        
    
    
    

# add lots more methods to this calculator class.
