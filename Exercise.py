#STRINGS
#Create 3 variables to store street, city and country, now create address variable to store entire address.
#Use two ways of creating this variable, one using + operator and the other using f-string.
#Now Print the address in such a way that the street, city and country prints in a separate line

street = 8
city = "Guatemala"
country = "Guatemala"

address= str(street) + " " + city + " " + country
print(address)

address = f"{street} {city} {country}"
print(address)


address= str(street) + "\n" + city + "\n" + country
print(address)

#Create a variable to store the string "Earth revolves around the sun"
#    Print "revolves" using slice operator
#    Print "sun" using negative index

variable ="Earth revolves around the sun"
print(variable[6:14])
print(variable[-3:])

#Create two variables to store how many fruits and vegetables you eat in a day.
#Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
#Use python f string for this.

fruits = 10
vegetables = 20
diet = f"I eat {vegetables} veggies {fruits} fruits"
print(diet)

#I have a string variable called s='maine 200 banana khaye'.
#This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
#Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s = 'maine 200 banana khaye'
print(s.replace('banana', 'samosa'))
print(s.replace('200', '10'))


s = 'maine 200 banana khaye'
print(s.replace('banana', 'samosa').replace('200', '10'))

#-----------------------------------------------------------------------------------------------------------------
#LISTS
#Let us say your expense for every month are listed below,

#    January - 2200
#    February - 2350
#    March - 2600
#    April - 2130
#    May - 2190
#Create a list to store these monthly expenses and using that find out,
#1. In Feb, how many dollars you spent extra compare to January?
#2. Find out your total expense in first quarter (first three months) of the year.
#3. Find out if you spent exactly 2000 dollars in any month
#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#5. You returned an item that you bought in a month of April and got a refund of 200$.
# Make a correction to your monthly expense list based on this

#1
month_exp = ["January", "February", "March", "April", "May"]
exp = [2200,2350,2600,2130,2190]
feb_diff = exp[1] - exp[0]
print(feb_diff)

#2
Q1_sum = exp[0]+exp[1]+exp[2]
print(Q1_sum)

Q1_sum=sum(exp[:3])
print(Q1_sum)

#3
var1 = 2000 in exp
print(var1)

#4
exp.append(1980)
print(exp)

#5
exp[3] = exp[3]-200
print(exp)

#You have a list of your favourite marvel super heros.
#heros=['spider man','thor','hulk','iron man','captain america']

#Using this find out,
#1. Length of the list
#2. Add 'black panther' at the end of this list
#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#   Do that with one line of code.
#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros=['spider man','thor','hulk','iron man','captain america']

#1
print(len(heros))

#2
heros.append("black panther")
print(heros)

#3
heros.pop(-1)
heros.insert(3,"black panther")
print(heros)

#4
del heros[1:3]
heros.insert(1,"doctor strange")
print(heros)

#5
heros.sort()
print(heros)