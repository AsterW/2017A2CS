#Andy Wang Stack
nullPtr = -1
##node initialisation
class listNode:
    def __init__(self):
        self.value = ""
        self.nextPtr = nullPtr
##list functions
class List():
##list initialisation
    def __init__(self):
        self.freePtr = 0
        self.startPtr = nullPtr
        self.records = []
        newNode = None
        for i in range (0,10):
            newNode = listNode()
            newNode.nextPtr = i + 1
            self.records.append(newNode)
        newNode.nextPtr = nullPtr
##insert node
    def push(self, newItem):
        if self.freePtr != nullPtr:
            newPtr = self.freePtr
            self.records[self.freePtr].value = newItem
            self.freePtr = self.records[self.freePtr].nextPtr
            if newPtr != 0:
                self.records[newPtr].nextPtr = newPtr-1
            else:
                self.records[newPtr].nextPtr = nullPtr
            self.startPtr = newPtr
        else:
            print("There is no space left in the list!")
##print list
    def printList(self):
        currentPtr = 0
        while currentPtr != self.startPtr+1:
            print(self.records[currentPtr].value, end=" ")
            currentPtr += 1
        print("")
##find node
    def findNode(self,dataItem):
        currentPtr = self.startPtr
        while currentPtr != nullPtr and self.records[currentPtr].value != dataItem:
            currentPtr = self.records[currentPtr].nextPtr
        print (currentPtr)
##delete a node
    def pop(self):
        thisnodePtr = self.startPtr
        self.startPtr = self.records[self.startPtr].nextPtr
        self.freePtr = thisnodePtr
##main
l = List()
l.push(1)
l.push(7)
l.push(3)
l.push(8)
l.push(5)
l.push(6)
l.findNode(6)
l.printList()
l.pop()
l.printList()

