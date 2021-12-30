'''
Program to Remove Last Occurrence of a Character in a String

'''


# Python Program to Remove Last Occurrence of a Character in a String
 
def removeLastOccur(string, char):
    string2 = ''
    length = len(string)
    i = 0

    while(i < length):
        if(string[i] == char):
            string2 = string[0 : i] + string[i + 1 : length]
        i = i + 1
    return string2
 
str1 = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

print("Original String :  ", str1)
print("Final String :     ", removeLastOccur(str1, char))