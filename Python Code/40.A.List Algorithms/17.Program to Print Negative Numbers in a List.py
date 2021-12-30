'''
Program to Print Negative Numbers in a List

'''

# Python Program to Print Negative Numbers in a List

def negative_number(NumList):
    for j in range(Number):
        if(NumList[j] < 0):
            print(NumList[j], end = '   ')


NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nNegative Numbers in this List are : ")
negative_number(NumList)


