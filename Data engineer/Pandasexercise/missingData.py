# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 14:56:17 2023

@author: mhouts
"""

import seaborn as sns
import pandas as pd

#------------------------------------------------------------------------------
#Exercise 1
#------------------------------------------------------------------------------
pd.set_option('display.max_rows', 1000)
df = pd.DataFrame(sns.load_dataset('titanic'))

print(df.isna().sum())

#------------------------------------------------------------------------------
#Exercise 2
#------------------------------------------------------------------------------

import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [6, np.nan, 8, np.nan, 10],
        'C': [11, 12, 13, np.nan, 15],
        'D': [np.nan, 22, 23, 24, 25]}

df = pd.DataFrame(data)

df['A'] = df['A'].fillna(df['A'].mean())

print(df)

#------------------------------------------------------------------------------
#Exercise 3
#------------------------------------------------------------------------------

import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [6, np.nan, 8, np.nan, 10],
        'C': [11, 12, 13, np.nan, 15],
        'D': [np.nan, 22, 23, 24, 25]}

df = pd.DataFrame(data)

df = df.dropna()

print(df)

#------------------------------------------------------------------------------
#Exercise 4
#------------------------------------------------------------------------------

import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [6, np.nan, 8, np.nan, 10],
        'C': [11, 12, 13, np.nan, 15],
        'D': [np.nan, 22, 23, 24, 25]}

df = pd.DataFrame(data)

df = df.fillna(method='ffill')

print(df)

