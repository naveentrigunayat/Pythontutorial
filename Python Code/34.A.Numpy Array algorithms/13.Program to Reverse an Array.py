'''
Program to Reverse an Array

'''


# Reverse an Array

import numpy as np

def reverseArray(orgarr, number) :
    j = number - 1
    i = 0
    
    while(i < j):
        temp = orgarr[i]
        orgarr[i] = orgarr[j]
        orgarr[j] = temp
        i += 1
        j -= 1


arrList = []
number = int(input("Enter the Total Array Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Array value = " %i))
    arrList.append(value)

orgarr = np.array(arrList)
print("Original Numeric Numpy Array Items = ", orgarr)

reverseArray(orgarr, number) 
print("After Reversing Numeric Numpy Array = ", orgarr)