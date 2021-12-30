'''
Program to Sort Array in Descending Order

'''


# Sort Array Descending

import numpy as np

def arrayDescending(dearr):
    for i in range(len(dearr)):
        for j in range(i + 1, len(dearr)):
            if (dearr[i] < dearr[j]):
                temp = dearr[i]
                dearr[i] = dearr[j]
                dearr[j] = temp
    
dearr = np.array([64, 36, 77, 55, 88, 95, 44, 91, 21])
print("***Sorting Numpy Array in Descending Order***")
print("Original Array             = ", dearr)

arrayDescending(dearr)
print("Array in Descending Order  = ", dearr)