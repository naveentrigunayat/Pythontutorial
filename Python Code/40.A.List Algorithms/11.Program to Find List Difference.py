'''
Program to Find List Difference

'''

# Difference Between two Lists
list1 = [1, 2, 6, 8, 11, 14]
list2 = [2, 3, 11, 9, 7, 14, 22]

print("First  List Items = ", list1)
print("Second List Items = ", list2)

listDifference = []

for val in list1 + list2:
    if val not in list1 or val not in list2:
        listDifference.append(val)

print("List Difference Result = ", listDifference)