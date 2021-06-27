from calculator import Calculator
from calculator_scientific import sci_Calculator

#chuck was here
#global variable for display (use global if needed in function)
current_state = 0

def getTwoNumbers():

    global current_state
    a = input("first number? ")
    if a == 'display':
        a = current_state
    else:
        a = float(a)
    b = input("second number? ")
    if b == 'display':
        b = current_state
    else:
        b= float(b)
    return a, b

def getOneNumber():
    #trig functions must be in radians with math.trig functions
    #want to store a radian into a, and if it's a degree, convert it to radian
    global current_state
    a = input('please enter value: ')
    if a == 'display':
        a = current_state
    else:
        a = float (a)
    return a


def displayResult(x):
    global current_state
    
    if x == 'err':
        print(x)
    else:
        print('---',float(x),'---')
        current_state = float(x) 


def switchUnitsMode():
    a = 'Degrees'
    b = 'Radians'

#def stateOfDisplay():
    #current_state = 
     

def performCalcLoop(calc):
    global current_state
    while True:

        choice = input("\n: ").lower()
        
        #commands to run

        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'help':
            print("List of commands:")
            print("'q' for quit")
            print("'clear' set display to 0")
            print("'display' to use number in display")
            print("Operations: 'add', 'subtract', 'multiply', 'divide', 'square', 'square root', 'inverse', factorial")
        elif choice == 'clear':
            displayResult(0)
            current_state = 0    

        #trig functions    
        elif choice == 'sin':
            a = getOneNumber()
            displayResult(calc.sin(a))
            current_state = calc.sin(a)
        elif choice == 'cos':
            a = getOneNumber()
            displayResult(calc.cos(a))
            current_state = calc.cos(a)
        elif choice == 'tan':
            a = getOneNumber()
            displayResult(calc.tan(a))
            current_state = calc.tan(a)
        elif choice == 'inverse sin':
            a = getOneNumber()
            displayResult(calc.inverse_sin(a))
            current_state = calc.inverse_sin(a)
        elif choice == 'inverse cos':
            a = getOneNumber()
            displayResult(calc.inverse_cos(a))
            current_state = calc.inverse_cos(a)
        elif choice == 'inverse tan':
            a = getOneNumber()
            displayResult(calc.inverse_tan(a))
            current_state = calc.inverse_tan(a)

        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
            current_state = calc.add(a,b)
        elif choice == 'subtract':
            a, b = getTwoNumbers()
            displayResult(calc.subtract(a, b))
            current_state = calc.subtract(a,b)
        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(calc.multiply(a, b))
            current_state = calc.multiply(a,b)
        elif choice == 'divide':
            a, b = getTwoNumbers()
            displayResult(calc.divide(a, b))
            current_state = calc.divide(a,b)
        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.square(a))
            current_state = calc.square(a)
        elif choice == 'square root':
            a = getOneNumber()
            displayResult(calc.square_root(a))
            current_state = calc.square_root(a)
        elif choice == 'inverse':
            a = getOneNumber
            displayResult()

        else:
            print("That is not a valid input.")
        
        
        


# main start
def main():
    
    calc = Calculator()
    print('\n\nthis is the best calculator :)\n')
    displayResult(0)
    
    
    performCalcLoop(calc)
    
    
    print("Done Calculating.")


if __name__ == '__main__':
    main()
