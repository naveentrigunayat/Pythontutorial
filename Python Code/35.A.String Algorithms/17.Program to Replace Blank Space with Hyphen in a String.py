'''
Program to Replace Blank Space with Hyphen in a String

'''


# Python program to Replace Blank Space with Hyphen in a String
 
str1 = input("Please Enter your Own String : ")

str2 = ''

for i in range(len(str1)):
    if(str1[i] == ' '):
        str2 = str2 + '_'
    else:
        str2 = str2 + str1[i]
        
print("Modified String :  ", str2)