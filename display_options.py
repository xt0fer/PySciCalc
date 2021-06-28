class DisplayOptions():

    def __init__(self):
        self.currentDisplay = None
        self.currentTrig = None

    def switch_modes(self, desiredMode):
        
        if desiredMode == '5':
            if self.currentDisplay == 'decimal':
                self.currentDisplay = 'octal'
                return self.currentDisplay
            elif self.currentDisplay == 'octal':
                self.currentDisplay = 'binary'
                return self.currentDisplay
                
            elif self.currentDisplay == 'binary':
                self.currentDisplay = 'hexadecimal'
                return self.currentDisplay
            elif self.currentDisplay == 'hexadecimal':
                self.currentDisplay = 'decimal'
                return self.currentDisplay

        elif desiredMode.lower() == '1': #or 'decimal':
            self.currentDisplay = 'decimal'
            return self.currentDisplay
        elif desiredMode.lower() == '2': #or 'octal':
            self.currentDisplay = 'octal'
            return self.currentDisplay
        elif desiredMode.lower() == '3': #or 'binary':
            self.currentDisplay = 'binary'
            return self.currentDisplay
        elif desiredMode.lower() == '4': #or 'hexadecimal':
            self.currentDisplay = 'hexadecimal'
            return self.currentDisplay

        else:
            return 'that is not a valid funciton'
    
    def switch_trig(self, desiredTrig):
        print('\nYour current Trig mode is ' + currentTrig + '. Please select one of the following options')
        print('1. Degrees, 2. Radians, 3. Switch')
        if desiredTrig.lower() == '1':# or 'degrees':
            self.currentTrig = 'degrees'
        elif desiredTrig.lower() == '2':# or 'radians':
            self.currentTrig = 'radians'
        elif desiredTrig.lower() == '3':# or 'switch':
            if self.currentTrig == 'degrees':
                self.currentTrig = 'radians'
            else:
                self.currentTrig = 'degrees' 


currentTrig = 'degrees'

