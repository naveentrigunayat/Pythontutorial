'''
Program to Print Negative Numbers in Set

'''


# Tuple Negative Numbers

def setnegativeNumbers(negativeSet):
    for negVal in negativeSet:
        if(negVal < 0):
            print(negVal, end = "  ")


negativeSet = set()

number = int(input("Enter the Total Negative Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    negativeSet.add(value)

print("Negative Set Items = ", negativeSet)

print("\nThe Negative Numbers in this negativeSet Set are:")
setnegativeNumbers(negativeSet)