from calculator import Calculator

#chuck was here
def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
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
        else:
            print("That is not a valid input.")


# main start
def main():
    calc = Calculator()
    print('this is the best calculator :)')
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
