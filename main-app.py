from calculator import Calculator
from calculator_scientific import sci_Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    a = float(input('please enter value\n'))
    #trig functions must be in radians with math.trig functions
    #want to store a radian into a, and if it's a degree, convert it to radian

    return a


def displayResult(x: float):
    print(x, "\n")

def switchUnitsMode():
    a = 'Degrees'
    b = 'Radians'


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))

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

        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
