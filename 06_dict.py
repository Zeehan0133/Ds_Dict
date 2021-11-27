"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Write a Python program to print all unique values in a dictionary.
"""

spl_dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
res=[]
print("original values: ",spl_dict)
u_dict=set( val for dic in spl_dict for val in dic.values())
print("unique values ", u_dict)
