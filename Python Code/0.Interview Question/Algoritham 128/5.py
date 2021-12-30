'''Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''


#Solution: 


class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter the String :")

    def printString(self): 
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()



'''
Program Explanation
1. A class called print1 is created and the __init__() method is used to initialize the value of the string to “”.
3. The first method, get, takes the value of the string from the user.
3. The second string, put, is used to print the value of the string.
5. An object for the class called obj is created.
6. Using the object, the methods get() and put() is printed.
7. The value of the string is printed.

'''