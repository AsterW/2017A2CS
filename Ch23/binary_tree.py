#Andy Wang Binary Tree
nullPtr = -1
class treeNode:
    def __init__(self):
        self.value = ""
        self.leftPtr = nullPtr
        self.rightPtr = nullPtr
class binaryTree:
    def __init__(self):
        self.rootPtr = nullPtr
        self.freePtr = 0
        self.records = []
        newNode = None
        for i in range (0, 7):
            newNode = treeNode()
            newNode.leftPtr = i + 1
            self.records.append(newNode)
        newNode.rightPtr = nullPtr
    def insertNode(self, newItem):
        turnedLeft = False
        if self.freePtr != nullPtr:
            newPtr = self.freePtr
            self.freePtr = self.records[self.freePtr].leftPtr
            self.records[newPtr].value = newItem
            self.records[newPtr].leftPtr = nullPtr
            self.records[newPtr].rightPtr = nullPtr
            if self.rootPtr == nullPtr:
                self.rootPtr = newPtr
            else:
                thisnodePtr = self.rootPtr
                while thisnodePtr != nullPtr:
                    prevnodePtr = thisnodePtr
                    if self.records[thisnodePtr].value > newItem:
                        turnedLeft = True
                        thisnodePtr = self.records[thisnodePtr].leftPtr
                    elif self.records[thisnodePtr].value == newItem:
                        print("This item already exists.")
                    else:
                        turendLeft = False
                        thisnodePtr = self.records[thisnodePtr].rightPtr
                if turnedLeft == True:
                    self.records[prevnodePtr].leftPtr = newPtr
                else:
                    self.records[prevnodePtr].rightPtr = newPtr
    def findNode(self, searchItem):
        thisnodePtr = self.rootPtr
        while thisnodePtr != nullPtr and self.records[thisnodePtr].value != searchItem:
            if self.records[thisnodePtr].value > searchItem:
                thisnodePtr = self.records[thisnodePtr].leftPtr
            else:
                thisnodePtr = self.records[thisnodePtr].rightPtr
        return thisnodePtr
l = binaryTree()
l.insertNode(1)
l.insertNode(2)
l.insertNode(3)
l.insertNode(4)
l.insertNode(5)
l.insertNode(6)
l.insertNode(7)
print(l.findNode(5))
