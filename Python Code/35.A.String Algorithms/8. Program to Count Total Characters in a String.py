'''
 Program to Count Total Characters in a String

'''


# Python Program to Count Total Characters in a String
 
str1 = input("Please Enter your Own String : ")
total = 0
 
for i in range(len(str1)):
    total = total + 1
 
print("Total Number of Characters in this String = ", total)