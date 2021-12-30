'''
program to Remove Odd Characters in a String

'''


# Python program to Remove Odd Characters in a String

def RemoveOddCharString(str1):
    str2 = ''

    for i in range(1, len(str1) + 1):
        if(i % 2 == 0):
            str2 = str2 + str1[i - 1]
    return str2

string = input("Please Enter your Own String : ")       
print("Original String :  ", string)
print("Final String    :  ", RemoveOddCharString(string))