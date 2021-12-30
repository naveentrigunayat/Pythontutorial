'''
Program to Find Second Largest in an Array

'''

# Second Largest Array Item

import numpy as np

secLarr = np.array([15, 22, 75, 99, 35, 70, 120, 60])
print("Array Items = ", secLarr)

first = second = min(secLarr)

for i in range(len(secLarr)):
    if (secLarr[i] > first):
        second = first
        first = secLarr[i]
    elif(secLarr[i] > second and secLarr[i] < first):
        second = secLarr[i]

print("The Largest Item in this Array = ", first)
print("The Second Largest Item in this Array = ", second)