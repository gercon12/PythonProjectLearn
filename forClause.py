'''
exp = [2340, 2500, 2100, 3100, 2980]
#total = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
total = 0
for item in exp:
    total = total + item
print(total)
'''

#------------------------------

for i in range(10):
    print(i+1)

for i in range(1,11):
    print(i)

#------------------------------
#print each month and its exp and the total
exp = [2340, 2500, 2100, 3100, 2980]
total = 0
for i in range(len(exp)):
    print("month is ", (i + 1), "expense is: ", exp[i] )
    total = total + exp[i]
print(total)

#------------------------------
#find the location of keys
key_location = "chair"
locations = ["garage","living room", "chair", "closet"]
for i in locations:
    if i == key_location:
        print("key is found in ", i)
        break
    else:
        print("key is not found in ", i)

#------------------------------
#print square of numbers between 1 y 11 EXCEPT even numbers
#skip even numbers
for i in range(1,11):
    if i%2 == 0:
        continue # si es par vuelve al ciclo
    print(i*i)

#------------------------------
#condition while, print 1 to 10
i = 1
while i <= 10:
    print(i)
    i = i + 1




