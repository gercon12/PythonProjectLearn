#Exercise: Python for loop

#    After flipping a coin 10 times you got this result,

#result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

#Using for loop figure out how many times you got heads

#    Print square of all numbers between 1 to 10 except even numbers

#    Your monthly expense list (from Jan to May) looks like this,
#expense_list = [2340, 2500, 2100, 3100, 2980]
#Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
#If expense is not found then it should print that as well.

#    Lets say you are running a 5 km race. Write a program that,
#        Upon completing each 1 km asks you "are you tired?"
#        If you reply "yes" then it should break and print "you didn't finish the race"
#        If you reply "no" then it should continue and ask "are you tired" on every km
#        If you finish all 5 km then it should print congratulations message

#    Write a program that prints following shape

#*
#**
#***
#****
#*****


result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i == "heads":
        count = count + 1
print("count of heads:",count)

for i in range(1,11):
    if i%2 == 0:
        cuad=i**2
        print(cuad)


expense_list = [2340, 2500, 2100, 3100, 2980]
month_list =["January", "February", "March","April", "May"]
expense_input = int(input("enter expense amount"))
count = 0
for i in expense_list:
    count = count + 1
    if i == expense_input:
        print("your expense amount is in the list:",i," ","in the month:",month_list[count-1])
print("your expense amount is NOT in the list:",expense_input)



for i in range(1,6):
    feeling = input("are you tired: ")
    if feeling == "yes":
        print("you didn't finish the race")
        break
    elif feeling == "no":
        print("are you tired on every km")
    elif i==5:
        print("congratulations")


for i in range(1,6):
    if i == 1:
        print("*")
    elif i == 2:
        print("**")
    elif i == 3:
        print("***")
    elif i == 4:
        print("****")
    elif i ==5:
        print("*****")

list_print =["*","**","***","****","*****"]
for j in list_print:
    print(j)

