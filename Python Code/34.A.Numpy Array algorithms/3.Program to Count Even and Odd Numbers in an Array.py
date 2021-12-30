'''

Program to Count Even and Odd Numbers in an Array

'''



# Count Even and Odd in Array using Function


import numpy as np
def CountEvenOddNumbers(evenOddArr):
    evenArrCount = 0
    oddArrCount = 0
    for i in evenOddArr:
        if (np.remainder(i, 2) == 0):
            evenArrCount = evenArrCount + 1
        else:
            oddArrCount = oddArrCount + 1

    return evenArrCount, oddArrCount

evenOddArr = np.array([11, 88, 15, 122, 140, 17, 10, 48, 35, 64])
even, odd = CountEvenOddNumbers(evenOddArr)
print("The Count of Even Numbers in evenOddArr Array = ", even)
print("The Count of Odd Numbers in evenOddArr Array  = ", odd)