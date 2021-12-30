'''
Program to Find Minimum and Maximum Value in an Array

'''

# Smallest Array Item

import numpy as np

smtlgtarr = np.array([99, 120, 625, 150, 9, 428, 716, 190])
print("Numpy Array Items = ", smtlgtarr)

smallest = smtlgtarr[0]
largest = smtlgtarr[0]

for i in range(1, len(smtlgtarr) - 1) :
    if(largest < smtlgtarr[i]) :
        largest = smtlgtarr[i]
        larposition = i
    if(smallest > smtlgtarr[i]) :
        smallest = smtlgtarr[i]
        smtposition = i
        
print("The Smallest Number in this Numpy Array   = ", smallest)
print("The Index Position of the Smallest Number = ", smtposition)
print("The Largest Number in this Numpy Array    = ", largest)
print("The Index Position of the Largest Number  = ", larposition)