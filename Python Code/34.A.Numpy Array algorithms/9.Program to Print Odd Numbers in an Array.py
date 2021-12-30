'''
Program to Print Odd Numbers in an Array

'''


# Print Odd in Array

import numpy as np

def printOddNumbers(evenArr):
    for i in oddArr:
        if (np.remainder(i, 2) != 0):
            print(i, end = "  ")
    

oddArr = np.array([1, 5, 22, 17, 10, 11, 35, 44, 98])

print("**The List of odd Numbers in this oddArr Array***")
printOddNumbers(oddArr)