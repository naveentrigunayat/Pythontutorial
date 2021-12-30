'''
Program to Find Smallest Number in an Array

'''


# Smallest Array Item
import numpy as np
smtarr = np.array([14, 27, 99, 10, 50, 65, 18, 4, 195, 100])
print("Numeric Numpy Array Items = ", smtarr)

smallest = smtarr[0]
for i in range(1, len(smtarr)-1) :
    if(smallest > smtarr[i]) :
        smallest = smtarr[i]
        position = i
        
print("The Smallest Number in this Numpy Array   = ", smallest)
print("The Index Position of the Smallest Number = ", position)