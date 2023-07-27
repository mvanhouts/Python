# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:28:34 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Convert two lists into a dictionary
#------------------------------------------------------------------------------
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(res_dict)

#altenative

thisdict = {}
for x in range(len(keys)):
    thisdict.update({keys[x]: values[x]})
    
print(thisdict)

#------------------------------------------------------------------------------
# Exercise 2 Merge two Python dictionaries into one
#------------------------------------------------------------------------------

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dictMerge = {**dict1, **dict2}
print(dictMerge)

#------------------------------------------------------------------------------
# Exercise 3 Print the value of key ‘history’ from the below dict
#------------------------------------------------------------------------------
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

#------------------------------------------------------------------------------
# Exercise 4 Initialize dictionary with default values
#------------------------------------------------------------------------------
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

newDefaults = dict.fromkeys(employees, defaults)
print(newDefaults)

#------------------------------------------------------------------------------
# Exercise 5 Create a dictionary by extracting the keys from a given dictionary
#------------------------------------------------------------------------------
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
    
print(newDict)

#------------------------------------------------------------------------------
# Exercise 6 Delete a list of keys from a dictionary
#------------------------------------------------------------------------------
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for x in keys:
    sampleDict.pop(x)
    
print(sampleDict)

#------------------------------------------------------------------------------
# Exercise 7 Check if a value exists in a dictionary
#------------------------------------------------------------------------------
sampleDict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sampleDict.values():
    print(sampleDict['b'],  "present in the dict")
else:
    print(sampleDict['b'], 'Not present in the Dict')
    
#------------------------------------------------------------------------------
# Exercise 8 Rename key of a dictionary
#------------------------------------------------------------------------------
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sampleDict['location'] = sampleDict['city']
del sampleDict['city']
print(sampleDict)

#------------------------------------------------------------------------------
# Exercise 9 Rename key of a dictionary
#------------------------------------------------------------------------------
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sampleDict, key=sampleDict.get))

#------------------------------------------------------------------------------
# Exercise 10 Change value of a key in a nested dictionary
#------------------------------------------------------------------------------
sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sampleDict['emp3']['salary'] = 8500

print(sampleDict)
