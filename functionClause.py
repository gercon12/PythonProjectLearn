#calculate total each list
tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

total = 0
for item in tom_exp_list:
    total += item
print("Tom's total expense is:",total)

total = 0
for item in joe_exp_list:
    total += item
print("Joe's total expense is:",total)

#------------------------------
#Function to calculate total each list
def calculate(expense):
    total = 0
    for item in expense:
        total += item
    return total

tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

toms_total = calculate(tom_exp_list)
joes_total = calculate(joe_exp_list)

print("Tom's total expense is:",toms_total)
print("Joe's total expense is:",joes_total)

#------------------------------
#Suma sencilla
def sum(a, b):
    total = 0
    total = a + b
    return total
num = sum(1, 2)

print("Suma es: ",num)

#Suma con argumentos
def sum(a,b):
    print("a:", a)
    print("b:", b)
    total = a + b
    print("Total inside function:", total)
    return total

n = sum(b = 5,a = 6)
print("Total outside function",n)