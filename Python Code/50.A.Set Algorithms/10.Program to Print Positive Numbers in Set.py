'''
Program to Print Positive Numbers in Set

'''


# Set Positive Numbers

def setPositiveNumbers(positiveSet):
    for posVal in positiveSet:
        if(posVal >= 0):
            print(posVal, end = "  ")


positiveSet = set()

number = int(input("Enter the Total Positive Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    positiveSet.add(value)

print("Positive Set Items = ", positiveSet)

print("\nThe Positive Numbers in this positiveSet Set are:")
setPositiveNumbers(positiveSet)



