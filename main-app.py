from display_options import DisplayOptions
from calculator import Calculator
from calculator_scientific import sci_Calculator

#chuck was here

currentState = 0

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
    a = float(input('please enter value\n'))
    #trig functions must be in radians with math.trig functions
    #want to store a radian into a, and if it's a degree, convert it to radian

    return a

def getMenuOption():
    a = str(input("please enter a menu option"))
    return a

currentDisplayMode = 'decimal'




def displayResult(x: float):
    print(x)

def displayDisplay(x):
    print(x)

def main_menu(calDisplay):
    print('\n1. Switch Display by Choice: \n   display options: decimal, octal, binary, hexadecimal\n   or iterate')
    print('\n2. Switch Trig calculations to Degrees or Radians')
    print('\n3. Do Math')
    print('\n4. Quit')
    while True:
        menuChoice = input('\n: ').lower()
        if menuChoice == '4' or 'quit' or 'q':
            break
        elif menuChoice == '1':
            a = getMenuOption()
            currentMode = displayDisplay(calDisplay.switch_modes(a))

        elif menuChoice == '2':
            a = getMenuOption()
            currentTrig = displayDisplay(calDisplay.switch_trig(a)) 
        elif menuChoice == '3':
           pass
        else:
            print('this is not a valid input')







        



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

    currentTrig = 'degrees'
    currentDisplayMode = 'decimal'

    calc = Calculator()
    calDisplay = DisplayOptions()
    
    main_menu()  
    
    performCalcLoop(calc)
    
    print('\n\nthis is the best calculator :)\n')
    

    print("Done Calculating.")


if __name__ == '__main__':
    main()