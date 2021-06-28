class Memory():

    def __init__(self):
        self.memoryValue = 0

    
    def memoryAdd(self, memoryCall):
        #adds new value to memory
        self.memoryValue = memoryCall
        return self.memoryValue
            

    def memoryClear(self):
        #sets memory value to 0
        self.memoryValue = 0
        return self.memoryValue

    def memoryRecall(self):
        #recalls last memory set 
        return self.memoryValue



