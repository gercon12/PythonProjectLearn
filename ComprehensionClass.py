numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
print(even)

print("------------------------------")

even = [i for i in numbers if i % 2 == 0]
print(even)

square = [i**2 for i in numbers ]
print(square)

print("------------------------------")

s = set([1,2,3,4,5,2,3])
print(s)

print("------------------------------")
even = {i for i in s if i % 2 == 0}
print(even)

print("------------------------------")
cities = ("mumbai","new york","paris")
countries = ("india","usa","france")

z= zip(cities,countries)
print(z)

for a in z:
    print(a)

d = {city:country for city,country in zip(cities,countries)}
print(d)
