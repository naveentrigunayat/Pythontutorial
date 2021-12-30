'''
Program to Remove Even Numbers in a List

'''

# Remove Even index List Items

evenList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    evenList.append(listValue)

print("List Items = ", evenList)

oddList = list(filter(lambda x : (x % 2 != 0), evenList))    
print("List Items after removing even Items = ", oddList)