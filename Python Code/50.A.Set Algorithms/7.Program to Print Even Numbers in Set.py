'''
Program to Print Even Numbers in Set

'''


# Set Even Numbers

def setEvenNumbers(evset):
    for val in evSet:
        if(val % 2 == 0):
            print(val, end = "  ")


evSet = set()

number = int(input("Enter the Total Even Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    evSet.add(value)

print("Even Set Items = ", evSet)

print("\nThe Even Numbers in this evSet Set are:")
setEvenNumbers(evSet)


