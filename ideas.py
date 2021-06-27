from itertools import cycle

currentDisplayMode = 'decimal'

def switchDisplayMode(desired):
    if currentDisplayMode == 'decimal' and desired == '':
        currentDisplayMode = 'octal'
    elif currentDisplayMode == 'octal' and desired == '':
        currentDisplayMode = 'binary'
    elif currentDisplayMode == 'binary' and desired == '':
      currentDisplayMode = 'hexadecimal'
    elif currentDisplayMode == 'hexadecimal' and desired == '':
      currentDisplayMode = 'decimal'

a = switchDisplayMode('')
print(a)


#print(switchDisplayMode)

#displayModeOptions = cycle(['decimal', 'octal', 'binary', 'hexadecimal'])
#for i in displayModeOptions:
#    print(i)