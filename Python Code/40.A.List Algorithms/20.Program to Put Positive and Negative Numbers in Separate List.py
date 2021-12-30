'''
Program to Put Positive and Negative Numbers in Separate List

'''

# Python Program to Put Positive and Negative Numbers in Separate List
def positive_numbers(NumList):
    Positive = []
    for j in range(Number):
        if(NumList[j] >= 0):
            Positive.append(NumList[j])
    print("Element in Positive List is : ", Positive)

def negative_numbers(NumList):
    Negative = []
    for j in range(Number):
        if(NumList[j] < 0):
            Negative.append(NumList[j])
    print("Element in Negative List is : ", Negative)
    
NumList = []
Positive = []
Negative = []
j = 0
Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

positive_numbers(NumList)
negative_numbers(NumList)