'''

Program to check if a Given key exists in a Dictionary

'''


 # Python Program to check if a Given key exists in a Dictionary

myDict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange', 'm': 'Mango'}
print("Dictionary : ", myDict)

key = input("Please enter the Key you want to search for: ")

# Check Whether the Given key exists in a Dictionary or Not
if key in myDict.keys():
    print("\nKey Exists in this Dictionary")
    print("Key = ", key, " and Value = ", myDict[key])
else:
    print("\nKey Does not Exists in this Dictionary")