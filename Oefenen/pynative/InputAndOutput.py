# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:14:59 2023

@author: mhouts
"""

#----- exercise 1 -------
# Accept numbers from a user

number = input("Type a number")
print("Is this your number:", number)

#----- exercise 2 -------
# Display three string “Name”, “Is”, “James” as “Name**Is**James”

print('Name','Is','James', sep ='**')

#----- exercise 3 -------
# Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)

#----- exercise 4 -------
# Display float number with 2 decimal places using print()

num = 458.541315
print(round(num, 2))

#----- exercise 5 -------
# Accept a list of 5 float numbers as an input from the user
floatList = []

for x in range(0,5):
    floatList.append(float(input("Give me a float ")))

print(floatList)
    
#----- exercise 6 -------
# Write all content of a given file into a new file by skipping line number 5
lineCount = 0
fp = open('C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/lines.txt', 'r')
lines = fp.readlines()
print(lines[3])

for x in lines:
    if lineCount != 4:
        print(lines[lineCount])
    lineCount += 1
    
#----- exercise 7 -------
# Accept any three string from one input() call
lineCount = 0
inputString = input("give names seperated by a space: ")
stringList = inputString.split(' ')
for x in stringList:
    print(stringList[lineCount])
    lineCount += 1
    
#Alternative not dynamic:
str1, str2, str3 = input("give names seperated by a space: ").split()
print(str1)
print(str2)
print(str3)

#----- exercise 8 -------
# Format variables using a string.format() method.

totalMoney = 1000
quantity = 3
price = 450

print("I have {totalmoney} dollars so I can buy {quantity} football for {price} dollars.".format(totalmoney = totalMoney, quantity = quantity, price = price))

#----- exercise 9 -------
# Check file is empty or not

import os
bytesInt = os.stat("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Emptyfile.txt").st_size

if bytesInt == 0:
    print("The file is empty")
else:
    print("The file is not empty.")
    
#----- exercise 10 -------
# Read line number 4 from the following file

lineCount = 0
fp = open('C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/lines.txt', 'r')
lines = fp.readlines()
print(lines[3])
