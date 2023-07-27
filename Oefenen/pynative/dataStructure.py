# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:06:44 2023

@author: mhouts
"""

#----- exercise 1 -------
# Create a list by picking an odd-index items from the first list and even index items from the second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 =[]

for x in l1:
    if l1.index(x) % 2 != 0:
        l3.append(x)

for x in l2:
    if l2.index(x) % 2 == 0:
        l3.append(x)

print("Element at odd-index positions from list one: ", l3[0:3])
print("Element at even-index positions from list two: ", l3[3:])
print("full list: ", l3)

#alternative:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print("Element at odd-index positions from list one: ", l1[1::2])
print("Element at even-index positions from list two: ", l2[0::2])
print("full list: ", l1[1::2] + l2[0::2])

#----- exercise 2 -------
# Remove and add item in a list

list1 = [34, 54, 67, 89, 11, 43, 94]

removed = list1.pop(4)
print("List After removing element at index 4: ", list1)

list1.insert(2, removed)
print("List after Adding element at index 2: ", list1)

list1.append(removed)
print("List after Adding element at last: ", list1)

#----- exercise 3 -------
# Slice list into 3 equal chunks and reverse each chunk
l1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]

print("Chunk 1: ", l1[0:3])
print("Reverse: ", l1[2::-1])

print("Chunk 2: ", l1[3:6])
print("Reverse: ", l1[5:2:-1])

print("Chunk 3: ", l1[6:9])
print("Reverse: ", l1[8:5:-1])

#----- exercise 4 -------
# Count the occurrence of each element from a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
