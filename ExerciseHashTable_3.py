DELETED = "<DELETED>"
class HashTable():
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        start_index = h

        while True:
            #if it is empty o deleted, insert
            if self.arr[h] == None or self.arr[h]== DELETED:
                self.arr[h] = (key,value)
                return

            #if the key already exist, update
            if self.arr[h][0] == key:
                self.arr[h] = (key,value)
                return

            #if not, move the next index
            h = (h + 1) % self.MAX

            #If we went all the way around → full table
            if h == start_index:
                print("Table full")
                return

    def __getitem__(self,key):
        h = self.get_hash(key)
        start_index = h
        while True:
            if self.arr[h] == None:
                return "Not found"

            if self.arr[h] != DELETED and self.arr[h][0] == key:
                return self.arr[h][1]

            h = (h + 1) % self.MAX

            if h == start_index:
                return "Not found"

    def __delitem__(self,key):
        h = self.get_hash(key)
        start_index = h
        while True:
            if self.arr[h] == None:
                return "Not found"

            if self.arr[h] != DELETED and self.arr[h][0] == key:
                self.arr[h] = None

            h = (h + 1) % self.MAX

            if h == start_index:
                return "Not found"
t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
t["march 17"] = 29
t["nov 1"] = 1
t["march 33"] = 234
print(t["dec 1"])
print(t["march 33"])
t["march 33"] = 999
print(t["march 33"])
t["april 1"] = 87
t["april 2"] = 123
t["april 3"] = 234234
t["april 4"] = 91
t["May 22"] = 4
t["May 7"] = 47
t["jan 1"] = 0

del t["april 2"]

t["jan 1"] = 0

#t["april 4"] = 91


'''
t["march 6"]= 120
t["march 6"]= 78
t["march 8"]= 67
t["march 9"]= 4
t["march 17"]= 459

print(t["march 17"])
t["march 10"]= 19
t["march 11"]= 9
t["march 12"]= 79
t["march 13"]= 15 
t["march 14"]= 16
t["march 15"]= 17
t["march 16"]= 18

del(t["march 17"])
'''
print(t.arr)

