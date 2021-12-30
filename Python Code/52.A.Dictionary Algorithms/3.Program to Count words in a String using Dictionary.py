'''
Program to Count words in a String using Dictionary

'''


# Python Program to Count words in a String using Dictionary

string = input("Please enter any String : ")
words = []

words = string.split() # or string.lower().split()
myDict = {}
for key in words:
    myDict[key] = words.count(key)

print("Dictionary Items  :  ",  myDict)