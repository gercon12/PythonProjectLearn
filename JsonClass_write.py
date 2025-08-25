#JSON =  Java Script Object Notation
book ={}
book['tom'] = {
    "name" : "tom",
    "address" : "1 red street NY",
    "phone" : 98989898
}

book['bob'] = {
    "name" : "bob",
    "address" : "1 green street NY",
    "phone" : 23424234
}

book['german'] = {
    "name" : "german",
    "address" : "proy. sta maria la paz 2",
    "phone" : 85236975
}

book['erick'] = {
    "name" : "erick",
    "address" : "14 street zona 14",
    "phone" : 12635689
}

import json
s = json.dumps(book)
print(s)
print(type(s))

with open('C://Users//DELL LATITUDE//PycharmProjects//PythonProjectLearn//book.txt', 'w') as f:
    f.write(s)