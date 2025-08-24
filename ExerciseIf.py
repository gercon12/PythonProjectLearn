#-----------------------------------------------------------------------------------------------------------------
#Exercise: Python If Condition
#Using following list of cities per country,

#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]

#    Write a program that asks user to enter a city name and it should tell which country the city
#    belongs to

#    Write a program that asks user to enter two cities and it tells you if they both are in same
#    country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India"
#    but if I enter mumbai and dhaka it should print "They don't belong to same country"

#Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.

#    Ask user to enter his fasting sugar level
#    If it is below 80 to 100 range then print that sugar is low
#    If it is above 100 then print that it is high otherwise print that it is normal

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("enter the city: ")
if city in india:
    print("the city is in india")
elif city in pakistan:
    print("the citiy is in pakistan")
elif city in bangladesh:
    print("the city is in bangladesh")
else:
    print("the cities are not in the list of countries")

city = input("enter the city: ")
city_1 = input("enter the city: ")
if city and city_1 in india:
    print("Both cities are in india")
elif city and city_1 in pakistan:
    print("Both cities are in pakistan")
elif city and city_1 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")

sugar_level = int(input("enter the sugar level: "))
if sugar_level < 80:
    print("The sugar level is low")
elif sugar_level > 100:
    print("The sugar level is high")
else:
    print("The sugar level is good")