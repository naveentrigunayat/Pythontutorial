
'''

Program to Find Smallest Item in a Tuple

'''



# Tuple Max Item

def tupleSmallest(smTuple):
    tupSmallest = smTuple[0]
    for i in smTuple:
        if(tupSmallest > i):
            tupSmallest = i
    return tupSmallest

smTuple = (19, 77, 13, 87, 33, 6, 17, 45, 66) 
print("Tuple Items = ", smTuple)

smt = tupleSmallest(smTuple)
print("Smallest Item in smTuple Tuple = ", smt)