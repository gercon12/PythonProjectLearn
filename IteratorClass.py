a = ["Hey", "Bro", "you're", "awesome"]

for i in a:
    print(i)

print("------------------------------------")

itr = iter(a)
print(next(itr))
print(next(itr))
print(next(itr))

print("------------------------------------")
itr = reversed(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

print("------------------------------------")

for element in [1,2,3]:
    print(element)

for element in (1,2,3):
    print(element)

dic = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
for element in dic:
    print(element, dic[element])

for char in "123456":
    print(char)

for line in open("poem.txt"):
    print(line)







