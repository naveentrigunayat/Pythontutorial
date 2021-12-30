'''
program to find ASCII Value of Total Characters in a String

'''


# Python program to find ASCII Values of Total Characters in a String
 
str1 = input("Please Enter your Own String : ")
 
for i in range(len(str1)):
    print("The ASCII Value of Character %c = %d" %(str1[i], ord(str1[i])))