# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:43:32 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Create a 4X2 integer array and Prints its attributes
#------------------------------------------------------------------------------
import numpy as np

arr = np.array([[64392, 31655],[32579, 0],[49248, 462],[0 ,0]])

print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.itemsize)

#------------------------------------------------------------------------------
# Exercise 2 Create a 4X2 integer array and Prints its attributes
#------------------------------------------------------------------------------
import numpy as np
seq = np.arange(100, 200, 10)
arr = seq.reshape(5,2)
print(arr)

#------------------------------------------------------------------------------
# Exercise 3 Following is the provided numPy array. Return array of items by taking the third column from all rows
#------------------------------------------------------------------------------
import numpy as np
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])

print(sampleArray[:, 2])

#------------------------------------------------------------------------------
# Exercise 4 Return array of odd rows and even columns from below numpy array
#------------------------------------------------------------------------------
import numpy as np
sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

print(sampleArray[::2, 1::2])

#------------------------------------------------------------------------------
# Exercise 5 Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
#------------------------------------------------------------------------------
import numpy
arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

print(numpy.square(numpy.add(arrayOne, arrayTwo)))

#------------------------------------------------------------------------------
# Exercise 6 Split the array into four equal-sized sub-arrays
#------------------------------------------------------------------------------
import numpy as np
seq = np.arange(10,34,1)
arr = seq.reshape(8,3)
arr = np.split(arr, 4)
print(arr)

#------------------------------------------------------------------------------
# Exercise 7 Sort following NumPy array
#------------------------------------------------------------------------------
import numpy as np
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

print(sampleArray)

sortedRow = sampleArray[:,sampleArray[1,:].argsort()]
print(sortedRow)

sortedCol = sampleArray[sampleArray[:,1].argsort()]
print(sortedCol)

#------------------------------------------------------------------------------
# Exercise 8 Print max from axis 0 and min from axis 1 from the following 2-D array.
#------------------------------------------------------------------------------
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

maxArr = np.max(sampleArray,axis=0)
print(maxArr)

minArr = np.min(sampleArray,axis=1)
print(minArr)

#------------------------------------------------------------------------------
# Exercise 9 Delete the second column from a given array and insert the following new column in its place.
#------------------------------------------------------------------------------
import numpy

sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = numpy.array([[10,10,10]])

delArray = numpy.delete(sampleArray,1,axis=1)
print(delArray)

insertArray = numpy.insert(delArray,1,newColumn,axis=1)
print(insertArray)
