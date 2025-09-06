#Fibonacci series: 0, 1, 1, 2 , 3, 5, 8, 13......

def fib():
    a, b = 0, 1
    while True:
        yield a
        a = b
        b = a + b

num = input("Enter a number: ")
num = int(num)

fib_list = []
for i in fib():
    if  i > num:
        break
    fib_list.append(i)
    print(i)

print(fib_list)