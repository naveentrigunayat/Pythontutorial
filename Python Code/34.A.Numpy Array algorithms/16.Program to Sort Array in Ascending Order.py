'''
Program to Sort Array in Ascending Order

'''


# Sort Array Ascending

import numpy as np

def arrayReverse(orarr):
    length = len(orarr)

    for i in range(length):
        for j in range(i + 1, length):
            if (orarr[i] > orarr[j]):
                temp = orarr[i]
                orarr[i] = orarr[j]
                orarr[j] = temp

orarr = np.array([22, 17, 68, 55, 19, 99, 58, 77])
print("***Sorting Numpy Array in Ascending Order***")
print("Original Array           = ", orarr)

arrayReverse(orarr)
print("Array in Ascending Order = ", orarr)