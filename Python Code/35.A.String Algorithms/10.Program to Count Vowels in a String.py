'''

Program to Count Vowels in a String

'''



# Python Program to Count Vowels in a String

str1 = input("Please Enter Your Own String : ")

vowels = 0
str1.lower()

for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)