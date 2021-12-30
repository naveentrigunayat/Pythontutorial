'''
List Multiplication Program

'''


# List Multiplication

def listMultiplication(multiList):
    listMulti = 1

    for num in multiList:
        listMulti = listMulti * num
    return listMulti

multiList = []

listNumber = int(input("Enter the Total List Items = "))
for i in range(1, listNumber + 1):
    listValue = int(input("Enter the %d List Item = " %i))
    multiList.append(listValue)

print("List Items = ", multiList)

listMultip = listMultiplication(multiList)

print("The Multiplication of all the List Items = ", listMultip)