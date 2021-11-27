"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  script to sort (ascending and descending) a dictionary by value
"""
'''
The Python operator module is one of the inbuilt modules in Python, 
and it provides us with a lot of functions such as add(x, y), floordiv(x, y) etc., which 
we can use to perform various mathematical, relational, logical and bitwise operations
on two input number
'''

import operator
mydict={"c":40,"b":20,"a":50}
print("original dict =", mydict)
asc=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print("assending order",asc)
dsc=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print("decending order",dsc)
