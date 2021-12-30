'''

Program to Print Characters in a String

'''


# Python program to Print Characters in a String
 
str1 = input("Please Enter your Own String : ")
 
for i in range(len(str1)):
    print("The Character at %d Index Position = %c" %(i, str1[i]))