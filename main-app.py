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
    a = input("please enter a menu option\n")
    return a


def displayResult(x):
    
    if x == 'err':
        print('---',x,'---')
        calculator.current_state = x
    else:
        print('---',float(x),'---')
        calculator.current_state = float(x)




def main_menu(calDisplay):
    #current_menu = 
    #currentTrigMode = 'degrees'
    print('\n1. Switch Display by Choice: \n   display options: decimal, octal, binary, hexadecimal\n   or iterate')
    print('\n2. Switch Trig calculations to Degrees or Radians')
    print('\n3. Do Math')
    print('\n4. Quit')
    while True:
        menuChoice = input('Please enter one of the main menu options 1-4. Press 4 to quit from the Main Menu.\n').lower()
        if menuChoice == '4':# or 'quit' or 'q':
            print('You selected Menu Choice 4')
            break
        elif menuChoice == '1':
            print('You selected Menu Choice 1')
            print('Your current display mode is: '+  calDisplay.currentDisplay  + '. Please select one of the following options:')
            print('1. Decimal, 2. Octal, 3. binary, 4. hexadecimal, 5. iterate')
            a = getMenuOption()
            calDisplay.switch_modes(a)
            print('Your current display is: ' + calDisplay.currentDisplay)



        elif menuChoice == '2':
            print('You selected Menu Choice 2')
            print('Your current trig measurement is: ' + calDisplay.currentTrig + '. Please select one of the following:')
            print('1. Degrees, 2. Radians, 3. Iterate')
            a = getMenuOption()
            calDisplay.switch_trig(a)
            print('Your current trig measurement is: ' + calDisplay.currentTrig)
        
        elif menuChoice == '3':
            print('You selected Menu Choice 3')
            print("Performing Calculations\n")

            numberToChange = None
            if calDisplay.currentDisplay == 'decimal':
                performCalcLoop(Calculator())
            elif calDisplay.currentDisplay == 'octal':

                print(calDisplay.currentDisplay)
                numberToChange = performCalcLoop(Calculator())
                if numberToChange == None:
                    pass
                else:
                    oct(int(numberToChange))
            elif calDisplay.currentDisplay == 'binary':
                if numberToChange == None:
                    pass
                else:
                    bin(int(numberToChange))
            elif calDisplay.currentDisplay == 'hexadecimal':
                if numberToChange == None:
                    pass
                else:
                    hex(int(numberToChange))

            #performCalcLoop(Calculator())
            #print("Leaving Calculations. Back to the main menu\n")
           
        else:
            print('this is not a valid input')



#def stateOfDisplay():
    #current_state = 
     


def performCalcLoop(calc):
    
    print("calculator is in: " + display.currentTrig)
    while True:
        while calculator.current_state == 'err':
            choice = input("\n: ").lower()
            if choice == 'clear':
                displayResult(0)
            elif choice == 'q':
                break
            else:
                print('---',calculator.current_state,'---')
                print('please clear display')

        choice = input("Please enter a math function. Enter help for options. Enter q for the main menu\n").lower()
        
        #commands to run

        if choice == 'q':
            break  # user types q to quit calculator.
        elif choice == 'switch':
            main_menu(DisplayOptions())
        elif choice == 'help':
            print("List of commands:")
            print("'q' for quit")
            print("'clear' set display to 0")
            print("'display' to use number in display")
            print("Operations: 'add', 'subtract', 'multiply', 'divide', 'square', 'square root', 'inverse', factorial")
            print("1. M+, 2. MC, 3. MRC")
        elif choice == 'clear':

            displayResult(0)    
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == '1':
            mem.memoryAdd(calculator.current_state)
        elif choice == '2':
            mem.memoryClear()
        elif choice == '3':
            mem.memoryRecall()
            print("Memory Value: " + str(mem.memoryValue))

        #trig functions

        elif choice == 'sin':
            print('current display is: ' + calDisplay.currentTrig)
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                
                a = math.radians(a)
                a = calc.sin(a)
                displayResult(a)
            else:    
                print('radians mode: ')
                displayResult(calc.sin(a))
        elif choice == 'cos':
            a = getOneNumber()
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.cos(a)
                displayResult(a)    
            else:
                displayResult(calc.cos(a))
        elif choice == 'tan':
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.tan(a)
                displayResult(a)    
            else:
                displayResult(calc.tan(a))
        elif choice == 'inverse sin':
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.inverse_sin(a)
                displayResult(a)  
            else:  
                displayResult(calc.inverse_sin(a))
        elif choice == 'inverse cos':
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.inverse_cos(a)
                displayResult(a) 
            else:   
                displayResult(calc.inverse_cos(a))
        elif choice == 'inverse tan':
            if calDisplay.currentTrig == 'degrees':
                a = math.radians(a)
                a = calc.inverse_tan(a)
                displayResult(a)
            else:    
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

        elif choice == 'inverse':
            a = getOneNumber
            displayResult()


        else:
            print("That is not a valid input.")
        
        
        


# main start
def main():


    currentTrig = 'degrees'
    currentDisplayMode = 'decimal'

    #firstCalculator = display()

    #Here are the following options: ')


    calc = Calculator()
    calDisplay = DisplayOptions()

    print('Your current mode is decimal')
    print('Your current TrigMeasurement is radian')
    print('\nWelcome to our Calculator!')

    displayResult(0)

    main_menu(calDisplay)  
    
    print('\n\nthis is the best calculator :)\n')
    

    print("Done Calculating.")


if __name__ == '__main__':
    main()