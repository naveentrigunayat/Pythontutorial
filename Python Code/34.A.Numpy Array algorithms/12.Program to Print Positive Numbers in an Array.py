'''
Program to Print Positive Numbers in an Array

'''


# Print Positive in Array

import numpy as np

def printPositiveNumbers(posArr):
    for i in posArr:
        if (np.greater_equal(i, 0) == True):
            print(i, end = "  ")
    

posArr = np.array([1, -11, 0, 15, -9, -17, 22, -67, 55])

print("**The Positive Numbers in this posArr Array***")
printPositiveNumbers(posArr)