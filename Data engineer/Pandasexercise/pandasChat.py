# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 10:31:04 2023

@author: mhouts
"""
import seaborn as sns
import pandas as pd

#------------------------------------------------------------------------------
#Exercise 1
#------------------------------------------------------------------------------

df = pd.DataFrame(sns.load_dataset('iris'))

print(df.head(5))

#------------------------------------------------------------------------------
#Exercise 2
#------------------------------------------------------------------------------
import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel'],
        'Age': [25, 30, 28, 32, 27],
        'Country': ['USA', 'UK', 'Canada', 'USA', 'Australia'],
        'Salary': [50000, 70000, 65000, 80000, 55000]}

df = pd.DataFrame(data)

averageSalary = df['Salary'].sum() / df['Name'].nunique()

print(averageSalary)

#------------------------------------------------------------------------------
#Exercise 3
#------------------------------------------------------------------------------
import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel'],
        'Age': [25, 30, 28, 32, 27],
        'Country': ['USA', 'UK', 'Canada', 'USA', 'Australia'],
        'Salary': [50000, 70000, 65000, 80000, 55000]}

df = pd.DataFrame(data)

df = df.sort_values(by=['Age'], ascending=False)

print(df)

#------------------------------------------------------------------------------
#Exercise 4
#------------------------------------------------------------------------------

import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel'],
        'Age': [25, 30, 28, 32, 27],
        'Country': ['USA', 'UK', 'Canada', 'USA', 'Australia'],
        'Salary': [50000, 70000, 65000, 80000, 55000]}

df = pd.DataFrame(data)

df.insert(4, 'Bonus', df['Salary'] / 10)

print(df)

#------------------------------------------------------------------------------
#Exercise 5
#------------------------------------------------------------------------------

import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel'],
        'Age': [25, 30, 28, 32, 27],
        'Country': ['USA', 'UK', 'Canada', 'USA', 'Australia'],
        'Salary': [50000, 70000, 65000, 80000, 55000]}

df = pd.DataFrame(data)

onlyUsa = df.loc[df['Country'] == 'USA']

print(onlyUsa)

#------------------------------------------------------------------------------
#Exercise 6
#------------------------------------------------------------------------------

import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel'],
        'Age': [25, 30, 28, 32, 27],
        'Country': ['USA', 'UK', 'Canada', 'USA', 'Australia'],
        'Salary': [50000, 70000, 65000, 80000, 55000]}

df = pd.DataFrame(data)

maxSalary = df['Salary'].max()

print(maxSalary)

#------------------------------------------------------------------------------
#Exercise 7
#------------------------------------------------------------------------------

import pandas as pd

data = {'Name': ['John', 'Emma', 'Ryan', 'Emily', 'Daniel'],
        'Age': [25, 30, 28, 32, 27],
        'Country': ['USA', 'UK', 'Canada', 'USA', 'Australia'],
        'Salary': [50000, 70000, 65000, 80000, 55000]}

df = pd.DataFrame(data)

avgCountry = df.groupby(by='Country').mean()

print(avgCountry)
