

'''

Program to Count Positive and Negative Numbers in an Array

'''





# Count Positive and Negative in Array

import numpy as np

posNegaArr = np.array([4, 25, -9, 8, -6, -7, 0, 11, -17, 6, -44, 89])
posArrCount = posArrCount1 = 0
negaArrCount = negaArrCount1 = 0

for i in posNegaArr:
    if (i >= 0):
        posArrCount = posArrCount + 1
    else:
        negaArrCount = negaArrCount + 1
        
print("The Count of Positive Numbers in evennegaArr Array = ", posArrCount)
print("The Count of Negative Numbers in evennegaArr Array  = ", negaArrCount)

print("\n=== Using greater_equal function===")
for i in posNegaArr:
    if (np.greater_equal(i, 0) == True):
        posArrCount1 = posArrCount1 + 1
    else:
        negaArrCount1 = negaArrCount1 + 1

print("The Count of Positive Numbers in evennegaArr Array = ", posArrCount1)
print("The Count of Negative Numbers in evennegaArr Array  = ", negaArrCount1)