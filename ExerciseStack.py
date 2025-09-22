#Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.

#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

word = "We will conquere COVID-19"

word_list=[]
for char in word:
    word_list.append(char)
print(word_list)
print(word_list[0])
#OPTION 1:
word = "We will conquere COVID-19"
word_reverse=""
for i in range(len(word)-1,-1,-1):
    word_reverse += word[i]
print(word_reverse)

#OPTION 2
print("--------------------------------------")
from collections import deque
word = "We will conquere COVID-19"
dq = deque(word)
dq.reverse()
word_reverse = "".join(dq)
print(word_reverse)
