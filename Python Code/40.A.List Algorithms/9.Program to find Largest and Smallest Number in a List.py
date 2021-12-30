'''
Program to find Largest and Smallest Number in a List

'''



# Python Program to find Largest and Smallest Number in a List 

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j
    if(largest < NumList[j]):
        largest = NumList[j]
        max_position = j

print("The Smallest Element in this List is : ", smallest)
print("The Index position of Smallest Element in this List is : ", min_position)
print("The Largest Element in this List is : ", largest)
print("The Index position of Largest Element in this List is : ", max_position)