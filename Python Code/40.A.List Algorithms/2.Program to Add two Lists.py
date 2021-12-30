'''
Program to Add two Lists

'''


# Python Program to Add two Lists
 
NumList1 = []
NumList2 = []
total = []

Number = int(input("Please enter the Total Number of List Elements: "))
print("Please enter the Items of a First and Second List   ")
for i in range(1, Number + 1):
    List1value = int(input("Please enter the %d Element of List1 : " %i))
    NumList1.append(List1value)

    List2value = int(input("Please enter the %d Element of List2 : " %i))
    NumList2.append(List2value)
    
for j in range(Number):
    total.append( NumList1[j] + NumList2[j])
 
print("\nThe total Sum of Two Lists =  ", total)