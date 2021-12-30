'''
Program to Remove Duplicates from List

'''

# Remove Duplicates from List

dupList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    dupList.append(listValue)

print("List Items = ", dupList)

uniqList = []

for val in dupList:
    if val not in uniqList:
        uniqList.append(val)
   
print("List Items after removing Duplicates = ", uniqList)