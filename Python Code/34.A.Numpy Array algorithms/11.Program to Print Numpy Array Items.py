'''
Program to Print Numpy Array Items

'''

# Print Array Items
import numpy as np
arr = np.array([12, 20, 50, 18, 33, 50, 99])

print("*** Numpy Array Items ***")
for i in range(len(arr)):
    print("Array Item at %d Position = %d" %(i, arr[i]))