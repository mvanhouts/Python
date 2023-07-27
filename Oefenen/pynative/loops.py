# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:57:41 2023

@author: mhouts
"""

#----- exercise 1 -------
# Print First 10 natural numbers using while loop

for x in range(1, 11):
    print(x)
    x += 1
    
#----- exercise 2 -------
# Print the following pattern

listPrint = []

for x in range(1,6):
    listPrint.append(x)
    print(listPrint)
    x+=1
 
#----- exercise 3 -------
# Calculate the sum of all numbers from 1 to a given number
j = 0

nbInput = int(input("give me a number"))
for x in range(1,nbInput+1,1):
    j += x
    
print(j)

#----- exercise 4 -------
# Write a program to print multiplication table of a given number
nbInput = int(input("Number?"))
y = nbInput
for x in range(10):
    print(y)
    y +=nbInput
    
#----- exercise 5 -------
# Display numbers from a list using loop

nbList = [12, 75, 150, 180, 145, 525, 50]
for x in nbList:
    if x > 500:
        break
    else:
        if x <= 150 and x % 5 == 0:
            print(x)

#----- exercise 6 -------
# Count the total number of digits in a number

x = 7589365777987897
counter = 0

while x != 0:
    x = x // 10
    counter = counter + 1
print(counter)

#----- exercise 7 -------
# Print the following pattern
number = 5

for x in range(0, number + 1):
    for y in range(number - x, 0, -1):
        print(y, end=' ')
    print()

#----- exercise 8 -------
# Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
list1.reverse()

for x in list1:
    print(x)

#----- exercise 9 -------
# Display numbers from -10 to -1 using for loop
for x in range(-10,0, 1):
    print(x)
   
#----- exercise 10 -------
# Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)  
else:
    print('Done')

#----- exercise 11 -------
# Write a program to display all prime numbers within a range
# range
start = 25
end = 50

for x in range(start, end + 1):
    if x > 1:
        for y in range(2, x):
            if x % y == 0:
                break
    else:
        print(x)
        
#----- exercise 12 -------
# Display Fibonacci series up to 10 terms        
fibList = []
fibList.append(0)
for x in range(0,9,1):
    if x == 0:
        fibList.append(1)
    else:
        fibList.append(int(fibList[x]) + int(fibList[x - 1]))
print(fibList)
    