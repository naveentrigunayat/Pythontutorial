'''

Program to Find Largest Number in an Array

'''


# Largest Array Item
import numpy as np
lgtarr = np.array([270, 199, 220, 195, 1200, 1750, 100])
print("Numeric Largest Numpy Array Items = ", lgtarr)

largest = lgtarr[0]

for i in range(1, len(lgtarr)-1) :
    if(largest < lgtarr[i]) :
        largest = lgtarr[i]
        larposition = i
        
print("The Largest Number in this Numpy Array   = ", largest)
print("The Index Position of the Largest Number = ", larposition)