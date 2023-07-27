# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:17:17 2023

@author: mhouts
"""

import pandas as pd

df = pd.read_csv('mockdata.csv')

df = df.drop_duplicates()

df = df.dropna()

print(df)