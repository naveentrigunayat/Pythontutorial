'''
Program to find Sum of Elements in a List

'''


# Python Program to find Sum of all Elements in a List

def sum_of_list(NumList):
    total = 0
    for j in range(Number):
        total = total + NumList[j]
    return total


NumList = []
Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

total = sum_of_list(NumList)
print("\n The Sum of All Element in this List is : ", total)