'''

Program to Create Dictionary of Numbers 1 to n in (x, x*x) form

'''



# Python Program to Create Dictionary of Numbers 1 to n in (x, x*x) form

number = int(input("Please enter the Maximum Number : "))
myDict = {}

for x in range(1, number + 1):
    myDict[x] = x * x
    
print("\nDictionary = ", myDict)