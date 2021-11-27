"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :   Python program to count the values associated with key in a
dictionary.
"""
my_list = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
success_count = 0
for dictionary in my_list:
    if 'success' in dictionary:
        if dictionary['success'] == True:
            success_count += 1
print(success_count)
