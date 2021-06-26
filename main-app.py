from calculator import Calculator

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
    a = float(input('number? '))
    return a

def displayResult(x: float):
    print(x)

def currentState():
    return 

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
