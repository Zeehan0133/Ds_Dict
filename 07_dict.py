"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Write a Python program to create a dictionary from a string..
"""
str1 = 'w3resource' 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) +1
print(my_dict)
