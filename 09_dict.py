"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Write a Python program to convert a list into a nested dictionary of keys.
"""
num_list=[1,2,3,4,5,6]
new_dict=current={}
for dic in num_list:
    current[dic]={}
    current = current[dic]
    print(new_dict)
