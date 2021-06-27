import math

class scientific_calculator:

    def _init_(self):
        pass

# The following function allows user to change number system
    def switchDisplayMode():
        print("Please choose a display mode: \n A. Binary \n B. Octal \n C. Decimal \n D. Hexadecimal")
        display_mode = input("Choose:")
        if display_mode == "A" or display_mode == "a":
            current_display = "Binary"
            base_number = 2
            print('You chose Binary - base 2. Click "X" to return to main menu.')
        elif display_mode == "B" or display_mode == "b":
            print('You chose Octal - base 8. Click "X" to return to main menu.')
            current_display = "Octal"
            base_number = 8
        elif display_mode == "C" or display_mode == "c":
            print('You chose Decimal - base 10. Click "X" to return to main menu.')
            current_display = "Decimal"
            base_number = 10
        elif display_mode == "D" or display_mode == "d":
            print('You chose Hexadecimal - base 16. Click "X" to return to main menu.')
            current_display = "Hexadecimal"
            base_number = 16
        else:
            print('Invalid Input.')
        return current_display, base_number

# The following function allows user to change the angle mode
    def switchUnitsMode():
        print("Please choose a units mode: \n A. Degrees \n B. Radians")
        units_mode = input("Choose:")
        if units_mode == "A" or units_mode == "a":
            current_units = "Degrees"
            print('You chose to work in degrees. Click "X" to return to main menu.')
        elif units_mode == "B" or units_mode == "b":
            current_units = "Radians"
            print('You chose to work in radians. Click "X" to return to main menu.')
        else:
            print('Invalid Input.')
        return current_units

# The following function finds sin, cos, tan of an angle taken from the user
    def trig_function(display, mode):
        current_value = 0
        previous_value = 0
        trig = "t"

        while trig == "t" or trig == "T":
            print("Please choose a function: \n A. sin(x) or B. arcsin(x) \n C. cos(x) or D. arccos(x) \n E. tan(x) or F. arctan(x)")
            trig = input("Choose:")
            while trig == "A" or trig == "a":
                print("---SINE CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                calculate = input("Please enter angle measure:")
                solution = int(calculate,mode)

                if mode == "Degrees":
                    solution = math.degrees(math.sin(solution))
                    previous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)
                else:
                    solution = math.radians(math.sin(solution))
                    prevous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)

                trig = input("Click 'A' to calculate another sine value, 'T' to select another trig function, or 'X' to go back to main menu.")

            while trig == "c" or trig == "C":
                print("---COSINE CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                calculate = input("Please enter angle measure:")
                solution = int(calculate,mode)

                if mode == "Degrees":
                    cosine = math.degrees(math.cos(solution))
                    previous_value = current_value
                    current_value = cosine
                    print("Answer = ", cosine)
                else:
                    cosine = math.radians(math.cos(solution))
                    prevous_value = current_value
                    current_value = solution
                    print("Answer = ", cosine)

                trig = input("Click 'B' to calculate another cosine value, 'T' to select another trig function, or 'X' to go back to main menu.")

            while trig == "E" or trig == "e":
                print("---TANGENT CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                calculate = input("Please enter angle measure:")
                solution = int(calculate,mode)

                if mode == "Degrees":
                    solution = math.degrees(math.tan(solution))
                    previous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)
                else:
                    solution = math.radians(math.tan(solution))
                    prevous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)

                trig = input("Click 'C' to calculate another sine value, 'T' to select another trig function, or 'X' to go back to main menu.")

            while trig == "b" or trig == "B":
                print("---INVERSE SINE CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                calculate = input("Please enter ratio:")
                solution = int(calculate,mode)

                if mode == "Degrees":
                    solution = math.degrees(math.asin(solution))
                    previous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)
                else:
                    solution = math.radians(math.asin(solution))
                    prevous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)

                trig = input("Click 'D' to calculate another inverse sine value, 'T' to select another trig function, or 'X' to go back to main menu.")

            while trig == "D" or trig == "d":
                print("---INVERSE COSINE CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                calculate = input("Please enter ratio:")
                solution = int(calculate,mode)

                if mode == "Degrees":
                    solution = math.degrees(math.acos(solution))
                    previous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)
                else:
                    solution = math.radians(math.acos(solution))
                    prevous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)

                trig = input("Click 'E' to calculate another inverse cosine value, 'T' to select another trig function, or 'X' to go back to main menu.")

            while trig == "F" or trig == "f":
                print("---INVERSE TANGENT CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                calculate = input("Please enter ratio:")
                solution = int(calculate,mode)

                if mode == "Degrees":
                    solution = math.degrees(math.atan(solution))
                    previous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)
                else:
                    solution = math.radians(math.atan(solution))
                    prevous_value = current_value
                    current_value = solution
                    print("Answer = ", solution)

                trig = input("Click 'F' to calculate another sine value, 'T' to select another trig function, or 'X' to go back to main menu.")
            return previous_value, current_value

    # Probability Calculator - performs factorials, combinations, and permutations
    def probability(mode):
        previous_value = 0
        current_value = 0
        prob = "p"

        while prob == "p" or prob == "P":
            print("Please choose a function: \n A. Factorial \n B. Combination \n C. Permutation")
            prob = input("Choose:")

            while prob == "A" or prob == "a":
                print("---FACTORIAL CALCULATOR---")
                print("Previous Value:", previous_value)
                print("Current Value:", current_value)
                factorial = input("Please enter a number.")
                print(factorial, "! = ", math.factorial(int(factorial, mode)))
                previous_value = current_value
                current_value = math.factorial(int(factorial, mode))
                prob = input("Click 'A' to calculate another factorial, 'P' to perform another probability function, or 'X' to go back to main menu.")

            while prob == "b" or prob == "B":
                print("---COMBINATION CALCULATOR---")
                pop = input("What is the total?")
                samp = input("How many are you choosing?")
                n = int(pop, mode)
                r = int(samp, mode)

                combination = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
                print(combination, "combinations")
                prob = input("Click 'A' to calculate another factorial, 'P' to perform another probability function, or 'X' to go back to main menu.")

            while prob == "c" or prob == "C":
                print("---PERMUTATION CALCULATOR---")
                pop = input("What is the total?")
                samp = input("How many are you choosing?")
                n = int(pop, mode)
                r = int(samp, mode)

                combination = math.factorial(n) / math.factorial(n - r)
                print(combination, "permutations")
                prob = input("Click 'A' to calculate another factorial, 'P' to perform another probability function, or 'X' to go back to main menu.")













