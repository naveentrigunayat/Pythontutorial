'''
Program to Find Set Length

'''


# Set Length

intSet = set()
number = int(input("Enter the Total Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set value = " %i))
    intSet.add(value)
    
print("Set Items = ", intSet)

intSetLength = len(intSet)
print("Set Length = ", intSetLength)