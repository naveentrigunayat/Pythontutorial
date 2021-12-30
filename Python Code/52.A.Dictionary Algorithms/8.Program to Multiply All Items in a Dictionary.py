'''
Program to Multiply All Items in a Dictionary

'''


# Python Program to Multiply All Items in a Dictionary

myDict = {'x': 2, 'y':50, 'z':70}
print("Dictionary: ", myDict)

total = 1
# Multiply Items
for i in myDict.values():
    total = total * i
    
print("\nAfter Multiplying Items in this Dictionary: ", total)