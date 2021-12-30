'''
Program to Find Sum of Tuple Items

'''

# Tuple Sum

def sumOfTupleItems(numTuple):
    tupleSum = 0
    for tup in numTuple:
        tupleSum = tupleSum + tup
    return tupleSum

numTuple = (16, 31, 24, 98, 123, 78, 56, 67, 22)
print("Tuple Items = ", numTuple)

tSum = sumOfTupleItems(numTuple)
print("\nThe Sum of numTuple Tuple Items = ", tSum)