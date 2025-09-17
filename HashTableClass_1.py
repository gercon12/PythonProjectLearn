class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h=h+ord(char)
        return h % self.MAX

    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

t = HashTable()
t.add("9/03/2025",150)
print(t.get("9/03/2025"))
#print(t.get_hash("march 6"))