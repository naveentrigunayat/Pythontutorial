'''
Program to Find Smallest Set Item

'''



# Set Min Item

def SetSmallest(smtSet, setSmallest):
    for i in smtSet:
        if(setSmallest > i):
            setSmallest = i
    return setSmallest

smtSet = set()

number = int(input("Enter the Total Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    smtSet.add(value)

setSmallest = value
print("Set Items = ", smtSet)

lar = SetSmallest(smtSet, setSmallest)
print("Smallest Item in smtSet Set = ", lar)