#Write circle_calc() function that takes radius of a circle as an input from user and then it calculates
# and returns area, circumference and diameter. You should get these values in your main program by calling
# circle_calc function and then print them

import math

def circle_calc(r_value):
    area = round(2*math.pi*r_value**2,2)
    circunf = round(2*math.pi*r_value,2)
    diameter = round(2*r_value,2)
    result = {"area":area, "circunference":circunf, "diameter":diameter}
    return  result

if __name__ == '__main__':
    r_value = float(input("enter radius: "))
    print(circle_calc(r_value))

