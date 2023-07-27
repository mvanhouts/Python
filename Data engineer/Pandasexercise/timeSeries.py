# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 10:31:04 2023

@author: mhouts
"""
import pandas as pd
import csv


data = '''\
timestamp,user_id,event_type,event_data
2023-06-26 10:30:15,12345,click,{"page": "homepage"}
2023-06-26 10:30:18,54321,click,{"page": "product", "product_id": "P001"}
2023-06-26 10:30:20,12345,purchase,{"product_id": "P002", "amount": 49.99}
'''

splitData = data.split('\n')

filename = 'data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in splitData:
        writer.writerow(row.split(','))
        
df = pd.read_csv('data.csv')

print(df)

