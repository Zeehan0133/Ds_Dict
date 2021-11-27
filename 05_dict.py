"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Python program to remove a key from a dictionary.
one
"""
mydict={"zero":0,"one":1,"two":2}
print("before removing :" ,mydict)
if "zero" in mydict:
    del mydict["zero"]
print("after removing :",mydict)
