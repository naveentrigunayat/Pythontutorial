'''
Program to Add Key-Value Pair to a Dictionary

'''


# Python Program to Add Key-Value Pair to a Dictionary

key = input("Please enter the Key : ")
value = input("Please enter the Value : ")

myDict = {}

# Add Key-Value Pair to a Dictionary in Python
myDict.update({key:value})
print("\nUpdated Dictionary = ", myDict)