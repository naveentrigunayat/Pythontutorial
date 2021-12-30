#                                 String Palindrome program in python


'''How this Python program will behave?
To check String is Palindrome or not?  This Program will take a String as an input. And after applying some logic it will return output as String is Palindrome or not.

For Example: 

Suppose if we give input a string “madam”. This is palindrome String then our program will print “Given string is palindrome”.

And if we give “abcd” then our program will give “Given String is not palindrome”.'''


string = input("Please give a String : ")
if(string == string[:: - 1]):
   print("Given String is a Palindrome")
else:
   print("Given String is not a Palindrome") 