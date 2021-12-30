'''
Program to Find Largest Set Item

'''

# Set Max Item

def SetLargest(mxSet, setLargest):
    for i in mxSet:
        if(setLargest < i):
            setLargest = i
    return setLargest

mxSet = set()

number = int(input("Enter the Total Set Items = "))
for i in range(1, number + 1):
    value = int(input("Enter the %d Set Item = " %i))
    mxSet.add(value)

setLargest = value
print("Set Items = ", mxSet)

lar = SetLargest(mxSet, setLargest)
print("Largest Item in mxSet Set = ", lar)