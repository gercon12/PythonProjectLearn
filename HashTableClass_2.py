class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h=h+ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
t["9/03/2025"]=130
print(t["9/03/2025"])

t["6/03/2025"]= 140
print(t["6/03/2025"])

t["7/03/2025"]= 160
print(t["7/03/2025"])

t["8/03/2025"]= 170
print(t["8/03/2025"])

print(t.arr)

for i in range(len(t.arr)):
    if t.arr[i] in (130, 140, 160, 170):
        print(i)

del t["9/03/2025"]

print(t.arr)
