'''
Program to Print Odd Numbers in a List

'''

# Python Program to Print Odd Numbers in a List

def odd_numbers(NumList):
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            print(NumList[j], end = '   ')

      
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nOdd Numbers in this List are : ")
odd_numbers(NumList)