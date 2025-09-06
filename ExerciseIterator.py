def square_f():
    a =  1
    while True:
        yield a**2
        a += 1


num = input("Enter a number: ")
num = int(num)

square_list = []
for i in square_f():
    if  i > num:
        break
    square_list.append(i)
    print(i)

print(square_list)