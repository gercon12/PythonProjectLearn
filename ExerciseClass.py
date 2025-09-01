#Exercise: Class and Objects
#    Create a sample class named Employee with two attributes id and name
#employee :
#    id
#    name
#object initializes id and name dynamically for every Employee object created.
#emp = Employee(1, "coder")
#    Use del property to first delete id attribute and then the entire object

class Employee:
    #properties
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def display(self):
        print(f"Id: {self.id} \nhas name {self.name}")

emp = Employee(1, "coder")
print(emp.id)
print(emp.name)

emp.display()

'''
del emp.id
print(emp.id)
print(emp.name)

del emp
'''