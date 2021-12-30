
'''
Program to Reverse Tuple

'''


# Tuple Reverse

intRTuple = (10, 19, 29, 39, 55, 60, 90, 180)
print("Original Tuple Items = ", intRTuple)

revintTuple = ()

for i in reversed(range(len(intRTuple))):
    revintTuple += (intRTuple[i],)

print("After Reversing the Tuple = ", revintTuple)