"""
For this mod, cli area = 80

"""

def printline(description):
    length = 79
    print('{:^{}}'.format(description, length))

def printline2(description, value):
    str(description)
    str(value)
    length = 78
    position = length - (len(description))
    
    print('length ' + str(length))
    print('value ' + str(len(value)))
    print('position ' + str(position))
    
    
    print('{0:<}: {1:>{2}}'.format(str(description), value, int(position)))

def printline3(description, value, unitsymbol):
    length = 78
    position = length - (len(description) + len(unitsymbol))
    print('{0}: {1:>{3}}{2:>}'.format(description, value, unitsymbol, position))
