'''
Find Max and Min Number in Python List

'''

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))