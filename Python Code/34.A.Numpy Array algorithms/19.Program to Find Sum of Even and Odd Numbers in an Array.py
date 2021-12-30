'''
Program to Find Sum of Even and Odd Numbers in an Array

'''


# Sum of Even and Odd in Array

import numpy as np

def SumEvenOddNumbers(evenOddSumArr):
    evenArrSum = 0
    oddArrSum = 0
    for i in evenOddSumArr:
        if (np.remainder(i, 2) == 0):
            evenArrSum = evenArrSum + i
        else:
            oddArrSum = oddArrSum + i

    return evenArrSum, oddArrSum


evenOddSumArr = np.array([10, 20, 25, 55, 100, 85, 200])
evensum, oddsum = SumEvenOddNumbers(evenOddSumArr)

print("The Sum of Even Numbers in evenOddSumArr Array = ", evensum)
print("The Sum of Odd Numbers in evenOddSumArr Array  = ", oddsum)