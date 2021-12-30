'''
Program to Print Odd Numbers in Set

'''


# Tuple Odd Numbers

def setOddNumbers(oddSet):
    for odval in oddSet:
        if(odval % 2 != 0):
            print(odval, end = "  ")


oddSet = set()

number = int(input("Enter the Total Odd Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    oddSet.add(value)

print("Odd Set Items = ", oddSet)

print("\nThe Odd Numbers in this oddSet Set are:")
setOddNumbers(oddSet)