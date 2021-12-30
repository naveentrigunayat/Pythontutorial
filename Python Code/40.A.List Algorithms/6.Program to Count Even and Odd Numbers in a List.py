'''
Program to Count Even and Odd Numbers in a List

'''


# Python Program to Count Even and Odd Numbers in a List

def count_even(NumList):
    Even_count = 0
    for j in range(Number):
        if(NumList[j] % 2 == 0):
            Even_count = Even_count + 1
    return Even_count

def count_odd(NumList):
    Odd_count = 0
    for j in range(Number):
        if(NumList[j] % 2 != 0):
            Odd_count = Odd_count + 1
    return Odd_count

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

even_cnt = count_even(NumList)
odd_cnt = count_odd(NumList)
print("\nTotal Number of Even Numbers in this List =  ", even_cnt)
print("Total Number of Odd Numbers in this List = ", odd_cnt)