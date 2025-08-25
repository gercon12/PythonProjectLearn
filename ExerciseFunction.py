#Exercise: Functions in python

#    Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,

#area = (1/2)*base*height

#    Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,

#rectangle area=length*width

#If no shape is supplied then it should take triangle as a default shape

#    Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,

#*
#**
#***

#if input is 4 then it should print

#*
#**
#***
#****

#Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def triangle_area(b,h):
    area=(1/2)*b*h
    return area

print("triangle area is: ", triangle_area(100,200))


def area_function(x,y,shape):
    if shape=='rectangle':
        area =x*y
        print("area of rectangle is: ", area)
    elif shape=='triangle':
        area = (1/2)*x*y
        print("area of triangle is: ", area)
    else:
        area = (1/2) * x * y
        print("area of shape is: ", area)

area_function(10,20,"triangle")
area_function(10,20,"rectangle")
area_function(10,20,"unknown")


def print_line(number):
    s = ""
    for i in range(1,number+1):
        s = s + "*"
        print(s)

number = int(input("enter number: "))
print_line(number)

