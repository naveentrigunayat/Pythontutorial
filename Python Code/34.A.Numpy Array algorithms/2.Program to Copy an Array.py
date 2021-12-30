'''
Program to Copy an Array

'''





# Program to Copy an Array using the For Loop range.

import numpy as np

cparr = np.array([12, 22, 35, 55, 47])
copyarr = np.empty(5)

for i in range(len(cparr)):
    copyarr[i] = cparr[i]

print("***Numpy Arrya Copy Result***")
print("Original Array = ", cparr)
print("Copied Array   = ", copyarr)