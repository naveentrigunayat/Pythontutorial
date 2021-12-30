'''
Program to access List Index and Values

'''

# Access List Index and Values

orgList = [22, 44, 66, 88, 122]

print("List Index and Values are")
for index, value in zip(range(len(orgList)), orgList):
    print("Index Number = ", index, " and Value = ", value)