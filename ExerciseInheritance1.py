'''
class Animal():
    def general_animal(self):
        print("general animal")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("animal Dog")
    def habitat(self):
        print("habitat dog house")

doggy = Dog()
#doggy.habitat()
'''

class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        print("Woof woof!")


x = Dog()
x.print_habitat()
x.sound()

