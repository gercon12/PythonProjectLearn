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
#5. You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this

month_list = ["January", "February", "March", "April", "May",]
exp_list = [2200,2350,2600,2130,2190]

#1
diff = exp_list[1]-exp_list[0]
print(diff)

#2
Q1_total = sum(exp_list[:3])
print(Q1_total)

#3
x = 2000 in exp_list
print(x)

#4
exp_list.append(1980)
month_list.append("June")
print(exp_list,"\n", month_list)

#5
exp_list[3]=exp_list[3]-200
print(exp_list)
print("----------------------------------------------------------------------------------------------------------")

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
heros.pop(5)
heros.insert(3,"black panther")
print(heros)

#4
heros.remove("thor")
heros.remove("hulk")
heros.insert(1,"doctor strange")
print(heros)

#5
heros.sort()
print(heros)