'''

Program to Remove First Occurrence of a Character in a String

'''


# Python Program to Remove First Occurrence of a Character in a String
 
def removeFirstOccur(string, char):
    string2 = ''
    length = len(string)

    for i in range(length):
        if(string[i] == char):
            string2 = string[0:i] + string[i + 1:length]
            break
    return string2

str1 = input("Please enter your own String : ")
char = input("Please enter your own Character : ")

print("Original String :  ", str1)
print("Final String :     ", removeFirstOccur(str1, char))