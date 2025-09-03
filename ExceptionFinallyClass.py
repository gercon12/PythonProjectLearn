#Using the exact error
try:
    raise MemoryError ("Memory error")
except MemoryError as e:
    print(e)

print("---------------------------------")

#Using generic class exception
try:
    raise Exception ("Memory error")
except Exception as e:
    print(e)

print("---------------------------------")

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception: ", self.msg)
try:
    raise Accident("Crash between two cars")
except Accident as e:
    e.print_exception()

print("---------------------------------")

class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("accident ocurred. take detour ", self.msg)
try:
    raise Accident("Crash between two cars")
except Accident as e:
    e.handle()