""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  Python script to concatenate following dictionaries to create a new
one
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
mydict = {}
for d in (dic1, dic2, dic3):
     mydict.update(d)
print(mydict)
