'''
Program to Count Positive and Negative Numbers in Set

'''


# Count of Set Positive and Negative Numbers

def CountOfSetPositiveandNegativeNumbers(pongtSet):
    sPositiveCount = sNegativeCount = 0

    for eoVal in pongtSet:
        if(eoVal >= 0):
            sPositiveCount = sPositiveCount + 1
        else:
            sNegativeCount = sNegativeCount + 1
    return sPositiveCount, sNegativeCount


pongtSet = set()

number = int(input("Enter the Total Positive Negative Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    pongtSet.add(value)

print("Positive and Negative Set Items = ", pongtSet)

sECount, sOCount = CountOfSetPositiveandNegativeNumbers(pongtSet)
print("The Count of Positive Numbers in pongtSet = ", sECount)
print("The Count of Negative  Numbers in pongtSet = ", sOCount)