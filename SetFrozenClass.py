#Set is an unordered collection of unique elements
#Set doesn't allow a list of duplicate elements

basket = {'apple', 'orange', 'mango', 'orange', 'apple'}
print(basket)
print(type(basket))

a = set()
a.add(1)
a.add(2)
print(a)
print(type(a))

#initialize set a converts it as dictionary
a = { }
print(type(a))

#introduce some element to a converts as set
a ={'something'}
print(type(a))

numbers = [1,2,3,4,5,2,3,4]
unique_numbers = set(numbers)
print(unique_numbers)
print(type(unique_numbers))

unique_numbers.add(6)
print(unique_numbers)

print("---------------------------------------------------------------------")

#Frozen meaning you should not be able to change the content of your set
#Frozen doesn't allow to add a new element
frozen_set = frozenset(numbers)
print(frozen_set)

#frozen_set.add(9)
#print(frozen_set)

print("---------------------------------------------------------------------")

x = {'a','b','c'}

print('a' in x)

for i in x:
    print(i)

y = {'a','g','h','i'}
print('a' in y)

#Union of x and y
print(x|y)

#Intersection of x and y
print(x&y)

#Difference of x minus y quit the common element (a from x)
print(x-y)

print(y-x)

x = {'h','g','a'}
print(x&y)

print(x <  y)


