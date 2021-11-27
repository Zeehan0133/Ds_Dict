"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :  multiple key exist or not

"""
mydic={0:"zero",1:"0ne",2:"two"}
u_input=int(input("enter key :"))
if u_input in mydic:
    print("key is present")
else:
    print("key is absent")
