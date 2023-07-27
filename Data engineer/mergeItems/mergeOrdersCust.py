# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 13:11:03 2023

@author: mhouts
"""

#Your task is to merge the two datasets based on the CustomerID column and create a consolidated output file with the following columns:

#    CustomerID
#    Name
#    Age
#    City
#    OrderID
#    OrderDate
#    Product
#    Quantity

import pandas as pd

try: #read the first csv
    dfCustomers = pd.read_csv("customers.csv")
    
except FileNotFoundError:
    print("File not found")
    raise 
    
try: #read the second csv
    dfOrders = pd.read_csv("orders.csv")
    
except FileNotFoundError:
    print("File not found")
    raise 

try: #merge the two dataframes
    mergeFrame = pd.merge(dfCustomers, dfOrders, on='CustomerID')
    
except:
    raise 

try: #export the results to a new csv
    mergeFrame.to_csv('mergedItems.csv', index=False)

except:
    raise