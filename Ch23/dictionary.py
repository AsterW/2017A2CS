# Andy Wang
# Dictionary
class Dictionary():
    def __init__(self,length=50):
        self.length=length
        self.key=[[] for i in range(50)]
        self.value=[[] for i in range(50)]
    def hash(self,key):
        address=0
        for i in range (len(key)):
            address+=ord(str(key)[i])
        address=address % self.length
        return address
    def insert(self,key,value):
        index=self.hash(key)
        while self.key[index] !=[]:
            index+=1
            if index > self.length:
                index=1
            print("Checking index",index)
        self.key[index]=key
        self.value[index]=value
    def Find(self,searchKey):
        index=self.hash(searchKey)
        print("Checking index",index)
        while (self.key[index]!=searchKey) and (self.key[index]!=[]):
            index+=1
            if index > self.length:
                index=0
                print("Checking index",index)
        if self.key[index]:
            return self.value[index]
