# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:18:26 2023

@author: mhouts
"""


#----- exercise 1 -------
# From the given dataset print the first and last five rows
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
print(df.head(5))
print(df.tail(5))

#----- exercise 2 -------
# Clean the dataset and update the CSV file
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df.replace("?","NaN")
df.to_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv",index = False)

#----- exercise 3 -------
# Find the most expensive car company name
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df = df[df['price']==df['price'].max()]
print(df)

#----- exercise 4 -------
# Print All Toyota Cars details
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df = df[df['company']=='toyota']
print(df)

#----- exercise 5 -------
# Count total cars per company
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df.groupby('company').size()

#----- exercise 6 -------
# Find each company’s Higesht price car
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df = df.groupby('company')['price'].max()
print(df)

#----- exercise 7 -------
# Find the average mileage of each car making company
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df = df.groupby('company')['average-mileage'].mean()
print(df)

#----- exercise 8 -------
# Sort all cars by Price column
import pandas as pd
df = pd.read_csv("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/pynative/Automobile_data.csv")
df = df.sort_values('price', ascending = False)
print(df)

#----- exercise 9 -------
#  Concatenate two data frames using the following conditions
import pandas as pd
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

df1 = pd.DataFrame(GermanCars)
df2 = pd.DataFrame(japaneseCars)

conDf = pd.concat([df1, df2], keys =["Germany", "Japanese"])

print(conDf)

#----- exercise 10 -------
#  Merge two data frames using the following condition
import pandas as pd
carPrice = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carHorsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}

df1 = pd.DataFrame(carPrice)
df2 = pd.DataFrame(carHorsepower)

mergeDf = pd.merge(df1,df2, on = 'Company', how = 'inner')
print(mergeDf)

