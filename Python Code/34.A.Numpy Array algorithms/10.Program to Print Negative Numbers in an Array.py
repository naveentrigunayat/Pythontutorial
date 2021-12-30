'''
Program to Print Negative Numbers in an Array

'''

# Print Negative in Array

import numpy as np

def printNegativeNumbers(negaArr):
    for i in negaArr:
        if (np.less(i, 0) == True):
            print(i, end = "  ")
    

negaArr = np.array([16, -99, -88, 0, -77, 44, -55, -2, 19])

print("**The Negative Numbers in this negaArr Array***")
printNegativeNumbers(negaArr)