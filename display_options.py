class DisplayOptions():

    def __init__(self):
        pass

    def switch_modes(self, desiredMode):
        print('\nYour current display mode is: ' + currentDisplayMode + '. Please select one of the following options:')
        print('1. Decimal, 2. Octal, 3. binary, 4. hexadecimal, 5. iterate')
        
        if desiredMode == '5':
            if currentDisplayMode == 'decimal':
                currentDisplayMode = 'octal'
                return 'octal'
            elif currentDisplayMode == 'octal':
                currentDisplayMode = 'binary'
                return 'binary'
            elif currentDisplayMode == 'binary':
                currentDisplayMode = 'hexadecimal'
                return 'hexadecimal'
            elif currentDisplayMode == 'hexadecimal':
                currentDisplayMode = 'decimal'
                return 'decimal'
        elif desiredMode.lower() == '1' or 'decimal':
            return 'decimal'
        elif desiredMode.lower() == '2' or 'octal':
            return 'octal'
        elif desiredMode.lower() == '3' or 'binary':
            return 'binary'
        elif desiredMode.lower() == '4' or 'hexadecimal':
            return 'hexadecimal'

        else:
            return 'that is not a valid funciton'
    
    def switch_trig(self, desiredTrig):
        print('\nYour current Trig mode is ' + currentTrig + '. Please select one of the following options')
        print('1. Degrees, 2. Radians, 3. Switch')
        if desiredTrig.lower() == '1' or 'degrees':
            return 'degrees'
        elif desiredTrig.lower() == '2' or 'radians':
            return 'radians'
        elif desiredTrig.lower() == '3' or 'switch':
            if currentTrig == 'degrees':
                currentTrig = 'radians'
            else:
                currentTrig = 'degrees' 


currentTrig = 'degrees'

print(DisplayOptions.switch_trig('radians'))

