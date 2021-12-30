
'''

Program to Perform Arithmetic Operations on Array

'''



# Array Arithemetic Operations
import numpy as np

optarr1 = np.array([10, 25, 35, 45, 50, 70, 90])
optarr2 = np.array([5, 40, 65, 7, 19, 22, 11])
addarr = np.empty(7)
subarr = np.empty(7)
multarr = np.empty(7)
modarr = np.empty(7)
divarr = np.empty(7)

for i in range(len(optarr1)):
    addarr[i] = optarr1[i] + optarr2[i]
    subarr[i] = optarr1[i] - optarr2[i]
    multarr[i] = optarr1[i] * optarr2[i]
    modarr[i] = optarr1[i] % optarr2[i]
    divarr[i] = optarr1[i] / optarr2[i]

print("**The Array Items After Perfroming Arithmetic Operations ***")
print("Array Addition = ", addarr)
print("Array Subtraction = ", subarr)
print("Array Multiplication =  ", multarr)
print("Array Modulus = ", modarr)
print("Array division = ", divarr)