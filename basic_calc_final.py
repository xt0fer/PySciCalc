import math

validMenuOptions = ["+", "-", "*", "/","**", "S", "P","R","F","I","E","C"]


def displayMenu():
    print("----------------------------")
    print("        Menu        ")
    print("Enter (+) for Addition")
    print("Enter (-) for Subtraction")
    print("Enter (*) for Multiplication")
    print("Enter (/) for Division")
    print("enter ('P') to the ^ power")
    print("enter (S) for squared")
    print("enter ('R') for Square Root")
    print("Enter ('F') for Neg/Pos" )
    print("Enter ('I') for Inverse")
    print("Enter ('C') for Clear")
    print("Enter (E) to Exit")
    print("----------------------------")
while True:
    displayMenu()

    
    menuSelection = input("Enter your Option: ")

    # Handling user's menu input
    if menuSelection not in validMenuOptions:
        print("[-] Error: Invalid Input!")

    elif menuSelection == "C":
        print("0")
        
    elif menuSelection == "E":
        print("[+] Program Ended")
        break
    else:
        # Asking user to enter numbers
        try:
            firstNumber = float(input("Enter 1st Number: "))
            #secondNumber = float(input("Enter 2nd Number: "))

            result = 0

            # Checking each possibility and storing the output in 'result' variable
            if menuSelection == "+":
                secondNumber = float(input("Enter 2nd Number: "))
                result = firstNumber + secondNumber
                print("[+] Answer: ", result)
            
            elif menuSelection == "-":
                secondNumber = float(input("Enter 2nd Number: "))
                result = firstNumber - secondNumber
                print("[+] Answer: ", result)

            elif menuSelection == "*":
                secondNumber = float(input("Enter 2nd Number: "))
                result = firstNumber * secondNumber
                print("[+] Answer: ", result)

            elif menuSelection == "/":

                secondNumber = float(input("Enter 2nd Number: "))
                if secondNumber == 0:
                    print("[-] Error: Cannot divide by zero")
                else:
                    result = firstNumber / secondNumber
                    print("[+] Answer: ", result)
                
            elif menuSelection == "P":
                secondNumber = float(input("Enter 2nd Number: "))
                result = firstNumber ** secondNumber
                print("[+] Answer:", result)

            elif menuSelection == "S":
                result = firstNumber**2 
                print("[+] Answer:", result)

            elif menuSelection == ("R"):
                result = math.sqrt(firstNumber)
                print("[+] Answer:", result)

            elif menuSelection == ("I"):
                if firstNumber == 0:
                    print("error")
                else:    
                    result = 1/firstNumber
                    print("[+] Answer:", result)

            elif menuSelection == "F":
                result = -firstNumber
                print("[+] Answer:", result)
                
        except:
            print("[-] Error: Invalid Input! ")
