'''
Program to Find Sum of Even and Odd Numbers in Set

'''

# Sum of Set Even and Odd Numbers

def sumOfSetEvenandOddNumbers(evenoddSet):
    sEvenSum = sOddSum = 0

    for eoVal in evenoddSet:
        if(eoVal % 2 == 0):
            sEvenSum = sEvenSum + eoVal
        else:
            sOddSum = sOddSum + eoVal
    return sEvenSum, sOddSum


evenoddSet = set()

number = int(input("Enter the Total Even Odd Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    evenoddSet.add(value)

print("Even and Odd Set Items = ", evenoddSet)

sESum, sOSum = sumOfSetEvenandOddNumbers(evenoddSet)
print("The Sum of Even Numbers in evenoddSet = ", sESum)
print("The Sum of Odd  Numbers in evenoddSet = ", sOSum)