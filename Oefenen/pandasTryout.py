# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:53:46 2023

@author: mhouts
"""

import pandas as pd
data = pd.read_excel("C:/Users/mhouts/OneDrive - Centric/Documents/Portfolio/Python/Oefenen/Pooh.xlsx")

sortedData = data.sort_values(by=["Poohsticks score", "Matches Played"], ascending=[False, False])


print(sortedData)