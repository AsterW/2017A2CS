#Andy Wang Binary Search
l = [12, 99, 19, 92, 23, 88, 27, 84, 33, 80, 37, 41, 75, 45, 71, 56, 62, 59, 60]
x = 0
y = len(l)-1
r = len(l)
def arrangeList():
    for i in range (1,y+1):
        while (l[i] < l[i-1] and i != 0):
            t = l[i-1]
            l[i-1] = l[i]
            l[i] = t
            i = i-1
    print(l)
def binarySearch(x=0,y=len(l)-1,r=len(l)):
    while r != 1:
        print(x,y,r)
        if 37 < l[(y+x)//2]:
            r = r-r//2-1
            y = y//2
        elif 37 == l[(y+x)//2]:
            print ((y+x)//2)
        else:
            
            x = (x+y)//2
            r = r-r//2-1
    print(x,y,r)
    print((x+y)//2+1)
    return ((x+y)//2+1)
arrangeList()
binarySearch()
