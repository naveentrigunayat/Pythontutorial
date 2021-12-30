'''
Program to Iterate Set Items

'''

# Itearte Over Sets

set1 = {11, 33, 55, 77, 99, 111}

print("The Total Items in this Set = ")
for i, value in enumerate(set1):
    print(i, value)

set2 = set("Python")

print("\nThe Total Items in this Set = ")
for i, value in enumerate(set2):
     print(i, value)


print("\nThe Total Items in this Set = ")
for _, value in enumerate(set1):
    print(value, end = '  ')

print("\nThe Total Items in this Set = ")
for _, value in enumerate(set2):
     print(value, end = '  ')