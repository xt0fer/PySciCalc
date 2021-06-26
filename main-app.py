from calculator import Calculator
from calculator_scientific import sci_Calculator

#chuck was here


def getTwoNumbers():
    a = input("first number? ")
    if a == 'display':
        a = currentState()
    else:
        a = float(a)
    b = input("second number? ")
    if b == 'display':
        b = currentState()
    else:
        b= float(b)
    return a, b

def getOneNumber():
<<<<<<< HEAD
    a = float(input('please enter value\n'))
    #trig functions must be in radians with math.trig functions
    #want to store a radian into a, and if it's a degree, convert it to radian

    return a

=======
    a = float(input('number? '))
    return a
>>>>>>> cd050b4c0fd9720bd3e4ec52a27bcd3c9f47d67e

def displayResult(x: float):
    print(x)

<<<<<<< HEAD
def switchUnitsMode():
    a = 'Degrees'
    b = 'Radians'

=======
def currentState():
    return 
>>>>>>> cd050b4c0fd9720bd3e4ec52a27bcd3c9f47d67e

def performCalcLoop(calc):
    while True:
        choice = input("\n: ").lower()
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'help':
            print("List of commands:")
            print("'q' for quit")
            print("'clear' set display to 0")
            print("Operations: 'add', 'subtract', 'multiply', 'divide', 'square', 'square root'")
        elif choice == 'clear':
            displayResult(0)    
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
<<<<<<< HEAD

        #trig functions    
        elif choice == 'sin':
            a = getOneNumber()
            displayResult(calc.sin(a))
        elif choice == 'cos':
            a = getOneNumber()
            displayResult(calc.cos(a))
        elif choice == 'tan':
            a = getOneNumber()
            displayResult(calc.tan(a))
        elif choice == 'inverse sin':
            a = getOneNumber()
            displayResult(calc.inverse_sin(a))
        elif choice == 'inverse cos':
            a = getOneNumber()
            displayResult(calc.inverse_cos(a))
        elif choice == 'inverse tan':
            a = getOneNumber()
            displayResult(calc.inverse_tan(a))
=======
        elif choice == 'subtract':
            a, b = getTwoNumbers()
            displayResult(calc.subtract(a, b))
        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(calc.multiply(a, b))
        elif choice == 'divide':
            a, b = getTwoNumbers()
            displayResult(calc.divide(a, b))
        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.square(a))
        elif choice == 'square root':
            a = getOneNumber()
            displayResult(calc.square_root(a))
>>>>>>> cd050b4c0fd9720bd3e4ec52a27bcd3c9f47d67e

        else:
            print("That is not a valid input.")
        
        
        


# main start
def main():
    current_display_result = 0
    calc = Calculator()
    print('\n\nthis is the best calculator :)\n')
    displayResult(0)
    
    
    performCalcLoop(calc)
    
    
    print("Done Calculating.")


if __name__ == '__main__':
    main()
