'''

Program to find First Occurrence of a Character in a String

'''



# Python Program to check First Occurrence of a Character in a String

def first_Occurrence(char, string):
    for i in range(len(string)):
        if(string[i] == char):
            return i
    return -1

str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

flag =  first_Occurrence(ch, str1)
if(flag == -1):
    print("Sorry! We haven't found the Search Character in this string ")
else:
    print("The first Occurrence of ", ch, " is Found at Position " , flag + 1)