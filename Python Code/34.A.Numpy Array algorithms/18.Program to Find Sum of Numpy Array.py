'''
Program to Find Sum of Numpy Array

'''


# Sum Of Array Items

import numpy as np

sumArr = np.array([10, 30, 50, 70, 90, 120, 150])
total = 0
for num in sumArr:
    total = total + num

print("The Sum of Total Array Item = ", total)