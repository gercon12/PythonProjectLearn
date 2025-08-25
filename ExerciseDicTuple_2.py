#You are given following list of stocks and their prices in last 3 days,
#Stock 	Prices
#info 	[600,630,620]
#ril 	[1430,1490,1567]
#mtl 	[234,180,160]

#    Write a program that asks user for operation. Value of operations could be,
#        print: When user enters print it should print following,
#
#        info ==> [600, 630, 620] ==> avg:  616.67
#        ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#        mtl ==> [234, 180, 160] ==> avg:  191.33

#add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc)
#then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata'
#and 560 will add tata ==> #[560] to the dictionary of stocks.

stock = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

def print_function():
        for key, values in stock.items():
            avg = round(sum(values) / len(values),2)
            print(key, "==>", stock[key],"==>","avg: ",avg)

def add_function():
    stock_question = input("enter your order stock: ")
    stock_price = int(input("enter your price: "))
    if stock_question in stock:
        print("product in stock")
        if stock_price != stock[stock_question]:
            stock[stock_question].append(stock_price)
            print("product in stock",stock_question,"new price:",stock_price)
            print(stock)
    else:
        stock[stock_question] = stock_price
        print(stock)


def main_function():
    choice_input = input("enter option: print, add, exit: ")
    if choice_input == "print":
        print_function()
    if choice_input == "add":
        add_function()


if __name__ == '__main__':
    main_function()
