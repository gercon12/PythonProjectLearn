def calculate_area(base, height):
    print("__name__ ",__name__)
    return base * height / 2

if __name__ == '__main__':
    print("I am in NameClass.py")
    a = calculate_area(10,10)
    print("area: ",a)