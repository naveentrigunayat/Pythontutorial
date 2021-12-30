'''
Program to Put Even and Odd Numbers in Separate List

'''

# Python Program to Put Even and Odd Numbers in Separate List

def even_numbers(NumList):
    Even = []
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            Even.append(NumList[j])

    print("Element in Even List is : ", Even)

def odd_numbers(NumList):
    Odd = []
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Odd.append(NumList[j])

    print("Element in Odd List is : ", Odd)
      
NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

even_numbers(NumList)
odd_numbers(NumList)