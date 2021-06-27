from Scientific_Calculator import scientific_calculator

# Setting default mode

current_display = "decimal"
current_units = "degrees"
base_number = 10
exit = "X"

# Displays the main menu of the calculator, and allows user to choose a screen

def main_menu():
    print("Main Menu: \n A. Display Mode (", current_display, ") \n B. Units Mode (", current_units, ") \n C. Trig Calculator \n D. Probability Calculator")
    choice = input("Choose:")
    return choice

while exit == "x" or exit == "X":
    choice = main_menu()
    if choice == "A" or choice =="a": # goes to the first screen - allows user to choose display
        current_display = scientific_calculator.switchDisplayMode()
        exit = input()
    elif choice == "B" or choice == "b": # goes to the second screen - allows user to change mode
        current_units = scientific_calculator.switchUnitsMode()
        exit = input()
    elif choice == "c" or choice == "C":
        scientific_calculator.trig_function(current_display, base_number)
    elif choice == "d" or choice == "D":
        scientific_calculator.probability(base_number)
    else:
        print("Invalid input. Please choose from the given options.")
