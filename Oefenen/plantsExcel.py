# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:40:05 2023

@author: mhouts
"""

import openpyxl

plantsList = []

path = "C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/Plants.xlsx"

wb = openpyxl.load_workbook(path)

sheet = wb.active

for row in sheet.iter_rows():
    if row[0].value == None:
        break
    if row[7].value == "No":
         plantsList.append(row[0].value)
         
print(plantsList)
     
    