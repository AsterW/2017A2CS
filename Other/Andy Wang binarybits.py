field = 5
#bit = input(int("input the bit you want to test:"))
#task = input("input the task you want to check:")

def testbit (field, bit):
    field  = field>>bit
    x=field%2
    return x

def setbit (field, bit):
    field = field>>bit
    x=field%2
    if x==0:
        field = (field+1)<<bit
    else:
        field = field<<bit
    return field

def cleanbit(field, bit):
    field = field>>bit
    x=field%2
    if x==0:
        field = field<<bit
    else:
        field = (field+1)<<bit
    return field

def togglebit(field, bit):
    field = field>>bit
    x=field%2
    if x==0:
        field = (field+1)<<bit
    else:
        field = (field-1)<<bit
    return field

