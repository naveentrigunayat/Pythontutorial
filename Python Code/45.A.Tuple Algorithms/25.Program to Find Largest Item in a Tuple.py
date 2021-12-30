'''
Program to Find Largest Item in a Tuple

'''


# Tuple Max Item

def tupleLargest(mxTuple):
    tupLargest = mxTuple[0]
    for i in mxTuple:
        if(tupLargest < i):
            tupLargest = i
    return tupLargest

mxTuple = (19, 25, 77, 56, 89, 45, 55, 12) 
print("Tuple Items = ", mxTuple)

lar = tupleLargest(mxTuple)
print("Largest Item in mxTuple Tuple = ", lar)