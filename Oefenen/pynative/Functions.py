# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 14:57:14 2023

@author: mhouts
"""

#----- exercise 1 -------
# Write a program to create a function that takes two arguments, name and age, and print their value.

def TwoArguments(name, age):
    print(name, age)
    
TwoArguments("Max", 31)

#----- exercise 2 -------
# Create a function with variable length of arguments

def func1(*args):
    for x in args:
        print(x)

func1(20, 40, 60)

func1(80, 100)

#----- exercise 3 -------
# Return multiple values from a function

def calculation(a, b):
    addition = a + b
    substraction = a - b
    return addition, substraction

res = calculation(40, 10)
print(res)

#----- exercise 4 -------
# Create a function with a default argument

def show_employee(name, salary = 9000):
    print("Name:",name, "Salary:",salary)
   
show_employee("Ben", 12000)
show_employee("Jessa")

#----- exercise 5 -------
# Create an inner function to calculate the addition in the following way

def outer_function(a, b):
    def inner_function(a, b):
        return a + b
    c = inner_function(a, b)
    return c + 5

outer_function(2, 1)

#----- exercise 6 -------
# Create a recursive function
def rec_function(x):
    if x == 0:
        return 0
    else:
        return x + rec_function(x - 1)
    rec_function()

total = rec_function(10)
print(total)

#----- exercise 7 -------
# Assign a different name to function and call it through the new name

def display_student(name, age):
    print(name, age)

show_student = display_student

show_student("Emma", 26)

#----- exercise 8 -------
# Generate a Python list of all the even numbers between 4 to 30
listNumber = []
for x in range(4, 30, 1):
    if x % 2 == 0:
        listNumber.append(x)
print(listNumber)

#or
print(list(range(4, 30, 2)))

#----- exercise 9 -------
# Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]

print(max(x))