#!/usr/bin/python

dict = {'Name': 'Ruben', 'Age': 50, 'City': 'Amsterdam'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# Access the data using a key, from the dictionary
print("dict['Ruben']: ", dict['Ruben'])

# Access the data using a key (which is non-existent), from the dictionary, will give an error
print(dict['Dept'])

#You can update the dictionary by 
##1. adding a new entry or adding a key value pair 
##2. modifying an existing entry

#dict = {'Name': 'Ruben', 'Age': 50, 'City': 'Amsterdam'}
dict['Age'] = 52; # update existing entry

dict['Company'] = "XYZ"; # Add new entry (key-value pair)

#Print the contents of the dict now
dict

#Delete dictionary elements
#You can either delete one element at a time or
# clear teh entire contenst of the dict. or delete the entire dict in one operation

del dict['Name']; # remove entry with key 'Name'

#print the contents
dict

dict.clear();     # remove all entries in dict

#check again the contents of dict
dict

del dict;        # delete entire dictionary

#now dict will just show the word dict

"""
Dictionary values can be any python object
However, keys are a bit different
1. No duplicate enteries are allowed epr key
2. Keys must eb immutable

Built in functions and methods of dictionaries are
i. cmp(dict1, dict2)
ii. len(dict)
iii. str(dict)
iv. type(variable)

Methods:
i. clear()
ii. copy()
iii. fromkeys()
iv. get()
v. has_key()
vi. keys()
vii. items()
viii. setdefault()
ix. update()
x. values() """
