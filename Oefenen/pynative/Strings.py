# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 09:15:02 2023

@author: mhouts
"""

#----- exercise 1 -------
#  Create a string made of the middle three characters
def middle_string(stringInput):
    
    strLength = int(len(stringInput) / 2)

    print(stringInput[strLength - 1:strLength + 2])

str1 = "JhonDipPeta"
str2 = "JaSonAy"

middle_string(str1)
middle_string(str2)

#----- exercise 2 -------
#  Append new string in the middle of a given string

s1 = "Ault"
s2 = "Kelly"

s1Middle = int(len(s1) / 2)

print(s1[s1Middle - 2:s1Middle],s2,s1[s1Middle :s1Middle + 2], sep ='')

#----- exercise 3 -------
# Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"

# Wrong exercise, but fun to program
listText = []

for x in range(len(s1)):
    listText.append(s1[x:x+1])
    listText.append(s2[x:x+1])
    
print(''.join(listText))
# End wrong exercise.
s1Lt = int(len(s1) / 2)
s2Lt = int(len(s2) / 2)

print(s1[0:1],s2[0:1],s1[s1Lt:s1Lt+1], s2[s2Lt:s2Lt+1],s1[-1],s2[-1], sep = '')

#----- exercise 4 -------
# Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"
listLower = []
listUpper = []

for x in range(len(str1)):
    if str1[x].islower() == True:
        listLower.append(str1[x])
    else:
        listUpper.append(str1[x])
        
for x in listUpper:
    listLower.append(x)
    
print(''.join(listLower))

#----- exercise 5 -------
# Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

Chars = 0 
Digits = 0
Symbols = 0

for x in range(len(str1)):
    if str1[x].isalpha():
        Chars += 1
    elif str1[x].isdigit():
        Digits += 1
    else:
        Symbols += 1

print("Chars =", Chars, "\n", "Digits =", Digits, "\n", "Symbols =", Symbols)

#----- exercise 6 -------
# Create a mixed String using the following rules
s1 = "Abc"
s2 = "Xyz"
newstring = ''

s2 = s2[::-1]

for x in range(len(s1)):
    newstring += s1[x]
    newstring += s2[x]

print(newstring)

#----- exercise 7 -------
# String characters balance Test

def stringChecker(str1,str2):
    boolState = True
    for x in s1:
        if x in s2:
            continue
        else:
            boolState = False
    return boolState
        
#case 1
s1 = "Yn"
s2 = "PYnative"
        
boolState = stringChecker(s1,s2)
print(boolState)

#case 2
s1 = "Ynf"
s2 = "PYnative"
boolState = stringChecker(s1,s2)
print(boolState)

#----- exercise 8 -------
# Find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to USA. usa awesome, isn't it?"
countUsa = 0
listWords = str1.lower().split()

for x in listWords:
    if "usa" in x:
        countUsa += 1

print(countUsa)

#alternative
subString = "USA"
lowerString = str1.lower()

print(lowerString.count(subString.lower()))

#----- exercise 9 -------
# Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
listDigits = []

for x in range(len(str1)):
    if str1[x].isdigit():
        listDigits.append(int(str1[x]))

sumDigits = sum(listDigits)
averageDigits = (sumDigits / len(listDigits))
print("Sum is:",sumDigits, "Average is:",averageDigits)
        
#----- exercise 10 -------
# Write a program to count occurrences of all characters within a string

str1 = "Apple"
strDict = dict()

for x in str1:
    count = str1.count(x)
    strDict[x] = count

print(strDict)

#----- exercise 11 -------
# Reverse a given string
str1 = "PYnative"

reverseStr1 = str1[::-1]
print(reverseStr1)

#----- exercise 12 -------
# Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."

x = str1.rfind("Emma")
print(x)

#----- exercise 13 -------
# Split a string on hyphens

str1 = "Emma-is-a-data-scientist"
str1 = str1.split("-")
for x in str1:
    print(x)
    
#----- exercise 14 -------
# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str_list = list(filter(None, str_list))

print(str_list)

#----- exercise 15 -------
# Remove special symbols / punctuation from a string

str1 = "/*Jon is @developer & musician"