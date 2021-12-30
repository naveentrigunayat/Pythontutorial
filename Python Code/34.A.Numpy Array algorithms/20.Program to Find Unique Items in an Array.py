'''
Program to Find Unique Items in an Array

'''



# Print Unique Array Items

import numpy as np

orarr = np.array([10, 20, 10, 30, 40, 30, 70, 11, 19, 40])
print("Original Array      = ", orarr)

uniquearr = np.unique(orarr)
print("Unique Array Items  = ", uniquearr)