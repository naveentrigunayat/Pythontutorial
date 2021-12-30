

'''

Program to Find Tuple Length

'''



# Tuple Length

intTuple = ()
number = int(input("Enter the Total Tuple Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d value = " %i))
    intTuple += (value,)
    
print("Tuple Items = ", intTuple)

inttupleLength = len(intTuple)
print("Tuple Length = ", inttupleLength)