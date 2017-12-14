#Andy Wang Queue
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
        self.endPtr = nullPtr
        self.records = []
        newNode = None
        for i in range (0,10):
            newNode = listNode()
            newNode.nextPtr = i + 1
            self.records.append(newNode)
        newNode.nextPtr = nullPtr
##enqueue a node
    def enqueue(self, newItem):
        if self.freePtr != nullPtr:
            newPtr = self.freePtr
            self.records[newPtr].value = newItem
            self.freePtr = self.records[self.freePtr].nextPtr
            if newPtr != 0:
                self.records[self.endPtr].nextPtr = newPtr
                self.endPtr = newPtr
            else:
                self.endPtr = newPtr
                self.startPtr = newPtr
                
        else:
            print("There is no space left in the list!")
##print list
    def printList(self):
        currentPtr = self.startPtr
        while currentPtr != nullPtr:
            print(self.records[currentPtr].value, end=" ")
            currentPtr = self.records[currentPtr].nextPtr
        print("")
        
##find node
    def findNode(self,dataItem):
        currentPtr = self.endPtr
        while currentPtr != nullPtr and self.records[currentPtr].value != dataItem:
            currentPtr = self.records[currentPtr].nextPtr
        return currentPtr
##dequeue a node
    def dequeue(self):
        self.records[self.startPtr].nextPtr = self.freePtr
        self.freePtr = self.startPtr
        self.startPtr = self.records[self.startPtr].nextPtr
        return self.records[self.freePtr].value
##main
l = List()
l.enqueue(1)
l.enqueue(3)
l.enqueue(8)
l.enqueue(5)
l.enqueue(6)
l.findNode(6)
l.printList()
l.dequeue()
l.printList()
