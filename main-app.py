from calculator import Calculator


def get_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def get_one_number():
    c = float(input("Enter a number: "))
    return c


def displayResult(x):
    print('----------------------------')
    print(x)


def displayMenu():
    print("----------------------------")
    print("        Menu        ")
    print("Enter (+) for Addition")
    print("Enter (-) for Subtraction")
    print("Enter (*) for Multiplication")
    print("Enter (/) for Division")
    print("enter ('e') for exponentiate")
    print("enter ('s') for squared")
    print("Enter ('n') for Neg/Pos" )
    print("Enter ('i') for Inverse")
    print("enter ('sq') for Square Root")
    print("Enter ('sin') for Sine")
    print("Enter ('cos') for Cosine")
    print("Enter ('tan') for Tangent")
    print("Enter ('arcsin') for Inverse Sine")
    print("Enter ('arccos') for Inverse Cosine")
    print("Enter ('arctan') for Inverse Tangent")
    print("Enter ('f') for factorial")
    print("Enter ('ln') for Natural Log")
    print("Enter ('log') for Logarithm")
    print("Enter ('c') for Clear")
    print("Enter (q) to Quit")
    print("----------------------------")

def performCalcLoop(calc):
    displayResult(0)   # First run, display 0
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
            displayResult(calc.get_state())
        elif choice == '-':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.subtract(a, b))
            displayResult(calc.get_state())
        elif choice == '*':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.add(a, b))
            displayResult(calc.get_state())
        elif choice == '/':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.divide(a, b))
            displayResult(calc.get_state())
        elif choice == 'e':
            if calc.first_run:
                a, b = get_two_numbers()
            else:
                a = calc.get_state()
                b = get_one_number()
            calc.set_state(calc.exponentiate(a, b))
            displayResult(calc.get_state())
        elif choice == 's':
            a = calc.get_state()
            calc.set_state(calc.square(a))
            displayResult(calc.get_state())
        elif choice == 'n':
            a = calc.get_state()
            calc.set_state(calc.invert_sign(a))
            displayResult(calc.get_state())
        elif choice == 'i':
            a = calc.get_state()
            calc.set_state(calc.inverse(a))
            displayResult(calc.get_state())
        elif choice == 'sq':
            a = calc.get_state()
            calc.set_state(calc.square(a))
            displayResult(calc.get_state())
        elif choice == 'c':
            calc.set_state(0)
            displayResult(0)
        else:
            print("That is not a valid input.")
        calc.first_run = False


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
