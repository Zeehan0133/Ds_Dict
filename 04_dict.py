"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
one
"""
dic=int(input("Enter a number:"))
mydict={}
for x in range(1,dic+1):
    mydict[x]=x*x
print(mydict)
