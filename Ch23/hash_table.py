#Andy Wang Hash Table
hashTable = 0
for i in range (10):
    hashTable = 0
print(hashTable)
def hash(key):
    address = key % 10
    return address

def insert(newRecord):
    index = hash(newRecord)
    while hashTable[index] != 0:
        index = index + 1
        if index > 9:
            index = 1
    hashTable[index] = newRecord
