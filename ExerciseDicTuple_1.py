#Exercise: Python Dict and Tuples

#We have following information on countries and their population (population is in crores),
#Country 	Population
#China 	143
#India 	136
#USA 	32
#Pakistan 21

#Using above create a dictionary of countries and its population
#Write a program that asks user for three type of inputs,
#print: if user enter print then it should print all countries with their population in this format,

#        china==>143
#        india==>136
#        usa==>32
#        pakistan==>21

#add: if user input add then it should further ask for a country name to add. If country already exist in our dataset
# then it should print that it exist and do nothing.
#If it doesn't then it asks for population and add that new country/population in our dictionary and print it

#remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove
# it and print new dictionary using format shown above in (a). #Else print that country doesn't exist!

#query: on this again ask user for which country he or she wants to query.
# When user inputs that country it will print population of that country.
import json
import os

file_country= "country_dic.json"

if os.path.exists(file_country):
    with open(file_country, "r") as f:
        country_dic = json.load(f)
else:
    country_dic = {'china': 143, 'india': 136, 'usa':32,'pakistan':21}

while True:
    choice_action = input("enter your choice: print, add, remove, query, exit: ")
    if choice_action == "print":
        for key in country_dic:
            print(key,"==>", country_dic[key])
    elif choice_action == "add":
        country_name = input("enter country name: ")
        if country_name in country_dic:
            print("country name already exist", country_name)
        else:
            population = int(input("enter population: "))
            country_dic[country_name] = population
            print("new country added: ", country_name, country_dic[country_name])
            print(country_dic)
    elif choice_action == "remove":
        country_name = input("enter country name to remove: ")
        if country_name in country_dic:
            del country_dic[country_name]
            print(country_dic)
        else:
            print("country name does not exist", country_name)
    elif choice_action == "query":
        country_name = input("enter country name to query: ")
        if country_name in country_dic:
            print("country name", country_name,"population",country_dic[country_name])
    elif choice_action == "exit":
        with open(file_country, "w") as f:
            json.dump(country_dic, f, indent=4)
        print("end of program")
        break
    else:
        print("continue in program")


