'''
Program to Remove an Item from Tuple

'''

# Remove an Item from Tuple

numTuple = (2, 22, 33, 44, 5, 66, 77)
print("Tuple Items = ", numTuple)

numList = list(numTuple)
numList.remove(44)

numTuple1 = tuple(numList)
print("After Removing 3rd Tuple Item = ", numTuple1)