def getHash(key):
    k=0
    for i in key:
        k=k+ord(i)
    return k%10

def insertData(key,data):
    index = getHash(key)
    if len(hashTable[index]):
        hashTable[index].append(key,data)
    else:
        hashTable[index]=[(key,data)]

def searchData(key):
    index = getHash(key)
    if len(hashTable[index]):
        for i in range(len(hashTable[index])):
            if hashTable[index][i][0]==key:
                return hashTable[index][i][1]
        else:
            return "Item not found"
    else:
        return "The bucket is empty"

hashTable=[[],]*10
