# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:24:47 2023

@author: mhouts
"""

import numpy as np

medalsArray = np.array([[1, 39, 41, 33],
                        [2, 38, 32, 18],
                        [3, 27, 14, 17],
                        [4, 22, 21, 22],
                        [5, 20, 28, 23]])

for i in range(medalsArray.shape[1] + 1):
    print(np.sum(medalsArray[i,1:4]))
