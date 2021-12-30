'''
Program to Find Numpy Array Length

'''


# Array Length
import numpy as np

arrList = []
number = int(input("Enter the Total Array Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Array value = " %i))
    arrList.append(value)

intArr = np.array(arrList)
print("Integer Numpy Array Items = ", intArr)

intArrLength = len(intArr)
print("Integer Numpy Array Length = ", intArrLength)