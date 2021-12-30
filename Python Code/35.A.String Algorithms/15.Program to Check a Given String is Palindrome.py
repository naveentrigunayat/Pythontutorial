'''
Program to Check a Given String is Palindrome

'''


# Python Program to Check a Given String is Palindrome or Not

def reverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return reverse(str1[1 : ]) + str1[0]
    
string = input("Please enter your own String : ")
str1 = reverse(string)
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")