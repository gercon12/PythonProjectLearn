'''
x = input("Enter number 1: ")
y = input("Enter number 2: ")
try:
    z = round(int(x)/int(y),2)
except Exception as e:
    print("Exception ocurred: ",e)
    z = None
print("Division is: ", z)


#Error type ZeroDivisionError
#exception by zero exception
#x = input("Enter number 1: ")
#y = input("Enter number 2: ")
try:
    z = round(int(x)/int(y),2)
except ZeroDivisionError as e:
    print("Division by zero exception ocurred")
    z = None
print("Division is: ", z)


#try
#    while road_is_clear()
#        drive()
#except Accident as e:
#    take_detour()

#Error type string between integer
try:
    z = x/int(y)
except ZeroDivisionError as e:
    print("Division by zero exception ocurred")
    z = None
except TypeError as e:
    print("exception type", type(e).__name__)
    z = None
print("Division is: ", z)
'''

x = input("Enter number 1: ")
y = input("Enter number 2: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("Division by zero exception")
    z = None
except TypeError as e:
    print("exception type")
    z = None
print("Division is: ", z)