'''
Program to Toggle Characters Case in a String

'''


# Python Program to Toggle Characters Case in a String  swapcase() Function
 
string = input("Please Enter your Own String : ")

string1 = string.swapcase()
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)







# Python Program to Toggle Characters Case in a String using for loop
 
string = input("Please Enter your Own String : ")

string1 = ''

for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'): 
        string1 = string1 + chr((ord(string[i]) - 32)) 
    elif(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
    else:
        string1 = string1 + string[i]
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)