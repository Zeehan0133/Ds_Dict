"""
@Author: Zeehan 
@Date: 2021-26-11 19:00:30
@Title :   program to count number of items in a dictionary value
that is a list.
"""
# dict =   {"rahul":['subj1', 'subj2', 'subj3'], "ravi": ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)


my_list = [{'id': 1, 'success': True, 'name': 'Lary'},
           {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]

# solution 1
success_count = 0
for dictionary in my_list:
    if 'success' in dictionary:
        if dictionary['success'] == True:
            success_count += 1
print(success_count)
