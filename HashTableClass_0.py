import csv
#Array
stock_prices=[]
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
print(stock_prices)

for element in stock_prices:
    if element[0] == "9/03/2025":
        print(element[1])

#Dictionary
stock_prices={}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print(stock_prices)

print(stock_prices["9/03/2025"])