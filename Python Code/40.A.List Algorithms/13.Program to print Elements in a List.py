'''
Program to print Elements in a List

'''


# Python Program to print Elements in a List 

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range(Number):
    print("The Element at index position %d = %d " %(i, NumList[i]))