'''
Program to Count Even and Odd Numbers in Set

'''

# Count of Set Even and Odd Numbers

def CountOfSetEvenandOddNumbers(evodSet):
    sEvenCount = sOddCount = 0

    for eoVal in evodSet:
        if(eoVal % 2 == 0):
            sEvenCount = sEvenCount + 1
        else:
            sOddCount = sOddCount + 1
    return sEvenCount, sOddCount


evodSet = set()

number = int(input("Enter the Total Even Odd Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    evodSet.add(value)

print("Even and Odd Set Items = ", evodSet)

sECount, sOCount = CountOfSetEvenandOddNumbers(evodSet)
print("The Count of Even Numbers in evodSet = ", sECount)
print("The Count of Odd  Numbers in evodSet = ", sOCount)