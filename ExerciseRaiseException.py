#Exercise: Raise Exception And Finally

#    Create a custom exception AdultException.
#    Create a class Person with attributes name and age in it.
#    Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.
#    Create a function display_person() which prints the age and name of a person.

#let us say,

#if age>18
#    he is major
#else
#    raise exception

#create custom Exception named is major and raise it if age<18.

'''
#STUDENT SOLUTION 1
class AdultException(Exception):
    def __init__(self, message):
        self.message = message
    def print_message(self):
        print("user defined exception, adulto: ", self.message)

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_minor_age(self):
        if self.age > 18:
            try:
                raise AdultException("person adult")
            except AdultException as e:
                e.print_message()
                #print("person adult")
        else:
            print(f"person child {self.age} name {self.name}")


p = person("Bhavin",17)
p.get_minor_age()

p = person("Dhaval", 23)
p.get_minor_age()
'''


#STUDENT SOLUTION 2
class AdultException(Exception):
    def  print_message(self):
        print("Exception: person is adult")
    pass

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if self.age > 18:
            raise AdultException
        else:
            print(f"person child {self.age}")

    def display_function(self):
        try:
            print(f"age: ",{person.get_minor_age(self)})
        except AdultException as e:
            e.print_message()
        finally:
            print(f"person name: {self.name}")


person("Bhavin",27).display_function()


