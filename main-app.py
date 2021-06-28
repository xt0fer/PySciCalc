from display_options import DisplayOptions
from calculator import Calculator
#from calculator_scientific import sci_Calculator
from memoryOptions import Memory
import math

#chuck was here

calculator  = Calculator()
display = DisplayOptions()
calDisplay = DisplayOptions()
mem = Memory()

#global variable for display (use global if needed in function)

def getTwoNumbers():

    
    a = input("first number? ")
    if a == 'display':
        a = calculator.current_state
    else:
        a = float(a)
    b = input("second number? ")
    if b == 'display':
        b = calculator.current_state
    else:
        b= float(b)
    return a, b

def getOneNumber():

    #trig functions must be in radians with math.trig functions
    #want to store a radian into a, and if it's a degree, convert it to radian
    
    a = input('please enter value for one number: \n')
    if a == 'display':
        a = calculator.current_state
    else:
        a = float (a)
    return a

def getMenuOption():
    a = input(":")
    return a


def displayResult(x,calDisplay):
    
    if x == 'err':
        print('---|',x,'|---\n')
        calculator.current_state = x
    else:
        if calDisplay.currentDisplay == 'decimal':
            print('---|',float(x),'|---\n')
        elif calDisplay.currentDisplay == 'octal':
            print('---|',oct(int(x)),'|---\n')
        elif calDisplay.currentDisplay == 'binary':
            print('---|',bin(int(x)),'|---\n')
        elif calDisplay.currentDisplay == 'hexadecimal':
            print('---|',hex(int(x)),'|---\n')
        else:
            print('---|',float(x),'|---\n')
        calculator.current_state = float(x)


def main_menu(calDisplay):
   
    print('\n1. Switch Display by Choice: \n   display options: decimal, octal, binary, hexadecimal\n   or iterate')
    print('\n2. Switch Trig calculations to Degrees or Radians')
    print('\n3. Do Math')
    print('\n4. Quit')
    while True:
        menuChoice = input('\nPlease enter one of the main menu options 1-4. Press 4 to quit from the Main Menu.\n:').lower()
        if menuChoice == '4':# or 'quit' or 'q':
            print('You selected Menu Choice 4')
            break
        elif menuChoice == '1':
            print('\nYou selected Menu Choice 1')
            print('Your current display mode is: '+  calDisplay.currentDisplay  + '. Please select one of the following options(number):')
            print('1. Decimal, 2. Octal, 3. binary, 4. hexadecimal, 5. iterate')
            a = getMenuOption()
            calDisplay.switch_modes(a)
            print('\nYour current display is: ' + calDisplay.currentDisplay)



        elif menuChoice == '2':
            print('\nYou selected Menu Choice 2')
            print('Your current trig measurement is: ' + calDisplay.currentTrig + '. Please select one of the following:')
            print('1. Degrees, 2. Radians, 3. Iterate')
            a = getMenuOption()
            calDisplay.switch_trig(a)
            print('Your current trig measurement is: ' + calDisplay.currentTrig)
        
        elif menuChoice == '3':
            print('\nYou selected Menu Choice 3')
            print("Performing Calculations\n")
            performCalcLoop(Calculator(),calDisplay)
            
           
        else:
            print('this is not a valid input')


def performCalcLoop(calc,calDisplay):
    
    print("calculator is in: " + calDisplay.currentTrig)
    print('Your current display is: '+ calDisplay.currentDisplay)
    print("Please enter a math operation. Enter 'help' for options. Enter q for the main menu")
    displayResult(calculator.current_state,calDisplay)
    while True:
        while calculator.current_state == 'err':
            choice = input("\n: ").lower()
            if choice == 'clear':
                displayResult(0,calDisplay)
            elif choice == 'q':
                break
            else:
                print('---|',calculator.current_state,'|---')
                print('please clear display')

        choice = input(":").lower()
        
        #commands to run

        if choice == 'q':
            break  # user types q to quit calculator.
        elif choice == 'switch':
            main_menu(DisplayOptions())
        elif choice == 'help':
            print("\nList of commands:")
            print("'q' for quit")
            print("'clear' set display to 0")
            print("'display' to use number in display")
            print("Operations: 'add', 'subtract', 'multiply', 'divide', 'square', 'square root', 'inverse', 'invert', 'factorial'")
            print("'sin', 'cos', 'tan', 'inverse sin', 'inverse cos', 'inverse tan'")
            print("1. M+, 2. MC, 3. MRC\n")
        elif choice == 'clear':

            displayResult(0,calDisplay)    
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b),calDisplay)
        elif choice == '1':
            mem.memoryAdd(calculator.current_state)
        elif choice == '2':
            mem.memoryClear()
        elif choice == '3':
            mem.memoryRecall()
            print("Memory Value: " + str(mem.memoryValue))

        #trig functions

        elif choice == 'sin':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                
                a = math.radians(a)
                a = calc.sin(a)
                displayResult(a,calDisplay)
            else:    
                print('radians mode: ')
                displayResult(calc.sin(a),calDisplay)
        elif choice == 'cos':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.cos(a)
                displayResult(a,calDisplay)    
            else:
                displayResult(calc.cos(a),calDisplay)
        elif choice == 'tan':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.tan(a)
                displayResult(a,calDisplay)    
            else:
                displayResult(calc.tan(a),calDisplay)
        elif choice == 'inverse sin':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.inverse_sin(a)
                displayResult(a,calDisplay)  
            else:  
                displayResult(calc.inverse_sin(a),calDisplay)
        elif choice == 'inverse cos':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.inverse_cos(a)
                displayResult(a,calDisplay) 
            else:   
                displayResult(calc.inverse_cos(a),calDisplay)
        elif choice == 'inverse tan':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.inverse_tan(a)
                displayResult(a,calDisplay)
            else:    
                displayResult(calc.inverse_tan(a),calDisplay)

        elif choice == 'subtract':
            a, b = getTwoNumbers()
            displayResult(calc.subtract(a, b),calDisplay)
        elif choice == 'multiply':
            a, b = getTwoNumbers()
            displayResult(calc.multiply(a, b),calDisplay)
        elif choice == 'divide':
            a, b = getTwoNumbers()
            displayResult(calc.divide(a, b),calDisplay)
        elif choice == 'square':
            a = getOneNumber()
            displayResult(calc.square(a),calDisplay)
        elif choice == 'square root':
            a = getOneNumber()
            displayResult(calc.square_root(a),calDisplay)
        elif choice == 'inverse':
            displayResult(calc.divide(1,calculator.current_state),calDisplay)
        elif choice == "invert":
            displayResult(-1*calculator.current_state,calDisplay)
        elif choice == 'factorial':
            a = getOneNumber()
            displayResult(calc.factorial(a),calDisplay)
        elif choice == 'variable exponentiation':
            a = getTwoNumbers()
            displayResult(calc.variable_exponentiation(a,b),calDisplay)
        elif choice == "compound interest":
            p = float(input('What is the principal investment amount:'))
            r = float(input('What is the annual interest rate (percentage):')) * .01
            n = float(input('What is the number of times that interest is compounded per year:'))
            t = float(input('For how many years:'))
            a = p * calc.variable_exponentiation((1 + calc.divide(r,n)),(n*t))
            print('you can make',p,'turn into',a)
            displayResult(a,calDisplay)


        else:
            print("That is not a valid input.\n")
        
        
        


# main start
def main():


    #currentTrig = 'degrees'
    #currentDisplayMode = 'decimal'

    #firstCalculator = display()

    #Here are the following options: ')

    
    calc = Calculator()
    calDisplay = DisplayOptions()
    calDisplay.currentDisplay = 'decimal'
    calDisplay.currentTrig = 'radian'
    print('---------------------------\nWelcome to our Calculator!\n(work in progress)\n---------------------------')
    print('Your current mode is decimal')
    print('Your current TrigMeasurement is radian')
    

    displayResult(0,calDisplay)
    

    main_menu(calDisplay)  
    
    print('\n-------------------------\nBye!!! Come Back Soon!!!)\n-------------------------')
    

    


if __name__ == '__main__':
    main()