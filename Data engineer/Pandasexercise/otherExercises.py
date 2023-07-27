# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:17:17 2023

@author: mhouts
"""
#-------------------------------------------------------------------------------
#Exercise 1
#-------------------------------------------------------------------------------

import pandas as pd

def calculate_average_age(file_path):
    df = pd.read_csv(file_path)

    return df['Age'].sum() / df['Age'].count()

print(calculate_average_age('user_data.csv'))

#-------------------------------------------------------------------------------
#Exercise 2
#-------------------------------------------------------------------------------

import random

def generate_dates(num_dates):
    dates = []
    for x in range(num_dates):
        year = random.randint(2000,2023)
        month = random.randint(1,12)
        day = random.randint(1,28)
        date = f'{year:04d}-{month:02d}-{day:02d}'
        dates.append(date)
    return dates

def format_dates(x):
    reverseList = []
    
    for x in dateList:
        dayReverse = x[8:]
        monthReverse = x[5:7]
        yearReverse = x[:4]
        reverseList.append(dayReverse + '-' + monthReverse + '-' + yearReverse)
    return reverseList

dateList = generate_dates(10)

print(format_dates(dateList))
    
#alternative:

    
def format_dates2(x):
    reverseList = []
    
    for x in dateList:
        year, month, day = x.split('-')
        reverseList.append(f'{day}-{month}-{year}')
    return reverseList

print(format_dates2(dateList))




