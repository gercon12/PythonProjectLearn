'''
num = input('Enter a number: ')
num = int(num)
if num % 2 == 0:
    print(num, 'is even')
else:
    print(num, 'is odd')
'''

indian = ["samosa","daal","naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza","pasta","risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print(dish, 'is in indian')
elif dish in chinese:
    print(dish, 'is in chinese')
elif dish in italian:
    print(dish, 'is in italian')
else:
    print(dish, 'is not in the list')

