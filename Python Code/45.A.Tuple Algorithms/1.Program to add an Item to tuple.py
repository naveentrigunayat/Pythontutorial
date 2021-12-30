'''
Program to add an Item to tuple

'''

# Add an Item to Tuple

intTuple = ()

number = int(input("Enter the Total Number of Tuple Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Tuple value = " %i))
    intTuple = intTuple + (value,)
    
print("Tuple Items = ", intTuple)