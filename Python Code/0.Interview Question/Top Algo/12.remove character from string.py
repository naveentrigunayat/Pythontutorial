'''In this tutorial you will learn writing program to remove a given character from a string in python.

 

For Example:

Input String: Quescol

Input Character : e

Output: Quscol (After removing ‘e’)'''



#                             Remove character from string in Python



str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch," ")) 