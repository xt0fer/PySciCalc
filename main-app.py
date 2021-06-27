

from math import sqrt
from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getOneNumber():
    c = float(input("enter number"))
    return c


def displayResult(x: float):
    print(x, "\n")


def displayMenu():
    print("----------------------------")
    print("        Menu        ")
    print("Enter (+) for Addition")
    print("Enter (-) for Subtraction")
    print("Enter (*) for Multiplication")
    print("Enter (/) for Division")
    print("enter ('p') to the ^ power")
    print("enter ('s') for squared")
    print("Enter ('n') for Neg/Pos" )
    print("Enter ('i') for Inverse")
    print("enter ('sq') for Square Root")
    print("Enter ('c') for Clear")
    print("Enter (q) to Quit")
    print("----------------------------")

def performCalcLoop(calc):
    while True:
        displayMenu()

        choice = input("Hello make a selection ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == '+':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))

        elif choice == '-':
           a,b = getTwoNumbers()
           displayResult(a-b)
        
        elif choice == '*':
            a,b = getTwoNumbers()
            displayResult (a*b)

        elif choice == '/':
            a,b = getTwoNumbers()
            if b == 0:
                displayResult("[-] Error: Cannot divide by zero")
            else:
                displayResult(a/b)
                 
        elif choice == 'p':
            a,b = getTwoNumbers()
            displayResult(a**b)

        elif choice == 'sq':
            c = getOneNumber()
            displayResult(sqrt(c))
        
        elif choice == 'n':
            c = getOneNumber()
            displayResult(-c)

        elif choice == 'i':
            c = getOneNumber()
            if c == 0:
                displayResult("error cannot use 0")
            else:
                displayResult(1/c)
        
        elif choice == 's':
            c = getOneNumber()
            displayResult(c**2)

        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
