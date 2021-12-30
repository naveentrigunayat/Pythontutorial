'''
 Program to Reverse String

'''


# Python Program to Reverse String  using Recursion

def StringReverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return StringReverse(str1[1:]) + str1[0]

string = input("Please enter your own String : ")

string2 = StringReverse(string)
print("\nThe Original String = ", string)
print("The Reversed String = ", string2)