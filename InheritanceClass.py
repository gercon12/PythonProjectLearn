#Parent
class Vehicle:
    def general_usage(self):
        print("general usage: transportation")

#Children
class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("specific use: commute to work = vacation with family")

#Children
class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a motorcycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("specific use: road trip, racing")

#Object
c = Car()
c.general_usage()
c.specific_usage()

m = Motorcycle()
m.general_usage()
m.specific_usage()
print("------------------------------------------------------------")

#Parent
class Vehicle:
    def general_usage(self):
        print("general usage: transportation")

#Children
class Car(Vehicle):
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work = vacation with family")

#Children
class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm a motorcycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")

#Object
c = Car()
c.specific_usage()

m = Motorcycle()
m.specific_usage()

# is c a Car: True
print(isinstance(c, Car))

# is c a Motorcycle: False
print(isinstance(c, Motorcycle))

#is Car a Vehicle?
print(issubclass(Car, Vehicle))

#is Car a Motorcycle?
print(issubclass(Car, Motorcycle))