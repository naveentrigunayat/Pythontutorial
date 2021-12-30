'''

Program to Replace Characters in a String

'''


# Python program to Replace Characters in a String
 
str1 = input("Please Enter your Own String : ")
ch = input("Please Enter your Own Character : ")
newch = input("Please Enter the New Character : ")

str2 = ''
for i in range(len(str1)):
    if(str1[i] == ch):
        str2 = str2 + newch
    else:
        str2 = str2 + str1[i]

print("\nOriginal String :  ", str1)
print("Modified String :  ", str2)