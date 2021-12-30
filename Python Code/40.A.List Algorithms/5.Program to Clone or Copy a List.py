'''
Program to Clone or Copy a List

'''

orgList = [25, 35, 45, 55, 65, 75, 85]
print("Original List Items = ", orgList)

newList = []

for lVal in orgList:
    newList.append(lVal)
print("New List Items      = ", newList)

newList2 = []

for i in range(len(orgList)):
    newList2.append(orgList[i])
print("New List Items      = ", newList2)