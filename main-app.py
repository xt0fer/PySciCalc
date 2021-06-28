from calculator import Calculator
from colors import Colors

def get_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def get_one_number():
    c = float(input("Enter a number: "))
    return c


def displayResult(calc):
    print(Colors.GREEN)
    print('*--------------  Calculator ----------------*')
    print(f'| {calc.trig_mode}                                  |')
    print('|------------------------------------------|')
    print(f'                   {calc.get_state()}                      ')
    print(Colors.RESET)


def displayMenu():
    print(Colors.YELLOW)
    print("----------------------------------------------")
    print("|                  MENU                      |")
    print("|    Enter (+) for Addition                  |")
    print("|    Enter (-) for Subtraction               |")
    print("|    Enter (*) for Multiplication            |")
    print("|    Enter (/) for Division                  |")
    print("|    enter ('e') for exponentiate            |")
    print("|    enter ('s') for squared                 |")
    print("|    Enter ('n') for Neg/Pos                 |")
    print("|    Enter ('i') for Inverse                 |")
    print("|    enter ('sq') for Square Root            |")
    print("|    ---      Trigonometry      ---          |")
    print("|    Enter ('tog') to toggle trig units      |")
    print("|    Enter ('sin') for Sine                  |")
    print("|    Enter ('cos') for Cosine                |")
    print("|    Enter ('tan') for Tangent               |")
    print("|    Enter ('arcsin') for Inverse Sine       |")
    print("|    Enter ('arccos') for Inverse Cosine     |")
    print("|    Enter ('arctan') for Inverse Tangent    |")
    print("|    Enter ('f') for factorial               |")
    print("|    Enter ('ln') for Natural Log            |")
    print("|    Enter ('log') for Logarithm             |")
    print("|    Enter ('c') for Clear                   |")
    print("|    Enter (q) to Quit                       |")
    print("______________________________________________")
    print(Colors.RESET)


def performCalcLoop(calc):
    displayResult(calc)
    # MAIN LOOP
    a = 0
    b = 0
    while True:
        displayMenu()
        choice = input("Select Operation: ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == '+':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.add(a, b))
            displayResult(calc)
        elif choice == '-':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.subtract(a, b))
            displayResult(calc)
        elif choice == '*':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.multiply(a, b))
            displayResult(calc)
        elif choice == '/':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.divide(a, b))
            displayResult(calc)
        elif choice == 'e':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.exponentiate(a, b))
            displayResult(calc)
        elif choice == 's':
            a = calc.get_state()
            calc.set_state(calc.square(a))
            displayResult(calc)
        elif choice == 'n':
            a = calc.get_state()
            calc.set_state(calc.invert_sign(a))
            displayResult(calc)
        elif choice == 'i':
            a = calc.get_state()
            calc.set_state(calc.inverse(a))
            displayResult(calc)
        elif choice == 'sq':
            a = calc.get_state()
            calc.set_state(calc.square(a))
            displayResult(calc)
        elif choice == 'c':
            calc.set_state(0)
            displayResult(calc)
        elif choice == 'sin':
            a = calc.get_state()
            calc.set_state(calc.sine(a))
            displayResult(calc)
        elif choice == 'cos':
            a = calc.get_state()
            calc.set_state(calc.cosine(a))
            displayResult(calc)
        elif choice == 'tan':
            a = calc.get_state()
            calc.set_state(calc.tangent(a))
            displayResult(calc)   
        elif choice == 'arcsine':
            a = calc.get_state()
            calc.set_state(calc.inverse_sine(a))
            displayResult(calc) 
        elif choice == 'arccos':
            a = calc.get_state()
            calc.set_state(calc.inverse_cosine(a))
            displayResult(calc) 
        elif choice == 'arctan':
            a = calc.get_state()
            calc.set_state(calc.inverse_tangent(a))
            displayResult(calc) 
        elif choice == 'log':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.log(a, b))
            displayResult(calc)
        elif choice == 'ln':
            a = calc.get_state()
            calc.set_state(calc.natural_log(a))
            displayResult(calc) 
        elif choice == 'f':
            a = calc.get_state()
            calc.set_state(calc.factorial(a))
            displayResult(calc) 
        elif choice == 'tog':
            calc.toggle_trig_unit()
            displayResult(calc)
        else:
            calc.set_state('Err')
            displayResult(calc)
        calc.first_run = False


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
