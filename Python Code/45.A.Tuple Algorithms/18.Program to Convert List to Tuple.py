'''
Program to Convert List to Tuple

'''

# Convert List to Tuple

list1 = []

number = int(input("Enter the Total List Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d List value = " %i))
    list1.append(value)
    
print("List Items     = ", list1)
print("List Data Type = ", type(list1))

intTuple = tuple(list1)
print("\nTuple Items     = ", intTuple)
print("Tuple Data Type = ", type(intTuple))

intTuple1 = (*list1,)
print("\nTuple Items     = ", intTuple1)
print("Tuple Data Type = ", type(intTuple1))