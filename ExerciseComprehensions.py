
#    Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
#Example :
#    integer = [0, 1, 2, 3, 4]
#    binary = ["0", "1", "10", "11", "100"]
#    binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

integer = [0,1,2,3,4]
binario = []
#binary = [bin(integer) for i in integer bin.append(i)]
#print(binary)

numero = bin(10)
print(numero)

for i in integer:
    #binario = bin(i)
    binario.append(bin(i))
print(binario)

print("-------------------")
binario = [bin(i) for i in integer]
print(binario)

binario = [format(i,'b') for i in integer]
print(binario)

b = {ent:binary for ent,binary in zip(integer, binario)}
print(b)


#Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
#a + i = 0
#Example:
#integer = [1, -1, 2, 3, 5, 0, -7]
#additive_inverse = [-1, 1, -2, -3, -5, 0, 7]

integer = [1, -1, 2, 3, 5, 0, -7]

additive_inverse = [-i for i in integer]
print(additive_inverse)


#    Create a set which only contains unique sqaures from a given a integer list.

#integer = [1, -1, 2, -2, 3, -3]
#sq_set = {1, 4, 9}

integer = [1, -1, 2, -2, 3, -3]

#option 1
sq_set = set([i**2 for i in integer])
print(sq_set)

#option 2
sq_set = {i**2 for i in integer}
print(sq_set)

