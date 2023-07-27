# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:52:45 2023

@author: mhouts
"""

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active
sheet["A1"] = "First Number ->"
sheet["A2"] = "Second Number ->"
sheet["B1"] = 13
sheet["B2"] = 8
sheet["B3"] = "=B1 + B2"

workbook.save(filename="calculatorPython.xlsx")
