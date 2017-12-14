#Andy Wang List Creating
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
    def insertNode(self, newItem):
        if self.freePtr != nullPtr:
            self.newPtr = self.freePtr
            self.records[self.freePtr].value = newItem
            self.freePtr = self.records[self.freePtr].nextPtr
            thisnodePtr = self.startPtr
            prevnodePtr = nullPtr
            while thisnodePtr != nullPtr and self.records[thisnodePtr].value < newItem:
                prevnodePtr = thisnodePtr
                thisnodePtr = self.records[thisnodePtr].nextPtr
            if prevnodePtr == nullPtr:
                self.records[self.newPtr].nextPtr = self.startPtr
                self.startPtr = self.newPtr
            else:
                self.records[self.newPtr].nextPtr = self.records[prevnodePtr].nextPtr
                self.records[prevnodePtr].nextPtr = self.newPtr
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
        currentPtr = self.startPtr
        while currentPtr != nullPtr and self.records[currentPtr].value != dataItem:
            currentPtr = self.records[currentPtr].nextPtr
        print (currentPtr)
##delete a node
    def deleteNode(self,dataItem):
        thisnodePtr = self.startPtr
        while thisnodePtr != nullPtr and self.records[thisnodePtr].value != dataItem:
            prevnodePtr = thisnodePtr
            thisnodePtr = self.records[thisnodePtr].nextPtr
        if thisnodePtr != nullPtr:
            if thisnodePtr == self.startPtr:
                self.startPtr = self.records[self.startPtr].nextPtr
            else:
                self.records[prevnodePtr].nextPtr = self.records[thisnodePtr].nextPtr
            self.records[thisnodePtr].nextPtr = self.freePtr
            self.freePtr = thisnodePtr

##create a list
l = List()
l.insertNode(1)
l.insertNode(7)
l.insertNode(3)
l.insertNode(8)
l.insertNode(5)
l.insertNode(6)
l.findNode(6)
l.printList()
l.deleteNode(5)
l.printList()
