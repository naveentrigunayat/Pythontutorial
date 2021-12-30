'''
Program to Map two lists into a Dictionary

'''


# Python Program to Map two lists into a Dictionary

keys = []
values = []
num = int(input("Please enter the Number of elements for this Dictionary : "))
print("Integer Values for Keys")
for i in range(0, num):
    x = int(input("Enter Key " + str(i + 1) + " = "))
    keys.append(x)
    
print("Integer Values for Values")
for i in range(0, num):
    x = int(input("Enter Value " + str(i + 1) + " = "))
    values.append(x)
    
myDict = dict(zip(keys, values))
print("Dictionary Items  :  ",  myDict)