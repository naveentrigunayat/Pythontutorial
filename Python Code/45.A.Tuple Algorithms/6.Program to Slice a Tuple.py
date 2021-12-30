'''
program to slice a tuple

'''


# Tuple Slice

numTuple = (11, 22, 33, 44, 55, 66, 77, 88, 99, 100)
print("Tuple Items = ", numTuple)

slice1 = numTuple[2:6]
print("Tuple Items from 3 to 5 = ", slice1)

slice2 = numTuple[3:]
print("Tuple Items from 4 to End = ", slice2)

slice3 = numTuple[:7]
print("Tuple Items from Start to 6 = ", slice3)

slice4 = numTuple[:]
print("Tuple Items from Start to End = ", slice4)