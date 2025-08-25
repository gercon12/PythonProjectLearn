x = input("Enter number 1: ")
y = input("Enter number 2: ")
try:
    z = round(int(x)/int(y),2)
except Exception as e:
    print("Exception ocurred: ",e)
    z = None
print("Division is: ", z)