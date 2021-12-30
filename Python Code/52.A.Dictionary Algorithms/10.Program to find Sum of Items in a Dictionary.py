'''

Program to find Sum of Items in a Dictionary

'''



# Python Program to find Sum of Items in a Dictionary

myDict = {'x': 250, 'y':500, 'z':410}
print("Dictionary: ", myDict)
total = 0

# Print Values using get
for i in myDict:
    total = total + myDict[i]
    
print("\nThe Total Sum of Values : ", total)