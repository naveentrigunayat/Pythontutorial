'''
Program to find Smallest Number in a List

'''


# Python Program to find Smallest Number in a List 

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

NumList.sort()
print("The Smallest Element in this List is : ", NumList[0])