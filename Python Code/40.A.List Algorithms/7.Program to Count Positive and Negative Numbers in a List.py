'''
Program to Count Positive and Negative Numbers in a List

'''

# Python Program to Count Positive and Negative Numbers in a List

def count_Positive(NumList):
    Positive_count = 0
    for j in range(Number):
        if(NumList[j] >= 0):
            Positive_count = Positive_count + 1
    return Positive_count

def count_Negative(NumList):
    Negative_count = 0
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Negative_count = Negative_count + 1
    return Negative_count

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

Positive_cnt = count_Positive(NumList)
Negative_cnt = count_Negative(NumList)
print("\nTotal Number of Positive Numbers in this List =  ", Positive_cnt)
print("Total Number of Negative Numbers in this List = ", Negative_cnt)