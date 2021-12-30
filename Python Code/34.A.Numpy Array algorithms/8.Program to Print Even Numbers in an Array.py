'''
Program to Print Even Numbers in an Array

'''


# Print Even in Array
import numpy as np

def printEvenNumbers(evenArr):
    for i in evenArr:
        if (np.remainder(i, 2) == 0):
            print(i, end = "  ")
    

evenArr = np.array([1, 8, 5, 22, 14, 17, 10, 18, 35, 44])
print("**The List of Even Numbers in this evenArr Array***")
printEvenNumbers(evenArr)



