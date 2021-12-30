'''
 Program to Find Largest and Smallest Item in a Tuple

'''


# Tuple Max Item

def tupleLargest(lgsmTuple):
    tupLargest = lgsmTuple[0]
    for i in lgsmTuple:
        if(tupLargest < i):
            tupLargest = i
    return tupLargest

def tupleSmallest(lgsmTuple):
    tupSmallest = lgsmTuple[0]
    for i in lgsmTuple:
        if(tupSmallest > i):
            tupSmallest = i
    return tupSmallest

lgsmTuple = (33, 56, 22, 18, 2, 76, 45, 95, 77, 15) 
print("Tuple Items = ", lgsmTuple)

lar = tupleLargest(lgsmTuple)
print("Largest  Item in lgsmTuple Tuple = ", lar)

smt = tupleSmallest(lgsmTuple)
print("Smallest Item in lgsmTuple Tuple = ", smt)