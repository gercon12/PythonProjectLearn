#Read file JSON
#String format
f = open('C://Users//DELL LATITUDE//PycharmProjects//PythonProjectLearn//book.txt', 'r')
s = f.read()
print(s)
print(type(s))

#Convert string into dictionary
import json
book = json.loads(s)
print(book)
print(type(book))

print("----------------------------------")

#see data of bob
print(book["bob"])
print(book["bob"]["phone"])

#see data of tom
print(book["tom"])
print(book["tom"]["phone"])

print("----------------------------------")
#print the content of book
for person in book:
    print(book[person])