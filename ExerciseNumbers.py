#Exercise: Numbers in python

#    You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
#    You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
#    Find out using python, how many dollars is the shopkeeper going to give you back?
#    You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
#    If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
#    Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
#    Print binary representation of number 17


length_field = 92
wide_field = 48.8
football_area = length_field * wide_field
print("Football area is:", football_area,"m2")

packet_potato = 9
cost_potato = 1.49
total = 20
cash_back = total - packet_potato*cost_potato
print("Your cash back is: ",cash_back)

tile_length = 5.5
tile_price =500
tiles_cost = (tile_length **2)* tile_price
print("Cost of tiles is:",tiles_cost)

print("Binary format of 17 is: ",bin(17))
