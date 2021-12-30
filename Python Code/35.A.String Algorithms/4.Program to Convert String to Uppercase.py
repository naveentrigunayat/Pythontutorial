'''

Program to Convert String to Uppercase

'''



# Python Program to Convert String to Uppercase
 
string = input("Please Enter your Own String : ")

string1 = string.upper()
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)



# Python Program to Convert String to Uppercase
 
string = input("Please Enter your Own String : ")
string1 = ''

for i in range(len(string)):
    if(string[i] >= 'a' and string[i] <= 'z'):
        string1 = string1 + chr((ord(string[i]) - 32))
    else:
        string1 = string1 + string[i]
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)



